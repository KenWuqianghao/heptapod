# Reconstruction of `sanitized.fr`

## Conventions

The new fields are denoted
\[
X_0,\qquad X_{1\mu},\qquad X_{2\mu\nu}.
\]

The model uses physical SM gauge fields \(A_\mu,Z_\mu,W^+_\mu,W^-_\mu,G^a_\mu\). I write
\[
F^V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu
\]
for abelian/physical field strengths as they appear in the file, and
\[
\widetilde F^V_{\mu\nu}=\frac12\epsilon_{\mu\nu\rho\sigma}F^{V\,\rho\sigma}.
\]
For gluons,
\[
G^a_{\mu\nu}
=
\partial_\mu G^a_\nu-\partial_\nu G^a_\mu
+g_s f^{abc}G^b_\mu G^c_\nu .
\]

The file does not declare gauge groups or covariant derivatives directly. It relies on SM symbols and FeynRules field strengths. Where the spin-2 fermion tensors require a covariant derivative, the SM gauge content is the usual one:
\[
D_\mu
=
\partial_\mu
+i g_s G^a_\mu T^a
+i e Q_f A_\mu
+i\frac{e}{s_w c_w}\left(T^3_f-Q_f s_w^2\right)Z_\mu
+i\frac{e}{\sqrt2 s_w}\left(T^+W^+_\mu+T^-W^-_\mu\right),
\]
with the \(SU(3)\) term only for quarks and the charged-current \(W^\pm\) terms only for left-handed weak doublets.

---

## Lagrangian

The total new-physics Lagrangian is

\[
\mathcal L_{\rm HCNP}
=
\mathcal L_{0f}
+\mathcal L_{0v}
+\mathcal L_1
+\mathcal L_{2f}
+\mathcal L_{2v}.
\]

### Scalar \(X_0\) fermion couplings

`L0f`
\[
\mathcal L_{0f}
=
-
X_0\,
c_\alpha
\left[
k_{Htt}\frac{m_t}{v}\bar t t
+
k_{Hbb}\frac{m_b}{v}\bar b b
+
k_{H\ell\ell}\frac{m_\tau}{v}\bar\tau\tau
\right].
\]

`L0f`
\[
\mathcal L_{0f}
\supset
-
iX_0\,
s_\alpha
\left[
k_{Att}\frac{m_t}{v}\bar t\gamma^5 t
+
k_{Abb}\frac{m_b}{v}\bar b\gamma^5 b
+
k_{A\ell\ell}\frac{m_\tau}{v}\bar\tau\gamma^5\tau
\right].
\]

Here \(c_\alpha=\texttt{ca}\), \(s_\alpha=\texttt{sa}=\sqrt{1-c_\alpha^2}\), and \(v=\texttt{vev}\).

### Scalar \(X_0\) gauge-boson couplings

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac14 X_0\,c_\alpha k_{Haa}g_{Haa}\,
F^A_{\mu\nu}F^{A\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac14 X_0\,s_\alpha k_{Aaa}g_{Aaa}\,
F^A_{\mu\nu}\widetilde F^{A\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac12 X_0\,c_\alpha k_{Hza}g_{Hza}\,
F^Z_{\mu\nu}F^{A\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac12 X_0\,s_\alpha k_{Aza}g_{Aza}\,
F^Z_{\mu\nu}\widetilde F^{A\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac14 X_0\,c_\alpha k_{Hgg}g_{Hgg}\,
G^a_{\mu\nu}G^{a\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac14 X_0\,s_\alpha k_{Agg}g_{Agg}\,
G^a_{\mu\nu}\widetilde G^{a\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{1}{4\Lambda}X_0\,c_\alpha k_{Hzz}\,
F^Z_{\mu\nu}F^{Z\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{1}{4\Lambda}X_0\,s_\alpha k_{Azz}\,
F^Z_{\mu\nu}\widetilde F^{Z\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{1}{2\Lambda}X_0\,c_\alpha k_{Hww}\,
F^{W^-}_{\mu\nu}F^{W^+\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{1}{2\Lambda}X_0\,s_\alpha k_{Aww}\,
F^{W^-}_{\mu\nu}\widetilde F^{W^+\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{c_\alpha k_{Hda}}{\Lambda}
X_0\,Z_\nu\,\partial_\mu F^{A\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{c_\alpha k_{Hdz}}{\Lambda}
X_0\,Z_\nu\,\partial_\mu F^{Z\,\mu\nu}.
\]

`L0v`
\[
\mathcal L_{0v}
\supset
-\frac{c_\alpha}{\Lambda}
X_0
\left[
k_{Hdw}W^-_\nu\,\partial_\mu F^{W^+\,\mu\nu}
+
k_{Hdw}^\ast W^+_\nu\,\partial_\mu F^{W^-\,\mu\nu}
\right],
\]
with
\[
k_{Hdw}=k_{HdwR}+i k_{HdwI}.
\]

### Vector \(X_1\) fermion couplings

`L1f`
\[
\mathcal L_{1f}
=
X_{1\mu}
\sum_{n,i}
\bar u_{n i}\gamma^\mu
\left(k_{qa}a_u-k_{qb}b_u\gamma^5\right)
u_{n i}.
\]

`L1f`
\[
\mathcal L_{1f}
\supset
X_{1\mu}
\sum_{n,i}
\bar d_{n i}\gamma^\mu
\left(k_{qa}a_d-k_{qb}b_d\gamma^5\right)
d_{n i}.
\]

`L1f`
\[
\mathcal L_{1f}
\supset
X_{1\mu}
\sum_n
\bar\nu_n\gamma^\mu
\left(k_{\ell a}a_\nu-k_{\ell b}b_\nu\gamma^5\right)
\nu_n.
\]

`L1f`
\[
\mathcal L_{1f}
\supset
X_{1\mu}
\sum_n
\bar\ell_n\gamma^\mu
\left(k_{\ell a}a_\ell-k_{\ell b}b_\ell\gamma^5\right)
\ell_n.
\]

The internal SM-like vector/axial coefficients are
\[
a_u=\frac{e}{2s_wc_w}\left(\frac12-\frac43s_w^2\right),
\qquad
b_u=\frac{e}{2s_wc_w}\frac12,
\]
\[
a_d=\frac{e}{2s_wc_w}\left(-\frac12+\frac23s_w^2\right),
\qquad
b_d=\frac{e}{2s_wc_w}\left(-\frac12\right),
\]
\[
a_\nu=b_\nu=\frac{e}{2s_wc_w}\frac12,
\]
\[
a_\ell=\frac{e}{2s_wc_w}\left(-\frac12+2s_w^2\right),
\qquad
b_\ell=\frac{e}{2s_wc_w}\left(-\frac12\right).
\]

### Vector \(X_1\) charged-vector couplings

`L1w`
\[
\mathcal L_{1w}
\supset
i k_{w1}g_{WWZ}
\left[
F^{W^-}_{\mu\nu}W^{+\mu}
-
F^{W^+}_{\mu\nu}W^{-\mu}
\right]X_1^\nu .
\]

`L1w`
\[
\mathcal L_{1w}
\supset
i k_{w2}g_{WWZ}
W^-_\mu W^+_\nu
F^{X_1\,\mu\nu}.
\]

`L1w`
\[
\mathcal L_{1w}
\supset
-k_{w3}
W^-_\mu W^+_\nu
\left(
\partial^\mu X_1^\nu+\partial^\nu X_1^\mu
\right).
\]

`L1w`
\[
\mathcal L_{1w}
\supset
i k_{w4}
W^-_\mu W^+_\nu
\widetilde F^{X_1\,\mu\nu}.
\]

`L1w`
\[
\mathcal L_{1w}
\supset
-k_{w5}
\epsilon_{\mu\nu\rho\sigma}
\left[
W^{-\mu}\partial^\rho W^{+\nu}
-
(\partial^\rho W^{-\mu})W^{+\nu}
\right]X_1^\sigma .
\]

where
\[
g_{WWZ}=-\frac{ec_w}{s_w}.
\]

### Vector \(X_1\) neutral-vector couplings

`L1z`
\[
\mathcal L_{1z}
\supset
-k_{z1}
F^Z_{\mu\nu}Z^\mu X_1^\nu .
\]

`L1z`
\[
\mathcal L_{1z}
\supset
-k_{z3}
X_{1\mu}
(\partial_\nu Z^\mu)Z^\nu .
\]

`L1z`
\[
\mathcal L_{1z}
\supset
-k_{z5}
\epsilon_{\mu\nu\rho\sigma}
X_1^\mu Z^\nu \partial^\rho Z^\sigma .
\]

### Spin-2 \(X_2\) fermion couplings

`L2f`
\[
\mathcal L_{2f}
=
-\frac{1}{\Lambda}
X_2^{\mu\nu}
\left[
k_q T^{q}_{\mu\nu}
+
k_{q3}\left(T^{q_3}_{\mu\nu}+Y^q_{\mu\nu}\right)
+
k_\ell\left(T^\ell_{\mu\nu}+Y^\ell_{\mu\nu}\right)
\right].
\]

The file defines
\[
T^q_{\mu\nu}
=
\sum_{f=u,d,c,s}T^f_{\mu\nu},
\qquad
T^{q_3}_{\mu\nu}
=
T^t_{\mu\nu}+T^b_{\mu\nu},
\]
\[
T^\ell_{\mu\nu}
=
\sum_{f=\nu_e,\nu_\mu,\nu_\tau,e,\mu,\tau}T^f_{\mu\nu}.
\]

The fermion energy-momentum tensor represented by `Tfermion[f,mu,nu]` is the symmetric kinetic tensor
\[
T^f_{\mu\nu}
=
\frac{i}{4}
\left[
\bar f\gamma_\mu D_\nu f
-
(D_\nu\bar f)\gamma_\mu f
+
\bar f\gamma_\nu D_\mu f
-
(D_\mu\bar f)\gamma_\nu f
\right].
\]

The extra Yukawa/mass-trace pieces encoded in `TYq` and `TYl` are
\[
Y^q_{\mu\nu}
=
\eta_{\mu\nu}
\left(
m_t\bar t t+m_b\bar b b
\right),
\]
\[
Y^\ell_{\mu\nu}
=
\eta_{\mu\nu}
m_\tau\bar\tau\tau .
\]

### Spin-2 \(X_2\) gauge-boson couplings

`L2v`
\[
\mathcal L_{2v}
=
-\frac{1}{\Lambda}
X_2^{\mu\nu}
\left[
k_g T^g_{\mu\nu}
+
k_a T^\gamma_{\mu\nu}
+
k_z T^Z_{\mu\nu}
+
k_w T^W_{\mu\nu}
\right].
\]

The gluon tensor is
\[
T^g_{\mu\nu}
=
\frac14\eta_{\mu\nu}G^a_{\rho\sigma}G^{a\,\rho\sigma}
-
G^a_{\mu\rho}G_\nu^{a\,\rho}.
\]

The photon tensor is
\[
T^\gamma_{\mu\nu}
=
\frac14\eta_{\mu\nu}F^A_{\rho\sigma}F^{A\,\rho\sigma}
-
F^A_{\mu\rho}F^A_{\nu}{}^{\rho}.
\]

The \(Z\)-boson tensor is
\[
T^Z_{\mu\nu}
=
\eta_{\mu\nu}
\left[
\frac14F^Z_{\rho\sigma}F^{Z\,\rho\sigma}
-\frac12m_Z^2 Z_\rho Z^\rho
\right]
-
F^Z_{\mu\rho}F^Z_{\nu}{}^\rho
+
m_Z^2 Z_\mu Z_\nu .
\]

The charged-\(W\) tensor is
\[
T^W_{\mu\nu}
=
\eta_{\mu\nu}
\left[
\frac12F^{W^-}_{\rho\sigma}F^{W^+\,\rho\sigma}
-
m_W^2 W^-_\rho W^{+\rho}
\right]
-
F^{W^-}_{\mu\rho}F^{W^+}_{\nu}{}^\rho
-
F^{W^-}_{\nu\rho}F^{W^+}_{\mu}{}^\rho
+
m_W^2
\left(
W^-_\mu W^+_\nu
+
W^-_\nu W^+_\mu
\right).
\]

---

## Field table

| `.fr` class | Field | Spin | SU(3) rep | SU(2) rep | \(Q\) | \(Y\) | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---|---|
| `S[100]` | `X0` | 0 | singlet, no color index declared | singlet/not declared | 0 | 0 | yes | `MX0 = 125.0` |
| `V[101]` | `X1` | 1 | singlet, no color index declared | singlet/not declared | 0 | 0 | yes | `MX1 = 125.0` |
| `T[102]` | `X2` | 2 | singlet, no color index declared | singlet/not declared | 0 | 0 | yes | `MX2 = 125.0` |

Widths are also declared:
\[
WX0=WX1=WX2=0.00407.
\]

---

## External parameters

| Parameter | Value | Multiplies | Physical meaning |
|---|---:|---|---|
| `Lambda` | `1000.` | inverse powers in `L0v`, `L2f`, `L2v` | EFT scale suppressing dimension-5 operators |
| `ca` | `1.` | CP-even scalar pieces | scalar CP-even mixing coefficient \(c_\alpha\) |
| `kSM` | `1.` | no term in `LHCNP` in this file | declared external normalization, unused in the shown Lagrangian |
| `kHtt` | `1.` | \(X_0\bar t t\) | CP-even top Yukawa modifier |
| `kAtt` | `1.` | \(X_0\bar t i\gamma^5 t\) | CP-odd top Yukawa modifier |
| `kHbb` | `1.` | \(X_0\bar b b\) | CP-even bottom Yukawa modifier |
| `kAbb` | `1.` | \(X_0\bar b i\gamma^5 b\) | CP-odd bottom Yukawa modifier |
| `kHll` | `1.` | \(X_0\bar\tau\tau\) | CP-even tau Yukawa modifier |
| `kAll` | `1.` | \(X_0\bar\tau i\gamma^5\tau\) | CP-odd tau Yukawa modifier |
| `kHaa` | `1.` | \(X_0F^A_{\mu\nu}F^{A\mu\nu}\) | CP-even \(X_0\gamma\gamma\) coupling modifier |
| `kAaa` | `1.` | \(X_0F^A_{\mu\nu}\widetilde F^{A\mu\nu}\) | CP-odd \(X_0\gamma\gamma\) coupling modifier |
| `kHza` | `1.` | \(X_0F^Z_{\mu\nu}F^{A\mu\nu}\) | CP-even \(X_0Z\gamma\) coupling modifier |
| `kAza` | `1.` | \(X_0F^Z_{\mu\nu}\widetilde F^{A\mu\nu}\) | CP-odd \(X_0Z\gamma\) coupling modifier |
| `kHgg` | `1.` | \(X_0G^a_{\mu\nu}G^{a\mu\nu}\) | CP-even \(X_0gg\) coupling modifier |
| `kAgg` | `1.` | \(X_0G^a_{\mu\nu}\widetilde G^{a\mu\nu}\) | CP-odd \(X_0gg\) coupling modifier |
| `kHzz` | `0.` | \(X_0F^Z_{\mu\nu}F^{Z\mu\nu}/\Lambda\) | CP-even \(X_0ZZ\) EFT coupling |
| `kAzz` | `0.` | \(X_0F^Z_{\mu\nu}\widetilde F^{Z\mu\nu}/\Lambda\) | CP-odd \(X_0ZZ\) EFT coupling |
| `kHww` | `0.` | \(X_0F^{W^-}_{\mu\nu}F^{W+\mu\nu}/\Lambda\) | CP-even \(X_0W^+W^-\) EFT coupling |
| `kAww` | `0.` | \(X_0F^{W^-}_{\mu\nu}\widetilde F^{W+\mu\nu}/\Lambda\) | CP-odd \(X_0W^+W^-\) EFT coupling |
| `kHda` | `0.` | \(X_0Z_\nu\partial_\mu F^{A\mu\nu}/\Lambda\) | derivative \(X_0Z\gamma\) coupling |
| `kHdz` | `0.` | \(X_0Z_\nu\partial_\mu F^{Z\mu\nu}/\Lambda\) | derivative \(X_0ZZ\) coupling |
| `kHdwR` | `0.` | real part of `kHdw` | real part of derivative \(X_0W^+W^-\) coupling |
| `kHdwI` | `0.` | imaginary part of `kHdw` | imaginary part of derivative \(X_0W^+W^-\) coupling |
| `kqa` | `1.` | vector quark current coupled to \(X_1\) | quark vector-current strength |
| `kqb` | `1.` | axial quark current coupled to \(X_1\) | quark axial-current strength |
| `kla` | `1.` | vector lepton/neutrino current coupled to \(X_1\) | lepton vector-current strength |
| `klb` | `1.` | axial lepton/neutrino current coupled to \(X_1\) | lepton axial-current strength |
| `kw1` | `1.` | first \(X_1W^+W^-\) tensor structure | anomalous charged-vector coupling |
| `kw2` | `1.` | \(W^-W^+F^{X_1}\) | anomalous charged-vector coupling |
| `kw3` | `0.` | \(W^-W^+\partial X_1\) symmetric derivative | anomalous charged-vector coupling |
| `kw4` | `0.` | \(W^-W^+\widetilde F^{X_1}\) | CP-odd/dual charged-vector coupling |
| `kw5` | `0.` | \(\epsilon W\partial W X_1\) | parity-odd charged-vector coupling |
| `kz1` | `0.` | \(F^Z Z X_1\) | anomalous \(X_1ZZ\) coupling |
| `kz3` | `1.` | \(X_1(\partial Z)Z\) | anomalous \(X_1ZZ\) derivative coupling |
| `kz5` | `0.` | \(\epsilon X_1Z\partial Z\) | parity-odd \(X_1ZZ\) coupling |
| `kq` | `1.` | \(X_2T_{\mu\nu}\) of light quarks \(u,d,c,s\) | spin-2 coupling to light-quark energy-momentum tensor |
| `kq3` | `1.` | \(X_2T_{\mu\nu}\) of \(t,b\) plus mass trace | spin-2 coupling to third-generation quark tensor |
| `kl` | `1.` | \(X_2T_{\mu\nu}\) of leptons plus tau mass trace | spin-2 coupling to lepton tensor |
| `kg` | `1.` | \(X_2T^g_{\mu\nu}\) | spin-2 coupling to gluon tensor |
| `ka` | `1.` | \(X_2T^\gamma_{\mu\nu}\) | spin-2 coupling to photon tensor |
| `kz` | `1.` | \(X_2T^Z_{\mu\nu}\) | spin-2 coupling to \(Z\)-boson tensor |
| `kw` | `1.` | \(X_2T^W_{\mu\nu}\) | spin-2 coupling to charged-\(W\) tensor |

Internal parameters appearing in the Lagrangian are
\[
s_\alpha=\sqrt{1-c_\alpha^2},
\qquad
k_{Hdw}=k_{HdwR}+ik_{HdwI},
\]
and the loop-normalized effective coefficients
\[
g_{Haa},\ g_{Aaa},\ g_{Hza},\ g_{Aza},\ g_{Hgg},\ g_{Agg}.
\]

---

## Physics summary

The file encodes a neutral spin-0, spin-1, and spin-2 resonance sector coupled to SM fermions and electroweak/gluon gauge bosons through Yukawa-like, anomalous gauge-field-strength, vector-current, and energy-momentum-tensor operators. The scalar \(X_0\) has both CP-even and CP-odd couplings controlled by \(c_\alpha\) and \(s_\alpha\); the vector \(X_1\) couples to SM vector/axial currents and to \(WW/ZZ\); the tensor \(X_2\) couples universally or non-universally to SM stress tensors. These interactions mediate production and decay channels such as \(gg,\gamma\gamma,Z\gamma,ZZ,W^+W^-,f\bar f\leftrightarrow X_i\), with spin-dependent angular structures.