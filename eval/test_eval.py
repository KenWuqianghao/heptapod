#!/usr/bin/env python3
"""
# test_eval.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.

Tests for the benchmark harness.

Offline tests cover the deterministic scoring (particle/parameter recall, charge
accuracy, aggregation) and a fully-mocked run of the runner (tools patched to
return canned outputs) to verify orchestration + report aggregation. The real
benchmark (needs an LLM + FeynRules) runs via `python eval/run_eval.py`.
"""

import argparse
import json
import sys
from pathlib import Path
from unittest import mock

SCRIPT_PATH = Path(__file__).resolve()
EVAL_DIR = SCRIPT_PATH.parent
REPO_ROOT = EVAL_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

from eval import run_eval as RE
from eval.scoring import aggregate, score_case, score_parameters, score_particles

_PRODUCED = {
    "particles": [
        {
            "class_name": "S1",
            "particle_name": "S1",
            "unphysical": False,
            "quantum_numbers": {"Q": "-1/3"},
        },
        {"class_name": "Phi", "unphysical": True, "definitions": ["Phi[1] -> 0"]},
    ],
    "parameters": [{"name": "yRR11"}],
}


def test_score_particles() -> bool:
    print(">> Testing particle scoring...\n")
    r = score_particles(_PRODUCED, [{"name": "S1", "charge": "-1/3"}])
    assert r["matched"] == 1 and r["recall"] == 1.0, r
    assert r["produced"] == 1, r  # unphysical excluded
    assert r["charge_accuracy"] == 1.0, r
    # Charge mismatch: name still matches, but charge accuracy drops.
    r2 = score_particles(_PRODUCED, [{"name": "S1", "charge": "2/3"}])
    assert r2["recall"] == 1.0 and r2["charge_accuracy"] == 0.0, r2
    # Missing particle.
    r3 = score_particles(_PRODUCED, [{"name": "Zprime"}])
    assert r3["recall"] == 0.0 and r3["missing"] == ["Zprime"], r3
    print("[✓] Particle scoring test passed\n")
    return True


def test_score_parameters() -> bool:
    print(">> Testing parameter scoring...\n")
    r = score_parameters(_PRODUCED, ["yRR11", "gX"])
    assert r["matched"] == 1 and r["recall"] == 0.5, r
    assert r["missing"] == ["gX"], r
    print("[✓] Parameter scoring test passed\n")
    return True


def test_score_case_and_aggregate() -> bool:
    print(">> Testing case scoring + aggregation...\n")
    sc = score_case(_PRODUCED, {"particles": [{"name": "S1", "charge": "-1/3"}]})
    assert 0.0 < sc["extraction_score"] <= 1.0, sc
    results = [
        {"name": "a", "extracted": True, "generated": True, "validated": True, "score": sc},
        {"name": "b", "extracted": False, "generated": False, "validated": False, "score": None},
    ]
    agg = aggregate(results)
    assert agg["n_cases"] == 2, agg
    assert agg["extraction_rate"] == 0.5, agg
    assert agg["validation_pass_rate"] == 0.5, agg
    assert aggregate([])["n_cases"] == 0
    print("[✓] Case scoring + aggregation test passed\n")
    return True


def _class_returning(canned: str):
    """A stand-in tool class: Cls(**kw)._run() -> canned string."""
    inst = mock.Mock()
    inst._run.return_value = canned
    return mock.Mock(return_value=inst)


def test_run_case_mocked() -> bool:
    print(">> Testing run_case orchestration (mocked tools)...\n")
    extract_out = json.dumps(
        {
            "status": "ok",
            "schema": "lagrangian-extraction-1.0",
            "model_name": "S1x",
            "n_particles": 1,
            "n_parameters": 0,
            "model": {
                "model_name": "S1x",
                "particles": [
                    {
                        "class_name": "S1",
                        "particle_name": "S1",
                        "unphysical": False,
                        "quantum_numbers": {"Q": "-1/3"},
                    }
                ],
            },
        }
    )
    gen_out = json.dumps({"status": "ok", "fr_path": "models/x.fr"})
    val_out = json.dumps({"status": "ok", "passed": True, "checks": [{"name": "ufo_generation", "passed": True}]})

    case = {
        "name": "S1x",
        "scenario": "scalar leptoquark",
        "paper_text": "A scalar leptoquark S1 with Q=-1/3.",
        "expected": {"particles": [{"name": "S1", "charge": "-1/3"}]},
    }

    with mock.patch.object(RE, "ExtractLagrangianTool", _class_returning(extract_out)), \
         mock.patch.object(RE, "GenerateFeynRulesModelTool", _class_returning(gen_out)), \
         mock.patch.object(RE, "ValidateModelTool", _class_returning(val_out)):
        rec = RE.run_case(case, base_directory="/tmp/does-not-matter",
                          feynrules_path="/fr", wolframscript_path="ws")

    assert rec["extracted"] and rec["generated"] and rec["validated"], rec
    assert rec["score"]["particles"]["recall"] == 1.0, rec
    print("[✓] run_case (mocked) test passed\n")
    return True


def test_run_case_extraction_failure_mocked() -> bool:
    print(">> Testing run_case extraction-failure path (mocked)...\n")
    # ExtractLagrangianTool returns a plain-string error -> extracted stays False.
    with mock.patch.object(RE, "ExtractLagrangianTool",
                           _class_returning("Error: LLM Unavailable\n- Reason: no config")):
        case = {"name": "z", "scenario": "x", "paper_text": "y", "expected": {"particles": []}}
        rec = RE.run_case(case, base_directory="/tmp/x", feynrules_path="/fr", wolframscript_path="ws")
    assert rec["extracted"] is False, rec
    assert rec["errors"] and "extraction" in rec["errors"][0], rec
    print("[✓] run_case extraction-failure test passed\n")
    return True


TESTS = [
    test_score_particles,
    test_score_parameters,
    test_score_case_and_aggregate,
    test_run_case_mocked,
    test_run_case_extraction_failure_mocked,
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests for the eval harness")
    parser.add_argument("--keep-files", action="store_true", help="(no-op; kept for runner parity)")
    parser.parse_args()

    all_passed = True
    for test in TESTS:
        try:
            if not test():
                all_passed = False
        except Exception as e:  # noqa: BLE001
            print(f"[✗] {test.__name__} failed: {e}\n")
            all_passed = False

    if all_passed:
        print("[✓] All tests passed!\n")
        sys.exit(0)
    print("[✗] Some tests failed!\n")
    sys.exit(1)
