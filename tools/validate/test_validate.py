#!/usr/bin/env python3
"""
# test_validate.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.

Tests for the model validation tool.

Offline tests cover the deterministic checks (UFO file presence, particle
presence, expected-name extraction) and the tool's control flow with a mocked
FeynRulesToUFOTool (success and failure). A gated live test compiles a generated
.fr to a UFO and validates it when FeynRules + wolframscript are configured.
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from unittest import mock

SCRIPT_PATH = Path(__file__).resolve()
TOOL_DIR = SCRIPT_PATH.parent
REPO_ROOT = TOOL_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))

import tools.validate.validate_tool as VT
from tools.validate.validate_tool import (
    ValidateModelTool,
    check_particles_present,
    check_ufo_files,
    _expected_particle_names,
)

TEST_DIR = TOOL_DIR / "test_files"


def _make_fake_ufo(ufo_dir: Path, particle_names=("S1",)) -> None:
    ufo_dir.mkdir(parents=True, exist_ok=True)
    for fname in ("__init__.py", "particles.py", "parameters.py", "vertices.py", "couplings.py"):
        (ufo_dir / fname).write_text("# ufo\n")
    body = "\n".join(f"{n} = Particle(pdg_code=100, name='{n}')" for n in particle_names)
    (ufo_dir / "particles.py").write_text(body + "\n")


def _write_dummy_fr(rel="models/x.fr") -> str:
    p = TEST_DIR / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('M$ModelName = "X";\n')
    return rel


def test_check_ufo_files() -> bool:
    print(">> Testing UFO file presence checks...\n")
    ufo = TEST_DIR / "ufo_a"
    ufo.mkdir(parents=True, exist_ok=True)
    (ufo / "particles.py").write_text("x")  # only one present
    checks = check_ufo_files(str(ufo))
    by = {c["name"]: c["passed"] for c in checks}
    assert by["ufo_file:particles.py"] is True, by
    assert by["ufo_file:vertices.py"] is False, by
    print("[✓] UFO file-check test passed\n")
    return True


def test_check_particles_present() -> bool:
    print(">> Testing particle-presence checks...\n")
    ufo = TEST_DIR / "ufo_b"
    _make_fake_ufo(ufo, particle_names=("S1",))
    checks = check_particles_present(str(ufo), ["S1", "Zprime"])
    by = {c["name"]: c["passed"] for c in checks}
    assert by["particle_in_ufo:S1"] is True, by
    assert by["particle_in_ufo:Zprime"] is False, by
    print("[✓] Particle-presence test passed\n")
    return True


def test_expected_particle_names() -> bool:
    print(">> Testing expected-name extraction (skips unphysical)...\n")
    model = {
        "particles": [
            {"class_name": "S1", "particle_name": "S1", "unphysical": False},
            {"class_name": "Phi", "unphysical": True, "definitions": ["Phi[1] -> 0"]},
        ]
    }
    names = _expected_particle_names(json.dumps(model))
    assert names == ["S1"], names
    assert _expected_particle_names(None) == []
    print("[✓] Expected-name extraction test passed\n")
    return True


def test_validate_missing_model() -> bool:
    print(">> Testing missing model handling...\n")
    tool = ValidateModelTool(
        model_path="models/nope.fr",
        base_directory=str(TEST_DIR),
        feynrules_path="/fr",
        wolframscript_path="wolframscript",
    )
    result = tool._run()
    assert "not found" in result.lower() or "error" in result.lower(), result
    print("[✓] Missing-model test passed\n")
    return True


def test_validate_success_mocked() -> bool:
    print(">> Testing validation success path (mocked UFO tool)...\n")
    rel = _write_dummy_fr()
    ufo_dir = TEST_DIR / "UFO_ok"
    _make_fake_ufo(ufo_dir, particle_names=("S1",))
    model_json = json.dumps({"particles": [{"class_name": "S1", "unphysical": False}]})

    inst = mock.Mock()
    inst._run.return_value = json.dumps({"ok": True, "output_dir": str(ufo_dir)})
    with mock.patch.object(VT, "FeynRulesToUFOTool", return_value=inst):
        tool = ValidateModelTool(
            model_path=rel,
            feynrules_model_json=model_json,
            base_directory=str(TEST_DIR),
            feynrules_path="/fr",
            wolframscript_path="wolframscript",
        )
        result = json.loads(tool._run())

    assert result["passed"] is True, result
    names = {c["name"]: c["passed"] for c in result["checks"]}
    assert names["ufo_generation"] is True, result
    assert names["particle_in_ufo:S1"] is True, result
    print("[✓] Validation success (mocked) test passed\n")
    return True


def test_validate_failure_mocked() -> bool:
    print(">> Testing validation failure path (mocked UFO tool error)...\n")
    rel = _write_dummy_fr()
    inst = mock.Mock()
    # FeynRulesToUFOTool returns a plain-string format_error on failure.
    inst._run.return_value = "Error: UFO Generation Failed\n- Reason: LoadModel::NoClasses"
    with mock.patch.object(VT, "FeynRulesToUFOTool", return_value=inst):
        tool = ValidateModelTool(
            model_path=rel,
            base_directory=str(TEST_DIR),
            feynrules_path="/fr",
            wolframscript_path="wolframscript",
        )
        result = json.loads(tool._run())

    assert result["passed"] is False, result
    gen = [c for c in result["checks"] if c["name"] == "ufo_generation"][0]
    assert gen["passed"] is False, result
    assert "feynrules_log" in result, result
    print("[✓] Validation failure (mocked) test passed\n")
    return True


def test_validate_live() -> bool:
    print(">> Testing live .fr -> UFO validation (needs FeynRules + wolframscript)...\n")
    try:
        from config import feynrules_path, wolframscript_path
    except Exception:  # noqa: BLE001
        print("[⊘] Skipping: config.py not set up\n")
        return True
    if not shutil.which(wolframscript_path) or feynrules_path in (None, "/path/to/FeynRules"):
        print("[⊘] Skipping: wolframscript/FeynRules not configured\n")
        return True

    from tools.frgen.frgen_tool import GenerateFeynRulesModelTool
    from tools.frgen.test_frgen import _s1_model

    s1 = _s1_model()
    gen = GenerateFeynRulesModelTool(
        model_json=s1.model_dump_json(),
        output_path="models/val_S1.fr",
        base_directory=str(TEST_DIR),
    )
    gres = json.loads(gen._run())
    assert gres["status"] == "ok", gres

    tool = ValidateModelTool(
        model_path=gres["fr_path"],
        feynrules_model_json=s1.model_dump_json(),
        output_dir="UFO_val_S1",
        base_directory=str(TEST_DIR),
        feynrules_path=feynrules_path,
        wolframscript_path=wolframscript_path,
        timeout_sec=900,
    )
    vres = json.loads(tool._run())
    assert vres["passed"], vres
    print("[✓] Live validation passed\n")
    return True


def cleanup_test_files() -> None:
    print("\n>> Cleaning up test files...\n")
    if TEST_DIR.exists():
        shutil.rmtree(TEST_DIR)
        print(f"[✓] Removed: {TEST_DIR.name}\n")
    else:
        print("[i] No test files to clean up\n")


TESTS = [
    test_check_ufo_files,
    test_check_particles_present,
    test_expected_particle_names,
    test_validate_missing_model,
    test_validate_success_mocked,
    test_validate_failure_mocked,
    test_validate_live,
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests for the validate toolkit")
    parser.add_argument("--keep-files", action="store_true", help="Keep test-generated files")
    args = parser.parse_args()

    all_passed = True
    for test in TESTS:
        try:
            if not test():
                all_passed = False
        except Exception as e:  # noqa: BLE001
            print(f"[✗] {test.__name__} failed: {e}\n")
            all_passed = False

    if not args.keep_files:
        cleanup_test_files()
    else:
        print("\n[i] Keeping test files (--keep-files set)\n")

    if all_passed:
        print("[✓] All tests passed!\n")
        sys.exit(0)
    print("[✗] Some tests failed!\n")
    sys.exit(1)
