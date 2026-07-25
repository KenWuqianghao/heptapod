# Reconstructed Physics From `sanitized.fr`

## Lagrangian

The total Lagrangian defined in the file is
\[
\mathcal L_{\rm Tot}
=
\mathcal L_{\rm ZpF}
+\mathcal L_{\rm PhiXKin}
+\mathcal L_{\rm HiggsX}
-V_{\rm PhiX}
+\mathcal L_{\rm NuDiracYuk}
+\mathcal L_{\rm NuDiracYuk}^{\dagger}
+\mathcal L_{\rm NuMajoranaYuk}.
\]

The new Abelian covariant derivative convention used by the file is
\[
D_\mu = D_\mu^{\rm SM} + i g_X q_X Z'_\mu ,
\]
where, for the SM Higgs doublet,
\[
D_\mu^{\rm SM} H
=
\left(
\partial_\mu
+i g\, W_\mu^a T^a
+i g'\, Y_H B_\mu
\right)H .
\]
For the singlet scalar \(\Phi_X\), only the new \(U(1)_X\) gauge field appears:
\[
D_\mu \Phi_X =
\left(\partial_\mu+i g_X q_X^\Phi Z'_\mu\right)\Phi_X .
\]

The chiral projectors are
\[
P_L=\frac{1-\gamma^5}{2},\qquad
P_R=\frac{1+\gamma^5}{2}.
\]

### `LZpF`

\[
\mathcal L_{\rm ZpF}
=
-g_X Z'_\mu
\sum_{f=1}^{3}
\left[
q_X^Q
\left(
\bar u_f \gamma^\mu P_L u_f
+
\bar d_f \gamma^\mu P_L d_f
\right)
+
q_X^u \bar u_f \gamma^\mu P_R u_f
+
q_X^d \bar d_f \gamma^\mu P_R d_f
\right.
\]
\[
\left.
+
q_X^L
\left(
\bar\nu_f \gamma^\mu P_L \nu_f
+
\bar e_f \gamma^\mu P_L e_f
\right)
+
q_X^e \bar e_f \gamma^\mu P_R e_f
+
q_X^N \bar N_f \gamma^\mu P_R N_f
\right].
\]

Color indices are summed for the quark bilinears. Generation index \(f=1,2,3\) is summed.

The \(U(1)_X\) charges are defined internally as
\[
q_X^Q=\frac{x_H}{6}+\frac{x_\Phi}{3},
\qquad
q_X^u=\frac{2x_H}{3}+\frac{x_\Phi}{3},
\qquad
q_X^d=-\frac{x_H}{3}+\frac{x_\Phi}{3},
\]
\[
q_X^L=-\frac{x_H}{2}-x_\Phi,
\qquad
q_X^e=-x_H-x_\Phi,
\qquad
q_X^N=-x_\Phi,
\]
\[
q_X^H=-\frac{x_H}{2},
\qquad
q_X^\Phi=2x_\Phi .
\]

### `LPhiXKin`

\[
\mathcal L_{\rm PhiXKin}
=
\partial_\mu \Phi_X^\dagger \partial^\mu \Phi_X
+
i g_X q_X^\Phi Z'_\mu
\left(
\Phi_X^\dagger \partial^\mu \Phi_X
-
\partial^\mu \Phi_X^\dagger \Phi_X
\right)
+
g_X^2 (q_X^\Phi)^2 Z'_\mu Z'^\mu \Phi_X^\dagger \Phi_X .
\]

Equivalently,
\[
\mathcal L_{\rm PhiXKin}
=
(D_\mu \Phi_X)^\dagger D^\mu \Phi_X ,
\qquad
D_\mu \Phi_X=
(\partial_\mu+i g_X q_X^\Phi Z'_\mu)\Phi_X .
\]

The field definition is
\[
\Phi_X
=
\frac{1}{\sqrt 2}
\left(
v_\Phi+\phi_X+iG_{Z'}
\right),
\qquad
v_\Phi=\frac{M_{Z'}}{2g_X}.
\]

### `LHiggsX`

\[
\mathcal L_{\rm HiggsX}
=
i g_X q_X^H Z'_\mu
\left[
H^\dagger D_{\rm SM}^\mu H
-
(D_{\rm SM}^\mu H)^\dagger H
\right]
+
g_X^2 (q_X^H)^2 Z'_\mu Z'^\mu H^\dagger H .
\]

This is the \(U(1)_X\)-dependent part of
\[
(D_\mu H)^\dagger D^\mu H,
\qquad
D_\mu H=
D_\mu^{\rm SM}H+i g_X q_X^H Z'_\mu H .
\]

### `VPhiX`

The file defines
\[
V_{\rm PhiX}
=
m_\Phi^2\, \Phi_X^\dagger \Phi_X
+
\lambda_\Phi
(\Phi_X^\dagger \Phi_X)^2
+
\lambda'
(H^\dagger H)(\Phi_X^\dagger \Phi_X).
\]

It enters the total Lagrangian as
\[
\mathcal L \supset -V_{\rm PhiX}.
\]

### `LNuDiracYuk`

\[
\mathcal L_{\rm NuDiracYuk}
=
-
\sum_{i,j=1}^{3}
(Y_\nu)_{ij}\,
\bar L_i\, P_R N_j\, H^\dagger
\]

with the \(SU(2)\) index contracted as written in the file:
\[
\mathcal L_{\rm NuDiracYuk}
=
-
(Y_\nu)_{ij}\,
\bar L_{i,a}\,P_R N_j\,H_a^\dagger .
\]

The total Lagrangian also includes its Hermitian conjugate:
\[
\mathcal L_{\rm NuDiracYuk}^\dagger
=
-
(Y_\nu)_{ij}^*\,
H_a\,\bar N_j P_L L_{i,a}.
\]

The file declares \(Y_\nu\) real, so \(Y_\nu^*=Y_\nu\).

### `LNuMajoranaYuk`

\[
\mathcal L_{\rm NuMajoranaYuk}
=
-\frac12
\sum_{i=1}^{3}
Y_{N_i}\,
\Phi_X\,
\bar N_i P_R N_i
-
\frac12
\sum_{i=1}^{3}
Y_{N_i}\,
\Phi_X^\dagger\,
\bar N_i P_L N_i .
\]

Equivalently, in two-component chiral notation,
\[
\mathcal L_{\rm NuMajoranaYuk}
=
-\frac12
\sum_i
Y_{N_i}\,
\Phi_X\,
\overline{N_{Ri}^{\,c}}\,N_{Ri}
+\text{h.c.}
\]

The internal Yukawa definitions are
\[
Y_{N_i}=\frac{\sqrt2\,m_{N_i}}{v_\Phi}.
\]

## Field Table

| `.fr` class | Symbol | Spin | SU(3) | SU(2) | \(U(1)\) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---|---:|---|
| `V[100]` | `Zp` \((Z'_\mu)\) | 1 | singlet | singlet | gauge boson of \(U(1)_X\); no matter charge assigned | yes | \(M_{Z'}=\texttt{MZp}=7500\) |
| `F[101]` | `NR` \((N_1,N_2,N_3)\) | 1/2 | singlet | singlet | right-chiral component has \(q_X^N=-x_\Phi\) | yes, Majorana | \(m_{N_1}=m_{N_2}=m_{N_3}=10000\) |
| `S[102]` | `phiX` \((\phi_X)\) | 0 | singlet | singlet | real excitation of \(\Phi_X\), whose parent has \(X=2x_\Phi\), \(Q=0\), \(Y=0\) | yes | \(m_{\phi_X}=1000\) |
| `S[103]` | `GZp` \((G_{Z'})\) | 0 | singlet | singlet | Goldstone component of \(\Phi_X\), whose parent has \(X=2x_\Phi\), \(Q=0\), \(Y=0\) | yes | \(M_{Z'}=7500\) |
| `S[104]` | `PhiX` \((\Phi_X)\) | 0 | singlet | singlet | \(Q=0,\;Y=0,\;X=2x_\Phi\) | no | unphysical field, \(\Phi_X=(v_\Phi+\phi_X+iG_{Z'})/\sqrt2\) |

## Parameters

| Parameter | Value in file | Multiplies / controls | Physical meaning |
|---|---:|---|---|
| `gX` | \(0.1\) | every \(Z'\) interaction and \(U(1)_X\) covariant derivative | new Abelian gauge coupling |
| `xH` | \(0\) | internal charge definitions \(q_X^Q,q_X^u,q_X^d,q_X^L,q_X^e,q_X^H\) | coefficient controlling the hypercharge-like part of the \(U(1)_X\) charge assignment |
| `xPhi` | \(1\) | internal charge definitions, especially \(q_X^\Phi=2x_\Phi\) and \(q_X^N=-x_\Phi\) | coefficient controlling the singlet-scalar and right-handed-neutrino \(U(1)_X\) charge normalization |
| `lamPhi` | \(0.1\) | \((\Phi_X^\dagger\Phi_X)^2\) in `VPhiX` | quartic self-coupling of the new complex singlet scalar |
| `lamHP` | \(0\) | \((H^\dagger H)(\Phi_X^\dagger\Phi_X)\) in `VPhiX` | Higgs-portal quartic coupling |
| `mPhi2` | \(1000000\) | \(\Phi_X^\dagger\Phi_X\) in `VPhiX` | quadratic scalar-potential mass parameter for \(\Phi_X\) |
| `yNu[i,j]` | all entries \(0\) | \(- (Y_\nu)_{ij}\bar L_i P_R N_j H^\dagger+\text{h.c.}\) | Dirac neutrino Yukawa matrix coupling SM lepton doublets to the new Majorana singlets |

The file also defines the following internal parameters:
\[
v_\Phi=\frac{M_{Z'}}{2g_X},
\qquad
Y_{N_i}=\frac{\sqrt2\,m_{N_i}}{v_\Phi}.
\]

## Physics Summary

The file encodes a \(U(1)_X\) extension of the Standard Model with a new neutral gauge boson \(Z'\), three self-conjugate singlet fermions \(N_i\), and a complex singlet scalar \(\Phi_X\) whose vacuum expectation value breaks the new gauge symmetry and supplies the \(Z'\) and \(N_i\) masses. The \(Z'\) couples chirally to SM quarks, charged leptons, neutrinos, and the right-handed component of the Majorana singlets with charges determined by \(x_H\) and \(x_\Phi\).

It mediates dilepton, dijet, neutrino, and heavy-neutral-lepton production through \(s\)-channel \(Z'\) exchange, while the scalar sector allows singlet-Higgs portal interactions and Majorana mass generation through \(\Phi_X \overline{N_R^c}N_R\).