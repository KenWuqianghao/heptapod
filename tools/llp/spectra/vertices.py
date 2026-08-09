"""
# vertices.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

THE MODEL. Everything model-dependent about an LLP production spectrum lives in
this file: the spin-summed squared amplitude for radiating the LLP off a
charged-lepton leg, with the overall coupling factored out.

EXTENDING TO A NEW INTERACTION
------------------------------
Add one function with the signature

    msq(P, p_l, p_nu, p_phi, m_l, m_phi) -> array

returning the spin-summed |M|^2 at unit coupling, and register it in
`VERTICES`. Nothing else moves: `kinematics.py` (phase space, quadrature) and
`production_spectrum.py` (parents, I/O, provenance) are model-independent by
construction. The natural next entries are a pseudoscalar coupling
(gamma_5 at the emission vertex), a vector coupling (gamma^mu), and an
axial-vector coupling (gamma^mu gamma_5).

Only the SCALAR vertex for PSEUDOSCALAR parents is implemented and validated
here. An unvalidated amplitude is worse than a missing one, so the others are
left to be added alongside their own cross-checks rather than stubbed out
speculatively.

THE VECTOR PARENT GAP is the known one, and it is worth stating what "adding
it" requires. V -> l+ l- phi has two diagrams (the LLP radiated off either
lepton leg) which interfere, and the polarisation sum must be averaged over the
parent's three states. Validating it therefore needs more than agreement with
another implementation of the same formula: it needs the Ward identity to hold
numerically, and it needs the rate to reproduce the MEASURED V -> l+ l- partial
width when the LLP-emission vertex is removed. Both checks are physics, not
self-consistency, and both should be in the test suite before the vertex is
advertised as available. Until then ProductionSpectrumTool rejects vector
parents with a pointer to the workaround: MesonDecayToLLP is model-agnostic and
accepts a hand-supplied (x, pdf) table plus B_hat, so a vector channel costs
the caller one spectrum, not a change to the chain.

PHYSICS
-------
The LLP is radiated from an internal, off-shell charged lepton of momentum
q = p_l + p_phi, propagator

    S_F(q) = i (qslash + m_l) / (q^2 - m_l^2),
    q^2 - m_l^2 = m_phi^2 + 2 p_l . p_phi,

so the amplitude carries 1/D with D = 2 p_l.p_phi + m_phi^2. Squaring and
summing over spins gives a ratio of Dirac traces; the epsilon (gamma_5) terms
vanish for three independent momenta, so the closed form below is exact.

Amplitude structure follows Carlson & Rislow, Phys. Rev. D 86, 035013 (2012)
[arXiv:1206.3587]; its application to forward LLP production is set out in
Mammen Abraham & Fieg [arXiv:2501.09071]. The vector-parent amplitude, when
added, should follow Mitra & Sahoo, Phys. Rev. D 104, 015002 (2021)
[arXiv:2103.08284], including its Ward-identity check.
"""
from __future__ import annotations

import numpy as np

from .kinematics import mdot


def _tr4(ab, cd, ac, bd, ad, bc):
    """Tr[a/ b/ c/ d/] / 4 from the standard contraction identity."""
    return ab * cd - ac * bd + ad * bc


def msq_scalar_pseudoscalar_parent(P, p_l, p_nu, p_phi, m_l, m_phi):
    """Spin-summed |M|^2 for P -> l nu phi with a SCALAR L = -g phi lbar l.

    Unit coupling: the physical rate carries C_P^2 g^2 on top, with
    C_P = (G_F |V_P| f_P / sqrt(2)) supplied by the caller.

    Evaluated from the trace closed form

      T = 2 { Tr[l/_1 l/ P/ p/_2 P/ l/]
              + m^2 Tr[P/ p/_2 P/ l/]
              + m^2 Tr[l/_1 P/ p/_2 P/]
              + m^2 Tr[l/ P/ p/_2 P/] } / D^2,

    with l = p_l + p_phi the off-shell lepton momentum and
    D = 2 p_l.p_phi + m_phi^2 the propagator denominator. Vectorised over any
    leading grid shape.
    """
    ell = p_l + p_phi
    v = {"l1": p_l, "p2": p_nu, "P": P, "l": ell}
    keys = list(v)
    d = {(a, b): mdot(v[a], v[b]) for a in keys for b in keys}

    def t4(a, b, c, e):
        return _tr4(d[a, b], d[c, e], d[a, c], d[b, e], d[a, e], d[b, c])

    def t6(a, b, c, e, f, g):
        return (d[a, b] * t4(c, e, f, g)
                - d[a, c] * t4(b, e, f, g)
                + d[a, e] * t4(b, c, f, g)
                - d[a, f] * t4(b, c, e, g)
                + d[a, g] * t4(b, c, e, f))

    m2 = m_l * m_l
    T = 2.0 * 4.0 * (t6("l1", "l", "P", "p2", "P", "l")
                     + m2 * t4("P", "p2", "P", "l")
                     + m2 * t4("l1", "P", "p2", "P")
                     + m2 * t4("l", "P", "p2", "P"))
    D = 2.0 * mdot(p_l, p_phi) + m_phi * m_phi
    return T / (D * D)


# Registry: (family, interaction) -> squared amplitude at unit coupling.
VERTICES = {
    ("pseudoscalar", "scalar"): msq_scalar_pseudoscalar_parent,
}

#: Interactions available per parent family, for error messages and discovery.
AVAILABLE = {
    "pseudoscalar": sorted(i for (f, i) in VERTICES if f == "pseudoscalar"),
    "vector": sorted(i for (f, i) in VERTICES if f == "vector"),
}


def get(family, interaction):
    """Look up a squared amplitude, with an actionable error if absent."""
    try:
        return VERTICES[(family, interaction)]
    except KeyError:
        have = AVAILABLE.get(family, [])
        raise KeyError(
            f"no {interaction!r} vertex for a {family} parent; "
            f"implemented: {have or 'none'}. Add one function to "
            f"spectra/vertices.py and register it in VERTICES -- the "
            f"kinematics and the tool shell are model-independent.")
