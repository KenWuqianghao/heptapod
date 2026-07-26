"""
# slha_decay.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json, os
from typing import Optional, List

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField


# Minimal property defaults for product particles the LHE/UFO model often
# leaves out of the shower (most commonly the gravitino in GMSB). Keyed by
# absolute PDG id. spinType is Pythia's 2S+1 convention. These are only used
# when the agent does NOT pass an explicit definition in extra_particle_defs.
# Task-agnostic: any massless, colorless, neutral, stable singlet.
_DEFAULT_PARTICLE_DEFS = {
    # Gravitino: spin-3/2 (spinType 4), charge 0, colorless, ~massless, stable.
    1000039: {
        "name": "gravitino",
        "antiname": "gravitino",
        "spinType": 4,
        "chargeType": 0,
        "colType": 0,
        "m0": 0.0,
    },
}


class BuildDecayTableTool(BaseTool):
    """
    Build a Pythia-readable decay-table fragment for a BSM state that the LHE
    left stable (a generic "decay an NLSP/parent the parton level kept stable"
    helper).

    The classic case is the GMSB neutralino NLSP decaying to photon + gravitino
    (chi0 -> gamma G~), where the gravitino is absent from the MG5 model and the
    neutralino is therefore left undecayed in the LHE. This tool emits a fragment
    that (i) defines any missing product particle (e.g. the gravitino: spin,
    charge 0, colorless, mass ~0, stable), (ii) sets the parent mass, and
    (iii) turns the parent's decay on with a single BR=1 prompt channel into the
    requested products.

    Inputs (runtime):
      - parent_pdg: PDG id of the decaying parent (NLSP), e.g. 1000022.
      - parent_mass_gev: mass of the parent in GeV (used in <parent>:m0).
      - products: list of product PDG ids, e.g. [22, 1000039] for gamma + G~.
      - extra_particle_defs: (optional) list of dicts, each fully describing a
        product particle to define, e.g.
          {"pdg": 1000039, "name": "gravitino", "spinType": 4,
           "chargeType": 0, "colType": 0, "m0": 0.0}
        If a product is missing from this list AND has a built-in default
        (currently the gravitino, 1000039), the default is emitted.
      - out_path: sandbox-relative file to write the .cmnd fragment to.

    Output (JSON): status, out_path (relative), and the fragment text.

    The fragment is task-agnostic Pythia ParticleData syntax and can be appended
    to the shower run card (or read via Pythia's `read` mechanism).
    """
    # --------------------------- Runtime fields --------------------------- #
    parent_pdg: int = RuntimeField(description="PDG id of the decaying parent (NLSP), e.g. 1000022")
    parent_mass_gev: float = RuntimeField(description="Parent mass in GeV")
    products: List[int] = RuntimeField(description="List of product PDG ids, e.g. [22, 1000039] for gamma + gravitino")
    extra_particle_defs: Optional[List[dict]] = RuntimeField(
        default=None,
        description="Optional list of dicts defining product particles (keys: pdg, name, spinType, chargeType, colType, m0, [antiname]). Missing products with a built-in default (e.g. gravitino 1000039) are defined automatically."
    )
    out_path: str = RuntimeField(description="Sandbox-relative path to write the Pythia .cmnd decay-table fragment")
    # ---------------------------------------------------------------------- #

    # ---------------------------- State fields ---------------------------- #
    base_directory: str = StateField(default=".", description="Base directory for safe paths")
    # ---------------------------------------------------------------------- #

    def _setup(self):
        self.base_directory = os.path.abspath(self.base_directory)
        if not os.path.exists(self.base_directory):
            raise ValueError(f"Base directory does not exist: {self.base_directory}")

    def _safe_path(self, rel: str) -> Optional[str]:
        if not rel:
            return None
        full = os.path.abspath(os.path.join(self.base_directory, rel))
        return full if full.startswith(self.base_directory) else None

    @staticmethod
    def build_fragment(parent_pdg: int, parent_mass_gev: float,
                       products: List[int],
                       extra_particle_defs: Optional[List[dict]] = None) -> str:
        """Construct the Pythia decay-table fragment text. Pure function so it
        can be unit-tested without instantiating the tool."""
        # Index any user-supplied definitions by PDG id.
        user_defs = {}
        for d in (extra_particle_defs or []):
            if "pdg" not in d:
                raise ValueError("each extra_particle_defs entry needs a 'pdg' key")
            user_defs[int(d["pdg"])] = d

        lines = [
            "! Auto-generated decay-table fragment (BuildDecayTableTool).",
            f"! Decay parent {parent_pdg} -> {' '.join(str(p) for p in products)} (BR=1, prompt).",
        ]

        # (i) Define any product particle that is missing from the model.
        # We emit a definition for every product that either the user supplied
        # explicitly or that has a built-in default; SM products (e.g. the
        # photon, 22) are already known to Pythia and are skipped.
        for pid in products:
            apid = abs(int(pid))
            spec = None
            if apid in user_defs:
                spec = dict(user_defs[apid])
            elif apid in _DEFAULT_PARTICLE_DEFS:
                spec = dict(_DEFAULT_PARTICLE_DEFS[apid])
            if spec is None:
                continue  # known SM particle or product the agent left to Pythia
            name = spec.get("name", f"bsm{apid}")
            antiname = spec.get("antiname", name)
            spin = int(spec.get("spinType", 1))
            charge = int(spec.get("chargeType", 0))
            col = int(spec.get("colType", 0))
            m0 = float(spec.get("m0", 0.0))
            # ParticleData syntax: id:all = name antiname spinType chargeType colType m0 mWidth mMin mMax tau0
            lines.append(
                f"{apid}:all = {name} {antiname} {spin} {charge} {col} {m0} 0.0 0.0 0.0 0.0"
            )
            # Make the defined product stable (e.g. the gravitino escapes as MET).
            lines.append(f"{apid}:mayDecay = off")

        # (ii) Set the parent mass.
        lines.append(f"{int(parent_pdg)}:m0 = {float(parent_mass_gev)}")

        # (iii) Turn the parent decay on with a single BR=1 prompt channel.
        lines.append(f"{int(parent_pdg)}:mayDecay = on")
        prod_str = " ".join(str(int(p)) for p in products)
        # oneChannel: BR meMode product1 product2 ...; meMode 0 = phase space.
        lines.append(f"{int(parent_pdg)}:oneChannel = 1 1.0 0 {prod_str}")

        return "\n".join(lines) + "\n"

    def _run(self) -> str:
        # Validate inputs.
        if not isinstance(self.products, (list, tuple)) or len(self.products) < 1:
            return self.format_error(
                error="Invalid Input",
                reason="products must be a non-empty list of PDG ids",
                suggestion="e.g. products=[22, 1000039] for chi0 -> gamma gravitino"
            )
        try:
            int(self.parent_pdg)
        except (TypeError, ValueError):
            return self.format_error(error="Invalid Input", reason="parent_pdg must be an integer PDG id")
        if self.parent_mass_gev is None or float(self.parent_mass_gev) < 0:
            return self.format_error(
                error="Invalid Input",
                reason="parent_mass_gev must be a non-negative number"
            )

        dst = self._safe_path(self.out_path)
        if not dst:
            return self.format_error(error="Access Denied", reason="out_path escapes base_directory")

        try:
            fragment = self.build_fragment(
                int(self.parent_pdg), float(self.parent_mass_gev),
                [int(p) for p in self.products], self.extra_particle_defs
            )
        except Exception as e:
            return self.format_error(error="Build Error", reason=str(e))

        try:
            dst_dir = os.path.dirname(dst)
            if dst_dir:
                os.makedirs(dst_dir, exist_ok=True)
            with open(dst, "w") as f:
                f.write(fragment)
        except Exception as e:
            return self.format_error(error="Write Error", reason=str(e))

        result = {
            "status": "ok",
            "out_path": os.path.relpath(dst, self.base_directory),
            "parent_pdg": int(self.parent_pdg),
            "products": [int(p) for p in self.products],
            "fragment": fragment,
        }
        return json.dumps(result, separators=(",", ":"), ensure_ascii=False)
