# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Location

The paper defines the minimal \(U(1)_X\) model in **Sec. II, “The \(U(1)_X\) Model”**. The relevant definitions are:

- **Table I**: gauge representations and \(U(1)_X\) charges of \(q_L,u_R,d_R,\ell_L,e_R,N_R,H,\Phi\).
- **Eq. (1)**: Yukawa interactions.
- **Eq. (2)**: renormalizable Higgs potential.
- **Eq. (3)**: scalar VEVs.
- **Eq. (4)**: \(Z'\) mass after symmetry breaking.
- **Eq. (6)**: \(Z'\) interactions with SM fermions.
- **Eqs. (7)-(9)**: partial widths, including light neutrino and RHN couplings.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---:|---|
| Gauge group \(SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X\), Sec. II | Same model summarized as a \(U(1)_X\) extension | **agree** | Same gauge extension. |
| Field content and reps for SM fermions, \(N_R\), \(H\), \(\Phi\), Table I | New-field table plus \(U(1)_X\) charge formulas for SM fermions | **missing-in-reconstruction** | Reconstruction does not give the full SM field representation table under \(SU(3)_C\), \(SU(2)_L\), \(U(1)_Y\), though it does encode their \(U(1)_X\) charges in the \(Z'\) couplings. |
| \(q_X(q_L)=\frac{x_H}{6}+\frac{x_\Phi}{3}\), Table I | \(q_X^Q=\frac{x_H}{6}+\frac{x_\Phi}{3}\) | **agree** | Matches. |
| \(q_X(u_R)=\frac{2x_H}{3}+\frac{x_\Phi}{3}\), Table I | \(q_X^u=\frac{2x_H}{3}+\frac{x_\Phi}{3}\) | **agree** | Matches. |
| \(q_X(d_R)=-\frac{x_H}{3}+\frac{x_\Phi}{3}\), Table I | \(q_X^d=-\frac{x_H}{3}+\frac{x_\Phi}{3}\) | **agree** | Matches. |
| \(q_X(\ell_L)=-\frac{x_H}{2}-x_\Phi\), Table I | \(q_X^L=-\frac{x_H}{2}-x_\Phi\) | **agree** | Matches. |
| \(q_X(e_R)=-x_H-x_\Phi\), Table I | \(q_X^e=-x_H-x_\Phi\) | **agree** | Matches. |
| \(q_X(N_R)=-x_\Phi\), Table I | \(q_X^N=-x_\Phi\) | **agree** | Matches. |
| \(q_X(H)=-\frac{x_H}{2}\), Table I | \(q_X^H=-\frac{x_H}{2}\) | **agree** | Matches. |
| \(q_X(\Phi)=2x_\Phi\), Table I | \(q_X^\Phi=2x_\Phi\) | **agree** | Matches. |
| Full Yukawa sector, Eq. (1): quark and charged-lepton Yukawas plus neutrino Yukawas | Reconstruction includes only neutrino Dirac and Majorana Yukawas | **missing-in-reconstruction** | The paper’s SM Yukawa terms \(Y_u,Y_d,Y_e\) are absent. This may be intentional if the implementation only reconstructs the new-sector additions, but it is not the full paper Lagrangian. |
| Dirac neutrino Yukawa, Eq. (1): \(-Y_\nu^{\alpha\beta}\ell_L^\alpha H N_R^\beta+\text{H.c.}\), as printed | \(- (Y_\nu)_{ij}\bar L_{i,a}P_RN_j H_a^\dagger+\text{H.c.}\) | **disagree** | The reconstruction uses \(H^\dagger\). With Table I charges, the gauge-invariant \(U(1)_X\) contraction uses the Higgs field carrying \(q_X(H)=-x_H/2\), not its conjugate. The reconstruction term is only \(U(1)_X\)-neutral for special choices such as \(x_H=0\). |
| Majorana Yukawa, Eq. (1): \(-Y_N^\alpha\Phi N_R^{\alpha c}N_R^\alpha+\text{H.c.}\) | \(-\frac12Y_{N_i}\Phi_X\bar NP_RN-\frac12Y_{N_i}\Phi_X^\dagger\bar NP_LN\) | **agree** | Same physics in four-component Majorana notation. The factor \(1/2\) is conventional for Majorana four-component writing. |
| Higgs potential, Eq. (2): \(-m_h^2H^\dagger H+\lambda(H^\dagger H)^2+m_\Phi^2\Phi^\dagger\Phi+\lambda_\Phi(\Phi^\dagger\Phi)^2+\lambda'(H^\dagger H)(\Phi^\dagger\Phi)\) | \(m_\Phi^2\Phi_X^\dagger\Phi_X+\lambda_\Phi(\Phi_X^\dagger\Phi_X)^2+\lambda'(H^\dagger H)(\Phi_X^\dagger\Phi_X)\), entering as \(-V\) | **missing-in-reconstruction** | The \(\Phi\) mass, \(\Phi\) quartic, and portal terms agree, but the SM Higgs potential terms \(-m_h^2H^\dagger H+\lambda(H^\dagger H)^2\) are missing. |
| Scalar VEVs, Eq. (3): \(\langle H\rangle\) and \(\langle\Phi\rangle=(v_\Phi+\phi)/\sqrt2\) | \(\Phi_X=(v_\Phi+\phi_X+iG_{Z'})/\sqrt2\) | **agree** | The \(\Phi\) expansion agrees up to inclusion of the Goldstone mode. The reconstruction does not state the Higgs VEV. |
| Higgs VEV, Eq. (3): \(\langle H\rangle\) with electroweak VEV \(v\simeq246\) GeV | Not included | **missing-in-reconstruction** | The reconstruction uses \(H\) in interactions but omits the Higgs VEV definition. |
| \(Z'\) mass, Eq. (4): \(M_{Z'}=g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}\simeq2g'v_\Phi\) | \(v_\Phi=M_{Z'}/(2g_X)\) | **agree** | Agrees with the paper’s large-\(v_\Phi\), \(x_\Phi=1\) approximation. The reconstruction does not retain the small electroweak contribution proportional to \(x_H^2v^2\). |
| \(Z'\) couplings to SM quarks and leptons, Eq. (6) | \(-g_XZ'_\mu\sum_f[\cdots]\) with \(P_L,P_R\) charges | **agree** | Same chiral charge structure, modulo notation \(g_X\leftrightarrow g'\). |
| \(Z'\) coupling to light neutrinos, implied by Table I and Eq. (8) | \(q_X^L\bar\nu\gamma^\mu P_L\nu\) | **agree** | Same left-handed light-neutrino coupling. |
| \(Z'\) coupling to RHNs, Table I and Eq. (9) | \(q_X^N\bar N\gamma^\mu P_RN\) | **agree** | Same right-chiral RHN charge. In Majorana notation this corresponds to the usual chiral/axial current. |
| \(\Phi\) kinetic term implied by gauge symmetry and used in Eq. (4) | \((D_\mu\Phi_X)^\dagger D^\mu\Phi_X\) expanded | **agree** | Correct covariant derivative structure with \(q_X^\Phi=2x_\Phi\). |
| Higgs \(U(1)_X\) covariant kinetic contribution implied by Table I and Eq. (4) | \(U(1)_X\)-dependent part of \((D_\mu H)^\dagger D^\mu H\) | **agree** | Correct \(q_X^H=-x_H/2\) dependence. |
| Explicit Goldstone field \(G_{Z'}\) and unphysical \(\Phi_X\) component fields | Included in field table | **extra-in-reconstruction** | The paper writes only the physical singlet fluctuation \(\phi\) in Eq. (3). The Goldstone is an implementation-level gauge-basis detail, not a physics conflict. |
| Fixed parameter values \(g_X=0.1\), \(x_H=0\), \(x_\Phi=1\), \(M_{Z'}=7500\), \(m_N=10000\), \(m_{\phi_X}=1000\) | Listed as file values | **extra-in-reconstruction** | The paper fixes \(x_\Phi=1\) without loss of generality and often uses \(M_{Z'}=7.5\) TeV benchmarks, but it scans \(x_H\) and commonly uses different \(g'\) values. These are implementation benchmark choices, not general paper definitions. |

## Disagreements and Severity

| issue | severity | what a human should check |
|---|---:|---|
| Dirac neutrino Yukawa uses \(H^\dagger\) in the reconstruction instead of the Higgs contraction appearing in Eq. (1). | **substantive** | Check the original implementation’s \(SU(2)\), hypercharge, and \(U(1)_X\) conventions, because with Table I charges the reconstructed \(H^\dagger\) term is not gauge invariant for general \(x_H\). |
| SM quark and charged-lepton Yukawa terms from Eq. (1) are absent. | **substantive** | Check whether the implementation intentionally reconstructed only BSM additions or was meant to encode the full minimal \(U(1)_X\) Lagrangian. |
| SM Higgs potential terms \(-m_h^2H^\dagger H+\lambda(H^\dagger H)^2\) from Eq. (2) are absent. | **substantive** | Check whether the base SM Higgs sector is imported elsewhere in the implementation or accidentally omitted. |
| Full SM field representation table from Table I is not reproduced. | **cosmetic** | Check whether the reconstruction was intended to document only new fields and derived \(U(1)_X\) charges rather than the full model content. |
| Higgs VEV from Eq. (3) is omitted. | **convention** | Check whether electroweak symmetry breaking is handled by an external SM model file. |
| \(Z'\) mass relation uses \(v_\Phi=M_{Z'}/(2g_X)\), dropping the \(x_H^2v^2/4\) contribution in Eq. (4). | **convention** | Check whether the implementation is explicitly working in the paper’s \(v_\Phi^2\gg v^2\), \(x_\Phi=1\) approximation. |
| Reconstruction includes explicit \(G_{Z'}\) and unphysical \(\Phi_X\) fields not shown in the paper’s Eq. (3). | **cosmetic** | Check the gauge choice in the implementation; this is likely just an implementation-basis detail. |
| Reconstruction lists fixed benchmark parameters such as \(g_X=0.1\), \(x_H=0\), and \(m_{\phi_X}=1000\). | **convention** | Check whether these are harmless numerical defaults or whether they restrict scans that the paper treats as free parameters. |

## Overall Assessment

The reconstruction captures the central \(U(1)_X\) charge assignment, the chiral \(Z'\) couplings, the singlet-scalar kinetic structure, the \(\Phi\)-sector potential terms, and the RHN Majorana Yukawa structure of the paper’s Sec. II model. The most important physics mismatch is the reconstructed Dirac neutrino Yukawa contraction with \(H^\dagger\), which conflicts with the paper’s Table I charge assignments for general \(x_H\). Several other omissions appear to be boundary choices between a BSM implementation file and a full model definition: the SM Yukawas, SM Higgs potential, SM field reps, and Higgs VEV may live in an imported SM sector, but they are part of the paper’s complete Lagrangian as written.