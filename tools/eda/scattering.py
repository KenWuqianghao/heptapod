"""
# scattering.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Tree-level 2 -> 2 scattering: coverage, amplitude assembly, cross section.

WHY THIS MODULE EXISTS.  The 2->2 path used to consist of one hand-written
special case (all-fermion externals with a vector mediator, s- and
t-channel only) plus a fallback that emitted ``amp = I g^2 FAD[...]`` --
no spinors, no polarisation vectors, no vertex structure -- for every
other process.  That fallback did not raise; it produced a well-formed
script and a confident, meaningless number.  This module replaces it with
a compositional builder that covers the full space and refuses, loudly,
outside it.

THE SPACE IS CLOSED AND SMALL.  Enumerating over heptapod's own
``VALID_3PT_VERTICES`` / ``VALID_4PT_VERTICES`` gives 20 distinct external
spin classes for 2->2: 112 single-diagram (class, channel, mediator)
exchange structures plus 6 contact classes.  Those 118 topologies do NOT
need 118 code paths, because the case analysis factorises into small
independent tables:

    external wavefunction (spin 0 / 1/2 / 1, in|out, particle|anti)   3 cases
    vertex factor          reuse the existing library                 0 new
    propagator numerator   (1) / (q-slash + m) / (-g + q q / M^2)     3 cases
    denominator            1/(q^2 - M^2), q^2 in {s, t, u}            1 case
    index threading        bosonic mediator vs fermionic mediator     2 cases

CONVENTIONS (fixed here, asserted by the numeric harness):
  * Metric (+,-,-,-); FeynCalc default.
  * p1, p2 incoming; p3, p4 outgoing; all four on shell.
  * s = (p1+p2)^2, t = (p1-p3)^2, u = (p1-p4)^2, s + t + u = sum_i m_i^2.
    ``u`` is eliminated in favour of (s, t) EVERYWHERE, so the generated
    script has exactly two independent kinematic variables and the
    t-integration is well posed.
  * Vertex factors use the ALL-INCOMING momentum convention: a leg whose
    physical momentum flows out of the vertex enters as -p.
  * The assembled amplitude is normalised to 4 dimensions with
    ``ChangeDimension[amp, 4]`` before squaring.  Tree level never needs
    D dimensions, and mixing 4-dim spinors / polarisation vectors with
    D-dim Dirac algebra is precisely what FeynCalc rejects
    (``DiracTrace::mixmsg``).  Normalising once, centrally, lets the
    existing (D-dimensional) vertex library be reused verbatim.
  * Propagator denominators are PLAIN SCALARS ``1/(q^2 - M^2)``.  ``FAD``
    is a loop-integral denominator and carries D-4 pieces; it has no place
    in a tree amplitude.
  * sigma = (1/S) (1/N_init) C * Int |M|^2 / (16 pi lambda(s,m1^2,m2^2)) dt
    with S the identical-final-particle symmetry factor, N_init the
    initial-state spin/polarisation multiplicity, C the colour factor and
    lambda the Kallen function.
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum, auto
from itertools import product as _iproduct
from typing import Dict, List, Optional, Sequence, Set, Tuple

from tools.nda.simple_diagram import (
    Diagram,
    Particle,
    Propagator,
    Vertex,
    compute_symmetry_factor,
)
from tools.nda.lorentz_validation import VALID_3PT_VERTICES, VALID_4PT_VERTICES

from .fc_symbols import _coupling_value, _fmt_mma, _is_antiparticle, _mass_symbol


class Channel(Enum):
    """Scattering channel for 2->2 processes."""
    S = auto()
    T = auto()
    U = auto()
    CONTACT = auto()


#: Which external legs meet at each vertex, per channel.  Legs are indexed
#: 0..3 as (p1, p2, p3, p4) = (in, in, out, out).
CHANNEL_PAIRING: Dict[Channel, Tuple[Tuple[int, int], Tuple[int, int]]] = {
    Channel.S: ((0, 1), (2, 3)),
    Channel.T: ((0, 2), (1, 3)),
    Channel.U: ((0, 3), (1, 2)),
}

#: Momentum symbol per leg index.
LEG_MOMENTA = ("p1", "p2", "p3", "p4")

#: True when the leg's physical momentum flows into the diagram.
LEG_INCOMING = (True, True, False, False)

#: The Mandelstam invariant carried by the propagator in each channel.
CHANNEL_INVARIANT = {Channel.S: "s", Channel.T: "t", Channel.U: "uExpr"}

PROP_MASS = "mProp0"


class UnsupportedScattering(ValueError):
    """Raised when a requested 2->2 structure is outside the covered space.

    Deliberately an exception rather than a warning-plus-nonsense: a
    silently wrong amplitude is worse than a refusal.
    """


# ---------------------------------------------------------------------------
# Coverage
# ---------------------------------------------------------------------------

def _multiset(spins: Sequence[float]):
    return frozenset(Counter(float(s) for s in spins).items())


def is_valid_3pt(spins: Sequence[float]) -> bool:
    return _multiset(spins) in VALID_3PT_VERTICES


def is_valid_4pt(spins: Sequence[float]) -> bool:
    return _multiset(spins) in VALID_4PT_VERTICES


def allowed_exchange_structures() -> Set[Tuple[Tuple[float, ...], str, float]]:
    """Every (external spins, channel, mediator spin) with two valid vertices.

    External spins are ordered (p1, p2, p3, p4).  Returned for coverage
    reporting and to drive the parametrised tests.
    """
    out: Set[Tuple[Tuple[float, ...], str, float]] = set()
    spins = (0.0, 0.5, 1.0)
    for ext in _iproduct(spins, repeat=4):
        for chan, ((a, b), (c, d)) in CHANNEL_PAIRING.items():
            for med in spins:
                if is_valid_3pt([ext[a], ext[b], med]) and is_valid_3pt([ext[c], ext[d], med]):
                    out.add((ext, chan.name, med))
    return out


def allowed_contact_structures() -> Set[Tuple[float, ...]]:
    """Every external spin assignment admitting a valid 4-point vertex."""
    spins = (0.0, 0.5, 1.0)
    return {ext for ext in _iproduct(spins, repeat=4) if is_valid_4pt(ext)}


def external_spins(diagram: Diagram) -> Tuple[float, ...]:
    legs = list(diagram.initial) + list(diagram.final)
    return tuple(float(p.spin or 0.0) for p in legs)


def check_supported(diagram: Diagram, channel: Channel) -> None:
    """Raise :class:`UnsupportedScattering` if this structure is not covered."""
    ext = external_spins(diagram)
    if len(ext) != 4:
        raise UnsupportedScattering(
            f"2->2 needs exactly 4 external legs, got {len(ext)}."
        )

    if channel is Channel.CONTACT:
        if not is_valid_4pt(ext):
            raise UnsupportedScattering(
                f"External spins {ext} do not form a valid 4-point vertex. "
                f"Valid contact classes: SSSS, VVVV, FFFF, SSVV."
            )
        if _multiset(ext) == _multiset([1.0, 1.0, 1.0, 1.0]):
            raise UnsupportedScattering(
                "The VVVV quartic gauge vertex is not implemented: its colour "
                "structure is not expressible in heptapod's diagram spec, which "
                "carries a single scalar colour_factor. Supply the process as a "
                "sum of exchange diagrams instead."
            )
        return

    med = diagram.propagators[0].spin if diagram.propagators else None
    if med is None:
        raise UnsupportedScattering(
            "An exchange diagram needs a propagator with a declared spin."
        )
    (a, b), (c, d) = CHANNEL_PAIRING[channel]
    if not is_valid_3pt([ext[a], ext[b], med]):
        raise UnsupportedScattering(
            f"Vertex ({_spin_name(ext[a])}, {_spin_name(ext[b])}, "
            f"{_spin_name(med)}) is not a valid 3-point vertex, so the "
            f"{channel.name.lower()}-channel diagram does not exist."
        )
    if not is_valid_3pt([ext[c], ext[d], med]):
        raise UnsupportedScattering(
            f"Vertex ({_spin_name(ext[c])}, {_spin_name(ext[d])}, "
            f"{_spin_name(med)}) is not a valid 3-point vertex, so the "
            f"{channel.name.lower()}-channel diagram does not exist."
        )


def _spin_name(s: float) -> str:
    return {0.0: "S", 0.5: "F", 1.0: "V"}.get(float(s), f"spin-{s}")


# ---------------------------------------------------------------------------
# Legs
# ---------------------------------------------------------------------------

@dataclass
class VLeg:
    """One line attached to a vertex, with its all-incoming momentum."""
    particle: Optional[Particle]
    momentum: str            # bare physical momentum symbol, or "q"
    flows_in: bool           # True if the physical momentum flows into the vertex
    index: Optional[str]     # Lorentz index, for spin-1 lines
    spin: float
    is_mediator: bool = False
    leg_slot: Optional[int] = None   # 0..3 for external legs

    @property
    def p_in(self) -> str:
        """Momentum entering the vertex, as a Mathematica expression."""
        return self.momentum if self.flows_in else f"(-{self.momentum})"

    @property
    def mass(self) -> str:
        if self.is_mediator:
            return PROP_MASS
        return _mass_symbol(self.particle, self.leg_slot or 0)


def _external_legs(diagram: Diagram) -> List[VLeg]:
    parts = list(diagram.initial) + list(diagram.final)
    legs: List[VLeg] = []
    for i, p in enumerate(parts):
        spin = float(p.spin or 0.0)
        legs.append(
            VLeg(
                particle=p,
                momentum=LEG_MOMENTA[i],
                flows_in=LEG_INCOMING[i],
                index=f"mu{i + 1}" if spin == 1.0 else None,
                spin=spin,
                leg_slot=i,
            )
        )
    return legs


def _spinor_for(leg: VLeg) -> Tuple[str, bool]:
    """FeynCalc spinor for an external fermion leg, and whether it is barred.

    Incoming particle -> SpinorU, incoming antiparticle -> SpinorVBar,
    outgoing particle -> SpinorUBar, outgoing antiparticle -> SpinorV.
    Barred spinors sit at the LEFT end of a chain.
    """
    anti = _is_antiparticle(leg.particle.label if leg.particle else None)
    m = leg.mass
    if leg.flows_in:
        return (f"SpinorVBar[{leg.momentum}, {m}]", True) if anti else \
               (f"SpinorU[{leg.momentum}, {m}]", False)
    return (f"SpinorV[{leg.momentum}, {m}]", False) if anti else \
           (f"SpinorUBar[{leg.momentum}, {m}]", True)


# ---------------------------------------------------------------------------
# Vertex factors
# ---------------------------------------------------------------------------

@dataclass
class VertexExpr:
    """A vertex, split into its commuting part and its Dirac part.

    ``dirac`` is None for purely bosonic vertices; when present it must be
    placed inside a spinor chain rather than multiplied in.
    """
    prefactor: str = "1"
    dirac: Optional[str] = None


def _mom_sum(legs: Sequence[VLeg]) -> str:
    """All-incoming momentum sum over legs, e.g. 'p1 - p3'."""
    terms = [(leg.momentum if leg.flows_in else f"-{leg.momentum}") for leg in legs]
    out = " + ".join(terms).replace("+ -", "- ")
    return out


def _vtype(vertex: Optional[Vertex]) -> str:
    return (vertex.type.lower() if vertex else "").replace("-", "").replace("_", "")


def vertex_factor(gen, vertex: Optional[Vertex], legs: List[VLeg],
                  couplings: Dict[str, float]) -> VertexExpr:
    """Build the factor for one 3-point vertex from its three attached lines.

    Dispatch is on the multiset of spins, so a vertex is built the same way
    whether a given line is external or the mediator -- that uniformity is
    what makes the 118 topologies collapse onto six vertex types.
    """
    g = _coupling_value(vertex, couplings) if vertex else "g"
    vt = _vtype(vertex)
    spins = sorted(leg.spin for leg in legs)

    if spins == [0.0, 0.0, 0.0]:
        return VertexExpr(prefactor=f"I ({g})")

    if spins == [0.0, 0.0, 1.0]:
        # SSV: i g (pA - pB)^mu, both scalars incoming.  The A/B ordering
        # fixes an overall sign; it is taken in leg order (mediator last)
        # so repeated builds of the same diagram agree.
        scalars = [l for l in legs if l.spin == 0.0]
        vec = next(l for l in legs if l.spin == 1.0)
        a, b = scalars[0], scalars[1]
        return VertexExpr(
            prefactor=f"I ({g}) FVD[{a.p_in} - {b.p_in}, {vec.index}]"
        )

    if spins == [0.0, 1.0, 1.0]:
        # SVV: i g g^{mu nu} contracting the two vector lines.
        vecs = [l for l in legs if l.spin == 1.0]
        return VertexExpr(
            prefactor=f"I ({g}) MTD[{vecs[0].index}, {vecs[1].index}]"
        )

    if spins == [1.0, 1.0, 1.0]:
        # ------------------------------------------------------------------
        # UNRESOLVED CONVENTION -- see VVV_CONVENTION_NOTE at the bottom of
        # this module before trusting a VVV result. This builder uses the
        # textbook ALL-INCOMING momenta; heptapod's DECAY path
        # (feyncalc_codegen._amplitude_decay_no_prop) uses the physical
        # momenta as drawn. The two are NOT equal at finite masses.
        # ------------------------------------------------------------------
        # VVV triple gauge, all-incoming convention:
        #   g [ g^{m1 m2}(k1-k2)^{m3} + g^{m2 m3}(k2-k3)^{m1}
        #                             + g^{m3 m1}(k3-k1)^{m2} ]
        v1, v2, v3 = legs
        m1, m2, m3 = v1.index, v2.index, v3.index
        k1, k2, k3 = v1.p_in, v2.p_in, v3.p_in
        return VertexExpr(
            prefactor=(
                f"I ({g}) ("
                f"MTD[{m1}, {m2}] FVD[{k1} - {k2}, {m3}] + "
                f"MTD[{m2}, {m3}] FVD[{k2} - {k3}, {m1}] + "
                f"MTD[{m3}, {m1}] FVD[{k3} - {k1}, {m2}])"
            )
        )

    if spins == [0.0, 0.5, 0.5]:
        # SFF -- reuse the validated decay-side vertex library.
        return VertexExpr(dirac=gen._sff_coupling_structure(vt, g))

    if spins == [0.5, 0.5, 1.0]:
        # VFF -- likewise; the vector line supplies the Lorentz index and,
        # for tensor/dipole structures, its momentum.
        vec = next(l for l in legs if l.spin == 1.0)
        return VertexExpr(
            dirac=gen._vff_gamma_structure(vt, g, vec.index, vec_momentum=vec.momentum)
        )

    raise UnsupportedScattering(
        f"No vertex factor for spin configuration {spins}."
    )


# ---------------------------------------------------------------------------
# Propagator
# ---------------------------------------------------------------------------

def _is_massless(mass) -> bool:
    return isinstance(mass, (int, float)) and float(mass) == 0.0


def propagator_numerator(prop: Propagator, q_expr: str,
                         mu: str, nu: str) -> str:
    """Numerator of the tree propagator for spin 0, 1/2 or 1.

    The 1/2 numerator is returned for completeness but is threaded into the
    spinor chain by the caller, not multiplied in.
    """
    spin = float(prop.spin if prop.spin is not None else 0.0)
    if spin == 0.0:
        return "1"
    if spin == 0.5:
        return f"(GSD[{q_expr}] + {PROP_MASS})"
    if spin == 1.0:
        if _is_massless(prop.mass):
            return f"(-MTD[{mu}, {nu}])"
        return (
            f"(-MTD[{mu}, {nu}] + FVD[{q_expr}, {mu}] FVD[{q_expr}, {nu}]"
            f"/{PROP_MASS}^2)"
        )
    raise UnsupportedScattering(
        f"No tree propagator for mediator spin {spin}."
    )


def propagator_denominator(prop: Propagator, channel: Channel) -> str:
    """i / (q^2 - M^2), with q^2 the channel invariant.

    The explicit ``I`` matters only once amplitudes are SUMMED: every
    propagator carries it, so the relative phase between two exchange
    diagrams survives either way, but between a contact diagram (no
    propagator) and an exchange diagram it does not. Carrying it here keeps
    the amplitude absolutely normalised, which is what a coherent sum needs.
    It has no effect on a single diagram, where |i| = 1.
    """
    inv = CHANNEL_INVARIANT[channel]
    if _is_massless(prop.mass):
        return f"I/({inv})"
    return f"I/({inv} - {PROP_MASS}^2)"


# ---------------------------------------------------------------------------
# Amplitude assembly
# ---------------------------------------------------------------------------

def _pol_factors(legs: Sequence[VLeg]) -> str:
    return " ".join(
        f"PolarizationVector[{l.momentum}, {l.index}]"
        for l in legs if l.spin == 1.0
    )


def _chain(bar: str, dirac: str, nonbar: str) -> str:
    return f"{bar} . ({dirac}) . {nonbar}"


def _split_fermion_pair(pair: Sequence[VLeg]) -> Tuple[str, str]:
    """Return (barred spinor, unbarred spinor) for a two-fermion vertex."""
    exprs = [(_spinor_for(l)) for l in pair]
    barred = [e for e, b in exprs if b]
    unbarred = [e for e, b in exprs if not b]
    if len(barred) != 1 or len(unbarred) != 1:
        raise UnsupportedScattering(
            "A fermion bilinear needs exactly one barred and one unbarred "
            "spinor; got labels "
            f"{[l.particle.label if l.particle else '?' for l in pair]}. "
            "Check the particle/antiparticle labelling (a 'bar'/'~'/'+' "
            "suffix marks an antiparticle)."
        )
    return barred[0], unbarred[0]


def _vertex_expr(gen, vertex, legs_at_vertex, couplings) -> str:
    """One vertex as a single multiplicative expression.

    A vertex carrying two external fermions becomes a closed spinor chain;
    everything else is a commuting factor.
    """
    vf = vertex_factor(gen, vertex, legs_at_vertex, couplings)
    if vf.dirac is None:
        return vf.prefactor
    fermions = [l for l in legs_at_vertex if l.spin == 0.5 and not l.is_mediator]
    if len(fermions) != 2:
        raise UnsupportedScattering(
            "Internal error: a Dirac vertex structure reached a vertex with "
            f"{len(fermions)} external fermions."
        )
    bar, nonbar = _split_fermion_pair(fermions)
    return _chain(bar, vf.dirac, nonbar)


def _exchange_bosonic(gen, diagram: Diagram, legs: List[VLeg],
                      channel: Channel, prop: Propagator,
                      amp_var: str = "amp", q_var: str = "qMom") -> List[str]:
    (a, b), (c, d) = CHANNEL_PAIRING[channel]
    A_ext, B_ext = [legs[a], legs[b]], [legs[c], legs[d]]
    med_spin = float(prop.spin if prop.spin is not None else 0.0)

    q_expr = _mom_sum(A_ext)
    # The mediator leaves vertex A and enters vertex B.
    medA = VLeg(None, q_var, flows_in=False,
                index="muP" if med_spin == 1.0 else None,
                spin=med_spin, is_mediator=True)
    medB = VLeg(None, q_var, flows_in=True,
                index="nuP" if med_spin == 1.0 else None,
                spin=med_spin, is_mediator=True)

    v0 = diagram.vertices[0] if diagram.vertices else None
    v1 = diagram.vertices[1] if len(diagram.vertices) >= 2 else v0

    exprA = _vertex_expr(gen, v0, A_ext + [medA], diagram.couplings)
    exprB = _vertex_expr(gen, v1, B_ext + [medB], diagram.couplings)
    num = propagator_numerator(prop, q_var, "muP", "nuP")
    den = propagator_denominator(prop, channel)
    pol = _pol_factors(legs)

    parts = [f"({exprA})", f"({num})", f"({exprB})", f"({den})"]
    if pol:
        parts.append(pol)
    return [f"{q_var} = {q_expr};",
            f"{amp_var} = " + " ".join(parts) + ";"]


def _exchange_fermionic(gen, diagram: Diagram, legs: List[VLeg],
                        channel: Channel, prop: Propagator,
                        amp_var: str = "amp", q_var: str = "qMom") -> List[str]:
    """Mediator is a fermion: the propagator sits INSIDE the spinor chain."""
    (a, b), (c, d) = CHANNEL_PAIRING[channel]
    A_ext, B_ext = [legs[a], legs[b]], [legs[c], legs[d]]

    def _split(pair):
        f = [l for l in pair if l.spin == 0.5]
        boson = [l for l in pair if l.spin != 0.5]
        if len(f) != 1 or len(boson) != 1:
            raise UnsupportedScattering(
                "A fermion-mediated vertex needs exactly one external fermion "
                "and one external boson."
            )
        return f[0], boson[0]

    fA, _ = _split(A_ext)
    fB, _ = _split(B_ext)
    sA, barA = _spinor_for(fA)
    sB, barB = _spinor_for(fB)
    if barA == barB:
        raise UnsupportedScattering(
            "The two external fermions must sit at opposite ends of the "
            "fermion line (one barred, one unbarred). Got "
            f"{fA.particle.label!r} and {fB.particle.label!r}; check the "
            "particle/antiparticle labelling."
        )

    v0 = diagram.vertices[0] if diagram.vertices else None
    v1 = diagram.vertices[1] if len(diagram.vertices) >= 2 else v0

    # The barred spinor sits at the LEFT end; momentum flows along the arrow
    # from the right vertex to the left one.
    if barA:
        left_ext, left_v, left_spinor = A_ext, v0, sA
        right_ext, right_v, right_spinor = B_ext, v1, sB
    else:
        left_ext, left_v, left_spinor = B_ext, v1, sB
        right_ext, right_v, right_spinor = A_ext, v0, sA

    q_expr = _mom_sum(right_ext)
    medR = VLeg(None, q_var, flows_in=False, index=None, spin=0.5, is_mediator=True)
    medL = VLeg(None, q_var, flows_in=True, index=None, spin=0.5, is_mediator=True)

    vfL = vertex_factor(gen, left_v, left_ext + [medL], diagram.couplings)
    vfR = vertex_factor(gen, right_v, right_ext + [medR], diagram.couplings)
    if vfL.dirac is None or vfR.dirac is None:
        raise UnsupportedScattering(
            "A fermion-mediated diagram needs a Dirac structure at both "
            "vertices."
        )

    num = f"(GSD[{q_var}] + {PROP_MASS})"
    den = propagator_denominator(prop, channel)
    pol = _pol_factors(legs)

    chain = (
        f"{left_spinor} . ({vfL.dirac}) . {num} . ({vfR.dirac}) . {right_spinor}"
    )
    parts = [f"({chain})", f"({den})"]
    if pol:
        parts.append(pol)
    return [f"{q_var} = {q_expr};",
            f"{amp_var} = " + " ".join(parts) + ";"]


def _contact_amplitude(gen, diagram: Diagram, legs: List[VLeg],
                       amp_var: str = "amp") -> List[str]:
    vertex = diagram.vertices[0] if diagram.vertices else None
    g = _coupling_value(vertex, diagram.couplings) if vertex else "g"
    vt = _vtype(vertex)
    ms = _multiset(external_spins(diagram))

    if ms == _multiset([0.0, 0.0, 0.0, 0.0]):
        return [f"{amp_var} = I ({g});"]

    if ms == _multiset([0.0, 0.0, 1.0, 1.0]):
        vecs = [l for l in legs if l.spin == 1.0]
        pol = _pol_factors(legs)
        return [
            f"{amp_var} = I ({g}) MTD[{vecs[0].index}, {vecs[1].index}] {pol};"
        ]

    if ms == _multiset([0.5, 0.5, 0.5, 0.5]):
        # Four-fermion contact operator.  The pairing (p1 p2)(p3 p4) is the
        # operator's own definition, not something the tool can infer.
        bar1, non1 = _split_fermion_pair([legs[0], legs[1]])
        bar2, non2 = _split_fermion_pair([legs[2], legs[3]])
        if vt in ("", "vector", "gaugevector", "currentcurrent"):
            s1, s2 = "GAD[muC]", "GAD[muC]"
        elif vt in ("scalar", "yukawa"):
            s1, s2 = "1", "1"
        elif vt in ("lefthanded", "va", "vectoraxial", "chiral"):
            s1, s2 = "GAD[muC].GA[7]", "GAD[muC].GA[7]"
        else:
            raise UnsupportedScattering(
                f"Unknown 4-fermion contact structure {vertex.type!r}. "
                "Supported: vector, scalar, left-handed."
            )
        return [
            f"{amp_var} = I ({g}) ({bar1} . ({s1}) . {non1}) "
            f"({bar2} . ({s2}) . {non2});"
        ]

    raise UnsupportedScattering(
        f"No contact amplitude for external spins {external_spins(diagram)}."
    )


def build_amplitude(gen, diagram: Diagram, channel: Channel,
                    amp_var: str = "amp", q_var: str = "qMom",
                    normalise_dimension: bool = True) -> str:
    """Emit the ``amp = ...`` section for one 2->2 tree diagram.

    Raises :class:`UnsupportedScattering` rather than emitting a
    structurally empty amplitude.

    ``amp_var`` / ``q_var`` let a caller build several diagrams into
    distinct variables; :func:`build_amplitude_sum` uses that to add them
    coherently. ``normalise_dimension=False`` defers the
    ``ChangeDimension`` to the caller, which is what a sum wants: the
    normalisation is applied ONCE, to the total.
    """
    check_supported(diagram, channel)
    legs = _external_legs(diagram)

    labels_i = " ".join(p.label or "?" for p in diagram.initial)
    labels_f = " ".join(p.label or "?" for p in diagram.final)
    head = [
        f"(* Step 1: Amplitude for {labels_i} -> {labels_f} "
        f"({channel.name.lower()}-channel) *)"
    ]

    if channel is Channel.CONTACT:
        body = _contact_amplitude(gen, diagram, legs, amp_var=amp_var)
    else:
        prop = diagram.propagators[0]
        med_spin = float(prop.spin if prop.spin is not None else 0.0)
        if med_spin == 0.5:
            body = _exchange_fermionic(gen, diagram, legs, channel, prop,
                                       amp_var=amp_var, q_var=q_var)
        else:
            body = _exchange_bosonic(gen, diagram, legs, channel, prop,
                                     amp_var=amp_var, q_var=q_var)

    tail = []
    if normalise_dimension:
        tail = [
            "(* Tree level lives in 4 dimensions; normalising here lets the "
            "D-dimensional *)",
            "(* vertex library be reused without tripping DiracTrace::mixmsg. *)",
            f"{amp_var} = ChangeDimension[{amp_var}, 4];",
        ]
    return "\n".join(head + body + tail) + "\n"


def build_amplitude_sum(gen, diagrams: Sequence[Tuple[Diagram, Channel]],
                        relative_signs: Optional[Sequence[int]] = None) -> str:
    """Emit several diagrams and add their amplitudes COHERENTLY.

    Most real 2->2 processes are a sum: phi phi -> phi phi with a cubic
    coupling is s + t + u; identical-fermion scattering is s + t. A tool
    that only ever emits one diagram is silently wrong whenever more than
    one contributes, which is why this exists.

    WHAT THIS DOES NOT DO. It cannot work out WHICH diagrams contribute --
    that needs a Lagrangian, and heptapod's diagram spec deliberately
    carries topology rather than a model. The caller supplies the list.

    ``relative_signs`` carries the (-1) between diagrams related by
    interchange of two external fermion lines. It defaults to all +1, which
    is correct only when no such interchange relates them; pass it
    explicitly for identical-fermion final states.

    All diagrams must share external legs and masses, since they are added
    before squaring; that is checked here rather than left to produce a
    meaningless sum.
    """
    if not diagrams:
        raise UnsupportedScattering("build_amplitude_sum needs at least one diagram.")
    signs = list(relative_signs) if relative_signs is not None else [1] * len(diagrams)
    if len(signs) != len(diagrams):
        raise UnsupportedScattering(
            f"relative_signs has {len(signs)} entries for {len(diagrams)} diagrams."
        )

    ref_spins = external_spins(diagrams[0][0])
    ref_masses = _leg_masses(diagrams[0][0])
    for d, _ in diagrams[1:]:
        if external_spins(d) != ref_spins or _leg_masses(d) != ref_masses:
            raise UnsupportedScattering(
                "All diagrams in a coherent sum must share the same external "
                "legs and masses; got "
                f"{ref_spins}/{ref_masses} and {external_spins(d)}/{_leg_masses(d)}."
            )

    sections: List[str] = []
    terms: List[str] = []
    for i, (d, ch) in enumerate(diagrams, start=1):
        sections.append(
            build_amplitude(gen, d, ch, amp_var=f"amp{i}", q_var=f"qMom{i}",
                            normalise_dimension=False)
        )
        terms.append(("- " if signs[i - 1] < 0 else "+ ") + f"amp{i}")
    total = " ".join(terms).lstrip("+ ").strip()
    sections.append(
        "(* Coherent sum of the diagrams above, normalised to 4 dimensions "
        "ONCE. *)\n"
        f"amp = ChangeDimension[{total}, 4];\n"
    )
    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Kinematics and the cross section
# ---------------------------------------------------------------------------

def _leg_masses(diagram: Diagram) -> List[str]:
    parts = list(diagram.initial) + list(diagram.final)
    return [_mass_symbol(p, i) for i, p in enumerate(parts)]


def kinematics_block(diagram: Diagram) -> str:
    """Scalar products in terms of (s, t), with u eliminated on shell.

    Mirrors the decay path's proven idiom (explicit ``ScalarProduct``
    assignments) rather than ``SetMandelstam``: it leaves exactly two
    independent variables, which is what makes the t-integration well
    posed and stops a symbolic ``u`` surviving into the final answer.
    """
    m1, m2, m3, m4 = _leg_masses(diagram)
    lines = [
        "(* Step 2: Kinematics — two independent invariants (s, t). *)",
        "(* u is eliminated on shell: s + t + u = sum_i m_i^2. *)",
        f"uExpr = {m1}^2 + {m2}^2 + {m3}^2 + {m4}^2 - s - t;",
        "FCClearScalarProducts[];",
        f"ScalarProduct[p1, p1] = {m1}^2;",
        f"ScalarProduct[p2, p2] = {m2}^2;",
        f"ScalarProduct[p3, p3] = {m3}^2;",
        f"ScalarProduct[p4, p4] = {m4}^2;",
        f"ScalarProduct[p1, p2] = (s - {m1}^2 - {m2}^2)/2;",
        f"ScalarProduct[p3, p4] = (s - {m3}^2 - {m4}^2)/2;",
        f"ScalarProduct[p1, p3] = ({m1}^2 + {m3}^2 - t)/2;",
        f"ScalarProduct[p2, p4] = ({m2}^2 + {m4}^2 - t)/2;",
        f"ScalarProduct[p1, p4] = ({m1}^2 + {m4}^2 - uExpr)/2;",
        f"ScalarProduct[p2, p3] = ({m2}^2 + {m3}^2 - uExpr)/2;",
    ]
    return "\n".join(lines) + "\n"


def initial_state_multiplicity(diagram: Diagram) -> int:
    """N_init = product of (2s+1), with 2 for a massless vector.

    The old code used (2s+1) unconditionally, which over-counts a massless
    vector's polarisations by 3/2.
    """
    n = 1
    for p in diagram.initial:
        spin = float(p.spin or 0.0)
        if spin == 1.0 and _is_massless(p.mass):
            n *= 2
        else:
            n *= int(round(2 * spin + 1))
    return n


def cross_section_block(diagram: Diagram) -> str:
    """The 2->2 master formula, symbolic in s.

    sigma = (1/S)(1/N_init) C Int dt |M|^2 / (16 pi lambda(s, m1^2, m2^2))

    Every factor the old implementation dropped is explicit here: the
    identical-particle symmetry factor S (absent entirely, which made
    phi phi -> phi phi come out exactly a factor 2 high), the massless-vector
    polarisation count in N_init, and a genuinely symbolic s (the old code
    mixed a numeric sqrt_s into the prefactor while |M|^2 still carried a
    symbolic s, so the two never met).
    """
    m1, m2, m3, m4 = _leg_masses(diagram)
    n_init = initial_state_multiplicity(diagram)
    sym = compute_symmetry_factor(diagram)
    lines = [
        "(* Step 6: Total cross section *)",
        "kallen[a_, b_, c_] := a^2 + b^2 + c^2 - 2 a b - 2 a c - 2 b c;",
        f"lam12 = kallen[s, {m1}^2, {m2}^2];   (* initial-state Kallen *)",
        f"lam34 = kallen[s, {m3}^2, {m4}^2];   (* final-state Kallen *)",
        "",
        "(* t range at cos(theta) = -+1 *)",
        f"tMid = {m1}^2 + {m3}^2 - (s + {m1}^2 - {m2}^2) (s + {m3}^2 - {m4}^2)/(2 s);",
        "tHalf = Sqrt[lam12 lam34]/(2 s);",
        "tMin = tMid - tHalf;",
        "tMax = tMid + tHalf;",
        "",
        f"nInit = {n_init};            (* initial spin/polarisation average *)",
        f"symmetryFactor = {sym};      (* identical final-state particles *)",
        f"colorFactor = {_fmt_mma(diagram.color_factor)};",
        "",
        "(* dsigma/dt = |M|^2 / (16 pi lambda(s, m1^2, m2^2)) *)",
        "dSigmaDt = ampSqKin colorFactor/(16 Pi lam12 nInit symmetryFactor);",
        "sigma = Integrate[dSigmaDt, {t, tMin, tMax}];",
        "sigma = sigma // Simplify;",
        "",
        "(* Symbolic integration is not guaranteed to close: a coherent sum of",
        "   several diagrams gives a rational integrand whose antiderivative can",
        "   come back Undefined or unevaluated even though the integral is",
        "   perfectly finite. Say so rather than letting a bad symbol propagate,",
        "   and provide the numeric route. *)",
        "If[!FreeQ[sigma, Integrate],",
        "  Print[\"WARNING: the symbolic t-integration did not close. \" <>",
        "        \"Use sigmaNIntegrate[rules] for a number.\"]];",
        "",
        "(* Numeric fallback. The symbolic antiderivative can be well formed and",
        "   STILL evaluate to Undefined at a parameter point, when the endpoints",
        "   cancel -- so this is the reliable numeric route, not just a rescue",
        "   for an unevaluated Integrate. Substitutes values FIRST, then",
        "   integrates:  sigmaNIntegrate[{mphi -> 60., mProp0 -> 300., g -> 55.,",
        "                                 s -> 700.^2}]  *)",
        "sigmaNIntegrate[rules_] := Module[{fInt, tLo, tHi},",
        "  fInt = N[dSigmaDt /. rules];",
        "  tLo = N[tMin /. rules]; tHi = N[tMax /. rules];",
        "  NIntegrate[fInt, {t, tLo, tHi}]];",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# VVV_CONVENTION_NOTE
# ---------------------------------------------------------------------------
# The triple-gauge vertex is written in this module with ALL MOMENTA INCOMING,
# the textbook statement (Peskin & Schroeder ch. 16):
#
#     V^{m1 m2 m3}(k1,k2,k3) = g[ eta^{m1 m2}(k1-k2)^{m3}
#                               + eta^{m2 m3}(k2-k3)^{m1}
#                               + eta^{m3 m1}(k3-k1)^{m2} ],   k1+k2+k3 = 0.
#
# heptapod's DECAY path writes the same functional form but evaluates it at the
# PHYSICAL momenta as drawn -- parent P incoming, daughters q1, q2 outgoing:
#
#     g[ eta^{mu nu}(P-q1)^rho + eta^{nu rho}(q1-q2)^mu + eta^{rho mu}(q2-P)^nu ]
#
# Those momenta satisfy P - q1 - q2 = 0, not P + q1 + q2 = 0, so this is the
# standard form evaluated off its defining constraint. The two are NOT
# equivalent. Measured on hepbench's decay_V_to_VVp part (a)
# (g=0.8, mV=900, m1=200, m2=250 GeV):
#
#     as-drawn (decay path)   128.5515157524 GeV
#     all-incoming (here)     374.5880874852 GeV      ratio 2.9139
#
# What is settled:
#   * BOTH forms are totally antisymmetric in their (index, momentum) pairs,
#     as f^{abc} requires.
#   * BOTH converge to the standard longitudinal asymptotics
#     Gamma -> g^2 mV^5 / (192 pi m^4) for mV >> m (measured: 0.00520832 and
#     0.00520835 against 1/192 = 0.00520833), so that limit does not
#     discriminate. They differ only in the subleading terms -- which is
#     exactly where the benchmark parameter points sit (mV/m ~ 4).
#   * On shell the as-drawn form COLLAPSES to a single structure,
#     g (eps1.eps2)((q1-q2).eps0), because its other two terms are
#     proportional to q2.eps2 and q1.eps1. The all-incoming form keeps three.
#
# What is NOT settled: which one hepbench's decay_V_to_VVp ground truth SHOULD
# encode. Its derivation.py uses the as-drawn form and validates it by two
# contractions OF THAT SAME EXPRESSION (explicit polarisation vectors vs a
# completeness-tensor einsum), which checks the contraction algebra, not the
# vertex definition -- so agreement between heptapod's decay path and that
# truth is circular and does not anchor the convention to the literature.
#
# Nothing here is changed unilaterally: decay_V_to_VVp grading and heptapod's
# shipped decay behaviour both depend on the answer. test_scattering.py has a
# test that DETECTS the mismatch so it cannot be quietly forgotten.
