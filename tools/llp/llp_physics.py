"""
# llp_physics.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
"""
Shared physics for the `llp` bundle: analytic parent-flux kernels, a
declared parent-rest-frame LLP energy spectrum (a pinned data product,
NOT a hard-coded amplitude), decay-volume geometry, and the boost /
decay-probability conventions used by LLPFluxFromMesonDecayTool and
DecayInVolumeTool.

The bundle is model- and setting-agnostic by construction:
  - the collider-forward vs beam-dump choice lives entirely in the kernel
    YAML (parent mass, momentum and angular scales, per-interaction
    normalization) and the geometry YAML;
  - the PRODUCTION PHYSICS (which LLP energies the parent decay yields)
    lives entirely in the spectrum data product (`spectrum_spec`), so no
    benchmark's ground-truth amplitude is baked into tool code. A `table`
    spectrum (x, pdf) covers any declared 3-body radiation density; a
    `two_body` spectrum (delta function in x) covers dark-photon-like
    (pi0 -> gamma X) and dark-scalar-like (B -> K X) production.
Nothing in this module hard-codes a parent mass, a beam energy, a
detector location, or a matrix element.

Conventions (declared, and mirrored from the validated reference):
  - Kernels parametrize d^2 N_M / (dp dtheta) per primary interaction for
    *decaying* parents only (the decay-before-absorption fraction is folded
    into n_per_int by whoever pins the kernel).
  - The LLP energy in the parent rest frame is drawn from the declared
    spectrum in x = 2 E*/m_parent; the LLP direction is isotropic in the
    parent rest frame (spin-0 parent convention).
  - Event weights are g^2-stripped: w_i = n_per_int * kappa_M / n_samples,
    so N_sig(g) = N_int * g^2 * sum_i w_i * P_dec,i(g) * acc_i.
  - The LLP travels in a straight line from the primary vertex at its lab
    angle; the parent flight length is absorbed into the kernel.
  - P_dec = exp(-L1/lam) - exp(-L2/lam), lam = beta*gamma*ctau. The
    lifetime is set either by portal scaling
    (ctau = hbar*c / (g^2 * width_ref)) or by a directly declared
    ctau_grid_m (model-agnostic).
  - Two-track acceptance is evaluated at the MIDPOINT of the in-volume
    segment (g-independent, preserving exact coupling reweighting), with
    the two daughter masses declared (default mu mu).

Attribution: the kernel and geometry loaders and the rest-frame -> lab
boost formula are adapted from the HEPbench reference ground-truth
implementation, benchmarks/llp_forward/_shared/{kernels, pipeline}.py
(HEPbench authors, GPL v3+). The production amplitude that used to live
here has been removed on purpose: it now lives in the pinned spectrum
data product, keeping the tools free of any benchmark's ground truth.
"""

import csv
import math
import os

import numpy as np
import yaml

# hbar*c in GeV*m — the single constant tying the g^2-stripped reference
# width to a lab-frame decay length.
HBARC_M_GEV = 1.973269804e-16


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
# parent-rest-frame LLP energy spectrum (a declared data product)
# ---------------------------------------------------------------------------
class LLPSpectrum:
    """The parent-rest-frame LLP energy spectrum, declared as a pinned
    data product rather than computed from a hard-coded amplitude.

    The spectrum is expressed in the dimensionless energy fraction
    x = 2 E* / m_parent (E* the LLP energy in the parent rest frame).
    Two declared types are supported:

    `type: table`
        A tabulated density: columns `x` and `pdf` (the pdf may be
        unnormalized; it is normalized on load). x is sampled by
        inverse-CDF interpolation. This serves any declared 3-body
        radiation density (e.g. M -> lepton nu phi): the ground truth
        exports d(Br)/dx integrated over the other kinematics as the
        table, one file per (parent, m_phi). Loadable from a CSV file
        (header row `x,pdf`, optional `#` comment lines) or a YAML
        mapping carrying `type: table` and either inline `x:`/`pdf:`
        lists or a `csv:` path.

    `type: two_body`
        A delta-function spectrum from two-body kinematics
        M -> phi + X, with the other daughter mass `m_other_gev`. x is
        fixed at x0 = (m_parent^2 + m_phi^2 - m_other^2) / m_parent^2,
        so every event carries the same E*. This serves dark-photon-like
        (pi0 -> gamma X) and dark-scalar-like (B -> K X) production.
        Declared as a YAML mapping with `type: two_body` and
        `m_other_gev`.

    Kinematic openness and the reported cutoff are type-dependent:
      - two_body: open iff m_phi <= m_parent - m_other; cutoff is
        m_parent - m_other.
      - table: open iff the maximum tabulated x gives E* >= m_phi
        (E*_max = x_max * m_parent / 2 >= m_phi); cutoff is the
        E* implied by x_max, i.e. x_max * m_parent / 2.
    """

    def __init__(self, spec_type, *, x=None, pdf=None, m_other_gev=None,
                 source=None):
        self.type = spec_type
        self.source = source
        if spec_type == "table":
            x = np.asarray(x, dtype=float)
            pdf = np.asarray(pdf, dtype=float)
            if x.ndim != 1 or pdf.shape != x.shape or len(x) < 2:
                raise ValueError("table spectrum needs matching x and pdf "
                                 "columns of length >= 2")
            if np.any(pdf < 0.0):
                raise ValueError("table spectrum pdf must be non-negative")
            order = np.argsort(x)
            self.x = x[order]
            self.pdf = pdf[order]
            if not np.any(self.pdf > 0.0):
                raise ValueError("table spectrum pdf is identically zero")
            self.x_max = float(self.x[-1])
            self.x_min = float(self.x[0])
            self.m_other = None
            # inverse-CDF grid (trapezoidal cumulative integral)
            dcdf = 0.5 * (self.pdf[1:] + self.pdf[:-1]) * np.diff(self.x)
            cdf = np.concatenate([[0.0], np.cumsum(dcdf)])
            self._cdf = cdf / cdf[-1]
        elif spec_type == "two_body":
            if m_other_gev is None or float(m_other_gev) < 0.0:
                raise ValueError("two_body spectrum needs m_other_gev >= 0")
            self.m_other = float(m_other_gev)
            self.x = None
            self.pdf = None
            self.x_max = None
            self.x_min = None
            self._cdf = None
        else:
            raise ValueError(f"unknown spectrum type '{spec_type}' "
                             "(expected 'table' or 'two_body')")

    # ---- loaders ----
    @classmethod
    def from_path(cls, path):
        """Load a spectrum from a CSV (table) or YAML (table/two_body)."""
        lower = str(path).lower()
        if lower.endswith(".csv"):
            x, pdf = cls._read_csv(path)
            return cls("table", x=x, pdf=pdf, source=str(path))
        with open(path) as fh:
            doc = yaml.safe_load(fh)
        if not isinstance(doc, dict):
            raise ValueError("spectrum YAML must be a mapping")
        spec = doc.get("spectrum", doc)
        stype = spec.get("type")
        if stype == "two_body":
            return cls("two_body", m_other_gev=spec.get("m_other_gev"),
                       source=str(path))
        if stype == "table":
            if "csv" in spec:
                csv_path = spec["csv"]
                if not os.path.isabs(csv_path):
                    csv_path = os.path.join(os.path.dirname(path), csv_path)
                x, pdf = cls._read_csv(csv_path)
            else:
                x, pdf = spec.get("x"), spec.get("pdf")
                if x is None or pdf is None:
                    raise ValueError("table spectrum YAML needs inline "
                                     "'x' and 'pdf' lists or a 'csv' path")
            return cls("table", x=x, pdf=pdf, source=str(path))
        raise ValueError("spectrum spec missing a valid 'type' "
                         "(expected 'table' or 'two_body')")

    @staticmethod
    def _read_csv(path):
        xs, ps = [], []
        with open(path, newline="") as fh:
            rows = list(csv.reader(fh))
        header_seen = False
        for row in rows:
            if not row:
                continue
            first = row[0].strip()
            if first.startswith("#"):
                continue
            if not header_seen and not _is_number(first):
                header_seen = True  # column header line (x,pdf)
                continue
            header_seen = True
            xs.append(float(row[0]))
            ps.append(float(row[1]))
        if len(xs) < 2:
            raise ValueError(f"CSV spectrum {path} has < 2 data rows")
        return np.asarray(xs, dtype=float), np.asarray(ps, dtype=float)

    # ---- kinematics ----
    def is_open(self, m_parent, m_phi):
        """Whether the channel is kinematically open at this mass."""
        if self.type == "two_body":
            return m_phi < m_parent - self.m_other
        # table: max tabulated x must reach the phi rest energy
        return 0.5 * self.x_max * m_parent > m_phi

    def cutoff_gev(self, m_parent):
        """The reported kinematic cutoff (max open m_phi)."""
        if self.type == "two_body":
            return m_parent - self.m_other
        return 0.5 * self.x_max * m_parent

    def sample_x(self, m_parent, m_phi, n, rng):
        """Draw n values of x = 2 E*/m_parent from the spectrum."""
        if self.type == "two_body":
            x0 = (m_parent * m_parent + m_phi * m_phi
                  - self.m_other * self.m_other) / (m_parent * m_parent)
            return np.full(n, x0, dtype=float)
        u = rng.uniform(0.0, 1.0, n)
        return np.interp(u, self._cdf, self.x)


def _is_number(s):
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False


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


def two_track_pass(p4_phi, vertex, m_phi, m1, m2, geom, rng):
    """g-independent two-track acceptance at the midpoint convention.

    p4_phi: (n, 4) lab four-momenta [E, px, py, pz]; vertex: (n, 3)
    decay positions. Samples one isotropic two-body decay
    phi -> d1(m1) d2(m2) per event, boosts both daughters to the lab,
    propagates straight lines to z_det, and requires both to hit
    r < r_det moving forward. m1 and m2 need not be equal (default use
    is mu mu); the two daughters are back-to-back in the phi rest frame
    with a common momentum magnitude but individual energies."""
    n = len(p4_phi)
    if m_phi <= m1 + m2:
        raise ValueError(
            f"phi -> d1 d2 closed: m_phi <= m1 + m2 "
            f"(m_phi={m_phi}, m1={m1}, m2={m2})")
    # Kallen momentum: back-to-back |k*| for the two daughters.
    lam = (m_phi ** 2 - (m1 + m2) ** 2) * (m_phi ** 2 - (m1 - m2) ** 2)
    pstar = math.sqrt(lam) / (2.0 * m_phi)
    estar1 = (m_phi ** 2 + m1 ** 2 - m2 ** 2) / (2.0 * m_phi)
    estar2 = (m_phi ** 2 + m2 ** 2 - m1 ** 2) / (2.0 * m_phi)
    cth = rng.uniform(-1.0, 1.0, n)
    sth = np.sqrt(1.0 - cth ** 2)
    az = rng.uniform(0.0, 2.0 * np.pi, n)
    kstar = pstar * np.stack(
        [sth * np.cos(az), sth * np.sin(az), cth], axis=1)
    E, pvec = p4_phi[:, 0], p4_phi[:, 1:]
    ok = np.ones(n, dtype=bool)
    for sign, estar in ((+1.0, estar1), (-1.0, estar2)):
        k = sign * kstar
        _, klab = boost_to_lab(estar, k, E, pvec, m_phi)
        forward = klab[:, 2] > 0.0
        dz = geom.z_det - vertex[:, 2]
        t = np.where(forward, dz / np.where(forward, klab[:, 2], 1.0), np.inf)
        xy = vertex[:, :2] + t[:, None] * klab[:, :2]
        r = np.sqrt(np.einsum("ij,ij->i", xy, xy))
        ok &= forward & (r < geom.r_det)
    return ok
