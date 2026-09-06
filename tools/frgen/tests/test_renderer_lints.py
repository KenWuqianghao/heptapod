#!/usr/bin/env python3
"""
Renderer lint tests for tools.frgen.render.

These tests are pure Python. They do not call Wolfram or FeynRules.
"""

from __future__ import annotations

import json
import sys
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

from frgen.frgen_tool import GenerateFeynRulesModelTool
from frgen.frmodel import (  # noqa: E402
    FeynRulesModel,
    LagrangianTerm,
    MassSpec,
    ModelInfo,
    Parameter,
    ParticleClass,
    Rule,
)
from frgen.render import (  # noqa: E402
    LINT_REJECT_FIELD_FREE_TERMS,
    LINT_REJECT_INVALID_PARTICLE_IDENTIFIERS,
    LINT_REJECT_TENSOR_PATTERN_DEFINITIONS,
    LINT_REQUIRE_ADD_GAUGE_REPRESENTATION,
    LINT_REQUIRE_INTERACTION_ORDER,
    LINT_REQUIRE_SINGLE_TOTAL_LAGRANGIAN,
    RendererLintError,
    render_model,
    run_renderer_lints,
)


def _base_model() -> FeynRulesModel:
    return FeynRulesModel(
        model_name="LintModel",
        info=ModelInfo(
            authors=["Dev User"],
            version="1.0.0",
            date="2026-09-06",
            institutions=["HEPSIM5"],
            emails=["dev@example.org"],
        ),
        parameters=[
            Parameter(
                name="yRR11",
                parameter_type="External",
                block_name="BSMINPUTS",
                complex=False,
                interaction_order=("NP", 1),
                value="0.5",
                description="test yukawa",
            )
        ],
        particles=[
            ParticleClass(
                spin_type="S",
                class_index=100,
                class_name="S1",
                self_conjugate=False,
                indices=["Colour"],
                mass=MassSpec(sym="MS1", value="1500."),
                width=MassSpec(sym="W1", value="1."),
                quantum_numbers={"Q": "-1/3"},
                particle_name="S1",
                antiparticle_name="S1~",
                full_name="Scalar test field",
                propagator_label="S1",
            )
        ],
        raw_blocks=["AddGaugeRepresentation[S1, SU3C, T, Colour];"],
        lagrangian_terms=[
            LagrangianTerm(
                name="Lkin",
                expression=(
                    "Block[{mu,aa}, DC[S1bar[aa],mu] DC[S1[aa],mu] "
                    "- MS1^2 * HC[S1].S1]"
                ),
            ),
            LagrangianTerm(
                name="Lint",
                expression="Block[{aa}, yRR11 * HC[S1][aa] * S1[aa]]",
                delayed=True,
            ),
            LagrangianTerm(name="Ltotal", expression="Lkin + Lint"),
        ],
    )


def _checks_by_name(model: FeynRulesModel):
    checks = run_renderer_lints(model)
    return {c["name"]: c for c in checks}


def _assert_lint_fails(model: FeynRulesModel, lint_name: str) -> None:
    checks = _checks_by_name(model)
    assert lint_name in checks, checks
    assert checks[lint_name]["passed"] is False, checks[lint_name]
    with pytest.raises(RendererLintError):
        render_model(model)


@pytest.fixture
def valid_model() -> FeynRulesModel:
    return _base_model()


@pytest.fixture
def no_interaction_order_model(valid_model: FeynRulesModel) -> FeynRulesModel:
    model = valid_model.model_copy(deep=True)
    model.parameters[0].interaction_order = None
    return model


@pytest.fixture
def tensor_pattern_definition_model(valid_model: FeynRulesModel) -> FeynRulesModel:
    model = valid_model.model_copy(deep=True)
    model.parameters.append(
        Parameter(
            name="YT",
            parameter_type="Internal",
            indices=["Colour"],
            definitions=[Rule(lhs="YT[a_,b_]", rhs="0")],
        )
    )
    return model


@pytest.fixture
def invalid_particle_name_model(valid_model: FeynRulesModel) -> FeynRulesModel:
    model = valid_model.model_copy(deep=True)
    model.particles[0].particle_name = "S1-bad"
    return model


@pytest.fixture
def field_free_term_model(valid_model: FeynRulesModel) -> FeynRulesModel:
    model = valid_model.model_copy(deep=True)
    model.lagrangian_terms = [LagrangianTerm(name="Ltotal", expression="1/2")]
    return model


@pytest.fixture
def missing_add_gauge_representation_model(valid_model: FeynRulesModel) -> FeynRulesModel:
    model = valid_model.model_copy(deep=True)
    model.raw_blocks = []
    return model


@pytest.fixture
def multi_total_lagrangian_model(valid_model: FeynRulesModel) -> FeynRulesModel:
    model = valid_model.model_copy(deep=True)
    model.lagrangian_terms.append(
        LagrangianTerm(name="Lalt", expression="Lint")
    )
    return model


def test_positive_fixture_passes_all_lints(valid_model: FeynRulesModel) -> None:
    checks = run_renderer_lints(valid_model)
    assert checks, checks
    assert all(c["passed"] for c in checks), checks
    text = render_model(valid_model)
    assert "M$ModelName" in text


def test_require_interaction_order_negative(
    no_interaction_order_model: FeynRulesModel,
) -> None:
    _assert_lint_fails(no_interaction_order_model, LINT_REQUIRE_INTERACTION_ORDER)


def test_reject_tensor_pattern_definitions_negative(
    tensor_pattern_definition_model: FeynRulesModel,
) -> None:
    _assert_lint_fails(
        tensor_pattern_definition_model, LINT_REJECT_TENSOR_PATTERN_DEFINITIONS
    )


def test_reject_invalid_particle_names_negative(
    invalid_particle_name_model: FeynRulesModel,
) -> None:
    _assert_lint_fails(
        invalid_particle_name_model, LINT_REJECT_INVALID_PARTICLE_IDENTIFIERS
    )


def test_reject_field_free_constant_terms_negative(
    field_free_term_model: FeynRulesModel,
) -> None:
    _assert_lint_fails(field_free_term_model, LINT_REJECT_FIELD_FREE_TERMS)


def test_require_add_gauge_representation_negative(
    missing_add_gauge_representation_model: FeynRulesModel,
) -> None:
    _assert_lint_fails(
        missing_add_gauge_representation_model, LINT_REQUIRE_ADD_GAUGE_REPRESENTATION
    )


def test_require_one_total_lagrangian_negative(
    multi_total_lagrangian_model: FeynRulesModel,
) -> None:
    _assert_lint_fails(
        multi_total_lagrangian_model, LINT_REQUIRE_SINGLE_TOTAL_LAGRANGIAN
    )


def test_tool_reports_structured_lint_failures(
    no_interaction_order_model: FeynRulesModel, tmp_path: Path
) -> None:
    tool = GenerateFeynRulesModelTool(
        model_json=no_interaction_order_model.model_dump_json(),
        base_directory=str(tmp_path),
    )
    result = json.loads(tool._run())
    assert result["status"] == "lint_failed", result
    assert result["passed"] is False, result
    failed = {c["name"] for c in result["failed_checks"]}
    assert LINT_REQUIRE_INTERACTION_ORDER in failed, result
