# Reverse-check review package — `DMsimp_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `DMsimp/model/DMsimp_gen.fr` |
| original model name | `DMsimp_gen` (hidden from the agent) |
| paper | DMsimp/text/1508.00564.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `L0X` (`:=`)

```mathematica
1/2 MXr gSXr Xr Xr Y0 + MXc gSXc Xcbar Xc Y0 + Xdbar.(gSXd + I gPXd Ga[5]).Xd Y0
```

### `L0SM` (`:=`)

```mathematica
1/Sqrt[2] yt tbar.(gSt + I gPt Ga[5]).t Y0
```

### `L0SMg` (`:=`)

```mathematica
1/Lambda FS[G,mu,nu,a] (gSg FS[G,mu,nu,a] + gPg Dual[FS][G,mu,nu,a]) Y0
```

### `L0DM` (`:=`)

```mathematica
L0X + L0SM + L0SMg
```

### `L1X` (`:=`)

```mathematica
I gVXc/2 (Xcbar del[Xc,mu] - del[Xcbar,mu] Xc) Y1[mu] + Xdbar.Ga[mu].(gVXd + gAXd Ga[5]).Xd Y1[mu]
```

### `L1SM` (`:=`)

```mathematica
tbar.Ga[mu].(gVt + gAt Ga[5]).t Y1[mu] + bbar.Ga[mu].(-gAt Ga[5]).b Y1[mu]
```

### `L1DM` (`:=`)

```mathematica
L1X + L1SM
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Conventions: repeated Lorentz and color indices are summed. The gluon field strength is
\[
G^a_{\mu\nu}
=
\partial_\mu G^a_\nu-\partial_\nu G^a_\mu
+ g_s f^{abc}G^b_\mu G^c_\nu ,
\qquad
\widetilde G^{a\mu\nu}
=
\frac12 \epsilon^{\mu\nu\rho\sigma}G^a_{\rho\sigma}.
\]
No `DC[...]` covariant derivatives appear in the file. The only derivative acting on a new field is an ordinary partial derivative. All new fields have `Q -> 0` and no declared color or weak indices, so they are SM gauge singlets; their gauge covariant derivative would therefore reduce to
\[
D_\mu = \partial_\mu
\]
on the new fields. The SM quark and gluon objects use the standard FeynRules SM gauge content.

### `L0X`

\[
\mathcal L_{\texttt{L0X},\,X_r}
=
\frac12\, M_{X_r}\, g_{S X_r}\, X_r X_r\, Y_0 .
\]

\[
\mathcal L_{\texttt{L0X},\,X_c}
=
M_{X_c}\, g_{S X_c}\, X_c^\dagger X_c\, Y_0 .
\]

\[
\mathcal L_{\texttt{L0X},\,X_d}
=
\bar X_d
\left(
g^S_{\rm DM}
+ i g^P_{\rm DM}\gamma^5
\right)
X_d\,Y_0 .
\]

### `L0SM`

\[
\mathcal L_{\texttt{L0SM}}
=
\frac{y_t}{\sqrt2}\,
\bar t_i
\left(
g^S_t
+ i g^P_t\gamma^5
\right)
t_i\,Y_0 .
\]

Here \(i\) is the color index, contracted as \(\delta_{ij}\).

### `L0SMg`

\[
\mathcal L_{\texttt{L0SMg},\,S}
=
\frac{g^S_g}{\Lambda}\,
Y_0\,G^a_{\mu\nu}G^{a\mu\nu}.
\]

\[
\mathcal L_{\texttt{L0SMg},\,P}
=
\frac{g^P_g}{\Lambda}\,
Y_0\,G^a_{\mu\nu}\widetilde G^{a\mu\nu}.
\]

### `L0DM`

\[
\mathcal L_{\texttt{L0DM}}
=
\mathcal L_{\texttt{L0X}}
+
\mathcal L_{\texttt{L0SM}}
+
\mathcal L_{\texttt{L0SMg}} .
\]

### `L1X`

\[
\mathcal L_{\texttt{L1X},\,X_c}
=
\frac{i g_{V X_c}}{2}
\left[
X_c^\dagger \partial_\mu X_c
-
(\partial_\mu X_c^\dagger)X_c
\right]
Y_1^\mu .
\]

\[
\mathcal L_{\texttt{L1X},\,X_d}
=
\bar X_d\gamma^\mu
\left(
g^V_{\rm DM}
+
g^A_{\rm DM}\gamma^5
\right)
X_d\,Y_{1\mu}.
\]

Equivalently, in chiral form,
\[
\bar X_d\gamma^\mu
\left[
(g^V_{\rm DM}-g^A_{\rm DM})P_L
+
(g^V_{\rm DM}+g^A_{\rm DM})P_R
\right]
X_d\,Y_{1\mu}.
\]

### `L1SM`

\[
\mathcal L_{\texttt{L1SM},\,t}
=
\bar t_i\gamma^\mu
\left(
g^V_t
+
g^A_t\gamma^5
\right)
t_i\,Y_{1\mu}.
\]

Equivalently,
\[
\bar t_i\gamma^\mu
\left[
(g^V_t-g^A_t)P_L
+
(g^V_t+g^A_t)P_R
\right]
t_i\,Y_{1\mu}.
\]

\[
\mathcal L_{\texttt{L1SM},\,b}
=
-\,g^A_t\,
\bar b_i\gamma^\mu\gamma^5 b_i\,Y_{1\mu}.
\]

Equivalently,
\[
\mathcal L_{\texttt{L1SM},\,b}
=
\bar b_i\gamma^\mu
\left[
g^A_t P_L
-
g^A_t P_R
\right]
b_i\,Y_{1\mu}.
\]

### `L1DM`

\[
\mathcal L_{\texttt{L1DM}}
=
\mathcal L_{\texttt{L1X}}
+
\mathcal L_{\texttt{L1SM}} .
\]

## Field Table

| Symbol | Class | Spin | SU(3) rep | SU(2) rep | U(1) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---|---|
| \(X_r\) | `S[7]` | 0 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | Yes, real scalar | \(M_{X_r}=10\) |
| \(X_c\) | `S[8]` | 0 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | No, complex scalar | \(M_{X_c}=10\) |
| \(X_d\) | `F[7]` | \(1/2\) | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | No, Dirac fermion | \(M_{X_d}=10\) |
| \(Y_0\) | `S[9]` | 0 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | Yes, real scalar | \(M_{Y_0}=1000\) |
| \(Y_1\) | `V[7]` | 1 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | Yes, real vector | \(M_{Y_1}=1000\) |

Widths declared in the file are \(\Gamma_{X_r}=0\), \(\Gamma_{X_c}=0\), \(\Gamma_{X_d}=0\), \(\Gamma_{Y_0}=W_{Y_0}=10\), and \(\Gamma_{Y_1}=W_{Y_1}=10\).

## Parameters

| Symbol | Default value | Appears in | Physical meaning |
|---|---:|---|---|
| `gSXr` | 0 | \(\frac12 M_{X_r} g_{S X_r} X_r^2 Y_0\) | Scalar coupling of the real scalar \(X_r\) to the scalar mediator \(Y_0\). |
| `gSXc` | 0 | \(M_{X_c} g_{S X_c} X_c^\dagger X_c Y_0\) | Scalar coupling of the complex scalar \(X_c\) to \(Y_0\). |
| `gSXd` | 1 | \(\bar X_d g^S_{\rm DM} X_d Y_0\) | Scalar Yukawa-like coupling of Dirac fermion \(X_d\) to \(Y_0\). |
| `gPXd` | 0 | \(i\bar X_d g^P_{\rm DM}\gamma^5 X_d Y_0\) | Pseudoscalar coupling of \(X_d\) to \(Y_0\). |
| `gSt` | 1 | \(\frac{y_t}{\sqrt2}\bar t g^S_t tY_0\) | Scalar coupling of \(Y_0\) to top quarks, normalized by \(y_t/\sqrt2\). |
| `gPt` | 0 | \(\frac{y_t}{\sqrt2}i\bar t g^P_t\gamma^5 tY_0\) | Pseudoscalar coupling of \(Y_0\) to top quarks, normalized by \(y_t/\sqrt2\). |
| `Lambda` | 10000 | \(\Lambda^{-1}Y_0G_{\mu\nu}G^{\mu\nu}\), \(\Lambda^{-1}Y_0G_{\mu\nu}\widetilde G^{\mu\nu}\) | Heavy scale suppressing the effective scalar and pseudoscalar gluon operators. |
| `gSg` | 0 | \(\frac{g^S_g}{\Lambda}Y_0G^a_{\mu\nu}G^{a\mu\nu}\) | Effective CP-even coupling of \(Y_0\) to gluons. |
| `gPg` | 0 | \(\frac{g^P_g}{\Lambda}Y_0G^a_{\mu\nu}\widetilde G^{a\mu\nu}\) | Effective CP-odd coupling of \(Y_0\) to gluons. |
| `gVXc` | 0 | \(\frac{i g_{V X_c}}2 X_c^\dagger\overleftrightarrow{\partial_\mu}X_c\,Y_1^\mu\) | Vector-current coupling of complex scalar \(X_c\) to vector mediator \(Y_1\). |
| `gVXd` | 1 | \(\bar X_d\gamma^\mu g^V_{\rm DM}X_dY_{1\mu}\) | Vector coupling of Dirac fermion \(X_d\) to \(Y_1\). |
| `gAXd` | 0 | \(\bar X_d\gamma^\mu g^A_{\rm DM}\gamma^5X_dY_{1\mu}\) | Axial-vector coupling of \(X_d\) to \(Y_1\). |
| `gVt` | 1 | \(\bar t\gamma^\mu g^V_t tY_{1\mu}\) | Vector coupling of \(Y_1\) to top quarks. |
| `gAt` | 0 | \(\bar t\gamma^\mu g^A_t\gamma^5tY_{1\mu}\), \(-\bar b\gamma^\mu g^A_t\gamma^5bY_{1\mu}\) | Axial-vector coupling of \(Y_1\) to tops and, with opposite sign structure in the Lagrangian, to bottoms. |

## Physics Summary

The file encodes a simplified SM-singlet dark-sector mediator setup with three possible dark matter candidates: a real scalar \(X_r\), a complex scalar \(X_c\), and a Dirac fermion \(X_d\). A scalar mediator \(Y_0\) couples to these dark states, to top quarks through scalar and pseudoscalar bilinears, and to gluons through dimension-five CP-even and CP-odd operators; a vector mediator \(Y_1\) couples to scalar and fermion dark currents, to top vector/axial currents, and to a bottom axial current.

The interactions mediate production or annihilation channels such as \(gg\to Y_0\to X\bar X\), \(t\bar t\to Y_0/Y_1\to X\bar X\), mediator-associated heavy-quark processes, and mediator decays into dark matter, tops, bottoms, or gluons depending on the enabled couplings and masses.

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Location

The paper defines the simplified model in **Section 2, “Simplified Model”**. It states that the mediator couples only to top quarks and dark matter, with a bottom-quark coupling added only for the axial-vector case to cancel the gauge anomaly. The dark matter particle \(\chi\) is taken to be a **Dirac fermion** in the study, although the implementation is described as flexible enough to allow real or complex scalar dark matter.

The interaction Lagrangians are:

- **Eq. (1)**: scalar mediator \(Y_0\)
  \[
  \mathcal L^{Y_0}_{DM}=\bar\chi(g^S_{DM}+i g^P_{DM}\gamma^5)\chi Y_0,
  \qquad
  \mathcal L^{Y_0}_{SM}=\bar t\,\frac{y_t}{\sqrt2}(g^S_t+i g^P_t\gamma^5)tY_0.
  \]

- **Eq. (2)**: vector mediator \(Y_1\)
  \[
  \mathcal L^{Y_1}_{DM}=\bar\chi\gamma^\mu(g^V_{DM}+g^A_{DM}\gamma^5)\chi Y_{1\mu},
  \]
  \[
  \mathcal L^{Y_1}_{SM}
  =
  \bar t\gamma^\mu(g^V_t+g^A_t\gamma^5)tY_{1\mu}
  +
  \bar b\gamma^\mu(-g^A_t\gamma^5)bY_{1\mu}.
  \]

- **Eq. (3)** appears later in Section 4.2 as an **infinite-top-mass EFT approximation**, not as the primary simplified-model Lagrangian:
  \[
  \mathcal L=
  \frac{\alpha_s}{12\pi v}g^S_t\,G_{\mu\nu}G^{\mu\nu}Y_0
  +
  \frac{\alpha_s}{8\pi v}g^P_t\,G_{\mu\nu}\tilde G^{\mu\nu}Y_0.
  \]

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Dirac dark matter \(\chi\), Section 2 | \(X_d\), Dirac fermion, SM singlet | agree | The paper uses \(\chi\); the reconstruction uses \(X_d\). Physics content matches for the fermionic DM used in the study. |
| Scalar mediator \(Y_0\), Section 2 / Eq. (1) | \(Y_0\), real scalar SM singlet | agree | The paper does not spell out gauge reps, but the mediator is a neutral s-channel boson; the reconstruction’s singlet assignment is consistent. |
| Vector mediator \(Y_1\), Section 2 / Eq. (2) | \(Y_1\), real vector SM singlet | agree | Consistent with the paper’s neutral vector mediator. |
| \(\bar\chi(g^S_{DM}+i g^P_{DM}\gamma^5)\chi Y_0\), Eq. (1) | \(\bar X_d(g^S_{DM}+i g^P_{DM}\gamma^5)X_dY_0\) | agree | Same scalar and pseudoscalar Dirac bilinears, same \(i\gamma^5\) structure. |
| \(\bar t\,\frac{y_t}{\sqrt2}(g^S_t+i g^P_t\gamma^5)tY_0\), Eq. (1) | \(\frac{y_t}{\sqrt2}\bar t_i(g^S_t+i g^P_t\gamma^5)t_iY_0\) | agree | Same top coupling and Yukawa normalization. Reconstruction makes the color contraction explicit. |
| \(\bar\chi\gamma^\mu(g^V_{DM}+g^A_{DM}\gamma^5)\chi Y_{1\mu}\), Eq. (2) | \(\bar X_d\gamma^\mu(g^V_{DM}+g^A_{DM}\gamma^5)X_dY_{1\mu}\) | agree | Same vector and axial-vector Dirac-current structure. |
| \(\bar t\gamma^\mu(g^V_t+g^A_t\gamma^5)tY_{1\mu}\), Eq. (2) | \(\bar t_i\gamma^\mu(g^V_t+g^A_t\gamma^5)t_iY_{1\mu}\) | agree | Same top vector and axial couplings; reconstruction makes color explicit. |
| \(\bar b\gamma^\mu(-g^A_t\gamma^5)bY_{1\mu}\), Eq. (2) | \(-g^A_t\bar b_i\gamma^\mu\gamma^5b_iY_{1\mu}\) | agree | Same bottom axial coupling, with opposite sign to the top axial coupling as required for anomaly cancellation. |
| Bottom coupling introduced only for axial-vector anomaly cancellation, Section 2 after Eq. (2) | Bottom term tied only to \(g^A_t\), no bottom vector term | agree | Reconstruction correctly omits a bottom vector coupling and includes only the axial structure. |
| Top-EFT scalar gluon operator \(\frac{\alpha_s}{12\pi v}g^S_tG_{\mu\nu}G^{\mu\nu}Y_0\), Eq. (3) | \(\frac{g^S_g}{\Lambda}Y_0G^a_{\mu\nu}G^{a\mu\nu}\) | disagree | Same operator shape, but different coefficient structure: paper’s Eq. (3) is fixed by \(\alpha_s/(12\pi v)\,g^S_t\), while reconstruction has an independent \(g^S_g/\Lambda\). |
| Top-EFT pseudoscalar gluon operator \(\frac{\alpha_s}{8\pi v}g^P_tG_{\mu\nu}\tilde G^{\mu\nu}Y_0\), Eq. (3) | \(\frac{g^P_g}{\Lambda}Y_0G^a_{\mu\nu}\widetilde G^{a\mu\nu}\) | disagree | Same CP-odd operator shape, but paper’s coefficient is \(\alpha_s/(8\pi v)\,g^P_t\); reconstruction uses independent \(g^P_g/\Lambda\). |
| Base simplified model in Section 2 has no independent \(Y_0GG\) or \(Y_0G\tilde G\) contact term | `L0SMg` included in `L0DM` | extra-in-reconstruction | Eq. (3) is discussed as an infinite-top-mass approximation later, not as an independent base-model interaction with free \(g_g/\Lambda\) coefficients. |
| Paper study takes \(\chi\) to be a Dirac fermion, Section 2 | \(X_r\) real scalar DM with \(\frac12M_{X_r}g_{SX_r}X_r^2Y_0\) | extra-in-reconstruction | The paper says the implementation is flexible to allow scalar DM, but the displayed paper Lagrangian and study use Dirac \(\chi\). |
| Paper study takes \(\chi\) to be a Dirac fermion, Section 2 | \(X_c\) complex scalar DM with \(M_{X_c}g_{SX_c}X_c^\dagger X_cY_0\) | extra-in-reconstruction | Same caveat: plausible implementation extension, but not part of the explicit paper Lagrangian. |
| Paper Eq. (2) gives vector mediator coupling to fermionic DM only | \(X_c^\dagger\overleftrightarrow{\partial_\mu}X_cY_1^\mu\) | extra-in-reconstruction | The complex-scalar vector current is not present in the paper’s displayed Lagrangian. |
| Masses and widths are free/benchmark-dependent, Section 2 and Tables 1-2 | Fixed defaults \(M_{X}=10\), \(M_{Y}=1000\), \(\Gamma_{Y}=10\) | disagree | The paper treats masses and widths as parameters and gives benchmark values; reconstruction reports implementation defaults that do not correspond to the paper’s benchmark table. |
| Scalar real-DM coupling in paper | None explicitly displayed | missing-in-reconstruction | Not applicable as a paper term: the paper does not provide explicit real-scalar DM Lagrangian terms, so there is no paper-defined scalar-DM term missing from the reconstruction. |
| Complex scalar-DM coupling in paper | None explicitly displayed | missing-in-reconstruction | Not applicable as a paper term: scalar DM is mentioned as implementation flexibility, not defined term-by-term in the paper. |

## Disagreements and Checks

- **Independent gluon contact operators** — severity: **substantive**. A human should check whether the implementation intentionally extends the paper model with free \(g^S_g/\Lambda\) and \(g^P_g/\Lambda\) operators, or whether these were meant to reproduce Eq. (3), in which case the coefficient mapping is missing.

- **Eq. (3) coefficient mismatch** — severity: **substantive**. A human should check whether \(g^S_g/\Lambda\) and \(g^P_g/\Lambda\) are externally constrained to \(\alpha_s g^S_t/(12\pi v)\) and \(\alpha_s g^P_t/(8\pi v)\); without that mapping, the reconstruction describes a more general EFT than the paper’s top-EFT approximation.

- **Real scalar dark matter \(X_r\)** — severity: **convention**. A human should check whether the review target is the paper’s displayed study model, which uses Dirac \(\chi\), or the broader implementation alluded to by the paper as allowing real scalar dark matter.

- **Complex scalar dark matter \(X_c\)** — severity: **convention**. A human should check whether the implementation file was expected to include scalar-DM options beyond the paper’s explicit Lagrangian.

- **Complex scalar vector-current coupling to \(Y_1\)** — severity: **convention**. A human should check whether this is an implementation extension for scalar DM rather than a mismatch with the fermionic paper model.

- **Default masses and widths** — severity: **cosmetic**. A human should check whether the reconstruction is reporting UFO/FeynRules default parameter values, because the paper’s physical benchmarks use different mass and width choices.

## Overall Assessment

The reconstruction matches the paper’s explicit fermionic simplified-model Lagrangian in Eq. (1) and Eq. (2): the scalar/pseudoscalar \(Y_0\) couplings to Dirac dark matter and tops, the vector/axial \(Y_1\) couplings to Dirac dark matter and tops, and the special bottom axial coupling all have the correct field content, chirality, signs, and normalization. The main differences are that the reconstruction contains implementation-level extensions not present in the displayed paper model, especially real and complex scalar dark matter interactions and independent \(Y_0GG\), \(Y_0G\tilde G\) operators. The gluon operators are physically close in form to the paper’s Eq. (3), but their coefficient structure is not the same unless an external parameter mapping is imposed.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 19 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

