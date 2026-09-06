"""
# feynrules.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json
import os
import re
import shutil
import signal
import subprocess
import threading
import time
from pathlib import Path
from typing import Optional

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField

SCHEMA_VERSION = "tool-1.0"

def _utc_now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

# ====================================================================== #
# =================== FeynRules model \to UFO tool ===================== #
# ====================================================================== #

class FeynRulesToUFOTool(BaseTool):
    """
    Generate a UFO model directory from a FeynRules .fr model file by calling Mathematica's `wolframscript`.

    Inputs (runtime):
      - model_path: path to the FeynRules model file (.fr). Can be absolute or relative to base_directory.
      - output_dir: output directory where the UFO will be written. Relative to base_directory is recommended.
      - feynrules_path: optional path to the FeynRules installation root (directory that contains "FeynRules.m" and "Models/").
                        If omitted, the tool uses the environment variable FR_PATH, if set.
      - wolframscript_path: command or absolute path to the preferred wolframscript binary. Defaults to "wolframscript".
                           Use this to select a specific Mathematica version, e.g. "/Applications/Mathematica 13.3.app/Contents/MacOS/wolframscript".
      - log_dir: optional directory to store stdout/stderr logs. Defaults to {output_dir}/_logs.
      - timeout_sec: optional wall-clock limit for the Mathematica run. Defaults to 3600 seconds.
      - stall_timeout_sec: optional inactivity limit in seconds for known sextet/high-dimension
                           compile patterns. Used only when the model file contains sextet/high-dim
                           markers. Defaults to 600 seconds.

    Returns:
      JSON summary including paths, logs, and file listing of the generated UFO.
    """

    # --------------------------- Runtime fields --------------------------- #
    model_path: str = RuntimeField(default=None, description="Path to FeynRules .fr model file")
    output_dir: str = RuntimeField(default="UFO_Output", description="Directory for UFO output")
    log_dir: Optional[str] = RuntimeField(default=None, description="Directory to store logs")
    timeout_sec: Optional[int] = RuntimeField(default=3600, description="Timeout in seconds for Mathematica run")
    stall_timeout_sec: Optional[int] = RuntimeField(default=600, description="Inactivity timeout for sextet/high-dim compile detection")
    # ---------------------------------------------------------------------- #

    # ---------------------------- State fields ---------------------------- #
    feynrules_path: str = StateField(description="Path to FeynRules installation root")
    wolframscript_path: str = StateField(description="Command/path to wolframscript")
    base_directory: str = StateField(description="Base working directory for relative paths")
    # ---------------------------------------------------------------------- #

    def _abs_path(self, maybe_rel: Optional[str]) -> Optional[str]:
        """Convert a possibly relative path to an absolute path based on base_directory."""
        if maybe_rel is None:
            return None
        p = Path(maybe_rel)
        if not p.is_absolute():
            p = Path(self.base_directory) / p
        return str(p.resolve())

    def _ensure_dir(self, path: str) -> None:
        """Create directory if it doesn't exist."""
        Path(path).mkdir(parents=True, exist_ok=True)

    def _resolve_wolframscript_command(self) -> str:
        """Pick a usable wolframscript command; prefer the real binary when present."""
        configured = (self.wolframscript_path or "").strip() or "wolframscript"
        placeholders = {"/path/to/wolframscript", "REPLACE_WITH_WOLFRAMSCRIPT_PATH"}

        if configured not in placeholders:
            if os.path.isabs(configured):
                if os.path.isfile(configured) and os.access(configured, os.X_OK):
                    return configured
            else:
                resolved = shutil.which(configured)
                if resolved:
                    return resolved

        fallback = shutil.which("wolframscript")
        if fallback:
            return fallback
        return configured

    def _model_has_sextet_or_high_dim_marker(self, model_path: str) -> tuple[bool, list[str]]:
        """Heuristic marker scan for sextet/high-dimension models that often hang."""
        model_file = Path(model_path)
        if not model_file.exists():
            return False, []

        try:
            text = model_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return False, []

        markers: list[str] = []
        if re.search(r"\bSextet\b", text, flags=re.IGNORECASE):
            markers.append("token:Sextet")
        if re.search(r"\bS\[\s*368\s*\]", text):
            markers.append("class-index:S[368]")
        if re.search(r"AddGaugeRepresentation\[[^\]]*SU3C[^\]]*(Sextet|,\s*6\b)", text, flags=re.IGNORECASE):
            markers.append("gauge-rep:SU3C-sextet")

        for match in re.finditer(r"(?:ColorDim|ColourDim)\s*->\s*(\d+)", text):
            dim = int(match.group(1))
            if dim >= 6:
                markers.append(f"color-dim:{dim}")

        return bool(markers), sorted(set(markers))

    def _terminate_process_group(self, proc: subprocess.Popen, grace_sec: float = 3.0) -> None:
        """Terminate process and child process group, then hard-kill if needed."""
        if proc.poll() is not None:
            return

        used_group_signal = False
        if os.name != "nt":
            try:
                os.killpg(proc.pid, signal.SIGTERM)
                used_group_signal = True
            except (ProcessLookupError, PermissionError):
                pass

        if not used_group_signal:
            try:
                proc.terminate()
            except ProcessLookupError:
                return

        try:
            proc.wait(timeout=grace_sec)
            return
        except subprocess.TimeoutExpired:
            pass

        if os.name != "nt":
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                pass
        try:
            proc.kill()
        except ProcessLookupError:
            return
        try:
            proc.wait(timeout=2.0)
        except subprocess.TimeoutExpired:
            return

    def _structured_failure(
        self,
        *,
        code: str,
        reason: str,
        model_path: str,
        output_dir: str,
        selected_wolframscript: str,
        stdout_path: str,
        stderr_path: str,
        elapsed_sec: float,
        timeout_sec: Optional[int] = None,
        stall_timeout_sec: Optional[int] = None,
        markers: Optional[list[str]] = None,
    ) -> str:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "ok": False,
            "created_at_utc": _utc_now_iso(),
            "model_path": model_path,
            "output_dir": output_dir,
            "wolframscript_path": selected_wolframscript,
            "logs": {"stdout": stdout_path, "stderr": stderr_path},
            "error": {
                "code": code,
                "reason": reason,
                "elapsed_sec": round(elapsed_sec, 3),
            },
        }
        if timeout_sec is not None:
            payload["error"]["timeout_sec"] = timeout_sec
        if stall_timeout_sec is not None:
            payload["error"]["stall_timeout_sec"] = stall_timeout_sec
        if markers:
            payload["error"]["model_markers"] = markers
        return json.dumps(payload, indent=2)

    def _run(self) -> str:
        """Run the FeynRules to UFO conversion using wolframscript."""
        if not self.model_path:
            return self.format_error(error="Missing Parameter", reason="model_path is required")
        if not self.output_dir:
            return self.format_error(error="Missing Parameter", reason="output_dir is required")

        abs_model = self._abs_path(self.model_path)
        abs_out = self._abs_path(self.output_dir)
        abs_fr = self._abs_path(self.feynrules_path) if self.feynrules_path else None
        self._ensure_dir(abs_out)
        selected_wolframscript = self._resolve_wolframscript_command()

        env = os.environ.copy()
        if abs_fr:
            env["FEYNRULES_PATH"] = abs_fr

        log_dir = self._abs_path(self.log_dir) if self.log_dir else str(Path(abs_out) / "_logs")
        self._ensure_dir(log_dir)
        stdout_path = str(Path(log_dir) / "wolframscript_stdout.log")
        stderr_path = str(Path(log_dir) / "wolframscript_stderr.log")

        # Assume .wl script is colocated with this file
        driver = Path(__file__).parent / "UFO_generator.wl"
        if not driver.exists():
            return self.format_error(error="Missing Script", reason=f"{driver} not found")

        # Build command
        cmd = [
            selected_wolframscript, "-f", str(driver),
            f"ModelPath={abs_model}",
            f"FeynRulesPath={abs_fr or ''}",
            f"OutputDir={abs_out}",
        ]
        try:
            timeout_sec = int(self.timeout_sec) if self.timeout_sec is not None else 3600
        except (TypeError, ValueError):
            return self.format_error(error="Invalid Parameter", reason=f"timeout_sec must be an integer, got {self.timeout_sec!r}")
        if timeout_sec <= 0:
            return self.format_error(error="Invalid Parameter", reason="timeout_sec must be > 0")

        stall_timeout_sec: Optional[int] = None
        if self.stall_timeout_sec is not None:
            try:
                parsed_stall = int(self.stall_timeout_sec)
            except (TypeError, ValueError):
                return self.format_error(error="Invalid Parameter", reason=f"stall_timeout_sec must be an integer, got {self.stall_timeout_sec!r}")
            if parsed_stall > 0:
                stall_timeout_sec = parsed_stall

        sextet_guard_active, model_markers = self._model_has_sextet_or_high_dim_marker(abs_model)

        stdout_chunks: list[str] = []
        stderr_chunks: list[str] = []
        last_output_lock = threading.Lock()
        start_monotonic = time.monotonic()
        last_output_monotonic = start_monotonic

        def _reader(stream, sink: list[str]) -> None:
            nonlocal last_output_monotonic
            if stream is None:
                return
            try:
                for line in iter(stream.readline, ""):
                    sink.append(line)
                    with last_output_lock:
                        last_output_monotonic = time.monotonic()
            finally:
                stream.close()

        popen_kwargs = dict(
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.base_directory,
            env=env,
            text=True,
            bufsize=1,
        )
        if os.name != "nt":
            popen_kwargs["preexec_fn"] = os.setsid

        try:
            proc = subprocess.Popen(cmd, **popen_kwargs)
        except FileNotFoundError:
            return self.format_error(error="Executable Not Found", reason=f"wolframscript_path not found: {selected_wolframscript}")

        stdout_thread = threading.Thread(target=_reader, args=(proc.stdout, stdout_chunks), daemon=True)
        stderr_thread = threading.Thread(target=_reader, args=(proc.stderr, stderr_chunks), daemon=True)
        stdout_thread.start()
        stderr_thread.start()

        watchdog_hit = False
        sextet_stall_hit = False

        while proc.poll() is None:
            now = time.monotonic()
            elapsed = now - start_monotonic
            if elapsed > timeout_sec:
                watchdog_hit = True
                self._terminate_process_group(proc)
                break
            if sextet_guard_active and stall_timeout_sec is not None:
                with last_output_lock:
                    idle_for = now - last_output_monotonic
                if idle_for > stall_timeout_sec:
                    sextet_stall_hit = True
                    self._terminate_process_group(proc)
                    break
            time.sleep(0.2)

        try:
            proc.wait(timeout=5.0)
        except subprocess.TimeoutExpired:
            self._terminate_process_group(proc)
        stdout_thread.join(timeout=1.0)
        stderr_thread.join(timeout=1.0)

        stdout_text = "".join(stdout_chunks)
        stderr_text = "".join(stderr_chunks)
        Path(stdout_path).write_text(stdout_text, encoding="utf-8")
        Path(stderr_path).write_text(stderr_text, encoding="utf-8")
        elapsed_total = time.monotonic() - start_monotonic

        if watchdog_hit:
            return self._structured_failure(
                code="compile_timeout",
                reason=f"wolframscript exceeded wall-clock timeout ({timeout_sec}s)",
                model_path=abs_model,
                output_dir=abs_out,
                selected_wolframscript=selected_wolframscript,
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                elapsed_sec=elapsed_total,
                timeout_sec=timeout_sec,
                stall_timeout_sec=stall_timeout_sec,
                markers=model_markers if sextet_guard_active else None,
            )

        if sextet_stall_hit:
            return self._structured_failure(
                code="sextet_stall_detected",
                reason=(
                    "compile output stalled for sextet/high-dimension model; "
                    "terminated early"
                ),
                model_path=abs_model,
                output_dir=abs_out,
                selected_wolframscript=selected_wolframscript,
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                elapsed_sec=elapsed_total,
                timeout_sec=timeout_sec,
                stall_timeout_sec=stall_timeout_sec,
                markers=model_markers,
            )

        proc_stderr = stderr_text

        ok = proc.returncode == 0
        files_created = []
        if ok and Path(abs_out).exists():
            files_created = sorted(p.name for p in Path(abs_out).iterdir())

        summary = {
            "schema_version": SCHEMA_VERSION,
            "ok": ok,
            "created_at_utc": _utc_now_iso(),
            "model_path": abs_model,
            "output_dir": abs_out,
            "wolframscript_path": selected_wolframscript,
            "feynrules_path": abs_fr,
            "logs": {"stdout": stdout_path, "stderr": stderr_path},
            "files_created": files_created,
            "watchdog": {
                "timeout_sec": timeout_sec,
                "stall_timeout_sec": stall_timeout_sec,
                "sextet_stall_guard_active": sextet_guard_active,
                "model_markers": model_markers,
            },
        }

        if not ok:
            hint = None
            for line in (proc_stderr or "").splitlines()[-20:]:
                if "Error" in line or "LoadModel" in line or "WriteUFO" in line:
                    hint = line.strip()
                    break
            return self.format_error(error="UFO Generation Failed", reason=hint or "wolframscript returned non-zero exit status")

        return json.dumps(summary, indent=2)