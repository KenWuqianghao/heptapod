#!/usr/bin/env python3
"""Tests for pure-Python structural validators."""

from __future__ import annotations

import json
import sys
import types
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[3]
FIXTURES_DIR = SCRIPT_PATH.parent / "fixtures"
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

import frgen.frgen_tool as frgen_tool_module  # noqa: E402
from frgen.frgen_tool import GenerateFeynRulesModelTool  # noqa: E402
from frgen.frmodel import FeynRulesModel  # noqa: E402
from frgen.structural_validators import (  # noqa: E402
    LINT_REQUIRE_FIELD_COMPLETENESS,
    run_structural_validators,
)
from frgen.structural_validators.charge_and_su2 import (  # noqa: E402
    LINT_REQUIRE_CHARGE_AND_SU2,
    check_charge_and_su2,
)
from frgen.structural_validators.charge_conjugation import (  # noqa: E402
    LINT_REQUIRE_NEUTRAL_FERMION_CC,
    check_charge_conjugation,
)
from frgen.structural_validators.dimension_counter import (  # noqa: E402
    LINT_REQUIRE_DIMENSION_FOUR,
    check_dimension_counter,
)
from frgen.structural_validators.field_completeness import (  # noqa: E402
    check_field_completeness,
)


def _load_fixture(name: str) -> dict:
    return json.loads((FIXTURES_DIR / name).read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    ("fixture_name", "validator", "check_name"),
    [
        (
            "structural_field_completeness_top_phillic_zprime.json",
            check_field_completeness,
            LINT_REQUIRE_FIELD_COMPLETENESS,
        ),
        (
            "structural_dimension_counter_368_sextet.json",
            check_dimension_counter,
            LINT_REQUIRE_DIMENSION_FOUR,
        ),
        (
            "structural_charge_conjugation_efflrsm.json",
            check_charge_conjugation,
            LINT_REQUIRE_NEUTRAL_FERMION_CC,
        ),
        (
            "structural_charge_and_su2_general_u1.json",
            check_charge_and_su2,
            LINT_REQUIRE_CHARGE_AND_SU2,
        ),
    ],
)
def test_structural_validator_fails_and_passes(
    fixture_name: str,
    validator,
    check_name: str,
) -> None:
    fixture = _load_fixture(fixture_name)
    failing_model = FeynRulesModel(**fixture["failing_model"])
    passing_model = FeynRulesModel(**fixture["passing_model"])

    failed = validator(failing_model)
    passed = validator(passing_model)

    assert failed["name"] == check_name, failed
    assert failed["passed"] is False, failed
    assert passed["name"] == check_name, passed
    assert passed["passed"] is True, passed


def test_structural_validator_runner_returns_all_four_checks() -> None:
    fixture = _load_fixture("structural_field_completeness_top_phillic_zprime.json")
    model = FeynRulesModel(**fixture["failing_model"])
    checks = run_structural_validators(model)
    names = {check["name"] for check in checks}
    assert LINT_REQUIRE_FIELD_COMPLETENESS in names
    assert LINT_REQUIRE_DIMENSION_FOUR in names
    assert LINT_REQUIRE_NEUTRAL_FERMION_CC in names
    assert LINT_REQUIRE_CHARGE_AND_SU2 in names


def test_tool_reports_structural_failures_before_render(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    fixture = _load_fixture("structural_field_completeness_top_phillic_zprime.json")
    model = FeynRulesModel(**fixture["failing_model"])

    def _fail_if_called(_model):  # noqa: ANN001
        raise AssertionError("render_model should not run when structural lint fails")

    monkeypatch.setattr(frgen_tool_module, "render_model", _fail_if_called)
    tool = GenerateFeynRulesModelTool(
        model_json=model.model_dump_json(),
        base_directory=str(tmp_path),
    )
    result = json.loads(tool._run())
    assert result["status"] == "lint_failed", result
    failed_names = {check["name"] for check in result["failed_checks"]}
    assert LINT_REQUIRE_FIELD_COMPLETENESS in failed_names, result
