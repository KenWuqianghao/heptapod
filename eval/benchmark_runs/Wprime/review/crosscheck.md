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