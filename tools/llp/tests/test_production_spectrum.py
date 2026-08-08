"""
# test_production_spectrum.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Unit tests for ProductionSpectrumTool and the spectra package.

The physics checks compare against things that are true independently of this
implementation -- a closed-form normalisation, an independent quadrature, and
convergence in the grid parameters -- rather than against stored golden
numbers, which would only lock in whatever the code did on the day.
"""
import json
import math
import os
import shutil
import sys
import tempfile
from pathlib import Path

import numpy as np

SCRIPT_PATH = Path(__file__).resolve()
TOOL_DIR = SCRIPT_PATH.parent.parent
REPO_ROOT = TOOL_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.llp.production_spectrum import ProductionSpectrumTool   # noqa: E402
from tools.llp.spectra import kinematics as kin                    # noqa: E402
from tools.llp.spectra import parents as sm                        # noqa: E402
from tools.llp.spectra import vertices as vtx                      # noqa: E402
from tools.llp.llp_physics import LLPSpectrum                      # noqa: E402

base_directory = str(TOOL_DIR / "test_files_spectrum")


def _setup():
    if os.path.isdir(base_directory):
        shutil.rmtree(base_directory)
    os.makedirs(base_directory, exist_ok=True)


def _tool(**kw):
    kw.setdefault("base_directory", base_directory)
    return ProductionSpectrumTool(**kw)


def _run(**kw):
    return json.loads(_tool(**kw)._run())


# ---------------------------------------------------------------- physics --
def test_spectrum_is_normalised():
    """f_h(x) must integrate to 1 -- the contract the sampler relies on."""
    print(">> f(x) is normalised ...")
    msq = vtx.get("pseudoscalar", "scalar")
    for h in sm.PSEUDOSCALARS:
        p = sm.get(h)
        m_phi = 0.4 * sm.kinematic_limit(h)
        _, xs, fx = kin.width_and_spectrum(p.mass_gev, sm.M_MU_GEV, m_phi, msq)
        # integrate on the same GL nodes the spectrum was built on
        _, wx = kin._gl_nodes_x(p.mass_gev, sm.M_MU_GEV, m_phi, kin.N_X_DEFAULT)
        integral = float(np.dot(fx, wx))
        assert abs(integral - 1.0) < 1e-10, (h, integral)
    print("[OK] all hosted pseudoscalar spectra integrate to 1")


def test_quadrature_defaults_are_converged():
    """The shipped n_x/n_c must agree with a much finer grid.

    This is the guard on the defaults: if someone lowers them, or changes the
    substitution, this fails.
    """
    print(">> default quadrature is converged ...")
    msq = vtx.get("pseudoscalar", "scalar")
    worst = 0.0
    for h in sm.PSEUDOSCALARS:
        p = sm.get(h)
        lim = sm.kinematic_limit(h)
        for frac in (0.02, 0.5, 0.99):
            m_phi = frac * lim
            g_def, _, _ = kin.width_and_spectrum(
                p.mass_gev, sm.M_MU_GEV, m_phi, msq)
            g_fine, _, _ = kin.width_and_spectrum(
                p.mass_gev, sm.M_MU_GEV, m_phi, msq, n_x=192, n_c=192)
            worst = max(worst, abs(g_def / g_fine - 1.0))
    assert worst < 1e-4, f"defaults not converged: worst {worst:.2e}"
    print(f"[OK] worst deviation from a 192x192 grid: {worst:.2e}")


def test_substitution_beats_plain_gauss_legendre():
    """The sqrt substitution must actually be doing work.

    Without it the phase-space edge at x_min caps convergence; this pins the
    reason the integrator is written the way it is.
    """
    print(">> the x = x_min + t^2 substitution earns its place ...")
    msq = vtx.get("pseudoscalar", "scalar")
    p = sm.get("K")
    m_phi = 0.1 * sm.kinematic_limit("K")
    ref, _, _ = kin.width_and_spectrum(p.mass_gev, sm.M_MU_GEV, m_phi, msq,
                                       n_x=256, n_c=128)

    def plain(n_x):
        x_lo, x_hi = kin.x_domain(p.mass_gev, sm.M_MU_GEV, m_phi)
        t, w = np.polynomial.legendre.leggauss(n_x)
        xs = 0.5 * (x_hi - x_lo) * (t + 1.0) + x_lo
        wx = 0.5 * (x_hi - x_lo) * w
        cs, wc = np.polynomial.legendre.leggauss(64)
        P, pl, pn, pp, ok = kin.momenta(p.mass_gev, sm.M_MU_GEV, m_phi,
                                        xs[:, None], cs[None, :])
        val = np.where(ok, msq(P, pl, pn, pp, sm.M_MU_GEV, m_phi), 0.0)
        pref = kin.jacobian(p.mass_gev, sm.M_MU_GEV, m_phi, xs) / (
            (2 * np.pi) ** 3 * 32.0 * p.mass_gev ** 3)
        return float(np.dot(pref * (val @ wc), wx))

    n = kin.N_X_DEFAULT
    with_sub, _, _ = kin.width_and_spectrum(p.mass_gev, sm.M_MU_GEV, m_phi,
                                            msq, n_x=n, n_c=64)
    e_sub = abs(with_sub / ref - 1.0)
    e_plain = abs(plain(n) / ref - 1.0)
    assert e_sub < e_plain, (e_sub, e_plain)
    print(f"[OK] at n_x={n}: substituted {e_sub:.2e} vs plain {e_plain:.2e} "
          f"({e_plain/max(e_sub,1e-15):.0f}x better)")


def test_closed_channel_is_reported_not_an_error():
    """A mass grid must be allowed to span a threshold."""
    print(">> closed channels report, they do not fail ...")
    _setup()
    lim = sm.kinematic_limit("K")
    r = _run(parent="K", masses=[0.5 * lim, 1.5 * lim], output_dir="spec")
    assert r["status"] == "ok", r
    assert r["n_open"] == 1 and r["n_closed"] == 1, r
    closed = [m for m in r["masses"] if not m["open"]][0]
    assert "closed" in closed["reason"]
    print(f"[OK] limit {lim:.5f} GeV; open 1, closed 1, status ok")


# ------------------------------------------------------------- the chain --
def test_csv_feeds_the_downstream_sampler_unmodified():
    """The emitted CSV must load straight into LLPSpectrum.

    This is the seam between the two tools; if it needs conversion, the split
    has cost the agent something.
    """
    print(">> emitted CSV loads directly as a downstream spectrum ...")
    _setup()
    r = _run(parent="K", m_phi_gev=0.06, output_path="spec/K_m0.060.csv")
    assert r["status"] == "ok", r
    rec = r["masses"][0]
    path = os.path.join(base_directory, rec["spectrum_path"])
    spec = LLPSpectrum.from_path(path) if hasattr(LLPSpectrum, "from_path") \
        else LLPSpectrum.from_csv(path)
    rng = np.random.default_rng(3)
    x = spec.sample_x(sm.get("K").mass_gev, 0.06, 20000, rng)
    assert np.all(x >= rec["x_min"] - 1e-9)
    assert np.all(x <= rec["x_max"] + 1e-9)
    # the sampled mean must match the tabulated mean
    grid, pdf = spec.x, spec.pdf
    mean_tab = float(np.trapezoid(grid * pdf, grid) / np.trapezoid(pdf, grid))
    assert abs(x.mean() / mean_tab - 1.0) < 0.02, (x.mean(), mean_tab)
    print(f"[OK] sampled <x>={x.mean():.4f} vs tabulated {mean_tab:.4f}")


# --------------------------------------------------------------- the API --
def test_grid_mode_writes_manifest_and_creates_dirs():
    print(">> grid mode writes files + manifest, creating directories ...")
    _setup()
    r = _run(parent="D", masses=[0.2, 0.8, 1.4], output_dir="deep/nested/spec")
    assert r["status"] == "ok", r
    d = os.path.join(base_directory, "deep/nested/spec")
    assert os.path.isdir(d), "output_dir must be created"
    man = os.path.join(base_directory, r["manifest_path"])
    assert os.path.isfile(man)
    payload = json.load(open(man))
    assert payload["parent"] == "D" and "provenance" in payload
    for rec in r["masses"]:
        if rec["open"]:
            assert os.path.isfile(os.path.join(base_directory,
                                               rec["spectrum_path"]))
    print(f"[OK] {r['n_open']} spectra + manifest under {d}")


def test_provenance_cites_every_constant():
    print(">> every constant carries a source ...")
    _setup()
    r = _run(parent="K", m_phi_gev=0.06, output_path="s.csv")
    prov = r["provenance"]
    assert prov["constants"], prov
    for name, (value, source) in prov["constants"].items():
        assert source, f"{name} has no source"
        assert isinstance(value, float), name
    assert "Carlson" in prov["amplitude_reference"]
    assert "arXiv:2501.09071" in prov["application_reference"]
    assert prov["modelling_assumptions"]
    print(f"[OK] {len(prov['constants'])} constants cited, amplitude + "
          f"application references present")


def test_errors_are_actionable():
    print(">> bad input gives an actionable error, not a traceback ...")
    _setup()
    bad = _tool(parent="nosuch", m_phi_gev=0.1, output_path="s.csv")._run()
    assert "hosted parents are" in bad, bad
    bad = _tool(parent="K", m_phi_gev=0.1, interaction="tensor",
                output_path="s.csv")._run()
    assert "vertices.py" in bad, bad
    bad = _tool(parent="K", m_phi_gev=0.1,
                output_path="../../../tmp/evil.csv")._run()
    assert "denied" in bad.lower(), bad
    bad = _tool(parent="K", m_phi_gev=-1.0, output_path="s.csv")._run()
    assert "m_phi_gev" in bad, bad
    print("[OK] unknown parent, unsupported vertex, traversal, bad mass")


def test_kinematic_limits_match_the_physics():
    print(">> kinematic limits ...")
    for h in sm.PSEUDOSCALARS:
        p = sm.get(h)
        assert abs(sm.kinematic_limit(h)
                   - (p.mass_gev - sm.M_MU_GEV)) < 1e-12
    for h in sm.VECTORS:
        p = sm.get(h)
        assert abs(sm.kinematic_limit(h)
                   - (p.mass_gev - 2 * sm.M_MU_GEV)) < 1e-12
    assert sm.is_open("K", 0.3) and not sm.is_open("K", 0.4)
    # electron channels open much further than muon ones
    assert sm.kinematic_limit("K", "e") > sm.kinematic_limit("K", "mu")
    print("[OK] pseudoscalar m_h - m_l, vector m_h - 2 m_l, lepton-dependent")


if __name__ == "__main__":
    for fn in [v for k, v in sorted(globals().items())
               if k.startswith("test_")]:
        fn()
    print("\nall production-spectrum tests passed")
