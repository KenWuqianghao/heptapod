"""Field completeness validator."""

from __future__ import annotations

from ..frmodel import FeynRulesModel
from .common import flatten_mass_symbols, particle_symbols, references

LINT_REQUIRE_FIELD_COMPLETENESS = (
    "lint:require_declared_fields_in_kinetic_and_mass_terms"
)

_KINETIC_MARKERS = ("DC[", "CovD[", "del[", "Del[", "FS[", "FieldStrength")


def check_field_completeness(model: FeynRulesModel) -> dict[str, object]:
    """Require each declared field to appear in kinetic and mass terms."""
    missing_kinetic: list[str] = []
    missing_mass: list[str] = []

    for particle in model.particles:
        if particle.unphysical:
            continue

        symbols = particle_symbols(particle)
        mass_tokens = flatten_mass_symbols(particle)
        requires_mass = bool(mass_tokens)

        for symbol in symbols:
            has_kinetic = any(
                references(term.expression, symbol)
                and any(marker in term.expression for marker in _KINETIC_MARKERS)
                for term in model.lagrangian_terms
            )
            if not has_kinetic:
                missing_kinetic.append(symbol)

            if not requires_mass:
                continue
            has_mass = any(
                references(term.expression, symbol)
                and any(references(term.expression, mass) for mass in mass_tokens)
                for term in model.lagrangian_terms
            )
            if not has_mass:
                missing_mass.append(symbol)

    if missing_kinetic or missing_mass:
        detail_parts: list[str] = []
        if missing_kinetic:
            detail_parts.append(
                f"missing kinetic term references for {sorted(set(missing_kinetic))}"
            )
        if missing_mass:
            detail_parts.append(
                f"missing mass term references for {sorted(set(missing_mass))}"
            )
        return {
            "name": LINT_REQUIRE_FIELD_COMPLETENESS,
            "passed": False,
            "detail": "; ".join(detail_parts),
        }

    return {
        "name": LINT_REQUIRE_FIELD_COMPLETENESS,
        "passed": True,
        "detail": "all declared fields appear in kinetic and mass terms",
    }
