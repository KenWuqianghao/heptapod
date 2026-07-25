# Reverse-check review package — `HeavyN_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `HeavyN/model/HeavyN_gen.fr` |
| original model name | `HeavyN_gen` (hidden from the agent) |
| paper | HeavyN/text/1602.06957.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LNKin` (`:=`)

```mathematica
I/2 N1bar[s1].Ga[v,s1,s2].del[N1[s2],v] - 1/2 mN1 N1bar[s1] N1[s1] + I/2 N2bar[s1].Ga[v,s1,s2].del[N2[s2],v] - 1/2 mN2 N2bar[s1] N2[s1] + I/2 N3bar[s1].Ga[v,s1,s2].del[N3[s2],v] - 1/2 mN3 N3bar[s1] N3[s1]
```

### `LNCCbare` (`:=`)

```mathematica
gN/Sqrt[2]*(VeN1*N1bar.W[m].ProjM[m].e + VmuN1*N1bar.W[m].ProjM[m].mu + VtaN1*N1bar.W[m].ProjM[m].ta) + gN/Sqrt[2]*(VeN2*N2bar.W[m].ProjM[m].e + VmuN2*N2bar.W[m].ProjM[m].mu + VtaN2*N2bar.W[m].ProjM[m].ta) + gN/Sqrt[2]*(VeN3*N3bar.W[m].ProjM[m].e + VmuN3*N3bar.W[m].ProjM[m].mu + VtaN3*N3bar.W[m].ProjM[m].ta)
```

### `LNCC` (`:=`)

```mathematica
LNCCbare + HC[LNCCbare]
```

### `LNNCBare` (`:=`)

```mathematica
1/2*gN/cw*(VeN1*N1bar.Z[m].ProjM[m].ve + VmuN1*N1bar.Z[m].ProjM[m].vm + VtaN1*N1bar.Z[m].ProjM[m].vt) + 1/2*gN/cw*(VeN2*N2bar.Z[m].ProjM[m].ve + VmuN2*N2bar.Z[m].ProjM[m].vm + VtaN2*N2bar.Z[m].ProjM[m].vt) + 1/2*gN/cw*(VeN3*N3bar.Z[m].ProjM[m].ve + VmuN3*N3bar.Z[m].ProjM[m].vm + VtaN3*N3bar.Z[m].ProjM[m].vt)
```

### `LNNC` (`:=`)

```mathematica
LNNCBare + HC[LNNCBare]
```

### `LNHbare` (`:=`)

```mathematica
-gN*mN1/(2*MW)*(VeN1*N1bar.ProjM.ve H + VmuN1*N1bar.ProjM.vm H + VtaN1*N1bar.ProjM.vt H) - gN*mN2/(2*MW)*(VeN2*N2bar.ProjM.ve H + VmuN2*N2bar.ProjM.vm H + VtaN2*N2bar.ProjM.vt H) - gN*mN3/(2*MW)*(VeN3*N3bar.ProjM.ve H + VmuN3*N3bar.ProjM.vm H + VtaN3*N3bar.ProjM.vt H)
```

### `LNH` (`:=`)

```mathematica
LNHbare + HC[LNHbare]
```

### `LNGbare` (`:=`)

```mathematica
I*gN*mN1/(2*MW)*(VeN1*vebar.ProjP.N1 G0 + VmuN1*vmbar.ProjP.N1 G0 + VtaN1*vtbar.ProjP.N1 G0) + I*gN*mN2/(2*MW)*(VeN2*vebar.ProjP.N2 G0 + VmuN2*vmbar.ProjP.N2 G0 + VtaN2*vtbar.ProjP.N2 G0) + I*gN*mN3/(2*MW)*(VeN3*vebar.ProjP.N3 G0 + VmuN3*vmbar.ProjP.N3 G0 + VtaN3*vtbar.ProjP.N3 G0) + I*gN*mN1/(Sqrt[2]*MW)*(VeN1*ebar.ProjP.N1 GPbar + VmuN1*mubar.ProjP.N1 GPbar + VtaN1*tabar.ProjP.N1 GPbar) + I*gN*mN2/(Sqrt[2]*MW)*(VeN2*ebar.ProjP.N2 GPbar + VmuN2*mubar.ProjP.N2 GPbar + VtaN2*tabar.ProjP.N2 GPbar) + I*gN*mN3/(Sqrt[2]*MW)*(VeN3*ebar.ProjP.N3 GPbar + VmuN3*mubar.ProjP.N3 GPbar + VtaN3*tabar.ProjP.N3 GPbar)
```

### `LNG` (`:=`)

```mathematica
LNGbare + HC[LNGbare]
```

### `LN` (`:=`)

```mathematica
LNKin + LNCC + LNNC + LNH + LNG
```

### `LFull` (`:=`)

```mathematica
LSM + LN
```

## Blank-slate reconstruction

# Reconstructed Physics from `sanitized.fr`

## Lagrangian

The file defines
\[
\texttt{LFull}=\mathcal L_{\rm SM}+\texttt{LN},
\]
with
\[
\texttt{LN}=\texttt{LNKin}+\texttt{LNCC}+\texttt{LNNC}+\texttt{LNH}+\texttt{LNG}.
\]

The new fermions \(N_i\), \(i=1,2,3\), are self-conjugate neutral spin-\(\tfrac12\) fields. Since they are declared with \(Q=0\), \(Y=0\), no color index, and no weak-isospin index, their covariant derivative contains no gauge connection:
\[
D_\mu N_i=\partial_\mu N_i .
\]

Let \(\ell_\alpha=(e,\mu,\tau)\), \(\nu_\alpha=(\nu_e,\nu_\mu,\nu_\tau)\), and \(V_{\alpha i}\in\mathbb R\) denote the parameters
\[
V_{\alpha i}=
\begin{pmatrix}
\texttt{VeN1} & \texttt{VeN2} & \texttt{VeN3}\\
\texttt{VmuN1} & \texttt{VmuN2} & \texttt{VmuN3}\\
\texttt{VtaN1} & \texttt{VtaN2} & \texttt{VtaN3}
\end{pmatrix}.
\]
The internal coupling is
\[
g_N=\frac{e}{s_w}.
\]
Here \(P_L=\frac{1-\gamma^5}{2}\), \(P_R=\frac{1+\gamma^5}{2}\). FeynRules `ProjM` is expanded as \(P_L\), and `ProjP` as \(P_R\).

### `LNKin`

\[
\boxed{
\texttt{LNKin}
=
\sum_{i=1}^3
\left[
\frac{i}{2}\,\overline N_i\gamma^\mu\partial_\mu N_i
-
\frac{1}{2}m_{N_i}\,\overline N_i N_i
\right]
}
\]

### `LNCC`

The bare term in the file is
\[
\texttt{LNCCbare}
=
\frac{g_N}{\sqrt2}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \ell_\alpha\,W_\mu .
\]

The Lagrangian term is
\[
\boxed{
\texttt{LNCC}
=
\frac{g_N}{\sqrt2}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \ell_\alpha\,W_\mu
+\text{h.c.}
}
\]

### `LNNC`

The bare term in the file is
\[
\texttt{LNNCBare}
=
\frac{g_N}{2c_w}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \nu_\alpha\,Z_\mu .
\]

The Lagrangian term is
\[
\boxed{
\texttt{LNNC}
=
\frac{g_N}{2c_w}
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
V_{\alpha i}\,
\overline N_i\gamma^\mu P_L \nu_\alpha\,Z_\mu
+\text{h.c.}
}
\]

### `LNH`

The bare term in the file is
\[
\texttt{LNHbare}
=
-
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline N_i P_L \nu_\alpha\,H .
\]

The Lagrangian term is
\[
\boxed{
\texttt{LNH}
=
-
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline N_i P_L \nu_\alpha\,H
+\text{h.c.}
}
\]

### `LNG`

The neutral-Goldstone part of the bare term is
\[
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline{\nu_\alpha}P_R N_i\,G^0 .
\]

The charged-Goldstone part of the bare term is
\[
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{\sqrt2 M_W}
V_{\alpha i}\,
\overline{\ell_\alpha}P_R N_i\,G^- .
\]

Thus
\[
\boxed{
\texttt{LNG}
=
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{2M_W}
V_{\alpha i}\,
\overline{\nu_\alpha}P_R N_i\,G^0
+
i
\sum_{i=1}^3\sum_{\alpha=e,\mu,\tau}
\frac{g_N m_{N_i}}{\sqrt2 M_W}
V_{\alpha i}\,
\overline{\ell_\alpha}P_R N_i\,G^-
+\text{h.c.}
}
\]

## Field Table

| `.fr` class | Symbol | Spin | SU(3) rep | SU(2) rep | \(U(1)\) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `F[131]` | `N1` | \(1/2\) | singlet, no color index declared | singlet, no weak index declared | \(Q=0,\ Y=0\) | yes | `mN1 = 300.` |
| `F[132]` | `N2` | \(1/2\) | singlet, no color index declared | singlet, no weak index declared | \(Q=0,\ Y=0\) | yes | `mN2 = 500.` |
| `F[133]` | `N3` | \(1/2\) | singlet, no color index declared | singlet, no weak index declared | \(Q=0,\ Y=0\) | yes | `mN3 = 1000.` |

Widths are also declared:
\[
\texttt{WN1}=0.303,\qquad
\texttt{WN2}=1.50,\qquad
\texttt{WN3}=12.3.
\]

## Parameters

| Parameter | Type | Value | Multiplies | Physical meaning |
|---|---:|---:|---|---|
| `VeN1` | external, real | `1.0` | \(N_1\)-electron-family terms in `LNCC`, `LNNC`, `LNH`, `LNG` | mixing coefficient between \(N_1\) and the electron lepton family |
| `VeN2` | external, real | `0.0` | \(N_2\)-electron-family terms | mixing coefficient between \(N_2\) and the electron lepton family |
| `VeN3` | external, real | `0.0` | \(N_3\)-electron-family terms | mixing coefficient between \(N_3\) and the electron lepton family |
| `VmuN1` | external, real | `0.0` | \(N_1\)-muon-family terms | mixing coefficient between \(N_1\) and the muon lepton family |
| `VmuN2` | external, real | `1.0` | \(N_2\)-muon-family terms | mixing coefficient between \(N_2\) and the muon lepton family |
| `VmuN3` | external, real | `0.0` | \(N_3\)-muon-family terms | mixing coefficient between \(N_3\) and the muon lepton family |
| `VtaN1` | external, real | `0.0` | \(N_1\)-tau-family terms | mixing coefficient between \(N_1\) and the tau lepton family |
| `VtaN2` | external, real | `0.0` | \(N_2\)-tau-family terms | mixing coefficient between \(N_2\) and the tau lepton family |
| `VtaN3` | external, real | `1.0` | \(N_3\)-tau-family terms | mixing coefficient between \(N_3\) and the tau lepton family |

The file also defines one internal parameter:
\[
\texttt{gN}=\frac{\texttt{ee}}{\texttt{sw}},
\]
so the new interactions use the Standard Model weak \(SU(2)_L\) coupling normalization.

## Physics Summary

The model adds three electrically neutral, hypercharge-zero, self-conjugate spin-\(\tfrac12\) fermions \(N_1,N_2,N_3\) to the Standard Model. They are gauge singlets at the level of their kinetic terms, but interact through mixing-suppressed charged-current, neutral-current, Higgs, and Goldstone couplings to the SM lepton families.

It mediates processes such as production and decay of heavy neutral leptons through \(W^\pm\), \(Z\), and Higgs exchange, including channels \(N_i\leftrightarrow \ell_\alpha W\), \(N_i\leftrightarrow \nu_\alpha Z\), and \(N_i\leftrightarrow \nu_\alpha H\), with rates controlled by \(V_{\alpha i}\) and the masses \(m_{N_i}\).

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Locations

The paper defines the heavy-neutrino model in the **“HEAVY NEUTRINO MODEL”** section.

Relevant definitions:

- **Eq. (7):** chiral neutrino fields are rotated into light and heavy mass eigenstates using blocks \(U_{3\times3}\), \(V_{3\times n}\), \(X_{n\times3}\), \(Y_{n\times n}\).
- **Eq. (8):** the flavor neutrino state is
  \[
  \nu_\ell=\sum_{m=1}^3 U_{\ell m}\nu_m+\sum_{m'=1}^n V_{\ell m'}N^c_{m'} .
  \]
- Immediately after Eq. (8), the paper states: **“For simplicity, we consider only one heavy mass eigenstate, labeled by \(N\).”**
- **Eq. (9):** the electroweak interaction Lagrangian with \(W\), \(Z\), and \(h\) is given.
- **“COMPUTATIONAL SETUP” section:** the paper says the above Lagrangian is implemented **“with Goldstone boson couplings in the Feynman gauge”**, but does not print the Goldstone terms explicitly.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---:|---|
| Heavy-light mixing rotation \((\nu_L, N_R^c)^T = \begin{pmatrix}U & V\\ X & Y\end{pmatrix}(\nu_m,N_{m'}^c)^T\), Eq. (7) | Three independent self-conjugate neutral fermions \(N_i\), \(i=1,2,3\), with mixing parameters \(V_{\alpha i}\) | disagree | The paper gives the general \(n\)-heavy-state rotation but then specializes the analysis to **one** heavy mass eigenstate \(N\). The reconstruction keeps three heavy states \(N_1,N_2,N_3\). |
| Flavor state \(\nu_\ell=\sum_m U_{\ell m}\nu_m+\sum_{m'}V_{\ell m'}N^c_{m'}\), Eq. (8) | Uses \(\ell_\alpha\), \(\nu_\alpha\), and \(V_{\alpha i}\), but does not reconstruct the \(U_{\ell m}\) light-neutrino mixing part | missing-in-reconstruction | The reconstruction captures active-heavy mixing \(V_{\alpha i}\), but omits the explicit light-neutrino PMNS block \(U_{\ell m}\) appearing in the paper’s field definition. |
| Paper specialization to one heavy mass eigenstate \(N\), text after Eq. (8) | Field table contains \(N_1,N_2,N_3\) with masses 300, 500, 1000 GeV and widths 0.303, 1.50, 12.3 | disagree | The reconstruction appears to describe a three-heavy-neutrino implementation or benchmark file, not the one-heavy-state simplified model printed in the paper. |
| New heavy field is a neutral heavy neutrino mass eigenstate \(N\), Eqs. (7)-(9) | \(N_i\) are neutral, color-singlet, weak-singlet, hypercharge-zero, self-conjugate spin-\(\tfrac12\) fields | agree | The singlet Majorana interpretation is consistent with the Type-I-like heavy-neutrino setup and the use of \(N^c\) in the paper, aside from the multiplicity mismatch. |
| Heavy-neutrino kinetic and mass terms, implicit in the mass-eigenstate setup around Eqs. (7)-(9) | \(\sum_i \left[\frac{i}{2}\bar N_i\gamma^\mu\partial_\mu N_i-\frac12 m_{N_i}\bar N_iN_i\right]\) | agree | The Majorana normalization is standard. The paper does not print this term explicitly, so agreement is with the implied field content, not with a displayed equation. |
| Light-neutrino charged-current term \(-\frac{g}{\sqrt2}W^+_\mu\sum_{\ell=e}^{\tau}\sum_{m=1}^3 \bar\nu_m U^*_{\ell m}\gamma^\mu P_L\ell^- + \mathrm{H.c.}\), Eq. (9) | Not included except through a generic \(\mathcal L_{\rm SM}\) placeholder | missing-in-reconstruction | If \(\mathcal L_{\rm SM}\) is meant to include the PMNS-rotated light-neutrino charged current, this may be only a documentation omission. As written, the reconstruction does not state the \(U_{\ell m}\) structure. |
| Heavy-neutrino charged-current term \(-\frac{g}{\sqrt2}W^+_\mu\sum_{\ell=e}^{\tau}\bar N^c V^*_{\ell N}\gamma^\mu P_L\ell^-+\mathrm{H.c.}\), Eq. (9) | \(+\frac{g_N}{\sqrt2}\sum_{i,\alpha}V_{\alpha i}\bar N_i\gamma^\mu P_L\ell_\alpha W_\mu+\mathrm{h.c.}\), with \(g_N=e/s_w\) | disagree | Coupling magnitude and chirality agree if \(g_N=g\), \(V\) is real, and \(N=N^c\). Differences: sign, \(V^*\) vs real \(V\), \(W^+\) charge labeling suppressed, and three \(N_i\) instead of one \(N\). |
| Light-neutrino neutral-current term \(-\frac{g}{2c_W}Z_\mu\sum_{\ell=e}^{\tau}\sum_{m=1}^3\bar\nu_m U^*_{\ell m}\gamma^\mu P_L\nu_\ell+\mathrm{H.c.}\), Eq. (9) | Not included except through generic \(\mathcal L_{\rm SM}\) placeholder | missing-in-reconstruction | The reconstruction does not spell out the PMNS light-neutrino neutral current present in the paper’s Eq. (9). |
| Heavy-neutrino neutral-current term \(-\frac{g}{2c_W}Z_\mu\sum_{\ell=e}^{\tau}\bar N^c V^*_{\ell N}\gamma^\mu P_L\nu_\ell+\mathrm{H.c.}\), Eq. (9) | \(+\frac{g_N}{2c_w}\sum_{i,\alpha}V_{\alpha i}\bar N_i\gamma^\mu P_L\nu_\alpha Z_\mu+\mathrm{h.c.}\) | disagree | Coupling magnitude and left chirality agree under \(g_N=g\), real \(V\), and Majorana \(N\). Differences are the overall sign, missing complex conjugation, and three heavy states rather than the paper’s one-state simplification. |
| Heavy-neutrino Higgs term \(-\frac{g m_N}{2M_W}h\sum_{\ell=e}^{\tau}\bar N^c V^*_{\ell N}P_L\nu_\ell+\mathrm{H.c.}\), Eq. (9) | \(-\sum_{i,\alpha}\frac{g_Nm_{N_i}}{2M_W}V_{\alpha i}\bar N_iP_L\nu_\alpha H+\mathrm{h.c.}\) | disagree | Coefficient, mass proportionality, chirality, and sign match for one real-mixing Majorana state. Differences are \(V^*\) vs real \(V\), \(N^c\) vs \(N_i\), and three heavy states instead of one. |
| Goldstone boson couplings included in Feynman gauge, “COMPUTATIONAL SETUP” section | Neutral Goldstone \(i\frac{g_Nm_{N_i}}{2M_W}V_{\alpha i}\bar\nu_\alpha P_RN_iG^0+\mathrm{h.c.}\); charged Goldstone \(i\frac{g_Nm_{N_i}}{\sqrt2M_W}V_{\alpha i}\bar\ell_\alpha P_RN_iG^-+\mathrm{h.c.}\) | agree | The paper states Goldstone couplings are implemented but does not print them. The reconstruction has the standard Feynman-gauge mass-proportional Goldstone completion of the heavy-neutrino interactions, modulo the same one-vs-three and real-\(V\) issues. |
| Cross-section factorization \(\sigma(pp\to NX)=|V_{N\ell}|^2\sigma_0(pp\to NX)\), Eq. (10) | Mixing parameters \(V_{\alpha i}\) multiply all \(W/Z/h/G\) interactions; benchmark values are diagonal \(V_{eN1}=V_{\mu N2}=V_{\tau N3}=1\) | agree | The reconstruction’s interactions are linear in \(V_{\alpha i}\), so rates factorize as \(|V_{\alpha i}|^2\) for single-coupling channels. The benchmark choice with three unit mixings is not the one-heavy-state simplification used in the paper text. |
| Paper model uses SM weak coupling \(g\), Eq. (9) | Defines \(g_N=e/s_w\) | agree | This is the usual electroweak identity \(g=e/\sin\theta_W\). |

## Disagreements and Checks

| issue | severity | what a human should check |
|---|---:|---|
| The paper specializes to one heavy mass eigenstate \(N\), while the reconstruction contains three \(N_i\). | substantive | Check whether `sanitized.fr` intentionally implements a three-state generalization of the public model file, or whether the paper comparison should be restricted to a single selected state such as `n2`. |
| The reconstruction omits the explicit light-neutrino \(U_{\ell m}\) charged- and neutral-current terms from Eq. (9). | substantive | Check whether these terms are supplied by the imported SM/FeynRules base model or whether the implementation drops PMNS-rotated light-neutrino interactions. |
| The charged-current and neutral-current heavy-neutrino terms have the opposite displayed overall sign from Eq. (9). | convention | Check the FeynRules sign convention, field ordering, and whether a field or mixing-parameter phase redefinition makes the signs equivalent in generated vertices. |
| The reconstruction treats \(V_{\alpha i}\) as real, while the paper writes \(V^*_{\ell N}\). | substantive | Check whether the implementation is restricted to real active-heavy mixing or whether complex phases are supported elsewhere but lost in the reconstruction. |
| The reconstruction uses \(N_i\) directly, while Eq. (9) writes \(N^c\). | convention | For Majorana heavy neutrinos this is usually equivalent, but check the implementation’s Majorana/self-conjugate declaration and fermion-flow conventions. |
| The reconstruction gives explicit masses and widths for three heavy states, while the paper discusses results as functions of a single \(m_N\). | substantive | Check whether the benchmark masses and widths are implementation defaults rather than part of the paper’s analytical model definition. |
| The Goldstone terms are reconstructed explicitly, but the paper only states that Goldstone couplings are included in Feynman gauge. | cosmetic | Check the actual model file or generated Feynman rules if an exact sign-level validation of Goldstone vertices is required. |

## Overall Assessment

The reconstruction captures the core heavy-neutrino interaction structure of the paper: neutral Majorana singlet fermions coupled to SM leptons through active-heavy mixing, with the expected \(W\), \(Z\), Higgs, and Feynman-gauge Goldstone interactions and the correct weak-coupling normalization. The largest mismatch is scope: the paper’s displayed model specializes to one heavy mass eigenstate \(N\), while the reconstruction describes three benchmark heavy states with a matrix of real mixings. The reconstruction also suppresses or delegates the light-neutrino \(U_{\ell m}\) sector from Eq. (9), and it loses the paper’s complex conjugation on \(V_{\ell N}\). Most sign and \(N\) versus \(N^c\) differences may be convention-dependent for Majorana fields, but the heavy-state multiplicity and real-versus-complex mixing assumptions are physics-level differences a reviewer should verify against the actual implementation intent.

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

