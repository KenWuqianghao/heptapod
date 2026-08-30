"""
# feyncalc_codegen.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

FeynCalc code generator — converts Diagram dataclasses into runnable
Mathematica/FeynCalc scripts for exact tree-level calculations.

Supports:
  - 1 -> 2 decays (tree-level, with or without one propagator)
  - 2 -> 2 scattering (tree-level, s/t/u-channel + contact)

The generated scripts follow the standard workflow:
  amplitude -> square -> spin/pol sums -> traces -> kinematics -> observable
and emit SYMBOLIC_RESULT / NUMERICAL_RESULT markers compatible with
wolfram_runner.py parsing.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

from tools.nda.simple_diagram import Diagram, Particle, Vertex, Propagator
from .scattering import (  # noqa: F401
    Channel,
    UnsupportedScattering,
    build_amplitude as _build_scattering_amplitude,
    kinematics_block as _scattering_kinematics,
    cross_section_block as _scattering_cross_section,
)


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

class ProcessType(Enum):
    """Classification of the scattering / decay process."""
    DECAY_1TO2 = auto()            # 1 initial, 2 final, 0 propagators
    DECAY_1TO2_1PROP = auto()      # 1 initial, 2 final, 1 propagator
    SCATTERING_2TO2 = auto()       # 2 initial, 2 final
    UNSUPPORTED = auto()


# Channel now lives in `scattering`, alongside the 2->2 builder that uses it.
# Re-exported here so existing importers of feyncalc_codegen.Channel keep working.


@dataclass
class GeneratedCode:
    """Container for the generated FeynCalc script."""
    code: str = ""
    process_type: ProcessType = ProcessType.UNSUPPORTED
    warnings: List[str] = field(default_factory=list)
    momentum_map: Dict[str, str] = field(default_factory=dict)
    channel: Optional[Channel] = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Pure symbol/formatting helpers live in fc_symbols so that `scattering`
# can reuse them without importing this module (which imports it in turn).
# Re-exported here: this module's public surface is unchanged.
from .fc_symbols import (  # noqa: F401
    _ANTIPARTICLE_SUFFIXES,
    _is_numeric,
    _fmt_mma,
    _is_antiparticle,
    _safe_symbol,
    _mass_symbol,
    _coupling_value,
)



#: (hbar c)^2 = 3.893793721e8 GeV^2 pb  (PDG physical constants).  The old
#: code hardcoded an nb factor only, while every cross-section benchmark
#: reports pb; emitting the constant by name keeps the script auditable.
GEV2_TO_BARN_COMMENT = "GeV2ToPb = 3.893793721*10^8;   (* (hbar c)^2 in GeV^2 pb *)"


# ---------------------------------------------------------------------------
# Main generator
# ---------------------------------------------------------------------------

class FeynCalcCodeGenerator:
    """
    Generate complete FeynCalc Mathematica scripts from Diagram objects.

    Usage::

        gen = FeynCalcCodeGenerator()
        result = gen.generate(diagram, sqrt_s=91.2)
        print(result.code)

    Args:
        assume_real_couplings: If True, skip coupling conjugation rules
            (treats all couplings as real). Default False: symbolic couplings get
            ``/. {g -> Conjugate[g], ...}`` rules so |M|^2 is correct for complex couplings.
    """

    def __init__(self, assume_real_couplings: bool = False, simplifications=None,
                 channel: Optional[str] = None):
        self.assume_real_couplings = assume_real_couplings
        self.simplifications = simplifications
        # Explicit s/t/u/contact selection for 2->2. None means "infer",
        # which falls back to s-channel and records the assumption in
        # GeneratedCode.warnings rather than hiding it.
        self.channel = channel
        self._channel_assumed = False

    def _collect_coupling_symbols(self, diagram: Diagram) -> List[str]:
        """Extract symbolic (non-numeric) coupling names from diagram vertices."""
        symbols = []
        for v in diagram.vertices:
            g = _coupling_value(v, diagram.couplings)
            if isinstance(g, str):
                if not _is_numeric(g):
                    symbols.append(g)
            elif isinstance(g, dict):
                for val in g.values():
                    if not _is_numeric(val):
                        symbols.append(val)
        return list(dict.fromkeys(symbols))  # dedupe, preserve order

    def generate(self, diagram: Diagram, sqrt_s: Optional[float] = None) -> GeneratedCode:
        """
        Main entry point.

        Args:
            diagram: A Diagram dataclass (from tools.nda.simple_diagram).
            sqrt_s: Centre-of-mass energy in GeV. OPTIONAL for 2->2 now that
                the cross section is built symbolically in ``s``; supply it
                only to have the script also report a number.

        Returns:
            GeneratedCode with the Mathematica script and metadata.
        """
        result = GeneratedCode()
        self._channel_assumed = False

        # 1. Classify
        proc = self._classify_process(diagram)
        result.process_type = proc

        if proc == ProcessType.UNSUPPORTED:
            result.warnings.append(
                f"Unsupported topology: {len(diagram.initial)} initial, "
                f"{len(diagram.final)} final, "
                f"{len(diagram.propagators)} propagators, "
                f"{sum(1 for p in diagram.propagators if p.is_loop_propagator)} loops."
            )
            return result

        # 2. Assign momenta
        mom_map = self._assign_momenta(diagram, proc)
        result.momentum_map = mom_map

        is_decay = proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP)

        # 3. Build sections
        sections: List[str] = []
        sections.append(self._header(diagram, proc))
        sections.append(self._mass_definitions(diagram))

        try:
            amp_section, amp_warnings = self._build_amplitude(diagram, proc, mom_map)
            sections.append(amp_section)
            result.warnings.extend(amp_warnings)

            if is_decay:
                # Decay ordering (unchanged, and validated): square and trace
                # first, then substitute rest-frame kinematics.
                coupling_syms = self._collect_coupling_symbols(diagram)
                sections.append(self._square_amplitude(coupling_syms))
                sections.append(self._spin_pol_sums(diagram, proc, mom_map))
                sections.append(self._trace_and_contract())
                sections.append(self._kinematics_decay(diagram, mom_map))
                sections.append(self._width_formula(diagram, proc, mom_map))
            else:
                # Scattering ordering: kinematics are fixed BEFORE the square,
                # so the traces are evaluated against on-shell scalar products
                # in (s, t) and no symbolic u survives into the observable.
                result.channel = self._infer_channel(diagram, proc)
                sections.append(self._kinematics_scattering(diagram, mom_map, sqrt_s))
                coupling_syms = self._collect_coupling_symbols(diagram)
                sections.append(self._square_amplitude(coupling_syms))
                sections.append(self._spin_pol_sums(diagram, proc, mom_map))
                sections.append(self._trace_and_contract())
                sections.append(
                    "(* Step 5: on-shell squared amplitude in (s, t) *)\n"
                    "ampSqKin = ampSq // Simplify;\n"
                )
                sections.append(self._cross_section_formula(diagram, mom_map, sqrt_s))
        except UnsupportedScattering as exc:
            result.process_type = ProcessType.UNSUPPORTED
            result.warnings.append(str(exc))
            return result

        if self._channel_assumed:
            result.warnings.append(
                "No channel was specified for this exchange diagram; assumed "
                "s-channel. Pass channel='s'|'t'|'u' to make it explicit."
            )

        sections.append(self._numerical_eval(diagram, proc, sqrt_s=sqrt_s))

        result.code = self._assemble_script(sections)
        return result

    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    def _classify_process(self, diagram: Diagram) -> ProcessType:
        n_init = len(diagram.initial)
        n_final = len(diagram.final)
        n_prop = len(diagram.propagators)
        n_loop = sum(1 for p in diagram.propagators if p.is_loop_propagator)

        if n_loop > 0:
            return ProcessType.UNSUPPORTED

        if n_init == 1 and n_final == 2 and n_prop == 0:
            return ProcessType.DECAY_1TO2
        if n_init == 1 and n_final == 2 and n_prop == 1:
            return ProcessType.DECAY_1TO2_1PROP
        if n_init == 2 and n_final == 2:
            return ProcessType.SCATTERING_2TO2

        return ProcessType.UNSUPPORTED

    # ------------------------------------------------------------------
    # Momentum assignment
    # ------------------------------------------------------------------

    def _assign_momenta(self, diagram: Diagram, proc: ProcessType) -> Dict[str, str]:
        """Return mapping {role -> momentum label}."""
        if proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP):
            mom = {"initial_0": "p", "final_0": "p1", "final_1": "p2"}
            if proc == ProcessType.DECAY_1TO2_1PROP:
                mom["prop_0"] = "q"
            return mom
        else:  # 2->2
            mom = {
                "initial_0": "p1", "initial_1": "p2",
                "final_0": "p3", "final_1": "p4",
            }
            if diagram.propagators:
                mom["prop_0"] = "q"
            return mom

    # ------------------------------------------------------------------
    # Spinor type assignment
    # ------------------------------------------------------------------

    def _spinor_expr(self, particle: Particle, momentum: str, role: str) -> str:
        """
        Return the FeynCalc spinor for an external fermion.

        role: 'incoming' or 'outgoing'
        """
        mass = _mass_symbol(particle, 0)
        anti = _is_antiparticle(particle.label)

        if role == "incoming":
            if anti:
                return f"SpinorVBar[{momentum}, {mass}]"
            else:
                return f"SpinorU[{momentum}, {mass}]"
        else:  # outgoing
            if anti:
                return f"SpinorV[{momentum}, {mass}]"
            else:
                return f"SpinorUBar[{momentum}, {mass}]"

    # ------------------------------------------------------------------
    # Code sections
    # ------------------------------------------------------------------

    def _header(self, diagram: Diagram, proc: ProcessType) -> str:
        labels_init = " ".join(p.label or "?" for p in diagram.initial)
        labels_final = " ".join(p.label or "?" for p in diagram.final)
        return (
            f'(* FeynCalc script generated by HEPTAPOD/Diagrammatica *)\n'
            f'(* Process: {labels_init} -> {labels_final} *)\n'
            f'(* Process type: {proc.name} *)\n\n'
            f'<< FeynCalc`\n'
        )

    def _mass_definitions(self, diagram: Diagram) -> str:
        lines = ["(* Mass definitions *)"]
        all_particles: List[Tuple[Particle, int]] = []
        for i, p in enumerate(diagram.initial):
            all_particles.append((p, i))
        for i, p in enumerate(diagram.final):
            all_particles.append((p, i))

        seen = set()
        for p, idx in all_particles:
            sym = _mass_symbol(p, idx)
            if sym not in seen:
                val = p.mass if p.mass is not None else 0
                lines.append(f"{sym} = {_fmt_mma(val)};")
                seen.add(sym)

        # Propagator masses
        for i, prop in enumerate(diagram.propagators):
            sym = f"mProp{i}"
            val = prop.mass if prop.mass is not None else 0
            lines.append(f"{sym} = {_fmt_mma(val)};")

        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------------
    # Vertex type normalization and coupling extraction
    # ------------------------------------------------------------------

    def _normalize_vtype(self, vtype: str) -> str:
        """Normalize vertex type: lowercase, strip hyphens/underscores, resolve aliases."""
        base = vtype.lower().replace("-", "").replace("_", "")
        # Strip valence suffixes
        for suffix in ("3pt", "4pt", "5pt"):
            if base.endswith(suffix):
                base = base[: -len(suffix)]
                break
        _ALIASES = {
            "yukawachiral": "chiral",
            "scalarchiral": "chiral",
            "vectorchiral": "chiral",
            "scalarva": "scalarva",
            "vectoraxial": "vectoraxial",
            "dipolechiral": "tensorchiral",
        }
        return _ALIASES.get(base, base)

    def _extract_chiral_couplings(self, coupling) -> Tuple[str, str]:
        """Extract gL, gR from coupling (string -> derive suffixes, dict -> use keys)."""
        if isinstance(coupling, dict):
            return coupling.get("gL", "gL"), coupling.get("gR", "gR")
        return f"{coupling}L", f"{coupling}R"

    def _extract_va_couplings(self, coupling) -> Tuple[str, str]:
        """Extract gV, gA from coupling (string -> derive suffixes, dict -> use keys)."""
        if isinstance(coupling, dict):
            return coupling.get("gV", "gV"), coupling.get("gA", "gA")
        return f"{coupling}V", f"{coupling}A"

    def _extract_va_sff_couplings(self, coupling) -> Tuple[str, str]:
        """Extract gS, gP from coupling (string -> derive suffixes, dict -> use keys)."""
        if isinstance(coupling, dict):
            return coupling.get("gS", "gS"), coupling.get("gP", "gP")
        return f"{coupling}S", f"{coupling}P"

    def _extract_single_coupling(self, coupling) -> str:
        """Extract a single coupling string (pass through str, take first dict value)."""
        if isinstance(coupling, dict):
            vals = list(coupling.values())
            return vals[0] if vals else "g"
        return str(coupling)

    # ------------------------------------------------------------------
    # VFF gamma structure dispatch
    # ------------------------------------------------------------------

    def _vff_gamma_structure(
        self, vtype: str, coupling, mu: str,
        vec_momentum: Optional[str] = None,
    ) -> str:
        """
        Build the VFF vertex factor string for FeynCalc.

        Args:
            vtype: Vertex type string (raw from diagram — normalized internally).
            coupling: Resolved coupling — a string for simple couplings, or a
                      dict for chiral / V-A vertices.
            mu: Lorentz index string (e.g., "mu0", "mu", "nu").
            vec_momentum: Momentum label for the vector boson (required for
                          tensor/dipole vertices; ignored for others).

        Returns:
            FeynCalc expression string for the vertex factor
            (without surrounding spinors).

        Notes:
            Uses FeynCalc's native chiral projectors:
              GA[7] = (1 - GA[5])/2 = P_L  (left-handed)
              GA[6] = (1 + GA[5])/2 = P_R  (right-handed)
        """
        base = self._normalize_vtype(vtype)

        # --- V-A: gV γ^μ - gA γ^μ γ^5 ---
        if base in ("vectoraxial", "va"):
            gV, gA = self._extract_va_couplings(coupling)
            return f"I GAD[{mu}] . (({gV}) - ({gA}) GA[5])"

        # --- Tensor / dipole: σ^{μν} k_ν ---
        if base in ("tensor", "dipole"):
            if vec_momentum is None:
                raise ValueError(
                    "Tensor/dipole vertex requires vec_momentum (the vector boson momentum)."
                )
            g = self._extract_single_coupling(coupling)
            return (
                f"I ({g}) DiracSigma[GA[{mu}], GA[nuT]] FV[{vec_momentum}, nuT]"
            )

        # --- Tensor-chiral / dipole-chiral: (gL P_L + gR P_R) σ^{μν} k_ν ---
        if base == "tensorchiral":
            if vec_momentum is None:
                raise ValueError(
                    "Tensor-chiral vertex requires vec_momentum (the vector boson momentum)."
                )
            gL, gR = self._extract_chiral_couplings(coupling)
            return (
                f"I (({gL}) GA[7] + ({gR}) GA[6]) . "
                f"DiracSigma[GA[{mu}], GA[nuT]] FV[{vec_momentum}, nuT]"
            )

        # --- Chiral VFF: γ^μ (gL P_L + gR P_R) ---
        if base == "chiral":
            gL, gR = self._extract_chiral_couplings(coupling)
            return f"I GAD[{mu}] . (({gL}) GA[7] + ({gR}) GA[6])"

        # --- Dict coupling fallback (agent passed dict but unknown type) ---
        if isinstance(coupling, dict):
            gL, gR = self._extract_chiral_couplings(coupling)
            return f"I GAD[{mu}] . (({gL}) GA[7] + ({gR}) GA[6])"

        # --- Single-projector types ---
        if base == "axialvector":
            return f"I ({coupling}) GAD[{mu}] . GA[5]"
        if base == "lefthanded":
            return f"I ({coupling}) GAD[{mu}] . GA[7]"
        if base == "righthanded":
            return f"I ({coupling}) GAD[{mu}] . GA[6]"

        # Default: pure vector γ^μ
        return f"I ({coupling}) GAD[{mu}]"

    # ------------------------------------------------------------------
    # SFF coupling structure dispatch
    # ------------------------------------------------------------------

    def _sff_coupling_structure(self, vtype: str, coupling) -> str:
        """
        Build the SFF vertex factor string for FeynCalc (no γ^μ — scalar parent).

        Args:
            vtype: Vertex type string (raw from diagram — normalized internally).
            coupling: Resolved coupling — a string for simple couplings, or a
                      dict for chiral / S-P scalar vertices.

        Returns:
            FeynCalc expression string for the vertex factor
            (without surrounding spinors).

        Notes:
            For chiral scalar couplings: ``yL GA[7] + yR GA[6]``
            (no γ^μ, unlike VFF where the vertex is γ^μ · projector).
        """
        base = self._normalize_vtype(vtype)

        # --- Scalar V-A: gS + gP γ^5 ---
        if base == "scalarva":
            gS, gP = self._extract_va_sff_couplings(coupling)
            return f"I (({gS}) + ({gP}) GA[5])"

        # --- Chiral scalar: yL P_L + yR P_R ---
        if base == "chiral":
            gL, gR = self._extract_chiral_couplings(coupling)
            return f"I (({gL}) GA[7] + ({gR}) GA[6])"

        # --- Dict coupling fallback ---
        if isinstance(coupling, dict):
            gL, gR = self._extract_chiral_couplings(coupling)
            return f"I (({gL}) GA[7] + ({gR}) GA[6])"

        # --- Pseudoscalar: i g γ^5 ---
        if base == "pseudoscalar":
            return f"I ({coupling}) GA[5]"

        # Default: scalar Yukawa  i·y
        return f"I ({coupling})"

    # ------------------------------------------------------------------
    # Amplitude construction
    # ------------------------------------------------------------------

    def _build_amplitude(
        self, diagram: Diagram, proc: ProcessType, mom_map: Dict[str, str]
    ) -> Tuple[str, List[str]]:
        """Build the amplitude expression. Returns (code_section, warnings)."""
        warnings: List[str] = []

        if proc == ProcessType.DECAY_1TO2:
            return self._amplitude_decay_no_prop(diagram, mom_map), warnings
        elif proc == ProcessType.DECAY_1TO2_1PROP:
            return self._amplitude_decay_1prop(diagram, mom_map), warnings
        elif proc == ProcessType.SCATTERING_2TO2:
            return self._amplitude_scattering(diagram, mom_map), warnings

        warnings.append("Cannot build amplitude for unsupported process.")
        return "(* Amplitude: unsupported *)\namp = 0;\n", warnings

    def _amplitude_decay_no_prop(self, diagram: Diagram, mom_map: Dict[str, str]) -> str:
        """1->2 decay with a single vertex, no propagator."""
        parent = diagram.initial[0]
        d0 = diagram.final[0]
        d1 = diagram.final[1]
        vertex = diagram.vertices[0] if diagram.vertices else None
        g = _coupling_value(vertex, diagram.couplings) if vertex else "g"
        vtype = (vertex.type.lower() if vertex else "").replace("-", "").replace("_", "")

        p = mom_map["initial_0"]
        p1 = mom_map["final_0"]
        p2 = mom_map["final_1"]

        lines = [f"(* Step 1: Amplitude for {parent.label} -> {d0.label} {d1.label} *)"]

        # Determine vertex structure from spins
        spins = sorted([parent.spin or 0, d0.spin or 0, d1.spin or 0])

        if spins == [0, 0, 0]:
            # SSS
            lines.append(f"amp = I ({g});")

        elif spins == [0, 0.5, 0.5]:
            # SFF or VFF?  Check parent spin
            if (parent.spin or 0) == 0:
                # SFF: Scalar/Pseudoscalar -> F Fbar
                fbar, f_ = self._order_fermion_pair(d0, d1, p1, p2, "outgoing")
                sff_vertex = self._sff_coupling_structure(vtype, g)
                lines.append(f"amp = {fbar} . ({sff_vertex}) . {f_};")
            else:
                # F -> f' S: parent is incoming fermion, one daughter is scalar
                parent_spinor = self._spinor_expr(parent, p, "incoming")
                sff_vertex = self._sff_coupling_structure(vtype, g)
                if (d0.spin or 0) == 0.5:
                    # d0 is the fermion daughter, d1 is the scalar
                    out_fermion = self._spinor_expr(d0, p1, "outgoing")
                else:
                    # d1 is the fermion daughter, d0 is the scalar
                    out_fermion = self._spinor_expr(d1, p2, "outgoing")
                lines.append(
                    f"amp = {out_fermion} . ({sff_vertex}) . {parent_spinor};"
                )

        elif spins == [0, 0, 1]:
            # SSV
            if (parent.spin or 0) == 1:
                # V -> S S: parent is the vector
                mu = "mu1"
                lines.append(
                    f"amp = I ({g}) PolarizationVector[{p}, {mu}] FVD[{p1} - {p2}, {mu}];"
                )
            else:
                # S -> S V: one daughter is the vector
                mu = "mu1"
                v_mom = p1 if (d0.spin or 0) == 1 else p2
                s_mom = p2 if (d0.spin or 0) == 1 else p1
                lines.append(
                    f"amp = I ({g}) PolarizationVector[{v_mom}, {mu}] FVD[{p} - {s_mom}, {mu}];"
                )

        elif spins == [0, 1, 1]:
            if (parent.spin or 0) == 1:
                # V -> S V: parent is vector, one daughter is scalar, one is vector
                mu0 = "mu0"
                if (d0.spin or 0) == 1:
                    v_mom, s_mom = p1, p2
                else:
                    v_mom, s_mom = p2, p1
                mu1 = "mu1"
                lines.append(
                    f"amp = I ({g}) PolarizationVector[{p}, {mu0}] "
                    f"PolarizationVector[{v_mom}, {mu1}] MTD[{mu0}, {mu1}];"
                )
            else:
                # S -> V V: scalar parent, two vector daughters
                mu1, mu2 = "mu1", "mu2"
                if vtype in ("fieldstrength", "dim5ff"):
                    # φFF: 2ig [(k1·k2)(ε1·ε2) - (k1·ε2)(k2·ε1)]
                    lines.append(
                        f"amp = 2 I ({g}) ("
                        f"SPD[{p1}, {p2}] MTD[{mu1}, {mu2}] - "
                        f"FVD[{p1}, {mu2}] FVD[{p2}, {mu1}]"
                        f") PolarizationVector[{p1}, {mu1}] PolarizationVector[{p2}, {mu2}];"
                    )
                elif vtype in ("dualfieldstrength", "dim5ffdual"):
                    # φFF̃: 2g ε^{μνρσ} k1_ρ k2_σ ε1_μ ε2_ν
                    lines.append(
                        f"amp = 2 ({g}) Eps[LorentzIndex[{mu1}], LorentzIndex[{mu2}], "
                        f"Momentum[{p1}], Momentum[{p2}]] "
                        f"PolarizationVector[{p1}, {mu1}] PolarizationVector[{p2}, {mu2}];"
                    )
                else:
                    # Default SVV: I g g^{μν}
                    lines.append(
                        f"amp = I ({g}) PolarizationVector[{p1}, {mu1}] "
                        f"PolarizationVector[{p2}, {mu2}] MTD[{mu1}, {mu2}];"
                    )

        elif spins == [0.5, 0.5, 1]:
            # VFF
            if (parent.spin or 0) == 1:
                # V -> F Fbar: parent is the vector boson
                mu = "mu0"  # parent polarization index
                fbar, f_ = self._order_fermion_pair(d0, d1, p1, p2, "outgoing")
                gamma_str = self._vff_gamma_structure(vtype, g, mu, vec_momentum=p)
                lines.append(
                    f"amp = PolarizationVector[{p}, {mu}] "
                    f"{fbar} . ({gamma_str}) . {f_};"
                )
            else:
                # F -> F V  (e.g., radiative fermion decay)
                mu = "mu1" if (d0.spin or 0) == 1 else "mu2"
                v_mom = p1 if (d0.spin or 0) == 1 else p2
                gamma_str = self._vff_gamma_structure(vtype, g, mu, vec_momentum=v_mom)
                # parent is incoming fermion
                parent_spinor = self._spinor_expr(parent, p, "incoming")
                if (d0.spin or 0) == 0.5:
                    out_fermion = self._spinor_expr(d0, p1, "outgoing")
                    lines.append(
                        f"amp = PolarizationVector[{v_mom}, {mu}] "
                        f"{out_fermion} . ({gamma_str}) . {parent_spinor};"
                    )
                else:
                    out_fermion = self._spinor_expr(d1, p2, "outgoing")
                    lines.append(
                        f"amp = PolarizationVector[{v_mom}, {mu}] "
                        f"{out_fermion} . ({gamma_str}) . {parent_spinor};"
                    )

        elif spins == [1, 1, 1]:
            # VVV: triple gauge — all three are vectors
            mu0, mu1, mu2 = "mu0", "mu1", "mu2"
            lines.append(
                f"amp = I ({g}) PolarizationVector[{p}, {mu0}] "
                f"PolarizationVector[{p1}, {mu1}] PolarizationVector[{p2}, {mu2}] ("
                f"MTD[{mu0}, {mu1}] FVD[{p} - {p1}, {mu2}] + "
                f"MTD[{mu1}, {mu2}] FVD[{p1} - {p2}, {mu0}] + "
                f"MTD[{mu2}, {mu0}] FVD[{p2} - {p}, {mu1}]);"
            )

        else:
            lines.append(f"(* Unknown vertex spin config: {spins} *)")
            lines.append(f"amp = I ({g});")

        return "\n".join(lines) + "\n"

    def _amplitude_decay_1prop(self, diagram: Diagram, mom_map: Dict[str, str]) -> str:
        """1->2 decay with one propagator (e.g., off-shell intermediate)."""
        parent = diagram.initial[0]
        d0 = diagram.final[0]
        d1 = diagram.final[1]
        prop = diagram.propagators[0]
        p = mom_map["initial_0"]
        p1 = mom_map["final_0"]
        p2 = mom_map["final_1"]
        q = mom_map["prop_0"]

        # Two vertices
        v0 = diagram.vertices[0] if len(diagram.vertices) > 0 else None
        v1 = diagram.vertices[1] if len(diagram.vertices) > 1 else v0
        g0 = _coupling_value(v0, diagram.couplings) if v0 else "g1"
        g1 = _coupling_value(v1, diagram.couplings) if v1 else "g2"

        lines = [
            f"(* Step 1: Amplitude with propagator *)",
            f"(* Parent: {parent.label}, Prop: {prop.label}, Final: {d0.label} {d1.label} *)",
        ]

        prop_spin = prop.spin if prop.spin is not None else 0
        prop_mass = f"mProp0"

        # Momentum conservation: q = p - p1 (or p - p2, depends on topology)
        # We'll use q = p1 + p2 for s-channel-like, q = p - p1 for t-channel-like
        lines.append(f"(* Propagator momentum: q = p1 + p2 = p *)")

        # Build propagator numerator
        if prop_spin == 0:
            prop_expr = f"I FAD[{{{q}, {prop_mass}}}]"
        elif prop_spin == 0.5:
            prop_expr = f"I (GSD[{q}] + {prop_mass}) FAD[{{{q}, {prop_mass}}}]"
        elif prop_spin == 1:
            mu_l, mu_r = "muP", "nuP"
            if prop.mass and prop.mass > 0:
                prop_expr = (
                    f"I (-MTD[{mu_l}, {mu_r}] + FVD[{q}, {mu_l}] FVD[{q}, {mu_r}]/{prop_mass}^2) "
                    f"FAD[{{{q}, {prop_mass}}}]"
                )
            else:
                prop_expr = f"I (-MTD[{mu_l}, {mu_r}]) FAD[{q}]"
        else:
            prop_expr = f"I FAD[{{{q}, {prop_mass}}}]"

        # Build vertex factors — simplified: treat as two VFF or SFF vertices
        # For now, emit a product of vertex1 * propagator * vertex2
        lines.append(f"(* Vertex 1 coupling: {g0}, Vertex 2 coupling: {g1} *)")
        lines.append(f"propNum = {prop_expr};")
        lines.append(f"amp = ({g0}) ({g1}) propNum;")
        lines.append(f"(* Note: full spinor/Lorentz structure depends on specific process *)")
        lines.append(f"(* For production use, specialize vertex structures per topology *)")

        return "\n".join(lines) + "\n"

    def _amplitude_scattering(self, diagram: Diagram, mom_map: Dict[str, str]) -> str:
        """2->2 tree amplitude, delegated to the compositional builder.

        The previous implementation covered exactly one exchange case
        (all-fermion externals with a vector mediator, s/t only -- u fell
        through to s) and emitted a structurally empty
        ``amp = I g^2 FAD[...]`` for everything else, which produced a
        confident wrong number rather than an error. `scattering` covers
        the full space and raises `UnsupportedScattering` outside it.
        """
        channel = self._infer_channel(diagram, ProcessType.SCATTERING_2TO2)
        return _build_scattering_amplitude(self, diagram, channel)

    # ------------------------------------------------------------------
    # Fermion ordering helpers
    # ------------------------------------------------------------------

    def _order_fermion_pair(
        self, p0: Particle, p1: Particle,
        mom0: str, mom1: str, role: str
    ) -> Tuple[str, str]:
        """
        For an outgoing fermion pair, return (UBar_expr, V_expr).
        For incoming, return (UBar_expr, V_expr) with incoming spinor types.

        Returns spinor expressions as (bar-spinor, spinor).
        """
        # Determine which is particle and which is antiparticle
        anti0 = _is_antiparticle(p0.label)
        anti1 = _is_antiparticle(p1.label)

        if role == "outgoing":
            if anti0 and not anti1:
                # p0 is antiparticle -> SpinorV, p1 is particle -> SpinorUBar
                return (
                    f"SpinorUBar[{mom1}, {_mass_symbol(p1, 1)}]",
                    f"SpinorV[{mom0}, {_mass_symbol(p0, 0)}]"
                )
            elif anti1 and not anti0:
                # p1 is antiparticle -> SpinorV, p0 is particle -> SpinorUBar
                return (
                    f"SpinorUBar[{mom0}, {_mass_symbol(p0, 0)}]",
                    f"SpinorV[{mom1}, {_mass_symbol(p1, 1)}]"
                )
            else:
                # Default: first is UBar, second is V
                return (
                    f"SpinorUBar[{mom0}, {_mass_symbol(p0, 0)}]",
                    f"SpinorV[{mom1}, {_mass_symbol(p1, 1)}]"
                )
        else:  # incoming
            if anti0 and not anti1:
                return (
                    f"SpinorU[{mom1}, {_mass_symbol(p1, 1)}]",
                    f"SpinorVBar[{mom0}, {_mass_symbol(p0, 0)}]"
                )
            elif anti1 and not anti0:
                return (
                    f"SpinorU[{mom0}, {_mass_symbol(p0, 0)}]",
                    f"SpinorVBar[{mom1}, {_mass_symbol(p1, 1)}]"
                )
            else:
                return (
                    f"SpinorU[{mom0}, {_mass_symbol(p0, 0)}]",
                    f"SpinorVBar[{mom1}, {_mass_symbol(p1, 1)}]"
                )

    def _order_fermion_pair_incoming(
        self, p0: Particle, p1: Particle, mom0: str, mom1: str
    ) -> Tuple[str, str]:
        """
        For an incoming fermion pair (e.g., e+ e-), return spinor bilinear parts.

        Convention for incoming:
          particle  -> SpinorU
          antiparticle -> SpinorVBar

        We return (bar_spinor, spinor) so the bilinear reads bar_spinor . Gamma . spinor.
        """
        anti0 = _is_antiparticle(p0.label)
        anti1 = _is_antiparticle(p1.label)

        if anti0 and not anti1:
            # p0 is antiparticle (VBar), p1 is particle (U)
            # bilinear: VBar[p0] . Gamma . U[p1]  but we want bar . G . spinor
            return (
                f"SpinorVBar[{mom0}, {_mass_symbol(p0, 0)}]",
                f"SpinorU[{mom1}, {_mass_symbol(p1, 1)}]"
            )
        elif anti1 and not anti0:
            # p1 is antiparticle, p0 is particle
            return (
                f"SpinorVBar[{mom1}, {_mass_symbol(p1, 1)}]",
                f"SpinorU[{mom0}, {_mass_symbol(p0, 0)}]"
            )
        else:
            # Default: assume p0 bar, p1 not
            return (
                f"SpinorVBar[{mom0}, {_mass_symbol(p0, 0)}]",
                f"SpinorU[{mom1}, {_mass_symbol(p1, 1)}]"
            )

    # ------------------------------------------------------------------
    # Square, spin sums, traces
    # ------------------------------------------------------------------

    def _square_amplitude(self, coupling_symbols: Optional[List[str]] = None) -> str:
        lines = "(* Step 2: Square the amplitude *)\n"
        lines += "ampCC = ComplexConjugate[amp];\n"
        if coupling_symbols and not self.assume_real_couplings:
            # Apply coupling conjugation as a separate replacement rule,
            # *after* ComplexConjugate has handled spinor chain reversal.
            # FeynCalc's ComplexConjugate[amp, Conjugate -> {...}] fails for
            # scalar chiral vertices (SFF with GA[7]/GA[6]) because the Dirac
            # structures interfere with the coupling-conjugation logic when
            # there are no Lorentz indices.  Separating the two operations
            # avoids this issue and works uniformly for all vertex types.
            rules = ", ".join(f"{s} -> Conjugate[{s}]" for s in coupling_symbols)
            lines += f"ampCC = ampCC /. {{{rules}}};\n"
        lines += "ampSq = amp ampCC;\n"
        return lines

    def _pol_sum_call(self, momentum: str, particle: Particle) -> str:
        """Generate DoPolarizationSums call for an external vector boson.

        Massive vectors: ``DoPolarizationSums[expr, p]`` — physical 3-state
        sum −g_μν + p_μ p_ν / M².

        Massless vectors: ``DoPolarizationSums[expr, p, 0]`` — covariant
        gauge reference vector n=0 (Ward identity ensures unphysical
        polarizations decouple).
        """
        mass = particle.mass
        is_massive = mass is not None and (isinstance(mass, str) or mass > 0)
        if is_massive:
            return f"ampSq = DoPolarizationSums[ampSq, {momentum}];"
        else:
            return f"ampSq = DoPolarizationSums[ampSq, {momentum}, 0];"

    def _spin_pol_sums(self, diagram: Diagram, proc: ProcessType, mom_map: Dict[str, str]) -> str:
        lines = ["(* Step 3: Spin and polarization sums *)"]

        # Check if there are any fermions
        has_fermions = any(
            (p.spin or 0) == 0.5
            for p in diagram.initial + diagram.final
        )
        if has_fermions:
            lines.append("ampSq = FermionSpinSum[ampSq];")

        # Polarization sums for external (on-shell) vector bosons.
        # Physical massive vectors: -g_{μν} + p_μ p_ν / p² (3-state sum).
        # Physical massless vectors: -g_{μν} (Ward identity ensures unphysical
        # polarizations decouple; equivalent to n=0 reference vector).
        # Note: VirtualBoson -> True gives -g_{μν} regardless of mass — only
        # correct for off-shell internal bosons, NOT for external particles.
        if proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP):
            # Check parent
            if (diagram.initial[0].spin or 0) == 1:
                p_mom = mom_map["initial_0"]
                lines.append(self._pol_sum_call(p_mom, diagram.initial[0]))

            # Check daughters
            for i, fp in enumerate(diagram.final):
                if (fp.spin or 0) == 1:
                    fp_mom = mom_map[f"final_{i}"]
                    lines.append(self._pol_sum_call(fp_mom, fp))
        else:  # Scattering
            for i, ip in enumerate(diagram.initial):
                if (ip.spin or 0) == 1:
                    ip_mom = mom_map[f"initial_{i}"]
                    lines.append(self._pol_sum_call(ip_mom, ip))
            for i, fp in enumerate(diagram.final):
                if (fp.spin or 0) == 1:
                    fp_mom = mom_map[f"final_{i}"]
                    lines.append(self._pol_sum_call(fp_mom, fp))

        return "\n".join(lines) + "\n"

    def _trace_and_contract(self) -> str:
        return (
            "(* Step 4: Evaluate traces and contract *)\n"
            "ampSq = DiracSimplify[ampSq] // Contract // Simplify;\n"
        )

    # ------------------------------------------------------------------
    # Kinematics
    # ------------------------------------------------------------------

    def _kinematics_decay(self, diagram: Diagram, mom_map: Dict[str, str]) -> str:
        """Rest-frame kinematic substitutions for 1->2 decay.

        Uses FCClearScalarProducts + ScalarProduct assignments (global)
        so FeynCalc resolves kinematics reliably — avoids late /. rules
        that can fail to substitute inside FeynCalc internal objects.
        """
        parent = diagram.initial[0]
        d0 = diagram.final[0]
        d1 = diagram.final[1]

        M = _mass_symbol(parent, 0)
        m1 = _mass_symbol(d0, 0)
        m2 = _mass_symbol(d1, 1)

        p = mom_map["initial_0"]
        p1 = mom_map["final_0"]
        p2 = mom_map["final_1"]

        lines = [
            "(* Step 5: Kinematics — rest frame of parent *)",
            f"(* p = ({M}, 0, 0, 0),  p1 + p2 = p *)",
            f"FCClearScalarProducts[];",
            f"ScalarProduct[{p}, {p}] = {M}^2;",
            f"ScalarProduct[{p1}, {p1}] = {m1}^2;",
            f"ScalarProduct[{p2}, {p2}] = {m2}^2;",
            f"ScalarProduct[{p}, {p1}] = ({M}^2 + {m1}^2 - {m2}^2)/2;",
            f"ScalarProduct[{p}, {p2}] = ({M}^2 - {m1}^2 + {m2}^2)/2;",
            f"ScalarProduct[{p1}, {p2}] = ({M}^2 - {m1}^2 - {m2}^2)/2;",
            f"ampSqKin = ampSq // Simplify;",
        ]

        return "\n".join(lines) + "\n"

    def _width_formula(self, diagram: Diagram, proc: ProcessType, mom_map: Dict[str, str]) -> str:
        """Compute partial decay width."""
        from tools.nda.simple_diagram import compute_symmetry_factor

        parent = diagram.initial[0]
        d0 = diagram.final[0]
        d1 = diagram.final[1]

        M = _mass_symbol(parent, 0)
        m1 = _mass_symbol(d0, 0)
        m2 = _mass_symbol(d1, 1)

        # Number of initial spin states
        spin_init = parent.spin if parent.spin is not None else 0
        n_spin_init = int(2 * spin_init + 1)

        # Identical-particle symmetry factor
        sym_factor = compute_symmetry_factor(diagram)

        lines = [
            "(* Step 6: Partial decay width *)",
            f"(* Gamma = pMag / (8 pi M^2) * (1/nInit) * |M|^2 * colorFactor / symmetryFactor *)",
            f"pMag = Sqrt[({M}^2 - ({m1} + {m2})^2)({M}^2 - ({m1} - {m2})^2)] / (2 {M});",
            f"nInit = {n_spin_init};",
            f"colorFactor = {_fmt_mma(diagram.color_factor)};",
            f"symmetryFactor = {sym_factor};",
            f"width = pMag / (8 Pi {M}^2) * (1/nInit) * ampSqKin * colorFactor / symmetryFactor;",
            f"width = width // Simplify;",
        ]

        return "\n".join(lines) + "\n"

    def _kinematics_scattering(
        self, diagram: Diagram, mom_map: Dict[str, str],
        sqrt_s: Optional[float] = None
    ) -> str:
        """Delegated: explicit ScalarProducts in (s, t), u eliminated on shell.

        Replaces the old ``SetMandelstam`` block, which left ``u`` alive as
        an independent symbol and mixed a NUMERIC sqrt_s into the flux
        prefactor while |M|^2 still carried a SYMBOLIC s -- so the two never
        met and ``N[sigma]`` never resolved.
        """
        return _scattering_kinematics(diagram)

    def _cross_section_formula(
        self, diagram: Diagram, mom_map: Dict[str, str],
        sqrt_s: Optional[float] = None
    ) -> str:
        """Delegated: the 2->2 master formula, symbolic in s.

        Restores the identical-particle symmetry factor (absent before, which
        made phi phi -> phi phi come out exactly 2x too large) and the
        massless-vector polarisation count.
        """
        return _scattering_cross_section(diagram)

    # ------------------------------------------------------------------
    # Numerical evaluation + markers
    # ------------------------------------------------------------------

    def _numerical_eval(self, diagram: Diagram, proc: ProcessType,
                        sqrt_s: Optional[float] = None) -> str:
        """Emit numerical evaluation, symbolic extraction, and LaTeX markers.

        Emits three categories of structured output:
          - SYMBOLIC_RESULT: Mathematica InputForm expressions
          - NUMERICAL_RESULT: Floating-point numerical values
          - LATEX_RESULT: LaTeX strings via TeXForm[] for paper-ready formulas

        Intermediate quantities extracted:
          - ampSq: Spin/polarization-summed |M|^2 after kinematic substitution
          - width (decay) or sigma (scattering): Final observable
        """
        lines = ["(* Step 7: Symbolic extraction and numerical evaluation *)"]

        # -- Intermediate: |M|^2 after kinematics --
        lines.extend([
            '',
            '(* Squared amplitude after kinematics *)',
            'Print["SYMBOLIC_RESULT[ampSq]: ", ampSqKin];',
            'Print["LATEX_RESULT[ampSq]: ", ToString[TeXForm[ampSqKin]]];',
        ])

        if proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP):
            lines.extend([
                '',
                '(* Decay width — symbolic and numerical *)',
                'Print["SYMBOLIC_RESULT[width]: ", width];',
                'Print["LATEX_RESULT[width]: ", ToString[TeXForm[width]]];',
                'widthNum = N[width];',
                'Print["NUMERICAL_RESULT[width_GeV]: ", widthNum];',
                '(* Convert to MeV for convenience *)',
                'Print["NUMERICAL_RESULT[width_MeV]: ", widthNum * 1000];',
            ])
        else:
            lines.extend([
                '',
                '(* Cross section — symbolic in s *)',
                'Print["SYMBOLIC_RESULT[sigma]: ", sigma];',
                'Print["LATEX_RESULT[sigma]: ", ToString[TeXForm[sigma]]];',
                'Print["SYMBOLIC_RESULT[dSigmaDt]: ", dSigmaDt];',
            ])
            if sqrt_s is not None:
                lines.extend([
                    '',
                    '(* Numerical evaluation at the requested sqrt(s) *)',
                    f'sigmaNum = N[sigma /. s -> ({_fmt_mma(sqrt_s)})^2];',
                    '(* A well-formed symbolic sigma can still evaluate to',
                    '   Undefined when the t-endpoints cancel; fall back to',
                    '   substituting first and integrating numerically. *)',
                    'If[!NumericQ[sigmaNum] || !FreeQ[sigmaNum, Undefined] ||',
                    '   !FreeQ[sigmaNum, Indeterminate] || !FreeQ[sigmaNum, DirectedInfinity],',
                    f'  sigmaNum = sigmaNIntegrate[{{s -> ({_fmt_mma(sqrt_s)})^2}}]];',
                    'Print["NUMERICAL_RESULT[sigma_GeV2]: ", sigmaNum];',
                    GEV2_TO_BARN_COMMENT,
                    'Print["NUMERICAL_RESULT[sigma_pb]: ", sigmaNum * GeV2ToPb];',
                    'Print["NUMERICAL_RESULT[sigma_fb]: ", sigmaNum * GeV2ToPb * 1000];',
                    'Print["NUMERICAL_RESULT[sigma_nb]: ", sigmaNum * GeV2ToPb / 1000];',
                ])

        lines.append('Print["STATUS: complete"];')

        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------------
    # Channel inference
    # ------------------------------------------------------------------

    def _infer_channel(self, diagram: Diagram, proc: ProcessType) -> Channel:
        """Resolve the s/t/u channel for a 2->2 diagram.

        The channel is a PROPERTY OF THE DIAGRAM, not something a topology
        spec determines: the same four external legs and the same mediator
        describe three different diagrams. The old heuristic returned
        ``Channel.S`` unconditionally, so every t- and u-channel request was
        silently computed as an s-channel one.

        Resolution order: an explicit ``channel`` on the generator, then a
        ``channel`` key carried by the diagram's topology string, then
        s-channel with a recorded assumption.
        """
        if proc != ProcessType.SCATTERING_2TO2:
            return Channel.S

        if not diagram.propagators:
            return Channel.CONTACT

        explicit = self.channel
        if explicit is None:
            topo = (diagram.topology or "").lower()
            for name in ("t_channel", "u_channel", "s_channel"):
                if name in topo:
                    explicit = name[0]
                    break

        if explicit is not None:
            key = str(explicit).strip().lower()
            try:
                return {"s": Channel.S, "t": Channel.T, "u": Channel.U,
                        "contact": Channel.CONTACT}[key]
            except KeyError:
                raise UnsupportedScattering(
                    f"Unknown scattering channel {explicit!r}; "
                    "expected one of s, t, u, contact."
                )

        self._channel_assumed = True
        return Channel.S

    # ------------------------------------------------------------------
    # Assembly
    # ------------------------------------------------------------------

    def _assemble_script(self, sections: List[str]) -> str:
        return "\n".join(sections)


# ---------------------------------------------------------------------------
# Symbolic code generator (masses/couplings left as symbols)
# ---------------------------------------------------------------------------

class SymbolicFeynCalcCodeGenerator(FeynCalcCodeGenerator):
    """
    Generate FeynCalc scripts with symbolic (unresolved) masses and couplings.

    The amplitude construction methods already use mass *symbols* like mH, mb
    internally — this subclass simply avoids binding them to numerical values.
    """

    def _mass_definitions(self, diagram: Diagram) -> str:
        """Emit mass symbols without numerical assignments."""
        all_particles: List[Tuple[Particle, int]] = []
        for i, p in enumerate(diagram.initial):
            all_particles.append((p, i))
        for i, p in enumerate(diagram.final):
            all_particles.append((p, i))

        seen = set()
        symbols = []
        for p, idx in all_particles:
            sym = _mass_symbol(p, idx)
            if sym not in seen:
                symbols.append(sym)
                seen.add(sym)

        for i, prop in enumerate(diagram.propagators):
            symbols.append(f"mProp{i}")

        lines = [
            "(* Mass definitions — symbolic (no numerical values assigned) *)",
            f"(* Masses: {', '.join(symbols)} *)",
        ]
        return "\n".join(lines) + "\n"

    def _numerical_eval(self, diagram: Diagram, proc: ProcessType,
                        sqrt_s: Optional[float] = None) -> str:
        """Emit only symbolic and LaTeX results, skip numerical evaluation."""
        lines = ["(* Step 7: Symbolic extraction (no numerical evaluation) *)"]

        lines.extend([
            '',
            '(* Squared amplitude after kinematics *)',
            'Print["SYMBOLIC_RESULT[ampSq]: ", ampSqKin];',
            'Print["LATEX_RESULT[ampSq]: ", ToString[TeXForm[ampSqKin]]];',
        ])

        if proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP):
            result_var = "width"
            lines.extend([
                '',
                '(* Decay width — symbolic only *)',
                'Print["SYMBOLIC_RESULT[width]: ", width];',
                'Print["LATEX_RESULT[width]: ", ToString[TeXForm[width]]];',
            ])
        else:
            result_var = "sigma"
            lines.extend([
                '',
                '(* Cross section — symbolic only *)',
                'Print["SYMBOLIC_RESULT[sigma]: ", sigma];',
                'Print["LATEX_RESULT[sigma]: ", ToString[TeXForm[sigma]]];',
                'Print["SYMBOLIC_RESULT[dSigmaDt]: ", dSigmaDt];',
            ])

        # In-script simplifications (optional)
        if self.simplifications:
            s = self.simplifications
            sv = f"{result_var}Simplified"
            lines.extend(['', f'(* Post-computation simplifications *)'])
            lines.append(f'{sv} = {result_var};')
            if s.get("substitutions"):
                rules = ", ".join(
                    f"{k} -> {v}" for k, v in s["substitutions"].items()
                )
                lines.append(f'{sv} = {sv} /. {{{rules}}};')
            if s.get("limit"):
                lim = s["limit"]
                var = lim.get("var", "x")
                point = lim.get("point", "0")
                direction = lim.get("direction")
                if direction:
                    lines.append(
                        f'{sv} = Limit[{sv}, {var} -> {point}, Direction -> {direction}];'
                    )
                else:
                    lines.append(f'{sv} = Limit[{sv}, {var} -> {point}];')
            if s.get("series"):
                ser = s["series"]
                var = ser.get("var", "eps")
                point = ser.get("point", "0")
                order = ser.get("order", 1)
                lines.append(f'{sv} = Normal[Series[{sv}, {{{var}, {point}, {order}}}]];')
            sfn = s.get("simplify", "Simplify")
            if sfn != "None":
                if s.get("assumptions"):
                    assumptions_str = ", ".join(s["assumptions"])
                    lines.append(
                        f'{sv} = Assuming[{{{assumptions_str}}}, {sfn}[{sv}]];'
                    )
                else:
                    lines.append(f'{sv} = {sfn}[{sv}];')
            lines.append(
                f'Print["SYMBOLIC_RESULT[{result_var}_simplified]: ", {sv}];'
            )
            lines.append(
                f'Print["LATEX_RESULT[{result_var}_simplified]: ", ToString[TeXForm[{sv}]]];'
            )

        lines.append('Print["STATUS: complete"];')
        return "\n".join(lines) + "\n"
