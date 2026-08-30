"""
# test_scattering.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Tests for the 2->2 scattering builder.

Three layers, cheapest first:
  1. convention self-tests for the numeric harness itself;
  2. a STRUCTURAL sweep over every allowed 2->2 topology -- each must
     either generate code or refuse with a reason, never crash and never
     emit a structurally empty amplitude;
  3. a NUMERIC cross-check of the generated FeynCalc against the
     independent harness in numeric_2to2.py.  Requires wolframscript and
     is skipped without it (each case costs a Mathematica start-up).

Run the slow layer explicitly:  python test_scattering.py --numeric
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from tools.eda.feyncalc_codegen import SymbolicFeynCalcCodeGenerator, ProcessType
from tools.eda.scattering import (
    CHANNEL_PAIRING,
    Channel,
    UnsupportedScattering,
    allowed_contact_structures,
    allowed_exchange_structures,
    build_amplitude_sum,
    cross_section_block,
    kinematics_block,
)
from tools.nda.symbolic_diagram import build_diagram_from_symbolic, parse_symbolic_diagram
from tools.eda.tests import numeric_2to2 as NUM

SPIN_NAME = {0.0: "S", 0.5: "F", 1.0: "V"}
LEG_INCOMING = (True, True, False, False)


def _wolframscript():
    for cand in (os.environ.get("WOLFRAMSCRIPT_PATH"),
                 "/Applications/Mathematica.app/Contents/MacOS/wolframscript",
                 shutil.which("wolframscript")):
        if cand and Path(cand).exists():
            return cand
    return None


# ---------------------------------------------------------------------------
# Diagram construction for the sweep
# ---------------------------------------------------------------------------

def _label_legs(ext, channel):
    """Label legs so every fermion bilinear has one barred and one unbarred end."""
    labels = [None] * 4
    pairs = [(0, 1), (2, 3)] if channel is Channel.CONTACT else list(CHANNEL_PAIRING[channel])
    used = 0
    base = "abcd"
    for i, j in pairs:
        pair_f = [k for k in (i, j) if ext[k] == 0.5]
        if len(pair_f) == 2:
            a, b = pair_f
            nm = f"f{base[used]}"
            used += 1
            if LEG_INCOMING[a] == LEG_INCOMING[b]:
                labels[a], labels[b] = nm, nm + "bar"   # pair created / annihilated
            else:
                labels[a] = labels[b] = nm              # line passing through
    ferm = [i for i, s in enumerate(ext) if s == 0.5]
    if len(ferm) == 2 and all(labels[k] is None for k in ferm):
        a, b = ferm
        if LEG_INCOMING[a] == LEG_INCOMING[b]:
            labels[a], labels[b] = "fa", "fabar"
        else:
            labels[a] = labels[b] = "fa"
    for i, s in enumerate(ext):
        if labels[i] is None:
            labels[i] = f"{SPIN_NAME[s].lower()}{base[i]}"
    return labels


def _vtype(spins):
    ms = sorted(spins)
    if ms == [0.0, 0.5, 0.5]:
        return "yukawa"
    if ms == [0.5, 0.5, 1.0]:
        return "vector"
    return "generic"


def _make_diagram(ext, channel, med):
    labels = _label_legs(ext, channel)
    spec = {
        "initial": [{"label": labels[i], "spin": ext[i]} for i in (0, 1)],
        "final": [{"label": labels[i], "spin": ext[i]} for i in (2, 3)],
    }
    if channel is Channel.CONTACT:
        spec["vertices"] = [{
            "type": "vector" if sorted(ext) == [0.5] * 4 else "contact",
            "coupling": "g",
        }]
    else:
        (a, b), (c, d) = CHANNEL_PAIRING[channel]
        spec["propagators"] = [{"label": "P", "spin": med}]
        spec["vertices"] = [
            {"type": _vtype([ext[a], ext[b], med]), "coupling": "g1"},
            {"type": _vtype([ext[c], ext[d], med]), "coupling": "g2"},
        ]
    return build_diagram_from_symbolic(parse_symbolic_diagram(spec))


# ---------------------------------------------------------------------------
# Layer 1 — harness conventions
# ---------------------------------------------------------------------------

def test_harness_conventions():
    print("=" * 60)
    print("Numeric harness conventions")
    print("=" * 60)
    fails = NUM.check_conventions()
    for f in fails:
        print(f"  [x] FAIL: {f}")
    ok = not fails
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: spinor / polarisation identities")
    print()
    return ok


# ---------------------------------------------------------------------------
# Layer 2 — structural sweep
# ---------------------------------------------------------------------------

def test_structural_sweep():
    print("=" * 60)
    print("Structural sweep over every allowed 2->2 topology")
    print("=" * 60)
    targets = [(ext, Channel[ch], med) for ext, ch, med in allowed_exchange_structures()]
    targets += [(ext, Channel.CONTACT, None) for ext in allowed_contact_structures()]

    generated, refused, crashed = 0, [], []
    for ext, channel, med in targets:
        try:
            d = _make_diagram(ext, channel, med)
            gen = SymbolicFeynCalcCodeGenerator(
                channel=None if channel is Channel.CONTACT else channel.name.lower())
            r = gen.generate(d)
            if r.code:
                generated += 1
                # a structurally empty amplitude is the failure mode this
                # whole module exists to prevent
                if "FAD[" in r.code:
                    crashed.append((ext, channel, "FAD leaked into a tree amplitude"))
                if "ChangeDimension" not in r.code:
                    crashed.append((ext, channel, "amplitude not normalised to 4 dims"))
            else:
                refused.append((ext, channel, r.warnings[0] if r.warnings else "?"))
        except Exception as exc:                     # noqa: BLE001
            crashed.append((ext, channel, f"{type(exc).__name__}: {exc}"))

    print(f"  structures swept : {len(targets)}")
    print(f"  generated code   : {generated}")
    print(f"  refused cleanly  : {len(refused)}")
    print(f"  crashed / bad    : {len(crashed)}")
    for ext, ch, why in refused:
        tag = "".join(SPIN_NAME[s] for s in ext)
        print(f"    refused {tag} {ch.name}: {why[:60]}")
    for ext, ch, why in crashed:
        tag = "".join(SPIN_NAME[s] for s in ext)
        print(f"    [x] {tag} {ch.name}: {why[:80]}")

    # Only the VVVV quartic is allowed to refuse: its colour structure is not
    # expressible in a spec carrying a single scalar colour_factor.
    ok = not crashed and len(refused) == 1
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: full coverage, no silent fallbacks")
    print()
    return ok


def test_unsupported_is_loud():
    print("=" * 60)
    print("Unsupported structures refuse rather than fake it")
    print("=" * 60)
    all_passed = True
    # (S, S, F) is not a valid vertex, so S F -> S F has no t-channel diagram.
    d = _make_diagram((0.0, 0.5, 0.0, 0.5), Channel.T, 0.5)
    r = SymbolicFeynCalcCodeGenerator(channel="t").generate(d)
    ok = (r.code == "" and r.process_type == ProcessType.UNSUPPORTED
          and bool(r.warnings))
    all_passed = all_passed and ok
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: impossible vertex refused with a reason")

    # An assumed channel must be recorded, never silent.
    d2 = _make_diagram((0.5, 0.5, 0.5, 0.5), Channel.S, 1.0)
    r2 = SymbolicFeynCalcCodeGenerator().generate(d2)
    ok = any("assumed" in w for w in r2.warnings)
    all_passed = all_passed and ok
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: an assumed channel is reported")
    print()
    return all_passed


# ---------------------------------------------------------------------------
# Layer 3 — numeric cross-check against the independent harness
# ---------------------------------------------------------------------------

NUMERIC_CASES = {
    "SF->SF, s-channel fermion exchange": dict(
        spec=dict(initial=[{"label": "sa", "spin": 0, "mass": 140.0},
                           {"label": "fa", "spin": 0.5, "mass": 35.0}],
                  final=[{"label": "sb", "spin": 0, "mass": 95.0},
                         {"label": "fb", "spin": 0.5, "mass": 60.0}],
                  propagators=[{"label": "Fm", "spin": 0.5, "mass": 300.0}],
                  vertices=[{"type": "yukawa", "coupling": "y1"},
                            {"type": "yukawa", "coupling": "y2"}]),
        channel="s", sqrt_s=700.0, n_init=2,
        subs="msa->140, mfa->35, msb->95, mfb->60, mProp0->300, y1->0.73, y2->0.41",
        masses=(140., 35., 95., 60.),
        fn=lambda ct: NUM.m2_sf_to_sf_fermion(0.73, 0.41, (140., 35., 95., 60.),
                                              300., 700.0 ** 2, ct)),
    "FV->FV, s-channel fermion exchange": dict(
        spec=dict(initial=[{"label": "fa", "spin": 0.5, "mass": 25.0},
                           {"label": "va", "spin": 1, "mass": 80.0}],
                  final=[{"label": "fb", "spin": 0.5, "mass": 45.0},
                         {"label": "vb", "spin": 1, "mass": 110.0}],
                  propagators=[{"label": "Fm", "spin": 0.5, "mass": 250.0}],
                  vertices=[{"type": "vector", "coupling": "g1"},
                            {"type": "vector", "coupling": "g2"}]),
        channel="s", sqrt_s=800.0, n_init=6,
        subs="mfa->25, mva->80, mfb->45, mvb->110, mProp0->250, g1->0.62, g2->0.37",
        masses=(25., 80., 45., 110.),
        fn=lambda ct: NUM.m2_fv_to_fv_fermion(0.62, 0.37, (25., 80., 45., 110.),
                                              250., 800.0 ** 2, ct)),
    "SS->VV, s-channel scalar exchange": dict(
        spec=dict(initial=[{"label": "sa", "spin": 0, "mass": 50.0},
                           {"label": "sb", "spin": 0, "mass": 70.0}],
                  final=[{"label": "va", "spin": 1, "mass": 90.0},
                         {"label": "vb", "spin": 1, "mass": 120.0}],
                  propagators=[{"label": "Sm", "spin": 0, "mass": 400.0}],
                  vertices=[{"type": "sss", "coupling": "g1"},
                            {"type": "svv", "coupling": "g2"}]),
        channel="s", sqrt_s=750.0, n_init=1,
        subs="msa->50, msb->70, mva->90, mvb->120, mProp0->400, g1->1.3, g2->0.85",
        masses=(50., 70., 90., 120.),
        fn=lambda ct: NUM.m2_ss_to_vv_scalar(1.3, 0.85, (50., 70., 90., 120.),
                                             400., 750.0 ** 2, ct)),
    "SS->SS, t-channel vector exchange": dict(
        spec=dict(initial=[{"label": "sa", "spin": 0, "mass": 40.0},
                           {"label": "sb", "spin": 0, "mass": 65.0}],
                  final=[{"label": "sa", "spin": 0, "mass": 40.0},
                         {"label": "sb", "spin": 0, "mass": 65.0}],
                  propagators=[{"label": "Vm", "spin": 1, "mass": 300.0}],
                  vertices=[{"type": "ssv", "coupling": "g1"},
                            {"type": "ssv", "coupling": "g2"}]),
        channel="t", sqrt_s=700.0, n_init=1,
        subs="msa->40, msb->65, mProp0->300, g1->0.9, g2->0.55",
        masses=(40., 65., 40., 65.),
        fn=lambda ct: NUM.m2_ss_to_ss_t_vector(0.9, 0.55, (40., 65., 40., 65.),
                                               300., 700.0 ** 2, ct)),
    "VV->VV, s-channel vector exchange": dict(
        spec=dict(initial=[{"label": "va", "spin": 1, "mass": 80.0},
                           {"label": "vb", "spin": 1, "mass": 95.0}],
                  final=[{"label": "vc", "spin": 1, "mass": 110.0},
                         {"label": "vd", "spin": 1, "mass": 70.0}],
                  propagators=[{"label": "Vm", "spin": 1, "mass": 260.0}],
                  vertices=[{"type": "vvv", "coupling": "g1"},
                            {"type": "vvv", "coupling": "g2"}]),
        channel="s", sqrt_s=900.0, n_init=9,
        subs="mva->80, mvb->95, mvc->110, mvd->70, mProp0->260, g1->0.7, g2->0.45",
        masses=(80., 95., 110., 70.),
        fn=lambda ct: NUM.m2_vv_to_vv_s_vector(0.7, 0.45, (80., 95., 110., 70.),
                                               260., 900.0 ** 2, ct)),
}


def _run_wl(ws, code, tag):
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / f"{tag}.wl"
        f.write_text(code)
        out = subprocess.run([ws, "-file", str(f)], capture_output=True,
                             text=True, timeout=1800).stdout
    def _grab(prefix):
        for line in out.splitlines():
            if line.startswith(prefix):
                try:
                    return float(line.split(prefix)[1].strip().replace("*^", "e"))
                except ValueError:
                    return None
        return None

    re_, im_ = _grab("XCHECK_RE:"), _grab("XCHECK_IM:")
    if re_ is None:
        return None
    # a spurious imaginary part means the amplitude, not the parser, is
    # wrong -- surface it rather than silently taking Re
    if im_ is not None and re_ and abs(im_) > 1e-10 * abs(re_):
        return None
    return re_


def test_numeric_crosscheck():
    print("=" * 60)
    print("Numeric cross-check: generated FeynCalc vs independent harness")
    print("=" * 60)
    ws = _wolframscript()
    if not ws:
        print("  [-] SKIP: wolframscript not found")
        print()
        return True

    all_passed = True
    for name, c in NUMERIC_CASES.items():
        d = build_diagram_from_symbolic(parse_symbolic_diagram(c["spec"]))
        r = SymbolicFeynCalcCodeGenerator(channel=c["channel"]).generate(d)
        if not r.code:
            print(f"  [x] FAIL: {name} refused: {r.warnings}")
            all_passed = False
            continue
        # A real cross section can come back as x + 0.*I from the symbolic
        # integration. Print Re and Im separately: Chop would be wrong here,
        # since a legitimately tiny sigma (1e-16 GeV^-2 is normal) sits below
        # its default tolerance and would be zeroed.
        code = r.code + (
            f'\nxch = N[sigma /. {{{c["subs"]}}} /. s -> ({c["sqrt_s"]})^2];\n'
            'Print["XCHECK_RE: ", Re[xch]];\n'
            'Print["XCHECK_IM: ", Im[xch]];\n'
        )
        fc = _run_wl(ws, code, name.split(",")[0].replace("->", "_to_"))
        s = c["sqrt_s"] ** 2
        ref = NUM.cross_section(lambda ct, c=c: c["fn"](ct) / c["n_init"], s, c["masses"])
        if fc is None:
            print(f"  [x] FAIL: {name}: FeynCalc produced no number")
            all_passed = False
            continue
        rel = abs(fc - ref) / abs(ref) if ref else abs(fc)
        ok = rel < 1e-8
        all_passed = all_passed and ok
        print(f"  {'[v] PASS' if ok else '[x] FAIL'}: {name}")
        print(f"        feyncalc {fc:.12e}   harness {ref:.12e}   rel {rel:.2e}")
    print()
    return all_passed


def test_literature_anchors():
    """Anchor the harness itself to published results, in their own conventions.

    Without this the harness only proves that two things the same author
    wrote agree with each other. These are external:
      * P&S eq. (5.13)  -- s-channel massless-vector annihilation;
      * P&S eq. (5.87)  -- Compton |M|^2, pointwise in the invariants;
      * Klein-Nishina   -- the Compton total cross section;
      * Thomson limit   -- sigma -> 8 pi r_e^2 / 3 as omega/m -> 0.
    Compton is the load-bearing one: it exercises the fermion-mediated
    threading, the VFF vertex normalisation, massless-photon polarisation
    sums, the u-channel and the coherent sum, all against a published
    formula.
    """
    import math

    print("=" * 60)
    print("Literature anchors for the numeric harness")
    print("=" * 60)
    all_passed = True

    alpha = 1 / 137.035999084
    e = math.sqrt(4 * math.pi * alpha)
    m = 0.51099895e-3

    # P&S (5.13)
    g, s = 0.55, 730.0 ** 2
    got = NUM.cross_section(
        lambda ct: NUM.m2_ffbar_to_ffbar_vector(g, g, (0, 0, 0, 0), 0.0, s, ct) / 4.0,
        s, (0, 0, 0, 0))
    ref = NUM.sigma_ps_5_13(g, s)
    ok = abs(got - ref) / ref < 1e-10
    all_passed = all_passed and ok
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: P&S (5.13)  "
          f"{got:.10e} vs {ref:.10e}")

    # P&S (5.87), pointwise
    worst = 0.0
    for x in (0.05, 0.5, 5.0):
        s = m * m * (1 + 2 * x)
        for ct in (-0.7, 0.0, 0.6):
            a = NUM.m2_compton(e, m, s, ct) / 4.0
            b = NUM.m2_compton_peskin_5_87(e, m, s, ct)
            worst = max(worst, abs(a - b) / abs(b))
    ok = worst < 1e-12
    all_passed = all_passed and ok
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: P&S (5.87) pointwise, "
          f"worst rel {worst:.2e}")

    # Klein-Nishina total cross section
    worst = 0.0
    for x in (0.05, 0.5, 5.0):
        s = m * m * (1 + 2 * x)
        got = NUM.cross_section(lambda ct, s=s: NUM.m2_compton(e, m, s, ct) / 4.0,
                                s, (m, 0.0, m, 0.0), n_points=600)
        worst = max(worst, abs(got - NUM.sigma_klein_nishina(e, m, s))
                    / NUM.sigma_klein_nishina(e, m, s))
    ok = worst < 1e-10
    all_passed = all_passed and ok
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: Klein-Nishina sigma, "
          f"worst rel {worst:.2e}")

    # Thomson limit
    s0 = m * m * (1 + 2e-4)
    got = NUM.cross_section(lambda ct: NUM.m2_compton(e, m, s0, ct) / 4.0,
                            s0, (m, 0.0, m, 0.0), n_points=600)
    ref = 8 * math.pi / 3 * (e * e / (4 * math.pi * m)) ** 2
    ok = abs(got - ref) / ref < 1e-3          # O(omega/m) correction
    all_passed = all_passed and ok
    print(f"  {'[v] PASS' if ok else '[x] FAIL'}: Thomson limit "
          f"{got:.6e} vs 8 pi r_e^2/3 {ref:.6e}")
    print()
    return all_passed


def test_vvv_convention_consistency():
    """DETECTOR for the unresolved VVV momentum convention.

    scattering.py uses the textbook all-incoming triple-gauge vertex;
    feyncalc_codegen's decay path uses the physical momenta as drawn. They
    are not equal at finite masses. This test does not assert which is
    right -- it asserts that the discrepancy is still the KNOWN one, so it
    cannot silently change or be forgotten. See VVV_CONVENTION_NOTE in
    scattering.py.
    """
    import math
    import numpy as np

    print("=" * 60)
    print("VVV convention: decay path vs scattering builder")
    print("=" * 60)

    g, mV, m1, m2 = 0.8, 900.0, 200.0, 250.0
    TRUTH_AS_DRAWN = 128.55151575236184        # hepbench decay_V_to_VVp part (a)
    KNOWN_RATIO = 2.913914202356               # all-incoming / as-drawn

    lam = NUM.kallen(mV ** 2, m1 ** 2, m2 ** 2)
    pmag = math.sqrt(lam) / (2 * mV)
    p = np.array([mV, 0.0, 0.0, 0.0])
    p1 = np.array([math.sqrt(pmag ** 2 + m1 ** 2), 0.0, 0.0, pmag])
    p2 = np.array([math.sqrt(pmag ** 2 + m2 ** 2), 0.0, 0.0, -pmag])

    def width(k0, k1, k2):
        tot = 0.0
        for e0 in NUM.pol_vectors(p, mV):
            for e1 in NUM.pol_vectors(p1, m1):
                for e2 in NUM.pol_vectors(p2, m2):
                    a1, a2 = e1.conj(), e2.conj()
                    amp = 1j * g * (NUM.dot(e0, a1) * NUM.dot(k0 - k1, a2)
                                    + NUM.dot(a1, a2) * NUM.dot(k1 - k2, e0)
                                    + NUM.dot(a2, e0) * NUM.dot(k2 - k0, a1))
                    tot += abs(amp) ** 2
        return pmag / (8 * math.pi * mV ** 2) * tot / 3.0

    as_drawn = width(p, p1, p2)
    all_inc = width(p, -p1, -p2)

    ok1 = abs(as_drawn - TRUTH_AS_DRAWN) / TRUTH_AS_DRAWN < 1e-12
    ok2 = abs(all_inc / as_drawn - KNOWN_RATIO) / KNOWN_RATIO < 1e-9
    print(f"  as-drawn (decay path) {as_drawn:.10f}  vs hepbench truth "
          f"{TRUTH_AS_DRAWN:.10f}")
    print(f"  all-incoming (here)   {all_inc:.10f}  ratio {all_inc / as_drawn:.9f}")
    print(f"  {'[v] PASS' if ok1 else '[x] FAIL'}: as-drawn form still reproduces "
          f"hepbench decay truth")
    print(f"  {'[v] PASS' if ok2 else '[x] FAIL'}: discrepancy is still the known "
          f"{KNOWN_RATIO:.4f}x -- UNRESOLVED, see VVV_CONVENTION_NOTE")
    print()
    return ok1 and ok2


def main():
    want_numeric = "--numeric" in sys.argv
    results = [
        ("Harness conventions", test_harness_conventions()),
        ("Structural sweep", test_structural_sweep()),
        ("Loud refusals", test_unsupported_is_loud()),
        ("Literature anchors", test_literature_anchors()),
        ("VVV convention detector", test_vvv_convention_consistency()),
    ]
    if want_numeric:
        results.append(("Numeric cross-check", test_numeric_crosscheck()))
    else:
        print("(numeric cross-check skipped; pass --numeric to run it)\n")

    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    for name, ok in results:
        print(f"  {'[v] PASS' if ok else '[x] FAIL'}: {name}")
    passed = sum(1 for _, ok in results if ok)
    print(f"\nTotal: {passed}/{len(results)} test groups passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
