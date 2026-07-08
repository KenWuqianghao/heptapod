"""
# flux_from_meson_decay.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json
import os
from typing import Optional

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField

SCHEMA_VERSION = "llpflux-1.0"
MANIFEST_SCHEMA_VERSION = "llpflux-manifest-1.0"
WEIGHT_CONVENTION = "g2_stripped_per_primary_interaction"

# numpy / yaml-backed physics is deferred to _run() so module import does
# not pull in numpy's cold load (heptapod toolkit startup convention).


class LLPFluxFromMesonDecayTool(BaseTool):
    """
    Sample weighted LLP lab-frame events from an analytic parent-flux
    kernel convolved with the declared 3-body production spectrum
    M -> mu nu phi (a scalar phi radiated off the muon leg).

    **Purpose:**
    Produce the phi flux entering a decay-in-volume reach study: per-event
    lab four-momenta with g^2-stripped weights, normalized per primary
    interaction, ready for DecayInVolumeTool. One call handles one parent
    channel (one kernel); run once per channel and concatenate the output
    files for a multi-channel study.

    **Inputs (runtime):**
    - kernel_spec: path to the kernel YAML (form `pexp_texp`), which carries
      the parent name, parent_mass_gev, and the momentum/angle parameters.
      The kernel parametrizes d^2 N / (dp dtheta) of *decaying* parents per
      primary interaction (decay-before-absorption folded into n_per_int),
      so the collider vs beam-dump setting lives entirely in this file.
    - m_phi_gev: LLP mass in GeV.
    - m_mu_gev: muon mass in GeV (default 0.1056584).
    - kappa: the declared branching coefficient at g = 1 for this channel,
      i.e. Br(M -> mu nu phi) = g^2 * kappa (from the model card).
    - n_samples: number of Monte Carlo events to draw.
    - seed: RNG seed (deterministic output for fixed inputs).
    - output_path: where to write the event records (line-delimited JSON).

    **Behavior:**
    Samples the parent (p, theta, azimuth) exactly from the kernel shape;
    draws x = 2 E_phi / m_M from the 1D marginal of the tree-level
    production density (trace-form matrix element, mirrored from the
    validated reference); takes the phi direction isotropic in the parent
    rest frame (exact for a spin-0 parent); and boosts to the lab with
    k_lab = k* + P [ (P.k*)/(M(E+M)) + E*/M ]. Each record carries the
    g^2-stripped per-event weight

        event_weight_g2_stripped = n_per_int * kappa / n_samples,

    so the physical yield is recovered downstream as
    N_sig(g) = N_int * g^2 * sum_i w_i * P_dec,i(g) * acc_i. A manifest
    JSON declaring this convention is written next to the events file.
    If m_phi >= m_parent - m_mu the channel is kinematically closed: the
    tool returns status ok with n_samples = 0 and the cutoff flagged
    (empty events file + manifest are still written), not an error.

    **Output (JSON string):**
    - status: "ok" on success.
    - n_samples: number of event records written (0 above the cutoff).
    - output_path: events file, one JSON record per line with fields
      E, px, py, pz (GeV), theta_lab (rad), parent_channel,
      event_weight_g2_stripped.
    - manifest_path: manifest JSON declaring the weight convention and
      all inputs (kernel, masses, kappa, seed, sum_weights).
    - weight_convention: "g2_stripped_per_primary_interaction".
    - sum_weights: sum of event weights = n_per_int * kappa (0 above
      the cutoff) — the g^2-stripped phi yield per primary interaction.
    - parent: parent name from the kernel spec.
    - kinematic_cutoff_gev: m_parent - m_mu, the maximum open m_phi.
    - above_kinematic_cutoff: true when the channel is closed.
    """
    # --------------------------- Runtime fields --------------------------- #
    kernel_spec: str = RuntimeField(
        description="Path to the parent-flux kernel YAML (form 'pexp_texp'; "
                    "carries parent name, parent_mass_gev, n_per_int, "
                    "p0_gev, a, theta0_rad)")
    m_phi_gev: float = RuntimeField(
        description="LLP (phi) mass in GeV")
    m_mu_gev: float = RuntimeField(
        default=0.1056584,
        description="Muon mass in GeV (default 0.1056584)")
    kappa: float = RuntimeField(
        description="Declared branching coefficient at g = 1 for this "
                    "channel: Br(M -> mu nu phi) = g^2 * kappa")
    n_samples: int = RuntimeField(
        description="Number of Monte Carlo events to sample")
    seed: int = RuntimeField(
        description="RNG seed for deterministic sampling")
    output_path: str = RuntimeField(
        description="Relative path for the line-delimited JSON event "
                    "records (e.g. 'flux/phi_K.jsonl')")
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
        """Sample the phi flux and write events + manifest."""
        import numpy as np

        from . import llp_physics as phys

        src = self._safe_path(self.kernel_spec)
        dst = self._safe_path(self.output_path)
        if not src or not dst:
            return self.format_error(
                error="Access Denied",
                reason="kernel_spec or output_path escapes base_directory",
                suggestion="Use relative paths inside base_directory")
        if not os.path.exists(src):
            return self.format_error(
                error="File Not Found",
                reason="kernel YAML not found",
                context=f"path={self.kernel_spec}",
                suggestion="Provide a valid kernel spec path")

        # ------------------------- load kernel ------------------------- #
        try:
            kernel = phys.AnalyticKernel.from_yaml(src)
        except Exception as e:
            return self.format_error(
                error="Kernel Error",
                reason=str(e),
                context=f"path={self.kernel_spec}",
                suggestion="Kernel YAML must declare name, parent, "
                           "parent_mass_gev, form: pexp_texp, and params "
                           "{n_per_int, p0_gev, a, theta0_rad}")

        # --------------------- validate parameters --------------------- #
        m_phi = float(self.m_phi_gev)
        m_mu = float(self.m_mu_gev)
        n = int(self.n_samples)
        if m_phi <= 0.0 or m_mu <= 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"masses must be positive (m_phi={m_phi}, m_mu={m_mu})",
                suggestion="Provide m_phi_gev > 0 and m_mu_gev > 0")
        if float(self.kappa) < 0.0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"kappa must be non-negative (kappa={self.kappa})",
                suggestion="kappa is Br(M -> mu nu phi) at g = 1")
        if n <= 0:
            return self.format_error(
                error="Invalid Parameter",
                reason=f"n_samples must be positive (n_samples={n})",
                suggestion="Provide n_samples >= 1")

        mM = kernel.parent_mass
        cutoff = mM - m_mu
        above_cutoff = m_phi >= cutoff

        base, _ = os.path.splitext(dst)
        manifest_path = base + ".manifest.json"
        os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)

        # ------------------------- sample events ----------------------- #
        try:
            if above_cutoff:
                n_written = 0
                sum_weights = 0.0
                with open(dst, "w") as fh:
                    pass  # empty events file: channel kinematically closed
            else:
                rng = np.random.default_rng(int(self.seed))
                # parent kinematics from the kernel (exact draws)
                p_par, th_par, az_par = kernel.sample(n, rng)
                e_par = np.sqrt(p_par ** 2 + mM ** 2)
                # phi in the parent rest frame: energy from the x marginal
                # of the production density, direction isotropic
                x = phys.sample_x(mM, m_mu, m_phi, n, rng)
                estar = 0.5 * x * mM
                pstar = np.sqrt(np.maximum(estar ** 2 - m_phi ** 2, 0.0))
                cth = rng.uniform(-1.0, 1.0, n)
                sth = np.sqrt(1.0 - cth ** 2)
                azs = rng.uniform(0.0, 2.0 * np.pi, n)
                kstar = pstar[:, None] * np.stack(
                    [sth * np.cos(azs), sth * np.sin(azs), cth], axis=1)
                # parent lab momentum vector
                dir_par = np.stack([np.sin(th_par) * np.cos(az_par),
                                    np.sin(th_par) * np.sin(az_par),
                                    np.cos(th_par)], axis=1)
                pvec_par = p_par[:, None] * dir_par
                # boost phi to the lab (validated boost formula)
                elab, klab = phys.boost_to_lab(estar, kstar, e_par,
                                               pvec_par, mM)
                theta_lab = np.arccos(np.clip(
                    klab[:, 2] / np.maximum(
                        np.linalg.norm(klab, axis=1), 1e-300),
                    -1.0, 1.0))
                w = kernel.n_per_int * float(self.kappa) / n
                with open(dst, "w") as fh:
                    for i in range(n):
                        rec = {
                            "schema": SCHEMA_VERSION,
                            "event_id": i,
                            "E": float(elab[i]),
                            "px": float(klab[i, 0]),
                            "py": float(klab[i, 1]),
                            "pz": float(klab[i, 2]),
                            "theta_lab": float(theta_lab[i]),
                            "parent_channel": kernel.parent,
                            "event_weight_g2_stripped": float(w),
                        }
                        fh.write(json.dumps(rec, separators=(",", ":")) + "\n")
                n_written = n
                sum_weights = float(kernel.n_per_int * float(self.kappa))
        except Exception as e:
            return self.format_error(
                error="Sampling Error",
                reason=str(e),
                context=f"kernel={kernel.name}, m_phi={m_phi}",
                suggestion="Check kernel parameters and mass inputs")

        # -------------------------- manifest --------------------------- #
        manifest = {
            "schema": MANIFEST_SCHEMA_VERSION,
            "weight_convention": WEIGHT_CONVENTION,
            "weight_definition": "event_weight_g2_stripped = n_per_int * "
                                 "kappa / n_samples; N_sig(g) = N_int * g^2 "
                                 "* sum_i w_i * P_dec,i(g) * acc_i",
            "events_path": os.path.relpath(dst, self.base_directory),
            "kernel_spec": os.path.relpath(src, self.base_directory),
            "kernel_name": kernel.name,
            "parent": kernel.parent,
            "parent_mass_gev": mM,
            "m_phi_gev": m_phi,
            "m_mu_gev": m_mu,
            "kappa": float(self.kappa),
            "n_samples": n_written,
            "seed": int(self.seed),
            "sum_weights": sum_weights,
            "kinematic_cutoff_gev": cutoff,
            "above_kinematic_cutoff": above_cutoff,
        }
        with open(manifest_path, "w") as fh:
            json.dump(manifest, fh, indent=2)

        result = {
            "status": "ok",
            "n_samples": n_written,
            "output_path": os.path.relpath(dst, self.base_directory),
            "manifest_path": os.path.relpath(manifest_path,
                                             self.base_directory),
            "weight_convention": WEIGHT_CONVENTION,
            "sum_weights": sum_weights,
            "parent": kernel.parent,
            "kinematic_cutoff_gev": cutoff,
            "above_kinematic_cutoff": above_cutoff,
        }
        return json.dumps(result, separators=(",", ":"), ensure_ascii=False)
