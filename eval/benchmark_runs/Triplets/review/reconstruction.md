# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Let the new scalar field be
\[
S_k \equiv \texttt{trip1}_k ,
\]
with color index \(k=1,2,3\). Its conjugate is \(S_k^\dagger \equiv \texttt{trip1bar}_k\). The Standard Model Higgs doublet is \(\Phi_i\).

The scalar is an \(SU(3)_c\) triplet, \(SU(2)_L\) singlet, with
\[
Y_S = Q_S = -\frac13 .
\]

The covariant derivative acting on \(S\) is
\[
D_\mu S_k
=
\partial_\mu S_k
+ i g_s G_\mu^a (T^a)_k{}^\ell S_\ell
+ i g' Y_S B_\mu S_k ,
\]
with no \(SU(2)_L\) term because \(S\) is an electroweak singlet.

### `LTripKin`

\[
\mathcal L_{\texttt{LTripKin}}
=
(D_\mu S)^\dagger_k (D^\mu S)_k
-
M_{\texttt{trip1}}^2 S_k^\dagger S_k .
\]

### `LD11`

The file defines
\[
\lambda^{QQ}_{nm} \equiv \texttt{LQQR}[n,m],
\qquad
\lambda^{UD}_{nm} \equiv \texttt{LUDL}[n,m].
\]

Using \(P_R = (1+\gamma^5)/2\), \(P_L=(1-\gamma^5)/2\), and \(u^c = C\bar u^T\), the interaction term is

\[
\mathcal L_{\texttt{LD11}}
=
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{QQ}_{nm}\,
\bar d_{n i}\,P_R\,u^c_{m j}.
\]

Because \(P_R u^c = (u_L)^c\), this is equivalently a left-chiral \(QQ\)-type diquark coupling:
\[
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{QQ}_{nm}\,
\overline{d_{L,n i}}\,(u_{L,m j})^c .
\]

The second term is

\[
\mathcal L_{\texttt{LD11}}
\supset
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{UD}_{nm}\,
\bar d_{n i}\,P_L\,u^c_{m j}.
\]

Because \(P_L u^c = (u_R)^c\), this is equivalently a right-chiral \(u_R d_R\)-type diquark coupling:
\[
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{UD}_{nm}\,
\overline{d_{R,n i}}\,(u_{R,m j})^c .
\]

Here \(i,j,k\) are color indices contracted with the antisymmetric \(SU(3)_c\) tensor \(\epsilon_{kij}\), and \(n,m\) are generation indices.

### `LD1`

\[
\mathcal L_{\texttt{LD1}}
=
\mathcal L_{\texttt{LD11}}
+
\mathcal L_{\texttt{LD11}}^\dagger .
\]

Explicitly, the hermitian conjugate contains the corresponding \(S_k\) couplings to conjugated quark bilinears.

### `LPot`

\[
\mathcal L_{\texttt{LPot}}
=
\lambda_{HS}\,
(\Phi^\dagger_i \Phi_i)\,
(S_k^\dagger S_k),
\qquad
\lambda_{HS} \equiv \texttt{LHS1}.
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{SS}\,
(S_{k_1}^\dagger S_{k_1})
(S_{k_2}^\dagger S_{k_2}),
\qquad
\lambda_{SS} \equiv \texttt{LSS11}.
\]

### `LTrip`

\[
\mathcal L_{\texttt{LTrip}}
=
\mathcal L_{\texttt{LTripKin}}
+
\mathcal L_{\texttt{LD1}}
+
\mathcal L_{\texttt{LPot}} .
\]

## Field Table

| `.fr` symbol | Particle | Spin | \(SU(3)_c\) | \(SU(2)_L\) | \(Y\) | \(Q\) | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `trip1` | complex scalar \(S\) | 0 | triplet | singlet | \(-1/3\) | \(-1/3\) | no | `Mtrip1 = 500.` |

The antiparticle is `trip1~`, represented in the Lagrangian as `trip1bar`.

## Parameters

| Symbol | Type | Value | Multiplies | Physical meaning |
|---|---:|---:|---|---|
| `LQQRR[n,m]` | external real matrix | nonzero entries: \(LQQRR_{12}=0.1\), \(LQQRR_{21}=-0.1\), \(LQQRR_{13}=0.1\), \(LQQRR_{31}=-0.1\), \(LQQRR_{23}=0.1\), \(LQQRR_{32}=-0.1\), diagonal \(0\) | real part of `LQQR[n,m]` in \(S^\dagger \bar d P_R u^c\) | real part of left-chiral \(QQ\)-type diquark coupling |
| `LQQRI[n,m]` | external real matrix | all entries \(0\) | imaginary part of `LQQR[n,m]` | imaginary part / CP phase of left-chiral diquark coupling |
| `LUDLR[n,m]` | external real matrix | \(LUDLR_{11}=LUDLR_{22}=LUDLR_{33}=0.1\), off-diagonal \(0\) | real part of `LUDL[n,m]` in \(S^\dagger \bar d P_L u^c\) | real part of right-chiral \(u_R d_R\)-type diquark coupling |
| `LUDLI[n,m]` | external real matrix | all entries \(0\) | imaginary part of `LUDL[n,m]` | imaginary part / CP phase of right-chiral diquark coupling |
| `LHS1` | external real scalar | \(1.0\) | \((\Phi^\dagger\Phi)(S^\dagger S)\) | Higgs-portal quartic coupling |
| `LSS11` | external real scalar | \(1.0\) | \((S^\dagger S)^2\) | scalar self-quartic coupling |

The internal complex couplings are
\[
\texttt{LQQR}_{nm}
=
\texttt{LQQRR}_{nm}
+
i\,\texttt{LQQRI}_{nm},
\]
\[
\texttt{LUDL}_{nm}
=
\texttt{LUDLR}_{nm}
+
i\,\texttt{LUDLI}_{nm}.
\]

## Physics Summary

This is a Standard Model extension by one complex color-triplet, electroweak-singlet scalar with electric charge \(-1/3\). It couples as a diquark to up- and down-type quarks through both left-chiral \(QQ\)-type and right-chiral \(u_R d_R\)-type bilinears, and it also has Higgs-portal and scalar self-interactions.

The model mediates baryon-number-sensitive quark-quark interactions such as resonant or virtual scalar exchange in \(u d\)-type partonic channels, including dijet production and flavor-changing quark processes depending on the generation structure of `LQQR` and `LUDL`.