# Reverse-check review package — `HiggsCharacterisation_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `HiggsCharacterisation/model/HiggsCharacterisation_gen.fr` |
| original model name | `HiggsCharacterisation_gen` (hidden from the agent) |
| paper | HiggsCharacterisation/text/1306.6464.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `L0v` (`:=`)

```mathematica
(-1/4 (ca kHaa gHaa FS[A,mu,nu] FS[A,mu,nu] + sa kAaa gAaa FS[A,mu,nu] Dual[FS][A,mu,nu]) - 1/2 (ca kHza gHza FS[Z,mu,nu] FS[A,mu,nu] + sa kAza gAza FS[Z,mu,nu] Dual[FS][A,mu,nu]) - 1/4 (ca kHgg gHgg FS[G,mu,nu,a] FS[G,mu,nu,a] + sa kAgg gAgg FS[G,mu,nu,a] Dual[FS][G,mu,nu,a]) - 1/4/Lambda (ca kHzz FS[Z,mu,nu] FS[Z,mu,nu] + sa kAzz FS[Z,mu,nu] Dual[FS][Z,mu,nu]) - 1/2/Lambda (ca kHww FS[Wbar,mu,nu] FS[W,mu,nu] + sa kAww FS[Wbar,mu,nu] Dual[FS][W,mu,nu]) - 1/Lambda (ca kHda Z[nu] del[FS[A,mu,nu],mu] + ca kHdz Z[nu] del[FS[Z,mu,nu],mu] + ca (kHdw Wbar[nu] del[FS[W,mu,nu],mu] + HC[kHdw Wbar[nu] del[FS[W,mu,nu],mu]]))) X0
```

### `L1f` (`:=`)

```mathematica
(kqa au uqbar[s,n,i].Ga[mu,s,t].uq[t,n,i] + kqa ad dqbar[s,n,i].Ga[mu,s,t].dq[t,n,i] + kla an vlbar[s,n].Ga[mu,s,t].vl[t,n] + kla al lbar[s,n].Ga[mu,s,t].l[t,n] - kqb bu uqbar[s,n,i].Ga[mu,s,t].Ga[5,t,u].uq[u,n,i] - kqb bd dqbar[s,n,i].Ga[mu,s,t].Ga[5,t,u].dq[u,n,i] - klb bn vlbar[s,n].Ga[mu,s,t].Ga[5,t,u].vl[u,n] - klb bl lbar[s,n].Ga[mu,s,t].Ga[5,t,u].l[u,n]) X1[mu]
```

### `L1w` (`:=`)

```mathematica
I kw1 gwwz (FS[Wbar,mu,nu] W[mu] - FS[W,mu,nu] Wbar[mu]) X1[nu] + I kw2 gwwz Wbar[mu] W[nu] FS[X1,mu,nu] - kw3 Wbar[mu] W[nu] (del[X1[nu],mu] + del[X1[mu],nu]) + I kw4 Wbar[mu] W[nu] Dual[FS][X1,mu,nu] - kw5 Eps[mu,nu,rho,sig] (Wbar[mu] del[W[nu],rho] - del[Wbar[mu],rho] W[nu]) X1[sig]
```

### `L1z` (`:=`)

```mathematica
-kz1 FS[Z,mu,nu] Z[mu] X1[nu] - kz3 X1[mu] del[Z[mu],nu] Z[nu] - kz5 Eps[mu,nu,rho,sig] X1[mu] Z[nu] del[Z[sig],rho]
```

### `L1` (`:=`)

```mathematica
L1f + L1w + L1z
```

### `L2f` (`:=`)

```mathematica
-1/Lambda (kq TFq[mu,nu] + kq3 (TFq3[mu,nu] + TYq[mu,nu]) + kl (TFl[mu,nu] + TYl[mu,nu])) X2[mu,nu]
```

### `L2v` (`:=`)

```mathematica
-1/Lambda (kg TGg[mu,nu] + ka TGa[mu,nu] + kz TGz[mu,nu] + kw TGw[mu,nu]) X2[mu,nu]
```

### `L2` (`:=`)

```mathematica
L2f + L2v
```

### `LHCNP` (`:=`)

```mathematica
L0f + L0v + L1 + L2
```

## Blank-slate reconstruction

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

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Locations

The model is defined in **Section 2, “Effective lagrangian”**. The paper states
\[
\mathcal L_{\mathrm{HC},J}=\mathcal L_{\mathrm{SM}-H}+\mathcal L_J
\]
in **eq. (2.1)**, where \(\mathcal L_J\) contains the kinetic and interaction terms of the new bosonic state \(X(J^P)\).

Relevant definitions:

- **Spin/parity content:** Section 2, before eq. (2.1): \(J^P=0^+,0^-,1^+,1^-,2^+\).
- **Spin-0 fermion Lagrangian:** **eq. (2.2)**, with \(c_\alpha,s_\alpha\) defined in **eq. (2.3)**.
- **Spin-0 vector Lagrangian:** **eq. (2.4)**.
- **Field strengths and duals:** **eqs. (2.5)-(2.7)**.
- **Spin-1 fermion Lagrangian:** **eq. (2.8)**; quark vector/axial coefficients in **eqs. (2.9)-(2.10)**, with analogous lepton coefficients stated in prose.
- **Spin-1 \(WW\) Lagrangian:** **eq. (2.11)**.
- **Spin-1 \(ZZ\) Lagrangian:** **eq. (2.12)**.
- **Spin-1 parity restrictions:** **eqs. (2.13)-(2.14)**.
- **Spin-2 fermion Lagrangian:** **eq. (2.15)**.
- **Spin-2 vector Lagrangian:** **eq. (2.16)**.
- **Explicit QED fermion/photon energy-momentum tensors:** **eqs. (2.17)-(2.18)**.
- **Universal RS-like spin-2 limit:** **eq. (2.19)**.
- **Non-universal spin-2 quark/gluon example:** **Section 4.1, eq. (4.1)**.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| \(\mathcal L_{\mathrm{HC},J}=\mathcal L_{\mathrm{SM}-H}+\mathcal L_J\), one chosen \(J\) sector, eq. (2.1) | \(\mathcal L_{\rm HCNP}=\mathcal L_{0f}+\mathcal L_{0v}+\mathcal L_1+\mathcal L_{2f}+\mathcal L_{2v}\) | disagree | The paper presents a model for a new state \(X(J^P)\) with a chosen spin/parity sector; the reconstruction sums spin-0, spin-1, and spin-2 sectors simultaneously. This may reflect implementation packaging, but it is not how eq. (2.1) is written. |
| New bosonic state \(X(J^P)\), \(J^P=0^+,0^-,1^+,1^-,2^+\), Section 2 | Separate \(X_0,X_{1\mu},X_{2\mu\nu}\) fields | agree | Physics content matches the spin assignments, though the paper phrases this as alternative hypotheses rather than necessarily simultaneous particles. |
| Below-EWSB physical-field EFT; no required \(SU(2)_L\times U(1)_Y\) assignment for spin-1, Section 2.2 | \(X_0,X_1,X_2\) listed as neutral color/electroweak singlets | agree | For spin-2 the paper explicitly says color, weak, and electromagnetic singlet before eq. (2.15). For spin-1 the paper explicitly avoids specifying EW representation; neutral physical \(X_1\) is consistent with the written \(ZZ/WW\) interactions. |
| Spin-0 Yukawa: \(-\sum_{f=t,b,\tau}\bar\psi_f(c_\alpha\kappa_{Hff}g_{Hff}+is_\alpha\kappa_{Aff}g_{Aff}\gamma_5)\psi_fX_0\), eq. (2.2) | \(-X_0c_\alpha[k_{Htt}m_t/v\,\bar tt+k_{Hbb}m_b/v\,\bar bb+k_{H\ell\ell}m_\tau/v\,\bar\tau\tau]\) plus \(-iX_0s_\alpha[\cdots\bar f\gamma^5f]\) | agree | Same third-generation scalar and pseudoscalar Yukawa structures, with \(g_{Hff}=g_{Aff}=m_f/v\). |
| \(c_\alpha=\cos\alpha,\ s_\alpha=\sin\alpha\), eq. (2.3) | \(c_\alpha=\texttt{ca},\ s_\alpha=\sqrt{1-c_\alpha^2}\) | agree | Equivalent only if the implementation restricts to the principal positive \(s_\alpha\). The paper treats \(s_\alpha\) as \(\sin\alpha\). |
| SM-like spin-0 vector mass terms \(c_\alpha\kappa_{\rm SM}[\frac12 g_{HZZ}Z_\mu Z^\mu+g_{HWW}W^+_\mu W^{-\mu}]X_0\), eq. (2.4) | `kSM` declared but “unused”; no \(X_0ZZ\) or \(X_0W^+W^-\) mass term listed | missing-in-reconstruction | This is a central term in eq. (2.4), needed to recover the SM limit with \(c_\alpha=1,\kappa_{\rm SM}=1\). |
| \(-\frac14[c_\alpha\kappa_{H\gamma\gamma}g_{H\gamma\gamma}A_{\mu\nu}A^{\mu\nu}+s_\alpha\kappa_{A\gamma\gamma}g_{A\gamma\gamma}A_{\mu\nu}\tilde A^{\mu\nu}]X_0\), eq. (2.4) | \(-\frac14X_0c_\alpha k_{Haa}g_{Haa}F^AF^A\), \(-\frac14X_0s_\alpha k_{Aaa}g_{Aaa}F^A\tilde F^A\) | agree | Same CP-even and CP-odd \(\gamma\gamma\) structures. |
| \(-\frac12[c_\alpha\kappa_{HZ\gamma}g_{HZ\gamma}Z_{\mu\nu}A^{\mu\nu}+s_\alpha\kappa_{AZ\gamma}g_{AZ\gamma}Z_{\mu\nu}\tilde A^{\mu\nu}]X_0\), eq. (2.4) | \(-\frac12X_0c_\alpha k_{Hza}g_{Hza}F^ZF^A\), \(-\frac12X_0s_\alpha k_{Aza}g_{Aza}F^Z\tilde F^A\) | agree | Same \(Z\gamma\) field-strength structures. |
| \(-\frac14[c_\alpha\kappa_{Hgg}g_{Hgg}G^a_{\mu\nu}G^{a\mu\nu}+s_\alpha\kappa_{Agg}g_{Agg}G^a_{\mu\nu}\tilde G^{a\mu\nu}]X_0\), eq. (2.4) | \(-\frac14X_0c_\alpha k_{Hgg}g_{Hgg}GG\), \(-\frac14X_0s_\alpha k_{Agg}g_{Agg}G\tilde G\) | agree | Same gluonic CP-even and CP-odd structures. |
| \(-\frac1{4\Lambda}[c_\alpha\kappa_{HZZ}Z_{\mu\nu}Z^{\mu\nu}+s_\alpha\kappa_{AZZ}Z_{\mu\nu}\tilde Z^{\mu\nu}]X_0\), eq. (2.4) | \(-\frac1{4\Lambda}X_0c_\alpha k_{Hzz}F^ZF^Z\), \(-\frac1{4\Lambda}X_0s_\alpha k_{Azz}F^Z\tilde F^Z\) | agree | Same higher-dimensional \(ZZ\) field-strength terms. |
| \(-\frac1{2\Lambda}[c_\alpha\kappa_{HWW}W^+_{\mu\nu}W^{-\mu\nu}+s_\alpha\kappa_{AWW}W^+_{\mu\nu}\tilde W^{-\mu\nu}]X_0\), eq. (2.4) | \(-\frac1{2\Lambda}X_0c_\alpha k_{Hww}F^{W^-}F^{W^+}\), \(-\frac1{2\Lambda}X_0s_\alpha k_{Aww}F^{W^-}\tilde F^{W^+}\) | agree | Same \(W^+W^-\) field-strength content; charge ordering is immaterial for these bilinears. |
| \(-\frac{c_\alpha}{\Lambda}[\kappa_{H\partial\gamma}Z_\nu\partial_\mu A^{\mu\nu}+\kappa_{H\partial Z}Z_\nu\partial_\mu Z^{\mu\nu}+\kappa_{H\partial W}W^+_\nu\partial_\mu W^{-\mu\nu}+\mathrm{h.c.}]X_0\), eq. (2.4) | \(-\frac{c_\alpha}{\Lambda}X_0[k_{Hda}Z_\nu\partial F_A+k_{Hdz}Z_\nu\partial F_Z+k_{Hdw}W^-_\nu\partial F_{W^+}+k_{Hdw}^*W^+_\nu\partial F_{W^-}]\) | disagree | Neutral derivative terms agree. The charged \(W\) term uses the complex coefficient on the charge-conjugate structure relative to the paper, so the imaginary part has the opposite convention unless \(k_{Hdw}\) is defined as \(\kappa_{H\partial W}^*\). |
| Field strengths \(V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu\), \(G^a_{\mu\nu}=\partial G+g_sf^{abc}G^bG^c\), dual \(\tilde V_{\mu\nu}=\frac12\epsilon_{\mu\nu\rho\sigma}V^{\rho\sigma}\), eqs. (2.5)-(2.7) | Same definitions for physical \(A,Z,W^\pm\), gluons, and duals | agree | Matches the paper definitions. |
| Spin-1 fermions \(\sum_{f=q,\ell}\bar\psi_f\gamma^\mu(\kappa_{fa}a_f-\kappa_{fb}b_f\gamma^5)\psi_fX_{1\mu}\), eq. (2.8) | Separate sums over \(u,d,\nu,\ell\) with \(k_{qa},k_{qb},k_{\ell a},k_{\ell b}\) and SM-like \(a_f,b_f\) | agree | Same vector/axial current structure; reconstruction makes generation and color sums explicit. |
| Quark coefficients \(a_u,b_u,a_d,b_d\), eqs. (2.9)-(2.10) | Same coefficients written with \(e/(s_wc_w)\) | agree | Since \(g=e/s_w\), the expressions match. |
| Lepton coefficients “similarly for the leptons,” after eq. (2.10) | Explicit \(a_\nu=b_\nu=e/(4s_wc_w)\), \(a_\ell=e( -1/2+2s_w^2)/(2s_wc_w)\), \(b_\ell=-e/(4s_wc_w)\) | agree | These are the standard SM \(Z\)-like vector/axial coefficients implied by the paper. |
| \(i\kappa_{W1}g_{WWZ}(W^+_{\mu\nu}W^{-\mu}-W^-_{\mu\nu}W^{+\mu})X_1^\nu\), eq. (2.11) | \(ik_{w1}g_{WWZ}(F^{W^-}_{\mu\nu}W^{+\mu}-F^{W^+}_{\mu\nu}W^{-\mu})X_1^\nu\) | disagree | This is the negative of the paper’s bracket if \(k_{w1}=\kappa_{W1}\) and the same \(g_{WWZ}\) convention is used. |
| \(i\kappa_{W2}g_{WWZ}W^+_\mu W^-_\nu X_1^{\mu\nu}\), eq. (2.11) | \(ik_{w2}g_{WWZ}W^-_\mu W^+_\nu F_{X_1}^{\mu\nu}\) | disagree | Because \(X_1^{\mu\nu}\) is antisymmetric, exchanging \(W^+\leftrightarrow W^-\) with the Lorentz indices gives an overall minus sign. |
| \(-\kappa_{W3}W^+_\mu W^-_\nu(\partial^\mu X_1^\nu+\partial^\nu X_1^\mu)\), eq. (2.11) | \(-k_{w3}W^-_\mu W^+_\nu(\partial^\mu X_1^\nu+\partial^\nu X_1^\mu)\) | agree | The derivative tensor is symmetric in \(\mu,\nu\), so the charge/index ordering is equivalent. |
| \(+i\kappa_{W4}W^+_\mu W^-_\nu\tilde X_1^{\mu\nu}\), eq. (2.11) | \(+ik_{w4}W^-_\mu W^+_\nu\tilde F_{X_1}^{\mu\nu}\) | disagree | Same antisymmetry issue as the \(W2\) term: the reconstruction has the opposite sign for equal coupling definitions. |
| \(-\kappa_{W5}\epsilon_{\mu\nu\rho\sigma}[W^{+\mu}\partial^\rho W^{-\nu}-(\partial^\rho W^{+\mu})W^{-\nu}]X_1^\sigma\), eq. (2.11) | \(-k_{w5}\epsilon_{\mu\nu\rho\sigma}[W^{-\mu}\partial^\rho W^{+\nu}-(\partial^\rho W^{-\mu})W^{+\nu}]X_1^\sigma\) | agree | After relabeling the antisymmetric \(\epsilon_{\mu\nu\rho\sigma}\) indices, this is equivalent. |
| \(g_{WWZ}=-e\cot\theta_W\), below eq. (2.11) | \(g_{WWZ}=-ec_w/s_w\) | agree | Same definition. |
| \(-\kappa_{Z1}Z_{\mu\nu}Z^\mu X_1^\nu\), eq. (2.12) | \(-k_{z1}F^Z_{\mu\nu}Z^\mu X_1^\nu\) | agree | Same structure. |
| \(-\kappa_{Z3}X_{1\mu}(\partial_\nu Z^\mu)Z^\nu\), eq. (2.12) | \(-k_{z3}X_{1\mu}(\partial_\nu Z^\mu)Z^\nu\) | agree | Same structure. |
| \(-\kappa_{Z5}\epsilon_{\mu\nu\rho\sigma}X_1^\mu Z^\nu\partial^\rho Z^\sigma\), eq. (2.12) | Same \(k_{z5}\epsilon XZZ\) structure | agree | Same structure. |
| No effective \(\mathcal L^\gamma_1\), after eq. (2.12) | No \(X_1\gamma\gamma\) or \(X_1gg\) term listed | agree | Matches the paper’s Landau-Yang discussion for on-shell spin-1. |
| Parity restrictions for pure \(1^-\) and \(1^+\), eqs. (2.13)-(2.14) | General \(X_1\) terms retained with independent coefficients | agree | The reconstruction describes the general implemented interaction set; the paper gives restrictions for pure-parity limits. |
| Spin-2 fermions \(-\frac1\Lambda\sum_{f=q,\ell}\kappa_fT^f_{\mu\nu}X_2^{\mu\nu}\), eq. (2.15) | \(-\frac1\Lambda X_2^{\mu\nu}[k_qT^q_{\mu\nu}+k_{q3}(T^{q_3}_{\mu\nu}+Y^q_{\mu\nu})+k_\ell(T^\ell_{\mu\nu}+Y^\ell_{\mu\nu})]\) | disagree | The paper’s eq. (2.15) uses \(\kappa_fT^f_{\mu\nu}\) for quarks/leptons; reconstruction introduces an explicit separate third-generation quark coefficient \(k_{q3}\) and separate mass-trace pieces \(Y^q,Y^\ell\). |
| Explicit QED fermion \(T^f_{\mu\nu}\), eq. (2.17), including \(-g_{\mu\nu}[\bar\psi(i\gamma^\rho D_\rho-m_f)\psi-\frac12\partial_\rho(\bar\psi i\gamma^\rho\psi)]\) and derivative terms | Symmetric kinetic tensor \(\frac i4[\bar f\gamma_\mu D_\nu f-(D_\nu\bar f)\gamma_\mu f+\mu\leftrightarrow\nu]\), plus separate mass traces for \(t,b,\tau\) | disagree | The reconstruction is not the same off-shell tensor as eq. (2.17); mass and total-derivative/\(g_{\mu\nu}\) pieces are treated differently and only some fermion masses are retained. |
| Spin-2 vectors \(-\frac1\Lambda\sum_{V=Z,W,\gamma,g}\kappa_VT^V_{\mu\nu}X_2^{\mu\nu}\), eq. (2.16) | \(-\frac1\Lambda X_2^{\mu\nu}[k_gT^g+k_aT^\gamma+k_zT^Z+k_wT^W]_{\mu\nu}\) | agree | Same coupling pattern to gluon, photon, \(Z\), and \(W\) energy-momentum tensors. |
| Explicit photon \(T^\gamma_{\mu\nu}\), eq. (2.18), containing \(\partial_\rho\partial_\sigma A^\sigma A^\rho\), \((\partial_\rho A^\rho)^2\), and \(\partial_\mu\partial_\rho A^\rho A_\nu\) terms | Maxwell form \(T^\gamma_{\mu\nu}=\frac14\eta_{\mu\nu}F^2-F_{\mu\rho}F_\nu{}^\rho\) | disagree | The reconstruction omits the derivative/gauge-fixing-like terms present in the paper’s explicit eq. (2.18). They may vanish under specific gauge/on-shell conditions but are part of the displayed paper tensor. |
| Spin-2 gluon tensor, implied by eq. (2.16) and standard E-M tensor | \(\frac14\eta_{\mu\nu}G^2-G_{\mu\rho}G_\nu{}^\rho\) | agree | This matches the standard gauge-field E-M tensor structure, up to metric-sign convention. |
| Spin-2 massive \(Z,W\) tensors, implied by eq. (2.16) and references | Proca-like \(Z\) and \(W^\pm\) stress tensors with mass terms | agree | The paper does not print these explicitly, but the reconstruction matches the expected massive-vector E-M tensor content. |
| Universal RS-like limit \(\kappa_f=\kappa_V\ \forall f,V\), eq. (2.19) | Independent \(k_q,k_{q3},k_\ell,k_g,k_a,k_z,k_w\) | agree | The reconstruction gives the general non-universal parameterization; the universal limit is obtained by setting all relevant couplings equal, modulo the extra \(k_{q3}\). |
| Non-universal quark/gluon example \(-\kappa_qT^qX_2/\Lambda-\kappa_gT^gX_2/\Lambda\), Section 4.1 eq. (4.1) | Independent \(k_q\) and \(k_g\) | agree | Matches the paper’s non-universal spin-2 discussion for quarks and gluons. |

## Disagreements and Severity

| disagreement | severity | what a human should check |
|---|---|---|
| Reconstruction sums spin-0, spin-1, and spin-2 sectors into one \(\mathcal L_{\rm HCNP}\), whereas the paper writes \(\mathcal L_{\mathrm{HC},J}\) for a chosen \(J\) sector in eq. (2.1). | convention | Check whether the implementation file intentionally contains all hypotheses simultaneously with couplings used as switches. |
| Reconstruction omits the SM-like spin-0 \(X_0ZZ\) and \(X_0W^+W^-\) mass terms proportional to \(c_\alpha\kappa_{\rm SM}\) in eq. (2.4). | substantive | Check whether those terms are present elsewhere in the implementation or whether `kSM` being unused is an extraction/reconstruction error. |
| Charged spin-0 derivative \(W\) term uses the complex coefficient on the charge-conjugate structure relative to eq. (2.4). | convention | Check the implementation’s definition of `kHdw`; it may be the complex conjugate of the paper’s \(\kappa_{H\partial W}\). |
| Spin-1 \(W1\) term has the opposite sign relative to eq. (2.11) if \(k_{w1}=\kappa_{W1}\). | substantive | Check the charged-\(W\) field naming and sign convention in the implementation, including the definition of \(W^\pm_{\mu\nu}\). |
| Spin-1 \(W2\) term has the opposite sign relative to eq. (2.11) because the charged fields carry swapped Lorentz indices contracted with antisymmetric \(X_1^{\mu\nu}\). | substantive | Check whether the implementation defines `kw2` with an implicit minus sign relative to the paper. |
| Spin-1 \(W4\) term has the opposite sign relative to eq. (2.11) for the same antisymmetric-index reason as \(W2\). | substantive | Check whether the implementation defines `kw4` with an implicit minus sign relative to the paper. |
| Spin-2 fermion sector introduces a separate \(k_{q3}\) third-generation quark coupling and extra mass-trace pieces not present in the compact paper eq. (2.15). | substantive | Check whether the implementation extends the paper’s displayed \(\kappa_q,\kappa_\ell\) structure or whether the paper’s \(\sum_f\) notation was intended to allow generation-dependent \(\kappa_f\). |
| Reconstruction’s fermion energy-momentum tensor differs from the explicit paper tensor in eq. (2.17), especially in \(g_{\mu\nu}\), mass, and total-derivative terms. | substantive | Check the exact FeynRules definition of `Tfermion` and whether equations of motion or on-shell simplifications were applied in the reconstruction. |
| Reconstruction’s photon energy-momentum tensor omits derivative terms shown explicitly in paper eq. (2.18). | substantive | Check whether the implementation uses a simplified transverse/on-shell tensor or includes the omitted terms elsewhere through gauge-fixing conventions. |
| Reconstruction retains only \(t,b,\tau\) mass-trace pieces in spin-2 fermion terms. | convention | Check whether light-fermion masses are intentionally neglected in the implementation, as is common phenomenologically. |

## Overall Assessment

The reconstruction captures the broad Higgs Characterisation model structure: a below-EWSB EFT for neutral spin-0, spin-1, and spin-2 resonance hypotheses, with scalar/pseudoscalar Yukawa and field-strength operators, vector/axial spin-1 fermion currents, anomalous \(X_1WW/X_1ZZ\) interactions, and spin-2 couplings to SM energy-momentum tensors. The main physics-level gaps are the missing SM-like scalar \(X_0ZZ/X_0WW\) mass terms, several charged \(X_1WW\) sign differences, and a spin-2 energy-momentum tensor reconstruction that is not identical to the explicit tensors printed in the paper. Some differences may be implementation conventions or on-shell simplifications, but they are important enough that a reviewer should inspect the original implementation definitions before treating the reconstruction as a faithful transcription of the paper.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 62 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

