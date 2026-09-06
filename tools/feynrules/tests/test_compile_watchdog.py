#!/usr/bin/env python3
"""
Watchdog and stall-detection tests for FeynRulesToUFOTool.

These tests use a stub subprocess and do not require Mathematica.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import textwrap
import time
import types
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[3]
sys.path.insert(0, str(REPO_ROOT / "tools"))


def _install_orchestral_stub() -> None:
    """Install a minimal orchestral stub for local unit tests."""
    if "orchestral.tools.base.tool" in sys.modules:
        return

    tool_mod = types.ModuleType("orchestral.tools.base.tool")
    field_mod = types.ModuleType("orchestral.tools.base.field_utils")
    base_mod = types.ModuleType("orchestral.tools.base")
    tools_mod = types.ModuleType("orchestral.tools")
    orch_mod = types.ModuleType("orchestral")

    class BaseTool:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

        def format_error(self, **kwargs):
            return json.dumps({"error": kwargs})

    def RuntimeField(default=None, description=None):  # noqa: ARG001
        return default

    def StateField(default=None, description=None):  # noqa: ARG001
        return default

    tool_mod.BaseTool = BaseTool
    field_mod.RuntimeField = RuntimeField
    field_mod.StateField = StateField

    sys.modules["orchestral"] = orch_mod
    sys.modules["orchestral.tools"] = tools_mod
    sys.modules["orchestral.tools.base"] = base_mod
    sys.modules["orchestral.tools.base.tool"] = tool_mod
    sys.modules["orchestral.tools.base.field_utils"] = field_mod


_install_orchestral_stub()

from feynrules.feynrules import FeynRulesToUFOTool  # noqa: E402


def _write_fake_wolframscript(tmp_path: Path) -> Path:
    script = tmp_path / "fake_wolframscript.py"
    script.write_text(
        textwrap.dedent(
            """\
            #!/usr/bin/env python3
            import os
            import sys
            import time

            mode = os.environ.get("FAKE_WL_MODE", "sleep")
            sleep_sec = float(os.environ.get("FAKE_WL_SLEEP_SEC", "5"))

            if mode == "emit_then_stall":
                print("compile-start", flush=True)
                time.sleep(sleep_sec)
                sys.exit(0)

            if mode == "quick_success":
                print("ok", flush=True)
                sys.exit(0)

            time.sleep(sleep_sec)
            sys.exit(0)
            """
        ),
        encoding="utf-8",
    )
    script.chmod(0o755)
    return script


def _make_model(tmp_path: Path, *, sextet: bool) -> Path:
    model = tmp_path / ("sextet_model.fr" if sextet else "simple_model.fr")
    if sextet:
        text = """
M$ModelName = "SextetModel";
S[368] == {
  ClassName -> S6,
  ColorDim -> 6
};
"""
    else:
        text = """
M$ModelName = "SimpleModel";
S[100] == {
  ClassName -> S1
};
"""
    model.write_text(text.strip() + "\n", encoding="utf-8")
    return model


def test_watchdog_timeout_returns_structured_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_wl = _write_fake_wolframscript(tmp_path)
    model = _make_model(tmp_path, sextet=False)
    monkeypatch.setenv("FAKE_WL_MODE", "sleep")
    monkeypatch.setenv("FAKE_WL_SLEEP_SEC", "8")

    tool = FeynRulesToUFOTool(
        base_directory=str(tmp_path),
        feynrules_path=str(tmp_path),
        wolframscript_path=str(fake_wl),
        model_path=str(model),
        output_dir="ufo_out",
        timeout_sec=1,
        stall_timeout_sec=10,
    )

    started = time.monotonic()
    result = json.loads(tool._run())
    elapsed = time.monotonic() - started

    assert result["ok"] is False, result
    assert result["error"]["code"] == "compile_timeout", result
    assert result["error"]["timeout_sec"] == 1, result
    assert elapsed < 6, elapsed
    assert Path(result["logs"]["stdout"]).exists(), result
    assert Path(result["logs"]["stderr"]).exists(), result


def test_sextet_stall_detection_fails_fast(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_wl = _write_fake_wolframscript(tmp_path)
    model = _make_model(tmp_path, sextet=True)
    monkeypatch.setenv("FAKE_WL_MODE", "emit_then_stall")
    monkeypatch.setenv("FAKE_WL_SLEEP_SEC", "8")

    tool = FeynRulesToUFOTool(
        base_directory=str(tmp_path),
        feynrules_path=str(tmp_path),
        wolframscript_path=str(fake_wl),
        model_path=str(model),
        output_dir="ufo_out",
        timeout_sec=30,
        stall_timeout_sec=1,
    )

    started = time.monotonic()
    result = json.loads(tool._run())
    elapsed = time.monotonic() - started

    assert result["ok"] is False, result
    assert result["error"]["code"] == "sextet_stall_detected", result
    assert "class-index:S[368]" in result["error"]["model_markers"], result
    assert elapsed < 6, elapsed


def test_non_sextet_compile_does_not_use_sextet_stall_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake_wl = _write_fake_wolframscript(tmp_path)
    model = _make_model(tmp_path, sextet=False)
    monkeypatch.setenv("FAKE_WL_MODE", "emit_then_stall")
    monkeypatch.setenv("FAKE_WL_SLEEP_SEC", "8")

    tool = FeynRulesToUFOTool(
        base_directory=str(tmp_path),
        feynrules_path=str(tmp_path),
        wolframscript_path=str(fake_wl),
        model_path=str(model),
        output_dir="ufo_out",
        timeout_sec=2,
        stall_timeout_sec=1,
    )

    result = json.loads(tool._run())
    assert result["ok"] is False, result
    assert result["error"]["code"] == "compile_timeout", result


def test_wolframscript_fallback_prefers_real_binary(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    tool = FeynRulesToUFOTool(
        base_directory=str(tmp_path),
        feynrules_path=str(tmp_path),
        wolframscript_path="/path/to/wolframscript",
    )

    def _fake_which(name: str) -> str | None:
        if name == "wolframscript":
            return "/usr/local/bin/wolframscript"
        return None

    monkeypatch.setattr("feynrules.feynrules.shutil.which", _fake_which)
    resolved = tool._resolve_wolframscript_command()
    assert resolved == "/usr/local/bin/wolframscript"


def test_real_wolframscript_smoke_if_available() -> None:
    """Optional smoke test for environments with an activated Wolfram Engine."""
    binary = shutil.which("wolframscript")
    if not binary:
        pytest.skip("wolframscript is not installed in this environment")

    proc = subprocess.run(
        [binary, "-code", "Print[2+2]"],
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    if proc.returncode != 0:
        pytest.skip(
            "wolframscript is present but not activated; run real E2E on Ken's shared Grok Bot box"
        )
    assert "4" in proc.stdout, proc.stdout
