# Comparison of `reconstruction.md` Against the Paper Model

## Paper Locations

The model is defined mainly in **Section 3, “Phenomenological Lagrangian”**.

Key references:

- **Eq. (1)**: initial effective \(U_1\) fermion-current interaction and field representation \(U_1 \sim (3,1,2/3)\).
- **Section 2 / Introduction**: companion vectors \(Z' \sim (1,1,0)\), \(G' \sim (8,1,0)\).
- **Eqs. (9), (10), (11)**: full phenomenological Lagrangian for \(U_1\), \(Z'\), and \(G'\).
- **Eq. (12)**: flavor basis choice,
  \[
  q_L^i=\begin{pmatrix}V^*_{ji}u_L^j\\ d_L^i\end{pmatrix},\qquad
  \ell_L^i=\begin{pmatrix}\nu_L^i\\ e_L^i\end{pmatrix}.
  \]
- **Eq. (13)**: benchmark flavor textures for \(\beta\), \(\zeta\), and \(\kappa\), including
  \[
  \beta_L^{13}=\frac{V_{td}^*}{V_{ts}^*}\beta_L^{23}.
  \]

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field content: \(U_1\sim(3,1,2/3)\), \(Z'\sim(1,1,0)\), \(G'\sim(8,1,0)\) (Intro, Sec. 2, Sec. 3) | Field table lists `VLQ` as color triplet, weak singlet, \(Y=2/3\); `Zp` as singlet; `Gp` as color octet | agree | Physics representations and charges match. |
| \(U_1\) kinetic term: \(-\frac12 U^\dagger_{1\mu\nu}U_1^{\mu\nu}\) (Eq. 9) | `LVLQKin`: \(-\frac12\bar U_{\mu\nu}^aU^{a\mu\nu}\) | agree | Same kinetic structure for a complex vector triplet. |
| \(U_1\) mass term: \(+M_U^2 U^\dagger_{1\mu}U_1^\mu\) (Eq. 9) | No explicit mass term in `LLeptoQuark`; mass only listed in particle declarations | missing-in-reconstruction | The paper includes the mass term in the Lagrangian. The reconstruction explicitly says no mass terms are written in `LLeptoQuark`. |
| \(U_1\)-gluon non-minimal term: \(-ig_s(1-\kappa_U)U^\dagger_{1\mu}T^aU_{1\nu}G^{a\mu\nu}\) (Eq. 9) | `LVLQG`: \(-ig_s(1-\kappa_U)\bar U_\mu T^AU_\nu G^{A\mu\nu}\) | agree | Coefficient, color generator, and Lorentz structure match. |
| \(U_1\)-hypercharge non-minimal term: \(-ig_Y\frac23(1-\tilde\kappa_U)U^\dagger_{1\mu}U_{1\nu}B^{\mu\nu}\) (Eq. 9) | `LVLQG`: \(-i\frac23g_1(1-\tilde\kappa_U)\bar U_\mu U_\nu B^{\mu\nu}\) | agree | Same structure; \(g_1\) vs \(g_Y\) is notation. |
| \(U_1\) LH fermion coupling: \(\frac{g_U}{\sqrt2}U_1^\mu\beta_L^{ij}\bar q_L^i\gamma_\mu\ell_L^j+\mathrm{h.c.}\) (Eq. 9) | `LVLQF` plus `HC[LVLQF]`, expanded into \(V_{ki}\bar u_k\gamma^\mu P_L\nu_j+\bar d_i\gamma^\mu P_L\ell_j\) | agree | Expansion agrees with Eq. (12): the barred up-quark component carries \(V_{ki}\). |
| \(U_1\) RH fermion coupling: \(\frac{g_U}{\sqrt2}U_1^\mu\beta_R^{ij}\bar d_R^i\gamma_\mu e_R^j+\mathrm{h.c.}\) (Eq. 9) | `LVLQF`: \(\frac{g_U}{\sqrt2}U_\mu\beta^{Rd}_{ij}\bar d_i\gamma^\mu P_R\ell_j\) plus H.c. | agree | Same physics; reconstruction labels the matrix \(\beta^{Rd}\) instead of \(\beta_R\). |
| \(U_1\) flavor texture: \(\beta_L=\begin{pmatrix}0&0&\beta_L^{13}\\0&0&\beta_L^{23}\\0&\beta_L^{32}&\beta_L^{33}\end{pmatrix}\), \(\beta_R=\mathrm{diag}(0,0,\beta_R^{33})\) (Eq. 13) | Nonzero \(\beta^L_{13},\beta^L_{23},\beta^L_{32},\beta^L_{33}\); \(\beta^{Rd}_{33}\) only | agree | Matches the texture. |
| Spurion relation: \(\beta_L^{13}=V_{td}^*/V_{ts}^*\,\beta_L^{23}\) (below Eq. 13) | \(\beta^L_{13}=(V_{31}/V_{32})^*\beta^L_{23}\) | agree | Same relation if \(V_{31}=V_{td}\), \(V_{32}=V_{ts}\). |
| \(Z'\) kinetic term: \(-\frac14Z'_{\mu\nu}Z'^{\mu\nu}\) (Eq. 10) | No `LZpKin` term included in reconstructed `LLeptoQuark` | missing-in-reconstruction | This is a real omission relative to the paper Lagrangian. |
| \(Z'\) mass term: \(+\frac12M_{Z'}^2Z'_\mu Z'^\mu\) (Eq. 10) | No explicit mass term in `LLeptoQuark`; mass only listed in particle declarations | missing-in-reconstruction | The paper includes the mass term in the Lagrangian. |
| \(Z'\) LH quark coupling: \(\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_q^{ij}\bar q_L^i\gamma^\mu q_L^j\) (Eq. 10) | `LZpF`: up-sector \(V_{ki}V^*_{nj}\bar u_k\gamma^\mu P_Lu_n\) and down-sector \(\bar d_i\gamma^\mu P_Ld_j\) | agree | Correct expansion using Eq. (12). |
| \(Z'\) RH up coupling: \(\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_u^{ij}\bar u_R^i\gamma^\mu u_R^j\) (Eq. 10) | `LZpF`: \(\zeta^u_{ij}\bar u_i\gamma^\mu P_Ru_j\) | agree | Same chirality and coefficient. |
| \(Z'\) RH down coupling: \(\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_d^{ij}\bar d_R^i\gamma^\mu d_R^j\) (Eq. 10) | `LZpF`: \(\zeta^d_{ij}\bar d_i\gamma^\mu P_Rd_j\) | agree | Same chirality and coefficient. |
| \(Z'\) LH lepton coupling: \(-3\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_\ell^{ij}\bar\ell_L^i\gamma^\mu\ell_L^j\) (Eq. 10) | `LZpF`: separate \(-3\zeta^\ell_{ij}\bar\ell_iP_L\ell_j\) and \(-3\zeta^\ell_{ij}\bar\nu_iP_L\nu_j\) | agree | Correct doublet expansion. |
| \(Z'\) RH charged-lepton coupling: \(-3\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_e^{ij}\bar e_R^i\gamma^\mu e_R^j\) (Eq. 10) | `LZpF`: \(-3\zeta^e_{ij}\bar\ell_i\gamma^\mu P_R\ell_j\) | agree | Same physics; reconstruction uses \(\ell\) for charged leptons. |
| \(Z'\) flavor textures: \(\zeta_\ell\), \(\zeta_e\), \(\zeta_Q=\mathrm{diag}(\zeta_Q^{ll},\zeta_Q^{ll},\zeta_Q^{33})\) (Eq. 13) | Nonzero \(\zeta^\ell_{22},\zeta^\ell_{23},\zeta^\ell_{32},\zeta^\ell_{33}\), \(\zeta^e_{22},\zeta^e_{33}\), diagonal light/third quark entries | agree | Matches Eq. (13), including Hermitian \(\zeta^\ell_{32}=(\zeta^\ell_{23})^*\). |
| \(G'\) kinetic term: \(-\frac14G'^a_{\mu\nu}G'^{a\mu\nu}\) (Eq. 11) | `LGpKin`: \(-\frac14G'^A_{\mu\nu}G'^{A\mu\nu}\) | agree | Same kinetic structure. |
| \(G'\) mass term: \(+\frac12M_{G'}^2G'^a_\mu G'^{a\mu}\) (Eq. 11) | No explicit mass term in `LLeptoQuark`; mass only listed in particle declarations | missing-in-reconstruction | The paper includes the mass term in the Lagrangian. |
| \(G'\)-gluon field-strength mixing: \(+\frac12\kappa_{G'}G'^a_{\mu\nu}G^{a\mu\nu}\) (Eq. 11) | `LGpG`: \(\frac12\kappa_{G'}G'^A_{\mu\nu}G^{A\mu\nu}\) | agree | Same coefficient and structure. |
| \(G'G'G\) non-minimal term: \(+g_s\tilde\kappa_{G'}f^{abc}G'^a_\mu G'^b_\nu G^{c\mu\nu}\) (Eq. 11) | `LGpG`: \(g_s\tilde\kappa_{G'}f^{ABC}G'^A_\mu G'^B_\nu G^{C\mu\nu}\) | agree | Same structure. |
| \(G'\) LH quark coupling: \(g_{G'}G'^a_\mu\kappa_q^{ij}\bar q_L^iT^a\gamma^\mu q_L^j\) (Eq. 11) | `LGpF`: up-sector \(V_{ki}V^*_{nj}\bar u_kT^A\gamma^\mu P_Lu_n\) and down-sector \(\bar d_iT^A\gamma^\mu P_Ld_j\) | agree | Correct expansion using Eq. (12). |
| \(G'\) RH up coupling: \(g_{G'}G'^a_\mu\kappa_u^{ij}\bar u_R^iT^a\gamma^\mu u_R^j\) (Eq. 11) | `LGpF`: \(\kappa^u_{ij}\bar u_iT^A\gamma^\mu P_Ru_j\) | agree | Same chirality, color generator, and coefficient. |
| \(G'\) RH down coupling: \(g_{G'}G'^a_\mu\kappa_d^{ij}\bar d_R^iT^a\gamma^\mu d_R^j\) (Eq. 11) | `LGpF`: \(\kappa^d_{ij}\bar d_iT^A\gamma^\mu P_Rd_j\) | agree | Same chirality, color generator, and coefficient. |
| \(G'\) flavor textures: \(\kappa_Q=\mathrm{diag}(\kappa_Q^{ll},\kappa_Q^{ll},\kappa_Q^{33})\), \(Q=q,u,d\) (Eq. 13) | Nonzero diagonal light-pair and third-generation entries for \(\kappa^q,\kappa^u,\kappa^d\) | agree | Matches Eq. (13). |
| Paper neglects Higgs couplings to \(Z'\) and other UV-completion-dependent interactions (Sec. 3) | Reconstruction contains no Higgs couplings or extra UV-sector interactions | agree | Consistent with the stated phenomenological setup. |
| Gauge-model limit: \(\kappa_U=\tilde\kappa_U=\kappa_{G'}=\tilde\kappa_{G'}=0\); later analyses take \(\kappa_{G'}=0\) (below Eq. 11) | External parameters default these anomalous couplings to zero | agree | The reconstruction captures the implementation benchmark, not just the symbolic Lagrangian. |
| `VLQ` carries `LeptonNumber -> -1` | No explicit lepton-number assignment for \(U_1\) in the paper Lagrangian | extra-in-reconstruction | This is an implementation bookkeeping convention; it is not an additional interaction. |
| `U` listed as an unphysical alias of `VLQ` | No separate alias field in the paper | extra-in-reconstruction | Cosmetic implementation detail, not a distinct physical state. |

## Disagreements and Human Checks

1. **Missing \(U_1\) mass term** — severity: **substantive**.  
   A human should check whether the implementation supplies the vector mass solely through particle declarations in a way that FeynRules/UFO treats equivalently, or whether the Lagrangian object itself is incomplete.

2. **Missing \(Z'\) kinetic term** — severity: **substantive**.  
   A human should check whether a separate `LZpKin` exists outside the reconstructed `LLeptoQuark` sum or whether the reconstruction/implementation accidentally omits the propagating \(Z'\) kinetic term.

3. **Missing \(Z'\) mass term** — severity: **substantive**.  
   A human should check whether the \(Z'\) mass is generated from particle metadata only, or whether the Lagrangian used for model export lacks the paper’s \(\frac12M_{Z'}^2Z'_\mu Z'^\mu\) term.

4. **Missing \(G'\) mass term** — severity: **substantive**.  
   A human should check whether the coloron mass is included elsewhere in the implementation or only assigned as a particle property.

5. **Implementation-only lepton-number assignment for `VLQ`** — severity: **cosmetic**.  
   A human should check that this bookkeeping charge does not enforce unintended selection rules or conflict with the intended \(U_1\) interactions.

6. **Implementation-only unphysical alias `U` for `VLQ`** — severity: **cosmetic**.  
   A human should check that the alias is not exported as an additional physical vector state.

## Overall Assessment

The reconstruction captures the paper’s main physics content very closely for the interaction terms: field representations, chiral structures, CKM rotations, color factors, anomalous gauge-field couplings, and the benchmark flavor textures all match Eqs. (9)–(13) up to notation. The important gaps are in the explicit propagator-sector terms: the paper writes mass terms for all three new vectors and a kinetic term for \(Z'\), while the reconstructed summed Lagrangian omits them, even though masses are listed separately in the field table. The main review question is therefore not the fermionic or gauge-interaction structure, which appears consistent, but whether the implementation supplies the omitted kinetic/mass pieces elsewhere in a form equivalent to the paper’s Lagrangian.