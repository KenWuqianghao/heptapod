# Reverse-check review package — `Wprime_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `Wprime/model/Wprime_gen.fr` |
| original model name | `Wprime_gen` (hidden from the agent) |
| paper | Wprime/text/hep-ph_0207290.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LkinWp` (`=`)

```mathematica
Block[{mu,nu}, -1/2 DC[HC[Wp[nu]],mu] DC[Wp[nu],mu] + 1/2 DC[HC[Wp[nu]],mu] DC[Wp[mu],nu] + MWp^2 HC[Wp[mu]] Wp[mu]]
```

### `LkinNuR` (`=`)

```mathematica
Block[{mu,sp1,sp2,i}, Sum[I bar[vR][sp1,i].Ga[mu,sp1,sp2].del[vR[sp2,i],mu] - MvR bar[vR][sp1,i].vR[sp1,i], {i,1,3}]]
```

### `LWpQuarkNonHC` (`:=`)

```mathematica
Block[{mu,sp1,sp2,sp3,i,j,aa}, Sum[1/Sqrt[2] Wp[mu] (gWpR Exp[I omegaWp] Cos[zetaWp] VpRQ[i,j] bar[uq][sp1,i,aa].Ga[mu,sp1,sp2].ProjP[sp2,sp3].dq[sp3,j,aa] + gWpL Sin[zetaWp] VpLQ[i,j] bar[uq][sp1,i,aa].Ga[mu,sp1,sp2].ProjM[sp2,sp3].dq[sp3,j,aa]), {i,1,3}, {j,1,3}, {aa,1,3}]]
```

### `LWpLeptonNonHC` (`:=`)

```mathematica
Block[{mu,sp1,sp2,sp3,i,j}, Sum[1/Sqrt[2] Wp[mu] (gWpR Exp[I omegaWp] Cos[zetaWp] VpRL[i,j] bar[vR][sp1,i].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,j] + gWpL Sin[zetaWp] VpLL[i,j] bar[vl][sp1,i].Ga[mu,sp1,sp2].ProjM[sp2,sp3].l[sp3,j]), {i,1,3}, {j,1,3}]]
```

### `LWpFermions` (`:=`)

```mathematica
LWpQuarkNonHC + LWpLeptonNonHC + HC[LWpQuarkNonHC + LWpLeptonNonHC]
```

### `LBSM` (`=`)

```mathematica
LkinWp + LkinNuR + LWpFermions
```

## Blank-slate reconstruction

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

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Lagrangian / Field Definitions Located

The paper defines the model interaction in the Introduction. The primary model-defining Lagrangian is Eq. (1), described as “the most general Lorentz invariant Lagrangian describing the coupling of a \(W'\) to fermions”:

\[
\mathcal L =
\frac{g}{\sqrt 2}\,
\bar f_i \gamma^\mu
\left(C^R_{f_i f_j} P_R + C^L_{f_i f_j} P_L\right)
W'_\mu f_j
+\text{H.c.}
\tag{1}
\]

with \(P_{R,L}=(1\pm\gamma^5)/2\), \(g\) the SM \(SU(2)_L\) coupling, and \(C^{R,L}_{f_i f_j}\) arbitrary quark/lepton-dependent couplings.

The paper then rewrites this in left-right-symmetric notation in Eq. (2):

\[
\mathcal L =
\frac{1}{\sqrt 2}\,
\bar f_i \gamma^\mu
\left(
g_R e^{i\omega}\cos\zeta\,V^R_{f_i f_j}P_R
+
g_L \sin\zeta\,V^L_{f_i f_j}P_L
\right)
W'_\mu f_j
+\text{H.c.}
\tag{2}
\]

where \(\zeta\) is a left-right mixing angle, \(\omega\) is a CP phase absorbable into \(V^R\), \(g_{R,L}\) are right/left gauge couplings, and \(V^{R,L}\) are generalized CKM matrices.

Additional relevant definitions appear in Sec. II: the width is decomposed in Eq. (3), leading-order partial widths are Eqs. (4)-(6), the effective coupling combination is Eq. (7),

\[
|gV'_{f_i f_j}|^2
=
|g_L\sin\zeta\,V^L_{f_i f_j}|^2
+
|g_R\cos\zeta\,V^R_{f_i f_j}|^2,
\tag{7}
\]

and the numerical CKM-like matrix is Eq. (24). The right-handed neutrino is discussed in the Introduction and Sec. II as a possible leptonic decay product: a right-handed \(W'_R\) decays leptonically only if \(m_{\nu_R}<m_{W'}\), or if there is large left-right mixing in the neutrino sector.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| General \(W'\)-fermion interaction, \(\frac{g}{\sqrt2}\bar f_i\gamma^\mu(C^R P_R+C^L P_L)W'_\mu f_j+\text{H.c.}\) (Eq. 1) | \(\mathcal L_{\texttt{LWpFermions}}=\mathcal L_{\texttt{LWpQuarkNonHC}}+\mathcal L_{\texttt{LWpLeptonNonHC}}+\text{h.c.}\) | agree | The reconstruction implements the same charged-current Lorentz structure with \(P_R\) and \(P_L\), plus Hermitian conjugate. It is expressed in the more specialized Eq. (2) parameterization rather than arbitrary \(C^{R,L}\). |
| Left-right form \(g_R e^{i\omega}\cos\zeta\,V^R P_R + g_L\sin\zeta\,V^L P_L\) (Eq. 2) | \(g_{WpR}e^{i\omega_{Wp}}\cos\zeta_{Wp}V^R P_R + g_{WpL}\sin\zeta_{Wp}V^L P_L\) | agree | Coefficient structure, CP phase placement, mixing-angle factors, and chiral projectors match Eq. (2). |
| Quark charged current implied by Eqs. (1)-(2), with GCKM matrices for quarks | \(W_\mu^{\prime +}\bar u_i^a\gamma^\mu P_{R,L}d_j^a\) with \(V^{R,q}_{ij},V^{L,q}_{ij}\), plus h.c. | agree | This is the expected explicit charged-current orientation for \(W^{\prime +}\); color is diagonally contracted, consistent with a color-singlet \(W'\). |
| Lepton charged current implied by Eqs. (1)-(2), with diagonal lepton couplings in the SM-like case | \(W_\mu^{\prime +}\bar\nu_{R i}\gamma^\mu P_R\ell_j\) and \(W_\mu^{\prime +}\bar\nu_i\gamma^\mu P_L\ell_j\), plus h.c. | agree | The reconstruction separates SM left neutrinos and new right-handed neutrinos. This matches the paper’s distinction between \(W'_L\) leptonic decays and \(W'_R\to \ell\nu_R\) when kinematically allowed. |
| Hermitian conjugate in Eqs. (1)-(2) | Explicit h.c. containing \(W_\mu^{\prime -}\bar d_j\gamma^\mu P_{R,L}u_i\), etc. | agree | The reconstruction correctly includes charge-conjugate interactions with complex-conjugated mixing matrices and \(e^{-i\omega}\). |
| Projector convention \(P_{R,L}=(1\pm\gamma^5)/2\) (Eq. 1 text) | \(P_R=(1+\gamma^5)/2\), \(P_L=(1-\gamma^5)/2\) | agree | Same convention. |
| Effective width coupling \(|gV'|^2=|g_L\sin\zeta V^L|^2+|g_R\cos\zeta V^R|^2\) (Eq. 7) | Separate left/right amplitudes with the same \(g_{WpL,R}\), \(\sin\zeta_{Wp}\), \(\cos\zeta_{Wp}\), and \(V^{L,R}\) factors | agree | The reconstruction’s Lagrangian is the pre-factorized form that yields the paper’s Eq. (7) under the paper’s assumption of at most one nonzero final-state mass. |
| Numerical quark mixing matrix \(V'_{\rm CKM}\) (Eq. 24) | \(V^{L,q}=V^{R,q}=\begin{pmatrix}0.9751&0.2215&0.0035\\0.2210&0.9743&0.0410\\0.0090&0.0400&1.0000\end{pmatrix}\) | agree | The reconstructed quark matrices match the paper’s numerical matrix. |
| Lepton mixing assumed identity in numerical results (Sec. II.A, before Eq. 24) | \(V^{L,\ell}=V^{R,\ell}=\mathbf 1\) | agree | Matches the paper’s numerical assumption \(V'_{l\nu}\) is the identity. |
| \(W'\) as charged massive vector boson, with both \(W^{\prime +}\) and \(W^{\prime -}\) through h.c. (Introduction, Eqs. 1-2) | Non-self-conjugate vector \(W_\mu^{\prime +}\), antiparticle \(W_\mu^{\prime -}\), electric charge \(Q=+1\) | agree | The explicit charge assignment is consistent with the charged-current interactions and Hermitian conjugate in the paper. |
| Right-handed neutrino as possible \(W'_R\) leptonic decay product, with kinematic condition \(m_{\nu_R}<m_{W'}\) (Introduction; Sec. II after Table I) | Three non-self-conjugate \(\nu_{R i}\) fields with mass \(M_{\nu_R}=100\) | agree | The presence of \(\nu_R\) agrees. The paper does not specify three generations or a Dirac-type kinetic/mass term, but three flavors are a natural implementation of the lepton matrix structure. |
| Paper’s general arbitrary couplings \(C^{R,L}_{f_i f_j}\), allowed to differ for quarks and leptons (Eq. 1 text) | Universal \(g_{WpR}\), \(g_{WpL}\) multiplying separate quark/lepton flavor matrices | disagree | The reconstruction matches the left-right Eq. (2) parameterization, but is less general than Eq. (1) if Eq. (1) is taken literally as independent arbitrary \(C^{R,L}\) for each fermion sector and flavor entry. |
| Paper does not define a standalone \(W'\) kinetic or electromagnetic covariant derivative term | \(\mathcal L_{\texttt{LkinWp}}=-\frac12 W_{\mu\nu}^{\prime -}W^{\prime +\mu\nu}+M_{W'}^2W_\mu^{\prime -}W^{\prime +\mu}\), with EM-only covariant derivative | extra-in-reconstruction | This is necessary for an implementation, but it is not specified by the paper’s model definition. The EM-only covariant derivative is an implementation choice not stated in the paper. |
| Paper does not define a standalone \(\nu_R\) kinetic or mass Lagrangian | \(\mathcal L_{\texttt{LkinNuR}}=\sum_i i\bar\nu_{R i}\gamma^\mu\partial_\mu\nu_{R i}-M_{\nu_R}\bar\nu_{R i}\nu_{R i}\) | extra-in-reconstruction | The paper only refers to the mass of \(\nu_R\) for whether the decay is open; it does not specify Dirac versus Majorana structure or the number of explicit \(\nu_R\) fields. |
| Paper numerical treatment uses calculated \(W'\) widths from partial widths, Eqs. (3)-(7), (22)-(23), Tables II-III | Reconstruction declares `WWp = 1.` | disagree | A fixed width of 1 GeV is not the paper’s width prescription. It may be a placeholder implementation parameter, but it does not reproduce the paper’s mass- and coupling-dependent total width. |
| Paper treats \(g_R\), \(g_L\), \(\zeta\), \(\omega\), and GCKM matrices as model parameters; numerical examples use SM-like coupling normalization | Reconstruction initializes \(g_{WpL}=g_{WpR}=0.653\), \(\zeta_{Wp}=0\), \(\omega_{Wp}=0\) | agree | The symbols and coupling normalization are consistent with the paper’s SM-like examples. The default \(\zeta=0\) selects a purely right-handed benchmark, not the whole arbitrary-coupling setup. |
| Paper defines no \(SU(2)_L\), hypercharge, or color representation for \(W'\) beyond its charged-current role | Reconstruction declares \(W'\) with no color or weak-isospin index and electric charge only | agree | This is compatible with the paper’s phenomenological treatment, though the paper discusses possible UV origins such as broken \(SU(2)_L\times SU(2)_R\). |

## Disagreements and Checks

| disagreement | severity | what a human should check |
|---|---|---|
| Reconstruction implements Eq. (2)’s factorized left-right form, while Eq. (1) allows fully arbitrary \(C^{R,L}_{f_i f_j}\) couplings that can differ by sector and flavor. | convention | Check whether the implementation is intended to reproduce the paper’s Eq. (2) benchmark parameterization or the maximally general Eq. (1) coupling freedom. |
| Reconstruction includes an explicit \(W'\) kinetic/mass term with an EM-only covariant derivative, which the paper does not specify. | substantive | Check whether photon interactions of \(W'\) generated by the EM covariant derivative are intended and whether they are used in processes beyond the paper’s \(s\)-channel charged-current calculation. |
| Reconstruction includes three Dirac-type right-handed neutrino fields with explicit kinetic and mass terms, while the paper only uses \(m_{\nu_R}\) as a kinematic condition for \(W'_R\) leptonic decays. | substantive | Check whether the implementation’s Dirac, non-self-conjugate \(\nu_R\) choice matches the target phenomenology, especially if neutrino-sector mixing or Majorana assumptions matter. |
| Reconstruction declares a fixed \(W'\) width `WWp = 1.`, whereas the paper computes total widths from the coupling-dependent partial widths in Sec. II. | substantive | Check whether the width is recalculated elsewhere at runtime; if not, the implementation will not reproduce the paper’s width and branching-ratio predictions. |
| Reconstruction default \(\zeta_{Wp}=0\) makes the default interaction purely right-handed, while the paper treats arbitrary left/right couplings and discusses both left- and right-handed cases. | convention | Check whether parameter cards used for comparisons set \(\zeta\) and couplings to the desired paper scenario rather than relying on the default. |

## Overall Assessment

The reconstructed charged-current interaction agrees closely with the paper’s Eq. (2) left-right-symmetric parameterization: the chiral projectors, \(g_R e^{i\omega}\cos\zeta\) and \(g_L\sin\zeta\) coefficient structure, Hermitian conjugation, quark CKM-like matrix, and identity lepton mixing all match the paper’s definitions and numerical assumptions. The main caveats are that the reconstruction is an implementation-level model rather than only the paper’s phenomenological interaction: it adds kinetic and mass terms for \(W'\) and \(\nu_R\), fixes a default right-handed benchmark, and declares a fixed \(W'\) width that does not by itself reproduce the paper’s calculated width prescription.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 9 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

