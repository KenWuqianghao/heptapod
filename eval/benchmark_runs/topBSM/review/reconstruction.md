# Reconstructed Physics from `sanitized.fr`

## Lagrangian

Conventions: \(G^a_{\mu\nu}\equiv\mathrm{FS}[G,\mu,\nu,a]\), \(\widetilde G^{a\mu\nu}=\frac12\epsilon^{\mu\nu\rho\sigma}G^a_{\rho\sigma}\), \(T^a\) are fundamental \(SU(3)_c\) generators, and \(d^{abc}\equiv\mathrm{dSUN}[a,b,c]\). Flavor indices are summed where present. The file defines
\[
g_Z \equiv \frac{e}{s_W c_W},\qquad e\,t_W \equiv \frac{e s_W}{c_W}.
\]

No `DC[...]` covariant derivatives appear explicitly in the interaction Lagrangian. From the declared gauge quantum numbers, \(S0,S1,S2\) are color and electroweak singlets with \(D_\mu=\partial_\mu\). \(O0^a,O1_\mu^a\) are color adjoints with \(Y=Q=0\), so if their kinetic terms are supplied elsewhere the QCD covariant derivative is
\[
(D_\mu X)^a=\partial_\mu X^a+g_s f^{abc}G^b_\mu X^c,
\]
with no \(SU(2)_L\) or \(U(1)_Y\) gauge piece.

### `LS0top`

\[
\mathcal L_{\mathrm{S0top}}
=
s0scalar\,\frac{m_t}{v}\,S0\,\bar t t
+
i\,s0axial\,\frac{m_t}{v}\,S0\,\bar t\gamma^5 t .
\]

### `LS0ggfusionScalar`

\[
\mathcal L_{\mathrm{S0ggfusionScalar}}
=
-\frac14\,s0fusionScalar\,S0\,G^a_{\mu\nu}G^{a\mu\nu}.
\]

### `LS0ggfusionAxial`

\[
\mathcal L_{\mathrm{S0ggfusionAxial}}
=
-\frac14\,s0fusionAxial\,S0\,G^a_{\mu\nu}\widetilde G^{a\mu\nu}.
\]

### `LS0ggfusion`

\[
\mathcal L_{\mathrm{S0ggfusion}}
=
\mathcal L_{\mathrm{S0ggfusionScalar}}
+
\mathcal L_{\mathrm{S0ggfusionAxial}} .
\]

### `LS0`

\[
\mathcal L_{\mathrm{S0}}
=
\mathcal L_{\mathrm{S0top}}
+
\mathcal L_{\mathrm{S0ggfusion}} .
\]

### `LO0top`

\[
\mathcal L_{\mathrm{O0top}}
=
o0scalar\,\frac{m_t}{v}\,O0^a\,\bar t\,T^a t
+
i\,o0axial\,\frac{m_t}{v}\,O0^a\,\bar t\,\gamma^5 T^a t .
\]

### `LO0ggfusionScalar`

\[
\mathcal L_{\mathrm{O0ggfusionScalar}}
=
-\frac14\,o0fusionScalar\,d^{abc}\,O0^a\,G^b_{\mu\nu}G^{c\mu\nu}.
\]

### `LO0ggfusionAxial`

\[
\mathcal L_{\mathrm{O0ggfusionAxial}}
=
-\frac14\,o0fusionAxial\,d^{abc}\,O0^a\,G^b_{\mu\nu}\widetilde G^{c\mu\nu}.
\]

### `LO0ggfusion`

\[
\mathcal L_{\mathrm{O0ggfusion}}
=
\mathcal L_{\mathrm{O0ggfusionScalar}}
+
\mathcal L_{\mathrm{O0ggfusionAxial}} .
\]

### `LO0`

\[
\mathcal L_{\mathrm{O0}}
=
\mathcal L_{\mathrm{O0top}}
+
\mathcal L_{\mathrm{O0ggfusion}} .
\]

### `LS1ul`

\[
\mathcal L_{\mathrm{S1ul}}
=
-\,s1uleft\,g_Z
\left(-\frac12+\frac23 s_W^2\right)
S1_\mu\,
\bar u_{L\,f c}\gamma^\mu u_L^{f c}.
\]

### `LS1dl`

\[
\mathcal L_{\mathrm{S1dl}}
=
-\,s1dleft\,g_Z
\left(\frac12-\frac13 s_W^2\right)
S1_\mu\,
\bar d_{L\,f c}\gamma^\mu d_L^{f c}.
\]

### `LS1ur`

\[
\mathcal L_{\mathrm{S1ur}}
=
-\,s1uright\,
\frac23\,e t_W\,
S1_\mu\,
\bar u_{R\,f c}\gamma^\mu u_R^{f c}.
\]

### `LS1dr`

\[
\mathcal L_{\mathrm{S1dr}}
=
+\,s1dright\,
\frac13\,e t_W\,
S1_\mu\,
\bar d_{R\,f c}\gamma^\mu d_R^{f c}.
\]

### `LS1el`

\[
\mathcal L_{\mathrm{S1el}}
=
-\,s1eleft\,g_Z
\left(\frac12-s_W^2\right)
S1_\mu\,
\bar e_{L\,f}\gamma^\mu e_L^f.
\]

### `LS1nu`

\[
\mathcal L_{\mathrm{S1nu}}
=
+\,s1nu\,\frac{g_Z}{2}\,
S1_\mu\,
\bar\nu_{L\,f}\gamma^\mu \nu_L^f.
\]

### `LS1er`

\[
\mathcal L_{\mathrm{S1er}}
=
+\,s1eright\,e t_W\,
S1_\mu\,
\bar e_{R\,f}\gamma^\mu e_R^f.
\]

### `LS1`

\[
\mathcal L_{\mathrm{S1}}
=
\mathcal L_{\mathrm{S1ul}}
+\mathcal L_{\mathrm{S1dl}}
+\mathcal L_{\mathrm{S1ur}}
+\mathcal L_{\mathrm{S1dr}}
+\mathcal L_{\mathrm{S1el}}
+\mathcal L_{\mathrm{S1er}}
+\mathcal L_{\mathrm{S1nu}} .
\]

### `LO1ul`

\[
\mathcal L_{\mathrm{O1ul}}
=
o1uleft\,g_s\,
O1^a_\mu\,
\bar u_{L\,f c_1}\gamma^\mu
T^a_{c_1c_2}
u_L^{f c_2}.
\]

### `LO1dl`

\[
\mathcal L_{\mathrm{O1dl}}
=
o1dleft\,g_s\,
O1^a_\mu\,
\bar d_{L\,f c_1}\gamma^\mu
T^a_{c_1c_2}
d_L^{f c_2}.
\]

### `LO1ur`

\[
\mathcal L_{\mathrm{O1ur}}
=
o1uright\,g_s\,
O1^a_\mu\,
\bar u_{R\,f c_1}\gamma^\mu
T^a_{c_1c_2}
u_R^{f c_2}.
\]

### `LO1dr`

\[
\mathcal L_{\mathrm{O1dr}}
=
o1dright\,g_s\,
O1^a_\mu\,
\bar d_{R\,f c_1}\gamma^\mu
T^a_{c_1c_2}
d_R^{f c_2}.
\]

### `LO1`

\[
\mathcal L_{\mathrm{O1}}
=
\mathcal L_{\mathrm{O1ul}}
+\mathcal L_{\mathrm{O1dl}}
+\mathcal L_{\mathrm{O1ur}}
+\mathcal L_{\mathrm{O1dr}} .
\]

## Field table

| `.fr` class | Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)\) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `S[21]` | `S0` | 0 | singlet | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MS0 = 400` |
| `S[22]` | `O0[a]` | 0 | adjoint, index `Gluon` | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MO0 = 400` |
| `V[7]` | `S1[mu]` | 1 | singlet | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MS1 = 2000` |
| `V[8]` | `O1[mu,a]` | 1 | adjoint, index `Gluon` | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MO1 = 2000` |
| `T[1]` | `S2` | 2 | singlet | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MS2 = 500` |

## Parameters

| External parameter | Value | Multiplies | Physical meaning |
|---|---:|---|---|
| `s0scalar` | 1 | \(S0\,\bar t t\), and internally `s0fusionScalar` | CP-even scalar coupling of color-singlet spin-0 state `S0` to top quarks; also controls loop-induced scalar gluon-fusion operator |
| `s0axial` | 1 | \(iS0\,\bar t\gamma^5 t\), and internally `s0fusionAxial` | CP-odd pseudoscalar coupling of `S0` to top quarks; also controls loop-induced dual-gluon operator |
| `o0scalar` | 1 | \(O0^a\bar tT^a t\), and internally `o0fusionScalar` | CP-even scalar coupling of color-octet spin-0 state `O0` to top quarks; also controls loop-induced \(d^{abc}O0^aG^bG^c\) operator |
| `o0axial` | 1 | \(iO0^a\bar t\gamma^5T^a t\), and internally `o0fusionAxial` | CP-odd pseudoscalar coupling of `O0` to top quarks; also controls loop-induced \(d^{abc}O0^aG^b\widetilde G^c\) operator |
| `s1uright` | 1 | `LS1ur` | Right-handed up-type quark coupling of neutral color-singlet vector `S1` |
| `s1uleft` | 1 | `LS1ul` | Left-handed up-type quark coupling of `S1` |
| `s1dright` | 1 | `LS1dr` | Right-handed down-type quark coupling of `S1` |
| `s1dleft` | 1 | `LS1dl` | Left-handed down-type quark coupling of `S1` |
| `s1eright` | 1 | `LS1er` | Right-handed charged-lepton coupling of `S1` |
| `s1eleft` | 1 | `LS1el` | Left-handed charged-lepton coupling of `S1` |
| `s1nu` | 1 | `LS1nu` | Left-handed neutrino coupling of `S1` |
| `o1uright` | 1 | `LO1ur` | Right-handed up-type quark coupling of color-octet vector `O1` |
| `o1uleft` | 1 | `LO1ul` | Left-handed up-type quark coupling of `O1` |
| `o1dright` | 1 | `LO1dr` | Right-handed down-type quark coupling of `O1` |
| `o1dleft` | 1 | `LO1dl` | Left-handed down-type quark coupling of `O1` |

Internal parameters `s0fusionScalar`, `s0fusionAxial`, `o0fusionScalar`, and `o0fusionAxial` are loop-form-factor coefficients built from the corresponding top couplings, \(g_s\), \(v\), and the spin-0 mass. Internal widths are `WS0`, `WO0`, `WS1`, and `WO1`. The tensor field `S2` has a fixed width declaration `WS2 = 2`, but no interactions are defined for it in the file.

## Physics summary

The file encodes neutral color-singlet and color-octet spin-0 and spin-1 resonances, plus a neutral singlet spin-2 state with no listed interactions. The spin-0 states couple to top quarks through scalar and pseudoscalar Yukawa-like terms and to gluons through effective \(GG\) and \(G\widetilde G\) operators, while the spin-1 states couple chirally to Standard Model fermion currents: the singlet vector to quarks and leptons with electroweak-charge-weighted coefficients, and the octet vector to quark color currents. These interactions mediate resonance production in gluon fusion or quark annihilation and decays to \(t\bar t\), dijets, charged leptons, and neutrinos depending on the state and coupling choices.