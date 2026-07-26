"""
# recast_linter.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json
import math
import os
from typing import List, Optional

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField


def _is_reco_jsonl(path: str) -> bool:
    """Heuristic: does this JSONL look like reco/Delphes output?

    Reco events carry detector-object collections (jets, electrons, muons,
    photons, met) rather than (or in addition to) a raw particle record.
    We sample the first parseable line and look for any such collection.
    """
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except Exception:
                    return False
                data = o.get("data", o) if isinstance(o, dict) else {}
                if not isinstance(data, dict):
                    return False
                reco_keys = {"jets", "electrons", "muons", "photons", "met"}
                return any(k in data for k in reco_keys)
    except Exception:
        return False
    return False


def _has_particle_record(path: str) -> bool:
    """Heuristic: does this JSONL carry a truth/particle-level record?"""
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except Exception:
                    return False
                data = o.get("data", o) if isinstance(o, dict) else {}
                if not isinstance(data, dict):
                    return False
                return "particles" in data
    except Exception:
        return False
    return False


def _load_histogram_values(path: str) -> Optional[List[Optional[float]]]:
    """Best-effort extraction of bin values from a results YAML/JSON.

    Avoids a hard YAML dependency: tries json, then a permissive YAML
    load if PyYAML is importable. Returns the first dependent-variable
    series' values, or None if nothing histogram-shaped is found.
    """
    try:
        with open(path, "r") as f:
            text = f.read()
    except Exception:
        return None

    docs = []
    # Try JSON first (a single doc).
    try:
        docs = [json.loads(text)]
    except Exception:
        try:
            import yaml  # type: ignore
            docs = list(yaml.safe_load_all(text))
        except Exception:
            return None

    for doc in docs:
        if not isinstance(doc, dict) or "dependent_variables" not in doc:
            continue
        deps = doc.get("dependent_variables") or []
        if not deps:
            continue
        series = deps[0]
        values: List[Optional[float]] = []
        for v in series.get("values", []) or []:
            raw = v.get("value") if isinstance(v, dict) else v
            if raw is None:
                values.append(None)
            else:
                try:
                    values.append(float(raw))
                except (TypeError, ValueError):
                    values.append(None)
        return values
    return None


class RecastLinterTool(BaseTool):
    """
    Presence-only, answer-free self-check the agent can run before declaring
    a ColliderBench recast "done".

    This is a PROCESS lint, NOT a grader: it NEVER consults the reference
    histogram and NEVER reveals whether the result is correct. It only
    inspects the agent's OWN sandbox artifacts for common recast mistakes
    and emits pass/warn advice. A clean report does not mean the answer is
    right; a warning flags a likely process error.

    Checks (each pass/warn with a short message):
      - observable provenance: a reco-level events file (Delphes/reco JSONL)
        should exist and the histogram should be built from it, not from the
        truth/particle record.
      - normalization applied: a histogram of suspiciously integer-valued raw
        counts looks unnormalized (apply sigma x lumi / N_generated). If the
        normalization inputs are supplied, the implied per-event weight is
        reported.
      - non-empty signal region: an all-zero / all-null histogram means the
        selection zeroed everything.
      - cross-section magnitude: a cross_section_pb orders of magnitude below
        the band expected for a collider signal flags a likely wrong process.
      - plausible yield: a normalized histogram summing to a tiny fraction of
        one event flags a likely cross-section/process error upstream.
      - generation warnings: if madgraph_manifest_path is given, re-surface any
        warnings MadGraph recorded (missing decay chain, default/stock spectrum)
        so they are not lost before the agent finishes; the realized BSM
        spectrum is echoed for a final benchmark-point cross-check.
      - decay completeness hint: a generic reminder to verify BSM particles
        decay.

    Inputs (all sandbox-relative, all optional):
      - reco_events_path: the reco/Delphes JSONL the observables were built from.
      - histogram_path: the results histogram YAML/JSON.
      - cross_section_pb / n_generated / luminosity_fb: normalization inputs;
        if all present, the implied per-event weight is reported.

    Output (JSON): {checks: [{name, status, message}], n_warnings}.
    """
    # --------------------------- Runtime fields --------------------------- #
    reco_events_path: Optional[str] = RuntimeField(
        default=None,
        description="Sandbox-relative path to the reco/Delphes events JSONL the observables were built from",
    )
    showered_events_path: str = RuntimeField(
        default="",
        description="Optional: sandbox-relative path to the SHOWERED events JSONL (Pythia output). If given, decay-completeness is checked for real — a final-state coloured BSM particle (gluino/squark) means the decay chain was left incomplete.",
    )
    histogram_path: Optional[str] = RuntimeField(
        default=None,
        description="Sandbox-relative path to the results histogram YAML/JSON",
    )
    cross_section_pb: Optional[float] = RuntimeField(
        default=None, description="Process cross section in pb (for the implied per-event weight)"
    )
    n_generated: Optional[int] = RuntimeField(
        default=None, description="Number of generated events (denominator of the per-event weight)"
    )
    luminosity_fb: Optional[float] = RuntimeField(
        default=None, description="Target integrated luminosity in fb^-1"
    )
    madgraph_manifest_path: str = RuntimeField(
        default="",
        description="Optional: sandbox-relative path to the MadGraph run's manifest.json. If given, any generation-time warnings it recorded (missing decay chain, default/stock spectrum) are re-surfaced here so they aren't lost before you finish.",
    )
    raw_selected_total: int = RuntimeField(
        default=-1,
        description="Optional: total RAW (unweighted) selected-event count summed over all histogram bins. If given together with cross_section_pb/n_generated/luminosity_fb, the linter cross-checks that your histogram's total normalized yield equals raw_selected_total * (sigma*1000*L/N_gen) — catching a normalization applied with the wrong (e.g. pb-vs-fb 1000x) factor.",
    )
    # ---------------------------------------------------------------------- #

    # ---------------------------- State fields ---------------------------- #
    base_directory: str = StateField(default=".", description="Base directory for safe paths")
    # ---------------------------------------------------------------------- #

    def _setup(self):
        self.base_directory = os.path.abspath(self.base_directory)
        if not os.path.exists(self.base_directory):
            raise ValueError(f"Base directory does not exist: {self.base_directory}")

    def _safe_path(self, rel: Optional[str]) -> Optional[str]:
        if not rel:
            return None
        full = os.path.abspath(os.path.join(self.base_directory, rel))
        return full if full.startswith(self.base_directory) else None

    def _run(self) -> str:
        checks: List[dict] = []

        def add(name: str, status: str, message: str):
            checks.append({"name": name, "status": status, "message": message})

        # ---------------- observable provenance ---------------- #
        # Robust to missing/escaping paths: a missing file is a warn, never a raise.
        reco_full = self._safe_path(self.reco_events_path)
        if not self.reco_events_path:
            add("observable_provenance", "warn",
                "No reco_events_path given; build observables from Delphes reco, "
                "not the particle record. Confirm a reco/Delphes JSONL exists.")
        elif reco_full is None:
            add("observable_provenance", "warn",
                "reco_events_path escapes the sandbox; cannot inspect it.")
        elif not os.path.exists(reco_full):
            add("observable_provenance", "warn",
                f"reco file '{self.reco_events_path}' not found; build observables "
                "from Delphes reco, not the particle record.")
        else:
            is_reco = _is_reco_jsonl(reco_full)
            has_truth = _has_particle_record(reco_full)
            if is_reco:
                add("observable_provenance", "pass",
                    f"'{self.reco_events_path}' carries reco-level objects "
                    "(jets/leptons/photons/met).")
            elif has_truth:
                add("observable_provenance", "warn",
                    f"'{self.reco_events_path}' looks like a truth/particle-level "
                    "record, not reco. Build observables from Delphes reco, not the "
                    "particle record.")
            else:
                add("observable_provenance", "warn",
                    f"could not confirm reco-level objects in '{self.reco_events_path}'; "
                    "build observables from Delphes reco, not the particle record.")

        # ---------------- normalization applied ---------------- #
        hist_full = self._safe_path(self.histogram_path)
        values: Optional[List[Optional[float]]] = None
        if self.histogram_path and hist_full and os.path.exists(hist_full):
            values = _load_histogram_values(hist_full)

        if not self.histogram_path:
            add("normalization_applied", "warn",
                "No histogram_path given; ensure yields are normalized via "
                "sigma x lumi / N_generated (e.g. with NormalizeYield).")
        elif hist_full is None:
            add("normalization_applied", "warn",
                "histogram_path escapes the sandbox; cannot inspect it.")
        elif not os.path.exists(hist_full):
            add("normalization_applied", "warn",
                f"histogram '{self.histogram_path}' not found; cannot check normalization.")
        elif values is None:
            add("normalization_applied", "warn",
                f"could not parse a histogram out of '{self.histogram_path}'; "
                "ensure it has a dependent_variables series.")
        else:
            nonnull = [v for v in values if v is not None]
            if not nonnull:
                add("normalization_applied", "warn",
                    "histogram has no non-null bins; cannot check normalization.")
            else:
                looks_integer = all(
                    abs(v - round(v)) < 1e-9 for v in nonnull
                )
                if looks_integer and any(v != 0 for v in nonnull):
                    add("normalization_applied", "warn",
                        "bin values look like raw counts (all integer-valued) — "
                        "apply sigma x lumi / N_generated, e.g. with NormalizeYield.")
                else:
                    add("normalization_applied", "pass",
                        "bin values are non-integer normalized yields (not raw counts).")

        # Report the implied per-event weight if the inputs are all present.
        if (self.cross_section_pb is not None and self.n_generated is not None
                and self.luminosity_fb is not None):
            try:
                xsec = float(self.cross_section_pb)
                n_gen = int(self.n_generated)
                lumi = float(self.luminosity_fb)
                if n_gen > 0:
                    w = (xsec * 1000.0 * lumi) / n_gen
                    add("per_event_weight", "pass",
                        f"implied per-event weight = sigma*1000*L/N_gen = {w:.6g} "
                        f"(sigma={xsec} pb, L={lumi} fb^-1, N_gen={n_gen}).")
                else:
                    add("per_event_weight", "warn",
                        "n_generated must be positive to compute a per-event weight.")
            except (TypeError, ValueError):
                add("per_event_weight", "warn",
                    "non-numeric normalization input; cannot compute per-event weight.")

        # ---------------- normalization self-consistency ---------------- #
        # The single highest-value check: with the correct per-event weight
        # w = sigma*1000*L/N_gen and the RAW selected total, the histogram's
        # total normalized yield MUST equal raw_total * w. A large mismatch
        # means the applied normalization used the wrong factor (classically the
        # pb->fb 1000x), which keeps the SHAPE right but the absolute scale wrong
        # — exactly the failure that cost the one near-miss trial its score.
        # This never consults the reference; it is purely internal consistency.
        try:
            rst = int(self.raw_selected_total)
        except (TypeError, ValueError):
            rst = -1
        if (rst > 0 and values is not None and self.cross_section_pb is not None
                and self.n_generated is not None and self.luminosity_fb is not None):
            try:
                w = (float(self.cross_section_pb) * 1000.0 * float(self.luminosity_fb)
                     / int(self.n_generated))
                expected_total = rst * w
                actual_total = sum(v for v in values if v is not None)
                if expected_total > 0 and actual_total > 0:
                    ratio = actual_total / expected_total
                    if ratio < 0.5 or ratio > 2.0:
                        add("normalization_consistency", "fail",
                            f"normalized total ({actual_total:.4g}) is {ratio:.3g}x the "
                            f"expected raw_total*sigma*1000*L/N_gen ({expected_total:.4g}). "
                            "The shape may be right but the absolute scale is off — most "
                            "often the pb->fb 1000x factor was dropped. Re-derive the yield "
                            "with NormalizeYield (it applies sigma*1000*L/N_gen).")
                    else:
                        add("normalization_consistency", "pass",
                            f"normalized total ({actual_total:.4g}) matches expected "
                            f"({expected_total:.4g}) within 2x.")
            except (TypeError, ValueError, ZeroDivisionError):
                pass

        # ---------------- cross-section magnitude ---------------- #
        # A reported cross-section many orders of magnitude outside the band
        # expected for a collider signal usually means the WRONG process was
        # generated (e.g. a single squark flavour stood in for gluino-pair).
        # Generic: keys on the magnitude only, no task/process specifics.
        if self.cross_section_pb is not None:
            try:
                xs = float(self.cross_section_pb)
                if xs <= 0:
                    add("cross_section_magnitude", "warn",
                        "cross_section_pb is zero/negative — re-read it from the "
                        "MadGraph banner.")
                elif xs < 1e-5:
                    add("cross_section_magnitude", "warn",
                        f"cross-section {xs:g} pb is very small for a collider signal "
                        "(TeV-scale coloured pair-production is ~1e-3 pb). If it is "
                        "orders of magnitude below your naive estimate, you likely "
                        "generated the wrong process — verify the production mechanism "
                        "and final state match the requested signal.")
                else:
                    add("cross_section_magnitude", "pass",
                        f"cross-section {xs:g} pb is within the plausible range.")
            except (TypeError, ValueError):
                pass

        # ---------------- implausible total yield ---------------- #
        # If the normalized histogram sums to a tiny fraction of one event, the
        # result is almost never a valid physics answer (normally a cross-section
        # magnitude error upstream). Only meaningful once values look normalized.
        if values is not None:
            nn = [v for v in values if v is not None]
            total = sum(nn) if nn else 0.0
            looks_norm = bool(nn) and not all(abs(v - round(v)) < 1e-9 for v in nn)
            if looks_norm and 0 < total < 1e-2:
                add("plausible_yield", "warn",
                    f"total normalized yield is {total:.3g} events — implausibly "
                    "small. This usually points to a wrong cross-section magnitude "
                    "or the wrong generated process, not a selection detail.")

        # ---------------- non-empty signal region ---------------- #
        if values is not None:
            nonnull = [v for v in values if v is not None]
            if not values or all(v is None for v in values):
                add("non_empty_signal_region", "warn",
                    "histogram is all-null — selection zeroed everything; check "
                    "object multiplicities / decay completeness.")
            elif all((v is None or v == 0) for v in values):
                add("non_empty_signal_region", "warn",
                    "histogram is all-zero — selection zeroed everything; check "
                    "object multiplicities / decay completeness.")
            else:
                add("non_empty_signal_region", "pass",
                    f"{len(nonnull)} non-null bin(s), {sum(1 for v in nonnull if v != 0)} "
                    "non-zero.")

        # ---------------- decay completeness ---------------- #
        # If the showered events are provided, actually CHECK: a final-state
        # (status==1) coloured BSM particle — a gluino (1000021) or squark
        # (1000001-1000006, 2000001-2000006) — is unambiguously a broken decay
        # chain (coloured states must hadronize/decay; they can never be a
        # stable final state). This catches the bare `p p > go go` failure mode
        # generally. (Neutral exotics like a neutralino can legitimately be the
        # stable LSP, so they are not flagged here — for those, see the
        # model-specific reminder.)
        _COLOURED_BSM = set(range(1000001, 1000007)) | set(range(2000001, 2000007)) | {1000021}
        sh_rel = (self.showered_events_path or "").strip()
        if sh_rel:
            sh_path = self._safe_path(sh_rel)
            if sh_path is None or not os.path.exists(sh_path):
                add("decay_completeness", "warn",
                    f"showered_events_path {sh_rel!r} not found — cannot verify "
                    "decay completeness; verify no stable coloured exotics remain.")
            else:
                n_evt = 0
                stable_coloured = {}
                try:
                    with open(sh_path, errors="replace") as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                o = json.loads(line)
                            except Exception:
                                continue
                            d = o.get("data") if isinstance(o.get("data"), dict) else o
                            for p in (d.get("particles") or []):
                                if int(p.get("status", 0)) == 1 and abs(int(p.get("id", 0))) in _COLOURED_BSM:
                                    pid = abs(int(p["id"]))
                                    stable_coloured[pid] = stable_coloured.get(pid, 0) + 1
                            n_evt += 1
                            if n_evt >= 500:
                                break
                except Exception as e:
                    stable_coloured = {}
                if stable_coloured:
                    add("decay_completeness", "fail",
                        f"BROKEN DECAY CHAIN: coloured BSM particle(s) left STABLE in "
                        f"the shower (final-state) over {n_evt} events: {stable_coloured}. "
                        "Coloured states must hadronize/decay — regenerate with the "
                        "full decay chain down to SM final states (e.g. "
                        "`p p > go go, (go > q q~ n1)`), not a bare `p p > go go`.")
                else:
                    add("decay_completeness", "pass",
                        f"no stable coloured BSM particles in {n_evt} showered events.")
        else:
            add("decay_completeness", "warn",
                "Reminder: verify all BSM particles decay (no stable exotics in the "
                "shower) — a particle the LHE left stable will not produce its "
                "decay-product objects. Pass showered_events_path to check this.")

        # ---------------- re-surface generation warnings ---------------- #
        # The MadGraph tool records non-fatal warnings (missing decay chain,
        # default/stock spectrum) in its manifest. They are easy to skip at
        # generation time; re-surface them here, at the final QA gate, so a
        # wrong spectrum or undecayed process can't slip through silently.
        mg_rel = (self.madgraph_manifest_path or "").strip()
        if mg_rel:
            mg_full = self._safe_path(mg_rel)
            if mg_full is None or not os.path.exists(mg_full):
                add("generation_warnings", "warn",
                    f"madgraph_manifest_path {mg_rel!r} not found — cannot re-check "
                    "generation-time warnings.")
            else:
                try:
                    mg = json.load(open(mg_full))
                except Exception:
                    mg = {}
                mg_warns = mg.get("warnings") or []
                spectrum = (mg.get("outputs") or {}).get("spectrum_bsm") or {}
                if mg_warns:
                    add("generation_warnings", "fail",
                        "MadGraph reported generation-time warning(s) that must be "
                        "resolved before trusting this result: " + " | ".join(mg_warns))
                else:
                    msg = "no generation-time warnings recorded by MadGraph."
                    if spectrum:
                        msg += " Realized BSM spectrum: " + ", ".join(
                            f"{k}={v:g}" for k, v in spectrum.items()) + \
                            " — confirm these match your benchmark point."
                    add("generation_warnings", "pass", msg)

        n_warnings = sum(1 for c in checks if c["status"] == "warn")
        n_failures = sum(1 for c in checks if c["status"] == "fail")
        result = {"checks": checks, "n_warnings": n_warnings, "n_failures": n_failures}
        return json.dumps(result, separators=(",", ":"), ensure_ascii=False)
