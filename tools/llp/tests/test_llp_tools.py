#!/usr/bin/env python3
"""
# test_llp_tools.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
"""
LLP Tools Test Suite

Tests cover:
- Path traversal prevention (security)
- Deterministic flux sampling from a tiny analytic kernel
  (mass shell, weight normalization, manifest convention)
- Above-kinematic-cutoff behavior (status ok, n_samples 0, flagged)
- Decay-in-volume smoke test (counts, audit columns, yields table)
- Exact g^4 weak-coupling scaling: N(r*g)/N(g) = r^4 for r = 3
  (mirrors the validation of the reference pipeline)
- Empty events input (closed channel) yields zeros, not an error

Run with:
    python test_llp_tools.py
"""

import argparse
import json
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

M_PHI = 0.25
M_MU = 0.1056584
KAPPA = 1.3e-5
N_INT = 2.2e16


def _width_ref(m_phi, m_mu):
    """Gamma(phi -> mu mu) at g = 1: m_phi beta^3 / (8 pi)."""
    import math
    beta = math.sqrt(1.0 - 4.0 * m_mu * m_mu / (m_phi * m_phi))
    return m_phi * beta ** 3 / (8.0 * math.pi)


def _setup_inputs():
    """Write the test kernel and geometry YAML files."""
    base = Path(base_directory)
    base.mkdir(parents=True, exist_ok=True)
    (base / "kernel.yaml").write_text(TEST_KERNEL)
    (base / "geometry.yaml").write_text(TEST_GEOMETRY)


def _run_flux(output_path="flux/phi_K.jsonl", m_phi=M_PHI, n_samples=20000,
              seed=42):
    """Run the flux tool with test defaults and return the parsed result."""
    tool = LLPFluxFromMesonDecayTool(
        base_directory=base_directory,
        kernel_spec="kernel.yaml",
        m_phi_gev=m_phi,
        m_mu_gev=M_MU,
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
        m_phi_gev=M_PHI,
        kappa=KAPPA,
        n_samples=10,
        seed=1,
        output_path="flux/out.jsonl",
    )
    tool._setup()
    result = tool._run()
    assert "denied" in result.lower() or "escape" in result.lower()
    print("[✓] Test 1 passed: flux tool kernel_spec traversal rejected")

    tool = LLPFluxFromMesonDecayTool(
        base_directory=base_directory,
        kernel_spec="kernel.yaml",
        m_phi_gev=M_PHI,
        kappa=KAPPA,
        n_samples=10,
        seed=1,
        output_path="../../../tmp/evil.jsonl",
    )
    tool._setup()
    result = tool._run()
    assert "denied" in result.lower() or "escape" in result.lower()
    print("[✓] Test 2 passed: flux tool output_path traversal rejected")

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
    print("[✓] Test 3 passed: decay tool events_path traversal rejected")

    print("\nAll path traversal prevention tests passed! [✓]\n")


def test_flux_sampling():
    """Deterministic flux smoke test: records, mass shell, weights."""
    print(">> Testing LLP flux sampling from a tiny kernel...\n")
    _setup_inputs()

    n_samples = 5000
    res = _run_flux(output_path="flux/smoke.jsonl", n_samples=n_samples,
                    seed=7)
    assert res["status"] == "ok", res
    assert res["n_samples"] == n_samples
    assert res["weight_convention"] == "g2_stripped_per_primary_interaction"
    assert res["parent"] == "K+"
    assert not res["above_kinematic_cutoff"]
    # sum of weights = n_per_int * kappa (g^2-stripped yield / interaction)
    expected_sw = 0.061 * KAPPA
    assert abs(res["sum_weights"] - expected_sw) / expected_sw < 1e-12
    print("[✓] Test 1 passed: status, weight convention, sum_weights")

    # records: mass shell + weight normalization + kinematic domain
    events_file = Path(base_directory) / res["output_path"]
    records = [json.loads(l) for l in events_file.read_text().splitlines()]
    assert len(records) == n_samples
    import math
    x_hi = 1.0 + (M_PHI ** 2 - M_MU ** 2) / 0.493677 ** 2
    for rec in records[::503]:
        m2 = rec["E"] ** 2 - rec["px"] ** 2 - rec["py"] ** 2 - rec["pz"] ** 2
        assert abs(math.sqrt(max(m2, 0.0)) - M_PHI) < 1e-6, rec
        assert 0.0 <= rec["theta_lab"] <= math.pi
        assert rec["parent_channel"] == "K+"
        w = rec["event_weight_g2_stripped"]
        assert abs(w - expected_sw / n_samples) / w < 1e-12
    print("[✓] Test 2 passed: records on mass shell with correct weights")

    # manifest declares the convention
    manifest = json.loads(
        (Path(base_directory) / res["manifest_path"]).read_text())
    assert manifest["weight_convention"] == \
        "g2_stripped_per_primary_interaction"
    assert manifest["parent_mass_gev"] == 0.493677
    print("[✓] Test 3 passed: manifest declares g^2-stripped convention")

    # determinism: same seed reproduces the sample exactly
    res2 = _run_flux(output_path="flux/smoke2.jsonl", n_samples=n_samples,
                     seed=7)
    records2 = [json.loads(l) for l in
                (Path(base_directory) / res2["output_path"])
                .read_text().splitlines()]
    assert records[0]["E"] == records2[0]["E"]
    assert records[-1]["pz"] == records2[-1]["pz"]
    print("[✓] Test 4 passed: seeded sampling is deterministic")

    print("\nAll flux sampling tests passed! [✓]\n")
    return True


def test_flux_above_cutoff():
    """m_phi >= m_M - m_mu returns a structured cutoff result, not an error."""
    print(">> Testing above-kinematic-cutoff behavior...\n")
    _setup_inputs()

    res = _run_flux(output_path="flux/closed.jsonl", m_phi=0.45,
                    n_samples=100, seed=3)
    assert res["status"] == "ok", res
    assert res["n_samples"] == 0
    assert res["above_kinematic_cutoff"] is True
    assert res["sum_weights"] == 0.0
    cutoff = 0.493677 - M_MU
    assert abs(res["kinematic_cutoff_gev"] - cutoff) < 1e-12
    events_file = Path(base_directory) / res["output_path"]
    assert events_file.exists() and events_file.read_text() == ""
    print("[✓] Test 1 passed: closed channel flagged with n_samples = 0")

    print("\nAbove-cutoff test passed! [✓]\n")
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
        m_mu_gev=M_MU,
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
    assert res["n_events"] == n_samples
    assert 0 < res["n_pass_geometry"] <= n_samples
    assert 0 < res["n_pass_two_track"] <= res["n_pass_geometry"]
    assert res["conventions"] == {"two_track": "midpoint",
                                  "weight": "g2_stripped"}
    assert len(res["yields"]) == len(g_grid)
    assert all(row["n_sig"] > 0.0 for row in res["yields"])
    print("[✓] Test 1 passed: yields computed with midpoint convention")

    # yields table on disk matches the tool result
    table = json.loads(
        (Path(base_directory) / res["output_path"]).read_text())
    assert table["yields"] == res["yields"]
    assert table["conventions"]["weight"] == "g2_stripped"
    print("[✓] Test 2 passed: yields table written and consistent")

    # audit file: one line per event with the required columns
    audit_file = Path(base_directory) / res["audit_path"]
    audit = [json.loads(l) for l in audit_file.read_text().splitlines()]
    assert len(audit) == n_samples
    required = {"parent_channel", "event_weight_g2_stripped", "beta_gamma",
                "L1_m", "L2_m", "geom_pass", "two_track_pass",
                "p_decay_at_g_ref", "weighted_contribution_at_g_ref"}
    assert required <= set(audit[0])
    assert sum(1 for a in audit if a["geom_pass"]) == res["n_pass_geometry"]
    n_keep = sum(1 for a in audit if a["geom_pass"] and a["two_track_pass"])
    assert n_keep == res["n_pass_two_track"]
    # weighted contributions at g_ref sum to the g_ref yield
    total = sum(a["weighted_contribution_at_g_ref"] for a in audit)
    assert abs(total - res["yields"][0]["n_sig"]) \
        / res["yields"][0]["n_sig"] < 1e-9
    print("[✓] Test 3 passed: audit columns complete and self-consistent")

    print("\nAll decay-in-volume tests passed! [✓]\n")
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
        m_mu_gev=M_MU,
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
    print(f"[✓] Test 1 passed: N(3g)/N(g) = {ratio:.3f} "
          f"(expected {r ** 4:.0f} within 2%)")

    print("\ng^4 scaling test passed! [✓]\n")
    return True


def test_empty_events():
    """A closed channel (empty events file) gives zero yields, status ok."""
    print(">> Testing empty events input (closed channel)...\n")
    _setup_inputs()

    flux = _run_flux(output_path="flux/closed2.jsonl", m_phi=0.45,
                     n_samples=100, seed=3)
    assert flux["status"] == "ok" and flux["n_samples"] == 0

    tool = DecayInVolumeTool(
        base_directory=base_directory,
        events_path="flux/closed2.jsonl",
        geometry_path="geometry.yaml",
        m_phi_gev=0.45,
        m_mu_gev=M_MU,
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
    print("[✓] Test 1 passed: empty input gives zero yields, not an error")

    print("\nEmpty events test passed! [✓]\n")
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
        test_flux_above_cutoff,
        test_decay_in_volume,
        test_g4_scaling,
        test_empty_events,
    ]
    for test in tests:
        try:
            test()
        except (AssertionError, Exception) as e:
            print(f"\n[✗] {test.__name__} failed: {e}\n")
            all_passed = False

    if all_passed:
        print()
        print("=" * 70)
        print("Test suite completed successfully! [✓]")
        print("=" * 70)
        if not args.keep_files:
            shutil.rmtree(base_directory, ignore_errors=True)
    else:
        print()
        print("=" * 70)
        print("Test suite completed with failures! [✗]")
        print("=" * 70)

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
