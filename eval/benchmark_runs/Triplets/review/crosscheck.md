# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Location

The model is defined in **Section 2, “Model And Constraints”**. The electroweak field assignments are summarized in **Table 1**, and the post-EWSB diquark-quark interaction Lagrangian is given in **Eq. (2.1)**:
\[
L = 2\sqrt{2}\left[\bar K^i_{ab}D_i\bar q^a(\lambda_L P_L+\lambda_R P_R)q_b^C+\text{h.c.}\right].
\]
The paper states that \(D_i\) is a scalar diquark in either the **sextet** or **antitriplet** of \(SU(3)_C\), with Clebsch-Gordan coefficients \(\bar K^i_{ab}\) coupling the diquark representation to two color triplets. The color conventions are detailed in **Appendix A**, especially **Eqs. (A.6)-(A.10)**. For the antitriplet case, **Eq. (A.7)** and the following paragraph give
\[
K_{abc}=\epsilon_{abc}/\sqrt{2}.
\]
The paper also states in Section 2 that, in the antitriplet case, the couplings must be antisymmetric in flavor.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Possible diquark electroweak assignments: Table 1 lists \(SU(2)_L=1\), \(Y=1/3\), \(|Q|=1/3\), coupling to \(QQ,UD\); also other possibilities \(SU(2)_L=3,Y=1/3\), \(SU(2)_L=1,Y=2/3\), \(SU(2)_L=1,Y=4/3\). | Reconstruction selects one scalar \(S\): \(SU(3)_c\) triplet, \(SU(2)_L\) singlet, \(Y=Q=-1/3\). | disagree | The reconstruction corresponds to the conjugate of the paper’s \(SU(2)\)-singlet \(Y=+1/3\) diquark if one identifies \(D=S^\dagger\). As written, the field table assigns the opposite hypercharge/charge to the named scalar relative to the paper’s \(D\). The paper is also generic over antitriplet or sextet color, while the reconstruction fixes the antitriplet/conjugate-triplet case. |
| Diquark color representation: Section 2 says \(D_i\) transforms as either \(6\) or \(\bar 3\) of \(SU(3)_C\); Appendix A gives both symmetric sextet and antisymmetric antitriplet Clebsch-Gordan tensors. | Reconstruction has a single complex color-triplet scalar \(S_k\), with \(S_k^\dagger\) entering the diquark coupling via \(\epsilon_{kij}\). | agree | For the antitriplet case only, this is equivalent if \(D_k\equiv S_k^\dagger\). The reconstruction does not represent the sextet option discussed in the paper. |
| Antitriplet Clebsch-Gordan structure: Appendix A, Eq. (A.7) and following text, \(K_{abc}=\epsilon_{abc}/\sqrt{2}\). | \(2\,\epsilon_{kij}S_k^\dagger \lambda\,\bar d_{ni}P_{R/L}u^c_{mj}\). | agree | Combining the paper’s coefficient \(2\sqrt2\) in Eq. (2.1) with \(K=\epsilon/\sqrt2\) gives an overall factor \(2\epsilon\), matching the reconstruction for the antitriplet case, up to the identification \(D=S^\dagger\). |
| Generic quark-diquark interaction: Eq. (2.1), \(2\sqrt2\,\bar K^i_{ab}D_i\bar q^a(\lambda_LP_L+\lambda_RP_R)q_b^C+\text{h.c.}\). | `LD11`: \(2\epsilon_{kij}S_k^\dagger\lambda^{QQ}_{nm}\bar d_{ni}P_Ru^c_{mj}\) plus \(2\epsilon_{kij}S_k^\dagger\lambda^{UD}_{nm}\bar d_{ni}P_Lu^c_{mj}\), with h.c. in `LD1`. | agree | This matches the paper’s antitriplet specialization and the \(QQ/UD\) singlet row of Table 1, provided \(D=S^\dagger\). The paper keeps \(q\) and flavor sums generic, while the reconstruction spells out \(d,u^c\) components. |
| Chirality projectors: Eq. (2.1), \(P_{L,R}=(1\mp\gamma^5)/2\), acting on \(q^C\). | Reconstruction interprets \(\bar dP_Ru^c\) as a left-chiral \(QQ\)-type coupling and \(\bar dP_Lu^c\) as a right-chiral \(UD\)-type coupling. | agree | Because charge conjugation flips chirality, this interpretation is physically consistent. The reconstruction’s parameter names `LQQR` and `LUDL` are notation-specific and should not be read as contradicting the physical chirality. |
| Hermitian conjugate: Eq. (2.1) explicitly includes \(+\text{h.c.}\). | `LD1 = LD11 + LD11^\dagger`. | agree | Direct match. |
| Flavor structure: Section 2 says flavor sums are suppressed and \(\lambda_{L,R}\) may be independent or model-constrained; in the antitriplet case, couplings must be antisymmetric in flavor. | Reconstruction has antisymmetric nonzero `LQQR` off-diagonal entries, but `LUDL` is diagonal. | disagree | The `LQQR` pattern is consistent with an antisymmetric \(QQ\) antitriplet coupling. The diagonal `LUDL` entries may be acceptable if treated as \(U\)-\(D\) species couplings rather than identical-flavor antisymmetry, but the paper’s broad statement that antitriplet couplings are antisymmetric in flavor makes this a point requiring human confirmation. |
| Gauge interactions of colored scalar: Section 2 says any nontrivial \(SU(3)_C\) state interacts with gluons; Section 4 and Appendix A use the diquark representation generators and Casimir \(C_D\), with \(C_D=4/3\) for antitriplet and \(10/3\) for sextet. | `LTripKin`: \((D_\mu S)^\dagger(D^\mu S)-M^2S^\dagger S\), with \(SU(3)_c\) and hypercharge gauge terms, no \(SU(2)_L\). | agree | The kinetic/mass term is not written explicitly in Eq. (2.1), but is implied by the paper’s production calculation for a massive colored scalar. The reconstruction fixes the antitriplet/conjugate-triplet and singlet-hypercharge case. |
| Diquark mass: production formulas use \(m_D\), e.g. Eqs. (3.3)-(3.4). | Mass term \(-M_{\texttt{trip1}}^2S^\dagger S\), with \(M_{\texttt{trip1}}=500\). | agree | The paper treats \(m_D\) as a variable mass parameter; the reconstruction gives one implementation value. |
| Higgs portal quartic \((\Phi^\dagger\Phi)(S^\dagger S)\). | `LPot`: \(\lambda_{HS}(\Phi^\dagger\Phi)(S^\dagger S)\). | extra-in-reconstruction | The paper does not define this scalar-potential term. It may exist in a UV-complete model, but it is outside the paper’s stated production Lagrangian. |
| Scalar self-quartic \((S^\dagger S)^2\). | `LPot`: \(\lambda_{SS}(S^\dagger S)^2\). | extra-in-reconstruction | The paper does not specify a scalar self-potential. |
| Sextet diquark option: Section 2 and Appendix A include the color sextet; Table 1 says each electroweak state may be \(\bar3\) or \(6\). | No sextet field or symmetric Clebsch-Gordan coupling appears. | missing-in-reconstruction | The reconstruction only covers the antitriplet/conjugate-triplet implementation, not the paper’s full generic color scope. |
| Other Table 1 electroweak possibilities: \(SU(2)_L=3,Y=1/3\) coupling to \(QQ\), singlet \(Y=2/3\) coupling to \(DD\), singlet \(Y=4/3\) coupling to \(UU\). | No \(SU(2)_L\) triplet, \(DD\), or \(UU\) couplings. | missing-in-reconstruction | The paper lists these for completeness but then uses a generic post-EWSB parameterization. The reconstruction is a specific \(QQ/UD\), \(SU(2)\)-singlet model. |

## Disagreements and Checks

1. **Named scalar charge and representation: substantive.**  
   The reconstruction names the fundamental scalar \(S\) as a color triplet with \(Y=Q=-1/3\), while the paper’s \(QQ/UD\) diquark in Table 1 has \(Y=+1/3\) and color \(\bar3\) or \(6\); a human should check whether the implementation intentionally defines \(S^\dagger\) as the paper’s produced diquark \(D\).

2. **Sextet omission: substantive.**  
   The paper’s model parameterization covers both color antitriplet and sextet diquarks, but the reconstruction only contains the antitriplet/conjugate-triplet epsilon structure; a human should check whether the implementation was intended to reproduce only the antitriplet benchmark rather than the full paper.

3. **Other electroweak assignments omitted: convention/substantive depending on scope.**  
   Table 1 includes \(QQ\) triplet, \(DD\), and \(UU\) singlet possibilities, but the reconstruction only implements the \(SU(2)_L\)-singlet \(QQ/UD\) case; a human should check whether the implementation target was the full table or one benchmark row.

4. **`LUDL` flavor symmetry: substantive if the paper’s antitriplet antisymmetry is meant to apply to all flavor matrices.**  
   The reconstruction gives diagonal right-chiral \(UD\) couplings, while the paper says antitriplet couplings must be antisymmetric in flavor; a human should check how the implementation defines flavor indices for \(U\)-\(D\) couplings and whether antisymmetry is required for non-identical up/down species.

5. **Scalar potential terms: substantive relative to the paper text, likely harmless for production.**  
   The reconstruction includes Higgs-portal and scalar self-quartic interactions not specified in the paper; a human should check whether these are implementation conveniences/default scalar potential terms or intended claims about the paper’s model.

## Overall Assessment

The reconstruction captures the core antitriplet \(QQ/UD\) diquark interaction of Eq. (2.1) well once the paper’s diquark is identified with \(S^\dagger\): the epsilon color tensor, the overall factor of \(2\), the hermitian conjugate, and the chirality interpretation are all consistent with the paper’s antitriplet Clebsch-Gordan normalization. The main caveats are scope and convention: the paper is written as a generic scalar diquark parameterization covering both \(\bar3\) and \(6\) color representations and multiple electroweak assignments, while the reconstruction is a specific singlet antitriplet/conjugate-triplet implementation with the named scalar carrying the opposite charge from the paper’s \(D\). The added scalar potential terms are not part of the paper’s defined production Lagrangian, and the right-chiral \(UD\) flavor structure deserves a targeted check against the implementation’s flavor-index convention.