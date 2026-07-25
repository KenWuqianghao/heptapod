# Reconstructed Model From `sanitized.fr`

## Notation

Generation indices are \(m,\ell\). Color triplet indices are \(i,x,y,z\), adjoint color index is \(a\), and sextet index is \(k=1,\dots,6\). Repeated indices are summed.

The file defines the color tensor
\[
\mathcal C^{a}_{ki}
\equiv
\sqrt{2}\,
K_6{}_{k y z}\,
(T^a)_{z x}\,
\bar K_3{}_{i x y},
\]
with hermitian-conjugate tensor
\[
\mathcal C^{a\,*}_{ki}
=
\sqrt{2}\,
K_3{}_{i x y}\,
(T^a)_{x z}\,
\bar K_6{}_{k z y}.
\]

The FeynRules expression
\[
\frac{i}{2}\left(\gamma^\mu\gamma^\nu-\gamma^\nu\gamma^\mu\right)
\]
is written as
\[
\sigma^{\mu\nu}.
\]

Charge conjugation is
\[
q_R^c \equiv C \bar q_R^{\,T}.
\]

The fields are all \(SU(2)_L\) singlets. For a field \(\Phi_k\) in the sextet representation with hypercharge \(Y_\Phi\),
\[
D_\mu \Phi_k
=
\partial_\mu \Phi_k
+ i g_s G_\mu^a (T_6^a)_{k k'} \Phi_{k'}
+ i g' Y_\Phi B_\mu \Phi_k .
\]
For the conjugate field,
\[
D_\mu \Phi^\dagger_k
=
\partial_\mu \Phi^\dagger_k
- i g_s G_\mu^a \Phi^\dagger_{k'}(T_6^a)_{k'k}
- i g' Y_\Phi B_\mu \Phi^\dagger_k .
\]

The field strengths are
\[
G^a_{\mu\nu}=FS[G,\mu,\nu,a],
\qquad
B_{\mu\nu}=FS[B,\mu,\nu].
\]

## Lagrangian

### `LSextetKin`

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
\bar sFu_k
\left(
i\gamma^\mu D_\mu - M_{Fu}
\right)
sFu_k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
\bar sFd_k
\left(
i\gamma^\mu D_\mu - M_{Fd}
\right)
sFd_k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu sSu^\dagger_k)(D^\mu sSu_k)
-
M_{Su}^2 sSu^\dagger_k sSu_k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu sSd^\dagger_k)(D^\mu sSd_k)
-
M_{Sd}^2 sSd^\dagger_k sSd_k .
\]

The covariant derivatives use the following hypercharges:
\[
Y_{sFu}=-\frac23,\qquad
Y_{sFd}=+\frac13,\qquad
Y_{sSu}=+\frac13,\qquad
Y_{sSd}=+\frac43.
\]

### `LFu`

\[
\mathcal L_{\texttt{LFu}}
\supset
i\, C_{Fu}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFu_k\,
\sigma^{\mu\nu}
(u_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

\[
\mathcal L_{\texttt{LFu}}
\supset
i\, C_{FBu}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFu_k\,
(u_R^c)_{m i}\,
G^a_{\mu\nu}B^{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Fu}^{m}=CFuR_m+i\,CFuI_m,
\qquad
C_{FBu}^{m}=CFBuR_m+i\,CFBuI_m .
\]

### `LFd`

\[
\mathcal L_{\texttt{LFd}}
\supset
i\, C_{Fd}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFd_k\,
\sigma^{\mu\nu}
(d_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

\[
\mathcal L_{\texttt{LFd}}
\supset
i\, C_{FBd}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFd_k\,
(d_R^c)_{m i}\,
G^a_{\mu\nu}B^{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Fd}^{m}=CFdR_m+i\,CFdI_m,
\qquad
C_{FBd}^{m}=CFBdR_m+i\,CFBdI_m .
\]

### `LSu`

\[
\mathcal L_{\texttt{LSu}}
\supset
i\, C_{Su}^{m\ell}\,
\mathcal C^{a}_{ki}\,
sSu^\dagger_k\,
\bar \ell_{R\ell}\,
\sigma^{\mu\nu}
(u_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Su}^{m\ell}=CSuR_{m\ell}+i\,CSuI_{m\ell}.
\]

### `LSd`

\[
\mathcal L_{\texttt{LSd}}
\supset
i\, C_{Sd}^{m\ell}\,
\mathcal C^{a}_{ki}\,
sSd^\dagger_k\,
\bar \ell_{R\ell}\,
\sigma^{\mu\nu}
(d_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Sd}^{m\ell}=CSdR_{m\ell}+i\,CSdI_{m\ell}.
\]

### `LTot`

\[
\mathcal L_{\texttt{LTot}}
=
\mathcal L_{\texttt{LSextetKin}}
+
\mathcal L_{\texttt{LFu}}
+
\mathcal L_{\texttt{LFd}}
+
\mathcal L_{\texttt{LSu}}
+
\mathcal L_{\texttt{LSd}} .
\]

## Field Table

| Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)_Y\) | Electric charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---|---|
| `sFu` | \(1/2\) Dirac fermion | \(\mathbf 6\) | \(\mathbf 1\) | \(-2/3\) | \(-2/3\) | No | \(M_{Fu}=500\) |
| `sFd` | \(1/2\) Dirac fermion | \(\mathbf 6\) | \(\mathbf 1\) | \(+1/3\) | \(+1/3\) | No | \(M_{Fd}=500\) |
| `sSu` | scalar | \(\mathbf 6\) | \(\mathbf 1\) | \(+1/3\) | \(+1/3\) | No | \(M_{Su}=500\) |
| `sSd` | scalar | \(\mathbf 6\) | \(\mathbf 1\) | \(+4/3\) | \(+4/3\) | No | \(M_{Sd}=500\) |

The antiparticles transform in the conjugate color representation \(\bar{\mathbf 6}\) with opposite gauge charges.

## External Parameters

| External parameter | Default | Multiplies | Physical meaning |
|---|---:|---|---|
| `CFBuR[m]` | \(0.1\) | Real part of \(C_{FBu}^m\) in `LFu` | Coupling of \(\bar sFu\,u_R^c\,G_{\mu\nu}B^{\mu\nu}\) |
| `CFBuI[m]` | \(0\) | Imaginary part of \(C_{FBu}^m\) in `LFu` | CP-odd/complex phase component of the same coupling |
| `CFBdR[m]` | \(0.1\) | Real part of \(C_{FBd}^m\) in `LFd` | Coupling of \(\bar sFd\,d_R^c\,G_{\mu\nu}B^{\mu\nu}\) |
| `CFBdI[m]` | \(0\) | Imaginary part of \(C_{FBd}^m\) in `LFd` | CP-odd/complex phase component of the same coupling |
| `CFuR[m]` | \(0.1\) | Real part of \(C_{Fu}^m\) in `LFu` | Chromomagnetic-type coupling \(\bar sFu\,\sigma^{\mu\nu}u_R^c\,G^a_{\mu\nu}\) |
| `CFuI[m]` | \(0\) | Imaginary part of \(C_{Fu}^m\) in `LFu` | CP-odd/complex phase component of the same coupling |
| `CFdR[m]` | \(0.1\) | Real part of \(C_{Fd}^m\) in `LFd` | Chromomagnetic-type coupling \(\bar sFd\,\sigma^{\mu\nu}d_R^c\,G^a_{\mu\nu}\) |
| `CFdI[m]` | \(0\) | Imaginary part of \(C_{Fd}^m\) in `LFd` | CP-odd/complex phase component of the same coupling |
| `CSuR[m,l]` | \(0.1\) | Real part of \(C_{Su}^{m\ell}\) in `LSu` | Coupling of \(sSu^\dagger\,\bar\ell_R\,\sigma^{\mu\nu}u_R^c\,G^a_{\mu\nu}\) |
| `CSuI[m,l]` | \(0\) | Imaginary part of \(C_{Su}^{m\ell}\) in `LSu` | CP-odd/complex phase component of the same coupling |
| `CSdR[m,l]` | \(0.1\) | Real part of \(C_{Sd}^{m\ell}\) in `LSd` | Coupling of \(sSd^\dagger\,\bar\ell_R\,\sigma^{\mu\nu}d_R^c\,G^a_{\mu\nu}\) |
| `CSdI[m,l]` | \(0\) | Imaginary part of \(C_{Sd}^{m\ell}\) in `LSd` | CP-odd/complex phase component of the same coupling |

## Physics Summary

The file encodes four new color-sextet, electroweak-singlet states: two Dirac fermions with charges \(-2/3\) and \(+1/3\), and two complex scalars with charges \(+1/3\) and \(+4/3\). Their interactions are higher-dimensional operators coupling them to right-handed charge-conjugated up- or down-type quarks, gluon field strengths, and in two fermion operators also the hypercharge field strength.

The model mediates processes involving color-sextet resonances connected to quarks plus gluons, and scalar sextet interactions involving a charged right-handed lepton, a charge-conjugated right-handed quark, and a gluon. These operators can generate exotic colored-particle production and decays into quark-gluon or lepton-quark-gluon final states, with generation-dependent complex couplings.