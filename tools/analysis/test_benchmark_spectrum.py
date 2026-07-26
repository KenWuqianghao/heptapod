"""Unit tests for ResolveBenchmarkSpectrumTool (toolgrad loop 16).

Parses the GeV masses encoded in a SUSY simplified-model benchmark point name.
No leakage of any reference/answer — only the masses already in the name.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from tools.analysis.benchmark_spectrum import ResolveBenchmarkSpectrumTool


def _run(name):
    return json.loads(ResolveBenchmarkSpectrumTool(benchmark_name=name)._run())


def test_two_mass_point():
    r = _run("T5Wg_1600_100")
    assert r["topology"] == "T5Wg"
    assert r["masses"] == [1600.0, 100.0]
    assert r["n_masses"] == 2


def test_embedded_digit_topology():
    # the leading topology token has its own digit (T5Wg/T6gg) — must not be
    # split there; only the trailing _<int> groups are masses.
    assert _run("T6gg_1750_1650")["topology"] == "T6gg"
    assert _run("T6gg_1750_1650")["masses"] == [1750.0, 1650.0]


def test_single_mass():
    r = _run("TChiWg_700")
    assert r["topology"] == "TChiWg" and r["masses"] == [700.0]


def test_electroweakino_point():
    r = _run("TChiWZ_550_200")
    assert r["topology"] == "TChiWZ" and r["masses"] == [550.0, 200.0]


def test_no_mass_suffix():
    r = _run("T2tt_comp")
    assert r["masses"] == []
    assert "default spectrum" in r["guidance"].lower() or "no mass" in r["guidance"].lower()


def test_empty_name_errors():
    assert "Invalid Input" in ResolveBenchmarkSpectrumTool(benchmark_name="")._run()


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print(f"[ok] {name}")
    print("all benchmark_spectrum tests passed")
