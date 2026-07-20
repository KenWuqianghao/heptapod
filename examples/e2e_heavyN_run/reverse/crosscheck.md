# Comparison of `reconstruction.md` Against the Paper Model

## Located Paper Definitions

The paper defines the heavy-neutrino model in **Section II, “Heavy Neutrino Model”**. The relevant definitions are:

- **Neutrino mixing / field content:** Section II, first displayed `eqnarray`, approximately **Eq. (7)**:
  \[
  \begin{pmatrix} \nu_{Li} \\ N_{Rj}^c \end{pmatrix}
  =
  \begin{pmatrix}
  U_{3\times3} && V_{3\times n} \\
  X_{n\times3} && Y_{n\times n}
  \end{pmatrix}
  \begin{pmatrix} \nu_m \\ N_{m'}^c \end{pmatrix}.
  \]
- **Flavor-state expansion:** Section II, next displayed equation, approximately **Eq. (8)**:
  \[
  \nu_\ell=\sum_{m=1}^3 U_{\ell m}\nu_m+\sum_{m'=1}^n V_{\ell m'}N_{m'}^c.
  \]
- **One-heavy-state simplification:** Section II immediately before the interaction Lagrangian: “For simplicity, we consider only one heavy mass eigenstate, labeled by \(N\).”
- **Interaction Lagrangian:** Section II, labeled `\label{eq:Lagrangian}`, approximately **Eq. (9)**.
- **Goldstone implementation:** Section III, “Computational Setup”: “We implement the above Lagrangian with Goldstone boson couplings in the Feynman gauge into FeynRules...”

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Heavy state \(N\) from one-heavy-mass-eigenstate simplification after Eq. (8), with mixing inherited from RH heavy states \(N_R^c\) in Eq. (7) | One self-conjugate Majorana fermion \(N_1\), SM gauge singlet | agree | The paper does not spell out gauge representations in a table, but the RH sterile-neutrino origin implies an SM singlet. Majorana/self-conjugate treatment is consistent with the use of \(N^c\) and the heavy-neutrino phenomenology, though the word “Majorana” is not explicit in the extracted text. |
| Full mixing rotation with \(U,V,X,Y\), Eq. (7) | Only \(V_{eN_1},V_{\mu N_1},V_{\tau N_1}\) parameters reconstructed | missing-in-reconstruction | The reconstruction captures the active-heavy \(V_{\ell N}\) coefficients relevant to the BSM interactions, but not the full neutrino rotation matrix or \(X,Y\) blocks. |
| Flavor state \(\nu_\ell=\sum_m U_{\ell m}\nu_m+\sum_{m'}V_{\ell m'}N_{m'}^c\), Eq. (8) | Effective flavor-dependent couplings \(V_{\ell N_1}\) to \(N_1\) | agree | For the one-heavy-state truncation, the reconstruction captures the active-heavy part. It omits the light-neutrino \(U_{\ell m}\nu_m\) piece. |
| SM light-neutrino charged current: \(-\frac{g}{\sqrt2}W^+_\mu\sum_{\ell,m}\bar\nu_m U_{\ell m}^*\gamma^\mu P_L\ell^-\), Eq. (9), first line | No corresponding term in reconstructed BSM Lagrangian | missing-in-reconstruction | Likely supplied by the base SM model rather than the sanitized BSM extension, but it is present in the paper’s displayed interaction Lagrangian. |
| Heavy charged current: \(-\frac{g}{\sqrt2}W^+_\mu\sum_{\ell=e}^{\tau}\overline{N^c}V_{\ell N}^*\gamma^\mu P_L\ell^-+\mathrm{H.c.}\), Eq. (9), second line | \(+\frac{g_N}{\sqrt2}\sum_\ell V_{\ell N_1}\bar N_1\gamma^\mu P_L\ell\,W^+_\mu+\mathrm{h.c.}\) | disagree | Field content, chirality, \(W^+\), and \(1/\sqrt2\) coefficient agree. Differences: paper has an overall minus sign and complex-conjugated \(V_{\ell N}^*\); reconstruction uses positive sign and real \(V_{\ell N_1}\). |
| SM light-neutrino neutral current: \(-\frac{g}{2c_W}Z_\mu\sum_{\ell,m}\bar\nu_mU_{\ell m}^*\gamma^\mu P_L\nu_\ell\), Eq. (9), third line | No corresponding term in reconstructed BSM Lagrangian | missing-in-reconstruction | Again likely part of the base SM/light-neutrino sector rather than the BSM addition, but it is present in the paper’s Eq. (9). |
| Heavy neutral current: \(-\frac{g}{2c_W}Z_\mu\sum_{\ell=e}^{\tau}\overline{N^c}V_{\ell N}^*\gamma^\mu P_L\nu_\ell+\mathrm{H.c.}\), Eq. (9), fourth line | \(+\frac{g_N}{2c_W}\sum_\ell V_{\ell N_1}\bar N_1\gamma^\mu P_L\nu_\ell Z_\mu+\mathrm{h.c.}\) | disagree | The \(Z\), \(P_L\), \(1/(2c_W)\), and flavor structure agree. Differences are the same as for the charged current: sign and complex conjugation/reality of \(V\). |
| Heavy Higgs interaction: \(-\frac{gm_N}{2M_W}h\sum_{\ell=e}^{\tau}\overline{N^c}V_{\ell N}^*P_L\nu_\ell+\mathrm{H.c.}\), Eq. (9), fifth line | \(-\frac{g_Nm_{N_1}}{2M_W}\sum_\ell V_{\ell N_1}\bar N_1P_L\nu_\ell H+\mathrm{h.c.}\) | agree | Coefficient, sign, chirality, Higgs coupling, and mass proportionality agree if \(N_1\) is identified with \(N^c\) up to Majorana convention and the reconstruction’s real \(V_{\ell N_1}\) is treated as the paper’s \(V_{\ell N}^*\) in a real benchmark. |
| Goldstone couplings in Feynman gauge, Section III | `LNGbare` and `LNG`: neutral \(G^0\) and charged \(G^\pm\) mass-proportional couplings with h.c. | agree | The paper states that Goldstone couplings are implemented but does not print their explicit form. The reconstruction’s mass-proportional Feynman-gauge Goldstone structure is consistent with the displayed \(W/Z/h\) interactions, but exact signs and \(i\) conventions cannot be verified directly from the paper text. |
| Heavy-neutrino free kinetic and mass terms | `LNKin`: \(\frac{i}{2}\bar N_1\gamma^\mu\partial_\mu N_1-\frac12m_{N_1}\bar N_1N_1\) | extra-in-reconstruction | The paper’s displayed Eq. (9) is explicitly the interaction Lagrangian with EW bosons; it does not print the free kinetic/mass term. The term is standard for a Majorana mass eigenstate and not in tension with the paper. |
| Coupling normalization \(g\), \(c_W=\cos\theta_W\), SM inputs Eq. (10) | \(g_N=e/s_W\), \(c_W\), \(M_W\) | agree | \(g_N=e/s_W\) is the standard weak coupling \(g\). The reconstruction’s normalization matches the paper’s interaction coefficients. |
| Flavor-mixing parameters \(V_{\ell N}\), constrained and cross sections scaling as \(|V_{\ell N}|^2\), Section II after Eq. (9) | Real external parameters with defaults \(V_{eN_1}=1\), \(V_{\mu N_1}=0\), \(V_{\tau N_1}=0\) | disagree | The paper treats \(V_{\ell N}\) as generally model-dependent and uses \(|V_{\ell N}|^2\). The reconstruction restricts them to real values and includes benchmark defaults; this is implementation-specific and narrower than the paper’s general parameterization. |

## Disagreements and Checks

- **Heavy charged-current sign and conjugation** — severity: **convention**. A human should check the FeynRules sign conventions and whether the UFO vertices use an overall interaction-sign convention opposite to the paper’s displayed Lagrangian.
- **Heavy neutral-current sign and conjugation** — severity: **convention**. A human should check whether \(V_{\ell N_1}\) is defined as the real value of \(V_{\ell N}^*\), and whether the sign is absorbed by field or Lagrangian conventions.
- **Real-only mixing parameters versus complex \(V_{\ell N}\)** — severity: **substantive**. A human should check whether the implementation intentionally supports only real active-heavy mixing, since complex phases would matter for CP-sensitive observables.
- **Missing full \(U,V,X,Y\) mixing rotation** — severity: **cosmetic** for the heavy-neutrino production model, **substantive** for a full neutrino-sector implementation. A human should check whether the implementation is meant only as a phenomenological one-heavy-state model rather than a complete seesaw mass model.
- **Missing SM light-neutrino charged and neutral currents** — severity: **cosmetic** if inherited from a base SM model, **substantive** if this reconstruction is supposed to describe the complete paper Lagrangian. A human should verify whether those interactions are supplied elsewhere in the model stack.
- **Extra explicit Majorana kinetic/mass term** — severity: **cosmetic**. A human should check only that the implementation’s \(m_{N_1}\) corresponds to the paper’s \(m_N\) and that the Majorana normalization is handled consistently.
- **Goldstone coefficient details not printed in the paper** — severity: **convention**. A human should compare directly against the original FeynRules file or generated UFO rules if exact \(i\), charge-conjugation, and Goldstone sign conventions matter.

Overall, the reconstruction captures the central BSM physics of the paper: a single heavy neutral lepton coupled to SM leptons through active-heavy mixing, with the expected \(W\), \(Z\), Higgs, and Feynman-gauge Goldstone interactions and the correct weak-coupling and mass-proportional coefficient structures. The main gaps are that the reconstruction is narrower than the paper’s formal neutrino mixing setup, omits the light-neutrino SM pieces shown in the paper’s Eq. (9), and treats the active-heavy mixings as real benchmark parameters. The only direct term-level mismatches in the heavy interaction terms are the overall signs and complex conjugation of \(V_{\ell N}\) in the charged- and neutral-current interactions, which are likely convention-dependent but should be checked against the actual FeynRules/UFO vertex conventions.