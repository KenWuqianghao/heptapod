"""
# scoring.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Deterministic scoring for the Lagrangian-extraction benchmark.

Given a produced FeynRulesModel (as a dict) and an expected spec, compute how
well extraction recovered the model's particle content, quantum numbers, and
parameters. Pure functions, unit-tested offline and independent of any LLM.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional


def _as_fraction(value: Optional[str]) -> Optional[Fraction]:
    """Parse a rational/int charge string ("-1/3", "2/3", "-1") to a Fraction."""
    if value is None:
        return None
    try:
        return Fraction(str(value).strip())
    except (ValueError, ZeroDivisionError):
        return None


def _physical_particles(model: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [p for p in model.get("particles", []) if not p.get("unphysical")]


def _particle_names(p: Dict[str, Any]) -> List[str]:
    names: List[str] = []
    for key in ("class_name", "particle_name", "antiparticle_name", "full_name"):
        v = p.get(key)
        if isinstance(v, str) and v:
            names.append(v.lower())
        elif isinstance(v, list):
            names.extend(str(x).lower() for x in v if x)
    return names


def score_particles(produced: Dict[str, Any], expected: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Match expected particles against produced; score recall + charge accuracy."""
    prod = _physical_particles(produced)
    prod_name_index = [(_particle_names(p), p) for p in prod]

    matched = 0
    charge_checked = 0
    charge_ok = 0
    pdg_checked = 0
    pdg_ok = 0
    missing: List[str] = []

    for exp in expected:
        exp_name = str(exp.get("name", "")).lower()
        hit = next((p for names, p in prod_name_index if exp_name and exp_name in names), None)
        if hit is None:
            missing.append(exp.get("name", ""))
            continue
        matched += 1
        if "charge" in exp:
            charge_checked += 1
            got = _as_fraction((hit.get("quantum_numbers") or {}).get("Q"))
            want = _as_fraction(exp["charge"])
            if got is not None and want is not None and got == want:
                charge_ok += 1
        if "pdg" in exp:
            pdg_checked += 1
            got_pdg = hit.get("pdg")
            if isinstance(got_pdg, list):
                pdg_ok += 1 if exp["pdg"] in got_pdg else 0
            else:
                pdg_ok += 1 if got_pdg == exp["pdg"] else 0

    n_exp = len(expected)
    return {
        "expected": n_exp,
        "produced": len(prod),
        "matched": matched,
        "recall": (matched / n_exp) if n_exp else 0.0,
        "precision": (matched / len(prod)) if prod else 0.0,
        "charge_accuracy": (charge_ok / charge_checked) if charge_checked else None,
        "pdg_accuracy": (pdg_ok / pdg_checked) if pdg_checked else None,
        "missing": [m for m in missing if m],
    }


def score_parameters(produced: Dict[str, Any], expected_names: List[str]) -> Dict[str, Any]:
    """Recall of expected parameter names among produced parameters."""
    prod_names = {str(p.get("name", "")).lower() for p in produced.get("parameters", [])}
    matched = sum(1 for n in expected_names if n.lower() in prod_names)
    n = len(expected_names)
    return {
        "expected": n,
        "produced": len(prod_names),
        "matched": matched,
        "recall": (matched / n) if n else 0.0,
        "missing": [n2 for n2 in expected_names if n2.lower() not in prod_names],
    }


def score_case(produced_model: Dict[str, Any], expected: Dict[str, Any]) -> Dict[str, Any]:
    """Combine particle + parameter scores for one benchmark case."""
    parts = score_particles(produced_model, expected.get("particles", []))
    params = score_parameters(produced_model, expected.get("parameters", []))
    # Headline extraction score: mean of particle recall and (when checked) charge accuracy.
    components = [parts["recall"]]
    if parts["charge_accuracy"] is not None:
        components.append(parts["charge_accuracy"])
    if params["expected"]:
        components.append(params["recall"])
    extraction_score = sum(components) / len(components) if components else 0.0
    return {
        "particles": parts,
        "parameters": params,
        "extraction_score": extraction_score,
    }


def aggregate(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Aggregate per-case results into headline benchmark metrics."""
    n = len(results)
    if n == 0:
        return {"n_cases": 0}
    extracted = [r for r in results if r.get("extracted")]
    validated = sum(1 for r in results if r.get("validated"))
    generated = sum(1 for r in results if r.get("generated"))
    scores = [r["score"]["extraction_score"] for r in results if r.get("score")]
    part_recall = [
        r["score"]["particles"]["recall"] for r in results if r.get("score")
    ]
    return {
        "n_cases": n,
        "extraction_rate": len(extracted) / n,
        "generation_rate": generated / n,
        "validation_pass_rate": validated / n,
        "mean_extraction_score": (sum(scores) / len(scores)) if scores else 0.0,
        "mean_particle_recall": (sum(part_recall) / len(part_recall)) if part_recall else 0.0,
    }
