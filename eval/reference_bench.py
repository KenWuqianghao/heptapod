"""
# reference_bench.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Benchmark an agent-generated FeynRules .fr against a physicist's REFERENCE .fr
(e.g. from the FeynRules model database), scoring EXTRACTION FIDELITY.

Both files are read with the same tools.frgen.fr_parser, then compared on a
NAME-INDEPENDENT physics signature — physicists name fields idiosyncratically
(S1m13hat, Sk, six1), so matching on names would be meaningless. We match new
fields on (spin, colour rep, the quantum number they carry) and report:

  * new-field count (reference vs generated) — a completeness proxy;
  * field-signature precision / recall / F1 (the headline fidelity number);
  * quantum-number-value overlap (looser: ignores the Q-vs-Y labelling that
    differs between gauge- and mass-eigenstate conventions);
  * parameter-name Jaccard overlap — a rough coupling-structure proxy.

This does NOT compile the .fr (that needs Mathematica/FeynRules); it measures
whether the automated extraction recovered the right physics content, which is
exactly what a licence-free machine can check against the reference.
"""

from __future__ import annotations

import sys
from collections import Counter
from typing import Any, Dict, List

sys.path.insert(0, __file__.rsplit("/eval/", 1)[0])

from tools.frgen.fr_parser import parse_fr_file  # noqa: E402


# Colour-rep dimension inferred from the FeynRules index a field carries.
_COLOUR_INDEX = {"Colour": "triplet", "Sextet": "sextet", "Gluon": "octet"}
_SU2_INDEX = {"SU2D": "doublet", "SU2L": "doublet", "SU2W": "triplet"}


def _colour_rep(indices: str) -> str:
    for idx, rep in _COLOUR_INDEX.items():
        if idx in (indices or ""):
            return rep
    return "singlet"


def _su2_rep(indices: str) -> str:
    for idx, rep in _SU2_INDEX.items():
        if idx in (indices or ""):
            return rep
    return "singlet"


def _spin(label: str) -> str:
    # label like "S[100]" / "F[7]" / "V[4]" — first char is the FeynRules spin class.
    return (label or "?")[:1] or "?"


def field_records(parsed: Dict[str, Any]) -> List[Dict[str, Any]]:
    """One normalized record per particle class."""
    recs = []
    for c in parsed.get("classes", []):
        qn = c.get("quantum_numbers") or {}
        recs.append({
            "name": c.get("class_name"),
            "spin": _spin(c.get("label", "")),
            "colour": _colour_rep(c.get("indices", "")),
            "su2": _su2_rep(c.get("indices", "")),
            "Q": str(qn["Q"]) if "Q" in qn else None,
            "Y": str(qn["Y"]) if "Y" in qn else None,
        })
    return recs


def _field_sig(r: Dict[str, Any]) -> tuple:
    """Strict signature: spin + colour + the quantum number the field carries.

    An explicit Q=0/Y=0 and an absent quantum-number entry both mean "neutral" —
    normalize them to the same tag so e.g. a singlet scalar written with
    ``QuantumNumbers -> {Q -> 0}`` matches one written with no QuantumNumbers.
    """
    q, y = r["Q"], r["Y"]
    if q not in (None, "0"):
        qn = ("Q", q)
    elif y not in (None, "0"):
        qn = ("Y", y)
    else:
        qn = ("neutral", "0")
    return (r["spin"], r["colour"], qn)


def _qn_values(recs: List[Dict[str, Any]]) -> Counter:
    """Loose: multiset of quantum-number *values* (Q or Y), colour-tagged, ignoring
    the Q-vs-Y label so a gauge eigenstate (Y) can still overlap a charge one."""
    c: Counter = Counter()
    for r in recs:
        v = r["Q"] if r["Q"] is not None else r["Y"]
        if v is not None:
            c[(r["colour"], v)] += 1
        else:
            c[(r["colour"], "0")] += 1
    return c


def _prf(produced: Counter, reference: Counter) -> Dict[str, float]:
    tp = sum((produced & reference).values())
    p = tp / sum(produced.values()) if sum(produced.values()) else 0.0
    r = tp / sum(reference.values()) if sum(reference.values()) else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return {"precision": round(p, 3), "recall": round(r, 3), "f1": round(f1, 3), "matched": tp}


def sm_baseline_sigs(sm_fr: str) -> Counter:
    """Field-signature multiset of the plain SM, for subtraction from
    standalone-style references that embed the full SM field content."""
    return Counter(_field_sig(r) for r in field_records(parse_fr_file(sm_fr)))


def score(generated_fr: str, reference_fr: str,
          sm_fr: str | None = None) -> Dict[str, Any]:
    """Score generated vs reference. If ``sm_fr`` is given, the SM's field
    signatures are multiset-subtracted from BOTH sides, so standalone
    references (which re-declare every SM field) are scored only on their
    genuinely new physics content."""
    gen = parse_fr_file(generated_fr)
    ref = parse_fr_file(reference_fr)
    grecs, rrecs = field_records(gen), field_records(ref)

    gsigs = Counter(_field_sig(r) for r in grecs)
    rsigs = Counter(_field_sig(r) for r in rrecs)
    gqn, rqn = _qn_values(grecs), _qn_values(rrecs)
    sm_subtracted = False
    if sm_fr:
        base = sm_baseline_sigs(sm_fr)
        qbase = _qn_values(field_records(parse_fr_file(sm_fr)))
        # Subtract the SM baseline PER SIDE, and only from a side that is
        # standalone-style (embeds the SM: >=10 shared signatures, which can't
        # happen by accident). An add-on side must NOT be subtracted — its
        # Z'/heavy-neutrino/mirror-fermion fields legitimately share SM
        # signatures and would be wrongly deleted. Typical case: standalone
        # reference (subtract) vs add-on generated model (keep everything).
        if sum((rsigs & base).values()) >= 10:
            sm_subtracted = True
            rsigs, rqn = rsigs - base, rqn - qbase
        if sum((gsigs & base).values()) >= 10:
            gsigs, gqn = gsigs - base, gqn - qbase

    field_prf = _prf(gsigs, rsigs)
    qn_prf = _prf(gqn, rqn)

    gp = {p["name"] for p in gen.get("parameters", [])}
    rp = {p["name"] for p in ref.get("parameters", [])}
    jacc = len(gp & rp) / len(gp | rp) if (gp | rp) else 0.0

    return {
        "reference_model": ref.get("model_name"),
        "generated_model": gen.get("model_name"),
        "sm_subtracted": sm_subtracted,
        "n_fields": {"reference": sum(rsigs.values()), "generated": sum(gsigs.values()),
                     "reference_raw": len(rrecs), "generated_raw": len(grecs)},
        "field_signature": field_prf,            # headline (strict, name-independent)
        "quantum_number_values": qn_prf,          # looser (ignores Q vs Y labelling)
        "n_parameters": {"reference": len(rp), "generated": len(gp)},
        "parameter_name_jaccard": round(jacc, 3),
        "reference_field_signatures": sorted(map(list, rsigs.elements())),
        "generated_field_signatures": sorted(map(list, gsigs.elements())),
    }


if __name__ == "__main__":
    import json
    if len(sys.argv) != 3:
        print("usage: python -m eval.reference_bench <generated.fr> <reference.fr>")
        raise SystemExit(2)
    print(json.dumps(score(sys.argv[1], sys.argv[2]), indent=2))
