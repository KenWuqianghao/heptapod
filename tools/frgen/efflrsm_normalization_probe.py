"""Pure-Python Eq.8 normalization probe for EffLRSM Z_R couplings."""

from __future__ import annotations

import ast
import math
import re
from dataclasses import dataclass
from typing import Mapping

DEFAULT_KAPPA_R = 1.0
DEFAULT_SW2 = 0.2312
DEFAULT_TOLERANCE = 1e-6


class NormalizationProbeError(ValueError):
    """Raised when crosscheck agrees on a shared normalization error."""


@dataclass(frozen=True)
class NormalizationProbeResult:
    extracted_factor: float
    reference_factor: float
    ratio: float
    rate_ratio: float

def _to_python_expr(expr: str) -> str:
    converted = expr.strip().replace("^", "**")
    converted = re.sub(r"\bSqrt\s*\[", "sqrt(", converted)
    converted = converted.replace("[", "(").replace("]", ")")
    return converted

def _eval_ast(node: ast.AST, values: Mapping[str, float]) -> float:
    if isinstance(node, ast.Expression):
        return _eval_ast(node.body, values)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ValueError(f"Unsupported literal: {node.value!r}")
    if isinstance(node, ast.Name):
        if node.id in values:
            return float(values[node.id])
        raise ValueError(f"Unknown symbol: {node.id}")
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_ast(node.operand, values)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp):
        left = _eval_ast(node.left, values)
        right = _eval_ast(node.right, values)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            return left**right
        raise ValueError("Unsupported binary operator")
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id != "sqrt":
            raise ValueError("Only Sqrt is supported")
        if len(node.args) != 1:
            raise ValueError("Sqrt requires one argument")
        return math.sqrt(_eval_ast(node.args[0], values))
    raise ValueError("Unsupported expression node")


def evaluate_expr(expr: str, values: Mapping[str, float]) -> float:
    parsed = ast.parse(_to_python_expr(expr), mode="eval")
    return _eval_ast(parsed, values)

def _close(a: float, b: float, tolerance: float) -> bool:
    scale = max(1.0, abs(a), abs(b))
    return abs(a - b) <= tolerance * scale

def _normalization_factor(
    coupling_expr: str,
    *,
    kappa_symbol: str,
    kappa_r: float = DEFAULT_KAPPA_R,
    sw2: float = DEFAULT_SW2,
    ee: float = 1.0,
) -> float:
    sw = math.sqrt(sw2)
    cw = math.sqrt(1.0 - sw2)
    values = {
        "sw": sw,
        "cw": cw,
        "ee": ee,
        "kRquark": kappa_r,
        "kRlepton": kappa_r,
        "kRq": kappa_r,
        "kRl": kappa_r,
        "kappa_R": kappa_r,
        "kappaR": kappa_r,
    }
    extracted = abs(evaluate_expr(coupling_expr, values))
    baseline = abs(evaluate_expr(f"{kappa_symbol}*ee/sw", values))
    if baseline == 0.0:
        raise ValueError("Baseline normalization is zero")
    return extracted / baseline


def probe_normalization_ratio(
    extracted_expr: str,
    reference_expr: str,
    *,
    kappa_symbol: str,
) -> NormalizationProbeResult:
    extracted_factor = _normalization_factor(extracted_expr, kappa_symbol=kappa_symbol)
    reference_factor = _normalization_factor(reference_expr, kappa_symbol=kappa_symbol)
    ratio = extracted_factor / reference_factor
    rate_ratio = ratio * ratio
    return NormalizationProbeResult(
        extracted_factor=extracted_factor,
        reference_factor=reference_factor,
        ratio=ratio,
        rate_ratio=rate_ratio,
    )


def enforce_crosscheck_precheck(
    extracted_expr: str,
    crosscheck_expr: str,
    reference_expr: str,
    *,
    kappa_symbol: str,
    tolerance: float = DEFAULT_TOLERANCE,
) -> NormalizationProbeResult:
    extracted_vs_ref = probe_normalization_ratio(
        extracted_expr,
        reference_expr,
        kappa_symbol=kappa_symbol,
    )
    crosscheck_factor = _normalization_factor(
        crosscheck_expr,
        kappa_symbol=kappa_symbol,
    )
    extracted_factor = extracted_vs_ref.extracted_factor
    if _close(extracted_factor, crosscheck_factor, tolerance) and not _close(
        extracted_factor, extracted_vs_ref.reference_factor, tolerance
    ):
        raise NormalizationProbeError(
            "Crosscheck must fail: extraction and crosscheck agree with each other "
            "but disagree with Eq.8 reference normalization."
        )
    return extracted_vs_ref


def enforce_efflrsm_precheck(
    extracted_couplings: Mapping[str, str],
    crosscheck_couplings: Mapping[str, str],
    reference_couplings: Mapping[str, str],
    *,
    tolerance: float = DEFAULT_TOLERANCE,
) -> dict[str, NormalizationProbeResult]:
    required = ("gZRq", "gZRl")
    for name in required:
        if name not in extracted_couplings:
            raise KeyError(f"Missing extracted coupling: {name}")
        if name not in crosscheck_couplings:
            raise KeyError(f"Missing crosscheck coupling: {name}")
        if name not in reference_couplings:
            raise KeyError(f"Missing reference coupling: {name}")
    return {
        "gZRq": enforce_crosscheck_precheck(
            extracted_couplings["gZRq"],
            crosscheck_couplings["gZRq"],
            reference_couplings["gZRq"],
            kappa_symbol="kRquark",
            tolerance=tolerance,
        ),
        "gZRl": enforce_crosscheck_precheck(
            extracted_couplings["gZRl"],
            crosscheck_couplings["gZRl"],
            reference_couplings["gZRl"],
            kappa_symbol="kRlepton",
            tolerance=tolerance,
        ),
    }
