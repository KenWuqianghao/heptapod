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
tools/wolfram/wolfram_runner.py parsing.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

from tools.nda.simple_diagram import Diagram, Particle, Vertex, Propagator


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

class ProcessType(Enum):
    """Classification of the scattering / decay process."""
    DECAY_1TO2 = auto()            # 1 initial, 2 final, 0 propagators
    DECAY_1TO2_1PROP = auto()      # 1 initial, 2 final, 1 propagator
    SCATTERING_2TO2 = auto()       # 2 initial, 2 final
    UNSUPPORTED = auto()


class Channel(Enum):
    """Scattering channel for 2->2 processes."""
    S = auto()
    T = auto()
    U = auto()
    CONTACT = auto()


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

_ANTIPARTICLE_SUFFIXES = ("bar", "~", "+")


def _is_numeric(s: str) -> bool:
    """Check if a string represents a numeric value."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def _fmt_mma(val) -> str:
    """Format a number for Mathematica — use integer form when possible.

    Avoids float contamination: ``3.0`` → ``3``, ``1.0`` → ``1``.
    Mathematica treats ``3.0`` as machine-precision, which spoils symbolic results.
    """
    if isinstance(val, float) and val == int(val):
        return str(int(val))
    return str(val)


def _is_antiparticle(label: str) -> bool:
    """Heuristic: is this an antiparticle label?"""
    if label is None:
        return False
    label_lower = label.lower().strip()
    # Explicit suffixes
    for suf in _ANTIPARTICLE_SUFFIXES:
        if label_lower.endswith(suf):
            return True
    # Positron
    if label_lower in ("e+", "mu+", "tau+", "positron"):
        return True
    return False


def _safe_symbol(label: str) -> str:
    """Turn a particle label into a safe Mathematica symbol fragment."""
    if label is None:
        return "X"
    s = label.replace("+", "p").replace("-", "m").replace("~", "bar").replace("/", "")
    s = s.replace("(", "").replace(")", "").replace(" ", "")
    if s and s[0].isdigit():
        s = "p" + s
    return s or "X"


def _mass_symbol(particle: Particle, idx: int) -> str:
    """Return a Mathematica symbol for the mass of a particle."""
    if particle.label:
        return f"m{_safe_symbol(particle.label)}"
    return f"m{idx}"


def _coupling_value(vertex: Vertex, couplings: Dict[str, float]) -> "str | Dict[str, str]":
    """Resolve coupling to Mathematica expression.

    Returns a string for simple couplings, or a dict of strings for
    chiral couplings (e.g., {"gL": "0.27", "gR": "0.23"}).
    """
    c = vertex.coupling
    if isinstance(c, (int, float)):
        return str(c)
    if isinstance(c, str):
        if c in couplings:
            return str(couplings[c])
        return c  # leave symbolic
    if isinstance(c, dict):
        resolved = {}
        for key, val in c.items():
            if isinstance(val, (int, float)):
                resolved[key] = str(val)
            elif isinstance(val, str):
                resolved[key] = str(couplings[val]) if val in couplings else val
            else:
                resolved[key] = str(val)
        return resolved
    return "g"


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

    def __init__(self, assume_real_couplings: bool = False, simplifications=None):
        self.assume_real_couplings = assume_real_couplings
        self.simplifications = simplifications

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
            sqrt_s: Centre-of-mass energy in GeV (required for 2->2 scattering).

        Returns:
            GeneratedCode with the Mathematica script and metadata.
        """
        result = GeneratedCode()

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

        if proc == ProcessType.SCATTERING_2TO2 and sqrt_s is None:
            result.warnings.append("sqrt_s is required for 2->2 scattering.")
            return result

        # 2. Assign momenta
        mom_map = self._assign_momenta(diagram, proc)
        result.momentum_map = mom_map

        # 3. Build sections
        sections: List[str] = []
        sections.append(self._header(diagram, proc))
        sections.append(self._mass_definitions(diagram))

        # 4. Build amplitude
        amp_section, amp_warnings = self._build_amplitude(diagram, proc, mom_map)
        sections.append(amp_section)
        result.warnings.extend(amp_warnings)

        # 5. Square + spin/pol sums + traces
        coupling_syms = self._collect_coupling_symbols(diagram)
        sections.append(self._square_amplitude(coupling_syms))
        sections.append(self._spin_pol_sums(diagram, proc, mom_map))
        sections.append(self._trace_and_contract())

        # 6. Kinematics
        if proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP):
            sections.append(self._kinematics_decay(diagram, mom_map))
        else:
            sections.append(self._kinematics_scattering(diagram, mom_map, sqrt_s))

        # 7. Observable
        if proc in (ProcessType.DECAY_1TO2, ProcessType.DECAY_1TO2_1PROP):
            sections.append(self._width_formula(diagram, proc, mom_map))
        else:
            sections.append(self._cross_section_formula(diagram, mom_map, sqrt_s))
            result.channel = self._infer_channel(diagram, proc)

        # 8. Numerical evaluation + markers
        sections.append(self._numerical_eval(diagram, proc))

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
        """2->2 scattering amplitude."""
        i0 = diagram.initial[0]
        i1 = diagram.initial[1]
        f0 = diagram.final[0]
        f1 = diagram.final[1]
        p1 = mom_map["initial_0"]
        p2 = mom_map["initial_1"]
        p3 = mom_map["final_0"]
        p4 = mom_map["final_1"]

        lines = [
            f"(* Step 1: Amplitude for {i0.label} {i1.label} -> {f0.label} {f1.label} *)"
        ]

        channel = self._infer_channel(diagram, ProcessType.SCATTERING_2TO2)

        if not diagram.propagators:
            # Contact 4-point interaction
            return self._amplitude_scattering_contact(diagram, mom_map, lines)

        prop = diagram.propagators[0]
        prop_mass = "mProp0"
        vertex = diagram.vertices[0] if diagram.vertices else None
        g = _coupling_value(vertex, diagram.couplings) if vertex else "g"

        # All external fermions? (e.g., e+e- -> mu+mu-)
        all_fermion = all(
            (p.spin or 0) == 0.5
            for p in [i0, i1, f0, f1]
        )

        if all_fermion and (prop.spin is None or prop.spin == 1):
            # Fermion scattering via vector boson (most common 2->2)
            return self._amplitude_ffff_vector(diagram, mom_map, channel, lines)

        # Generic fallback: coupling * propagator
        q = mom_map.get("prop_0", "q")
        if channel == Channel.S:
            lines.append(f"q = {p1} + {p2};")
        elif channel == Channel.T:
            lines.append(f"q = {p1} - {p3};")
        else:
            lines.append(f"q = {p1} - {p4};")

        prop_spin = prop.spin if prop.spin is not None else 1
        if prop_spin == 0:
            lines.append(f"amp = I ({g})^2 FAD[{{{q}, {prop_mass}}}];")
        elif prop_spin == 1:
            if prop.mass and prop.mass > 0:
                lines.append(f"amp = I ({g})^2 FAD[{{{q}, {prop_mass}}}];")
            else:
                lines.append(f"amp = I ({g})^2 FAD[{q}];")
        else:
            lines.append(f"amp = I ({g})^2 FAD[{{{q}, {prop_mass}}}];")

        return "\n".join(lines) + "\n"

    def _amplitude_ffff_vector(
        self, diagram: Diagram, mom_map: Dict[str, str],
        channel: Channel, lines: List[str]
    ) -> str:
        """e+e- -> mu+mu- style: fermion pair via vector boson."""
        i0 = diagram.initial[0]
        i1 = diagram.initial[1]
        f0 = diagram.final[0]
        f1 = diagram.final[1]
        p1 = mom_map["initial_0"]
        p2 = mom_map["initial_1"]
        p3 = mom_map["final_0"]
        p4 = mom_map["final_1"]

        prop = diagram.propagators[0]
        prop_mass = "mProp0"

        # Initial-state vertex (vertices[0])
        v0 = diagram.vertices[0] if diagram.vertices else None
        g0 = _coupling_value(v0, diagram.couplings) if v0 else "g"
        vtype0 = (v0.type.lower() if v0 else "").replace("-", "").replace("_", "")

        # Final-state vertex: use vertices[1] if available, else reuse vertices[0]
        v1 = diagram.vertices[1] if len(diagram.vertices) >= 2 else v0
        g1 = _coupling_value(v1, diagram.couplings) if v1 else "g"
        vtype1 = (v1.type.lower() if v1 else "").replace("-", "").replace("_", "")

        mu = "mu"  # Lorentz index on propagator

        # Determine spinor ordering for initial state
        ubar_i, v_i = self._order_fermion_pair_incoming(i0, i1, p1, p2)
        # Final state
        ubar_f, v_f = self._order_fermion_pair(f0, f1, p3, p4, "outgoing")

        # Build gamma structures for both vertices
        gamma_str_init = self._vff_gamma_structure(vtype0, g0, mu)
        gamma_str_final = self._vff_gamma_structure(vtype1, g1, "nu")

        if channel == Channel.S:
            lines.append(f"(* s-channel: ({i0.label} {i1.label}) -> propagator -> ({f0.label} {f1.label}) *)")
            if prop.mass and prop.mass > 0:
                prop_expr = f"(-MTD[{mu}, nu] + FVD[{p1}+{p2}, {mu}] FVD[{p1}+{p2}, nu]/{prop_mass}^2) FAD[{{{p1}+{p2}, {prop_mass}}}]"
            else:
                prop_expr = f"(-MTD[{mu}, nu]) FAD[{p1}+{p2}]"

            lines.append(
                f"amp = ({ubar_i} . ({gamma_str_init}) . {v_i}) "
                f"({prop_expr}) "
                f"({ubar_f} . ({gamma_str_final}) . {v_f});"
            )
        elif channel == Channel.T:
            lines.append(f"(* t-channel *)")
            if prop.mass and prop.mass > 0:
                prop_expr = f"(-MTD[{mu}, nu] + FVD[{p1}-{p3}, {mu}] FVD[{p1}-{p3}, nu]/{prop_mass}^2) FAD[{{{p1}-{p3}, {prop_mass}}}]"
            else:
                prop_expr = f"(-MTD[{mu}, nu]) FAD[{p1}-{p3}]"

            gamma_str_t_init = self._vff_gamma_structure(vtype0, g0, mu)
            gamma_str_t_final = self._vff_gamma_structure(vtype1, g1, "nu")
            lines.append(
                f"amp = ({ubar_f} . ({gamma_str_t_init}) . SpinorU[{p1}, m{_safe_symbol(i0.label)}]) "
                f"({prop_expr}) "
                f"(SpinorUBar[{p4}, m{_safe_symbol(f1.label)}] . ({gamma_str_t_final}) . {v_i});"
            )
        else:
            # Default to s-channel
            if prop.mass and prop.mass > 0:
                prop_expr = f"(-MTD[{mu}, nu] + FVD[{p1}+{p2}, {mu}] FVD[{p1}+{p2}, nu]/{prop_mass}^2) FAD[{{{p1}+{p2}, {prop_mass}}}]"
            else:
                prop_expr = f"(-MTD[{mu}, nu]) FAD[{p1}+{p2}]"

            lines.append(
                f"amp = ({ubar_i} . ({gamma_str_init}) . {v_i}) "
                f"({prop_expr}) "
                f"({ubar_f} . ({gamma_str_final}) . {v_f});"
            )

        return "\n".join(lines) + "\n"

    def _amplitude_scattering_contact(
        self, diagram: Diagram, mom_map: Dict[str, str], lines: List[str]
    ) -> str:
        """Contact 4-point interaction amplitude."""
        i0 = diagram.initial[0]
        i1 = diagram.initial[1]
        f0 = diagram.final[0]
        f1 = diagram.final[1]
        p1 = mom_map["initial_0"]
        p2 = mom_map["initial_1"]
        p3 = mom_map["final_0"]
        p4 = mom_map["final_1"]
        vertex = diagram.vertices[0] if diagram.vertices else None
        g = _coupling_value(vertex, diagram.couplings) if vertex else "g"

        spins = sorted([(p.spin or 0) for p in [i0, i1, f0, f1]])

        if spins == [0, 0, 0, 0]:
            lines.append(f"amp = I ({g});")
        elif spins == [0.5, 0.5, 0.5, 0.5]:
            mu = "mu"
            ubar_i, v_i = self._order_fermion_pair_incoming(i0, i1, p1, p2)
            ubar_f, v_f = self._order_fermion_pair(f0, f1, p3, p4, "outgoing")
            lines.append(
                f"amp = ({ubar_i} . (I ({g}) GAD[{mu}]) . {v_i}) "
                f"({ubar_f} . (I ({g}) GAD[{mu}]) . {v_f});"
            )
        else:
            lines.append(f"amp = I ({g})^2;")

        return "\n".join(lines) + "\n"

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

    def _kinematics_scattering(
        self, diagram: Diagram, mom_map: Dict[str, str], sqrt_s: float
    ) -> str:
        """Mandelstam kinematics for 2->2 scattering.

        Uses FCClearScalarProducts before SetMandelstam so FeynCalc
        starts with a clean slate and the Mandelstam relations resolve properly.
        """
        i0 = diagram.initial[0]
        i1 = diagram.initial[1]
        f0 = diagram.final[0]
        f1 = diagram.final[1]

        m1 = _mass_symbol(i0, 0)
        m2 = _mass_symbol(i1, 1)
        m3 = _mass_symbol(f0, 0)
        m4 = _mass_symbol(f1, 1)

        p1 = mom_map["initial_0"]
        p2 = mom_map["initial_1"]
        p3 = mom_map["final_0"]
        p4 = mom_map["final_1"]

        lines = [
            "(* Step 5: Mandelstam kinematics *)",
            f"FCClearScalarProducts[];",
            f"SetMandelstam[s, t, u, {p1}, {p2}, -{p3}, -{p4}, {m1}, {m2}, {m3}, {m4}];",
            f"ampSqKin = ampSq // Simplify;",
        ]

        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------------
    # Observables
    # ------------------------------------------------------------------

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

    def _cross_section_formula(
        self, diagram: Diagram, mom_map: Dict[str, str], sqrt_s: float
    ) -> str:
        """Compute total cross section for 2->2."""
        i0 = diagram.initial[0]
        i1 = diagram.initial[1]
        f0 = diagram.final[0]
        f1 = diagram.final[1]

        m1 = _mass_symbol(i0, 0)
        m2 = _mass_symbol(i1, 1)
        m3 = _mass_symbol(f0, 0)
        m4 = _mass_symbol(f1, 1)

        # Spin averaging for initial state
        s0 = i0.spin if i0.spin is not None else 0.5
        s1 = i1.spin if i1.spin is not None else 0.5
        n_spin = int((2*s0 + 1) * (2*s1 + 1))

        lines = [
            "(* Step 6: Total cross section *)",
            f"sqrtS = {sqrt_s};",
            f"sVal = sqrtS^2;",
            f"",
            f"(* Kallen function *)",
            f"kallen[a_, b_, c_] := a^2 + b^2 + c^2 - 2 a b - 2 a c - 2 b c;",
            f"",
            f"(* Initial and final state momenta in CM frame *)",
            f"pI = Sqrt[kallen[sVal, {m1}^2, {m2}^2]] / (2 sqrtS);",
            f"pF = Sqrt[kallen[sVal, {m3}^2, {m4}^2]] / (2 sqrtS);",
            f"",
            f"(* Spin averaging factor *)",
            f"nInit = {n_spin};",
            f"colorFactor = {_fmt_mma(diagram.color_factor)};",
            f"",
            f"(* dsigma/dt = |M|^2 / (64 pi s pI^2) *)",
            f"(* Integrate over t: tMin to tMax *)",
            f"tMin = ({m1}^2 + {m3}^2) - (sVal + {m1}^2 - {m2}^2)(sVal + {m3}^2 - {m4}^2)/(2 sVal) - 2 pI pF;",
            f"tMax = ({m1}^2 + {m3}^2) - (sVal + {m1}^2 - {m2}^2)(sVal + {m3}^2 - {m4}^2)/(2 sVal) + 2 pI pF;",
            f"",
            f"sigma = colorFactor / nInit * Integrate[ampSqKin / (64 Pi sVal pI^2), {{t, tMin, tMax}}];",
            f"sigma = sigma // Simplify;",
        ]

        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------------
    # Numerical evaluation + markers
    # ------------------------------------------------------------------

    def _numerical_eval(self, diagram: Diagram, proc: ProcessType) -> str:
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
                '(* Cross section — symbolic and numerical *)',
                'Print["SYMBOLIC_RESULT[sigma]: ", sigma];',
                'Print["LATEX_RESULT[sigma]: ", ToString[TeXForm[sigma]]];',
                'sigmaNum = N[sigma];',
                'Print["NUMERICAL_RESULT[sigma_GeV2]: ", sigmaNum];',
                '(* Convert to nb: 1 GeV^-2 = 0.3894e6 nb *)',
                'Print["NUMERICAL_RESULT[sigma_nb]: ", sigmaNum * 0.3894*10^6];',
            ])

        lines.append('Print["STATUS: complete"];')

        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------------
    # Channel inference
    # ------------------------------------------------------------------

    def _infer_channel(self, diagram: Diagram, proc: ProcessType) -> Channel:
        """Infer s/t/u channel for 2->2 scattering."""
        if proc != ProcessType.SCATTERING_2TO2:
            return Channel.S

        if not diagram.propagators:
            return Channel.CONTACT

        # Simple heuristic: if initial pair has a flavor-changing propagator
        # it's s-channel. Otherwise check particle labels.
        prop = diagram.propagators[0]

        # If propagator spin matches a neutral heavy boson, likely s-channel
        if prop.spin == 1 or prop.spin is None:
            return Channel.S

        return Channel.S  # Default

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

    def _numerical_eval(self, diagram: Diagram, proc: ProcessType) -> str:
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
