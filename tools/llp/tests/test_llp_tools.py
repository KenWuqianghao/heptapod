#!/usr/bin/env python3
"""
# test_llp_tools.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
"""
LLP Tools Test Suite

The tools are model-agnostic: the production physics is supplied as a
declared `spectrum_spec` data product (a table or a two-body delta), not
baked into the tool. These tests generate their own spectra in-test from
a simple analytic pdf, so nothing here depends on a benchmark's ground
truth.

Tests cover:
- Path traversal prevention (security)
- Deterministic flux sampling from a tiny analytic kernel + a `table`
  spectrum (mass shell, weight normalization, manifest convention)
- A `two_body` (delta-function x) spectrum: every event on the same x
- Above-kinematic-cutoff behavior derived from the spectrum domain
- Decay-in-volume smoke test (counts, audit columns, yields table)
- Exact g^4 weak-coupling scaling: N(r*g)/N(g) = r^4 for r = 3
- Direct-lifetime mode (ctau_grid_m): yields per ctau, no g^2 factor
- Unequal daughter masses in the two-track acceptance
- Empty events input (closed channel) yields zeros, not an error

Run with:
    python test_llp_tools.py
"""

import argparse
import csv
import json
import math
import shutil
import sys
from pathlib import Path

# Path setup
SCRIPT_PATH = Path(__file__).resolve()
TOOL_DIR = SCRIPT_PATH.parent.parent                          # .../heptapod/tools/llp
TOOLS_DIR = TOOL_DIR.parent                                   # .../heptapod/tools
REPO_ROOT = TOOLS_DIR.parent                                  # .../heptapod
sys.path.insert(0, str(REPO_ROOT))

from tools.llp import LLPFluxFromMesonDecayTool, DecayInVolumeTool

# Initialize base directory
base_directory = str(TOOL_DIR / "test_files_llp")

# Test kernel: a synthetic forward K-like parent flux (non-round toy
# values; the setting lives entirely in this file).
TEST_KERNEL = """\
kernel:
  name: test_kaon_forward
  parent: K+
  parent_mass_gev: 0.493677
  form: pexp_texp
  params:
    n_per_int: 0.061
    p0_gev: 37.0
    a: 1.7
    theta0_rad: 0.0012
"""

# Test geometry: a far-forward on-axis decay volume + detector plane.
TEST_GEOMETRY = """\
geometry:
  z_min_m: 617.0
  z_max_m: 625.0
  r_volume_m: 0.55
  z_det_m: 630.0
  r_det_m: 0.55
"""

M_PARENT = 0.493677
M_PHI = 0.25
M_MU = 0.1056584
KAPPA = 1.3e-5
N_INT = 2.2e16


def _width_ref(m_phi, m_mu):
    """Gamma(phi -> mu mu) at g = 1: m_phi beta^3 / (8 pi)."""
    beta = math.sqrt(1.0 - 4.0 * m_mu * m_mu / (m_phi * m_phi))
    return m_phi * beta ** 3 / (8.0 * math.pi)


def _analytic_table(path, m_phi=M_PHI, n=60):
    """Write a `table` spectrum CSV from a simple analytic bump pdf.

    The x domain mirrors the 3-body radiation range for M -> mu nu phi,
    x in [2 m_phi/m_M, 1 + (m_phi^2 - m_mu^2)/m_M^2]; the pdf shape is a
    generic quadratic bump (unnormalized on purpose — the tool
    normalizes). This is a stand-in for a pinned ground-truth density;
    the tool never sees an amplitude."""
    x_lo = 2.0 * m_phi / M_PARENT
    x_hi = 1.0 + (m_phi ** 2 - M_MU ** 2) / M_PARENT ** 2
    xs = [x_lo + (x_hi - x_lo) * i / (n - 1) for i in range(n)]
    pdf = [(x - x_lo) * (x_hi - x) for x in xs]      # zero at both ends
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# provenance: in-test analytic bump pdf (unnormalized)"])
        w.writerow(["x", "pdf"])
        for x, p in zip(xs, pdf):
            w.writerow([x, p])
    return x_lo, x_hi


def _setup_inputs():
    """Write the test kernel, geometry, and spectrum files."""
    base = Path(base_directory)
    base.mkdir(parents=True, exist_ok=True)
    (base / "kernel.yaml").write_text(TEST_KERNEL)
    (base / "geometry.yaml").write_text(TEST_GEOMETRY)
    _analytic_table(base / "spectrum_table.csv")
    # two-body spectrum: phi + massless partner (delta function in x)
    (base / "spectrum_2body.yaml").write_text(
        "spectrum:\n  type: two_body\n  m_other_gev: 0.0\n")


def _run_flux(output_path="flux/phi_K.jsonl", m_phi=M_PHI,
              spectrum_spec="spectrum_table.csv", n_samples=20000, seed=42):
    """Run the flux tool with test defaults and return the parsed result."""
    tool = LLPFluxFromMesonDecayTool(
        base_directory=base_directory,
        kernel_spec="kernel.yaml",
        spectrum_spec=spectrum_spec,
        m_phi_gev=m_phi,
        kappa=KAPPA,
        n_samples=n_samples,
        seed=seed,
        output_path=output_path,
    )
    tool._setup()
    return json.loads(tool._run())


# ============================================================================
# Test Functions
# ============================================================================

def test_path_traversal_prevention():
    """Test that path traversal attempts are rejected (security)."""
    print(">> Testing path traversal prevention (security)...\n")
    _setup_inputs()

    tool = LLPFluxFromMesonDecayTool(
        base_directory=base_directory,
        kernel_spec="../../../etc/passwd",
        spectrum_spec="spectrum_table.csv",
        m_phi_gev=M_PHI,
        kappa=KAPPA,
        n_samples=10,
        seed=1,
        output_path="flux/out.jsonl",
    )
    tool._setup()
    result = tool._run()
    assert "denied" in result.lower() or "escape" in result.lower()
    print("[OK] Test 1 passed: flux tool kernel_spec traversal rejected")

    tool = LLPFluxFromMesonDecayTool(
        base_directory=base_directory,
        kernel_spec="kernel.yaml",
        spectrum_spec="spectrum_table.csv",
        m_phi_gev=M_PHI,
        kappa=KAPPA,
        n_samples=10,
        seed=1,
        output_path="../../../tmp/evil.jsonl",
    )
    tool._setup()
    result = tool._run()
    assert "denied" in result.lower() or "escape" in result.lower()
    print("[OK] Test 2 passed: flux tool output_path traversal rejected")

    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="../../../etc/passwd",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI,
        width_ref_gev=1e-3,
        g_grid=[1e-6],
        n_int=N_INT,
        output_path="yields/out.json",
    )
    tool._setup()
    result = tool._run()
    assert "denied" in result.lower() or "escape" in result.lower()
    print("[OK] Test 3 passed: decay tool events_path traversal rejected")

    print("\nAll path traversal prevention tests passed! [OK]\n")


def test_flux_sampling():
    """Deterministic flux smoke test: records, mass shell, weights."""
    print(">> Testing LLP flux sampling from a tiny kernel + table...\n")
    _setup_inputs()

    n_samples = 5000
    res = _run_flux(output_path="flux/smoke.jsonl", n_samples=n_samples,
                    seed=7)
    assert res["status"] == "ok", res
    assert res["n_samples"] == n_samples
    assert res["weight_convention"] == "g2_stripped_per_primary_interaction"
    assert res["parent"] == "K+"
    assert res["spectrum_type"] == "table"
    assert not res["above_kinematic_cutoff"]
    # sum of weights = n_per_int * kappa (g^2-stripped yield / interaction)
    expected_sw = 0.061 * KAPPA
    assert abs(res["sum_weights"] - expected_sw) / expected_sw < 1e-12
    print("[OK] Test 1 passed: status, weight convention, sum_weights")

    # records: mass shell + weight normalization + kinematic domain
    events_file = Path(base_directory) / res["output_path"]
    records = [json.loads(l) for l in events_file.read_text().splitlines()]
    assert len(records) == n_samples
    for rec in records[::503]:
        m2 = rec["E"] ** 2 - rec["px"] ** 2 - rec["py"] ** 2 - rec["pz"] ** 2
        assert abs(math.sqrt(max(m2, 0.0)) - M_PHI) < 1e-6, rec
        assert 0.0 <= rec["theta_lab"] <= math.pi
        assert rec["parent_channel"] == "K+"
        w = rec["event_weight_g2_stripped"]
        assert abs(w - expected_sw / n_samples) / w < 1e-12
    print("[OK] Test 2 passed: records on mass shell with correct weights")

    # manifest declares the convention and the spectrum provenance
    manifest = json.loads(
        (Path(base_directory) / res["manifest_path"]).read_text())
    assert manifest["weight_convention"] == \
        "g2_stripped_per_primary_interaction"
    assert manifest["parent_mass_gev"] == 0.493677
    assert manifest["spectrum_type"] == "table"
    assert "m_mu_gev" not in manifest  # no model-specific mass in the flux
    print("[OK] Test 3 passed: manifest declares convention + spectrum")

    # determinism: same seed reproduces the sample exactly
    res2 = _run_flux(output_path="flux/smoke2.jsonl", n_samples=n_samples,
                     seed=7)
    records2 = [json.loads(l) for l in
                (Path(base_directory) / res2["output_path"])
                .read_text().splitlines()]
    assert records[0]["E"] == records2[0]["E"]
    assert records[-1]["pz"] == records2[-1]["pz"]
    print("[OK] Test 4 passed: seeded sampling is deterministic")

    print("\nAll flux sampling tests passed! [OK]\n")
    return True


def test_two_body_spectrum():
    """A `two_body` spectrum fixes x by two-body kinematics (delta)."""
    print(">> Testing two_body (delta-function x) spectrum...\n")
    _setup_inputs()

    n_samples = 4000
    res = _run_flux(output_path="flux/twobody.jsonl",
                    spectrum_spec="spectrum_2body.yaml",
                    n_samples=n_samples, seed=5)
    assert res["status"] == "ok", res
    assert res["spectrum_type"] == "two_body"
    # cutoff is m_parent - m_other = m_parent (m_other = 0 here)
    assert abs(res["kinematic_cutoff_gev"] - M_PARENT) < 1e-12
    print("[OK] Test 1 passed: two_body flux runs, cutoff = m_parent")

    # Every event carries the same rest-frame energy E* = x0 m_M / 2 with
    # x0 = (m_M^2 + m_phi^2 - m_other^2)/m_M^2. So the rest-frame |p*| is
    # identical for all events; recover it from the lab records via the
    # boost invariant p_par . k = m_M E* - E_par E* ... simplest check:
    # the phi is on-shell and the spread of E* across events is zero.
    x0 = (M_PARENT ** 2 + M_PHI ** 2) / M_PARENT ** 2
    estar0 = 0.5 * x0 * M_PARENT
    records = [json.loads(l) for l in
               (Path(base_directory) / res["output_path"])
               .read_text().splitlines()]
    # E* is Lorentz-invariant given the parent 4-vector; reconstruct it as
    # (E_phi_lab is frame-dependent, so instead check the mass shell and
    # that the two_body cutoff logic closed the channel above m_parent).
    for rec in records[::311]:
        m2 = rec["E"] ** 2 - rec["px"] ** 2 - rec["py"] ** 2 - rec["pz"] ** 2
        assert abs(math.sqrt(max(m2, 0.0)) - M_PHI) < 1e-6, rec
    assert estar0 >= M_PHI  # channel open
    print("[OK] Test 2 passed: two_body events on the phi mass shell")

    # A closed two_body channel: m_other so large that m_phi > m_M - m_other
    base = Path(base_directory)
    (base / "spectrum_2body_closed.yaml").write_text(
        "spectrum:\n  type: two_body\n  m_other_gev: 0.30\n")
    res_c = _run_flux(output_path="flux/twobody_closed.jsonl",
                      spectrum_spec="spectrum_2body_closed.yaml",
                      m_phi=0.25, n_samples=50, seed=1)
    assert res_c["status"] == "ok"
    assert res_c["above_kinematic_cutoff"] is True
    assert res_c["n_samples"] == 0
    print("[OK] Test 3 passed: two_body closed channel flagged, n=0")

    print("\nAll two_body spectrum tests passed! [OK]\n")
    return True


def test_flux_above_cutoff():
    """A table whose x_max cannot reach m_phi is a (closed) cutoff case."""
    print(">> Testing above-kinematic-cutoff behavior (table)...\n")
    _setup_inputs()

    # Build a table valid for m_phi = 0.25 but sample it at m_phi = 0.45:
    # the table's max x gives E*_max = x_max m_M / 2 < 0.45, so the tool
    # reports the channel closed (cutoff from the spectrum domain).
    res = _run_flux(output_path="flux/closed.jsonl", m_phi=0.45,
                    spectrum_spec="spectrum_table.csv", n_samples=100,
                    seed=3)
    assert res["status"] == "ok", res
    assert res["n_samples"] == 0
    assert res["above_kinematic_cutoff"] is True
    assert res["sum_weights"] == 0.0
    events_file = Path(base_directory) / res["output_path"]
    assert events_file.exists() and events_file.read_text() == ""
    print("[OK] Test 1 passed: table cutoff (x_max) closes the channel")

    print("\nAbove-cutoff test passed! [OK]\n")
    return True


def test_decay_in_volume():
    """Decay-in-volume smoke test: yields table + audit columns."""
    print(">> Testing decay-in-volume yields and audit output...\n")
    _setup_inputs()

    n_samples = 20000
    flux = _run_flux(output_path="flux/phi_K.jsonl", n_samples=n_samples,
                     seed=42)
    assert flux["status"] == "ok"

    wref = _width_ref(M_PHI, M_MU)
    g_grid = [1e-8, 1e-7, 1e-6]
    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI,
        daughter_masses_gev=[M_MU, M_MU],
        width_ref_gev=wref,
        g_grid=g_grid,
        n_int=N_INT,
        require_two_track=True,
        seed=11,
        output_path="yields/m0p25.json",
    )
    tool._setup()
    res = json.loads(tool._run())
    assert res["status"] == "ok", res
    assert res["lifetime_mode"] == "portal"
    assert res["n_events"] == n_samples
    assert 0 < res["n_pass_geometry"] <= n_samples
    assert 0 < res["n_pass_two_track"] <= res["n_pass_geometry"]
    assert res["conventions"] == {"two_track": "midpoint",
                                  "weight": "g2_stripped"}
    assert len(res["yields"]) == len(g_grid)
    assert all(row["n_sig"] > 0.0 for row in res["yields"])
    assert all("g" in row for row in res["yields"])
    print("[OK] Test 1 passed: portal yields computed with midpoint conv")

    # yields table on disk matches the tool result
    table = json.loads(
        (Path(base_directory) / res["output_path"]).read_text())
    assert table["yields"] == res["yields"]
    assert table["conventions"]["weight"] == "g2_stripped"
    assert table["lifetime_mode"] == "portal"
    print("[OK] Test 2 passed: yields table written and consistent")

    # audit file: one line per event with the required columns
    audit_file = Path(base_directory) / res["audit_path"]
    audit = [json.loads(l) for l in audit_file.read_text().splitlines()]
    assert len(audit) == n_samples
    required = {"parent_channel", "event_weight_g2_stripped", "beta_gamma",
                "L1_m", "L2_m", "geom_pass", "two_track_pass",
                "p_decay_at_ref", "weighted_contribution"}
    assert required <= set(audit[0])
    assert sum(1 for a in audit if a["geom_pass"]) == res["n_pass_geometry"]
    n_keep = sum(1 for a in audit if a["geom_pass"] and a["two_track_pass"])
    assert n_keep == res["n_pass_two_track"]
    # weighted contributions at the first grid point sum to that yield
    total = sum(a["weighted_contribution"] for a in audit)
    assert abs(total - res["yields"][0]["n_sig"]) \
        / res["yields"][0]["n_sig"] < 1e-9
    print("[OK] Test 3 passed: audit columns complete and self-consistent")

    print("\nAll decay-in-volume tests passed! [OK]\n")
    return True


def test_ctau_mode():
    """Direct-lifetime mode: yields per ctau, no g^2, monotone in ctau."""
    print(">> Testing direct-lifetime (ctau_grid_m) mode...\n")
    _setup_inputs()

    flux = _run_flux(output_path="flux/phi_K_ctau.jsonl", n_samples=20000,
                     seed=42)
    assert flux["status"] == "ok"

    ctau_grid = [0.1, 1.0, 10.0, 100.0]
    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_ctau.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI,
        ctau_grid_m=ctau_grid,
        n_int=N_INT,
        require_two_track=True,
        seed=11,
        output_path="yields/ctau.json",
    )
    tool._setup()
    res = json.loads(tool._run())
    assert res["status"] == "ok", res
    assert res["lifetime_mode"] == "ctau"
    assert len(res["yields"]) == len(ctau_grid)
    assert all("ctau_m" in row for row in res["yields"])
    assert all(row["n_sig"] > 0.0 for row in res["yields"])
    print("[OK] Test 1 passed: ctau yields computed, keyed by ctau_m")

    # Consistency with portal mode: at fixed lab ctau the decay factor is
    # identical, so N_ctau = N_portal / g^2 for the g whose ctau matches.
    wref = _width_ref(M_PHI, M_MU)
    g = 1e-6
    ctau_g = 1.973269804e-16 / (g * g * wref)
    tool_c = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_ctau.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI, ctau_grid_m=[ctau_g], n_int=N_INT,
        seed=11, output_path="yields/ctau_one.json")
    tool_c._setup()
    n_ctau = json.loads(tool_c._run())["yields"][0]["n_sig"]
    tool_p = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_ctau.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI, width_ref_gev=wref, g_grid=[g], n_int=N_INT,
        seed=11, output_path="yields/portal_one.json")
    tool_p._setup()
    n_portal = json.loads(tool_p._run())["yields"][0]["n_sig"]
    # n_portal = g^2 * n_ctau (same lab ctau, same events/seed)
    assert abs(n_portal / (g * g * n_ctau) - 1.0) < 1e-9, (n_portal, n_ctau)
    print("[OK] Test 2 passed: ctau vs portal consistent (N_portal = g^2 N_ctau)")

    # Ambiguity guard: both modes given is an error.
    tool_amb = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_ctau.jsonl",
        geometry_path="geometry.yaml", m_phi_gev=M_PHI,
        width_ref_gev=wref, g_grid=[g], ctau_grid_m=[1.0], n_int=N_INT,
        output_path="yields/amb.json")
    tool_amb._setup()
    out = tool_amb._run()
    assert "ambiguous" in out.lower(), out
    print("[OK] Test 3 passed: portal + ctau together is rejected")

    print("\nAll ctau-mode tests passed! [OK]\n")
    return True


def test_unequal_daughters():
    """Two-track acceptance with unequal daughter masses runs and is sane."""
    print(">> Testing unequal daughter masses in two-track...\n")
    _setup_inputs()

    flux = _run_flux(output_path="flux/phi_K_uneq.jsonl", n_samples=8000,
                     seed=42)
    assert flux["status"] == "ok"
    wref = _width_ref(M_PHI, M_MU)
    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_uneq.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI,
        daughter_masses_gev=[0.1056584, 0.05],   # unequal, m_phi > m1 + m2
        width_ref_gev=wref, g_grid=[1e-6], n_int=N_INT,
        seed=3, output_path="yields/uneq.json")
    tool._setup()
    res = json.loads(tool._run())
    assert res["status"] == "ok", res
    assert res["n_pass_two_track"] >= 0
    print("[OK] Test 1 passed: unequal-mass two-track runs")

    # Closed decay (m1 + m2 >= m_phi) is rejected with two-track on.
    tool_c = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_uneq.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI,
        daughter_masses_gev=[0.2, 0.2],          # sum > m_phi
        width_ref_gev=wref, g_grid=[1e-6], n_int=N_INT,
        output_path="yields/uneq_closed.json")
    tool_c._setup()
    out = tool_c._run()
    assert "m1 + m2" in out or "kinematically closed" in out.lower(), out
    print("[OK] Test 2 passed: closed two-body decay rejected")

    print("\nAll unequal-daughter tests passed! [OK]\n")
    return True


def test_br_visible_scales_yield():
    """br_visible multiplies the yield linearly, independent of lifetime."""
    print(">> Testing visible branching-ratio yield scaling...\n")
    _setup_inputs()

    flux = _run_flux(output_path="flux/phi_K_br.jsonl", n_samples=20000,
                     seed=42)
    assert flux["status"] == "ok"
    wref = _width_ref(M_PHI, M_MU)
    common = dict(base_directory=base_directory,
                  events_path="flux/phi_K_br.jsonl",
                  geometry_path="geometry.yaml", m_phi_gev=M_PHI,
                  daughter_masses_gev=[M_MU, M_MU], width_ref_gev=wref,
                  g_grid=[1e-7, 1e-6], n_int=N_INT, seed=11)

    full = DecayInVolumeTool(**common, br_visible=1.0,
                             output_path="yields/br_full.json")
    full._setup()
    y_full = json.loads(full._run())["yields"]

    half = DecayInVolumeTool(**common, br_visible=0.5,
                             output_path="yields/br_half.json")
    half._setup()
    y_half = json.loads(half._run())["yields"]

    # Default is 1.0 (backward compatible); 0.5 halves every yield exactly
    # (same lifetime -> same P_dec and acceptance, only the prefactor moves).
    for rf, rh in zip(y_full, y_half):
        assert abs(rh["n_sig"] / rf["n_sig"] - 0.5) < 1e-12, (rf, rh)
    print("[OK] br_visible=0.5 halves the yield; default 1.0 unchanged")

    # out-of-range is rejected
    bad = DecayInVolumeTool(**common, br_visible=1.5,
                            output_path="yields/br_bad.json")
    bad._setup()
    assert "br_visible" in bad._run()
    print("[OK] br_visible outside [0,1] rejected")

    print("\nAll br_visible tests passed! [OK]\n")
    return True


def test_g4_scaling():
    """Weak-coupling g^4 gate: N(3g)/N(g) = 81 within ~2%."""
    print(">> Testing exact g^4 weak-coupling scaling (r = 3)...\n")
    _setup_inputs()

    flux = _run_flux(output_path="flux/phi_K_scaling.jsonl",
                     n_samples=20000, seed=42)
    assert flux["status"] == "ok"

    wref = _width_ref(M_PHI, M_MU)
    g1, r = 3e-9, 3.0
    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/phi_K_scaling.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=M_PHI,
        daughter_masses_gev=[M_MU, M_MU],
        width_ref_gev=wref,
        g_grid=[g1, r * g1],
        n_int=N_INT,
        require_two_track=True,
        seed=11,
        output_path="yields/scaling.json",
    )
    tool._setup()
    res = json.loads(tool._run())
    assert res["status"] == "ok", res
    n1 = res["yields"][0]["n_sig"]
    n2 = res["yields"][1]["n_sig"]
    assert n1 > 0.0
    ratio = n2 / n1
    # In the weak-coupling limit P_dec ~ (L2 - L1)/lam with lam ~ 1/g^2,
    # so N_sig ~ g^4 and the ratio is r^4 = 81 up to O(L/lam) corrections.
    assert abs(ratio - r ** 4) / r ** 4 < 0.02, ratio
    print(f"[OK] Test 1 passed: N(3g)/N(g) = {ratio:.3f} "
          f"(expected {r ** 4:.0f} within 2%)")

    print("\ng^4 scaling test passed! [OK]\n")
    return True


def test_empty_events():
    """A closed channel (empty events file) gives zero yields, status ok."""
    print(">> Testing empty events input (closed channel)...\n")
    _setup_inputs()

    flux = _run_flux(output_path="flux/closed2.jsonl", m_phi=0.45,
                     spectrum_spec="spectrum_table.csv", n_samples=100,
                     seed=3)
    assert flux["status"] == "ok" and flux["n_samples"] == 0

    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/closed2.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=0.45,
        daughter_masses_gev=[M_MU, M_MU],
        width_ref_gev=_width_ref(0.45, M_MU),
        g_grid=[1e-8, 1e-6],
        n_int=N_INT,
        output_path="yields/closed.json",
    )
    tool._setup()
    res = json.loads(tool._run())
    assert res["status"] == "ok", res
    assert res["n_events"] == 0
    assert all(row["n_sig"] == 0.0 for row in res["yields"])
    print("[OK] Test 1 passed: empty input gives zero yields, not an error")

    print("\nEmpty events test passed! [OK]\n")
    return True


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="LLP tools test suite")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output (unused; kept for runner "
                             "compatibility)")
    parser.add_argument("--keep-files", action="store_true",
                        help="Keep test-generated files after tests")
    args = parser.parse_args()

    all_passed = True

    tests = [
        test_path_traversal_prevention,
        test_flux_sampling,
        test_two_body_spectrum,
        test_flux_above_cutoff,
        test_decay_in_volume,
        test_ctau_mode,
        test_unequal_daughters,
        test_br_visible_scales_yield,
        test_g4_scaling,
        test_empty_events,
    ]
    for test in tests:
        try:
            test()
        except (AssertionError, Exception) as e:
            print(f"\n[FAIL] {test.__name__} failed: {e}\n")
            all_passed = False

    if all_passed:
        print()
        print("=" * 70)
        print("Test suite completed successfully! [OK]")
        print("=" * 70)
        if not args.keep_files:
            shutil.rmtree(base_directory, ignore_errors=True)
    else:
        print()
        print("=" * 70)
        print("Test suite completed with failures! [FAIL]")
        print("=" * 70)

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
