"""U(1)_X conservation and SU(2) epsilon-structure validator."""

from __future__ import annotations

import re
from fractions import Fraction

from ..frmodel import FeynRulesModel, SpinType
from .common import (
    charge_keys_for_u1x,
    parse_charge,
    particle_symbols,
    references,
)

LINT_REQUIRE_CHARGE_AND_SU2 = (
    "lint:require_u1x_charge_conservation_and_su2_epsilon_for_doublet_yukawas"
)

_EPSILON_RE = re.compile(
    r"(?<![A-Za-z0-9$])(Eps|eps|Epsilon|LeviCivita|SU2Eps)(?![A-Za-z0-9$])"
)


def _signed_occurrence_count(expression: str, symbol: str) -> int:
    """Count field insertions, with sign flips for conjugated forms."""
    work = expression
    positive = 0
    negative = 0

    double_flip_patterns = [
        rf"anti\s*\[\s*CC\s*\[\s*{re.escape(symbol)}(?:\s*\[[^\]]*\])?\s*\]\s*\]",
    ]
    for pattern in double_flip_patterns:
        matches = re.findall(pattern, work)
        positive += len(matches)
        work = re.sub(pattern, " ", work)

    single_flip_patterns = [
        rf"HC\s*\[\s*{re.escape(symbol)}(?:\s*\[[^\]]*\])?\s*\]",
        rf"CC\s*\[\s*{re.escape(symbol)}(?:\s*\[[^\]]*\])?\s*\]",
        rf"anti\s*\[\s*{re.escape(symbol)}(?:\s*\[[^\]]*\])?\s*\]",
        rf"(?<![A-Za-z0-9$]){re.escape(symbol)}bar(?![A-Za-z0-9$])",
    ]
    for pattern in single_flip_patterns:
        matches = re.findall(pattern, work)
        negative += len(matches)
        work = re.sub(pattern, " ", work)

    plain_pattern = rf"(?<![A-Za-z0-9$]){re.escape(symbol)}(?![A-Za-z0-9$])"
    positive += len(re.findall(plain_pattern, work))
    return positive - negative


def _doublet_symbols(model: FeynRulesModel) -> set[str]:
    symbols: set[str] = set()
    for particle in model.particles:
        if any("SU2" in index for index in (particle.indices or [])):
            symbols.update(particle_symbols(particle))
    return symbols


def _symbol_spin_map(model: FeynRulesModel) -> dict[str, SpinType]:
    spins: dict[str, SpinType] = {}
    for particle in model.particles:
        for symbol in particle_symbols(particle):
            spins[symbol] = particle.spin_type
    return spins


def check_charge_and_su2(model: FeynRulesModel) -> dict[str, object]:
    """Validate U(1)_X charge conservation and SU(2) epsilon in doublet Yukawas."""
    charge_keys = charge_keys_for_u1x(model.particles)
    field_charges: dict[str, dict[str, Fraction]] = {}
    for particle in model.particles:
        symbols = particle_symbols(particle)
        for key in charge_keys:
            raw = (particle.quantum_numbers or {}).get(key)
            if raw is None:
                continue
            parsed = parse_charge(raw)
            if parsed is None:
                continue
            for symbol in symbols:
                field_charges.setdefault(symbol, {})[key] = parsed

    charge_violations: list[str] = []
    if charge_keys:
        for term in model.lagrangian_terms:
            for key in sorted(charge_keys):
                total = Fraction(0)
                for symbol, charges in field_charges.items():
                    if key not in charges:
                        continue
                    signed_count = _signed_occurrence_count(term.expression, symbol)
                    if signed_count:
                        total += charges[key] * signed_count
                if total != 0:
                    charge_violations.append(f"{term.name}:{key}={total}")

    doublets = _doublet_symbols(model)
    symbol_spins = _symbol_spin_map(model)
    epsilon_violations: list[str] = []
    for term in model.lagrangian_terms:
        referenced_doublets = [
            symbol for symbol in sorted(doublets) if references(term.expression, symbol)
        ]
        if len(referenced_doublets) < 2:
            continue
        has_fermion = any(
            symbol_spins.get(symbol) in {SpinType.F, SpinType.W, SpinType.R, SpinType.RW}
            for symbol in referenced_doublets
        )
        has_scalar = any(symbol_spins.get(symbol) == SpinType.S for symbol in referenced_doublets)
        if not (has_fermion and has_scalar):
            continue
        if _EPSILON_RE.search(term.expression) is None:
            epsilon_violations.append(term.name)

    if charge_violations or epsilon_violations:
        detail_parts: list[str] = []
        if charge_violations:
            detail_parts.append(
                "U(1)_X charge conservation failed in "
                f"{sorted(set(charge_violations))}"
            )
        if epsilon_violations:
            detail_parts.append(
                "SU(2) doublet-doublet Yukawa terms need epsilon contraction in "
                f"{sorted(set(epsilon_violations))}"
            )
        return {
            "name": LINT_REQUIRE_CHARGE_AND_SU2,
            "passed": False,
            "detail": "; ".join(detail_parts),
        }

    return {
        "name": LINT_REQUIRE_CHARGE_AND_SU2,
        "passed": True,
        "detail": "U(1)_X charge sums are zero and SU(2) doublet Yukawas include epsilon",
    }
