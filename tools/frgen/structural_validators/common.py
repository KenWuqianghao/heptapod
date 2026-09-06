"""Shared helpers for pure-Python structural validators."""

from __future__ import annotations

import math
import re
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Optional, Sequence, Set

from ..frmodel import FeynRulesModel, MassSpec, ParticleClass, SpinType

_TOKEN_RE_TEMPLATE = r"(?<![A-Za-z0-9$]){name}(?![A-Za-z0-9$])"

_SPIN_DIMENSIONS = {
    SpinType.S: 1.0,
    SpinType.V: 1.0,
    SpinType.U: 1.0,
    SpinType.T: 1.0,
    SpinType.F: 1.5,
    SpinType.W: 1.5,
    SpinType.R: 1.5,
    SpinType.RW: 1.5,
}

_LAMBDA_TOKEN_RE = r"(?:\\?Lambda|lambda)"


def references(text: str, name: str) -> bool:
    """True when ``name`` appears in ``text`` as a full token."""
    if not text or not name:
        return False
    pattern = _TOKEN_RE_TEMPLATE.format(name=re.escape(name))
    return re.search(pattern, text) is not None


def count_references(text: str, name: str) -> int:
    """Count full-token references of ``name`` in ``text``."""
    if not text or not name:
        return 0
    pattern = _TOKEN_RE_TEMPLATE.format(name=re.escape(name))
    return len(re.findall(pattern, text))


def particle_symbols(particle: ParticleClass) -> list[str]:
    """Field symbols declared by one particle class."""
    symbols = [particle.class_name]
    symbols.extend(member for member in (particle.class_members or []) if member)
    return [symbol for symbol in symbols if symbol]


def model_field_dimensions(model: FeynRulesModel) -> Dict[str, float]:
    """Map field symbols to canonical mass dimension."""
    dims: Dict[str, float] = {}
    for particle in model.particles:
        dim = _SPIN_DIMENSIONS.get(particle.spin_type)
        if dim is None:
            continue
        for symbol in particle_symbols(particle):
            dims[symbol] = dim
    return dims


def all_field_symbols(model: FeynRulesModel) -> Set[str]:
    symbols: Set[str] = set()
    for particle in model.particles:
        symbols.update(particle_symbols(particle))
    return symbols


def mass_symbols(spec: Optional[MassSpec]) -> Set[str]:
    """Mass parameter symbols referenced by one MassSpec."""
    if spec is None or spec.massless:
        return set()
    symbols: Set[str] = set()
    if spec.sym:
        symbols.add(spec.sym)
    for sub, _ in spec.members:
        if sub:
            symbols.add(sub)
    return symbols


def flatten_mass_symbols(particle: ParticleClass) -> Set[str]:
    """Mass symbols for one particle class, including member masses."""
    return mass_symbols(particle.mass)


def parse_charge(value: str) -> Optional[Fraction]:
    """Parse a charge string like ``-1/3`` or ``0.5``."""
    text = str(value).strip()
    if not text:
        return None
    if "/" in text and "*" not in text and "^" not in text:
        left, right = text.split("/", 1)
        try:
            return Fraction(int(left.strip()), int(right.strip()))
        except ValueError:
            return None
    try:
        return Fraction(text)
    except ValueError:
        try:
            return Fraction(str(float(text)))
        except ValueError:
            return None


def ceil_nonnegative(value: float) -> int:
    """Ceiling for non-negative values with floating noise guard."""
    if value <= 0:
        return 0
    return int(math.ceil(value - 1e-12))


def lambda_suppression_power(expression: str) -> int:
    """Estimate total ``1/Lambda^n`` suppression power in an expression."""
    if not expression:
        return 0
    text = expression
    total = 0
    total += sum(
        int(m.group(1))
        for m in re.finditer(
            rf"/\s*\(\s*{_LAMBDA_TOKEN_RE}\s*\^\s*(\d+)\s*\)",
            text,
            flags=re.IGNORECASE,
        )
    )
    total += sum(
        int(m.group(1) or 1)
        for m in re.finditer(
            rf"/\s*{_LAMBDA_TOKEN_RE}(?:\s*\^\s*(\d+))?",
            text,
            flags=re.IGNORECASE,
        )
    )
    total += len(
        re.findall(
            rf"/\s*\(\s*{_LAMBDA_TOKEN_RE}\s*\)",
            text,
            flags=re.IGNORECASE,
        )
    )
    total += sum(
        int(m.group(1))
        for m in re.finditer(
            rf"{_LAMBDA_TOKEN_RE}\s*\^\s*-\s*(\d+)",
            text,
            flags=re.IGNORECASE,
        )
    )
    return total


def field_symbols_with_property(
    model: FeynRulesModel,
    predicate,
) -> Set[str]:
    """Collect field symbols for particles that match a predicate."""
    symbols: Set[str] = set()
    for particle in model.particles:
        if predicate(particle):
            symbols.update(particle_symbols(particle))
    return symbols


def term_references_any(term_expression: str, names: Sequence[str]) -> bool:
    """True if a term expression references any name in ``names``."""
    return any(references(term_expression, name) for name in names)


def charge_keys_for_u1x(particles: Iterable[ParticleClass]) -> Set[str]:
    """Detect likely U(1)_X charge keys in QuantumNumbers."""
    keys: Set[str] = set()
    for particle in particles:
        for key in (particle.quantum_numbers or {}):
            lowered = key.lower()
            if lowered in {"x", "qx", "u1x"}:
                keys.add(key)
            elif "u1" in lowered and "x" in lowered:
                keys.add(key)
    return keys
