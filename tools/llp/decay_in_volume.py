"""
# decay_in_volume.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json
import os
from typing import List, Optional

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField

YIELDS_SCHEMA_VERSION = "llpyields-1.0"
AUDIT_SCHEMA_VERSION = "llpaudit-1.0"
CONVENTIONS = {
    "two_track": "midpoint",
    "weight": "g2_stripped",
    "propagation": "straight_line_from_primary_vertex",
}

# numpy / yaml-backed physics is deferred to _run() so module import does
# not pull in numpy's cold load (heptapod toolkit startup convention).


class DecayInVolumeTool(BaseTool):
    """
    Compute decay-in-volume LLP signal yields over a coupling grid with
    built-in exact g^2 reweighting, from g^2-stripped weighted events.

    **Purpose:**
    Turn a phi flux sample (LLPFluxFromMesonDecayTool output; multiple
    channels may be concatenated into one file) into N_sig(g) for every
    coupling in g_grid — the convention-sensitive step of a reach study.
    Because production scales as g^2, the total width as g^2, and the
    kinematics are g-independent, one event set covers the whole g axis
    exactly: N_sig(g) = N_int * g^2 * sum_i w_i * P_dec,i(g) * twotrack_i.

    **Inputs (runtime):**
    - events_path: line-delimited JSON events with per-record fields
      E, px, py, pz (GeV) and event_weight_g2_stripped (per primary
      interaction); parent_channel is carried through to the audit file
      if present. An empty file (kinematically closed channel) yields
      zeros, not an error.
    - geometry_path: YAML with z_min_m, z_max_m, r_volume_m (on-axis
      cylindrical decay volume) and z_det_m, r_det_m (downstream detector
      plane), all in meters from the primary vertex. The geometry file,
      like the kernel, carries the entire experimental setting.
    - m_phi_gev, m_mu_gev: LLP and muon masses in GeV.
    - width_ref_gev: Gamma_tot(phi) at g = 1 (g^2-stripped reference
      width); ctau(g) = hbar*c / (g^2 * width_ref_gev).
    - g_grid: list of couplings at which to evaluate N_sig.
    - n_int: number of primary interactions (sigma_inel * L_int for a
      collider setting, N_POT for a beam dump).
    - require_two_track: apply the two-track acceptance (default true).
      If false the acceptance factor is 1 and the audit column is null.
    - seed: RNG seed for the isotropic phi -> mu mu decay sampling.
    - output_path: where to write the yields table (JSON).

    **Behavior (declared conventions, mirrored from the validated
    reference pipeline):**
    - The phi travels in a straight line from the primary vertex at its
      lab angle; the parent flight length is absorbed into the kernel
      (decaying-parents-only normalization).
    - In-volume segment [L1, L2] = intersection of the ray with the
      on-axis cylinder; P_dec(g) = exp(-L1/lam) - exp(-L2/lam) with
      lam = beta*gamma*ctau(g) and beta*gamma = |p|/m_phi.
    - Two-track acceptance at the decay-volume MIDPOINT convention
      (g-independent, preserving exact reweighting): one isotropic
      phi -> mu+ mu- decay is sampled per event at the midpoint of
      [L1, L2], both muons are boosted to the lab and propagated to the
      z_det plane, and both must satisfy r < r_det moving forward.
    - Weights are g^2-stripped per primary interaction; the g^2 from
      production is applied here, the g^2 in the lifetime enters through
      P_dec.

    **Output (JSON string):**
    - status: "ok" on success.
    - n_events: number of event records read.
    - n_pass_geometry: events whose ray intersects the decay volume.
    - n_pass_two_track: events passing geometry AND two-track acceptance
      (these are the contributing events).
    - yields: [{g, n_sig}] over g_grid (expected signal decays).
    - output_path: yields table JSON (per-g rows + conventions block).
    - audit_path: per-event audit file (line-delimited JSON) with
      event_id, parent_channel, event_weight_g2_stripped, beta_gamma,
      L1_m, L2_m, geom_pass, two_track_pass, plus p_decay and the
      weighted contribution evaluated at g_ref = g_grid[0].
    - conventions: {two_track: "midpoint", weight: "g2_stripped"}.
    """
    # --------------------------- Runtime fields --------------------------- #
    events_path: str = RuntimeField(
        description="Path to line-delimited JSON events with E, px, py, pz "
                    "and event_weight_g2_stripped (concatenation of "
                    "multiple channels is fine)")
    geometry_path: str = RuntimeField(
        description="Path to geometry YAML (z_min_m, z_max_m, r_volume_m, "
                    "z_det_m, r_det_m in meters)")
    m_phi_gev: float = RuntimeField(
        description="LLP (phi) mass in GeV")
    m_mu_gev: float = RuntimeField(
        default=0.1056584,
        description="Muon mass in GeV (default 0.1056584)")
    width_ref_gev: float = RuntimeField(
        description="Gamma_tot(phi) at g = 1 in GeV (g^2-stripped "
                    "reference width for the ctau reweighting)")
    g_grid: List[float] = RuntimeField(
        description="Couplings g at which to evaluate N_sig (exact "
                    "reweighting: one event set covers the whole list)")
    n_int: float = RuntimeField(
        description="Number of primary interactions (sigma_inel * L_int "
                    "for a collider, N_POT for a beam dump)")
    require_two_track: bool = RuntimeField(
        default=True,
        description="Apply the midpoint two-track acceptance (default "
                    "true)")
    seed: int = RuntimeField(
        default=1,
        description="RNG seed for the isotropic phi -> mu mu decay "
                    "sampling (default 1)")
    output_path: str = RuntimeField(
        description="Relative path for the yields table JSON (e.g. "
                    "'yields/m0p25.json')")
    # ---------------------------------------------------------------------- #

    # ---------------------------- State fields ---------------------------- #
    base_directory: str = StateField(default=".", description="Base directory for safe paths")
    # ---------------------------------------------------------------------- #

    def _setup(self):
        """Setup base directory and validate it exists."""
        self.base_directory = os.path.abspath(self.base_directory)
        if not os.path.exists(self.base_directory):
            raise ValueError(f"Base directory does not exist: {self.base_directory}")

    def _safe_path(self, rel: str) -> Optional[str]:
        """Ensures that the path is within the allowed base directory."""
        if not rel:
            return None
        full = os.path.abspath(os.path.join(self.base_directory, rel))
        return full if full.startswith(self.base_directory) else None

    def _run(self) -> str:
        """Compute N_sig(g) over g_grid and write yields + audit files."""
        import numpy as np

        from . import llp_physics as phys

        src = self._safe_path(self.events_path)
        geo = self._safe_path(self.geometry_path)
        dst = self._safe_path(self.output_path)
        if not src or not geo or not dst:
            return self.format_error(
                error="Access Denied",
                reason="events_path, geometry_path or output_path escapes "
                       "base_directory",
                suggestion="Use relative paths inside base_directory")
        for path, label in ((src, "events_path"), (geo, "geometry_path")):
            if not os.path.exists(path):
                return self.format_error(
                    error="File Not Found",
                    reason=f"{label} not found",
                    context=f"path={getattr(self, label)}",
                    suggestion=f"Provide a valid {label}")

        # --------------------- validate parameters --------------------- #
        m_phi = float(self.m_phi_gev)
        m_mu = float(self.m_mu_gev)
        wref = float(self.width_ref_gev)
        n_int = float(self.n_int)
        g_grid = [float(g) for g in (self.g_grid or [])]
        if m_phi <= 0.0 or m_mu <= 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"masses must be positive (m_phi={m_phi}, m_mu={m_mu})",
                suggestion="Provide m_phi_gev > 0 and m_mu_gev > 0")
        if wref <= 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"width_ref_gev must be positive (got {wref})",
                suggestion="width_ref_gev is Gamma_tot at g = 1; for "
                           "phi -> mu mu it vanishes at m_phi <= 2 m_mu, "
                           "where no decay-in-volume signal exists")
        if not g_grid or any(g <= 0.0 for g in g_grid):
            return self.format_error(
                error="Invalid Parameter",
                reason="g_grid must be a non-empty list of positive couplings",
                suggestion="Provide g_grid like [1e-6, 3e-6, 1e-5]")
        if n_int <= 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"n_int must be positive (got {n_int})",
                suggestion="n_int is the number of primary interactions")
        if bool(self.require_two_track) and m_phi <= 2.0 * m_mu:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"two-track acceptance requires m_phi > 2 m_mu "
                       f"(m_phi={m_phi}, 2 m_mu={2.0 * m_mu})",
                suggestion="phi -> mu mu is kinematically closed; check "
                           "m_phi_gev / m_mu_gev or set require_two_track "
                           "to false")

        # -------------------------- load inputs ------------------------ #
        try:
            geom = phys.DecayVolume.from_yaml(geo)
        except Exception as e:
            return self.format_error(
                error="Geometry Error",
                reason=str(e),
                context=f"path={self.geometry_path}",
                suggestion="Geometry YAML must declare z_min_m, z_max_m, "
                           "r_volume_m, z_det_m, r_det_m")
        try:
            p4_list, w_list, channels = [], [], []
            with open(src) as fh:
                for ln, line in enumerate(fh):
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    p4_list.append([rec["E"], rec["px"], rec["py"],
                                    rec["pz"]])
                    w_list.append(rec["event_weight_g2_stripped"])
                    channels.append(rec.get("parent_channel"))
        except KeyError as e:
            return self.format_error(
                error="Event Format Error",
                reason=f"event record at line {ln + 1} is missing field {e}",
                context=f"path={self.events_path}",
                suggestion="Records need E, px, py, pz and "
                           "event_weight_g2_stripped (the "
                           "LLPFluxFromMesonDecayTool output format)")
        except Exception as e:
            return self.format_error(
                error="Read Error",
                reason=str(e),
                context=f"path={self.events_path}",
                suggestion="Verify the events file is line-delimited JSON")

        base, _ = os.path.splitext(dst)
        audit_path = base + ".audit.jsonl"
        os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
        g_ref = g_grid[0]
        n_events = len(p4_list)

        # ---------------- empty input: zero yields, not an error ------- #
        if n_events == 0:
            yields = [{"g": g, "n_sig": 0.0} for g in g_grid]
            with open(audit_path, "w") as fh:
                pass
            return self._write_outputs(dst, audit_path, yields, 0, 0, 0,
                                       m_phi, m_mu, wref, n_int, g_ref)

        # --------------------------- compute --------------------------- #
        try:
            p4 = np.asarray(p4_list, dtype=float)
            w = np.asarray(w_list, dtype=float)
            pmag = np.linalg.norm(p4[:, 1:], axis=1)
            theta = np.arccos(np.clip(
                p4[:, 3] / np.maximum(pmag, 1e-300), -1.0, 1.0))
            beta_gamma = pmag / m_phi
            L1, L2, ok = geom.segment(theta)
            # midpoint vertices for the two-track convention
            Lmid = 0.5 * (L1 + L2)
            dirs = p4[:, 1:] / np.maximum(pmag, 1e-300)[:, None]
            vertex = Lmid[:, None] * dirs
            if bool(self.require_two_track):
                rng = np.random.default_rng(int(self.seed))
                tt = phys.two_track_pass(p4, vertex, m_phi, m_mu, geom, rng)
            else:
                tt = None
            keep = ok & tt if tt is not None else ok
            # exact coupling-grid reweighting
            yields = []
            for g in g_grid:
                ctau = phys.HBARC_M_GEV / (g * g * wref)
                lam = beta_gamma[keep] * ctau
                pdec = phys.decay_probability(L1[keep], L2[keep], lam)
                n_sig = n_int * g * g * float(np.sum(w[keep] * pdec))
                yields.append({"g": g, "n_sig": n_sig})
            # per-event audit columns at g_ref
            ctau_ref = phys.HBARC_M_GEV / (g_ref * g_ref * wref)
            pdec_ref = phys.decay_probability(
                L1, L2, beta_gamma * ctau_ref)
            contrib_ref = n_int * g_ref * g_ref * w * pdec_ref \
                * keep.astype(float)
            with open(audit_path, "w") as fh:
                for i in range(n_events):
                    rec = {
                        "schema": AUDIT_SCHEMA_VERSION,
                        "event_id": i,
                        "parent_channel": channels[i],
                        "event_weight_g2_stripped": float(w[i]),
                        "beta_gamma": float(beta_gamma[i]),
                        "L1_m": float(L1[i]),
                        "L2_m": float(L2[i]),
                        "geom_pass": bool(ok[i]),
                        "two_track_pass": (bool(tt[i]) if tt is not None
                                           else None),
                        "p_decay_at_g_ref": float(pdec_ref[i]),
                        "weighted_contribution_at_g_ref":
                            float(contrib_ref[i]),
                    }
                    fh.write(json.dumps(rec, separators=(",", ":")) + "\n")
            n_geo = int(np.sum(ok))
            n_tt = int(np.sum(keep))
        except Exception as e:
            return self.format_error(
                error="Processing Error",
                reason=str(e),
                context=f"events={self.events_path}, "
                        f"geometry={self.geometry_path}",
                suggestion="Check event four-momenta and geometry values")

        return self._write_outputs(dst, audit_path, yields, n_events,
                                   n_geo, n_tt, m_phi, m_mu, wref, n_int,
                                   g_ref)

    def _write_outputs(self, dst, audit_path, yields, n_events, n_geo,
                       n_tt, m_phi, m_mu, wref, n_int, g_ref) -> str:
        """Write the yields table and format the tool result JSON."""
        table = {
            "schema": YIELDS_SCHEMA_VERSION,
            "conventions": dict(CONVENTIONS),
            "m_phi_gev": m_phi,
            "m_mu_gev": m_mu,
            "width_ref_gev": wref,
            "n_int": n_int,
            "g_ref": g_ref,
            "n_events": n_events,
            "n_pass_geometry": n_geo,
            "n_pass_two_track": n_tt,
            "yields": yields,
        }
        with open(dst, "w") as fh:
            json.dump(table, fh, indent=2)
        result = {
            "status": "ok",
            "n_events": n_events,
            "n_pass_geometry": n_geo,
            "n_pass_two_track": n_tt,
            "yields": yields,
            "output_path": os.path.relpath(dst, self.base_directory),
            "audit_path": os.path.relpath(audit_path, self.base_directory),
            "conventions": {"two_track": CONVENTIONS["two_track"],
                            "weight": CONVENTIONS["weight"]},
        }
        return json.dumps(result, separators=(",", ":"), ensure_ascii=False)
