# Reverse-check review package — `Sextets_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `Sextets/model/Sextets_gen.fr` |
| original model name | `Sextets_gen` (hidden from the agent) |
| paper | Sextets/text/0909.2666.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LSextetKin` (`:=`)

```mathematica
DC[six1bar[k], mu] DC[six1[k], mu] - MSIX1^2 six1bar[k] six1[k] + DC[six2bar[k], mu] DC[six2[k], mu] - MSIX2^2 six2bar[k] six2[k] + DC[six3bar[k], mu] DC[six3[k], mu] - MSIX3^2 six3bar[k] six3[k]
```

### `LD11` (`:=`)

```mathematica
2 Sqrt[2] (K6bar[k, i, j] six1[k] LQQR[n, m] ProjP[s, r] dqbar[s, n, i].CC[uq][r, m, j] + K6bar[k, i, j] six1[k] LUDL[n, m] ProjM[s, r] dqbar[s, n, i].CC[uq][r, m, j])
```

### `LD1` (`:=`)

```mathematica
LD11 + HC[LD11]
```

### `LD21` (`:=`)

```mathematica
2 Sqrt[2] K6bar[k, i, j] six2[k] LDDL[n, m] ProjM[s, r] dqbar[s, n, i].CC[dq][r, m, j]
```

### `LD2` (`:=`)

```mathematica
LD21 + HC[LD21]
```

### `LD31` (`:=`)

```mathematica
2 Sqrt[2] K6bar[k, i, j] six3[k] LUUL[n, m] ProjM[s, r] uqbar[s, n, i].CC[uq][r, m, j]
```

### `LD3` (`:=`)

```mathematica
LD31 + HC[LD31]
```

### `LD` (`:=`)

```mathematica
LD1 + LD2 + LD3
```

### `LPot` (`:=`)

```mathematica
ExpandIndices[LHS1 Phibar[ii] Phi[ii] six1bar[k] six1[k] + LHS2 Phibar[ii] Phi[ii] six2bar[k] six2[k] + LHS3 Phibar[ii] Phi[ii] six3bar[k] six3[k] + LSS11 six1bar[k1] six1[k1] six1bar[k2] six1[k2] + LSS121 six1bar[k1] six1[k1] six2bar[k2] six2[k2] + LSS122 six1bar[k1] six1[k2] six2bar[k2] six2[k1] + LSS131 six1bar[k1] six1[k1] six3bar[k2] six3[k2] + LSS132 six1bar[k1] six1[k2] six3bar[k2] six3[k1] + LSS22 six2bar[k1] six2[k1] six2bar[k2] six2[k2] + LSS231 six2bar[k1] six2[k1] six3bar[k2] six3[k2] + LSS232 six2bar[k1] six2[k2] six3bar[k2] six3[k1] + LSS33 six3bar[k1] six3[k1] six3bar[k2] six3[k2], FlavorExpand -> {SU2W, SU2D}]
```

### `LSextet` (`:=`)

```mathematica
LSextetKin + LD1 + LD2 + LD3 + LPot
```

## Blank-slate reconstruction

# Reconstructed Physics Content of `sanitized.fr`

## Conventions

Generation indices are \(n,m=1,2,3\). Fundamental color indices are \(i,j=1,2,3\). Sextet color indices are \(k,k_1,k_2=1,\dots,6\). The tensor
\[
K^{*}_{kij}\equiv \texttt{K6bar[k,i,j]}
\]
is the color Clebsch tensor contracting a color-sextet scalar with two color-triplet quarks; it is symmetric in the two fundamental color indices.

The three new scalar fields are denoted
\[
S_1^k\equiv \texttt{six1[k]},\qquad
S_2^k\equiv \texttt{six2[k]},\qquad
S_3^k\equiv \texttt{six3[k]}.
\]

FeynRules projectors are translated as
\[
\texttt{ProjP}=P_R=\frac{1+\gamma^5}{2},\qquad
\texttt{ProjM}=P_L=\frac{1-\gamma^5}{2}.
\]
The charge-conjugated spinor is
\[
q^c \equiv C\bar q^T.
\]

The scalar fields are \(SU(2)_L\) singlets. Their covariant derivative is therefore
\[
D_\mu S_a
=
\left[
\partial_\mu
+i g_s G_\mu^A (T_6^A)
+i g' Y_a B_\mu
\right]S_a ,
\]
or, after electroweak rotation,
\[
D_\mu S_a
=
\left[
\partial_\mu
+i g_s G_\mu^A (T_6^A)
+i e Q_a A_\mu
-i e Q_a \tan\theta_W Z_\mu
\right]S_a ,
\]
with \(Q_a=Y_a\) for these \(SU(2)_L\)-singlet scalars.

---

## Lagrangian

### `LSextetKin`

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu S_1)^\dagger_k(D^\mu S_1)^k
-
M_{\texttt{SIX1}}^2\,S_{1k}^\dagger S_1^k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu S_2)^\dagger_k(D^\mu S_2)^k
-
M_{\texttt{SIX2}}^2\,S_{2k}^\dagger S_2^k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu S_3)^\dagger_k(D^\mu S_3)^k
-
M_{\texttt{SIX3}}^2\,S_{3k}^\dagger S_3^k .
\]

### `LD11`

\[
\mathcal L_{\texttt{LD11}}
=
2\sqrt 2\,
K^{*}_{kij}\,
S_1^k
\left[
\lambda_{\texttt{QQ}}^{nm}\,
\bar d_{n i} P_R u^c_{m j}
+
\lambda_{\texttt{UD}}^{nm}\,
\bar d_{n i} P_L u^c_{m j}
\right],
\]
where
\[
\lambda_{\texttt{QQ}}^{nm}\equiv \texttt{LQQR[n,m]},
\qquad
\lambda_{\texttt{UD}}^{nm}\equiv \texttt{LUDL[n,m]}.
\]

### `LD1`

\[
\mathcal L_{\texttt{LD1}}
=
\mathcal L_{\texttt{LD11}}
+
\mathcal L_{\texttt{LD11}}^\dagger .
\]

### `LD21`

\[
\mathcal L_{\texttt{LD21}}
=
2\sqrt 2\,
K^{*}_{kij}\,
S_2^k\,
\lambda_{\texttt{DD}}^{nm}\,
\bar d_{n i} P_L d^c_{m j},
\]
where
\[
\lambda_{\texttt{DD}}^{nm}\equiv \texttt{LDDL[n,m]}.
\]

### `LD2`

\[
\mathcal L_{\texttt{LD2}}
=
\mathcal L_{\texttt{LD21}}
+
\mathcal L_{\texttt{LD21}}^\dagger .
\]

### `LD31`

\[
\mathcal L_{\texttt{LD31}}
=
2\sqrt 2\,
K^{*}_{kij}\,
S_3^k\,
\lambda_{\texttt{UU}}^{nm}\,
\bar u_{n i} P_L u^c_{m j},
\]
where
\[
\lambda_{\texttt{UU}}^{nm}\equiv \texttt{LUUL[n,m]}.
\]

### `LD3`

\[
\mathcal L_{\texttt{LD3}}
=
\mathcal L_{\texttt{LD31}}
+
\mathcal L_{\texttt{LD31}}^\dagger .
\]

### `LD`

\[
\mathcal L_{\texttt{LD}}
=
\mathcal L_{\texttt{LD1}}
+
\mathcal L_{\texttt{LD2}}
+
\mathcal L_{\texttt{LD3}} .
\]

### `LPot`

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{HS1}}\,
(\Phi^\dagger_i\Phi_i)\,
S_{1k}^\dagger S_1^k .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{HS2}}\,
(\Phi^\dagger_i\Phi_i)\,
S_{2k}^\dagger S_2^k .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{HS3}}\,
(\Phi^\dagger_i\Phi_i)\,
S_{3k}^\dagger S_3^k .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS11}}\,
(S_{1k_1}^\dagger S_1^{k_1})
(S_{1k_2}^\dagger S_1^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS121}}\,
(S_{1k_1}^\dagger S_1^{k_1})
(S_{2k_2}^\dagger S_2^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS122}}\,
S_{1k_1}^\dagger S_1^{k_2}
S_{2k_2}^\dagger S_2^{k_1} .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS131}}\,
(S_{1k_1}^\dagger S_1^{k_1})
(S_{3k_2}^\dagger S_3^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS132}}\,
S_{1k_1}^\dagger S_1^{k_2}
S_{3k_2}^\dagger S_3^{k_1} .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS22}}\,
(S_{2k_1}^\dagger S_2^{k_1})
(S_{2k_2}^\dagger S_2^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS231}}\,
(S_{2k_1}^\dagger S_2^{k_1})
(S_{3k_2}^\dagger S_3^{k_2}) .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS232}}\,
S_{2k_1}^\dagger S_2^{k_2}
S_{3k_2}^\dagger S_3^{k_1} .
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{\texttt{SS33}}\,
(S_{3k_1}^\dagger S_3^{k_1})
(S_{3k_2}^\dagger S_3^{k_2}) .
\]

### `LSextet`

\[
\mathcal L_{\texttt{LSextet}}
=
\mathcal L_{\texttt{LSextetKin}}
+
\mathcal L_{\texttt{LD1}}
+
\mathcal L_{\texttt{LD2}}
+
\mathcal L_{\texttt{LD3}}
+
\mathcal L_{\texttt{LPot}} .
\]

---

## Field Table

| `.fr` class | Field symbol | Spin | \(SU(3)_C\) rep | \(SU(2)_L\) rep | \(U(1)\) charge / hypercharge | Self-conjugate? | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `six1` | \(S_1\) | 0 | \(\mathbf 6\) | \(\mathbf 1\) | \(Q=Y=1/3\) | No | `MSIX1 = 500` |
| `six2` | \(S_2\) | 0 | \(\mathbf 6\) | \(\mathbf 1\) | \(Q=Y=-2/3\) | No | `MSIX2 = 500` |
| `six3` | \(S_3\) | 0 | \(\mathbf 6\) | \(\mathbf 1\) | \(Q=Y=4/3\) | No | `MSIX3 = 500` |

---

## Parameters

| External parameter | Value in file | Multiplies | Physical meaning |
|---|---:|---|---|
| `LQQRR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LQQR[n,m]` in \(S_1\,\bar d_n P_R u_m^c\) | real part of complex diquark Yukawa coupling |
| `LQQRI[n,m]` | \(0\) | imaginary part of `LQQR[n,m]` in \(S_1\,\bar d_n P_R u_m^c\) | imaginary part / CP phase of diquark coupling |
| `LUDLR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LUDL[n,m]` in \(S_1\,\bar d_n P_L u_m^c\) | real part of complex diquark Yukawa coupling |
| `LUDLI[n,m]` | \(0\) | imaginary part of `LUDL[n,m]` in \(S_1\,\bar d_n P_L u_m^c\) | imaginary part / CP phase of diquark coupling |
| `LUULR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LUUL[n,m]` in \(S_3\,\bar u_n P_L u_m^c\) | real part of complex up-type diquark Yukawa coupling |
| `LUULI[n,m]` | \(0\) | imaginary part of `LUUL[n,m]` in \(S_3\,\bar u_n P_L u_m^c\) | imaginary part / CP phase of up-type diquark coupling |
| `LDDLR[n,m]` | diagonal \(0.1\), off-diagonal \(0\) | real part of `LDDL[n,m]` in \(S_2\,\bar d_n P_L d_m^c\) | real part of complex down-type diquark Yukawa coupling |
| `LDDLI[n,m]` | \(0\) | imaginary part of `LDDL[n,m]` in \(S_2\,\bar d_n P_L d_m^c\) | imaginary part / CP phase of down-type diquark coupling |
| `LHS1` | \(0.1\) | \((\Phi^\dagger\Phi)(S_1^\dagger S_1)\) | Higgs-portal quartic coupling |
| `LHS2` | \(0.1\) | \((\Phi^\dagger\Phi)(S_2^\dagger S_2)\) | Higgs-portal quartic coupling |
| `LHS3` | \(0.1\) | \((\Phi^\dagger\Phi)(S_3^\dagger S_3)\) | Higgs-portal quartic coupling |
| `LSS11` | \(0.1\) | \((S_1^\dagger S_1)^2\) | scalar self-quartic coupling |
| `LSS121` | \(0.1\) | \((S_1^\dagger S_1)(S_2^\dagger S_2)\) | mixed scalar quartic coupling |
| `LSS122` | \(0.1\) | \(S_1^\dagger{}_{k_1}S_1^{k_2}S_2^\dagger{}_{k_2}S_2^{k_1}\) | independent color-contracted mixed scalar quartic |
| `LSS131` | \(0.1\) | \((S_1^\dagger S_1)(S_3^\dagger S_3)\) | mixed scalar quartic coupling |
| `LSS132` | \(0.1\) | \(S_1^\dagger{}_{k_1}S_1^{k_2}S_3^\dagger{}_{k_2}S_3^{k_1}\) | independent color-contracted mixed scalar quartic |
| `LSS22` | \(0.1\) | \((S_2^\dagger S_2)^2\) | scalar self-quartic coupling |
| `LSS231` | \(0.1\) | \((S_2^\dagger S_2)(S_3^\dagger S_3)\) | mixed scalar quartic coupling |
| `LSS232` | \(0.1\) | \(S_2^\dagger{}_{k_1}S_2^{k_2}S_3^\dagger{}_{k_2}S_3^{k_1}\) | independent color-contracted mixed scalar quartic |
| `LSS33` | \(0.1\) | \((S_3^\dagger S_3)^2\) | scalar self-quartic coupling |

The internal complex couplings are
\[
\texttt{LQQR}_{nm}=\texttt{LQQRR}_{nm}+i\,\texttt{LQQRI}_{nm},
\]
\[
\texttt{LUDL}_{nm}=\texttt{LUDLR}_{nm}+i\,\texttt{LUDLI}_{nm},
\]
\[
\texttt{LUUL}_{nm}=\texttt{LUULR}_{nm}+i\,\texttt{LUULI}_{nm},
\]
\[
\texttt{LDDL}_{nm}=\texttt{LDDLR}_{nm}+i\,\texttt{LDDLI}_{nm}.
\]

---

## Physics Summary

The file encodes three complex scalar color-sextet, electroweak-singlet fields with electric charges \(1/3\), \(-2/3\), and \(4/3\). They have QCD and hypercharge gauge interactions, Higgs-portal and scalar self-quartic interactions, and diquark Yukawa-type couplings to pairs of quarks through charge-conjugated spinors with explicitly chiral projectors.

The model mediates quark-quark resonant or virtual processes such as \(u d\), \(d d\), and \(u u\) scattering through scalar color-sextet exchange, with generation structure controlled by the complex matrices `LQQR`, `LUDL`, `LDDL`, and `LUUL`.

## Paper cross-check

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

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 27 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

