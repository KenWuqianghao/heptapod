#!/usr/bin/env python3
"""Tests for Wolfram-gated validation hooks."""

from __future__ import annotations

import json
import shutil
import sys
import textwrap
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

from frgen.frgen_tool import GenerateFeynRulesModelTool  # noqa: E402
from frgen.frmodel import (  # noqa: E402
    FeynRulesModel,
    LagrangianTerm,
    MassSpec,
    ModelInfo,
    Parameter,
    ParticleClass,
)
import frgen.wolfram_validation_hooks as wl_hooks  # noqa: E402
from frgen.wolfram_validation_hooks import (  # noqa: E402
    CHECK_HERMITICITY,
    CHECK_KINETIC_NORM,
    CHECK_MASS_SPECTRUM,
    CHECK_NUMERIC_COUPLING,
    run_wolfram_validation_hooks,
)


def _valid_model() -> FeynRulesModel:
    return FeynRulesModel(
        model_name="EffLRSMHookTest",
        info=ModelInfo(
            authors=["HEPSIM5"],
            version="1.0.0",
            date="2026-09-06",
            institutions=["HEP"],
            emails=["dev@example.org"],
        ),
        parameters=[
            Parameter(
                name="gZRq",
                parameter_type="Internal",
                value="kRquark*ee/sw/Sqrt[1 - (sw/(cw*kRquark))^2]",
            ),
            Parameter(
                name="gZRl",
                parameter_type="Internal",
                value="kRlepton*ee/sw/Sqrt[1 - (sw/(cw*kRlepton))^2]",
            ),
        ],
        particles=[
            ParticleClass(
                spin_type="S",
                class_index=100,
                class_name="S1",
                self_conjugate=False,
                mass=MassSpec(sym="MS1", value="1500."),
                width=MassSpec(sym="W1", value="1."),
                quantum_numbers={"Q": "-1/3"},
                particle_name="S1",
                antiparticle_name="S1~",
            )
        ],
        lagrangian_terms=[
            LagrangianTerm(
                name="LBSM",
                expression="DC[S1bar,mu] DC[S1,mu] - MS1^2 * HC[S1].S1",
                delayed=False,
            )
        ],
    )


def _write_fake_wolframscript(tmp_path: Path) -> Path:
    script = tmp_path / "fake_wolframscript.py"
    script.write_text(
        textwrap.dedent(
            """\
            #!/usr/bin/env python3
            import json
            import os
            import sys

            mode = os.environ.get("FAKE_WL_MODE", "ok")
            args = sys.argv[1:]

            if "-code" in args:
                if mode == "smoke_fail":
                    print("license not activated", file=sys.stderr, flush=True)
                    sys.exit(1)
                print("4", flush=True)
                sys.exit(0)

            payload_path = ""
            for arg in args:
                if arg.startswith("PayloadPath="):
                    payload_path = arg.split("=", 1)[1]
                    break

            if mode == "bad_json":
                print("not-json", flush=True)
                sys.exit(0)

            with open(payload_path, encoding="utf-8") as fh:
                payload = json.load(fh)

            values = {"gZRq": -0.58, "gZRl": -0.58}
            checks = [
                {"name": "kinetic_term_normalisation", "passed": True, "detail": "ok"},
                {"name": "mass_spectrum", "passed": True, "detail": "ok"},
                {"name": "hermiticity", "passed": True, "detail": "ok"},
                {
                    "name": "numeric_coupling_probe_efflrsm_zr",
                    "passed": True,
                    "detail": "ok",
                    "value": values,
                },
            ]
            if mode == "missing_one_check":
                checks = checks[:-1]

            out = {
                "schema_version": "wolfram-validation-1.0",
                "checks": checks,
                "meta": {"model_path": payload.get("model_path", "")},
            }
            print("log-line-before-json", flush=True)
            print("HEPTAPOD_WL_JSON:" + json.dumps(out), flush=True)
            sys.exit(0)
            """
        ),
        encoding="utf-8",
    )
    script.chmod(0o755)
    return script


def test_wolfram_hooks_skip_cleanly_when_binary_is_absent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    model = _valid_model()
    model_path = tmp_path / "model.fr"
    model_path.write_text('M$ModelName = "EffLRSMHookTest";\n', encoding="utf-8")
    # Force-disable PATH fallback so "absent" stays absent on Wolfram-enabled hosts.
    monkeypatch.setattr(wl_hooks.shutil, "which", lambda _name: None)

    report = run_wolfram_validation_hooks(
        model=model,
        model_path=str(model_path),
        base_directory=str(tmp_path),
        wolframscript_path="/definitely/missing/wolframscript",
    )
    assert report["status"] == "skipped", report
    assert report["available"] is False, report
    assert "not available" in report["reason"], report
    assert len(report["checks"]) == 4, report
    assert all(check["status"] == "skipped" for check in report["checks"]), report


def test_wolfram_hooks_parse_stubbed_json_payload(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake_wl = _write_fake_wolframscript(tmp_path)
    model = _valid_model()
    model_path = tmp_path / "model.fr"
    model_path.write_text('M$ModelName = "EffLRSMHookTest";\n', encoding="utf-8")

    monkeypatch.setenv("FAKE_WL_MODE", "ok")
    report = run_wolfram_validation_hooks(
        model=model,
        model_path=str(model_path),
        base_directory=str(tmp_path),
        wolframscript_path=str(fake_wl),
        timeout_sec=20,
        stall_timeout_sec=20,
    )

    assert report["status"] == "ok", report
    checks = {item["name"]: item for item in report["checks"]}
    assert checks[CHECK_KINETIC_NORM]["status"] == "passed", checks
    assert checks[CHECK_MASS_SPECTRUM]["status"] == "passed", checks
    assert checks[CHECK_HERMITICITY]["status"] == "passed", checks
    assert checks[CHECK_NUMERIC_COUPLING]["status"] == "passed", checks
    assert checks[CHECK_NUMERIC_COUPLING]["value"]["gZRq"] == pytest.approx(-0.58)


def test_tool_output_includes_wolfram_report_when_unavailable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    model_json = _valid_model().model_dump_json()
    # Force-disable PATH fallback so the tool reports deterministic skip.
    monkeypatch.setattr(wl_hooks.shutil, "which", lambda _name: None)
    tool = GenerateFeynRulesModelTool(
        model_json=model_json,
        base_directory=str(tmp_path),
        wolframscript_path="/missing/wolframscript",
        enable_wolfram_validation=True,
    )
    result = json.loads(tool._run())
    assert result["status"] == "ok", result
    assert "wolfram_validation" in result, result
    assert result["wolfram_validation"]["status"] == "skipped", result


def test_real_wolframscript_smoke_if_available(tmp_path: Path) -> None:
    binary = shutil.which("wolframscript")
    if not binary:
        pytest.skip("wolframscript is not installed in this environment")

    model = _valid_model()
    model_path = tmp_path / "model.fr"
    model_path.write_text('M$ModelName = "EffLRSMHookTest";\n', encoding="utf-8")

    report = run_wolfram_validation_hooks(
        model=model,
        model_path=str(model_path),
        base_directory=str(tmp_path),
        wolframscript_path=binary,
        timeout_sec=60,
        stall_timeout_sec=60,
    )
    if report["status"] == "skipped":
        pytest.skip(f"wolframscript present but not usable: {report['reason']}")
    assert report["status"] in {"ok", "error"}, report
