# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Conventions: \(u_i^a\) and \(d_i^a\) are SM up- and down-type Dirac quarks, with generation indices \(i,j=1,2,3\) and colour indices \(a,b,c=1,2,3\). Repeated indices are summed. Charge conjugation is written as
\[
q^c \equiv C\bar q^{\,T},\qquad \overline{q^c}=(q^c)^\dagger\gamma^0 .
\]
The FeynRules object `CC[dqbar]` is therefore written as \(\overline{d_i^{c,a}}\). The colour tensor `Eps[c1,c2,c3]` is \(\epsilon_{abc}\). The model adds the hermitian conjugate of all displayed interaction terms through `HC[...]`.

Let
\[
S\equiv \texttt{SMET},\qquad
X_\mu\equiv \texttt{VMET},\qquad
\chi\equiv \texttt{FMET},
\]
\[
\phi^a\equiv \texttt{phiC},\qquad
\tilde\phi^a\equiv \texttt{tphiC},\qquad
V_\mu^a\equiv \texttt{VC}.
\]

### `L0`

\[
\boxed{
\mathcal L_{\texttt{L0}}
=
S\,
\bar u_i^a
\left[
A0FC_{ij}+B0FC_{ij}\gamma^5
\right]
u_j^a
+\text{h.c.}
}
\]

Equivalently, using chiral projectors,
\[
A0FC_{ij}+B0FC_{ij}\gamma^5
=
(A0FC_{ij}-B0FC_{ij})P_L
+
(A0FC_{ij}+B0FC_{ij})P_R .
\]

### `L1`

\[
\boxed{
\mathcal L_{\texttt{L1}}
=
X_\mu\,
\bar u_i^a\gamma^\mu
\left[
A1FC_{ij}+B1FC_{ij}\gamma^5
\right]
u_j^a
+\text{h.c.}
}
\]

Equivalently,
\[
A1FC_{ij}+B1FC_{ij}\gamma^5
=
(A1FC_{ij}-B1FC_{ij})P_L
+
(A1FC_{ij}+B1FC_{ij})P_R .
\]

### `L120`

\[
\boxed{
\mathcal L_{\texttt{L120}}
\supset
\phi^c\,\epsilon_{abc}\,
\overline{d_i^{c,a}}
\left[
AQS_{ij}+BQS_{ij}\gamma^5
\right]
d_j^b
+\text{h.c.}
}
\]

\[
\boxed{
\mathcal L_{\texttt{L120}}
\supset
\phi^a\,
\bar u_i^a
\left[
A12S_i+B12S_i\gamma^5
\right]
\chi
+\text{h.c.}
}
\]

### `L120p`

Since `$Flag4F = 1`, this term is active.

\[
\boxed{
\mathcal L_{\texttt{L120p}}
\supset
\tilde\phi^c\,\epsilon_{abc}\,
\overline{d_i^{c,a}}
\left[
tAQS_{ij}+tBQS_{ij}\gamma^5
\right]
u_j^b
+\text{h.c.}
}
\]

\[
\boxed{
\mathcal L_{\texttt{L120p}}
\supset
\tilde\phi^a\,
\bar d_i^a
\left[
tA12S_i+tB12S_i\gamma^5
\right]
\chi
+\text{h.c.}
}
\]

### `L121`

\[
\boxed{
\mathcal L_{\texttt{L121}}
\supset
V_\mu^c\,\epsilon_{abc}\,
\overline{d_i^{c,a}}\gamma^\mu
\left[
AQV_{ij}+BQV_{ij}\gamma^5
\right]
d_j^b
+\text{h.c.}
}
\]

\[
\boxed{
\mathcal L_{\texttt{L121}}
\supset
V_\mu^a\,
\bar u_i^a\gamma^\mu
\left[
A12V_i+B12V_i\gamma^5
\right]
\chi
+\text{h.c.}
}
\]

### Full `LMono`

\[
\boxed{
\mathcal L_{\texttt{LMono}}
=
\mathcal L_{\texttt{L0}}
+
\mathcal L_{\texttt{L1}}
+
\mathcal L_{\texttt{L120}}
+
\mathcal L_{\texttt{L121}}
+
\mathcal L_{\texttt{L120p}}
}
\]

The file contains no explicit `DC[...]` covariant derivatives or `FS[...]` field-strength terms. From the declared quantum numbers, all new states are \(SU(2)_L\) singlets. With convention
\[
D_\mu=\partial_\mu-i g_s G_\mu^A T_R^A-i g'Y B_\mu ,
\]
the colour-singlet neutral fields \(S\), \(X_\mu\), and \(\chi\) have \(D_\mu=\partial_\mu\). The colour-triplet fields \(\phi^a\), \(\tilde\phi^a\), and \(V_\mu^a\) use the fundamental \(SU(3)_c\) generators \(T^A\), with hypercharges \(Y=2/3\), \(-1/3\), and \(2/3\), respectively. There is no \(SU(2)_L\) gauge term.

## Field Table

| `.fr` symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)_Y\) / electric charge | Self-conjugate? | Mass |
|---|---:|---:|---:|---:|---|---|
| `FMET` | \(1/2\) | \(\mathbf 1\) | singlet | \(Y=0,\ Q=0\) | yes, Majorana-like | `MFM = 50` |
| `VMET` | \(1\) | \(\mathbf 1\) | singlet | \(Y=0,\ Q=0\) | yes, real vector | `MVM = 50.` |
| `VC` | \(1\) | \(\mathbf 3\) | singlet | \(Y=2/3,\ Q=2/3\) | no | `MVC = 500` |
| `SMET` | \(0\) | \(\mathbf 1\) | singlet | \(Y=0,\ Q=0\) | yes, real scalar | `MSM = 50` |
| `phiC` | \(0\) | \(\mathbf 3\) | singlet | \(Y=2/3,\ Q=2/3\) | no | `MSC = 1000` |
| `tphiC` | \(0\) | \(\mathbf 3\) | singlet | \(Y=-1/3,\ Q=-1/3\) | no | `tMSC = 1000` |

## Parameters

| Parameter | Multiplies | Physical meaning | Default nonzero entries |
|---|---|---|---|
| `A0FC[i,j]` | \(S\,\bar u_i u_j\) | scalar flavour-changing up-quark coupling to `SMET` | \(A0FC_{13}=A0FC_{31}=0.1\) |
| `B0FC[i,j]` | \(S\,\bar u_i\gamma^5 u_j\) | pseudoscalar up-quark coupling to `SMET` | all zero |
| `A1FC[i,j]` | \(X_\mu\,\bar u_i\gamma^\mu u_j\) | vector flavour-changing up-quark coupling to `VMET` | \(A1FC_{13}=A1FC_{31}=0.1\) |
| `B1FC[i,j]` | \(X_\mu\,\bar u_i\gamma^\mu\gamma^5 u_j\) | axial-vector up-quark coupling to `VMET` | all zero |
| `A12S[i]` | \(\phi^a\,\bar u_i^a\chi\) | scalar coupling between `phiC`, up quark, and `FMET` | \(A12S_3=0.1\) |
| `B12S[i]` | \(\phi^a\,\bar u_i^a\gamma^5\chi\) | pseudoscalar coupling between `phiC`, up quark, and `FMET` | all zero |
| `tA12S[i]` | \(\tilde\phi^a\,\bar d_i^a\chi\) | scalar coupling between `tphiC`, down quark, and `FMET` | \(tA12S_1=tA12S_2=0.1\) |
| `tB12S[i]` | \(\tilde\phi^a\,\bar d_i^a\gamma^5\chi\) | pseudoscalar coupling between `tphiC`, down quark, and `FMET` | all zero |
| `AQS[i,j]` | \(\phi^c\epsilon_{abc}\overline{d_i^{c,a}}d_j^b\) | scalar diquark coupling of `phiC` to two down quarks | \(AQS_{12}=0.1,\ AQS_{21}=-0.1\) |
| `BQS[i,j]` | \(\phi^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^5 d_j^b\) | pseudoscalar diquark coupling of `phiC` to two down quarks | all zero |
| `tAQS[i,j]` | \(\tilde\phi^c\epsilon_{abc}\overline{d_i^{c,a}}u_j^b\) | scalar diquark coupling of `tphiC` to down-up quark pair | \(tAQS_{13}=0.1,\ tAQS_{23}=0.1\) |
| `tBQS[i,j]` | \(\tilde\phi^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^5 u_j^b\) | pseudoscalar diquark coupling of `tphiC` to down-up quark pair | all zero |
| `A12V[i]` | \(V_\mu^a\,\bar u_i^a\gamma^\mu\chi\) | vector coupling between `VC`, up quark, and `FMET` | \(A12V_3=0.1\) |
| `B12V[i]` | \(V_\mu^a\,\bar u_i^a\gamma^\mu\gamma^5\chi\) | axial-vector coupling between `VC`, up quark, and `FMET` | all zero |
| `AQV[i,j]` | \(V_\mu^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^\mu d_j^b\) | vector diquark coupling of `VC` to two down quarks | \(AQV_{11}=0.1\) |
| `BQV[i,j]` | \(V_\mu^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^\mu\gamma^5 d_j^b\) | axial-vector diquark coupling of `VC` to two down quarks | all zero |

## Physics Summary

The file encodes a simplified extension of the SM with neutral missing-energy states: a real scalar `SMET`, real vector `VMET`, and self-conjugate fermion `FMET`, plus coloured scalar and vector mediators carrying \(SU(3)_c\) triplet quantum numbers. The neutral scalar/vector couple flavour off-diagonally to up-type quarks, while the coloured mediators couple both to quark pairs through antisymmetric colour contractions and to a quark plus the neutral fermion. It mediates flavour-changing up-quark processes, diquark resonances, and quark-initiated production of invisible `FMET` states through coloured scalar or vector exchange.