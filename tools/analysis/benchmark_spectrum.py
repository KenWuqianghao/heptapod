"""
# benchmark_spectrum.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json
import re
from typing import List

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField


class ResolveBenchmarkSpectrumTool(BaseTool):
    """
    Parse the mass values a SUSY simplified-model benchmark POINT NAME encodes,
    so the agent sets the right spectrum instead of guessing or running defaults.

    Simplified-model points are named `<Topology>_<m1>[_<m2>...]`, where the
    trailing integers are GeV masses of the produced sparticle and the lighter
    state(s) it decays to — e.g. `T5Wg_1600_100` -> gluino 1600 GeV, LSP 100 GeV;
    `T6gg_1750_1650` -> squark 1750, neutralino 1650; `TChiWZ_550_200`. This tool
    does NOT reveal the answer (cross-sections, yields, or reference histogram) —
    it only echoes back the masses already present in the task's own point name,
    which several trials parsed wrong or skipped (running the model's default
    spectrum). Use it, then set these as BLOCK MASS in your param_card (or via
    `set mass <pdg> <GeV>`), and confirm them in MadGraph's echoed `spectrum_bsm`.

    Input (runtime):
      - benchmark_name: the point name, e.g. "T5Wg_1600_100". (You can paste the
        task's `Signal benchmark` value verbatim.)

    Output (JSON): {topology, masses: [GeV...], n_masses, guidance}.
    """
    benchmark_name: str = RuntimeField(
        description="The SUSY simplified-model benchmark point name, e.g. 'T5Wg_1600_100' (trailing integers are GeV masses).")
    base_directory: str = StateField(default=".", description="Base directory (unused; for harness consistency)")

    def _setup(self):
        pass

    def _run(self) -> str:
        name = (self.benchmark_name or "").strip()
        if not name:
            return self.format_error(error="Invalid Input", reason="benchmark_name is empty",
                                     suggestion="Pass the task's 'Signal benchmark', e.g. 'T5Wg_1600_100'.")
        # Topology = leading non-numeric token; masses = the trailing integers.
        nums = re.findall(r"(?<![\d.])(\d{2,5})(?:\.0+)?(?![\d.])", name)
        masses = [float(n) for n in nums]
        # Topology = name with trailing _<int> mass groups stripped (keeps any
        # embedded digit in the topology token itself, e.g. T5Wg, T6gg).
        topo = re.sub(r"(_\d{2,5})+$", "", name) or name
        if not masses:
            return json.dumps({
                "status": "ok", "topology": topo, "masses": [], "n_masses": 0,
                "guidance": ("No mass integers found in the benchmark name. If the "
                             "task names specific masses elsewhere, set them explicitly "
                             "in the param_card; do NOT run the model's default spectrum."),
            }, separators=(",", ":"))
        return json.dumps({
            "status": "ok",
            "topology": topo,
            "masses": masses,
            "n_masses": len(masses),
            "guidance": (
                f"The benchmark point '{name}' specifies {len(masses)} mass value(s) "
                f"(GeV): {masses}. Convention: the first is the pair-produced sparticle "
                "(e.g. gluino/squark/chargino), the rest are the lighter state(s) it "
                "decays to (down to the LSP). Set these as BLOCK MASS in your param_card "
                "(or `set mass <pdg> <GeV>`) for the states in your generated process, "
                "then verify them in MadGraph's echoed `spectrum_bsm`. Do NOT leave the "
                "model's default masses — a default spectrum fails the benchmark."),
        }, separators=(",", ":"))
