# Reverse-check review package — `pSPSS_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `pSPSS/repair3/final.fr` |
| original model name | `pSPSS_gen` (hidden from the agent) |
| paper | pSPSS/text/2210.10738.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `NuMixE` (`=`)

```mathematica
UnCL[1, 1] ve + UnCL[1, 2] vm + UnCL[1, 3] vt + UnCL[1, 4] n4 + UnCL[1, 5] n5
```

### `NuMixM` (`=`)

```mathematica
UnCL[2, 1] ve + UnCL[2, 2] vm + UnCL[2, 3] vt + UnCL[2, 4] n4 + UnCL[2, 5] n5
```

### `NuMixT` (`=`)

```mathematica
UnCL[3, 1] ve + UnCL[3, 2] vm + UnCL[3, 3] vt + UnCL[3, 4] n4 + UnCL[3, 5] n5
```

### `YukawaNP` (`=`)

```mathematica
yvn[1] (((-n4bar.ProjM.NuMixE + I n5bar.ProjM.NuMixE)/Sqrt[2]) PhiNP[2] -
    ((-n4bar.ProjM.e + I n5bar.ProjM.e)/Sqrt[2]) PhiNP[1]) +
  yvn[2] (((-n4bar.ProjM.NuMixM + I n5bar.ProjM.NuMixM)/Sqrt[2]) PhiNP[2] -
    ((-n4bar.ProjM.mu + I n5bar.ProjM.mu)/Sqrt[2]) PhiNP[1]) +
  yvn[3] (((-n4bar.ProjM.NuMixT + I n5bar.ProjM.NuMixT)/Sqrt[2]) PhiNP[2] -
    ((-n4bar.ProjM.ta + I n5bar.ProjM.ta)/Sqrt[2]) PhiNP[1])
```

### `LNP` (`=`)

```mathematica
RemoveHigherOrder[Block[{sp1}, - Mmaj CC[N1Lbar[sp1]].N2L[sp1] + YukawaNP + HC[- Mmaj CC[N1Lbar[sp1]].N2L[sp1] + YukawaNP]]]
```

### `LTot` (`:=`)

```mathematica
LKineticSterile + LNP
```

## Blank-slate reconstruction

# Reconstructed Physics from `sanitized.fr`

## Lagrangian

The file defines two sterile left-handed Weyl fields, `N1L` and `N2L`, both electroweak and color singlets:
\[
SU(3)_c:\mathbf{1},\qquad SU(2)_L:\mathbf{1},\qquad Y=0,\qquad Q=0 .
\]
Therefore their covariant derivative contains no gauge connection:
\[
D_\mu N_{1L,2L}=\partial_\mu N_{1L,2L}.
\]

The physical Majorana fields are `n4` and `n5`, with
\[
N_{1L}=\frac{i\,n_4+n_5}{\sqrt{2}},
\]
and
\[
N_{2L}
=
-\theta_e\,\nu_e-\theta_\mu\,\nu_\mu-\theta_\tau\,\nu_\tau
-\frac{i}{\sqrt{2}}\left(1-\frac{\theta^2}{2}\right)n_4
+\frac{1}{\sqrt{2}}\left(1-\frac{\theta^2}{2}\right)n_5,
\]
where
\[
\theta^2=\theta_e^2+\theta_\mu^2+\theta_\tau^2.
\]

The active neutrino combinations used in the Yukawa terms are, to second order in the mixings,
\[
\nu'_e
=
\left(1-\frac{\theta_e^2}{2}\right)\nu_e
-\frac{\theta_e\theta_\mu}{2}\nu_\mu
-\frac{\theta_e\theta_\tau}{2}\nu_\tau
-\frac{i\theta_e}{\sqrt{2}}n_4
+\frac{\theta_e}{\sqrt{2}}n_5 ,
\]
\[
\nu'_\mu
=
-\frac{\theta_\mu\theta_e}{2}\nu_e
+\left(1-\frac{\theta_\mu^2}{2}\right)\nu_\mu
-\frac{\theta_\mu\theta_\tau}{2}\nu_\tau
-\frac{i\theta_\mu}{\sqrt{2}}n_4
+\frac{\theta_\mu}{\sqrt{2}}n_5 ,
\]
\[
\nu'_\tau
=
-\frac{\theta_\tau\theta_e}{2}\nu_e
-\frac{\theta_\tau\theta_\mu}{2}\nu_\mu
+\left(1-\frac{\theta_\tau^2}{2}\right)\nu_\tau
-\frac{i\theta_\tau}{\sqrt{2}}n_4
+\frac{\theta_\tau}{\sqrt{2}}n_5 .
\]

Here `ProjM` is the left-handed projector,
\[
P_L=\frac{1-\gamma^5}{2},
\]
`HC[...]` denotes the Hermitian conjugate, and `CC[...]` denotes charge conjugation.

### `LKineticSterile`

\[
\mathcal{L}_{\texttt{LKineticSterile}}
=
i\,\overline{N_{1L}}\gamma^\mu \partial_\mu N_{1L}
+
i\,\overline{N_{2L}}\gamma^\mu \partial_\mu N_{2L}.
\]

### `YukawaNP`

Define
\[
y_e=\frac{M_{\rm maj}\theta_e}{v},\qquad
y_\mu=\frac{M_{\rm maj}\theta_\mu}{v},\qquad
y_\tau=\frac{M_{\rm maj}\theta_\tau}{v}.
\]

With the Higgs doublet written as
\[
\Phi =
\begin{pmatrix}
\Phi_1\\
\Phi_2
\end{pmatrix},
\]
the file encodes
\[
\mathcal{L}_{\texttt{YukawaNP}}
=
y_e
\left[
\frac{-\overline{n_4}P_L\nu'_e+i\,\overline{n_5}P_L\nu'_e}{\sqrt{2}}\,\Phi_2
-
\frac{-\overline{n_4}P_L e+i\,\overline{n_5}P_L e}{\sqrt{2}}\,\Phi_1
\right]
\]
\[
+
y_\mu
\left[
\frac{-\overline{n_4}P_L\nu'_\mu+i\,\overline{n_5}P_L\nu'_\mu}{\sqrt{2}}\,\Phi_2
-
\frac{-\overline{n_4}P_L \mu+i\,\overline{n_5}P_L \mu}{\sqrt{2}}\,\Phi_1
\right]
\]
\[
+
y_\tau
\left[
\frac{-\overline{n_4}P_L\nu'_\tau+i\,\overline{n_5}P_L\nu'_\tau}{\sqrt{2}}\,\Phi_2
-
\frac{-\overline{n_4}P_L \tau+i\,\overline{n_5}P_L \tau}{\sqrt{2}}\,\Phi_1
\right].
\]

Equivalently, using \(L_\alpha=(\nu'_\alpha,\ell_\alpha)^T\),
\[
\mathcal{L}_{\texttt{YukawaNP}}
=
\sum_{\alpha=e,\mu,\tau}
y_\alpha\,
\frac{-\overline{n_4}+i\overline{n_5}}{\sqrt{2}}\,
P_L
\left(
\nu'_\alpha \Phi_2-\ell_\alpha \Phi_1
\right),
\]
with the \(SU(2)_L\) contraction corresponding to the usual antisymmetric contraction with the Higgs doublet.

### `LNP`

The new-physics Lagrangian is
\[
\mathcal{L}_{\texttt{LNP}}
=
-
M_{\rm maj}\,
\overline{N_{1L}^{\,c}}\,
N_{2L}
+
\mathcal{L}_{\texttt{YukawaNP}}
+
\text{h.c.}
\]

That is,
\[
\mathcal{L}_{\texttt{LNP}}
=
-
M_{\rm maj}\,
\overline{N_{1L}^{\,c}}\,
N_{2L}
-
M_{\rm maj}\,
\overline{N_{2L}}\,
N_{1L}^{\,c}
+
\mathcal{L}_{\texttt{YukawaNP}}
+
\mathcal{L}_{\texttt{YukawaNP}}^\dagger .
\]

All terms are truncated by `RemoveHigherOrder` to second order in
\[
\theta_e,\theta_\mu,\theta_\tau .
\]

### `LTot`

\[
\mathcal{L}_{\texttt{LTot}}
=
\mathcal{L}_{\texttt{LKineticSterile}}
+
\mathcal{L}_{\texttt{LNP}}.
\]

## Field Table

| `.fr` class | Symbol / members | Spin | \(SU(3)_c\) | \(SU(2)_L\) | \(U(1)_Y\) / \(Q\) | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---|
| `F[100]` | `nH = {n4,n5}` | \(1/2\) | not declared; singlet by construction | not declared; singlet by construction | neutral | yes | `MN = {Mn4,Mn5}` |
| `W[100]` | `N1L` | left-handed Weyl \(1/2\) | singlet | singlet | \(Y=0,\ Q=0\) | no | unphysical |
| `W[101]` | `N2L` | left-handed Weyl \(1/2\) | singlet | singlet | \(Y=0,\ Q=0\) | no | unphysical |

The physical Majorana masses are internal parameters:
\[
M_{n4}=M_{\rm maj}\left(1+\frac{\theta^2}{2}\right)-\frac{\Delta m}{2},
\]
\[
M_{n5}=M_{\rm maj}\left(1+\frac{\theta^2}{2}\right)+\frac{\Delta m}{2}.
\]

With the default numerical inputs,
\[
M_{\rm maj}=100,\qquad
\Delta m=10^{-12},\qquad
\theta_e=0,\quad \theta_\mu=10^{-3},\quad \theta_\tau=0,
\]
so
\[
\theta^2=10^{-6},
\]
\[
M_{n4}=100.00005-5\times 10^{-13},
\]
\[
M_{n5}=100.00005+5\times 10^{-13}.
\]

## Parameters

| Parameter | Type | Default value | Appears in | Physical meaning |
|---|---:|---:|---|---|
| `Mmaj` | external real | \(100\) | `LNP`, `yvn`, `Mn4`, `Mn5` | Common sterile mass scale; multiplies \(-\overline{N_{1L}^c}N_{2L}\) and sets the active-sterile Yukawa strengths \(y_\alpha=M_{\rm maj}\theta_\alpha/v\). |
| `deltaM` | external real | \(10^{-12}\) | `Mn4`, `Mn5` | Small mass splitting between the two heavy Majorana states. |
| `theta1` | external real | \(0\) | `yvn[1]`, `UnCL`, `Un`, `Mn4`, `Mn5` through \(\theta^2\) | Electron-flavor active-sterile mixing angle \(\theta_e\). |
| `theta2` | external real | \(10^{-3}\) | `yvn[2]`, `UnCL`, `Un`, `Mn4`, `Mn5` through \(\theta^2\) | Muon-flavor active-sterile mixing angle \(\theta_\mu\). |
| `theta3` | external real | \(0\) | `yvn[3]`, `UnCL`, `Un`, `Mn4`, `Mn5` through \(\theta^2\) | Tau-flavor active-sterile mixing angle \(\theta_\tau\). |
| `damping` | external real | \(0\) | not used in the displayed Lagrangian | Declared external parameter with no role in `LKineticSterile`, `YukawaNP`, `LNP`, or `LTot`. |

The internal Yukawa parameters are
\[
\texttt{yvn[1]}=y_e=\frac{M_{\rm maj}\theta_e}{v},
\]
\[
\texttt{yvn[2]}=y_\mu=\frac{M_{\rm maj}\theta_\mu}{v},
\]
\[
\texttt{yvn[3]}=y_\tau=\frac{M_{\rm maj}\theta_\tau}{v}.
\]

## Physics Summary

The file encodes an extension of the Standard Model by two nearly degenerate neutral Majorana fermions, `n4` and `n5`, built from two sterile left-handed singlets and mixed with the three active neutrino flavors through small real parameters \(\theta_e,\theta_\mu,\theta_\tau\). The new interactions are sterile-neutrino Yukawa couplings to the SM lepton doublets and Higgs doublet, plus a sterile mass term producing a pseudo-Dirac pair split by \(\Delta m\).

Through the active-sterile mixing substitutions, the heavy neutral leptons inherit charged-current, neutral-current, and Higgs interactions with SM leptons and gauge bosons. The model therefore mediates processes such as heavy-neutral-lepton production in weak decays or electroweak interactions, followed by decays into charged leptons, neutrinos, \(W/Z\), or Higgs states depending on kinematics.

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Located Paper Definitions

The relevant model definitions are in:

- General sterile-neutrino Lagrangian: Eq. (2.1), with post-EWSB form Eq. (2.2).
- Symmetry-protected seesaw scenario: Section 4.1, especially LNLS charges Eq. (4.1), SPSS Lagrangian Eq. (4.2), mass Lagrangian Eq. (4.3), mass matrix Eq. (4.4), mixing definition Eq. (4.5), mixing parameter Eq. (4.6), masses Eq. (4.7), and mixing matrix Eq. (4.8).
- Small symmetry breaking: Section 4.2, especially Eq. (4.11) through Eq. (4.16).
- Phenomenological SPSS: Section 4.3, especially pSPSS mass prescription Eq. (4.17) and parameter list Table 2.
- FeynRules implementation: Section 5.1, especially the sterile kinetic terms, mass term, Yukawa term, neutrino replacement Eq. (5.2), and `RemoveHigherOrder` truncation.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---:|---|
| Sterile neutrinos are SM singlets; general sterile extension uses sterile neutrinos \(N_i\) added to the SM, Eq. (2.1), Section 5.1 | `N1L`, `N2L` are color and electroweak singlet left-handed Weyl fields with \(Y=Q=0\) | **agree** | Correct gauge content. The paper explicitly treats the sterile fields as SM singlets and left-chiral DOFs. |
| LNLS charge assignment: \(\ell:+1\), \(N_1:-1\), \(N_2:+1\), all other fields zero, Eq. (4.1) | No LNLS charge assignment listed | **missing-in-reconstruction** | The reconstruction captures the gauge charges but omits the lepton-number-like symmetry charges that protect the Dirac limit. |
| SPSS kinetic term \(N_i^c i\!\not\!\partial N_i\), Eq. (4.2); implementation: `I (N1Lbar.Ga[mu].del[N1L, mu] + N2Lbar.Ga[mu].del[N2L, mu])`, Section 5.1 | \(i\overline{N_{1L}}\gamma^\mu\partial_\mu N_{1L}+i\overline{N_{2L}}\gamma^\mu\partial_\mu N_{2L}\) | **agree** | Same sterile kinetic content. The reconstruction’s ordinary derivative is consistent with the singlet gauge representation. |
| Symmetric-limit Yukawa term \(-y_{1\alpha}N_1^c\widetilde H^\dagger\ell_\alpha+\mathrm{H.c.}\), Eq. (4.2); implementation: `yvn[ff1] (CC[N1Lbar].LL[... ] PhiNPbar[...] Eps[...])`, Section 5.1 | \(\sum_\alpha y_\alpha \frac{-\overline n_4+i\overline n_5}{\sqrt2}P_L(\nu'_\alpha\Phi_2-\ell_\alpha\Phi_1)+\mathrm{H.c.}\) | **agree** | Correctly couples only the \(N_1\)-type sterile combination to the SM lepton doublet and Higgs doublet. The antisymmetric \(SU(2)_L\) contraction is represented in component form. Overall sign conventions are not physically material here. |
| Yukawa-mixing relation \(\theta=m_D/m_M\), \(m_D=y_1v\), Eq. (4.6) | \(y_\alpha=M_{\rm maj}\theta_\alpha/v\) | **agree** | Correct inversion of Eq. (4.6), assuming the same Higgs-VEV convention as the implementation. |
| Sterile mass term \(-N_1^c m_M N_2+\mathrm{H.c.}\), Eq. (4.2); implementation: `- Mmaj CC[N1Lbar[sp1]].N2L[sp1]`, Section 5.1 | \(-M_{\rm maj}\overline{N_{1L}^{\,c}}N_{2L}+\mathrm{H.c.}\) | **agree** | Correct off-diagonal sterile mass term producing the pseudo-Dirac pair in the symmetry limit. |
| Interaction-basis mass Lagrangian \(-\frac12 n^cM_nn+\mathrm{H.c.}\), Eq. (4.3), with matrix Eq. (4.4) | Encoded indirectly through \(N_{1L},N_{2L}\), their mass term, and physical \(n_4,n_5\) masses | **agree** | The reconstruction does not reproduce the full matrix, but its terms imply the same \(N_1\)-\(N_2\) off-diagonal heavy block and active-sterile Dirac entries through the Yukawas. |
| Mixing matrix \(U_n\) through second order in \(\theta\), Eq. (4.8) | Explicit expressions for \(N_{1L}\), \(N_{2L}\), and \(\nu'_{e,\mu,\tau}\) through second order | **agree** | Matches Eq. (4.8) for real \(\theta_\alpha\). The paper writes complex conjugates \(\theta^\ast\), while the reconstruction treats the implemented parameters as real. |
| Exact charged-lepton block \(U_{CL}= (1+|\theta|^2)^{-1/2}(-i\theta^\ast/\sqrt2,\theta^\ast/\sqrt2)\), Eq. (4.9), and possible rescaling Eq. (4.10) | Uses second-order expansion with \(1-\theta^2/2\) factors | **agree** | Consistent with the paper’s stated second-order expansion and the FeynRules implementation’s truncation. |
| Symmetric-limit heavy masses \(m_4=m_5=m_M(1+\frac12|\theta|^2)+O(|\theta|^4)\), Eq. (4.7) | \(M_{n4}=M_{\rm maj}(1+\theta^2/2)-\Delta m/2\), \(M_{n5}=M_{\rm maj}(1+\theta^2/2)+\Delta m/2\) | **agree** | Reduces to Eq. (4.7) when \(\Delta m=0\). |
| pSPSS mass splitting \(m_{4/5}=m_M(1+\frac12|\theta|^2)\mp\frac12\Delta m\), Eq. (4.17) | Same mass prescription with `deltaM` | **agree** | Correct pSPSS implementation of the phenomenological mass splitting. |
| Generic small-LNV terms \(-y_{2\alpha}N_2^c\widetilde H^\dagger\ell_\alpha-\mu'_MN_1^cN_1-\mu_MN_2^cN_2+\cdots+\mathrm{H.c.}\), Eq. (4.11) | No explicit \(y_2\), \(\mu_M\), or \(\mu'_M\) Lagrangian terms; only \(\Delta m\) in masses | **agree** | This agrees with the pSPSS definition in Section 4.3: instead of implementing Eq. (4.11), the model directly parameterizes the heavy-neutrino mass splitting by \(\Delta m\). |
| Active neutrino replacement \(n_\alpha=(U'_{CL})_{\alpha i}n_i\), Eq. (5.2), used inside the SM lepton doublet, Section 5.1 | Defines \(\nu'_e,\nu'_\mu,\nu'_\tau\) as active-neutrino combinations including heavy admixtures | **agree** | Correct physics content for the implemented mixing replacement. |
| Complete pSPSS implementation: SM Lagrangian with neutrino fields replaced by `UnCL nL`, plus NP terms; complete Lagrangian named `LpSPSS`, Section 5.1 | `LTot = LKineticSterile + LNP` | **missing-in-reconstruction** | The reconstruction’s displayed `LTot` omits the SM Lagrangian pieces whose neutrino fields are replaced by the mixed fields. Its later physics summary mentions inherited weak/Higgs interactions, but the displayed total Lagrangian is incomplete relative to `LpSPSS`. |
| Truncation: implemented mixing matrix valid up to second order in \(\theta\); `RemoveHigherOrder` drops smaller terms, Section 5.1 | All terms truncated to second order in \(\theta_e,\theta_\mu,\theta_\tau\) | **agree** | Correct. |
| Free pSPSS parameters \(m_M\), \(\Delta m\), \(\theta_1,\theta_2,\theta_3\), damping \(\lambda\), Table 2 | `Mmaj`, `deltaM`, `theta1`, `theta2`, `theta3`, `damping` with the same defaults | **agree** | Correct parameter list and defaults. |
| Damping parameter \(\lambda\) included for MadGraph oscillation treatment, not as an ordinary FeynRules interaction term, Section 4.3 and Section 5.1 | `damping` declared but not used in displayed Lagrangian | **agree** | Correct. |
| Physical fields extended by self-conjugate neutrinos \(n_4,n_5\), Section 5.1 | `n4`, `n5` listed as self-conjugate Majorana fields | **agree** | Correct. |
| Dirac/pseudo-Dirac relative phase: heavy mass eigenstate couplings have relative phase \(-i\), Appendix A, especially Eq. (A.6) and Eq. (A.7) | \(N_{1L}=(in_4+n_5)/\sqrt2\), active admixtures \(-i\theta_\alpha n_4/\sqrt2+\theta_\alpha n_5/\sqrt2\) | **agree** | Correct relative phase structure for the pseudo-Dirac pair, up to equivalent field/sign conventions. |
| Complex structure: paper generally writes \(\theta^\ast\), \(|\theta|^2\), and complex vectors, Eq. (4.8) through Eq. (4.10) | Reconstruction uses \(\theta^2=\theta_e^2+\theta_\mu^2+\theta_\tau^2\) and real \(\theta_\alpha\) | **disagree** | This is acceptable only if the implementation restricts `theta1`, `theta2`, `theta3` to real external parameters. As a statement of the paper’s analytic model, it drops possible complex phases. |

## Disagreements and Human Checks

- **Missing LNLS charges** — severity: **substantive**. A human should check whether the reconstruction is intended to document only FeynRules gauge content or also the symmetry structure of the pSPSS, because Eq. (4.1) is central to why the allowed terms have the displayed form.

- **Displayed total Lagrangian omits the SM-with-mixed-neutrinos part** — severity: **substantive**. A human should check whether `LTot` in the reconstruction is meant to be only the new-physics addition or the full `LpSPSS`; the paper’s Section 5.1 says the SM fermion Lagrangian is modified by replacing \(\nu\) with `UnCL nL`.

- **Real versus complex active-sterile mixings** — severity: **convention**. A human should check the actual implementation parameter declarations: if `theta1`, `theta2`, and `theta3` are real, the reconstruction is faithful to the implementation, but it is narrower than the complex notation used in the paper’s analytic equations.

## Overall Assessment

The reconstruction captures the core pSPSS implementation well: two sterile singlet left-chiral fields, two self-conjugate heavy neutrino mass eigenstates, the off-diagonal pseudo-Dirac mass term, Yukawas proportional to \(M_{\rm maj}\theta_\alpha/v\), the second-order active-sterile mixing structure, the phenomenological mass splitting \(\Delta m\), and the default parameter block all agree with Sections 4.1, 4.3, and 5.1 of the paper. The main limitations are scope and documentation: it omits the LNLS charge assignment that explains the model’s symmetry protection, and its displayed `LTot` does not include the SM Lagrangian after the neutrino mixing replacement, even though that replacement is necessary for the weak interactions of \(n_4,n_5\). The only physics-content mismatch is the treatment of \(\theta_\alpha\) as real rather than generally complex, which may be a faithful implementation restriction but should be checked against the original model file.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 13 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

