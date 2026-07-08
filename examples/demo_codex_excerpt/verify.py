#!/usr/bin/env python3
"""verify.py — independently verify the Codex-generated S1 .fr.

Round-trips the generated model/S1_codex.fr through HEPTAPOD's own .fr parser
(NOT the generator that wrote it) and checks the physics is faithful to the
paper: complex colour-triplet scalar S1 with Q = -1/3, mass MS1, and a
right-handed Yukawa coupling yRR. Exit 0 iff every check passes.

Run:  ../../.venv/bin/python verify.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO))

from tools.frgen.fr_parser import parse_fr_file  # noqa: E402

FR = HERE / "model" / "S1_codex.fr"
if not FR.is_file():
    print(f"[FAIL] no generated .fr at {FR} — run ./run_demo.sh first")
    sys.exit(1)

body = FR.read_text()
parsed = parse_fr_file(str(FR))
s1 = next((c for c in parsed["classes"] if c["class_name"] == "S1"), None)
params = [p["name"] for p in parsed["parameters"]]

checks = {
    "file parses (round-trips through fr_parser)": s1 is not None,
    "S1 class present": s1 is not None,
    "electric charge Q = -1/3 (string-preserved)":
        bool(s1) and str(s1.get("quantum_numbers", {}).get("Q")) == "-1/3",
    "colour triplet (Index[Colour])": bool(s1) and "Colour" in str(s1.get("indices")),
    "complex scalar (SelfConjugate -> False)": "SelfConjugate -> False" in body,
    "distinct antiparticle (S1~)": "AntiParticleName" in body and "S1~" in body,
    "mass parameter MS1": "MS1" in body,
    "right-handed Yukawa coupling yRR": "yRR" in params or "yRR" in body,
    "hermitian-conjugated Yukawa term (HC[...])": "HC[" in body,
    "no doubled assignment operator": ":= :=" not in body and " = =" not in body,
}

width = max(len(k) for k in checks)
for name, ok in checks.items():
    print(f"  [{'PASS' if ok else 'FAIL'}] {name.ljust(width)}")

ok = all(checks.values())
print(f"\n{'[OK] all checks passed' if ok else '[FAIL] some checks failed'} "
      f"— {sum(checks.values())}/{len(checks)}")
sys.exit(0 if ok else 2)
