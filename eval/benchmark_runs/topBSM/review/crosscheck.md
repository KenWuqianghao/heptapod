**Lagrangian And Field Definitions**

The paper defines an EFT in the **INTRODUCTION** and **SETUP** sections. The master EFT Lagrangian is Eq. (1):
\[
\mathcal L_{\rm EFT}=\mathcal L_{\rm SM}+\sum_i \frac{C_i O_i}{\Lambda^2}+{\rm H.c.}
\]
The field notation is given in **SETUP**: \(Q\) is the third-generation left-handed quark doublet, \(q\) is a first- or second-generation left-handed quark doublet, \(t\) is the right-handed top quark, \(u,c\) are right-handed up/charm quarks, \(\phi\) is the Higgs doublet, and \(\tilde\phi=i\sigma_2\phi\).

The paper’s defining dimension-six operators are Eqs. (2)-(5):
\[
O^{(1,3)}_{uG}=y_t g_s(\bar q\sigma^{\mu\nu}T^A t)\tilde\phi G^A_{\mu\nu},
\]
\[
O^{(1,3)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar q t)\tilde\phi,
\]
\[
O^{(3,1)}_{uG}=y_t g_s(\bar Q\sigma^{\mu\nu}T^A u)\tilde\phi G^A_{\mu\nu},
\]
\[
O^{(3,1)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar Q u)\tilde\phi.
\]
The tree-level \(tuh\) interaction is Eq. (8), modified after removing \(u_L-t_R\) mixing to Eq. (11):
\[
\mathcal L'_{tuh}=
-C_{u\phi}\frac{m_t^2}{\Lambda^2}\frac{2y_t}{\sqrt2}(\bar u P_R t)h+{\rm H.c.}
\]
The paper also gives the effective \(utg\) interaction from \(O_{uG}\) in Eq. (30):
\[
\mathcal L_{\rm Eff}=
-\frac{C_{uG}}{\Lambda^2}2m_tg_s(\bar u_L\sigma^{\mu\nu}T^A t_R)\partial_\nu G^A_\mu.
\]

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| SM field content \(Q,q,t,u,c,\phi,\tilde\phi\) in **SETUP** | New fields \(S0,O0,S1,O1,S2\) plus SM fermions | disagree | The paper defines only SM fields in an EFT basis; the reconstruction defines new neutral spin-0, spin-1, and spin-2 resonances absent from the paper. |
| \(\mathcal L_{\rm EFT}=\mathcal L_{\rm SM}+\sum_i C_iO_i/\Lambda^2+{\rm H.c.}\), Eq. (1) | Sum of explicit resonance interactions \(\mathcal L_{S0},\mathcal L_{O0},\mathcal L_{S1},\mathcal L_{O1}\) | disagree | Paper is a dimension-six SM EFT; reconstruction is a simplified resonance model with independent new fields. |
| \(O^{(1,3)}_{uG}=y_tg_s(\bar q\sigma^{\mu\nu}T^At)\tilde\phi G^A_{\mu\nu}\), Eq. (2) | None | missing-in-reconstruction | No flavor-changing chromomagnetic \(q_L-t_R\) operator appears. |
| \(O^{(1,3)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar qt)\tilde\phi\), Eq. (3) | None | missing-in-reconstruction | No dimension-six flavor-changing Higgs-Yukawa operator appears. |
| \(O^{(3,1)}_{uG}=y_tg_s(\bar Q\sigma^{\mu\nu}T^Au)\tilde\phi G^A_{\mu\nu}\), Eq. (4) | None | missing-in-reconstruction | No opposite-flavor chromomagnetic operator involving \(Q_L\) and \(u_R/c_R\) appears. |
| \(O^{(3,1)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar Qu)\tilde\phi\), Eq. (5) | None | missing-in-reconstruction | No opposite-flavor Higgs-Yukawa operator involving \(Q_L\) and \(u_R/c_R\) appears. |
| Hermitian conjugates of Eqs. (2)-(5), discussed after Eq. (5) | Self-conjugate resonance fields and ordinary bilinears | disagree | The paper requires H.c. flavor-changing operators with chirality-flipped contributions; reconstruction has real self-conjugate bosons and flavor-diagonal currents. |
| \(y_t=\sqrt2m_t/v\), Eq. (7) | Uses \(m_t/v\) in scalar-top terms | convention | Related normalization appears, but the reconstruction applies it to new scalar resonance couplings rather than the paper’s EFT operators. |
| Tree-level \(tuh\) interaction \(-C_{u\phi}m_t^2\Lambda^{-2}(3y_t/\sqrt2)(\bar uP_Rt)h+{\rm H.c.}\), Eq. (8) | None | missing-in-reconstruction | Reconstruction contains no Higgs field \(h\), no \(t-u/c\) flavor change, and no \(P_R\) chiral structure of this kind. |
| Field rotations removing \(u_L-t_R\) mixing, Eqs. (9)-(10) | None | missing-in-reconstruction | Reconstruction has no flavor-changing mass mixing induced by \(O_{u\phi}\). |
| Rotated \(tuh\) interaction \(-C_{u\phi}m_t^2\Lambda^{-2}(2y_t/\sqrt2)(\bar uP_Rt)h+{\rm H.c.}\), Eq. (11) | None | missing-in-reconstruction | This is the paper’s physical tree-level \(tuh\) vertex after diagonalization; reconstruction has no counterpart. |
| Counterterm form \(O_{u\phi}\to -y_t^3(\phi^\dagger\phi-v^2/2)(\bar qt)\tilde\phi\), Eq. (12) | None | missing-in-reconstruction | Reconstruction has no Higgs-doublet EFT operator or subtraction of the vev-induced mixing term. |
| Effective decomposition \(\mathcal L_{\rm Eff}=\mathcal L_{tu}+\mathcal L_{tuh}\), Eqs. (25)-(27) | None | missing-in-reconstruction | Reconstruction lacks the \(u_L-t_R\) mixing and \(tuh\) counterterm structure. |
| \(utg\) dipole interaction from \(O_{uG}\), Eq. (30) | None | missing-in-reconstruction | Reconstruction has gluon field-strength operators, but they couple gluons to new scalars, not to a flavor-changing quark dipole. |
| EOM-vanishing counterterm operators \(O^{(1)},O^{(2)}\), Eqs. (33)-(34) | None | missing-in-reconstruction | These are part of the paper’s renormalization treatment of \(O_{uG}\); reconstruction has no analogous EFT renormalization structure. |
| Renormalized effective Lagrangian with \(C_{u\phi}\), \(C_{uG}\), and mixing counterterms, Eq. (37) | None | missing-in-reconstruction | Reconstruction does not contain Wilson coefficients \(C_{u\phi},C_{uG}\), operator mixing, or dimension-six counterterms. |
| None | \(S0\,\bar tt\) scalar coupling | extra-in-reconstruction | No color-singlet scalar resonance \(S0\) or flavor-diagonal \(S0\bar tt\) interaction is defined in the paper. |
| None | \(iS0\,\bar t\gamma^5t\) pseudoscalar coupling | extra-in-reconstruction | No pseudoscalar top resonance coupling appears in the paper. |
| None | \(S0\,G^a_{\mu\nu}G^{a\mu\nu}\) | extra-in-reconstruction | Paper has a chromomagnetic quark-Higgs-gluon operator, not a scalar-gluon-gluon effective resonance operator. |
| None | \(S0\,G^a_{\mu\nu}\tilde G^{a\mu\nu}\) | extra-in-reconstruction | No CP-odd scalar-gluon-gluon operator is part of the paper’s model. |
| None | \(O0^a\bar tT^at\) scalar color-octet coupling | extra-in-reconstruction | Paper has no color-octet scalar resonance. |
| None | \(iO0^a\bar t\gamma^5T^at\) color-octet pseudoscalar coupling | extra-in-reconstruction | Paper has no color-octet pseudoscalar top coupling. |
| None | \(d^{abc}O0^aG^b_{\mu\nu}G^{c\mu\nu}\) | extra-in-reconstruction | Paper has no \(d^{abc}\) scalar-octet gluon-fusion operator. |
| None | \(d^{abc}O0^aG^b_{\mu\nu}\tilde G^{c\mu\nu}\) | extra-in-reconstruction | Paper has no CP-odd color-octet scalar-gluon operator. |
| None | \(S1_\mu\bar u_L\gamma^\mu u_L\), \(S1_\mu\bar d_L\gamma^\mu d_L\), \(S1_\mu\bar u_R\gamma^\mu u_R\), \(S1_\mu\bar d_R\gamma^\mu d_R\) | extra-in-reconstruction | Paper has no neutral color-singlet vector resonance or flavor-diagonal quark-current interactions. |
| None | \(S1_\mu\bar e_L\gamma^\mu e_L\), \(S1_\mu\bar e_R\gamma^\mu e_R\), \(S1_\mu\bar\nu_L\gamma^\mu\nu_L\) | extra-in-reconstruction | Paper does not introduce lepton-current couplings. |
| None | \(O1^a_\mu\bar u_{L,R}\gamma^\mu T^au_{L,R}\), \(O1^a_\mu\bar d_{L,R}\gamma^\mu T^ad_{L,R}\) | extra-in-reconstruction | Paper has no color-octet vector resonance or flavor-diagonal color-current couplings. |
| None | Tensor field \(S2\), neutral singlet, no interactions | extra-in-reconstruction | No spin-2 field is present in the paper. |

**Disagreements**

| item | severity | what a human should check |
|---|---|---|
| Reconstruction introduces \(S0,O0,S1,O1,S2\) resonance fields absent from the paper. | substantive | Check whether `reconstruction.md` came from a different model file than the paper, possibly a generic resonance implementation. |
| Paper’s EFT master Lagrangian Eq. (1) is not reproduced. | substantive | Verify whether the implementation was supposed to encode the paper’s dimension-six EFT or a separate phenomenological model. |
| Missing \(O^{(1,3)}_{uG}\), Eq. (2). | substantive | Check for any hidden flavor-changing top-light-quark chromomagnetic operator in the original implementation. |
| Missing \(O^{(1,3)}_{u\phi}\), Eq. (3). | substantive | Check whether the implementation contains a \(tuh\) FCNC Yukawa vertex under another name. |
| Missing \(O^{(3,1)}_{uG}\), Eq. (4). | substantive | Check whether chirality-flipped or conjugate flavor structures were intentionally omitted. |
| Missing \(O^{(3,1)}_{u\phi}\), Eq. (5). | substantive | Check whether the implementation supports both \(t\to uh/ch\) chiralities. |
| Reconstruction lacks the paper’s Hermitian-conjugate FCNC structure. | substantive | Check whether both decay and conjugate amplitudes are generated in the implementation. |
| Reconstruction uses \(m_t/v\) normalization for unrelated scalar-top resonance couplings. | convention | Check whether this normalization was copied from another simplified model and not from the EFT paper. |
| Missing paper’s tree-level \(tuh\) interaction Eq. (8). | substantive | Check generated Feynman rules for a \(t-u/c-h\) vertex. |
| Missing field rotations Eqs. (9)-(10). | substantive | Check whether mass diagonalization or equivalent counterterms are implemented. |
| Missing physical rotated \(tuh\) coupling Eq. (11). | substantive | Check whether the implementation uses the correct factor \(2y_t/\sqrt2\), not the pre-rotation factor \(3y_t/\sqrt2\). |
| Missing counterterm-subtracted \(O_{u\phi}\) form Eq. (12). | substantive | Check whether vev-induced \(u_L-t_R\) mixing is removed consistently. |
| Missing \(\mathcal L_{tu}+\mathcal L_{tuh}\) counterterm structure Eqs. (25)-(27). | substantive | Check whether NLO renormalization was implemented at all. |
| Missing \(utg\) dipole interaction Eq. (30). | substantive | Check whether the implementation contains a flavor-changing \(t-u/c-g\) dipole vertex rather than only gluon-fusion resonance operators. |
| Missing EOM-vanishing counterterms Eqs. (33)-(34). | substantive | Check whether the implementation is intended only for tree level or includes the NLO operator-renormalization setup. |
| Missing renormalized Lagrangian Eq. (37). | substantive | Check whether Wilson-coefficient mixing \(C_{uG}\to C_{u\phi}\) is encoded elsewhere. |
| Extra \(S0\bar tt\), \(S0GG\), and \(S0G\tilde G\) terms. | substantive | Check whether the source implementation is for a scalar resonance model, not this FCNC Higgs EFT paper. |
| Extra \(O0\bar tT^at\), \(O0GG\), and \(O0G\tilde G\) terms. | substantive | Check whether color-octet scalar resonance interactions belong to another paper or benchmark. |
| Extra \(S1\) flavor-diagonal quark and lepton currents. | substantive | Check whether a \(Z'\)-like model was accidentally reconstructed instead of the paper’s EFT. |
| Extra \(O1\) color-octet vector quark currents. | substantive | Check whether an axigluon/coloron model was mixed into the reconstruction. |
| Extra inert spin-2 field \(S2\). | substantive | Check whether the implementation file contains unused benchmark particles unrelated to the paper. |

**Overall Assessment**

The reconstruction does not match the model defined in the paper. The paper is a Standard Model EFT treatment of flavor-changing top-Higgs interactions, centered on the dimension-six operators \(O_{uG}\) and \(O_{u\phi}\), their flavor assignments, chirality structure, Higgs-doublet dependence, and NLO QCD renormalization. The reconstruction instead describes a simplified resonance model with new scalar, vector, color-octet, and tensor fields coupled mostly to flavor-diagonal SM currents or gluon-fusion operators. Apart from incidental use of familiar SM quantities such as \(m_t/v\), \(g_s\), and color generators, the field content, operator basis, charges, chirality structure, and coefficient organization are substantively different.