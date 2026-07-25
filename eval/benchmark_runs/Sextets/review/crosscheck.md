# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Location

The paper defines the model in **Section 2, “Model And Constraints”**. The relevant ingredients are:

- **Table 1**: possible electroweak quantum numbers and allowed quark bilinears for scalar diquarks. Each listed state may be either an \(SU(3)_C\) antitriplet \(\bar{\mathbf 3}\) or sextet \(\mathbf 6\).
- **Eq. (2.1)**: the post-EWSB scalar diquark interaction
  \[
  \mathcal L =
  2\sqrt 2\left[
  \bar K^i_{ab}D_i\bar q^a(\lambda_L P_L+\lambda_R P_R)q_b^C
  +\text{h.c.}
  \right].
  \]
- **Eq. (2.2)**: example constraints for a sextet diquark coupled to right-handed up-type quarks.
- **Section 3, Eqs. (3.1)-(3.3)**: production process, Born amplitude, and normalization conventions.
- **Appendix A, especially Eqs. (A.6)-(A.16)**: Clebsch-Gordan tensors and sextet/antitriplet color-generator conventions.

## Term-By-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Generic scalar diquark \(D_i\), color representation either \(\mathbf 6\) or \(\bar{\mathbf 3}\) (Section 2; Table 1; Eq. (2.1)) | Three scalar fields \(S_1,S_2,S_3\), all in color \(\mathbf 6\) | missing-in-reconstruction | Reconstruction covers only the sextet branch. The paper explicitly allows both sextet and antitriplet color representations. |
| Antitriplet color option with antisymmetric flavor couplings (Section 2 after Eq. (2.1); Appendix A, Eq. (A.7)) | No antitriplet scalar, no antisymmetric flavor condition | missing-in-reconstruction | The paper states that in the antitriplet case the couplings must be antisymmetric in flavor. Reconstruction is sextet-only. |
| Sextet Clebsch tensor \(K^i_{ab}\), symmetric in the two triplet indices (Appendix A, Eq. (A.6), completeness Eq. (A.10)) | \(K^*_{kij}=\texttt{K6bar[k,i,j]}\), symmetric color-sextet contraction | agree | This matches the sextet color structure used by the paper. |
| Diquark may be scalar; paper concentrates on scalar case (Section 2) | \(S_1,S_2,S_3\) are spin-0 scalars | agree | Reconstruction matches the scalar specialization. |
| Table 1 singlet state: \(SU(2)_L=\mathbf 1\), \(Y=1/3\), \(|Q|=1/3\), couplings \(QQ,UD\) | \(S_1\sim(\mathbf 6,\mathbf 1,Y=1/3)\), couplings to \(du\) through `LQQR` and `LUDL` | agree | The two \(S_1\) chiral structures correspond to the paper’s \(QQ\) and \(UD\) entries after translating projectors acting on charge-conjugated spinors. |
| Table 1 triplet state: \(SU(2)_L=\mathbf 3\), \(Y=1/3\), \(|Q|=1/3,2/3,4/3\), coupling \(QQ\) | No \(SU(2)_L\) triplet diquark multiplet | missing-in-reconstruction | The paper lists this as a possible electroweak assignment, though the later QCD calculation is model-independent after EWSB. |
| Table 1 singlet state: \(SU(2)_L=\mathbf 1\), \(Y=2/3\), \(|Q|=2/3\), coupling \(DD\) | \(S_2\sim(\mathbf 6,\mathbf 1,Y=-2/3)\), coupling \(S_2\,\bar d P_L d^C\) | disagree | The reconstruction’s Yukawa term is gauge invariant for \(S_2\) charge \(-2/3\), while Table 1 lists \(Y=+2/3\). This may be a \(D\) versus \(D^\dagger\) naming convention, but the hypercharge sign differs as written. |
| Table 1 singlet state: \(SU(2)_L=\mathbf 1\), \(Y=4/3\), \(|Q|=4/3\), coupling \(UU\) | \(S_3\sim(\mathbf 6,\mathbf 1,Y=4/3)\), coupling \(S_3\,\bar u P_L u^C\) | agree | Charge, singlet electroweak representation, and up-type bilinear match the paper’s \(UU\) entry. |
| Eq. (2.1): universal coefficient \(2\sqrt2\) multiplying \(\bar K D\bar q(\lambda_LP_L+\lambda_RP_R)q^C+\text{h.c.}\) | All reconstructed diquark Yukawas use \(2\sqrt2\,K^*S\,\bar q P_{L/R}q^C\), with hermitian conjugates in `LD1`, `LD2`, `LD3` | agree | Coefficient and h.c. structure match for the sextet singlet interactions. |
| Eq. (2.1): generic independent flavor couplings \(\lambda_{L,R}\), depending on flavor channel | Complex matrices `LQQR`, `LUDL`, `LDDL`, `LUUL` | agree | Reconstruction’s independent coupling matrices are compatible with the paper’s model-independent parameterization. |
| Eq. (2.1): generic chiral projectors \(P_L,P_R\) | `ProjM=P_L`, `ProjP=P_R`; terms use \(P_R\) for \(QQ\), \(P_L\) for \(UD,DD,UU\) in the charge-conjugated-spinor notation | agree | With four-component charge-conjugation identities, these projector placements are consistent with the corresponding left-left or right-right quark bilinears. |
| Eq. (2.2): example sextet \(UU\)-type constraints \(\lambda^{uu}_R,\lambda^{uc}_R\lesssim0.1\), \(\lambda^{cc}_R\simeq0\) | Defaults all listed Yukawa matrices diagonal \(0.1\), off-diagonal \(0\) | disagree | The paper gives illustrative constraints, not a universal default coupling matrix. In particular, it singles out right-handed up-type sextet couplings, not all \(QQ,UD,DD,UU\) channels. |
| Section 3, Eq. (3.2): Born amplitude \(q q\to D\) with \(K_{iab}(\lambda_LP_L+\lambda_RP_R)C^\dagger\) | No explicit amplitude, but Yukawa Lagrangian implies the same sextet vertex up to standard Feynman-rule signs | agree | The missing overall \(-i\) is not a Lagrangian-content mismatch. |
| Paper treats a single generic diquark mass \(m_D\) in production formulas (Eqs. (3.3)-(3.4)) | Three independent masses `MSIX1`, `MSIX2`, `MSIX3`, all defaulting to 500 | extra-in-reconstruction | Multiple specific mass parameters are implementation details beyond the paper’s generic \(m_D\). |
| Paper says colored states interact with gluons; Appendix A defines generators in the diquark representation (Section 2; Appendix A.3) | Sextet covariant derivatives with \(g_sG_\mu^A T_6^A\) | agree | Reconstruction implements the QCD gauge interactions implied by the paper for the sextet case. |
| Paper does not specify electroweak gauge interactions after saying it is “not concerned about the electroweak structure” (Section 2) | Full \(U(1)_Y\), photon, and \(Z\) couplings for \(S_1,S_2,S_3\) | extra-in-reconstruction | These follow from chosen Table 1 electroweak assignments but are not part of the paper’s operative Lagrangian. |
| Paper gives no explicit scalar kinetic or mass Lagrangian | `LSextetKin` with canonical kinetic and mass terms for all three sextets | extra-in-reconstruction | Canonical kinetic terms are physically expected, but they are not written as part of the paper’s defined interaction Lagrangian. |
| Paper gives no Higgs-portal interactions | `LHS1`, `LHS2`, `LHS3`: \((\Phi^\dagger\Phi)(S_a^\dagger S_a)\) | extra-in-reconstruction | No such terms appear in the paper. |
| Paper gives no scalar self-quartic potential | `LSS11`, `LSS22`, `LSS33` and mixed `LSS12*`, `LSS13*`, `LSS23*` quartics | extra-in-reconstruction | These are implementation-level additions, not part of the phenomenological model used in the paper. |
| Paper ignores diquark decay and treats the produced diquark as stable on shell (Section 4) | Reconstruction includes only production-type diquark Yukawas and no explicit decay-sector additions beyond h.c. | agree | The Yukawa h.c. would mediate the inverse process/decay, but the reconstruction does not add a separate decay model. |

## Disagreements and Human Checks

- **Missing antitriplet branch** — severity: substantive. A human should check whether the implementation was intended to reproduce the full paper parameterization or only the sextet specialization used in parts of the numerical study.

- **Missing \(SU(2)_L\) triplet \(QQ\) electroweak option** — severity: substantive. A human should check whether Table 1 is meant as required model content for this implementation or only a catalogue of possible diquark assignments.

- **\(DD\) hypercharge sign mismatch: paper Table 1 lists \(Y=+2/3\), reconstruction uses \(Y=-2/3\)** — severity: convention if this is only a \(D\) versus \(D^\dagger\) naming choice, substantive if electroweak gauge vertices are used directly. A human should trace which field, \(S_2\) or \(S_2^\dagger\), is intended to be the physical \(DD\)-coupled diquark of the paper.

- **Universal default Yukawa values in reconstruction are broader than Eq. (2.2)** — severity: substantive for phenomenology, cosmetic for pure structure. A human should check whether the implementation defaults were chosen merely as placeholders or are being interpreted as paper-derived constraints.

- **Three separate sextet masses instead of one generic \(m_D\)** — severity: convention. A human should check whether analyses using the implementation set these masses consistently when comparing to the paper’s single-diquark production formulas.

- **Electroweak gauge interactions are reconstructed but not part of the paper’s operative Lagrangian** — severity: convention. A human should check whether any calculation uses photon or \(Z\) interactions, since the paper’s results are QCD-focused and do not validate those vertices.

- **Higgs-portal and sextet scalar quartic potential terms are extra** — severity: substantive if used in predictions beyond single production. A human should check whether these potential terms came from an implementation extension rather than from the paper.

## Overall Assessment

The reconstruction captures the paper’s central sextet scalar diquark Yukawa structure well: the \(2\sqrt2\) normalization, charge-conjugated quark bilinears, sextet Clebsch tensor, hermitian conjugates, and the singlet \(QQ/UD\) and \(UU\) channels are broadly consistent with Section 2 and Appendix A. The main caveat is scope: the paper defines a generic model-independent diquark parameterization, including antitriplet and multiple electroweak possibilities, while the reconstruction describes a specific sextet-only implementation with three singlet fields and a much larger scalar/gauge sector. The most physics-sensitive point to audit is the \(DD\) state’s hypercharge sign and field-conjugation convention, followed by whether the added scalar potential and default coupling matrices are being treated as paper content or implementation extras.