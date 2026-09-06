"""Operator-dimension validator."""

from __future__ import annotations

from ..frmodel import FeynRulesModel
from .common import (
    ceil_nonnegative,
    count_references,
    lambda_suppression_power,
    model_field_dimensions,
    references,
)

LINT_REQUIRE_DIMENSION_FOUR = (
    "lint:require_dimension_four_after_lambda_prefactors"
)

_DERIVATIVE_MARKERS = ("DC[", "CovD[", "del[", "Del[")
_COMMON_SCALARS = {"H", "Hd", "Hu", "Phi"}
_COMMON_FERMIONS = {"qL", "uR", "dR", "lL", "eR", "vL", "nuL", "nuR"}


def _extra_symbol_dimension(symbol: str) -> float | None:
    if symbol in _COMMON_SCALARS:
        return 1.0
    if symbol in _COMMON_FERMIONS:
        return 1.5
    if symbol.endswith(("L", "R")) and symbol[:1].islower():
        return 1.5
    return None


def _term_dimension_estimate(expression: str, field_dims: dict[str, float]) -> float:
    total = 0.0
    for symbol, dim in field_dims.items():
        total += count_references(expression, symbol) * dim
    for symbol in _COMMON_SCALARS | _COMMON_FERMIONS:
        if symbol in field_dims:
            continue
        total += count_references(expression, symbol) * _extra_symbol_dimension(symbol)
    return total


def _derivative_dimension(expression: str) -> int:
    return sum(expression.count(marker) for marker in _DERIVATIVE_MARKERS)


def _split_top_level_additive(expression: str) -> list[str]:
    chunks: list[str] = []
    depth = 0
    current: list[str] = []
    for char in expression:
        if char in "([{":
            depth += 1
        elif char in ")]}":
            depth = max(0, depth - 1)
        if char in "+-" and depth == 0:
            chunk = "".join(current).strip()
            if chunk:
                chunks.append(chunk)
            current = [char]
            continue
        current.append(char)
    tail = "".join(current).strip()
    if tail:
        chunks.append(tail)
    return chunks


def _references_other_terms(model: FeynRulesModel, term_name: str, expression: str) -> bool:
    for term in model.lagrangian_terms:
        if term.name == term_name:
            continue
        if references(expression, term.name):
            return True
    return False


def check_dimension_counter(model: FeynRulesModel) -> dict[str, object]:
    """Require each primitive term to reach dimension four after Lambda factors."""
    field_dims = model_field_dimensions(model)
    offenders: list[str] = []

    for term in model.lagrangian_terms:
        expr = term.expression
        if _references_other_terms(model, term.name, expr):
            continue
        if any(marker in expr for marker in _DERIVATIVE_MARKERS):
            continue

        monomials = _split_top_level_additive(expr)
        for monomial in monomials:
            field_dim = _term_dimension_estimate(monomial, field_dims)
            derivative_dim = _derivative_dimension(monomial)
            raw_dim = field_dim + derivative_dim
            if raw_dim <= 4.0:
                continue
            needed = ceil_nonnegative(raw_dim - 4.0)
            suppression = lambda_suppression_power(monomial)
            if suppression < needed:
                offenders.append(
                    f"{term.name}: dim~{raw_dim:g}, needs 1/Lambda^{needed}, found power {suppression}"
                )
                break

    if offenders:
        return {
            "name": LINT_REQUIRE_DIMENSION_FOUR,
            "passed": False,
            "detail": "dimension-four check failed for terms: " + ", ".join(offenders),
        }

    return {
        "name": LINT_REQUIRE_DIMENSION_FOUR,
        "passed": True,
        "detail": "all primitive lagrangian terms satisfy dimension four after Lambda prefactors",
    }
