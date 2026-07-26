"""Unit tests for NormalizeYieldTool (toolgrad loop 14/17/18).

Covers: the per-event-weight arithmetic, the loop-17 `breakdown` block, the
bidirectional plausibility warnings (too-small yield, too-high efficiency), and
the loop-18 refusal of physically impossible inputs (efficiency > 1).
Runs without MG5/Pythia.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from tools.analysis.normalization import NormalizeYieldTool


def _run(**kw):
    return NormalizeYieldTool(**kw)._run()


def test_basic_weight_and_breakdown():
    r = json.loads(_run(cross_section_pb=0.03, n_generated=50000,
                        luminosity_fb=35.9, bin_counts=[60, 80, 60, 76]))
    assert r["status"] == "ok"
    # weight = sigma * 1000 * L / N
    assert abs(r["per_event_weight"] - (0.03 * 1000 * 35.9 / 50000)) < 1e-12
    assert r["raw_total"] == 276
    b = r["breakdown"]
    assert b["total_produced_at_lumi"] == 0.03 * 1000 * 35.9
    assert abs(b["selection_efficiency"] - 276 / 50000) < 1e-12
    assert abs(r["expected_yield"] - 276 * r["per_event_weight"]) < 1e-9
    # a healthy SR efficiency: no warnings
    assert "warning" not in r


def test_normalized_bins_scale_with_weight():
    r = json.loads(_run(cross_section_pb=1.0, n_generated=1000,
                        luminosity_fb=1.0, bin_counts=[1, 2, 3]))
    w = r["per_event_weight"]
    assert r["normalized_bin_counts"] == [1 * w, 2 * w, 3 * w]


def test_small_yield_warns():
    # 211 raw events but a tiny cross-section -> implausibly small yield
    r = json.loads(_run(cross_section_pb=1.05e-7, n_generated=50000,
                        luminosity_fb=35.9, bin_counts=[15, 24, 172]))
    assert r["status"] == "ok"
    assert "warning" in r and "SMALL" in r["warning"]


def test_high_efficiency_warns():
    # 60% selection efficiency -> selection likely not applied / missing BR
    r = json.loads(_run(cross_section_pb=0.03, n_generated=50000,
                        luminosity_fb=35.9, bin_counts=[10000, 10000, 10000]))
    assert r["status"] == "ok"
    assert "warning" in r and "efficiency" in r["warning"].lower()


def test_refuse_efficiency_gt_one():
    # more selected than generated is impossible -> format_error (raw string)
    out = _run(cross_section_pb=0.03, n_generated=1000,
               luminosity_fb=35.9, bin_counts=[5000])
    assert "Impossible Normalization" in out
    assert "efficiency > 1" in out


def test_rejects_bad_inputs():
    assert "Invalid Input" in _run(cross_section_pb=-1, n_generated=1000,
                                   luminosity_fb=35.9, bin_counts=[5])
    assert "Invalid Input" in _run(cross_section_pb=0.03, n_generated=0,
                                   luminosity_fb=35.9, bin_counts=[5])
    assert "Invalid Input" in _run(cross_section_pb=0.03, n_generated=1000,
                                   luminosity_fb=35.9, bin_counts=[])


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print(f"[ok] {name}")
    print("all normalization tests passed")
