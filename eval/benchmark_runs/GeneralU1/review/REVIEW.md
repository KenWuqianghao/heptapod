# Reverse-check review package — `GeneralU1_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `GeneralU1/repair/final.fr` |
| original model name | `GeneralU1_gen` (hidden from the agent) |
| paper | GeneralU1/text/2104.10902.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LZpF` (`:=`)

```mathematica
Block[{ff,sp1,sp2,sp3,mu,cc}, -gX Zp[mu] (qQLX uqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjM[sp2,sp3].uq[sp3,ff,cc] + qQLX dqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjM[sp2,sp3].dq[sp3,ff,cc] + qURX uqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].uq[sp3,ff,cc] + qDRX dqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].dq[sp3,ff,cc] + qLLX vlbar[sp1,ff].Ga[mu,sp1,sp2].ProjM[sp2,sp3].vl[sp3,ff] + qLLX lbar[sp1,ff].Ga[mu,sp1,sp2].ProjM[sp2,sp3].l[sp3,ff] + qERX lbar[sp1,ff].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,ff] + qNRX NRbar[sp1,ff].Ga[mu,sp1,sp2].ProjP[sp2,sp3].NR[sp3,ff])]
```

### `LPhiXKin` (`:=`)

```mathematica
Block[{mu}, del[PhiXbar[],mu] del[PhiX[],mu] + I*gX*qPhiX*Zp[mu]*(PhiXbar[] del[PhiX[],mu] - del[PhiXbar[],mu] PhiX[]) + gX^2*qPhiX^2 Zp[mu] Zp[mu] PhiXbar[] PhiX[]]
```

### `LHiggsX` (`:=`)

```mathematica
Block[{ii,mu}, ExpandIndices[I*gX*qHX*Zp[mu]*(Phibar[ii] DC[Phi[ii],mu] - DC[Phibar[ii],mu] Phi[ii]) + gX^2*qHX^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand->{SU2D,SU2W}]]
```

### `VPhiX` (`:=`)

```mathematica
Block[{ii}, ExpandIndices[mPhi2 PhiXbar[] PhiX[] + lamPhi (PhiXbar[] PhiX[])^2 + lamHP (Phibar[ii] Phi[ii]) (PhiXbar[] PhiX[]), FlavorExpand->{SU2D,SU2W}]]
```

### `LNuDiracYuk` (`:=`)

```mathematica
Block[{ff1,ff2,ii,sp1,sp2}, ExpandIndices[-yNu[ff1,ff2] LLbar[sp1,ii,ff1].ProjP[sp1,sp2].NR[sp2,ff2] Phibar[ii], FlavorExpand->SU2D]]
```

### `LNuMajoranaYuk` (`:=`)

```mathematica
Block[{ff,sp1,sp2}, -1/2 yN[ff] PhiX[] NRbar[sp1,ff].ProjP[sp1,sp2].NR[sp2,ff] - 1/2 yN[ff] PhiXbar[] NRbar[sp1,ff].ProjM[sp1,sp2].NR[sp2,ff]]
```

### `LTot` (`:=`)

```mathematica
LZpF + LPhiXKin + LHiggsX - VPhiX + LNuDiracYuk + HC[LNuDiracYuk] + LNuMajoranaYuk
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

The total Lagrangian defined in the file is
\[
\mathcal L_{\rm Tot}
=
\mathcal L_{\rm ZpF}
+\mathcal L_{\rm PhiXKin}
+\mathcal L_{\rm HiggsX}
-V_{\rm PhiX}
+\mathcal L_{\rm NuDiracYuk}
+\mathcal L_{\rm NuDiracYuk}^{\dagger}
+\mathcal L_{\rm NuMajoranaYuk}.
\]

The new Abelian covariant derivative convention used by the file is
\[
D_\mu = D_\mu^{\rm SM} + i g_X q_X Z'_\mu ,
\]
where, for the SM Higgs doublet,
\[
D_\mu^{\rm SM} H
=
\left(
\partial_\mu
+i g\, W_\mu^a T^a
+i g'\, Y_H B_\mu
\right)H .
\]
For the singlet scalar \(\Phi_X\), only the new \(U(1)_X\) gauge field appears:
\[
D_\mu \Phi_X =
\left(\partial_\mu+i g_X q_X^\Phi Z'_\mu\right)\Phi_X .
\]

The chiral projectors are
\[
P_L=\frac{1-\gamma^5}{2},\qquad
P_R=\frac{1+\gamma^5}{2}.
\]

### `LZpF`

\[
\mathcal L_{\rm ZpF}
=
-g_X Z'_\mu
\sum_{f=1}^{3}
\left[
q_X^Q
\left(
\bar u_f \gamma^\mu P_L u_f
+
\bar d_f \gamma^\mu P_L d_f
\right)
+
q_X^u \bar u_f \gamma^\mu P_R u_f
+
q_X^d \bar d_f \gamma^\mu P_R d_f
\right.
\]
\[
\left.
+
q_X^L
\left(
\bar\nu_f \gamma^\mu P_L \nu_f
+
\bar e_f \gamma^\mu P_L e_f
\right)
+
q_X^e \bar e_f \gamma^\mu P_R e_f
+
q_X^N \bar N_f \gamma^\mu P_R N_f
\right].
\]

Color indices are summed for the quark bilinears. Generation index \(f=1,2,3\) is summed.

The \(U(1)_X\) charges are defined internally as
\[
q_X^Q=\frac{x_H}{6}+\frac{x_\Phi}{3},
\qquad
q_X^u=\frac{2x_H}{3}+\frac{x_\Phi}{3},
\qquad
q_X^d=-\frac{x_H}{3}+\frac{x_\Phi}{3},
\]
\[
q_X^L=-\frac{x_H}{2}-x_\Phi,
\qquad
q_X^e=-x_H-x_\Phi,
\qquad
q_X^N=-x_\Phi,
\]
\[
q_X^H=-\frac{x_H}{2},
\qquad
q_X^\Phi=2x_\Phi .
\]

### `LPhiXKin`

\[
\mathcal L_{\rm PhiXKin}
=
\partial_\mu \Phi_X^\dagger \partial^\mu \Phi_X
+
i g_X q_X^\Phi Z'_\mu
\left(
\Phi_X^\dagger \partial^\mu \Phi_X
-
\partial^\mu \Phi_X^\dagger \Phi_X
\right)
+
g_X^2 (q_X^\Phi)^2 Z'_\mu Z'^\mu \Phi_X^\dagger \Phi_X .
\]

Equivalently,
\[
\mathcal L_{\rm PhiXKin}
=
(D_\mu \Phi_X)^\dagger D^\mu \Phi_X ,
\qquad
D_\mu \Phi_X=
(\partial_\mu+i g_X q_X^\Phi Z'_\mu)\Phi_X .
\]

The field definition is
\[
\Phi_X
=
\frac{1}{\sqrt 2}
\left(
v_\Phi+\phi_X+iG_{Z'}
\right),
\qquad
v_\Phi=\frac{M_{Z'}}{2g_X}.
\]

### `LHiggsX`

\[
\mathcal L_{\rm HiggsX}
=
i g_X q_X^H Z'_\mu
\left[
H^\dagger D_{\rm SM}^\mu H
-
(D_{\rm SM}^\mu H)^\dagger H
\right]
+
g_X^2 (q_X^H)^2 Z'_\mu Z'^\mu H^\dagger H .
\]

This is the \(U(1)_X\)-dependent part of
\[
(D_\mu H)^\dagger D^\mu H,
\qquad
D_\mu H=
D_\mu^{\rm SM}H+i g_X q_X^H Z'_\mu H .
\]

### `VPhiX`

The file defines
\[
V_{\rm PhiX}
=
m_\Phi^2\, \Phi_X^\dagger \Phi_X
+
\lambda_\Phi
(\Phi_X^\dagger \Phi_X)^2
+
\lambda'
(H^\dagger H)(\Phi_X^\dagger \Phi_X).
\]

It enters the total Lagrangian as
\[
\mathcal L \supset -V_{\rm PhiX}.
\]

### `LNuDiracYuk`

\[
\mathcal L_{\rm NuDiracYuk}
=
-
\sum_{i,j=1}^{3}
(Y_\nu)_{ij}\,
\bar L_i\, P_R N_j\, H^\dagger
\]

with the \(SU(2)\) index contracted as written in the file:
\[
\mathcal L_{\rm NuDiracYuk}
=
-
(Y_\nu)_{ij}\,
\bar L_{i,a}\,P_R N_j\,H_a^\dagger .
\]

The total Lagrangian also includes its Hermitian conjugate:
\[
\mathcal L_{\rm NuDiracYuk}^\dagger
=
-
(Y_\nu)_{ij}^*\,
H_a\,\bar N_j P_L L_{i,a}.
\]

The file declares \(Y_\nu\) real, so \(Y_\nu^*=Y_\nu\).

### `LNuMajoranaYuk`

\[
\mathcal L_{\rm NuMajoranaYuk}
=
-\frac12
\sum_{i=1}^{3}
Y_{N_i}\,
\Phi_X\,
\bar N_i P_R N_i
-
\frac12
\sum_{i=1}^{3}
Y_{N_i}\,
\Phi_X^\dagger\,
\bar N_i P_L N_i .
\]

Equivalently, in two-component chiral notation,
\[
\mathcal L_{\rm NuMajoranaYuk}
=
-\frac12
\sum_i
Y_{N_i}\,
\Phi_X\,
\overline{N_{Ri}^{\,c}}\,N_{Ri}
+\text{h.c.}
\]

The internal Yukawa definitions are
\[
Y_{N_i}=\frac{\sqrt2\,m_{N_i}}{v_\Phi}.
\]

## Field Table

| `.fr` class | Symbol | Spin | SU(3) | SU(2) | \(U(1)\) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---|---:|---|
| `V[100]` | `Zp` \((Z'_\mu)\) | 1 | singlet | singlet | gauge boson of \(U(1)_X\); no matter charge assigned | yes | \(M_{Z'}=\texttt{MZp}=7500\) |
| `F[101]` | `NR` \((N_1,N_2,N_3)\) | 1/2 | singlet | singlet | right-chiral component has \(q_X^N=-x_\Phi\) | yes, Majorana | \(m_{N_1}=m_{N_2}=m_{N_3}=10000\) |
| `S[102]` | `phiX` \((\phi_X)\) | 0 | singlet | singlet | real excitation of \(\Phi_X\), whose parent has \(X=2x_\Phi\), \(Q=0\), \(Y=0\) | yes | \(m_{\phi_X}=1000\) |
| `S[103]` | `GZp` \((G_{Z'})\) | 0 | singlet | singlet | Goldstone component of \(\Phi_X\), whose parent has \(X=2x_\Phi\), \(Q=0\), \(Y=0\) | yes | \(M_{Z'}=7500\) |
| `S[104]` | `PhiX` \((\Phi_X)\) | 0 | singlet | singlet | \(Q=0,\;Y=0,\;X=2x_\Phi\) | no | unphysical field, \(\Phi_X=(v_\Phi+\phi_X+iG_{Z'})/\sqrt2\) |

## Parameters

| Parameter | Value in file | Multiplies / controls | Physical meaning |
|---|---:|---|---|
| `gX` | \(0.1\) | every \(Z'\) interaction and \(U(1)_X\) covariant derivative | new Abelian gauge coupling |
| `xH` | \(0\) | internal charge definitions \(q_X^Q,q_X^u,q_X^d,q_X^L,q_X^e,q_X^H\) | coefficient controlling the hypercharge-like part of the \(U(1)_X\) charge assignment |
| `xPhi` | \(1\) | internal charge definitions, especially \(q_X^\Phi=2x_\Phi\) and \(q_X^N=-x_\Phi\) | coefficient controlling the singlet-scalar and right-handed-neutrino \(U(1)_X\) charge normalization |
| `lamPhi` | \(0.1\) | \((\Phi_X^\dagger\Phi_X)^2\) in `VPhiX` | quartic self-coupling of the new complex singlet scalar |
| `lamHP` | \(0\) | \((H^\dagger H)(\Phi_X^\dagger\Phi_X)\) in `VPhiX` | Higgs-portal quartic coupling |
| `mPhi2` | \(1000000\) | \(\Phi_X^\dagger\Phi_X\) in `VPhiX` | quadratic scalar-potential mass parameter for \(\Phi_X\) |
| `yNu[i,j]` | all entries \(0\) | \(- (Y_\nu)_{ij}\bar L_i P_R N_j H^\dagger+\text{h.c.}\) | Dirac neutrino Yukawa matrix coupling SM lepton doublets to the new Majorana singlets |

The file also defines the following internal parameters:
\[
v_\Phi=\frac{M_{Z'}}{2g_X},
\qquad
Y_{N_i}=\frac{\sqrt2\,m_{N_i}}{v_\Phi}.
\]

## Physics Summary

The file encodes a \(U(1)_X\) extension of the Standard Model with a new neutral gauge boson \(Z'\), three self-conjugate singlet fermions \(N_i\), and a complex singlet scalar \(\Phi_X\) whose vacuum expectation value breaks the new gauge symmetry and supplies the \(Z'\) and \(N_i\) masses. The \(Z'\) couples chirally to SM quarks, charged leptons, neutrinos, and the right-handed component of the Majorana singlets with charges determined by \(x_H\) and \(x_\Phi\).

It mediates dilepton, dijet, neutrino, and heavy-neutral-lepton production through \(s\)-channel \(Z'\) exchange, while the scalar sector allows singlet-Higgs portal interactions and Majorana mass generation through \(\Phi_X \overline{N_R^c}N_R\).

## Paper cross-check

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

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 20 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

