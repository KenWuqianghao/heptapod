# Reconstructed Physics from `sanitized.fr`

## Lagrangian

The file defines
\[
\texttt{LFull}=\mathcal L_{\rm SM}+\texttt{LN},
\]
with
\[
\texttt{LN}=\texttt{LNKin}+\texttt{LNCC}+\texttt{LNNC}+\texttt{LNH}+\texttt{LNG}.
\]

The new fermions \(N_i\), \(i=1,2,3\), are self-conjugate neutral spin-\(\tfrac12\) fields. Since they are declared with \(Q=0\), \(Y=0\), no color index, and no weak-isospin index, their covariant derivative contains no gauge connection:
\[
D_\mu N_i=\partial_\mu N_i .
\]

Let \(\ell_\alpha=(e,\mu,\tau)\), \(\nu_\alpha=(\nu_e,\nu_\mu,\nu_\tau)\), and \(V_{\alpha i}\in\mathbb R\) denote the parameters
\[
V_{\alpha i}=
\begin{pmatrix}
\texttt{VeN1} & \texttt{VeN2} & \texttt{VeN3}\\
\texttt{VmuN1} & \texttt{VmuN2} & \texttt{VmuN3}\\
\texttt{VtaN1} & \texttt{VtaN2} & \texttt{VtaN3}
\end{pmatrix}.
\]
The internal coupling is
\[
g_N=\frac{e}{s_w}.
\]
Here \(P_L=\frac{1-\gamma^5}{2}\), \(P_R=\frac{1+\gamma^5}{2}\). FeynRules `ProjM` is expanded as \(P_L\), and `ProjP` as \(P_R\).

### `LNKin`

\[
\boxed{
\texttt{LNKin}
=
\sum_{i=1}^3
\left[
\frac{i}{2}\,\overline N_i\gamma^\mu\partial_\mu N_i
-
\frac{1}{2}m_{N_i}\,\overline N_i N_i
\right]
}
\]

### `LNCC`

The bare term in the file is
\[
\texttt{LNCCbare}
=
\frac{g_N}{\sqrt2}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \ell_\alpha\,W_\mu .
\]

The Lagrangian term is
\[
\boxed{
\texttt{LNCC}
=
\frac{g_N}{\sqrt2}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \ell_\alpha\,W_\mu
+\text{h.c.}
}
\]

### `LNNC`

The bare term in the file is
\[
\texttt{LNNCBare}
=
\frac{g_N}{2c_w}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \nu_\alpha\,Z_\mu .
\]

The Lagrangian term is
\[
\boxed{
\texttt{LNNC}
=
\frac{g_N}{2c_w}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \nu_\alpha\,Z_\mu
+\text{h.c.}
}
\]

### `LNH`

The bare term in the file is
\[
\texttt{LNHbare}
=
-
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline N_i P_L \nu_\alpha\,H .
\]

The Lagrangian term is
\[
\boxed{
\texttt{LNH}
=
-
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline N_i P_L \nu_\alpha\,H
+\text{h.c.}
}
\]

### `LNG`

The neutral-Goldstone part of the bare term is
\[
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline{\nu_\alpha}P_R N_i\,G^0 .
\]

The charged-Goldstone part of the bare term is
\[
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{\sqrt2 M_W}
V_{\alpha i}\,
\overline{\ell_\alpha}P_R N_i\,G^- .
\]

Thus
\[
\boxed{
\texttt{LNG}
=
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline{\nu_\alpha}P_R N_i\,G^0
+
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{\sqrt2 M_W}
V_{\alpha i}\,
\overline{\ell_\alpha}P_R N_i\,G^-
+\text{h.c.}
}
\]

## Field Table

| `.fr` class | Symbol | Spin | SU(3) rep | SU(2) rep | \(U(1)\) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `F[131]` | `N1` | \(1/2\) | singlet, no color index declared | singlet, no weak index declared | \(Q=0,\ Y=0\) | yes | `mN1 = 300.` |
| `F[132]` | `N2` | \(1/2\) | singlet, no color index declared | singlet, no weak index declared | \(Q=0,\ Y=0\) | yes | `mN2 = 500.` |
| `F[133]` | `N3` | \(1/2\) | singlet, no color index declared | singlet, no weak index declared | \(Q=0,\ Y=0\) | yes | `mN3 = 1000.` |

Widths are also declared:
\[
\texttt{WN1}=0.303,\qquad
\texttt{WN2}=1.50,\qquad
\texttt{WN3}=12.3.
\]

## Parameters

| Parameter | Type | Value | Multiplies | Physical meaning |
|---|---:|---:|---|---|
| `VeN1` | external, real | `1.0` | \(N_1\)-electron-family terms in `LNCC`, `LNNC`, `LNH`, `LNG` | mixing coefficient between \(N_1\) and the electron lepton family |
| `VeN2` | external, real | `0.0` | \(N_2\)-electron-family terms | mixing coefficient between \(N_2\) and the electron lepton family |
| `VeN3` | external, real | `0.0` | \(N_3\)-electron-family terms | mixing coefficient between \(N_3\) and the electron lepton family |
| `VmuN1` | external, real | `0.0` | \(N_1\)-muon-family terms | mixing coefficient between \(N_1\) and the muon lepton family |
| `VmuN2` | external, real | `1.0` | \(N_2\)-muon-family terms | mixing coefficient between \(N_2\) and the muon lepton family |
| `VmuN3` | external, real | `0.0` | \(N_3\)-muon-family terms | mixing coefficient between \(N_3\) and the muon lepton family |
| `VtaN1` | external, real | `0.0` | \(N_1\)-tau-family terms | mixing coefficient between \(N_1\) and the tau lepton family |
| `VtaN2` | external, real | `0.0` | \(N_2\)-tau-family terms | mixing coefficient between \(N_2\) and the tau lepton family |
| `VtaN3` | external, real | `1.0` | \(N_3\)-tau-family terms | mixing coefficient between \(N_3\) and the tau lepton family |

The file also defines one internal parameter:
\[
\texttt{gN}=\frac{\texttt{ee}}{\texttt{sw}},
\]
so the new interactions use the Standard Model weak \(SU(2)_L\) coupling normalization.

## Physics Summary

The model adds three electrically neutral, hypercharge-zero, self-conjugate spin-\(\tfrac12\) fermions \(N_1,N_2,N_3\) to the Standard Model. They are gauge singlets at the level of their kinetic terms, but interact through mixing-suppressed charged-current, neutral-current, Higgs, and Goldstone couplings to the SM lepton families.

It mediates processes such as production and decay of heavy neutral leptons through \(W^\pm\), \(Z\), and Higgs exchange, including channels \(N_i\leftrightarrow \ell_\alpha W\), \(N_i\leftrightarrow \nu_\alpha Z\), and \(N_i\leftrightarrow \nu_\alpha H\), with rates controlled by \(V_{\alpha i}\) and the masses \(m_{N_i}\).