# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Definition Located

The paper defines the relevant composite leptoquark model in **Section II, “Nambu-Jona-Lasinio Composite Leptoquark Model.”**

Key references:

- **Table I**: composite boson field content, constituents, electric charge \(Q_i=Y+t^i_{3L}\), weak isospin \(t^i_{3L}\), hypercharge \(Y\), color representation, and LQ nomenclature.
- **Eq. (1)**: scalar leptoquark kinetic and mass term,
  \[
  (D_\mu\Phi)^\dagger(D^\mu\Phi)+M_\Pi^2\Phi^\dagger\Phi .
  \]
- **Eq. (2)**: covariant derivative,
  \[
  D_\mu=\partial_\mu+i g_1YB_\mu+\frac12 i g_2\sigma^i W^i_\mu+i g_3T^aG^a_\mu .
  \]
- Text immediately after **Eq. (2)**: the color-triplet LQ bosons form \(SU_L(2)\) doublets,
  \[
  \Pi^a_{1/6}=
  \begin{pmatrix}
  \Pi^{2/3}_{u a}\\
  \Pi^{-1/3}_a
  \end{pmatrix},
  \qquad
  \Pi^a_{7/6}=
  \begin{pmatrix}
  \Pi^{5/3}_a\\
  \Pi^{2/3}_{d a}
  \end{pmatrix}.
  \]
- **Eq. (3)**: effective contact/Yukawa interactions for the first generation, plus h.c.
- Text after **Eq. (3)**: generalization to second and third generations, baryon/lepton numbers \(B=1/3\), \(L=-1\), and conjugation relations.
- **Eq. (4)**: example flavor-mixed Yukawa couplings, with CKM-like factors.
- **Section III**: states that the MadGraph/FeynRules implementation includes the gauge terms of Eq. (1) and contact terms of Eq. (3), implemented up to the third fermion generation.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Table I and text after Eq. (2): \(SU_c(3)\) triplet scalar LQs arranged as \(SU_L(2)\) doublets \(\Pi^a_{7/6}=(\Pi^{5/3}_a,\Pi^{2/3}_{d a})^T\), \(\Pi^a_{1/6}=(\Pi^{2/3}_{u a},\Pi^{-1/3}_a)^T\). | Twelve complex color-triplet scalars, but each has “SU(2) rep declared: none / singlet as declared”; no explicit weak-isospin index. | **disagree** | Component electric charges and hypercharges match the two paper doublets, but the reconstruction says the implementation has no \(SU(2)\) doublet structure. This removes explicit charged-\(W^\pm\) transitions between doublet components required by Eq. (2). |
| Eq. (1): \((D_\mu\Phi)^\dagger(D^\mu\Phi)+M_\Pi^2\Phi^\dagger\Phi\). | For each scalar, \((D_\mu\Pi)^\dagger(D^\mu\Pi)-M_\Pi^2\Pi^\dagger\Pi\). | **disagree** | The kinetic form agrees, but the mass term sign differs from the paper as written. This may be a metric/sign convention or a paper typo, but as text-to-text comparison it is different. |
| Eq. (2): covariant derivative includes \(+\frac12 i g_2\sigma^iW^i_\mu\), acting on \(SU(2)\) doublets. | Covariant derivative includes QCD and neutral electroweak couplings fixed by \(Q,Y\), with no charged \(W^\pm\) covariant-derivative mixing. | **disagree** | This is the same core issue as the field representation disagreement: the paper has Pauli-matrix \(SU(2)\) action on doublets; the reconstruction describes component singlets with no \(W^\pm\) doublet mixing. |
| Table I: \(\Pi^{5/3}_a\propto \bar e_R u_{L a}\), \(Q=5/3\), \(t_3=+1/2\), \(Y=7/6\), color triplet; Eq. (3): \(g_{\Pi5/3}(\bar e_Ru_{L a})\Pi^{-5/3}_a+\text{h.c.}\). | \(\lambda_{EU}\bar e_Ru_L^a\Pi_{5e}^{a\dagger}\), plus \(\mu c\) and \(\tau t\) analogues. | **agree** | Chirality, electric charge, hypercharge, color, conjugation in the interaction, and generation generalization agree. Reconstruction uses separate generation labels and default numerical couplings. |
| Table I: \(\Pi^{2/3}_{d a}\propto\bar e_R d_{L a}\), \(Q=2/3\), \(t_3=-1/2\), \(Y=7/6\); Eq. (3): \(g_{\Pi-2/3}(\bar e_Rd_{L a})\Pi^{-2/3}_{d a}+\text{h.c.}\). | \(\lambda_{ED}\bar e_Rd_L^a\Pi_{2de}^{a\dagger}\), plus \(\mu s\) and \(\tau b\) analogues. | **agree** | The component assignment, chirality, color, charge, hypercharge, and use of the conjugate scalar in the interaction agree. |
| Table I: \(\Pi^{2/3}_{u a}\propto\bar\nu^R_e u_{L a}\), \(Q=2/3\), \(t_3=+1/2\), \(Y=1/6\); Eq. (3): \(g_{\Pi-2/3}(\bar\nu^R_eu_{L a})\Pi^{-2/3}_{u a}+\text{h.c.}\). | \(\lambda_{\nu EU}\bar\nu_{eL}u_L^a\Pi_{2ue}^{a\dagger}\), plus \(\nu_\mu c\) and \(\nu_\tau t\) analogues. | **disagree** | The scalar charge and hypercharge match, and conjugation is analogous, but the paper uses a barred right-handed neutrino constituent in Table I/Eq. (3), while the reconstruction uses left-handed neutrinos. |
| Table I: \(\Pi^{-1/3}_a\propto\bar\nu^R_e d_{L a}\), \(Q=-1/3\), \(t_3=-1/2\), \(Y=1/6\); Eq. (3): \(g_{\Pi1/3}(\bar\nu^R_ed_{L a})\Pi^{1/3}_a+\text{h.c.}\). | \(\lambda_{\nu ED}\bar\nu_{eL}d_L^a\Pi_{-1e}^{a\dagger}\), plus \(\nu_\mu s\) and \(\nu_\tau b\) analogues. | **disagree** | Scalar charge, hypercharge, color, and conjugation match, but neutrino chirality differs from the paper’s Table I/Eq. (3). |
| Text after Eq. (3): conjugated fields \((\Pi^{5/3})^\dagger=\Pi^{-5/3}\), \((\Pi^{-1/3})^\dagger=\Pi^{1/3}\), and conjugates for the \(Q=2/3\) states. | All new scalars are complex and non-self-conjugate; Yukawa Lagrangian includes h.c. | **agree** | The reconstruction does not introduce separate independent antiparticle fields, but the complex scalar plus h.c. treatment captures the conjugate interactions. |
| Text after Eq. (3): \(B=1/3\), \(L=-1\) for these LQ states. | All new scalar fields declare \(B=1/3\), \(L=-1\). | **agree** | Matches the paper. |
| Text after Eq. (3): spectra and interactions generalized by \(\nu_e,e,u,d\to\nu_\mu,\mu,c,s\) and \(\nu_\tau,\tau,t,b\). | Reconstruction includes diagonal first-, second-, and third-generation couplings. | **agree** | The diagonal generation generalization is represented. |
| Eq. (3): \(g_{\Pi i}=(F_{\Pi i}/\Lambda)^2\sim O(1)\); paper later uses \(\lambda\) for \(g_{\Pi i}\). | Independent real parameters \(\lambda_{EU}\), \(\lambda_{\mu C}\), etc., defaulting to 1.0. | **agree** | The coefficient structure is compatible with the paper’s \(\lambda\sim O(1)\) convention. Equal default values are benchmark choices, not a structural disagreement. |
| Text after Eq. (3): masses \(M_{\Pi i}\) and couplings \(g_{\Pi i}\) can differ across generations. | Separate mass symbols for each scalar, but all default to 1000; separate coupling symbols, all default to 1.0. | **agree** | The reconstruction has independent parameters even though the displayed defaults are common benchmark values. |
| Eq. (4): example flavor-mixed couplings such as \(g_{\Pi5/3}(U_R^\dagger U_L)_{1,2}(\bar\mu_Rc_L)\Pi^{-5/3}_a\) and \((U_R^\dagger U_L)_{1,3}(\bar\tau_Rt_L)\Pi^{-5/3}_a\), with analogous terms possible for other LQs. | Only generation-aligned couplings are listed: \(eu\), \(\mu c\), \(\tau t\), \(ed\), \(\mu s\), \(\tau b\), and neutrino analogues. | **missing-in-reconstruction** | Eq. (4) describes flavor-mixed couplings of a given LQ state to other generations via mixing matrices. The reconstruction instead has separate generation-labeled LQ fields with diagonal couplings and no explicit CKM-like mixing factors. |
| Section III: implementation includes gauge Eq. (1) and contact Eq. (3) terms up to third generation. | `LBSM = LkinNJL + LNJLYukawa`, with twelve scalar fields and Yukawa terms plus h.c. | **agree** | At the broad implementation-scope level, the reconstruction matches the stated UFO contents, except for the specific disagreements above. |

## Disagreements and Human Checks

1. **Missing \(SU(2)_L\) doublet structure and charged-\(W\) interactions** — **substantive**.  
   A human should check whether the actual implementation intentionally broke the paper’s Eq. (2) doublet structure into electroweak-component singlets, because this changes gauge interactions involving \(W^\pm\).

2. **Neutrino chirality in the \(Y=1/6\) leptoquark interactions** — **substantive**.  
   A human should check the implementation file’s chiral projectors for the neutrino vertices against Table I and Eq. (3), since the paper uses \(\bar\nu_R q_L\) for the positive-charge \(Y=1/6\) constituents while the reconstruction reports \(\bar\nu_L q_L\).

3. **Mass-term sign relative to Eq. (1)** — **convention**.  
   A human should check the paper’s metric/sign convention and the FeynRules scalar mass convention before treating this as a physical mismatch.

4. **Flavor-mixed Yukawa terms of Eq. (4) absent from the reconstruction** — **substantive**.  
   A human should check whether Eq. (4) was intended as part of the implemented model or only as a phenomenological possibility, because the reconstruction contains only generation-aligned couplings without explicit mixing-matrix factors.

## Overall Assessment

The reconstruction captures the paper’s broad leptoquark content: complex color-triplet scalar states with charges \(5/3\), \(2/3\), and \(-1/3\), baryon number \(1/3\), lepton number \(-1\), generation-aligned Yukawa-like couplings, and hermitian conjugates. The main mismatches are notationally small but physically important: the paper defines the charged states as components of \(SU(2)_L\) doublets with the full \(W^i_\mu\) covariant derivative, while the reconstruction describes separate weak singlets with no charged-\(W\) mixing; and the neutrino-coupled \(Y=1/6\) terms use left-handed neutrinos in the reconstruction where the paper’s Table I and Eq. (3) use right-handed neutrino constituents. The absence of Eq. (4)-type flavor-mixed couplings is also important if the review target is the full paper model rather than only a simplified diagonal UFO benchmark.