# Reconstructed Physics from `sanitized.fr`

## Lagrangian

The file defines one new real vector field, denoted here by \(X_\mu \equiv \texttt{xb}_\mu\). It also defines two Lagrangian symbols: `LChernSimonsPortal` in the electroweak gauge basis and `LChernSimonsPortalBroken` in the broken basis.

The Higgs doublet is \(H_i\), with
\[
H^\dagger H \equiv H_i^\dagger H_i .
\]

The covariant derivative appearing in `DC[H, mu]` is the Standard Model electroweak covariant derivative on the Higgs doublet,
\[
D_\mu H
=
\left(
\partial_\mu
+ i g_w T^a W^a_\mu
+ i g_1 Y_H B_\mu
\right)H,
\qquad
Y_H=\frac12,
\qquad
T^a=\frac{\tau^a}{2}.
\]

The field strengths are
\[
B_{\lambda\rho}
=
\partial_\lambda B_\rho-\partial_\rho B_\lambda ,
\]
\[
W^a_{\lambda\rho}
=
\partial_\lambda W^a_\rho-\partial_\rho W^a_\lambda
+ g_w \epsilon^{abc} W^b_\lambda W^c_\rho .
\]

`Eps[mu,nu,la,ro]` is \(\epsilon^{\mu\nu\lambda\rho}\).

### `LChernSimonsPortal`

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortal},\,c_1}
=
c_1\,
\frac{H^\dagger_i (D_\mu H)_i}{H^\dagger_j H_j}\,
X_\nu\,
B_{\lambda\rho}\,
\epsilon^{\mu\nu\lambda\rho}
}
\]

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortal},\,c_2}
=
c_2\,
\frac{
H^\dagger_i (T^a)^i{}_{j} (D_\mu H)_j
}{
H^\dagger_k H_k
}\,
X_\nu\,
W^a_{\lambda\rho}\,
\epsilon^{\mu\nu\lambda\rho}
}
\]

### `LChernSimonsPortalBroken`

Using the `.fr` broken-basis fields \(A_\mu\), \(Z_\mu\), and the charged field \(W_\mu\) with `HC[W]` its Hermitian conjugate:

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,ZZ}
=
\frac12\,c_1\,s_w\,
X_\mu Z_\nu
\left(\partial_\lambda Z_\rho\right)
\epsilon^{\mu\nu\lambda\rho}
}
\]

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,ZA}
=
c_1\,c_w\,
X_\mu Z_\nu
\left(\partial_\lambda A_\rho\right)
\epsilon^{\mu\nu\lambda\rho}
}
\]

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,WW}
=
c_2\,
X_\mu W_\nu
\left(\partial_\lambda W_\rho^\dagger\right)
\epsilon^{\mu\nu\lambda\rho}
}
\]

Equivalently, if the FeynRules charged field `W` is the positively charged field,
\[
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,WW}
=
c_2\,
X_\mu W^+_\nu
\left(\partial_\lambda W^-_\rho\right)
\epsilon^{\mu\nu\lambda\rho}.
\]

No explicit `HC[...]` is wrapped around the full Lagrangian terms in the file, so the expressions above are the terms exactly as encoded.

## Field Table

| Symbol | FeynRules class | Spin | SU(3) rep | SU(2) rep | \(Q\) | \(Y\) | Self-conjugate | Mass |
|---|---:|---:|---|---|---:|---:|---|---|
| \(X_\mu\) / `xb` | `V[92]` | 1 | singlet, no color index declared | singlet, no weak index declared | 0 | 0 | yes | \(M_{\texttt{xb}} = 1.0\) |

The file also declares a width parameter:
\[
W_{\texttt{xb}} = 1.0 .
\]

## Parameters

| Symbol | Value | External? | Multiplies | Meaning |
|---|---:|---|---|---|
| `c1` | \(0.001\) | yes | \(\dfrac{H^\dagger D_\mu H}{H^\dagger H} X_\nu B_{\lambda\rho}\epsilon^{\mu\nu\lambda\rho}\), and in the broken basis the \(XZZ\) and \(XZ\gamma\) terms | dimensionless Chern-Simons portal coupling to the hypercharge field strength |
| `c2` | \(0.001\) | yes | \(\dfrac{H^\dagger T^a D_\mu H}{H^\dagger H} X_\nu W^a_{\lambda\rho}\epsilon^{\mu\nu\lambda\rho}\), and in the broken basis the charged \(XW^+W^-\) term | dimensionless Chern-Simons portal coupling to the weak-isospin field strength |

## Physics Summary

This is a Chern-Simons-like electroweak portal model containing a new electrically neutral, hypercharge-zero, self-conjugate massive spin-1 boson \(X_\mu\). The new vector couples through Higgs-dressed electroweak structures to the hypercharge and weak field strengths, producing anomalous-looking \(XZZ\), \(XZ\gamma\), and \(XW^+W^-\) interactions after electroweak symmetry breaking. It would mediate production or decay channels involving the new neutral vector together with electroweak gauge bosons, such as \(X \leftrightarrow Z\gamma\), \(X \leftrightarrow ZZ\), and charged \(W^+W^-\)-associated processes, depending on kinematics and how \(X\) is produced.