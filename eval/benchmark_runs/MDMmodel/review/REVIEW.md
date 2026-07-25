# Reverse-check review package — `MDMmodel_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `MDMmodel/repair/final.fr` |
| original model name | `MDMmodel_gen` (hidden from the agent) |
| paper | MDMmodel/text/1311.6661.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LFermionsDM` (`:=`)

```mathematica
Block[{mu, sp, cc}, ExpandIndices[I TLbar.Ga[mu].DC[TL, mu] + I TLbar.Ga[mu].DC[TR, mu] + I TRbar.Ga[mu].DC[TL, mu] + I TRbar.Ga[mu].DC[TR, mu] - Mdltn/vevf S (TLbar[sp, cc].TL[sp, cc] + TLbar[sp, cc].TR[sp, cc] + TRbar[sp, cc].TL[sp, cc] + TRbar[sp, cc].TR[sp, cc]), FlavorExpand -> {SU2W, SU2D}]/.{CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}]
```

### `LHiggsMDM` (`:=`)

```mathematica
Block[{ii, jj, mu, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 | GP | GPbar -> 0}, {}]; ExpandIndices[DC[Phibar[ii], mu] DC[Phi[ii], mu] - 1/2 del[S, mu] del[S, mu] - muS2/2 S^2 - dlams/24 S^4 - dkappa/2 S^2 Phibar[ii] Phi[ii] - muH2 Phibar[ii] Phi[ii] - dlamh/4 Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand -> {SU2D, SU2W}]/.feynmangaugerules]
```

### `LYukawaDM` (`:=`)

```mathematica
Block[{sp, ii, jj, cc, yuk, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 | GP | GPbar -> 0}, {}]; yuk = -yp QLb[sp, ii, 3, cc].TR[sp, cc] Phibar[jj] Eps[ii, jj]; yuk = ExpandIndices[yuk + HC[yuk], FlavorExpand -> SU2D]; yuk = yuk /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}; yuk/.feynmangaugerules]
```

### `LMDMNP` (`:=`)

```mathematica
LFermionsDM + LHiggsMDM + LYukawaDM
```

### `LTot` (`:=`)

```mathematica
LFermionsDM + LHiggsMDM + LYukawaDM
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Field definitions used by the Lagrangian:

\[
S = v_f + s_s\, h + c_s\, s_{\rm DM}
\]

\[
\Phi =
\begin{pmatrix}
-i G^+ \\
\dfrac{v + c_s h - s_s s_{\rm DM} + iG^0}{\sqrt{2}}
\end{pmatrix}
\]

\[
T_L = P_L(-s_l\, t + c_l\, t'), \qquad
T_R = P_R(-s_r\, t + c_r\, t')
\]

with

\[
P_L=\frac{1-\gamma^5}{2}, \qquad P_R=\frac{1+\gamma^5}{2}.
\]

The covariant derivatives are

\[
D_\mu \Phi =
\left(
\partial_\mu
- i g\, W_\mu^a \frac{\sigma^a}{2}
- i g' \frac{1}{2} B_\mu
\right)\Phi ,
\]

\[
D_\mu T =
\left(
\partial_\mu
- i g_s\, G_\mu^A T^A
- i g' \frac{2}{3} B_\mu
\right)T ,
\]

where \(T\) is an \(SU(3)_c\) triplet, \(SU(2)_L\) singlet fermion with \(Y=Q=2/3\). The singlet scalar \(S\) has ordinary derivative \(\partial_\mu S\).

### `LFermionsDM`

\[
\mathcal L_{\mathrm{kin},T}^{\texttt{LFermionsDM}}
=
i\,\overline{T_L}\gamma^\mu D_\mu T_L
+i\,\overline{T_L}\gamma^\mu D_\mu T_R
+i\,\overline{T_R}\gamma^\mu D_\mu T_L
+i\,\overline{T_R}\gamma^\mu D_\mu T_R .
\]

Equivalently, with \(T=T_L+T_R\),

\[
\mathcal L_{\mathrm{kin},T}^{\texttt{LFermionsDM}}
=
i\,\overline T \gamma^\mu D_\mu T .
\]

\[
\mathcal L_{S\overline TT}^{\texttt{LFermionsDM}}
=
-\frac{M_{\Delta}}{v_f}\,
S\,
\left(
\overline{T_L}T_L
+\overline{T_L}T_R
+\overline{T_R}T_L
+\overline{T_R}T_R
\right),
\]

with

\[
M_{\Delta}\equiv \texttt{Mdltn}=M_{T'}c_l .
\]

Equivalently,

\[
\mathcal L_{S\overline TT}^{\texttt{LFermionsDM}}
=
-\frac{M_{\Delta}}{v_f}\,S\,\overline T T .
\]

### `LHiggsMDM`

\[
\mathcal L_{\Phi,\mathrm{kin}}^{\texttt{LHiggsMDM}}
=
(D_\mu\Phi)^\dagger(D^\mu\Phi).
\]

\[
\mathcal L_{S,\mathrm{kin}}^{\texttt{LHiggsMDM}}
=
-\frac12\,\partial_\mu S\,\partial^\mu S .
\]

\[
\mathcal L_{S^2}^{\texttt{LHiggsMDM}}
=
-\frac{\mu_S^2}{2}\,S^2 .
\]

\[
\mathcal L_{S^4}^{\texttt{LHiggsMDM}}
=
-\frac{\lambda_S}{24}\,S^4 .
\]

\[
\mathcal L_{S^2\Phi^\dagger\Phi}^{\texttt{LHiggsMDM}}
=
-\frac{\kappa}{2}\,S^2\,\Phi^\dagger\Phi .
\]

\[
\mathcal L_{\Phi^\dagger\Phi}^{\texttt{LHiggsMDM}}
=
-\mu_H^2\,\Phi^\dagger\Phi .
\]

\[
\mathcal L_{(\Phi^\dagger\Phi)^2}^{\texttt{LHiggsMDM}}
=
-\frac{\lambda_H}{4}\,
(\Phi^\dagger\Phi)^2 .
\]

The parameters appearing here are the internal FeynRules symbols

\[
\kappa=\texttt{dkappa},\qquad
\lambda_H=\texttt{dlamh},\qquad
\lambda_S=\texttt{dlams},
\]

\[
\mu_S^2=\texttt{muS2},\qquad
\mu_H^2=\texttt{muH2}.
\]

### `LYukawaDM`

The FeynRules expression

\[
-\texttt{yp}\;
\overline{Q}_{L,3}^{\,i}\,
T_R\,
\Phi^{\dagger j}\,
\epsilon_{ij}
+\mathrm{h.c.}
\]

is

\[
\mathcal L_{\mathrm{Yuk}}^{\texttt{LYukawaDM}}
=
-y'\,\overline Q_{L,3}^{\,i}\,
\widetilde\Phi_i\,
T_R
+\mathrm{h.c.},
\]

where

\[
\widetilde\Phi_i \equiv \epsilon_{ij}\Phi^{\dagger j},
\qquad
Q_{L,3}=
\begin{pmatrix}
t_L\\
b_L
\end{pmatrix},
\]

and

\[
y'=\texttt{yp}=\frac{\sqrt2}{v}M_{T'}s_l .
\]

The hermitian conjugate is

\[
-y'^{\,*}\,
\overline{T_R}\,
\widetilde\Phi_i^\dagger
Q_{L,3}^{\,i}.
\]

## Field Table

| `.fr` class | Symbol | Spin | SU(3) rep | SU(2) rep | \(U(1)_Y\) / charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---|---|---|
| `S[21]` | `sDM` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | \(M_{s{\rm DM}}=\texttt{MsDM}=173.2\) |
| `F[7]` | `tp` | 1/2 | triplet | singlet | \(Y=2/3,\ Q=2/3\) | no | \(M_{T'}=\texttt{MTP}=1670.3\) |
| `S[31]` | `S` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | unphysical gauge/electroweak-basis field |
| `S[11]` | `Phi` | 0 | singlet | doublet | \(Y=1/2\) | no | unphysical Higgs doublet |
| `F[26]` | `TR` | 1/2 | triplet | singlet | \(Y=2/3,\ Q=2/3\) | no | unphysical right-chiral component |
| `F[27]` | `TL` | 1/2 | triplet | singlet | \(Y=2/3,\ Q=2/3\) | no | unphysical left-chiral component |

## External Parameters

| Symbol | Value | Appears in | Physical meaning |
|---|---:|---|---|
| `eta` | 0.33 | \(v_f=v/\eta\) | Ratio setting the singlet vev \(v_f\) relative to the SM Higgs vev \(v\). |
| `ts` | -0.23 | \(s_s=t_s/\sqrt{1+t_s^2}\), \(c_s=1/\sqrt{1+t_s^2}\), scalar potential parameters | Tangent of the scalar mixing angle, \(t_s=\tan\theta_S\). |
| `sl` | 0.12 | \(c_l=\sqrt{1-s_l^2}\), \(s_r=M_t s_l/(M_{T'}c_l)\), \(y'=\sqrt2 M_{T'}s_l/v\), \(M_\Delta=M_{T'}c_l\) | Sine of the left-handed top-partner mixing angle, \(s_l=\sin\theta_L\). |

## Physics Summary

The file encodes a singlet-scalar extension of the Higgs sector together with a vector-like color-triplet, electroweak-singlet fermion of charge \(2/3\) that mixes chirally with the SM top quark. The physical scalar `sDM` is a real scalar mixed with the SM Higgs through the singlet vev and portal interaction, while `tp` is a heavy top partner coupled to the third-generation quark doublet through a \(\widetilde\Phi\) Yukawa interaction. The model mediates Higgs-portal scalar interactions, scalar production and decay through mixing, and top-partner processes such as \(t'\) production and decays involving \(t\), \(h\), electroweak bosons, and the singlet-like scalar.

## Paper cross-check

**Located Paper Definitions**

The paper’s model definition is in Section II, “The Minimal Dilaton Model.” It defines the field content as one gauge-singlet scalar \(S\) and one fermion \(T\) with the same quantum numbers as the right-handed top quark. The effective Lagrangian is Eq. (2), the scalar potential is Eq. (3), scalar mixing is Eq. (4), the scalar-potential reparameterization is Eq. (5), \(\eta\) is Eq. (8), and the left-handed top/top-partner mixing is Eq. (9). Eq. (1) is background for traditional dilaton couplings and is explicitly not the distinctive MDM setup used later.

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field content: gauge-singlet scalar \(S\), fermion \(T\) with right-handed-top quantum numbers, Section II before Eq. (2) | \(S\) singlet scalar; \(T\) color triplet, \(SU(2)_L\) singlet, \(Y=Q=2/3\) | agree | “Same quantum number as right-handed top quark” implies the listed \(T\) gauge representation. |
| \(L_{\rm SM}\) without Higgs potential, Eq. (2) | Not reconstructed as full SM; only Higgs kinetic/covariant derivative and third-generation/top-partner pieces are shown | missing-in-reconstruction | The paper includes all SM kinetic, gauge, and Yukawa terms except the Higgs potential. The reconstruction is only the BSM/model-relevant subset. |
| Singlet kinetic term \(-\frac12\partial_\mu S\partial^\mu S\), Eq. (2) | \(-\frac12\partial_\mu S\partial^\mu S\) | agree | Same normalization and sign, modulo metric convention. |
| Top-partner kinetic term, schematically \(-\bar T \slashed D T\), Eq. (2) | \(i\bar T\gamma^\mu D_\mu T\), expanded through \(T_L,T_R\) | agree | Same physics up to common extraction/sign conventions for the Dirac kinetic term. The reconstruction’s cross-chiral expansion is redundant; the compact \(i\bar T\gamma^\mu D_\mu T\) is the meaningful form. |
| Dilaton/top-partner mass interaction \(-\bar T(M/f)S T\), Eq. (2) | \(-M_\Delta/v_f\, S\bar T T\), with \(M_\Delta=M_{T'}c_l\) | agree | Same structure if \(v_f=f\) and the implementation identifies the paper’s \(M\) with \(M_\Delta\). That mass-parameter mapping is not stated explicitly in the paper excerpt. |
| Yukawa interaction \(-[y'\,\bar T_R(q_{3L}\cdot H)+{\rm h.c.}]\), Eq. (2) | \(-y'\bar Q_{L,3}^{\,i}\widetilde\Phi_i T_R+{\rm h.c.}\) | agree | Equivalent physics when written in the hermitian-conjugate orientation with the usual \(\epsilon_{ij}\) contraction/\(\widetilde\Phi\) convention. |
| \(q_{3L}\) is the third-generation \(SU(2)_L\) left-handed quark doublet, text after Eq. (2) | \(Q_{L,3}=(t_L,b_L)^T\) | agree | Same field content. |
| Scalar potential \(+\frac{m_S^2}{2}S^2+\frac{\lambda_S}{4!}S^4+\frac{\kappa}{2}S^2|H|^2+m_H^2|H|^2+\frac{\lambda_H}{4}|H|^4\) inside \(\widetilde V\), Eq. (3), entering the Lagrangian as \(-\widetilde V\) | \(-\frac{\mu_S^2}{2}S^2-\frac{\lambda_S}{24}S^4-\frac{\kappa}{2}S^2\Phi^\dagger\Phi-\mu_H^2\Phi^\dagger\Phi-\frac{\lambda_H}{4}(\Phi^\dagger\Phi)^2\) | agree | Coefficients match once the reconstruction’s \(\mu_{S,H}^2\) are identified with the paper’s \(m_{S,H}^2\), and \(|H|^2=\Phi^\dagger\Phi\). |
| Higgs doublet neutral component \(H^0=\frac1{\sqrt2}(v+h\cos\theta_S-s\sin\theta_S)\), Eq. (4) | \(\Phi^0=\frac1{\sqrt2}(v+c_s h-s_s s_{\rm DM}+iG^0)\) | agree | Same neutral scalar mixing if \(c_s=\cos\theta_S\), \(s_s=\sin\theta_S\), and \(s_{\rm DM}=s\). Goldstone terms are gauge-completion details absent from the paper equation. |
| Singlet mixing \(S=f+h\sin\theta_S+s\cos\theta_S\), Eq. (4) | \(S=v_f+s_s h+c_s s_{\rm DM}\) | agree | Same mixing if \(v_f=f\), \(s_s=\sin\theta_S\), \(c_s=\cos\theta_S\). |
| Scalar-potential parameter relations for \(\kappa,\lambda_H,\lambda_S\), Eq. (5) | Reconstruction lists internal \(\kappa,\lambda_H,\lambda_S,\mu_S^2,\mu_H^2\), but does not reproduce the Eq. (5) formulas | missing-in-reconstruction | The Lagrangian terms are present, but the paper’s coefficient relations in terms of \(f,v,\theta_S,m_h,m_s\), including absolute values and \({\rm Sign}(\sin2\theta_S)\), are not fully reconstructed. |
| \(\eta\equiv v/(fN_T)\), with \(N_T=1\) for MDM, Eq. (8) | \(v_f=v/\eta\) | agree | Equivalent for \(N_T=1\). |
| Left-handed mixing \(q^u_{3L}=\cos\theta_L\,t_L+\sin\theta_L\,t'_L\), Eq. (9) | Not given; reconstruction only defines \(Q_{L,3}=(t_L,b_L)^T\) | missing-in-reconstruction | The paper explicitly gives the gauge-basis upper component of \(q_{3L}\) in terms of mass eigenstates. |
| Left-handed top-partner mixing \(T_L=-\sin\theta_L\,t_L+\cos\theta_L\,t'_L\), Eq. (9) | \(T_L=P_L(-s_l t+c_l t')\) | agree | Same relation if \(s_l=\sin\theta_L\), \(c_l=\cos\theta_L\). |
| Right-handed top-partner mixing | \(T_R=P_R(-s_r t+c_r t')\) | extra-in-reconstruction | Section II of the paper does not explicitly define a right-handed mixing angle. This may be an implementation detail inferred from mass diagonalization or from Ref. [15], but it is not in the displayed paper definition. |
| Full Higgs doublet with charged/neutral Goldstones | \(\Phi=(-iG^+,\,(v+c_sh-s_s s_{\rm DM}+iG^0)/\sqrt2)^T\) | extra-in-reconstruction | The paper only displays \(H^0\) in Eq. (4). The Goldstone and phase conventions are standard gauge-basis completion, not a contradiction. |
| Covariant derivative of \(\Phi\) with \(Y=1/2\) | Explicit \(D_\mu\Phi=(\partial_\mu-igW^a_\mu\sigma^a/2-ig'B_\mu/2)\Phi\) | agree | Consistent with the SM Higgs doublet contained in \(L_{\rm SM}\). |
| Covariant derivative of \(T\) with color triplet, \(SU(2)\) singlet, \(Y=2/3\) | Explicit \(D_\mu T=(\partial_\mu-ig_sG^AT^A-ig'(2/3)B_\mu)T\) | agree | Consistent with “same quantum number as the right-handed top quark.” |

**Disagreements And Checks**

- **Missing full \(L_{\rm SM}\) content**: severity **substantive**. A human should check whether the implementation intentionally imports the SM Lagrangian elsewhere, since the reconstruction itself only shows the BSM/Higgs-sector subset.

- **Missing Eq. (5) scalar-parameter relations**: severity **substantive**. A human should check the implementation definitions of \(\mu_S^2,\mu_H^2,\lambda_H,\lambda_S,\kappa\) against the paper’s formulas, especially the sign and absolute-value conventions.

- **Missing \(q^u_{3L}\) left-handed mixing relation from Eq. (9)**: severity **substantive**. A human should check whether the implementation rotates the SM top component consistently with \(q^u_{3L}=c_Lt_L+s_Lt'_L\), not only the heavy \(T_L\) component.

- **Extra right-handed mixing \(T_R=P_R(-s_rt+c_rt')\)**: severity **convention**. A human should check whether this is an implementation-level diagonalization convention compatible with the paper’s approximations \(m_{t'}\gg m_t\) and \(\tan\theta_L\ll m_{t'}/m_t\).

- **Extra Goldstone/full-doublet conventions**: severity **cosmetic**. A human should check only that the \(-iG^+\) and \(+iG^0\) phase conventions are used consistently in the implementation’s gauge fixing and Feynman rules.

- **Top-partner mass mapping \(M\leftrightarrow M_\Delta=M_{T'}c_l\)**: severity **convention**. A human should verify the implementation’s input-parameter definitions, because the paper names \(M\) as the strong-dynamics scale but does not explicitly state the reconstructed \(M_{T'}c_l\) relation in Eq. (2).

**Overall Assessment**

The reconstruction captures the central MDM Lagrangian structure from Section II: a real singlet scalar mixed with the neutral Higgs, the scalar potential with the same operator content and normalizations, a vector-like \(SU(3)_c\) triplet \(SU(2)_L\) singlet top partner of charge \(2/3\), its dilaton-proportional mass interaction, and the \(y'\) Yukawa mixing with the third-generation quark doublet. The main gaps are not obvious wrong operators but incomplete reconstruction of paper-level definitions: the full \(L_{\rm SM}\) context, the Eq. (5) coefficient relations, and the full left-handed top mixing relation for \(q^u_{3L}\). The extra right-handed rotation and Goldstone-expanded Higgs doublet look like implementation conventions rather than direct conflicts, but they should be checked against the implementation’s mass diagonalization and gauge conventions.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 18 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

