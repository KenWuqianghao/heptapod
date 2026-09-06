"""Pure-Python structural validators for extracted model JSON."""

from __future__ import annotations

from ..frmodel import FeynRulesModel
from .charge_and_su2 import LINT_REQUIRE_CHARGE_AND_SU2, check_charge_and_su2
from .charge_conjugation import (
    LINT_REQUIRE_NEUTRAL_FERMION_CC,
    check_charge_conjugation,
)
from .dimension_counter import LINT_REQUIRE_DIMENSION_FOUR, check_dimension_counter
from .field_completeness import LINT_REQUIRE_FIELD_COMPLETENESS, check_field_completeness


def run_structural_validators(model: FeynRulesModel) -> list[dict[str, object]]:
    """Run all structural validators and return named check records."""
    return [
        check_field_completeness(model),
        check_dimension_counter(model),
        check_charge_conjugation(model),
        check_charge_and_su2(model),
    ]


__all__ = [
    "LINT_REQUIRE_CHARGE_AND_SU2",
    "LINT_REQUIRE_DIMENSION_FOUR",
    "LINT_REQUIRE_FIELD_COMPLETENESS",
    "LINT_REQUIRE_NEUTRAL_FERMION_CC",
    "run_structural_validators",
]
