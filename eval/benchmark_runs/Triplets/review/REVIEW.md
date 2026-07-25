# Reverse-check review package — `Triplets_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `Triplets/model/Triplets_gen.fr` |
| original model name | `Triplets_gen` (hidden from the agent) |
| paper | Triplets/text/0909.2666.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LTripKin` (`:=`)

```mathematica
DC[trip1bar[k], mu] DC[trip1[k], mu] - Mtrip1^2 trip1bar[k] trip1[k]
```

### `LD11` (`:=`)

```mathematica
2 (Eps[k, i, j] trip1bar[k] LQQR[n, m] ProjP[s, r] dqbar[s, n, i].CC[uq][r, m, j] + Eps[k, i, j] trip1bar[k] LUDL[n, m] ProjM[s, r] dqbar[s, n, i].CC[uq][r, m, j])
```

### `LD1` (`:=`)

```mathematica
LD11 + HC[LD11]
```

### `LPot` (`:=`)

```mathematica
ExpandIndices[LHS1 Phibar[ii] Phi[ii] trip1bar[k] trip1[k] + LSS11 trip1bar[k1] trip1[k1] trip1bar[k2] trip1[k2], FlavorExpand -> {SU2W, SU2D}]
```

### `LTrip` (`:=`)

```mathematica
LTripKin + LD1 + LPot
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Let the new scalar field be
\[
S_k \equiv \texttt{trip1}_k ,
\]
with color index \(k=1,2,3\). Its conjugate is \(S_k^\dagger \equiv \texttt{trip1bar}_k\). The Standard Model Higgs doublet is \(\Phi_i\).

The scalar is an \(SU(3)_c\) triplet, \(SU(2)_L\) singlet, with
\[
Y_S = Q_S = -\frac13 .
\]

The covariant derivative acting on \(S\) is
\[
D_\mu S_k
=
\partial_\mu S_k
+ i g_s G_\mu^a (T^a)_k{}^\ell S_\ell
+ i g' Y_S B_\mu S_k ,
\]
with no \(SU(2)_L\) term because \(S\) is an electroweak singlet.

### `LTripKin`

\[
\mathcal L_{\texttt{LTripKin}}
=
(D_\mu S)^\dagger_k (D^\mu S)_k
-
M_{\texttt{trip1}}^2 S_k^\dagger S_k .
\]

### `LD11`

The file defines
\[
\lambda^{QQ}_{nm} \equiv \texttt{LQQR}[n,m],
\qquad
\lambda^{UD}_{nm} \equiv \texttt{LUDL}[n,m].
\]

Using \(P_R = (1+\gamma^5)/2\), \(P_L=(1-\gamma^5)/2\), and \(u^c = C\bar u^T\), the interaction term is

\[
\mathcal L_{\texttt{LD11}}
=
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{QQ}_{nm}\,
\bar d_{n i}\,P_R\,u^c_{m j}.
\]

Because \(P_R u^c = (u_L)^c\), this is equivalently a left-chiral \(QQ\)-type diquark coupling:
\[
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{QQ}_{nm}\,
\overline{d_{L,n i}}\,(u_{L,m j})^c .
\]

The second term is

\[
\mathcal L_{\texttt{LD11}}
\supset
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{UD}_{nm}\,
\bar d_{n i}\,P_L\,u^c_{m j}.
\]

Because \(P_L u^c = (u_R)^c\), this is equivalently a right-chiral \(u_R d_R\)-type diquark coupling:
\[
2\,\epsilon_{kij}\,
S_k^\dagger\,
\lambda^{UD}_{nm}\,
\overline{d_{R,n i}}\,(u_{R,m j})^c .
\]

Here \(i,j,k\) are color indices contracted with the antisymmetric \(SU(3)_c\) tensor \(\epsilon_{kij}\), and \(n,m\) are generation indices.

### `LD1`

\[
\mathcal L_{\texttt{LD1}}
=
\mathcal L_{\texttt{LD11}}
+
\mathcal L_{\texttt{LD11}}^\dagger .
\]

Explicitly, the hermitian conjugate contains the corresponding \(S_k\) couplings to conjugated quark bilinears.

### `LPot`

\[
\mathcal L_{\texttt{LPot}}
=
\lambda_{HS}\,
(\Phi^\dagger_i \Phi_i)\,
(S_k^\dagger S_k),
\qquad
\lambda_{HS} \equiv \texttt{LHS1}.
\]

\[
\mathcal L_{\texttt{LPot}}
\supset
\lambda_{SS}\,
(S_{k_1}^\dagger S_{k_1})
(S_{k_2}^\dagger S_{k_2}),
\qquad
\lambda_{SS} \equiv \texttt{LSS11}.
\]

### `LTrip`

\[
\mathcal L_{\texttt{LTrip}}
=
\mathcal L_{\texttt{LTripKin}}
+
\mathcal L_{\texttt{LD1}}
+
\mathcal L_{\texttt{LPot}} .
\]

## Field Table

| `.fr` symbol | Particle | Spin | \(SU(3)_c\) | \(SU(2)_L\) | \(Y\) | \(Q\) | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `trip1` | complex scalar \(S\) | 0 | triplet | singlet | \(-1/3\) | \(-1/3\) | no | `Mtrip1 = 500.` |

The antiparticle is `trip1~`, represented in the Lagrangian as `trip1bar`.

## Parameters

| Symbol | Type | Value | Multiplies | Physical meaning |
|---|---:|---:|---|---|
| `LQQRR[n,m]` | external real matrix | nonzero entries: \(LQQRR_{12}=0.1\), \(LQQRR_{21}=-0.1\), \(LQQRR_{13}=0.1\), \(LQQRR_{31}=-0.1\), \(LQQRR_{23}=0.1\), \(LQQRR_{32}=-0.1\), diagonal \(0\) | real part of `LQQR[n,m]` in \(S^\dagger \bar d P_R u^c\) | real part of left-chiral \(QQ\)-type diquark coupling |
| `LQQRI[n,m]` | external real matrix | all entries \(0\) | imaginary part of `LQQR[n,m]` | imaginary part / CP phase of left-chiral diquark coupling |
| `LUDLR[n,m]` | external real matrix | \(LUDLR_{11}=LUDLR_{22}=LUDLR_{33}=0.1\), off-diagonal \(0\) | real part of `LUDL[n,m]` in \(S^\dagger \bar d P_L u^c\) | real part of right-chiral \(u_R d_R\)-type diquark coupling |
| `LUDLI[n,m]` | external real matrix | all entries \(0\) | imaginary part of `LUDL[n,m]` | imaginary part / CP phase of right-chiral diquark coupling |
| `LHS1` | external real scalar | \(1.0\) | \((\Phi^\dagger\Phi)(S^\dagger S)\) | Higgs-portal quartic coupling |
| `LSS11` | external real scalar | \(1.0\) | \((S^\dagger S)^2\) | scalar self-quartic coupling |

The internal complex couplings are
\[
\texttt{LQQR}_{nm}
=
\texttt{LQQRR}_{nm}
+
i\,\texttt{LQQRI}_{nm},
\]
\[
\texttt{LUDL}_{nm}
=
\texttt{LUDLR}_{nm}
+
i\,\texttt{LUDLI}_{nm}.
\]

## Physics Summary

This is a Standard Model extension by one complex color-triplet, electroweak-singlet scalar with electric charge \(-1/3\). It couples as a diquark to up- and down-type quarks through both left-chiral \(QQ\)-type and right-chiral \(u_R d_R\)-type bilinears, and it also has Higgs-portal and scalar self-interactions.

The model mediates baryon-number-sensitive quark-quark interactions such as resonant or virtual scalar exchange in \(u d\)-type partonic channels, including dijet production and flavor-changing quark processes depending on the generation structure of `LQQR` and `LUDL`.

## Paper cross-check

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

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 9 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

