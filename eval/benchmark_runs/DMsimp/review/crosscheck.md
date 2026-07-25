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