# Reconstructed Physics From `sanitized.fr`

## Lagrangian

The model defines

\[
\mathcal L_{\rm BSM}
=
\mathcal L_{\texttt{LkinWp}}
+
\mathcal L_{\texttt{LkinNuR}}
+
\mathcal L_{\texttt{LWpFermions}} .
\]

The new charged vector is denoted \(W_\mu^{\prime +}\equiv Wp_\mu\), with
\(W_\mu^{\prime -}\equiv (W_\mu^{\prime +})^\dagger\).

The file declares only electric charge for \(W'\), \(Q(W^{\prime +})=+1\), and no color or weak-isospin indices. Thus the covariant derivative acting on the new vector contains the gauge connection for its declared electric charge and no declared \(SU(3)_c\) or \(SU(2)_L\) action:

\[
D_\mu W_\nu^{\prime +}
=
\left(\partial_\mu - i e A_\mu\right) W_\nu^{\prime +},
\qquad
D_\mu W_\nu^{\prime -}
=
\left(\partial_\mu + i e A_\mu\right) W_\nu^{\prime -}.
\]

Equivalently,

\[
W_{\mu\nu}^{\prime +}
=
D_\mu W_\nu^{\prime +}
-
D_\nu W_\mu^{\prime +},
\qquad
W_{\mu\nu}^{\prime -}
=
D_\mu W_\nu^{\prime -}
-
D_\nu W_\mu^{\prime -}.
\]

### `LkinWp`

\[
\boxed{
\mathcal L_{\texttt{LkinWp}}
=
-\frac12
\left(D_\mu W_\nu^{\prime -}\right)
\left(D^\mu W^{\prime +\,\nu}\right)
+
\frac12
\left(D_\mu W_\nu^{\prime -}\right)
\left(D^\nu W^{\prime +\,\mu}\right)
+
M_{W'}^2
W_\mu^{\prime -} W^{\prime +\,\mu}
}
\]

Equivalently, up to the usual integration-by-parts form for a complex Proca field,

\[
\mathcal L_{\texttt{LkinWp}}
=
-\frac12
W_{\mu\nu}^{\prime -} W^{\prime +\,\mu\nu}
+
M_{W'}^2
W_\mu^{\prime -} W^{\prime +\,\mu}.
\]

### `LkinNuR`

The model introduces three non-self-conjugate right-handed neutrino fields
\(\nu_{R i}\), \(i=1,2,3\).

\[
\boxed{
\mathcal L_{\texttt{LkinNuR}}
=
\sum_{i=1}^{3}
\left[
i\,\overline{\nu_{R i}}\gamma^\mu \partial_\mu \nu_{R i}
-
M_{\nu_R}\,\overline{\nu_{R i}}\nu_{R i}
\right]
}
\]

This is a Dirac-type mass term as written in the file, not a Majorana term.

### `LWpQuarkNonHC`

With \(P_R=(1+\gamma^5)/2\), \(P_L=(1-\gamma^5)/2\), generation indices \(i,j=1,2,3\), and color index \(a=1,2,3\),

\[
\boxed{
\mathcal L_{\texttt{LWpQuarkNonHC}}
=
\frac{1}{\sqrt2}
\sum_{i,j=1}^{3}
\sum_{a=1}^{3}
W_\mu^{\prime +}
\left[
g_{WpR}\,e^{i\omega_{Wp}}\cos\zeta_{Wp}\,
(V^{R,q})_{ij}\,
\overline{u_i^a}\gamma^\mu P_R d_j^a
+
g_{WpL}\,\sin\zeta_{Wp}\,
(V^{L,q})_{ij}\,
\overline{u_i^a}\gamma^\mu P_L d_j^a
\right]
}
\]

The color contraction is diagonal, \(\delta_{ab}\).

### `LWpLeptonNonHC`

\[
\boxed{
\mathcal L_{\texttt{LWpLeptonNonHC}}
=
\frac{1}{\sqrt2}
\sum_{i,j=1}^{3}
W_\mu^{\prime +}
\left[
g_{WpR}\,e^{i\omega_{Wp}}\cos\zeta_{Wp}\,
(V^{R,\ell})_{ij}\,
\overline{\nu_{R i}}\gamma^\mu P_R \ell_j
+
g_{WpL}\,\sin\zeta_{Wp}\,
(V^{L,\ell})_{ij}\,
\overline{\nu_i}\gamma^\mu P_L \ell_j
\right]
}
\]

Here \(\nu_i\equiv vl_i\) is the Standard Model left-neutrino field appearing in the base model, while \(\nu_{R i}\equiv vR_i\) is the new right-handed neutrino field declared in this file.

### `LWpFermions`

The full charged-current interaction includes the Hermitian conjugate:

\[
\boxed{
\mathcal L_{\texttt{LWpFermions}}
=
\mathcal L_{\texttt{LWpQuarkNonHC}}
+
\mathcal L_{\texttt{LWpLeptonNonHC}}
+
\text{h.c.}
}
\]

Explicitly, the Hermitian conjugate contains \(W_\mu^{\prime -}\) interactions such as

\[
\frac{1}{\sqrt2}
W_\mu^{\prime -}
\,
g_{WpR}\,e^{-i\omega_{Wp}}\cos\zeta_{Wp}\,
(V^{R,q}_{ij})^*
\,
\overline{d_j^a}\gamma^\mu P_R u_i^a
\]

and analogous conjugates for the left-handed quark, right-handed lepton, and left-handed lepton currents.

## Field Table

| `.fr` class | Particle symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)\) charge / hypercharge | Self-conjugate? | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Wp` | \(W_\mu^{\prime +}\), antiparticle \(W_\mu^{\prime -}\) | 1 vector | singlet, no color index declared | not declared; no weak-isospin index | electric charge \(Q=+1\); hypercharge not declared | no | `MWp = 1000.` |
| `vR` | \(\nu_{R i}\), \(i=1,2,3\): `veR`, `vmR`, `vtR` | \(1/2\) fermion | singlet, no color index declared | not declared; no weak-isospin index | electric charge \(Q=0\); hypercharge not declared | no | `MvR = 100.` |

The vector width is declared as `WWp = 1.`. The right-handed neutrino width is declared as zero.

## Parameters

| Parameter | Value | Multiplies | Physical meaning |
|---|---:|---|---|
| `gWpL` | `0.653` | Left-chiral \(W'\) currents \(\overline u\gamma^\mu P_L d\) and \(\overline\nu\gamma^\mu P_L\ell\), with overall factor \(\sin\zeta_{Wp}\) | Left-handed charged-current coupling of \(W'\) |
| `gWpR` | `0.653` | Right-chiral \(W'\) currents \(\overline u\gamma^\mu P_R d\) and \(\overline{\nu_R}\gamma^\mu P_R\ell\), with phase \(e^{i\omega_{Wp}}\) and factor \(\cos\zeta_{Wp}\) | Right-handed charged-current coupling of \(W'\) |
| `zetaWp` | `0.` | Appears as \(\cos\zeta_{Wp}\) on right-handed currents and \(\sin\zeta_{Wp}\) on left-handed currents | Mixing angle controlling right- versus left-chiral \(W'\) couplings |
| `omegaWp` | `0.` | Appears as \(e^{i\omega_{Wp}}\) multiplying right-handed currents | CP phase in the right-handed \(W'\) coupling |
| `VpLQ[i,j]` | CKM-like real matrix | Multiplies \(\overline u_i\gamma^\mu P_L d_j\) | Left-handed quark flavor mixing matrix |
| `VpRQ[i,j]` | CKM-like real matrix | Multiplies \(\overline u_i\gamma^\mu P_R d_j\) | Right-handed quark flavor mixing matrix |
| `VpLL[i,j]` | identity matrix | Multiplies \(\overline\nu_i\gamma^\mu P_L\ell_j\) | Left-handed lepton flavor mixing matrix |
| `VpRL[i,j]` | identity matrix | Multiplies \(\overline{\nu_{R i}}\gamma^\mu P_R\ell_j\) | Right-handed lepton flavor mixing matrix |

The quark mixing matrices are initialized as

\[
V^{L,q}=V^{R,q}=
\begin{pmatrix}
0.9751 & 0.2215 & 0.0035\\
0.2210 & 0.9743 & 0.0410\\
0.0090 & 0.0400 & 1.0000
\end{pmatrix}.
\]

The lepton mixing matrices are initialized as

\[
V^{L,\ell}=V^{R,\ell}
=
\mathbf 1_{3\times 3}.
\]

## Physics Summary

This file encodes a charged massive vector boson \(W^{\prime \pm}\) and three non-self-conjugate right-handed neutrinos \(\nu_{R i}\). The \(W'\) couples to charged quark and lepton currents with independently weighted right- and left-chiral structures, controlled by \(g_{WpR}\cos\zeta_{Wp}\), \(g_{WpL}\sin\zeta_{Wp}\), flavor matrices, and a right-handed CP phase \(e^{i\omega_{Wp}}\).

The model mediates charged-current processes such as \(q\bar q'\to W^{\prime \pm}\), \(W^{\prime +}\to u_i\bar d_j\), \(W^{\prime +}\to \nu_{R i}\ell_j^+\), and the Hermitian-conjugate \(W^{\prime -}\) decays.