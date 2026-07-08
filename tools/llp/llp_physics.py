"""
# llp_physics.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
"""
Shared physics for the `llp` bundle: analytic parent-flux kernels, the
tree-level 3-body production density for M -> mu nu phi, decay-volume
geometry, and the boost / decay-probability conventions used by
LLPFluxFromMesonDecayTool and DecayInVolumeTool.

The bundle is setting-agnostic by construction: the collider-forward vs
beam-dump choice lives entirely in the kernel YAML (parent mass, momentum
and angular scales, per-interaction normalization) and the geometry YAML.
Nothing in this module hard-codes a parent mass, a beam energy, or a
detector location.

Conventions (declared, and mirrored from the validated reference):
  - Kernels parametrize d^2 N_M / (dp dtheta) per primary interaction for
    *decaying* parents only (the decay-before-absorption fraction is folded
    into n_per_int by whoever pins the kernel).
  - Event weights are g^2-stripped: w_i = n_per_int * kappa_M / n_samples,
    so N_sig(g) = N_int * g^2 * sum_i w_i * P_dec,i(g) * acc_i.
  - The LLP travels in a straight line from the primary vertex at its lab
    angle; the parent flight length is absorbed into the kernel.
  - P_dec = exp(-L1/lam) - exp(-L2/lam), lam = beta*gamma*ctau,
    ctau = hbar*c / (g^2 * width_ref).
  - Two-track acceptance is evaluated at the MIDPOINT of the in-volume
    segment (g-independent, preserving exact coupling reweighting).

Attribution: the trace-form matrix element (msq_trace and helpers), the
(x, c) kinematics (momenta_from_x_c, jacobian_x_c, x_domain,
d2gamma_dx_dc, sample_x), the kernel and geometry loaders, and the
rest-frame -> lab boost formula are adapted from the HEPbench reference
ground-truth implementation, benchmarks/llp_forward/_shared/
{kernels, production, pipeline}.py (HEPbench authors, GPL v3+), which
these tools deliberately mirror convention-for-convention.
"""

import math

import numpy as np
import yaml

# hbar*c in GeV*m — the single constant tying the g^2-stripped reference
# width to a lab-frame decay length.
HBARC_M_GEV = 1.973269804e-16


def mdot(p, q):
    """Minkowski dot product of contravariant 4-vectors [E, px, py, pz]."""
    return p[0] * q[0] - p[1] * q[1] - p[2] * q[2] - p[3] * q[3]


# ---------------------------------------------------------------------------
# analytic parent-flux kernels
# (adapted from hepbench benchmarks/llp_forward/_shared/kernels.py)
# ---------------------------------------------------------------------------
class AnalyticKernel:
    """A closed-form parent-flux kernel loaded from a YAML spec.

    Form `pexp_texp` (the only supported form):

        d^2N/(dp dtheta) = n_per_int
            * p^a exp(-p/p0) / (Gamma(a+1) p0^(a+1))     [momentum factor]
            * (theta/theta0^2) exp(-theta/theta0)        [angular factor]

    Both factors are unit-normalized on (0, inf), so n_per_int is the mean
    number of decaying parents per primary interaction. Sampling is exact:
    p ~ Gamma(a+1, p0), theta ~ Gamma(2, theta0), azimuth uniform.

    The YAML must carry (optionally nested under a top-level `kernel:` key):
    name, parent, parent_mass_gev, form: pexp_texp, and
    params: {n_per_int, p0_gev, a, theta0_rad}.
    """

    REQUIRED = ("name", "parent", "parent_mass_gev", "form", "params")

    def __init__(self, spec):
        for key in self.REQUIRED:
            if key not in spec:
                raise ValueError(f"kernel spec missing '{key}'")
        if spec["form"] != "pexp_texp":
            raise ValueError(f"unknown kernel form '{spec['form']}'")
        self.spec = spec
        self.name = spec["name"]
        self.parent = spec["parent"]
        self.parent_mass = float(spec["parent_mass_gev"])
        p = spec["params"]
        self.n_per_int = float(p["n_per_int"])
        self.p0 = float(p["p0_gev"])
        self.a = float(p["a"])
        self.theta0 = float(p["theta0_rad"])

    @classmethod
    def from_yaml(cls, path):
        with open(path) as fh:
            doc = yaml.safe_load(fh)
        if not isinstance(doc, dict):
            raise ValueError("kernel YAML must be a mapping")
        return cls(doc["kernel"] if "kernel" in doc else doc)

    def density(self, p, theta):
        """d^2N/(dp dtheta) per primary interaction."""
        p = np.asarray(p, dtype=float)
        theta = np.asarray(theta, dtype=float)
        fp = p ** self.a * np.exp(-p / self.p0) \
            / (math.gamma(self.a + 1.0) * self.p0 ** (self.a + 1.0))
        ft = theta / self.theta0 ** 2 * np.exp(-theta / self.theta0)
        return self.n_per_int * fp * ft

    def sample(self, n, rng):
        """Exact draws of (p, theta, azimuth) from the kernel shape."""
        p = rng.gamma(shape=self.a + 1.0, scale=self.p0, size=n)
        theta = rng.gamma(shape=2.0, scale=self.theta0, size=n)
        phi_az = rng.uniform(0.0, 2.0 * np.pi, size=n)
        return p, theta, phi_az


# ---------------------------------------------------------------------------
# production density for M(P) -> mu(p1) nu(p2) phi(p3), g^2-/C^2-stripped
# (adapted from hepbench benchmarks/llp_forward/_shared/production.py)
# ---------------------------------------------------------------------------
def _tr4(a, b, c, d, dots):
    """Tr[slash(a) slash(b) slash(c) slash(d)] / 4."""
    return dots[a, b] * dots[c, d] - dots[a, c] * dots[b, d] \
        + dots[a, d] * dots[b, c]


def _tr6(a, b, c, d, e, f, dots):
    """Tr[slash(a)...slash(f)] / 4 by the standard recursion."""
    return (dots[a, b] * _tr4(c, d, e, f, dots)
            - dots[a, c] * _tr4(b, d, e, f, dots)
            + dots[a, d] * _tr4(b, c, e, f, dots)
            - dots[a, e] * _tr4(b, c, d, f, dots)
            + dots[a, f] * _tr4(b, c, d, e, dots))


def msq_trace(P, p1, p2, p3, m_mu, m_phi):
    """Spin-summed |A|^2 at g = C = 1 for M -> mu nu phi (scalar radiated
    off the muon leg), from the closed-form trace recursion.

    T = 2 { Tr[slash(p1) slash(l) slash(P) slash(p2) slash(P) slash(l)]
            + m^2 Tr[slash(P)  slash(p2) slash(P) slash(l)]
            + m^2 Tr[slash(p1) slash(P)  slash(p2) slash(P)]
            + m^2 Tr[slash(l)  slash(P)  slash(p2) slash(P)] },

    with l = p1 + p3 and epsilon terms vanishing for three independent
    momenta. Divide by D^2 with D = 2 p1.p3 + m_phi^2 (the muon
    propagator). Validated against explicit Dirac spinors in the
    reference implementation."""
    l = p1 + p3
    vecs = {"p1": p1, "p2": p2, "P": P, "l": l}
    names = list(vecs)
    dots = {}
    for i in names:
        for j in names:
            dots[i, j] = mdot(vecs[i], vecs[j])
    m2 = m_mu * m_mu
    T = 2.0 * 4.0 * (
        _tr6("p1", "l", "P", "p2", "P", "l", dots)
        + m2 * _tr4("P", "p2", "P", "l", dots)
        + m2 * _tr4("p1", "P", "p2", "P", dots)
        + m2 * _tr4("l", "P", "p2", "P", dots)
    )
    D = 2.0 * mdot(p1, p3) + m_phi * m_phi
    return T / (D * D)


def momenta_from_x_c(mM, m_mu, m_phi, x, c):
    """Parent-rest-frame momenta (P, p1, p2, p3) at (x, cos(theta*)).

    x = 2 E_phi / mM; theta_star is the muon helicity angle in the
    (mu nu) rest frame measured from the (mu nu) direction of flight
    (i.e. from -p_phi). phi is placed along -z, the (mu nu) system
    along +z, and the muon decayed in the x-z plane (azimuth is
    physically irrelevant for a spin-0 parent)."""
    E3 = 0.5 * x * mM
    if E3 < m_phi:
        raise ValueError("x below phi threshold")
    p3mag = np.sqrt(E3 * E3 - m_phi * m_phi)
    m12sq = mM * mM + m_phi * m_phi - 2.0 * mM * E3
    if m12sq <= m_mu * m_mu:
        raise ValueError("(x, c) outside Dalitz domain")
    m12 = np.sqrt(m12sq)
    # muon in the (mu nu) rest frame
    Es = (m12sq + m_mu * m_mu) / (2.0 * m12)
    ps = (m12sq - m_mu * m_mu) / (2.0 * m12)
    # boost of the (mu nu) system in the parent frame (along +z)
    E12 = mM - E3
    gam = E12 / m12
    gb = p3mag / m12  # gamma * beta
    s = np.sqrt(max(1.0 - c * c, 0.0))
    E1 = gam * Es + gb * ps * c
    p1z = gam * ps * c + gb * Es
    p1x = ps * s
    p1 = np.array([E1, p1x, 0.0, p1z])
    p3 = np.array([E3, 0.0, 0.0, -p3mag])
    P = np.array([mM, 0.0, 0.0, 0.0])
    p2 = P - p1 - p3
    return P, p1, p2, p3


def jacobian_x_c(mM, m_mu, m_phi, x):
    """|d(m12^2, m23^2) / d(x, c)| at fixed x (c-independent).

    m12^2 = mM^2 + m_phi^2 - x mM^2  ->  |dm12^2/dx| = mM^2.
    m23^2 = mM^2 + m_mu^2 - 2 mM E1 with
    E1 = gam Es + gb ps c              ->  |dm23^2/dc| = 2 mM gb ps."""
    E3 = 0.5 * x * mM
    p3mag = np.sqrt(max(E3 * E3 - m_phi * m_phi, 0.0))
    m12sq = mM * mM + m_phi * m_phi - 2.0 * mM * E3
    m12 = np.sqrt(max(m12sq, 0.0))
    if m12 <= m_mu:
        return 0.0
    ps = (m12sq - m_mu * m_mu) / (2.0 * m12)
    gb = p3mag / m12
    return (mM * mM) * (2.0 * mM * gb * ps)


def x_domain(mM, m_mu, m_phi):
    """Physical range of x = 2 E_phi / mM."""
    x_min = 2.0 * m_phi / mM
    x_max = 1.0 + (m_phi * m_phi - m_mu * m_mu) / (mM * mM)
    return x_min, x_max


def d2gamma_dx_dc(mM, m_mu, m_phi, x, c):
    """d^2Gamma/(dx dc) at g = C = 1 [PDG 50.22 + Jacobian]."""
    try:
        P, p1, p2, p3 = momenta_from_x_c(mM, m_mu, m_phi, x, c)
    except ValueError:
        return 0.0
    val = msq_trace(P, p1, p2, p3, m_mu, m_phi)
    J = jacobian_x_c(mM, m_mu, m_phi, x)
    return val * J / ((2.0 * np.pi) ** 3 * 32.0 * mM ** 3)


def sample_x(mM, m_mu, m_phi, n, rng, n_grid=400):
    """Draw x = 2E_phi/mM from the 1D marginal of the production
    density via inverse-CDF on a fine grid (c integrated; the overall
    orientation of the final state is isotropic for a spin-0 parent,
    so only the x marginal matters for the phi flux)."""
    x_lo, x_hi = x_domain(mM, m_mu, m_phi)
    xs = np.linspace(x_lo + 1e-9, x_hi - 1e-9, n_grid)
    cs = np.linspace(-1.0 + 1e-9, 1.0 - 1e-9, 60)
    dens = np.array([
        np.trapezoid([d2gamma_dx_dc(mM, m_mu, m_phi, x, c) for c in cs], cs)
        for x in xs])
    cdf = np.cumsum(dens)
    cdf = np.concatenate([[0.0], cdf]) / cdf[-1]
    grid = np.concatenate([[x_lo + 1e-9], xs])
    return np.interp(rng.uniform(0.0, 1.0, n), cdf, grid)


def boost_to_lab(estar, kstar, e_par, pvec_par, m_par):
    """Boost rest-frame momenta (estar, kstar) to the lab frame of a
    parent with lab energy e_par and 3-momentum pvec_par.

    Validated boost formula (reference pipeline):
        k_lab = k* + P [ (P.k*)/(M(E+M)) + E*/M ],
        E_lab = (E* E + P.k*) / M.

    estar: scalar or (n,); kstar: (n, 3); e_par: (n,); pvec_par: (n, 3).
    Returns (elab (n,), klab (n, 3))."""
    estar = np.broadcast_to(np.asarray(estar, dtype=float),
                            (len(kstar),))
    pdotk = np.einsum("ij,ij->i", pvec_par, kstar)
    elab = (estar * e_par + pdotk) / m_par
    coef = pdotk / (m_par * (e_par + m_par)) + estar / m_par
    klab = kstar + coef[:, None] * pvec_par
    return elab, klab


# ---------------------------------------------------------------------------
# geometry and decay-in-volume weighting
# (adapted from hepbench benchmarks/llp_forward/_shared/pipeline.py)
# ---------------------------------------------------------------------------
class DecayVolume:
    """On-axis cylindrical decay volume + downstream detector plane.

    Loaded from a YAML spec carrying (optionally nested under a top-level
    `geometry:` key): z_min_m, z_max_m, r_volume_m, z_det_m, r_det_m.
    All distances in meters from the primary interaction point."""

    def __init__(self, spec):
        if not isinstance(spec, dict):
            raise ValueError("geometry YAML must be a mapping")
        g = spec["geometry"] if "geometry" in spec else spec
        try:
            self.z_min = float(g["z_min_m"])
            self.z_max = float(g["z_max_m"])
            self.r_vol = float(g["r_volume_m"])
            self.z_det = float(g["z_det_m"])
            self.r_det = float(g["r_det_m"])
        except KeyError as e:
            raise ValueError(f"geometry spec missing {e}")

    @classmethod
    def from_yaml(cls, path):
        with open(path) as fh:
            return cls(yaml.safe_load(fh))

    def segment(self, theta):
        """In-volume path segment [L1, L2] for rays at angle theta.

        Vectorized; returns (L1, L2, ok). The ray r(z) = z tan(theta)
        must satisfy r < r_vol, capping the usable z at
        z_cap = r_vol / tan(theta). Valid for forward rays
        (theta < pi/2); callers must mask backward rays out of `ok`."""
        theta = np.asarray(theta, dtype=float)
        tan_t = np.tan(theta)
        cos_t = np.cos(theta)
        with np.errstate(divide="ignore"):
            z_cap = np.where(tan_t > 0.0, self.r_vol / tan_t, np.inf)
        z_hi = np.minimum(self.z_max, z_cap)
        ok = (z_hi > self.z_min) & (theta < 0.5 * np.pi)
        L1 = self.z_min / cos_t
        L2 = np.where(ok, z_hi / cos_t, self.z_min / cos_t)
        return L1, L2, ok


def decay_probability(L1, L2, lam):
    """P(decay in [L1, L2]) for decay length lam (vectorized)."""
    return np.exp(-L1 / lam) - np.exp(-L2 / lam)


def two_track_pass(p4_phi, vertex, m_phi, m_mu, geom, rng):
    """g-independent two-track acceptance at the midpoint convention.

    p4_phi: (n, 4) lab four-momenta [E, px, py, pz]; vertex: (n, 3)
    decay positions. Samples one isotropic phi -> mu mu decay per
    event, boosts both muons to the lab, propagates straight lines to
    z_det, and requires both to hit r < r_det moving forward."""
    n = len(p4_phi)
    if m_phi <= 2.0 * m_mu:
        raise ValueError("phi -> mu mu closed: m_phi <= 2 m_mu")
    pstar = np.sqrt(m_phi ** 2 / 4.0 - m_mu ** 2)
    estar = m_phi / 2.0
    cth = rng.uniform(-1.0, 1.0, n)
    sth = np.sqrt(1.0 - cth ** 2)
    az = rng.uniform(0.0, 2.0 * np.pi, n)
    kstar = pstar * np.stack(
        [sth * np.cos(az), sth * np.sin(az), cth], axis=1)
    E, pvec = p4_phi[:, 0], p4_phi[:, 1:]
    ok = np.ones(n, dtype=bool)
    for sign in (+1.0, -1.0):
        k = sign * kstar
        _, klab = boost_to_lab(estar, k, E, pvec, m_phi)
        forward = klab[:, 2] > 0.0
        dz = geom.z_det - vertex[:, 2]
        t = np.where(forward, dz / np.where(forward, klab[:, 2], 1.0), np.inf)
        xy = vertex[:, :2] + t[:, None] * klab[:, :2]
        r = np.sqrt(np.einsum("ij,ij->i", xy, xy))
        ok &= forward & (r < geom.r_det)
    return ok
