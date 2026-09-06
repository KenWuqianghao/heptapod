"""
Regression tests for EffLRSM Eq.8 sqrt normalization placement.
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[3]
sys.path.insert(0, str(REPO_ROOT / "tools" / "frgen"))

from efflrsm_normalization_probe import (  # noqa: E402
    NormalizationProbeError,
    enforce_efflrsm_precheck,
    probe_normalization_ratio,
)

FIXTURE_PATH = SCRIPT_PATH.parent / "fixtures" / "efflrsm_sqrt_regression.json"


def _load_fixture() -> dict:
    with open(FIXTURE_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def test_wrong_form_fails_and_correct_form_passes() -> None:
    fixture = _load_fixture()
    wrong = {item["name"]: item["value"] for item in fixture["wrong_json_entries"]}
    reference = {
        "gZRq": fixture["reference_couplings"]["paper_eq8_quark"],
        "gZRl": fixture["reference_couplings"]["paper_eq8_lepton"],
    }

    quark_probe = probe_normalization_ratio(
        wrong["gZRq"],
        reference["gZRq"],
        kappa_symbol="kRquark",
    )
    assert quark_probe.extracted_factor == pytest.approx(0.8362, abs=5e-4)
    assert quark_probe.reference_factor == pytest.approx(1.1959, abs=5e-4)
    assert quark_probe.ratio == pytest.approx(0.6990, abs=5e-4)
    assert quark_probe.rate_ratio == pytest.approx(0.49, abs=5e-3)

    with pytest.raises(NormalizationProbeError, match="Crosscheck must fail"):
        enforce_efflrsm_precheck(
            wrong,
            fixture["crosscheck_couplings"],
            reference,
        )

    corrected = {
        "gZRq": fixture["reference_couplings"]["ruiz_quark"],
        "gZRl": fixture["reference_couplings"]["ruiz_lepton"],
    }
    report = enforce_efflrsm_precheck(corrected, corrected, reference)
    assert report["gZRq"].ratio == pytest.approx(1.0, abs=1e-9)
    assert report["gZRl"].ratio == pytest.approx(1.0, abs=1e-9)


def test_probe_does_not_modify_chiral_coefficients() -> None:
    fixture = _load_fixture()
    extracted = {item["name"]: item["value"] for item in fixture["wrong_json_entries"]}
    extracted.update(fixture["chiral_coefficients"])
    extracted_before = copy.deepcopy(extracted)

    reference = {
        "gZRq": fixture["reference_couplings"]["paper_eq8_quark"],
        "gZRl": fixture["reference_couplings"]["paper_eq8_lepton"],
    }
    with pytest.raises(NormalizationProbeError):
        enforce_efflrsm_precheck(extracted, extracted, reference)

    assert extracted == extracted_before
    assert extracted["gZRuL"] == fixture["chiral_coefficients"]["gZRuL"]
    assert extracted["gZRuR"] == fixture["chiral_coefficients"]["gZRuR"]


def test_crosscheck_precheck_rejects_shared_error() -> None:
    fixture = _load_fixture()
    wrong = {item["name"]: item["value"] for item in fixture["wrong_json_entries"]}
    reference = {
        "gZRq": fixture["reference_couplings"]["paper_eq8_quark"],
        "gZRl": fixture["reference_couplings"]["paper_eq8_lepton"],
    }
    with pytest.raises(NormalizationProbeError, match="agree with each other"):
        enforce_efflrsm_precheck(wrong, fixture["crosscheck_couplings"], reference)
