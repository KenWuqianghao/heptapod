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
    Compute decay-in-volume LLP signal yields over a lifetime grid, from
    g^2-stripped weighted events (LLPFluxFromMesonDecayTool output).

    **Purpose:**
    Turn an LLP flux sample (the `output_path` events of
    LLPFluxFromMesonDecayTool; multiple channels may be concatenated into
    one file) into the expected number of signal decays — the
    convention-sensitive step of a reach study. Two mutually exclusive
    lifetime modes are supported:

    * **portal scaling** (`width_ref_gev` + `g_grid`): the model-card
      convention where production scales as g^2, the total width as g^2,
      and kinematics are g-independent, so one event set covers the whole
      g axis exactly by reweighting:
          N_sig(g) = N_int * g^2 * sum_i w_i * P_dec,i(g) * twotrack_i,
      with ctau(g) = hbar*c / (g^2 * width_ref_gev). Yields are reported
      per g.
    * **direct lifetimes** (`ctau_grid_m`): a list of lab-frame ctau
      values in meters, fully model-agnostic (no portal assumed). The
      caller owns any coupling factors. Yields are reported per ctau as
          N(ctau) = N_int * sum_i w_i * P_dec,i(ctau) * twotrack_i
      with NO g^2 factor — the g^2-stripped weights are used verbatim.

    Provide exactly one mode. `width_ref_gev`+`g_grid` XOR `ctau_grid_m`.

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
    - m_phi_gev: LLP mass in GeV.
    - daughter_masses_gev: the two visible-decay daughter masses in GeV
      (length-2 list; default [0.1056584, 0.1056584] = mu mu). Used only
      by the two-track acceptance; masses need not be equal.
    - width_ref_gev: Gamma_tot(phi) at g = 1 in GeV (g^2-stripped
      reference width) — portal-scaling mode.
    - g_grid: list of couplings g at which to evaluate N_sig — portal
      mode.
    - ctau_grid_m: list of lab-frame ctau values in meters — direct
      lifetime mode (mutually exclusive with width_ref_gev/g_grid).
    - n_int: number of primary interactions (sigma_inel * L_int for a
      collider setting, N_POT for a beam dump).
    - require_two_track: apply the two-track acceptance (default true).
      If false the acceptance factor is 1 and the audit column is null.
    - seed: RNG seed for the isotropic two-body decay sampling.
    - output_path: where to write the yields table (JSON).

    **Behavior (declared conventions, mirrored from the validated
    reference pipeline):**
    - The phi travels in a straight line from the primary vertex at its
      lab angle; the parent flight length is absorbed into the kernel
      (decaying-parents-only normalization).
    - In-volume segment [L1, L2] = intersection of the ray with the
      on-axis cylinder; P_dec = exp(-L1/lam) - exp(-L2/lam) with
      lam = beta*gamma*ctau and beta*gamma = |p|/m_phi.
    - Two-track acceptance at the decay-volume MIDPOINT convention
      (lifetime-independent, preserving exact reweighting): one isotropic
      phi -> d1 d2 decay is sampled per event at the midpoint of
      [L1, L2], both daughters are boosted to the lab and propagated to
      the z_det plane, and both must satisfy r < r_det moving forward.
    - Weights are g^2-stripped per primary interaction; in portal mode
      the g^2 from production is applied here and the g^2 in the lifetime
      enters through P_dec, while in ctau mode no g^2 is applied.

    **Output (JSON string):**
    - status: "ok" on success.
    - lifetime_mode: "portal" or "ctau".
    - n_events: number of event records read.
    - n_pass_geometry: events whose ray intersects the decay volume.
    - n_pass_two_track: events passing geometry AND two-track acceptance
      (these are the contributing events).
    - yields: portal mode -> [{g, n_sig}] over g_grid; ctau mode ->
      [{ctau_m, n_sig}] over ctau_grid_m (expected signal decays).
    - output_path: yields table JSON (per-point rows + conventions block).
    - audit_path: per-event audit file (line-delimited JSON) with
      event_id, parent_channel, event_weight_g2_stripped, beta_gamma,
      L1_m, L2_m, geom_pass, two_track_pass, plus p_decay and the
      weighted contribution evaluated at the first grid point.
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
    daughter_masses_gev: List[float] = RuntimeField(
        default=[0.1056584, 0.1056584],
        description="The two visible-decay daughter masses in GeV "
                    "(length 2; default [0.1056584, 0.1056584] = mu mu). "
                    "Used by the two-track acceptance")
    width_ref_gev: float = RuntimeField(
        default=0.0,
        description="Portal mode: Gamma_tot(phi) at g = 1 in GeV "
                    "(g^2-stripped reference width for ctau(g) = "
                    "hbar*c/(g^2*width_ref_gev)). Pair with g_grid. "
                    "Leave unset (0) for direct-lifetime mode")
    g_grid: List[float] = RuntimeField(
        default=[],
        description="Portal mode: couplings g at which to evaluate N_sig "
                    "(exact reweighting: one event set covers the list). "
                    "Pair with width_ref_gev. Leave empty for "
                    "direct-lifetime mode")
    ctau_grid_m: List[float] = RuntimeField(
        default=[],
        description="Direct-lifetime mode: lab-frame ctau values in "
                    "meters (model-agnostic; no g^2 applied). Mutually "
                    "exclusive with width_ref_gev/g_grid")
    n_int: float = RuntimeField(
        description="Number of primary interactions (sigma_inel * L_int "
                    "for a collider, N_POT for a beam dump)")
    require_two_track: bool = RuntimeField(
        default=True,
        description="Apply the midpoint two-track acceptance (default "
                    "true)")
    seed: int = RuntimeField(
        default=1,
        description="RNG seed for the isotropic phi -> d1 d2 decay "
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
        dmasses = [float(m) for m in (self.daughter_masses_gev or [])]
        n_int = float(self.n_int)
        if m_phi <= 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"m_phi must be positive (m_phi={m_phi})",
                suggestion="Provide m_phi_gev > 0")
        if len(dmasses) != 2 or any(m < 0.0 for m in dmasses):
            return self.format_error(
                error="Invalid Parameter",
                reason=f"daughter_masses_gev must be two non-negative "
                       f"masses (got {self.daughter_masses_gev})",
                suggestion="Provide e.g. [0.1056584, 0.1056584] for mu mu")
        m1, m2 = dmasses
        if n_int <= 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"n_int must be positive (got {n_int})",
                suggestion="n_int is the number of primary interactions")

        # ------------- lifetime mode: portal XOR direct ctau ----------- #
        # Sentinels: width_ref_gev defaults to 0 and the grids to [] so
        # each mode is detected by "was anything meaningful supplied".
        wref_given = float(self.width_ref_gev or 0.0) > 0.0
        g_given = bool(self.g_grid)
        ctau_given = bool(self.ctau_grid_m)
        has_portal = wref_given or g_given
        has_ctau = ctau_given
        if has_portal and has_ctau:
            return self.format_error(
                error="Invalid Parameter",
                reason="lifetime mode is ambiguous: both portal "
                       "(width_ref_gev/g_grid) and ctau_grid_m were given",
                suggestion="Provide EITHER width_ref_gev + g_grid OR "
                           "ctau_grid_m, not both")
        if not has_portal and not has_ctau:
            return self.format_error(
                error="Invalid Parameter",
                reason="no lifetime mode selected",
                suggestion="Provide width_ref_gev + g_grid (portal) or "
                           "ctau_grid_m (direct lifetimes)")

        if has_portal:
            lifetime_mode = "portal"
            wref = float(self.width_ref_gev or 0.0)
            g_grid = [float(g) for g in (self.g_grid or [])]
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
                    reason="g_grid must be a non-empty list of positive "
                           "couplings",
                    suggestion="Provide g_grid like [1e-6, 3e-6, 1e-5]")
            # (label_key, label_value, ctau_m, prefactor)
            points = [("g", g, phys.HBARC_M_GEV / (g * g * wref), g * g)
                      for g in g_grid]
        else:
            lifetime_mode = "ctau"
            wref = None
            ctau_grid = [float(c) for c in (self.ctau_grid_m or [])]
            if not ctau_grid or any(c <= 0.0 for c in ctau_grid):
                return self.format_error(
                    error="Invalid Parameter",
                    reason="ctau_grid_m must be a non-empty list of "
                           "positive lab-frame ctau values in meters",
                    suggestion="Provide ctau_grid_m like [0.1, 1.0, 10.0]")
            points = [("ctau_m", c, c, 1.0) for c in ctau_grid]

        if bool(self.require_two_track) and m_phi <= m1 + m2:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"two-track acceptance requires m_phi > m1 + m2 "
                       f"(m_phi={m_phi}, m1+m2={m1 + m2})",
                suggestion="phi -> d1 d2 is kinematically closed; check "
                           "m_phi_gev / daughter_masses_gev or set "
                           "require_two_track to false")

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
        label_key = points[0][0]
        ctau_ref = points[0][2]
        pref_ref = points[0][3]
        n_events = len(p4_list)

        # ---------------- empty input: zero yields, not an error ------- #
        if n_events == 0:
            yields = [{label_key: val, "n_sig": 0.0}
                      for (_, val, _, _) in points]
            with open(audit_path, "w") as fh:
                pass
            return self._write_outputs(dst, audit_path, yields, 0, 0, 0,
                                       m_phi, dmasses, wref, n_int,
                                       lifetime_mode)

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
                tt = phys.two_track_pass(p4, vertex, m_phi, m1, m2, geom, rng)
            else:
                tt = None
            keep = ok & tt if tt is not None else ok
            # exact lifetime-grid reweighting (one event set covers all
            # points; the prefactor is g^2 in portal mode, 1.0 in ctau)
            yields = []
            for lkey, lval, ctau, pref in points:
                lam = beta_gamma[keep] * ctau
                pdec = phys.decay_probability(L1[keep], L2[keep], lam)
                n_sig = n_int * pref * float(np.sum(w[keep] * pdec))
                yields.append({lkey: lval, "n_sig": n_sig})
            # per-event audit columns at the first grid point
            pdec_ref = phys.decay_probability(
                L1, L2, beta_gamma * ctau_ref)
            contrib_ref = n_int * pref_ref * w * pdec_ref \
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
                        "p_decay_at_ref": float(pdec_ref[i]),
                        "weighted_contribution": float(contrib_ref[i]),
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
                                   n_geo, n_tt, m_phi, dmasses, wref, n_int,
                                   lifetime_mode)

    def _write_outputs(self, dst, audit_path, yields, n_events, n_geo,
                       n_tt, m_phi, dmasses, wref, n_int,
                       lifetime_mode) -> str:
        """Write the yields table and format the tool result JSON."""
        table = {
            "schema": YIELDS_SCHEMA_VERSION,
            "conventions": dict(CONVENTIONS),
            "lifetime_mode": lifetime_mode,
            "m_phi_gev": m_phi,
            "daughter_masses_gev": list(dmasses),
            "width_ref_gev": wref,
            "n_int": n_int,
            "n_events": n_events,
            "n_pass_geometry": n_geo,
            "n_pass_two_track": n_tt,
            "yields": yields,
        }
        with open(dst, "w") as fh:
            json.dump(table, fh, indent=2)
        result = {
            "status": "ok",
            "lifetime_mode": lifetime_mode,
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
