# Reconstructed Physics Content of `sanitized.fr`

## Conventions

Generation indices are \(n,m=1,2,3\). Fundamental color indices are \(i,j=1,2,3\). Sextet color indices are \(k,k_1,k_2=1,\dots,6\). The tensor
\[
K^{*}_{kij}\equiv \texttt{K6bar[k,i,j]}
\]
is the color Clebsch tensor contracting a color-sextet scalar with two color-triplet quarks; it is symmetric in the two fundamental color indices.

The three new scalar fields are denoted
\[
S_1^k\equiv \texttt{six1[k]},\qquad
S_2^k\equiv \texttt{six2[k]},\qquad
S_3^k\equiv \texttt{six3[k]}.
\]

FeynRules projectors are translated as
\[
\texttt{ProjP}=P_R=\frac{1+\gamma^5}{2},\qquad
\texttt{ProjM}=P_L=\frac{1-\gamma^5}{2}.
\]
The charge-conjugated spinor is
\[
q^c \equiv C\bar q^T.
\]

The scalar fields are \(SU(2)_L\) singlets. Their covariant derivative is therefore
\[
D_\mu S_a
=
\left[
\partial_\mu
+i g_s G_\mu^A (T_6^A)
+i g' Y_a B_\mu
\right]S_a ,
\]
or, after electroweak rotation,
\[
D_\mu S_a
=
\left[
\partial_\mu
+i g_s G_\mu^A (T_6^A)
+i e Q_a A_\mu
-i e Q_a \tan\theta_W Z_\mu
\right]S_a ,
\]
with \(Q_a=Y_a\) for these \(SU(2)_L\)-singlet scalars.

---

## Lagrangian

### `LSextetKin`

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu S_1)^\dagger_k(D^\mu S_1)^k
-
M_{\texttt{SIX1}}^2\,S_{1k}^\dagger S_1^k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu S_2)^\dagger_k(D^\mu S_2)^k
-
M_{\texttt{SIX2}}^2\,S_{2k}^\dagger S_2^k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu S_3)^\dagger_k(D^\mu S_3)^k
-
M_{\texttt{SIX3}}^2\,S_{3k}^\dagger S_3^k .
\]

### `LD11`

\[
\mathcal L_{\texttt{LD11}}
=
2\sqrt 2\,
K^{*}_{kij}\,
S_1^k
\left[
\lambda_{\texttt{QQ}}^{nm}\,
\bar d_{n i} P_R u^c_{m j}
+
\lambda_{\texttt{UD}}^{nm}\,
\bar d_{n i} P_L u^c_{m j}
\right],
\]
where
\[
\lambda_{\texttt{QQ}}^{nm}\equiv \texttt{LQQR[n,m]},
\qquad
\lambda_{\texttt{UD}}^{nm}\equiv \texttt{LUDL[n,m]}.
\]

### `LD1`

\[
\mathcal L_{\texttt{LD1}}
=
\mathcal L_{\texttt{LD11}}
+
\mathcal L_{\texttt{LD11}}^\dagger .
\]

### `LD21`

\[
\mathcal L_{\texttt{LD21}}
=
2\sqrt 2\,
K^{*}_{kij}\,
S_2^k\,
\lambda_{\texttt{DD}}^{nm}\,
\bar d_{n i} P_L d^c_{m j},
\]
where
\[
\lambda_{\texttt{DD}}^{nm}\equiv \texttt{LDDL[n,m]}.
\]

### `LD2`

\[
\mathcal L_{\texttt{LD2}}
=
\mathcal L_{\texttt{LD21}}
+
\mathcal L_{\texttt{LD21}}^\dagger .
\]

### `LD31`

\[
\mathcal L_{\texttt{LD31}}
=
2\sqrt 2\,
K^{*}_{kij}\,
S_3^k\,
\lambda_{\texttt{UU}}^{nm}\,
\bar u_{n i} P_L u^c_{m j},
\]
where
\[
\lambda_{\texttt{UU}}^{nm}\equiv \texttt{LUUL[n,m]}.
\]

### `LD3`

\[
\mathcal L_{\texttt{LD3}}
=
\mathcal L_{\texttt{LD31}}
+
\mathcal L_{\texttt{LD31}}^\dagger .
\]

### `LD`

\[
\mathcal L_{\texttt{LD}}
=
\mathcal L_{\texttt{LD1}}
+
\mathcal L_{\texttt{LD2}}
+
\mathcal L_{\texttt{LD3}} .
\]

### `LPot`

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{HS1}}\,
(\Phi^\dagger_i\Phi_i)\,
S_{1k}^\dagger S_1^k .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{HS2}}\,
(\Phi^\dagger_i\Phi_i)\,
S_{2k}^\dagger S_2^k .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{HS3}}\,
(\Phi^\dagger_i\Phi_i)\,
S_{3k}^\dagger S_3^k .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS11}}\,
(S_{1k_1}^\dagger S_1^{k_1})
(S_{1k_2}^\dagger S_1^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS121}}\,
(S_{1k_1}^\dagger S_1^{k_1})
(S_{2k_2}^\dagger S_2^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS122}}\,
S_{1k_1}^\dagger S_1^{k_2}
S_{2k_2}^\dagger S_2^{k_1} .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS131}}\,
(S_{1k_1}^\dagger S_1^{k_1})
(S_{3k_2}^\dagger S_3^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS132}}\,
S_{1k_1}^\dagger S_1^{k_2}
S_{3k_2}^\dagger S_3^{k_1} .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS22}}\,
(S_{2k_1}^\dagger S_2^{k_1})
(S_{2k_2}^\dagger S_2^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS231}}\,
(S_{2k_1}^\dagger S_2^{k_1})
(S_{3k_2}^\dagger S_3^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS232}}\,
S_{2k_1}^\dagger S_2^{k_2}
S_{3k_2}^\dagger S_3^{k_1} .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS33}}\,
(S_{3k_1}^\dagger S_3^{k_1})
(S_{3k_2}^\dagger S_3^{k_2}) .
\]

### `LSextet`

\[
\mathcal L_{\texttt{LSextet}}
=
\mathcal L_{\texttt{LSextetKin}}
+
\mathcal L_{\texttt{LD1}}
+
\mathcal L_{\texttt{LD2}}
+
\mathcal L_{\texttt{LD3}}
+
\mathcal L_{\texttt{LPot}} .
\]

---

## Field Table

| `.fr` class | Field symbol | Spin | \(SU(3)_C\) rep | \(SU(2)_L\) rep | \(U(1)\) charge / hypercharge | Self-conjugate? | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `six1` | \(S_1\) | 0 | \(\mathbf 6\) | \(\mathbf 1\) | \(Q=Y=1/3\) | No | `MSIX1 = 500` |
| `six2` | \(S_2\) | 0 | \(\mathbf 6\) | \(\mathbf 1\) | \(Q=Y=-2/3\) | No | `MSIX2 = 500` |
| `six3` | \(S_3\) | 0 | \(\mathbf 6\) | \(\mathbf 1\) | \(Q=Y=4/3\) | No | `MSIX3 = 500` |

---

## Parameters

| External parameter | Value in file | Multiplies | Physical meaning |
|---|---:|---|---|
| `LQQRR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LQQR[n,m]` in \(S_1\,\bar d_n P_R u_m^c\) | real part of complex diquark Yukawa coupling |
| `LQQRI[n,m]` | \(0\) | imaginary part of `LQQR[n,m]` in \(S_1\,\bar d_n P_R u_m^c\) | imaginary part / CP phase of diquark coupling |
| `LUDLR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LUDL[n,m]` in \(S_1\,\bar d_n P_L u_m^c\) | real part of complex diquark Yukawa coupling |
| `LUDLI[n,m]` | \(0\) | imaginary part of `LUDL[n,m]` in \(S_1\,\bar d_n P_L u_m^c\) | imaginary part / CP phase of diquark coupling |
| `LUULR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LUUL[n,m]` in \(S_3\,\bar u_n P_L u_m^c\) | real part of complex up-type diquark Yukawa coupling |
| `LUULI[n,m]` | \(0\) | imaginary part of `LUUL[n,m]` in \(S_3\,\bar u_n P_L u_m^c\) | imaginary part / CP phase of up-type diquark coupling |
| `LDDLR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LDDL[n,m]` in \(S_2\,\bar d_n P_L d_m^c\) | real part of complex down-type diquark Yukawa coupling |
| `LDDLI[n,m]` | \(0\) | imaginary part of `LDDL[n,m]` in \(S_2\,\bar d_n P_L d_m^c\) | imaginary part / CP phase of down-type diquark coupling |
| `LHS1` | \(0.1\) | \((\Phi^\dagger\Phi)(S_1^\dagger S_1)\) | Higgs-portal quartic coupling |
| `LHS2` | \(0.1\) | \((\Phi^\dagger\Phi)(S_2^\dagger S_2)\) | Higgs-portal quartic coupling |
| `LHS3` | \(0.1\) | \((\Phi^\dagger\Phi)(S_3^\dagger S_3)\) | Higgs-portal quartic coupling |
| `LSS11` | \(0.1\) | \((S_1^\dagger S_1)^2\) | scalar self-quartic coupling |
| `LSS121` | \(0.1\) | \((S_1^\dagger S_1)(S_2^\dagger S_2)\) | mixed scalar quartic coupling |
| `LSS122` | \(0.1\) | \(S_1^\dagger{}_{k_1}S_1^{k_2}S_2^\dagger{}_{k_2}S_2^{k_1}\) | independent color-contracted mixed scalar quartic |
| `LSS131` | \(0.1\) | \((S_1^\dagger S_1)(S_3^\dagger S_3)\) | mixed scalar quartic coupling |
| `LSS132` | \(0.1\) | \(S_1^\dagger{}_{k_1}S_1^{k_2}S_3^\dagger{}_{k_2}S_3^{k_1}\) | independent color-contracted mixed scalar quartic |
| `LSS22` | \(0.1\) | \((S_2^\dagger S_2)^2\) | scalar self-quartic coupling |
| `LSS231` | \(0.1\) | \((S_2^\dagger S_2)(S_3^\dagger S_3)\) | mixed scalar quartic coupling |
| `LSS232` | \(0.1\) | \(S_2^\dagger{}_{k_1}S_2^{k_2}S_3^\dagger{}_{k_2}S_3^{k_1}\) | independent color-contracted mixed scalar quartic |
| `LSS33` | \(0.1\) | \((S_3^\dagger S_3)^2\) | scalar self-quartic coupling |

The internal complex couplings are
\[
\texttt{LQQR}_{nm}=\texttt{LQQRR}_{nm}+i\,\texttt{LQQRI}_{nm},
\]
\[
\texttt{LUDL}_{nm}=\texttt{LUDLR}_{nm}+i\,\texttt{LUDLI}_{nm},
\]
\[
\texttt{LUUL}_{nm}=\texttt{LUULR}_{nm}+i\,\texttt{LUULI}_{nm},
\]
\[
\texttt{LDDL}_{nm}=\texttt{LDDLR}_{nm}+i\,\texttt{LDDLI}_{nm}.
\]

---

## Physics Summary

The file encodes three complex scalar color-sextet, electroweak-singlet fields with electric charges \(1/3\), \(-2/3\), and \(4/3\). They have QCD and hypercharge gauge interactions, Higgs-portal and scalar self-quartic interactions, and diquark Yukawa-type couplings to pairs of quarks through charge-conjugated spinors with explicitly chiral projectors.

The model mediates quark-quark resonant or virtual processes such as \(u d\), \(d d\), and \(u u\) scattering through scalar color-sextet exchange, with generation structure controlled by the complex matrices `LQQR`, `LUDL`, `LDDL`, and `LUUL`.