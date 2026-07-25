# Reconstructed Physics from `sanitized.fr`

## Lagrangian

The file defines two sterile left-handed Weyl fields, `N1L` and `N2L`, both electroweak and color singlets:
\[
SU(3)_c:\mathbf{1},\qquad SU(2)_L:\mathbf{1},\qquad Y=0,\qquad Q=0 .
\]
Therefore their covariant derivative contains no gauge connection:
\[
D_\mu N_{1L,2L}=\partial_\mu N_{1L,2L}.
\]

The physical Majorana fields are `n4` and `n5`, with
\[
N_{1L}=\frac{i\,n_4+n_5}{\sqrt{2}},
\]
and
\[
N_{2L}
=
-\theta_e\,\nu_e-\theta_\mu\,\nu_\mu-\theta_\tau\,\nu_\tau
-\frac{i}{\sqrt{2}}\left(1-\frac{\theta^2}{2}\right)n_4
+\frac{1}{\sqrt{2}}\left(1-\frac{\theta^2}{2}\right)n_5,
\]
where
\[
\theta^2=\theta_e^2+\theta_\mu^2+\theta_\tau^2.
\]

The active neutrino combinations used in the Yukawa terms are, to second order in the mixings,
\[
\nu'_e
=
\left(1-\frac{\theta_e^2}{2}\right)\nu_e
-\frac{\theta_e\theta_\mu}{2}\nu_\mu
-\frac{\theta_e\theta_\tau}{2}\nu_\tau
-\frac{i\theta_e}{\sqrt{2}}n_4
+\frac{\theta_e}{\sqrt{2}}n_5 ,
\]
\[
\nu'_\mu
=
-\frac{\theta_\mu\theta_e}{2}\nu_e
+\left(1-\frac{\theta_\mu^2}{2}\right)\nu_\mu
-\frac{\theta_\mu\theta_\tau}{2}\nu_\tau
-\frac{i\theta_\mu}{\sqrt{2}}n_4
+\frac{\theta_\mu}{\sqrt{2}}n_5 ,
\]
\[
\nu'_\tau
=
-\frac{\theta_\tau\theta_e}{2}\nu_e
-\frac{\theta_\tau\theta_\mu}{2}\nu_\mu
+\left(1-\frac{\theta_\tau^2}{2}\right)\nu_\tau
-\frac{i\theta_\tau}{\sqrt{2}}n_4
+\frac{\theta_\tau}{\sqrt{2}}n_5 .
\]

Here `ProjM` is the left-handed projector,
\[
P_L=\frac{1-\gamma^5}{2},
\]
`HC[...]` denotes the Hermitian conjugate, and `CC[...]` denotes charge conjugation.

### `LKineticSterile`

\[
\mathcal{L}_{\texttt{LKineticSterile}}
=
i\,\overline{N_{1L}}\gamma^\mu \partial_\mu N_{1L}
+
i\,\overline{N_{2L}}\gamma^\mu \partial_\mu N_{2L}.
\]

### `YukawaNP`

Define
\[
y_e=\frac{M_{\rm maj}\theta_e}{v},\qquad
y_\mu=\frac{M_{\rm maj}\theta_\mu}{v},\qquad
y_\tau=\frac{M_{\rm maj}\theta_\tau}{v}.
\]

With the Higgs doublet written as
\[
\Phi =
\begin{pmatrix}
\Phi_1\\
\Phi_2
\end{pmatrix},
\]
the file encodes
\[
\mathcal{L}_{\texttt{YukawaNP}}
=
y_e
\left[
\frac{-\overline{n_4}P_L\nu'_e+i\,\overline{n_5}P_L\nu'_e}{\sqrt{2}}\,\Phi_2
-
\frac{-\overline{n_4}P_L e+i\,\overline{n_5}P_L e}{\sqrt{2}}\,\Phi_1
\right]
\]
\[
+
y_\mu
\left[
\frac{-\overline{n_4}P_L\nu'_\mu+i\,\overline{n_5}P_L\nu'_\mu}{\sqrt{2}}\,\Phi_2
-
\frac{-\overline{n_4}P_L \mu+i\,\overline{n_5}P_L \mu}{\sqrt{2}}\,\Phi_1
\right]
\]
\[
+
y_\tau
\left[
\frac{-\overline{n_4}P_L\nu'_\tau+i\,\overline{n_5}P_L\nu'_\tau}{\sqrt{2}}\,\Phi_2
-
\frac{-\overline{n_4}P_L \tau+i\,\overline{n_5}P_L \tau}{\sqrt{2}}\,\Phi_1
\right].
\]

Equivalently, using \(L_\alpha=(\nu'_\alpha,\ell_\alpha)^T\),
\[
\mathcal{L}_{\texttt{YukawaNP}}
=
\sum_{\alpha=e,\mu,\tau}
y_\alpha\,
\frac{-\overline{n_4}+i\overline{n_5}}{\sqrt{2}}\,
P_L
\left(
\nu'_\alpha \Phi_2-\ell_\alpha \Phi_1
\right),
\]
with the \(SU(2)_L\) contraction corresponding to the usual antisymmetric contraction with the Higgs doublet.

### `LNP`

The new-physics Lagrangian is
\[
\mathcal{L}_{\texttt{LNP}}
=
-
M_{\rm maj}\,
\overline{N_{1L}^{\,c}}\,
N_{2L}
+
\mathcal{L}_{\texttt{YukawaNP}}
+
\text{h.c.}
\]

That is,
\[
\mathcal{L}_{\texttt{LNP}}
=
-
M_{\rm maj}\,
\overline{N_{1L}^{\,c}}\,
N_{2L}
-
M_{\rm maj}\,
\overline{N_{2L}}\,
N_{1L}^{\,c}
+
\mathcal{L}_{\texttt{YukawaNP}}
+
\mathcal{L}_{\texttt{YukawaNP}}^\dagger .
\]

All terms are truncated by `RemoveHigherOrder` to second order in
\[
\theta_e,\theta_\mu,\theta_\tau .
\]

### `LTot`

\[
\mathcal{L}_{\texttt{LTot}}
=
\mathcal{L}_{\texttt{LKineticSterile}}
+
\mathcal{L}_{\texttt{LNP}}.
\]

## Field Table

| `.fr` class | Symbol / members | Spin | \(SU(3)_c\) | \(SU(2)_L\) | \(U(1)_Y\) / \(Q\) | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---|
| `F[100]` | `nH = {n4,n5}` | \(1/2\) | not declared; singlet by construction | not declared; singlet by construction | neutral | yes | `MN = {Mn4,Mn5}` |
| `W[100]` | `N1L` | left-handed Weyl \(1/2\) | singlet | singlet | \(Y=0,\ Q=0\) | no | unphysical |
| `W[101]` | `N2L` | left-handed Weyl \(1/2\) | singlet | singlet | \(Y=0,\ Q=0\) | no | unphysical |

The physical Majorana masses are internal parameters:
\[
M_{n4}=M_{\rm maj}\left(1+\frac{\theta^2}{2}\right)-\frac{\Delta m}{2},
\]
\[
M_{n5}=M_{\rm maj}\left(1+\frac{\theta^2}{2}\right)+\frac{\Delta m}{2}.
\]

With the default numerical inputs,
\[
M_{\rm maj}=100,\qquad
\Delta m=10^{-12},\qquad
\theta_e=0,\quad \theta_\mu=10^{-3},\quad \theta_\tau=0,
\]
so
\[
\theta^2=10^{-6},
\]
\[
M_{n4}=100.00005-5\times 10^{-13},
\]
\[
M_{n5}=100.00005+5\times 10^{-13}.
\]

## Parameters

| Parameter | Type | Default value | Appears in | Physical meaning |
|---|---:|---:|---|---|
| `Mmaj` | external real | \(100\) | `LNP`, `yvn`, `Mn4`, `Mn5` | Common sterile mass scale; multiplies \(-\overline{N_{1L}^c}N_{2L}\) and sets the active-sterile Yukawa strengths \(y_\alpha=M_{\rm maj}\theta_\alpha/v\). |
| `deltaM` | external real | \(10^{-12}\) | `Mn4`, `Mn5` | Small mass splitting between the two heavy Majorana states. |
| `theta1` | external real | \(0\) | `yvn[1]`, `UnCL`, `Un`, `Mn4`, `Mn5` through \(\theta^2\) | Electron-flavor active-sterile mixing angle \(\theta_e\). |
| `theta2` | external real | \(10^{-3}\) | `yvn[2]`, `UnCL`, `Un`, `Mn4`, `Mn5` through \(\theta^2\) | Muon-flavor active-sterile mixing angle \(\theta_\mu\). |
| `theta3` | external real | \(0\) | `yvn[3]`, `UnCL`, `Un`, `Mn4`, `Mn5` through \(\theta^2\) | Tau-flavor active-sterile mixing angle \(\theta_\tau\). |
| `damping` | external real | \(0\) | not used in the displayed Lagrangian | Declared external parameter with no role in `LKineticSterile`, `YukawaNP`, `LNP`, or `LTot`. |

The internal Yukawa parameters are
\[
\texttt{yvn[1]}=y_e=\frac{M_{\rm maj}\theta_e}{v},
\]
\[
\texttt{yvn[2]}=y_\mu=\frac{M_{\rm maj}\theta_\mu}{v},
\]
\[
\texttt{yvn[3]}=y_\tau=\frac{M_{\rm maj}\theta_\tau}{v}.
\]

## Physics Summary

The file encodes an extension of the Standard Model by two nearly degenerate neutral Majorana fermions, `n4` and `n5`, built from two sterile left-handed singlets and mixed with the three active neutrino flavors through small real parameters \(\theta_e,\theta_\mu,\theta_\tau\). The new interactions are sterile-neutrino Yukawa couplings to the SM lepton doublets and Higgs doublet, plus a sterile mass term producing a pseudo-Dirac pair split by \(\Delta m\).

Through the active-sterile mixing substitutions, the heavy neutral leptons inherit charged-current, neutral-current, and Higgs interactions with SM leptons and gauge bosons. The model therefore mediates processes such as heavy-neutral-lepton production in weak decays or electroweak interactions, followed by decays into charged leptons, neutrinos, \(W/Z\), or Higgs states depending on kinematics.