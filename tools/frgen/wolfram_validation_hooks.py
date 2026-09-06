"""Wolfram-gated validation hooks for generated FeynRules models."""

from __future__ import annotations

import datetime
import json
import os
import shutil
import signal
import subprocess
import tempfile
import threading
import time
from pathlib import Path
from typing import Optional

from .frmodel import FeynRulesModel

SCHEMA_VERSION = "wolfram-validation-1.0"
JSON_MARKER = "HEPTAPOD_WL_JSON:"

CHECK_KINETIC_NORM = "kinetic_term_normalisation"
CHECK_MASS_SPECTRUM = "mass_spectrum"
CHECK_HERMITICITY = "hermiticity"
CHECK_NUMERIC_COUPLING = "numeric_coupling_probe_efflrsm_zr"

ALL_CHECKS = (
    CHECK_KINETIC_NORM,
    CHECK_MASS_SPECTRUM,
    CHECK_HERMITICITY,
    CHECK_NUMERIC_COUPLING,
)


def _utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _resolve_wolframscript_command(configured_path: Optional[str]) -> str:
    configured = (configured_path or "").strip() or "wolframscript"
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


def _command_exists(command: str) -> bool:
    if os.path.isabs(command):
        return os.path.isfile(command) and os.access(command, os.X_OK)
    return shutil.which(command) is not None


def _terminate_process_group(proc: subprocess.Popen, grace_sec: float = 3.0) -> None:
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


def _run_with_watchdog(
    cmd: list[str],
    *,
    cwd: str,
    timeout_sec: int,
    stall_timeout_sec: int,
    env: Optional[dict[str, str]] = None,
) -> dict[str, object]:
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
        cwd=cwd,
        env=env or os.environ.copy(),
        text=True,
        bufsize=1,
    )
    if os.name != "nt":
        popen_kwargs["preexec_fn"] = os.setsid

    proc = subprocess.Popen(cmd, **popen_kwargs)
    stdout_thread = threading.Thread(target=_reader, args=(proc.stdout, stdout_chunks), daemon=True)
    stderr_thread = threading.Thread(target=_reader, args=(proc.stderr, stderr_chunks), daemon=True)
    stdout_thread.start()
    stderr_thread.start()

    timeout_hit = False
    stall_hit = False

    while proc.poll() is None:
        now = time.monotonic()
        elapsed = now - start_monotonic
        if elapsed > timeout_sec:
            timeout_hit = True
            _terminate_process_group(proc)
            break
        if stall_timeout_sec > 0:
            with last_output_lock:
                idle_for = now - last_output_monotonic
            if idle_for > stall_timeout_sec:
                stall_hit = True
                _terminate_process_group(proc)
                break
        time.sleep(0.2)

    try:
        proc.wait(timeout=5.0)
    except subprocess.TimeoutExpired:
        _terminate_process_group(proc)

    stdout_thread.join(timeout=1.0)
    stderr_thread.join(timeout=1.0)
    elapsed_total = time.monotonic() - start_monotonic

    return {
        "returncode": proc.returncode,
        "stdout": "".join(stdout_chunks),
        "stderr": "".join(stderr_chunks),
        "elapsed_sec": round(elapsed_total, 3),
        "timeout_hit": timeout_hit,
        "stall_hit": stall_hit,
    }


def _smoke_check_wolframscript(wolframscript_command: str, *, cwd: str) -> tuple[bool, str]:
    smoke = _run_with_watchdog(
        [wolframscript_command, "-code", "Print[2+2]"],
        cwd=cwd,
        timeout_sec=20,
        stall_timeout_sec=20,
    )
    if smoke["timeout_hit"] or smoke["stall_hit"]:
        return False, "wolframscript probe timed out"
    if int(smoke["returncode"] or 0) != 0:
        stderr_tail = str(smoke["stderr"]).strip().splitlines()[-1:] or [""]
        reason = stderr_tail[0] or "non-zero exit status"
        return False, f"wolframscript probe failed: {reason}"
    return True, "wolframscript probe succeeded"


def _skip_report(*, wolframscript_path: str, reason: str) -> dict[str, object]:
    checks = [
        {"name": name, "status": "skipped", "passed": None, "detail": reason}
        for name in ALL_CHECKS
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "skipped",
        "created_at_utc": _utc_now_iso(),
        "available": False,
        "wolframscript_path": wolframscript_path,
        "reason": reason,
        "checks": checks,
    }


def _error_report(
    *,
    wolframscript_path: str,
    reason: str,
    run_result: Optional[dict[str, object]] = None,
) -> dict[str, object]:
    report = {
        "schema_version": SCHEMA_VERSION,
        "status": "error",
        "created_at_utc": _utc_now_iso(),
        "available": True,
        "wolframscript_path": wolframscript_path,
        "reason": reason,
        "checks": [
            {"name": name, "status": "skipped", "passed": None, "detail": reason}
            for name in ALL_CHECKS
        ],
    }
    if run_result is not None:
        report["process"] = {
            "returncode": run_result.get("returncode"),
            "elapsed_sec": run_result.get("elapsed_sec"),
            "timeout_hit": run_result.get("timeout_hit"),
            "stall_hit": run_result.get("stall_hit"),
            "stdout_tail": "\n".join(str(run_result.get("stdout", "")).splitlines()[-20:]),
            "stderr_tail": "\n".join(str(run_result.get("stderr", "")).splitlines()[-20:]),
        }
    return report


def _guess_lagrangian_symbol(model: FeynRulesModel) -> str:
    if model.lagrangian_terms:
        return model.lagrangian_terms[-1].name
    return "LBSM"


def _extract_efflrsm_couplings(model: FeynRulesModel) -> dict[str, str]:
    couplings: dict[str, str] = {}
    for parameter in model.parameters:
        if parameter.name in {"gZRq", "gZRl"} and parameter.value:
            couplings[parameter.name] = parameter.value
    return couplings


def _parse_wolfram_json(stdout: str) -> Optional[dict[str, object]]:
    if JSON_MARKER in stdout:
        tail = stdout.rsplit(JSON_MARKER, 1)[-1].strip()
        if tail:
            for candidate in (tail, tail.splitlines()[0].strip()):
                if not candidate:
                    continue
                try:
                    parsed = json.loads(candidate)
                    if isinstance(parsed, dict):
                        return parsed
                except json.JSONDecodeError:
                    continue

    blob = stdout.strip()
    if not blob:
        return None
    first = blob.find("{")
    last = blob.rfind("}")
    if first >= 0 and last > first:
        candidate = blob[first : last + 1]
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            return None
    return None


def _normalize_checks(raw: dict[str, object]) -> list[dict[str, object]]:
    raw_checks = raw.get("checks")
    by_name: dict[str, dict[str, object]] = {}
    if isinstance(raw_checks, list):
        for item in raw_checks:
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            if isinstance(name, str):
                by_name[name] = item

    checks: list[dict[str, object]] = []
    for name in ALL_CHECKS:
        item = by_name.get(name)
        if item is None:
            checks.append(
                {
                    "name": name,
                    "status": "skipped",
                    "passed": None,
                    "detail": "check missing from wolframscript payload",
                }
            )
            continue
        passed = item.get("passed")
        if isinstance(passed, bool):
            status = "passed" if passed else "failed"
        else:
            status = "skipped"
            passed = None
        checks.append(
            {
                "name": name,
                "status": status,
                "passed": passed,
                "detail": str(item.get("detail", "")),
                "value": item.get("value"),
            }
        )
    return checks


def run_wolfram_validation_hooks(
    *,
    model: FeynRulesModel,
    model_path: str,
    base_directory: str,
    wolframscript_path: Optional[str] = "wolframscript",
    feynrules_path: Optional[str] = None,
    timeout_sec: int = 180,
    stall_timeout_sec: int = 60,
) -> dict[str, object]:
    """Run optional Wolfram/FeynRules checks and return structured JSON-friendly data."""
    selected_wolframscript = _resolve_wolframscript_command(wolframscript_path)
    if not _command_exists(selected_wolframscript):
        return _skip_report(
            wolframscript_path=selected_wolframscript,
            reason="wolframscript executable is not available",
        )

    smoke_ok, smoke_reason = _smoke_check_wolframscript(
        selected_wolframscript, cwd=base_directory
    )
    if not smoke_ok:
        return _skip_report(
            wolframscript_path=selected_wolframscript,
            reason=smoke_reason,
        )

    driver_path = Path(__file__).with_name("wolfram_validation_hooks.wl")
    if not driver_path.exists():
        return _error_report(
            wolframscript_path=selected_wolframscript,
            reason=f"validation driver script not found: {driver_path}",
        )

    payload = {
        "schema_version": SCHEMA_VERSION,
        "model_path": str(Path(model_path).resolve()),
        "feynrules_path": str(Path(feynrules_path).resolve()) if feynrules_path else "",
        "lagrangian_symbol": _guess_lagrangian_symbol(model),
        "coupling_expressions": _extract_efflrsm_couplings(model),
        "benchmark": {"kappa_R": 1.0, "sw2": 0.2312},
    }

    payload_fd, payload_path = tempfile.mkstemp(
        prefix="wl_validation_payload_", suffix=".json", dir=base_directory
    )
    os.close(payload_fd)
    Path(payload_path).write_text(json.dumps(payload), encoding="utf-8")

    try:
        run_result = _run_with_watchdog(
            [
                selected_wolframscript,
                "-f",
                str(driver_path),
                f"PayloadPath={payload_path}",
            ],
            cwd=base_directory,
            timeout_sec=max(1, int(timeout_sec)),
            stall_timeout_sec=max(0, int(stall_timeout_sec)),
        )
    finally:
        try:
            os.remove(payload_path)
        except OSError:
            pass

    if run_result["timeout_hit"]:
        return _error_report(
            wolframscript_path=selected_wolframscript,
            reason=f"wolframscript validation exceeded timeout ({timeout_sec}s)",
            run_result=run_result,
        )
    if run_result["stall_hit"]:
        return _error_report(
            wolframscript_path=selected_wolframscript,
            reason=f"wolframscript validation stalled ({stall_timeout_sec}s inactivity)",
            run_result=run_result,
        )
    if int(run_result["returncode"] or 0) != 0:
        return _error_report(
            wolframscript_path=selected_wolframscript,
            reason="wolframscript validation exited with non-zero status",
            run_result=run_result,
        )

    parsed = _parse_wolfram_json(str(run_result.get("stdout", "")))
    if parsed is None:
        return _error_report(
            wolframscript_path=selected_wolframscript,
            reason="could not parse Wolfram JSON payload",
            run_result=run_result,
        )

    checks = _normalize_checks(parsed)
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "ok",
        "created_at_utc": _utc_now_iso(),
        "available": True,
        "wolframscript_path": selected_wolframscript,
        "reason": smoke_reason,
        "checks": checks,
        "process": {
            "returncode": run_result.get("returncode"),
            "elapsed_sec": run_result.get("elapsed_sec"),
            "timeout_hit": run_result.get("timeout_hit"),
            "stall_hit": run_result.get("stall_hit"),
        },
        "raw_result": parsed,
    }
