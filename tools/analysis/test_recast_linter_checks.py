"""Unit tests for the toolgrad RecastLinter checks (loops 14/17).

Covers the answer-free checks added for recast QA: normalization
self-consistency, cross-section magnitude, plausible yield, and re-surfacing
MadGraph generation warnings. The linter never consults the reference.
"""
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from tools.analysis.recast_linter import RecastLinterTool


def _hist(d, name, values):
    os.makedirs(os.path.join(d, "results"), exist_ok=True)
    p = os.path.join(d, "results", name)
    json.dump({"dependent_variables": [{"values": [{"value": v} for v in values]}]}, open(p, "w"))
    return os.path.join("results", name)


def _checks(out):
    return {c["name"]: c for c in json.loads(out)["checks"]}


def test_normalization_consistency_flags_1000x():
    d = tempfile.mkdtemp()
    h = _hist(d, "h.json", [0.00058, 0.0013, 0.0017, 0.0024])  # 1000x too small
    out = RecastLinterTool(histogram_path=h, cross_section_pb=0.02988,
                           n_generated=50000, luminosity_fb=35.9,
                           raw_selected_total=276, base_directory=d)._run()
    c = _checks(out)["normalization_consistency"]
    assert c["status"] == "fail" and "1000" in c["message"] or "pb->fb" in c["message"]


def test_normalization_consistency_passes_correct():
    d = tempfile.mkdtemp()
    h = _hist(d, "h.json", [0.58, 1.3, 1.7, 2.4])
    out = RecastLinterTool(histogram_path=h, cross_section_pb=0.02988,
                           n_generated=50000, luminosity_fb=35.9,
                           raw_selected_total=276, base_directory=d)._run()
    assert _checks(out)["normalization_consistency"]["status"] == "pass"


def test_cross_section_magnitude_warns_tiny():
    d = tempfile.mkdtemp()
    h = _hist(d, "h.json", [1e-6, 2e-6])
    out = RecastLinterTool(histogram_path=h, cross_section_pb=1e-7,
                           n_generated=50000, luminosity_fb=35.9, base_directory=d)._run()
    assert _checks(out)["cross_section_magnitude"]["status"] == "warn"


def test_plausible_yield_warns_tiny_total():
    d = tempfile.mkdtemp()
    h = _hist(d, "h.json", [1.1e-6, 1.8e-6, 1.3e-5])  # normalized, ~0 total
    out = RecastLinterTool(histogram_path=h, cross_section_pb=1e-7,
                           n_generated=50000, luminosity_fb=35.9, base_directory=d)._run()
    assert _checks(out)["plausible_yield"]["status"] == "warn"


def test_generation_warnings_resurfaced():
    d = tempfile.mkdtemp()
    h = _hist(d, "h.json", [0.5, 1.0])
    mg = os.path.join(d, "mg_manifest.json")
    json.dump({"warnings": ["No spectrum was set ... stock/DEFAULT masses"],
               "outputs": {"spectrum_bsm": {"1000021": 1500.0}}}, open(mg, "w"))
    out = RecastLinterTool(histogram_path=h, madgraph_manifest_path="mg_manifest.json",
                           base_directory=d)._run()
    c = _checks(out)["generation_warnings"]
    assert c["status"] == "fail" and "DEFAULT" in c["message"]


def test_no_madgraph_manifest_no_genwarn_check():
    d = tempfile.mkdtemp()
    h = _hist(d, "h.json", [0.5, 1.0])
    out = RecastLinterTool(histogram_path=h, base_directory=d)._run()
    assert "generation_warnings" not in _checks(out)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print(f"[ok] {name}")
    print("all recast_linter check tests passed")
