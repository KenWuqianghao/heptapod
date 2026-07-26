"""
# normalization.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json
from typing import Optional, List

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField


class NormalizeYieldTool(BaseTool):
    """
    Normalize raw MC counts to an expected physics yield for an integrated
    luminosity.

    Closes the absolute-normalization gap: a correct selection *shape* still
    fails within_tolerance until it is scaled by sigma x lumi / N_generated.

    Expected yield = raw_count * (cross_section_pb * 1000 fb/pb * luminosity_fb)
                                 / n_generated

    The factor 1000 converts pb to fb so it matches luminosity_fb. The per-event
    weight is w = cross_section_pb * 1000 * luminosity_fb / n_generated, and the
    yield is simply raw_count * w (applied per bin for histograms).

    Inputs (runtime):
      - cross_section_pb: process cross section in pb (from MG5 log / banner).
      - n_generated: number of generated events (the denominator).
      - luminosity_fb: target integrated luminosity in fb^-1.
      - bin_counts: raw per-bin counts as a list of integers, e.g.
        [12, 8, 3, 1]. For a single scalar yield, pass a one-element list,
        e.g. [42]. ALWAYS a list — there is no separate scalar field.

    Output (JSON): per_event_weight, raw_total, normalized_bin_counts (the
    luminosity-normalized per-bin yields), and expected_yield (their sum).

    LLM-UX note: the inputs are deliberately minimal and unambiguous — one
    required list (`bin_counts`). Earlier this tool had a `n_passed` XOR
    `bin_counts` pair; the framework marked both required + non-nullable, so
    nulling the unused one failed schema validation and the agent gave up and
    hand-rolled. A single list field removes that trap.
    """
    # --------------------------- Runtime fields --------------------------- #
    cross_section_pb: float = RuntimeField(description="Process cross section in pb (read from the MadGraph banner/results)")
    n_generated: int = RuntimeField(description="Number of generated events (denominator of the per-event weight)")
    luminosity_fb: float = RuntimeField(description="Target integrated luminosity in fb^-1")
    bin_counts: List[int] = RuntimeField(description="Raw per-bin selected-event counts as a list of ints, e.g. [12,8,3,1]. For a single scalar yield pass a one-element list, e.g. [42].")
    # ---------------------------------------------------------------------- #

    # ---------------------------- State fields ---------------------------- #
    base_directory: str = StateField(default=".", description="Base directory (unused; for harness consistency)")
    # ---------------------------------------------------------------------- #

    def _setup(self):
        pass

    def _run(self) -> str:
        # Validate numeric inputs.
        try:
            xsec = float(self.cross_section_pb)
            n_gen = int(self.n_generated)
            lumi = float(self.luminosity_fb)
        except (TypeError, ValueError) as e:
            return self.format_error(error="Invalid Input", reason=f"non-numeric input: {e}")

        if n_gen <= 0:
            return self.format_error(
                error="Invalid Input",
                reason="n_generated must be a positive integer",
                suggestion="n_generated is the denominator of the per-event weight; it cannot be zero or negative."
            )
        if xsec < 0:
            return self.format_error(error="Invalid Input", reason="cross_section_pb must be non-negative")
        if lumi < 0:
            return self.format_error(error="Invalid Input", reason="luminosity_fb must be non-negative")

        # bin_counts: always a list of ints (scalar yield = single-element list).
        bc = self.bin_counts
        if bc is None or (isinstance(bc, (list, tuple)) and len(bc) == 0):
            return self.format_error(
                error="Invalid Input",
                reason="bin_counts is empty or missing",
                suggestion="Pass the raw per-bin selected-event counts as a list, "
                           "e.g. bin_counts=[12,8,3,1]; for a single scalar yield "
                           "pass a one-element list, e.g. bin_counts=[42].")
        try:
            bins = [int(c) for c in bc]
        except (TypeError, ValueError):
            return self.format_error(
                error="Invalid Input",
                reason=f"bin_counts must be a list of integers, got {bc!r}",
                suggestion="e.g. bin_counts=[12,8,3,1]")
        if any(c < 0 for c in bins):
            return self.format_error(error="Invalid Input",
                                     reason="bin_counts entries must be non-negative")

        # REFUSE physically impossible inputs (the c017 normalization errors were
        # ~10^6x off — garbage weights — and warnings alone were ignored). The
        # clearest impossibility: more events SELECTED than GENERATED, i.e. a
        # selection efficiency > 1. That means bin_counts and n_generated refer to
        # different samples (a units/count mismatch) and the yield is meaningless.
        raw_total = sum(bins)
        if raw_total > n_gen:
            return self.format_error(
                error="Impossible Normalization",
                reason=(f"raw selected events ({raw_total}) exceed n_generated ({n_gen}) "
                        "— selection efficiency > 1 is impossible."),
                suggestion=("bin_counts must be the RAW counts selected from THIS "
                            "generated sample, and n_generated its size. You likely "
                            "passed already-normalized/weighted values, or counts from a "
                            "different sample. Pass the raw integer counts and the matching "
                            "n_generated."))

        # Per-event weight: pb -> fb via *1000, times lumi[fb^-1], over N_gen.
        per_event_weight = (xsec * 1000.0 * lumi) / n_gen
        expected_yield = raw_total * per_event_weight

        # SHOW THE ARITHMETIC. The yield is a product of four factors and the
        # agent's repeated normalization errors (both too-high and too-low) come
        # from getting ONE of them wrong (often a missing branching ratio folded
        # into the cross-section, or a selection that isn't actually applied).
        # Surfacing each factor lets the agent sanity-check magnitudes itself.
        # No reference is consulted — this is pure internal arithmetic.
        total_produced = xsec * 1000.0 * lumi          # events produced at L, pre-selection
        efficiency = raw_total / n_gen if n_gen else 0.0
        breakdown = {
            "cross_section_pb": xsec,
            "luminosity_fb": lumi,
            "n_generated": n_gen,
            "total_produced_at_lumi": total_produced,   # = sigma * 1000 * L
            "raw_selected": raw_total,
            "selection_efficiency": efficiency,         # = raw_selected / n_generated
            "expected_yield": expected_yield,           # = total_produced * efficiency
        }
        result = {
            "status": "ok",
            "per_event_weight": per_event_weight,
            "raw_total": raw_total,
            "normalized_bin_counts": [c * per_event_weight for c in bins],
            "expected_yield": expected_yield,
            "breakdown": breakdown,
        }

        # Bidirectional magnitude sanity (non-fatal; status stays "ok"). The agent
        # otherwise sees only a number and no nudge that it is implausible.
        warnings = []
        if raw_total >= 10 and 0 < expected_yield < 1e-2:
            warnings.append(
                f"Implausibly SMALL yield: {raw_total} raw events selected but only "
                f"{expected_yield:.3g} expected at L={lumi:g} fb^-1. The cross-section "
                f"({xsec:g} pb) is likely wrong by orders of magnitude — check it against "
                "a naive estimate (TeV-scale coloured pair-production ~1e-3 pb) and that "
                "you generated the requested signal, not a different/leptonic process.")
        # A selection efficiency near 1 means the cuts barely removed anything —
        # for a specific signal region (especially a leptonic/photon one whose
        # branching ratio is small) that is almost always a selection NOT applied
        # or a missing object requirement, which inflates the yield.
        if efficiency > 0.5:
            warnings.append(
                f"Selection efficiency is {efficiency*100:.0f}% (raw_selected/n_generated) "
                "— implausibly high for a signal region. Confirm your full selection is "
                "actually applied, and that required leptons/photons (whose branching "
                "ratios suppress the yield) are demanded — a missing requirement makes "
                "the yield too high.")
        if warnings:
            result["warning"] = warnings[0]
            result["warnings"] = warnings
        return json.dumps(result, separators=(",", ":"), ensure_ascii=False)
