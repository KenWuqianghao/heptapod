# Reverse-check review package — `ChernSimonsPortal_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `ChernSimonsPortal/model/ChernSimonsPortal_gen.fr` |
| original model name | `ChernSimonsPortal_gen` (hidden from the agent) |
| paper | ChernSimonsPortal/text/0901.0639.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LChernSimonsPortal` (`:=`)

```mathematica
c1 HC[H].DC[H, mu]/(HC[H].H) xb[nu] FS[B, la, ro] Eps[mu, nu, la, ro] + c2 HC[H].Ta[aa].DC[H, mu]/(HC[H].H) xb[nu] FS[Wi, la, ro, aa] Eps[mu, nu, la, ro]
```

### `LChernSimonsPortalBroken` (`:=`)

```mathematica
1/2 c1 sw xb[mu] Z[nu] del[Z[ro], la] Eps[mu, nu, la, ro] + c1 cw xb[mu] Z[nu] del[A[ro], la] Eps[mu, nu, la, ro] + c2 xb[mu] W[nu] HC[del[W[ro], la]] Eps[mu, nu, la, ro]
```

## Blank-slate reconstruction

# Reconstructed Physics from `sanitized.fr`

## Lagrangian

The file defines one new real vector field, denoted here by \(X_\mu \equiv \texttt{xb}_\mu\). It also defines two Lagrangian symbols: `LChernSimonsPortal` in the electroweak gauge basis and `LChernSimonsPortalBroken` in the broken basis.

The Higgs doublet is \(H_i\), with
\[
H^\dagger H \equiv H_i^\dagger H_i .
\]

The covariant derivative appearing in `DC[H, mu]` is the Standard Model electroweak covariant derivative on the Higgs doublet,
\[
D_\mu H
=
\left(
\partial_\mu
+ i g_w T^a W^a_\mu
+ i g_1 Y_H B_\mu
\right)H,
\qquad
Y_H=\frac12,
\qquad
T^a=\frac{\tau^a}{2}.
\]

The field strengths are
\[
B_{\lambda\rho}
=
\partial_\lambda B_\rho-\partial_\rho B_\lambda ,
\]
\[
W^a_{\lambda\rho}
=
\partial_\lambda W^a_\rho-\partial_\rho W^a_\lambda
+ g_w \epsilon^{abc} W^b_\lambda W^c_\rho .
\]

`Eps[mu,nu,la,ro]` is \(\epsilon^{\mu\nu\lambda\rho}\).

### `LChernSimonsPortal`

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortal},\,c_1}
=
c_1\,
\frac{H^\dagger_i (D_\mu H)_i}{H^\dagger_j H_j}\,
X_\nu\,
B_{\lambda\rho}\,
\epsilon^{\mu\nu\lambda\rho}
}
\]

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortal},\,c_2}
=
c_2\,
\frac{
H^\dagger_i (T^a)^i{}_{j} (D_\mu H)_j
}{
H^\dagger_k H_k
}\,
X_\nu\,
W^a_{\lambda\rho}\,
\epsilon^{\mu\nu\lambda\rho}
}
\]

### `LChernSimonsPortalBroken`

Using the `.fr` broken-basis fields \(A_\mu\), \(Z_\mu\), and the charged field \(W_\mu\) with `HC[W]` its Hermitian conjugate:

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,ZZ}
=
\frac12\,c_1\,s_w\,
X_\mu Z_\nu
\left(\partial_\lambda Z_\rho\right)
\epsilon^{\mu\nu\lambda\rho}
}
\]

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,ZA}
=
c_1\,c_w\,
X_\mu Z_\nu
\left(\partial_\lambda A_\rho\right)
\epsilon^{\mu\nu\lambda\rho}
}
\]

\[
\boxed{
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,WW}
=
c_2\,
X_\mu W_\nu
\left(\partial_\lambda W_\rho^\dagger\right)
\epsilon^{\mu\nu\lambda\rho}
}
\]

Equivalently, if the FeynRules charged field `W` is the positively charged field,
\[
\mathcal L_{\texttt{LChernSimonsPortalBroken},\,WW}
=
c_2\,
X_\mu W^+_\nu
\left(\partial_\lambda W^-_\rho\right)
\epsilon^{\mu\nu\lambda\rho}.
\]

No explicit `HC[...]` is wrapped around the full Lagrangian terms in the file, so the expressions above are the terms exactly as encoded.

## Field Table

| Symbol | FeynRules class | Spin | SU(3) rep | SU(2) rep | \(Q\) | \(Y\) | Self-conjugate | Mass |
|---|---:|---:|---|---|---:|---:|---|---|
| \(X_\mu\) / `xb` | `V[92]` | 1 | singlet, no color index declared | singlet, no weak index declared | 0 | 0 | yes | \(M_{\texttt{xb}} = 1.0\) |

The file also declares a width parameter:
\[
W_{\texttt{xb}} = 1.0 .
\]

## Parameters

| Symbol | Value | External? | Multiplies | Meaning |
|---|---:|---|---|---|
| `c1` | \(0.001\) | yes | \(\dfrac{H^\dagger D_\mu H}{H^\dagger H} X_\nu B_{\lambda\rho}\epsilon^{\mu\nu\lambda\rho}\), and in the broken basis the \(XZZ\) and \(XZ\gamma\) terms | dimensionless Chern-Simons portal coupling to the hypercharge field strength |
| `c2` | \(0.001\) | yes | \(\dfrac{H^\dagger T^a D_\mu H}{H^\dagger H} X_\nu W^a_{\lambda\rho}\epsilon^{\mu\nu\lambda\rho}\), and in the broken basis the charged \(XW^+W^-\) term | dimensionless Chern-Simons portal coupling to the weak-isospin field strength |

## Physics Summary

This is a Chern-Simons-like electroweak portal model containing a new electrically neutral, hypercharge-zero, self-conjugate massive spin-1 boson \(X_\mu\). The new vector couples through Higgs-dressed electroweak structures to the hypercharge and weak field strengths, producing anomalous-looking \(XZZ\), \(XZ\gamma\), and \(XW^+W^-\) interactions after electroweak symmetry breaking. It would mediate production or decay channels involving the new neutral vector together with electroweak gauge bosons, such as \(X \leftrightarrow Z\gamma\), \(X \leftrightarrow ZZ\), and charged \(W^+W^-\)-associated processes, depending on kinematics and how \(X\) is produced.

## Paper cross-check

## Source Locations

The paper defines the low-energy model in Section 2, especially Eq. (1) for the SM plus massive \(U_X(1)\) vector sector, Eq. (2) for the desired broken-phase \(XZZ\), \(XZ\gamma\), and \(XW^+W^-\) structures, and Eq. (5) for the gauge-covariant D'Hoker-Farhi interaction terms. The UV field content and charges are given in Section 4, especially Table 4, Eq. (24), and the explicit charge example in Table 5. The broken-phase vertices used for phenomenology are given in Section 5, Eqs. (25)-(28).

## Term-By-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| \(L = L_{\rm SM}-\frac{1}{4g_X^2}\lvert F_X\rvert^2+\frac{M_X^2}{2}\lvert D\theta_X\rvert^2+L_{\rm int}\), with \(D\theta_X=d\theta_X+X\) (Section 2, Eq. (1)) | One new real vector \(X_\mu\), self-conjugate, massive; mass and width parameters listed | missing-in-reconstruction | The reconstruction captures the existence of a neutral massive vector but omits the explicit \(X\) kinetic normalization, the Stückelberg field \(\theta_X\), and the gauge-invariant \(D\theta_X\) mass structure. |
| Desired broken interactions \(\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda Z_\rho\), \(\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda\gamma_\rho\), \(\epsilon^{\mu\nu\lambda\rho}W^+_\mu X_\nu\partial_\lambda W^-_\rho\) (Section 2, Eq. (2)) | Broken-basis \(XZZ\), \(XZ A\), and \(XWW^\dagger\) terms | agree | The same three phenomenological structures are present, up to notation \(A=\gamma\) and possible index relabeling. |
| Gauge-covariant interaction \(L_{\rm int}=c_1\frac{H^\dagger D H}{\lvert H\rvert^2}D\theta_X F_Y+c_2\frac{H F_W D H^\dagger}{\lvert H\rvert^2}D\theta_X\) (Section 2, Eq. (5)) | \(c_1\frac{H^\dagger D_\mu H}{H^\dagger H}X_\nu B_{\lambda\rho}\epsilon^{\mu\nu\lambda\rho}\) and \(c_2\frac{H^\dagger T^aD_\mu H}{H^\dagger H}X_\nu W^a_{\lambda\rho}\epsilon^{\mu\nu\lambda\rho}\) | disagree | The \(c_1\) structure agrees in unitary gauge if \(D\theta_X\to X\). The \(c_2\) structure is not written with the same Higgs conjugation/order as the paper’s \(H F_W D H^\dagger\), and the reconstruction also replaces \(D\theta_X\) by \(X\). |
| Coefficients \(c_1,c_2\) are dimensionless and UV-determined (Section 2, after Eq. (5)) | External parameters \(c_1=c_2=0.001\), dimensionless | agree | The reconstruction adds implementation benchmark values, but the coefficient role and dimensionality match. |
| Toy UV Yukawa Lagrangian with chiral fermions and scalars in \(U(1)_A\times U(1)_B\) model (Section 2, Eq. (6), Table 1) | No corresponding fields or Yukawa terms | missing-in-reconstruction | This toy model is part of the paper’s explanatory construction, not necessarily the final FeynRules model, but it is absent from the reconstruction. |
| Low-energy toy Chern-Simons action \(S_{\rm cs}\), including \(\theta_BF_A\wedge F_A\), \(\theta_AF_A\wedge F_B\), and \(A\wedge B\wedge F_A\) (Section 2, Eq. (7)) | No corresponding toy-model action | missing-in-reconstruction | Absent from reconstruction. |
| Gauge-invariant toy result \(S_{\rm cs}=\int\kappa D\theta_A\wedge D\theta_B\wedge F_A\) (Section 2, Eq. (8)) | No corresponding toy-model action | missing-in-reconstruction | Absent from reconstruction. |
| SM toy model with heavy fermions, two Higgs fields \(H,\Phi\), VEV hierarchy \(v\ll V\), charge tables, and Yukawa structure (Section 3, Eqs. (11)-(24), Tables 2-3) | No heavy fermions, no \(\Phi\), no UV Yukawa structure | missing-in-reconstruction | The reconstruction only describes the low-energy portal implementation, not the UV completion developed in the paper. |
| Realistic UV fermion content: SU(2) doublets \(\psi^a_{1L},\chi^a_{2L},\psi^a_{2R},\chi^a_{1R}\), singlets \(\psi_{2L},\chi_{1L},\psi_{1R},\chi_{2R}\), with charges in Table 4 (Section 4, Table 4) | Only \(X_\mu\) is listed as a new field | missing-in-reconstruction | The paper’s realistic UV model contains several heavy chiral fermions and a heavy Higgs \(\Phi\); these are absent. |
| Realistic UV Yukawa interactions with \(H\) and \(\Phi_{1,2}\) (Section 4, Eq. (24)) | No corresponding Yukawa sector | missing-in-reconstruction | The implementation reconstruction omits the UV mass-generation sector entirely. |
| Explicit anomaly-free charge assignment for the realistic \(SU(2)\times U_Y(1)\times U_X(1)\) model (Section 4, Table 5) | \(X_\mu\) is neutral under SM and self-conjugate; no heavy-sector charges | missing-in-reconstruction | The reconstruction does not reproduce the heavy fermion charges responsible for the anomaly cancellation. |
| Broken-phase first interaction \(L_{XZY}=c_1(d\theta_Z+Z)F_YD\theta_X+O(\partial h/v)\) (Section 5, Eq. (25)) | \(XZZ\) and \(XZ\gamma\) broken-basis terms | agree | The reconstruction captures the leading gauge-boson interactions after taking unitary gauge and omitting Higgs-derivative corrections. |
| Higgs parametrization \(H=e^{i(\tau^+\theta^++\tau^-\theta^-+(\frac12+\tau^3)\theta_Z)}(0,v+h)^T\) (Section 5, Eq. (26)) | Standard Higgs doublet \(H_i\), \(H^\dagger H\), SM covariant derivative | missing-in-reconstruction | The reconstruction does not include the paper’s Goldstone parametrization or the \(O(\partial h/v)\) terms. |
| \(\Gamma^{\mu\nu\rho}_{XZZ}=\frac12c_1\sin\theta_w\epsilon^{\mu\nu\lambda\rho}(k_{2\lambda}-k_{1\lambda})\) (Section 5, Eq. (27)) | \(\frac12c_1s_w X_\mu Z_\nu(\partial_\lambda Z_\rho)\epsilon^{\mu\nu\lambda\rho}\) | agree | For two identical \(Z\) fields, the single derivative term gives the antisymmetrized momentum dependence of Eq. (27). |
| \(\Gamma^{\mu\nu\rho}_{XZ\gamma}=c_1\cos\theta_w\epsilon^{\mu\nu\lambda\rho}k_{2\rho}\) (Section 5, Eq. (27)) | \(c_1c_wX_\mu Z_\nu(\partial_\lambda A_\rho)\epsilon^{\mu\nu\lambda\rho}\) | agree | Same \(XZ\gamma\) structure, modulo index-label conventions for the photon momentum. |
| \(\Gamma^{\mu\nu\rho}_{XW^+W^-}=c_2\epsilon^{\mu\nu\lambda\rho}(k_{2\lambda}-k_{1\lambda})\) (Section 5, Eq. (28)) | \(c_2X_\mu W_\nu(\partial_\lambda W^\dagger_\rho)\epsilon^{\mu\nu\lambda\rho}\), with no full Hermitian conjugate | disagree | The paper’s vertex is antisymmetric in the two charged \(W\) momenta. The reconstructed single derivative term gives only one momentum unless the implementation has an implicit conjugate or equivalent antisymmetrization not reflected in the reconstruction. |
| Decay widths \(\Gamma_{X\to ZZ}\), \(\Gamma_{X\to W^+W^-}\), \(\Gamma_{X\to Z\gamma}\) (Section 5, Eq. (31)) | No decay-width terms | missing-in-reconstruction | Phenomenological consequences are summarized qualitatively but the formulas are not reconstructed. |
| Branching-ratio relations \( \Gamma_{Z\gamma}/\Gamma_{ZZ}=2\cos^2\theta_w/\sin^2\theta_w\), \( \Gamma_{WW}/\Gamma_{ZZ}=4c_2^2/(c_1^2\sin^2\theta_w)\) (Section 5, Eqs. (32)-(33)) | No explicit branching-ratio relations | missing-in-reconstruction | Not part of the Lagrangian implementation, but present in the paper’s model phenomenology. |
| Implementation mass \(M_{\texttt{xb}}=1.0\) and width \(W_{\texttt{xb}}=1.0\) | Listed in reconstruction | extra-in-reconstruction | The paper treats \(M_X\) as a free phenomenological mass scale and does not define these benchmark implementation values. |
| Explicit electroweak covariant derivative convention \(D_\mu H=(\partial_\mu+ig_wT^aW^a_\mu+ig_1Y_HB_\mu)H\), \(Y_H=1/2\) | Listed in reconstruction | convention | The paper uses differential-form notation and a Higgs hypercharge normalization in which some tables quote \(Q_Y(H)=1\). This is mostly a normalization/convention issue if gauge couplings are adjusted consistently. |

## Disagreements And Checks

1. **Replacement of \(D\theta_X\) by \(X_\mu\)** — severity: convention. A human should check whether the implementation is explicitly in unitary gauge or whether the Stückelberg/Goldstone mode was unintentionally omitted.

2. **Second gauge-covariant \(c_2\) operator differs in Higgs conjugation/order** — severity: substantive. A human should verify from the implementation whether \(H^\dagger T^a D_\mu H\,W^a_{\lambda\rho}\) is truly equivalent to the paper’s \(H F_W D H^\dagger\) after integration by parts, conjugation, and convention choices.

3. **Broken \(XW^+W^-\) term lacks an explicit antisymmetrized or Hermitian-conjugate contribution** — severity: substantive. A human should check the generated Feynman rule and confirm whether it produces the paper’s \((k_2-k_1)\) momentum structure in Eq. (28).

4. **UV heavy fermion sector is absent** — severity: substantive. A human should decide whether the implementation is intended to encode only the low-energy effective theory or the full anomaly-canceling UV model of Section 4.

5. **Heavy scalar \(\Phi\) and UV Yukawa terms are absent** — severity: substantive. A human should check whether the implementation intentionally integrates out \(\Phi\) and the heavy fermions, leaving only Eq. (5), or whether these fields were expected to be present.

6. **Paper’s Stückelberg mass-sector normalization is not reconstructed** — severity: convention. A human should check whether the vector kinetic and mass normalization in the implementation matches the paper’s \( -|F_X|^2/(4g_X^2)+M_X^2|D\theta_X|^2/2\).

7. **Implementation benchmark values \(c_1=c_2=0.001\), \(M_X=1.0\), width \(=1.0\) are not paper definitions** — severity: cosmetic. A human should check whether these are harmless simulation defaults rather than claimed physical predictions from the paper.

8. **Higgs hypercharge normalization differs in presentation** — severity: convention. A human should check that the implementation’s \(Y_H=1/2\) convention is consistently mapped to the paper’s charge normalization where \(Q_Y(H)=1\) appears in the UV charge tables.

## Overall Assessment

The reconstruction captures the low-energy phenomenological core of the paper: a new neutral massive vector \(X\) coupled through Chern-Simons-like electroweak portal operators that generate \(XZZ\), \(XZ\gamma\), and \(XW^+W^-\) interactions. It is much less complete as a reconstruction of the full paper model, because it omits the Stückelberg field, the explicit \(X\) kinetic/mass structure, the heavy anomaly-canceling fermion sector, the heavy scalar \(\Phi\), and the UV Yukawa/charge assignments of Section 4. The most important technical point to check is whether the reconstructed \(c_2\) operator and the broken-basis \(XW^+W^-\) term really reproduce the paper’s Eq. (28) momentum structure; if they do, the reconstruction is a reasonable low-energy/unitary-gauge implementation rather than a full UV model.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 3 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

