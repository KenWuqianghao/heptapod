"""Snapshot tests for HEPSIM5 extraction and crosscheck prompt text."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = REPO_ROOT / "tools" / "frgen" / "prompts"
FIXTURES_DIR = REPO_ROOT / "tools" / "frgen" / "tests" / "fixtures"

EXTRACTION_PROMPT = PROMPTS_DIR / "hepsim5_extraction_prompt.md"
CROSSCHECK_PROMPT = PROMPTS_DIR / "hepsim5_crosscheck_prompt.md"

EXTRACTION_SNAPSHOT = FIXTURES_DIR / "hepsim5_extraction_prompt.snapshot.md"
CROSSCHECK_SNAPSHOT = FIXTURES_DIR / "hepsim5_crosscheck_prompt.snapshot.md"

EXPECTED_CHECKLIST_LINES = [
    "1. Overall normalisation: state whether each Sqrt or root factor is in the numerator or denominator, and quote the paper equation number.",
    "2. Field completeness: every new vector or scalar field must include a kinetic term and a mass term.",
    "3. Dimension counting: every operator with mass dimension above 4 must carry the matching 1/Lambda^n prefactor.",
    "4. Majorana or light-neutrino mass terms: use charge conjugation for each such mass term.",
    "5. SU(2) and U(1) conventions: state epsilon versus dagger structure for SU(2) doublet contractions, and keep U(1) charge signs consistent with the covariant-derivative convention.",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _checklist_lines(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip().startswith(("1. ", "2. ", "3. ", "4. ", "5. "))
    ]


def test_extraction_prompt_matches_snapshot() -> None:
    assert _read(EXTRACTION_PROMPT) == _read(EXTRACTION_SNAPSHOT)


def test_crosscheck_prompt_matches_snapshot() -> None:
    assert _read(CROSSCHECK_PROMPT) == _read(CROSSCHECK_SNAPSHOT)


def test_both_prompts_include_five_line_checklist() -> None:
    assert _checklist_lines(_read(EXTRACTION_PROMPT)) == EXPECTED_CHECKLIST_LINES
    assert _checklist_lines(_read(CROSSCHECK_PROMPT)) == EXPECTED_CHECKLIST_LINES


def test_crosscheck_prompt_requires_independent_rederive_and_benchmark() -> None:
    crosscheck_text = _read(CROSSCHECK_PROMPT)
    assert "Re-derive normalisations from the paper independently." in crosscheck_text
    assert "Do not read the extraction output first." in crosscheck_text
    assert (
        "Report a numeric normalisation value at benchmark point "
        "kappa_R = 1 and sin^2(theta_W) = 0.2312." in crosscheck_text
    )
