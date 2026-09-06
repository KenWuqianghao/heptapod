"""Charge-conjugation validator for neutral-fermion mass terms."""

from __future__ import annotations

import re
from fractions import Fraction

from ..frmodel import FeynRulesModel, ParticleClass, SpinType
from .common import count_references, parse_charge, particle_symbols, references

LINT_REQUIRE_NEUTRAL_FERMION_CC = (
    "lint:require_charge_conjugation_for_neutral_fermion_mass_terms"
)


def _has_only_zero_charges(particle: ParticleClass) -> bool:
    quantum_numbers = particle.quantum_numbers or {}
    if not quantum_numbers:
        return False
    parsed: list[Fraction] = []
    for value in quantum_numbers.values():
        charge = parse_charge(value)
        if charge is None:
            return False
        parsed.append(charge)
    return bool(parsed) and all(charge == 0 for charge in parsed)


def _is_neutral_fermion(particle: ParticleClass) -> bool:
    if particle.spin_type not in {SpinType.F, SpinType.W, SpinType.R, SpinType.RW}:
        return False
    if particle.self_conjugate:
        return True
    symbols = particle_symbols(particle)
    if any("nu" in symbol.lower() or symbol.lower().startswith("v") for symbol in symbols):
        return True
    return _has_only_zero_charges(particle)


def _contains_cc_for_symbol(expression: str, symbol: str) -> bool:
    return re.search(rf"CC\s*\[\s*{re.escape(symbol)}(?:\s*\[|[\s\]])", expression) is not None


def check_charge_conjugation(model: FeynRulesModel) -> dict[str, object]:
    """Require CC[...] structure in neutral-fermion Majorana-like mass terms."""
    offenders: list[str] = []
    all_mass_symbols = [
        p.mass.sym
        for p in model.particles
        if p.mass is not None and not p.mass.massless and p.mass.sym
    ]

    for particle in model.particles:
        if not _is_neutral_fermion(particle):
            continue
        symbols = particle_symbols(particle)
        mass_hints = [p for p in all_mass_symbols if p]
        for symbol in symbols:
            for term in model.lagrangian_terms:
                if count_references(term.expression, symbol) < 2:
                    continue
                has_mass_hint = any(references(term.expression, hint) for hint in mass_hints)
                has_generic_mass_symbol = bool(
                    re.search(r"(?<![A-Za-z0-9$])M[A-Za-z0-9$]*(?![A-Za-z0-9$])", term.expression)
                )
                if not (has_mass_hint or has_generic_mass_symbol):
                    continue
                if not _contains_cc_for_symbol(term.expression, symbol):
                    offenders.append(f"{term.name}:{symbol}")

    if offenders:
        return {
            "name": LINT_REQUIRE_NEUTRAL_FERMION_CC,
            "passed": False,
            "detail": (
                "neutral-fermion mass terms require charge-conjugation form; "
                f"missing CC in {sorted(set(offenders))}"
            ),
        }

    return {
        "name": LINT_REQUIRE_NEUTRAL_FERMION_CC,
        "passed": True,
        "detail": "neutral-fermion mass terms use charge-conjugation form",
    }
