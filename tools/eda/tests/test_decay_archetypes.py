"""
# test_decay_archetypes.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Every dim-4 two-body decay archetype, against a literature-anchored width.

There are exactly TEN renormalisable 1 -> 2 archetypes: the six valid
3-point vertices (SSS, SFF, SVV, VFF, VVV, SSV) with each leg in turn as
the parent. Until this file existed the decay path had never been swept:
five of the ten had never been checked against anything, and one of those
five -- S -> S' V -- returned identically ZERO, because its vertex used
the momenta as drawn and (p - p_scalar) is the vector's own momentum, so
it died against eps . p = 0.

Reference widths are the ground truth of hepbench's `symbolic` family,
each derived from the cited literature and independently gated there
against explicit-spinor numerics. They are embedded as constants rather
than read from a hepbench checkout, so this suite stands alone.

The V -> V V' entry is DELIBERATELY NOT hepbench's committed value: that
one is built from the as-drawn triple-gauge momenta and is wrong at
finite masses (see scattering.VVV_CONVENTION_NOTE). It is anchored to the
standard Z' -> W+W- width instead.

Needs wolframscript; each case is a Mathematica round trip.
"""

import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from tools.eda.feyncalc_codegen import SymbolicFeynCalcCodeGenerator
from tools.nda.symbolic_diagram import build_diagram_from_symbolic, parse_symbolic_diagram


def _wolframscript():
    for cand in (os.environ.get("WOLFRAMSCRIPT_PATH"),
                 "/Applications/Mathematica.app/Contents/MacOS/wolframscript",
                 shutil.which("wolframscript")):
        if cand and Path(cand).exists():
            return cand
    return None


def _zprime_width(g, mV, m):
    """Standard heavy-vector -> V V width, equal daughter masses."""
    x = m * m / (mV * mV)
    return (g * g / (192 * math.pi)) * mV * (mV / m) ** 4 \
        * (1 - 4 * x) ** 1.5 * (1 + 20 * x + 12 * x * x)


# archetype -> (spec, substitutions, reference width, provenance)
ARCHETYPES = {
    "S -> f fbar": (
        dict(initial=[{"label": "S", "spin": 0, "mass": 1240.0}],
             final=[{"label": "f", "spin": 0.5, "mass": 320.0},
                    {"label": "fbar", "spin": 0.5, "mass": 320.0}],
             vertices=[{"type": "yukawa", "coupling": "y"}]),
        "mS->1240, mf->320, mfbar->320, y->0.87",
        23.464911722945107, "Djouadi hep-ph/0503172 sec 2.3 (beta^3)"),
    "S -> S S": (
        dict(initial=[{"label": "S", "spin": 0, "mass": 950.0}],
             final=[{"label": "Sa", "spin": 0, "mass": 350.0},
                    {"label": "Sb", "spin": 0, "mass": 410.0}],
             vertices=[{"type": "sss", "coupling": "mu"}]),
        "mS->950, mSa->350, mSb->410, mu->315",
        1.2442595485743093, "PDG Kinematics review eq. 50.18"),
    "F -> f S": (
        dict(initial=[{"label": "F", "spin": 0.5, "mass": 880.0}],
             final=[{"label": "f", "spin": 0.5, "mass": 130.0},
                    {"label": "S", "spin": 0, "mass": 340.0}],
             vertices=[{"type": "yukawa", "coupling": "y"}]),
        "mF->880, mf->130, mS->340, y->0.66",
        7.312873036225345, "Djouadi hep-ph/0503173 sec 1.3.4 (t -> b H+)"),
    "V -> f fbar": (
        dict(initial=[{"label": "V", "spin": 1, "mass": 2150.0}],
             final=[{"label": "f", "spin": 0.5, "mass": 640.0},
                    {"label": "fbar", "spin": 0.5, "mass": 640.0}],
             vertices=[{"type": "vector", "coupling": "g"}]),
        "mV->2150, mf->640, mfbar->640, g->0.47",
        11.915957872612209, "Barger & Phillips, Collider Physics"),
    "F -> f V": (
        dict(initial=[{"label": "F", "spin": 0.5, "mass": 900.0}],
             final=[{"label": "f", "spin": 0.5, "mass": 180.0},
                    {"label": "V", "spin": 1, "mass": 240.0}],
             vertices=[{"type": "vector", "coupling": "g"}]),
        "mF->900, mf->180, mV->240, g->0.74",
        109.51948309493523, "Denner, Fortsch.Phys. 41 (1993) 307"),
    "S -> V V": (
        dict(initial=[{"label": "S", "spin": 0, "mass": 400.0}],
             final=[{"label": "Va", "spin": 1, "mass": 90.0},
                    {"label": "Vb", "spin": 1, "mass": 150.0}],
             vertices=[{"type": "svv", "coupling": "g"}]),
        "mS->400, mVa->90, mVb->150, g->110",
        11.885133513029855, "Djouadi hep-ph/0503172 sec 2.2 (1-4x+12x^2)"),
    "V -> S S": (
        dict(initial=[{"label": "V", "spin": 1, "mass": 500.0}],
             final=[{"label": "Sa", "spin": 0, "mass": 120.0},
                    {"label": "Sb", "spin": 0, "mass": 210.0}],
             vertices=[{"type": "ssv", "coupling": "g"}]),
        "mV->500, mSa->120, mSb->210, g->0.85",
        0.9668097975501307, "Schwartz scalar-QED vertex; Sakurai rho -> pi pi"),
    "S -> S' V": (
        dict(initial=[{"label": "S", "spin": 0, "mass": 600.0}],
             final=[{"label": "Sp", "spin": 0, "mass": 140.0},
                    {"label": "V", "spin": 1, "mass": 250.0}],
             vertices=[{"type": "ssv", "coupling": "g"}]),
        "mS->600, mSp->140, mV->250, g->0.9",
        23.219067397452875, "Schwartz, scalar-QED emission vertex"),
    "V -> S V'": (
        dict(initial=[{"label": "V", "spin": 1, "mass": 700.0}],
             final=[{"label": "S", "spin": 0, "mass": 160.0},
                    {"label": "Vp", "spin": 1, "mass": 250.0}],
             vertices=[{"type": "svv", "coupling": "g"}]),
        "mV->700, mS->160, mVp->250, g->180",
        1.0525716496014468, "Djouadi hep-ph/0503172, 0503173"),
    "V -> V V'": (
        dict(initial=[{"label": "V", "spin": 1, "mass": 900.0}],
             final=[{"label": "Va", "spin": 1, "mass": 200.0},
                    {"label": "Vb", "spin": 1, "mass": 200.0}],
             vertices=[{"type": "vvv", "coupling": "g"}]),
        "mV->900, mVa->200, mVb->200, g->0.8",
        _zprime_width(0.8, 900.0, 200.0),
        "Z' -> W+W- standard form (NOT hepbench's as-drawn value)"),
}


def main():
    ws = _wolframscript()
    if not ws:
        print("[-] SKIP: wolframscript not found")
        return 0

    print("=" * 78)
    print("Every dim-4 two-body decay archetype vs a literature-anchored width")
    print("=" * 78)
    gen = SymbolicFeynCalcCodeGenerator()
    all_passed = True

    for name, (spec, subs, ref, cite) in ARCHETYPES.items():
        d = build_diagram_from_symbolic(parse_symbolic_diagram(spec))
        r = gen.generate(d)
        if not r.code:
            print(f"  [x] FAIL: {name}: no code ({r.warnings})")
            all_passed = False
            continue
        code = r.code + f'\nw = N[width /. {{{subs}}}];\nPrint["W: ", Re[w]];\n'
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "d.wl"
            f.write_text(code)
            out = subprocess.run([ws, "-file", str(f)], capture_output=True,
                                 text=True, timeout=1800).stdout
        got = None
        for line in out.splitlines():
            if line.startswith("W: "):
                try:
                    got = float(line[3:].strip().replace("*^", "e"))
                except ValueError:
                    got = None
        if got is None:
            print(f"  [x] FAIL: {name}: no number returned")
            all_passed = False
            continue
        rel = abs(got - ref) / abs(ref) if ref else abs(got)
        ok = rel < 1e-10
        all_passed = all_passed and ok
        print(f"  {'[v] PASS' if ok else '[x] FAIL'}: {name:<12} "
              f"{got:>22.12f} vs {ref:>22.12f}  rel {rel:.1e}")
        print(f"           {cite}")

    print()
    print(f"Total: {'all 10 archetypes anchored' if all_passed else 'FAILURES PRESENT'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
