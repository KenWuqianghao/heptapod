# Graded disagreements — agent reconstruction vs. paper

Every model in this bundle passed the tool chain (FeynRules compile, Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import). That says the tools accept the model. It does not say the physics is right. To test the physics, a second fresh agent — which saw only the sanitized `.fr`, with no paper and no model name — reconstructed the Lagrangian in LaTeX. A third fresh agent then compared that reconstruction against the paper term by term and graded every difference.

This file collects those grades across all models. The grades come from the agent, not from a physicist. **They are the question list, not the answer.**

Grade meanings, as the cross-check agent used them:

- **convention** — the two forms are probably the same physics written differently (sign convention, field ordering, `N` vs `N^c`). Confirm the convention, then dismiss.
- **substantive** — a real difference in content. Read this one.
- **cosmetic** — presentation only.
- **unclassified** — the agent gave no grade this parser could read; treat as unreviewed.

## Counts

| grade | rows |
|---|---:|
| convention | 45 |
| substantive | 79 |
| cosmetic | 13 |
| unclassified | 0 |

Parsed from 21 cross-check reports.

## 4 models have no cross-check to report

These models are in the bundle with a `.fr` and a `REVIEW.pdf`, but the reverse check did not finish, so their review package holds no term-by-term comparison. The cause was agent-transport failure during the run, not a physics result. Treat them as **not yet reviewed**:

- `331`
- `B-L-SM`
- `CHEIDI`
- `VLC_LN`

## Convention disagreements (45)

### Chirality and projectors

- **MDMmodel** — Extra right-handed mixing \(T_R=P_R(-s_rt+c_rt')\)
  - *check:* A human should check whether this is an implementation-level diagonalization convention compatible with the paper’s approximations \(m_{t'}\gg m_t\) and \(\tan\theta_L\ll m_{t'}/m_t\).
- **Wprime** — Reconstruction default \(\zeta_{Wp}=0\) makes the default interaction purely right-handed, while the paper treats arbitrary left/right couplings and discusses both left- and right-handed cases.
  - *check:* Check whether parameter cards used for comparisons set \(\zeta\) and couplings to the desired paper scenario rather than relying on the default.

### Gauge, metric and derivative convention

- **ChernSimonsPortal** — Replacement of \(D\theta_X\) by \(X_\mu\)
  - *check:* A human should check whether the implementation is explicitly in unitary gauge or whether the Stückelberg/Goldstone mode was unintentionally omitted.
- **Sextets** — Electroweak gauge interactions are reconstructed but not part of the paper’s operative Lagrangian
  - *check:* A human should check whether any calculation uses photon or \(Z\) interactions, since the paper’s results are QCD-focused and do not validate those vertices.
- **pNG** — The reconstruction includes Goldstone fields in \(\Phi\), including a \(-iG^+\) convention, while the paper writes the decomposition in unitary gauge in eq. (2.8); a human should check the FeynRules gauge convention, but this does not change the physical scalar sector if Goldstones are removed.
  - *check:* a human should check the FeynRules gauge convention, but this does not change the physical scalar sector if Goldstones are removed.

### Hermitian conjugation and complex phases

- **368sextets** — Scalar operators are written with \(\Phi^\dagger\) and reordered barred spinors rather than the paper’s \(\Phi(q_R^c\sigma\ell_R)\)
- **ChernSimonsPortal** — Second gauge-covariant \(c_2\) operator differs in Higgs conjugation/order
- **DMsimp** — Complex scalar dark matter \(X_c\)
  - *check:* A human should check whether the implementation file was expected to include scalar-DM options beyond the paper’s explicit Lagrangian.
- **DMsimp** — Complex scalar vector-current coupling to \(Y_1\)
  - *check:* A human should check whether this is an implementation extension for scalar DM rather than a mismatch with the fermionic paper model.
- **EffLRSM** — Light-neutrino charged-current conjugation
  - *check:* a human should check the original implementation’s particle class and FeynRules conventions to see whether the field is actually the charge-conjugated light neutrino or whether the reconstruction normalized it away incorrectly.
- **HeavyN** — The reconstruction uses \(N_i\) directly, while Eq. (9) writes \(N^c\).
  - *check:* For Majorana heavy neutrinos this is usually equivalent, but check the implementation’s Majorana/self-conjugate declaration and fermion-flow conventions.
- **HiggsCharacterisation** — Charged spin-0 derivative \(W\) term uses the complex coefficient on the charge-conjugate structure relative to eq. (2.4).
  - *check:* Check the implementation’s definition of `kHdw`; it may be the complex conjugate of the paper’s \(\kappa_{H\partial W}\).
- **MDMmodel** — Extra Goldstone/full-doublet conventions
  - *check:* A human should check only that the \(-iG^+\) and \(+iG^0\) phase conventions are used consistently in the implementation’s gauge fixing and Feynman rules.
- **Monotops** — Real neutral scalar/vector assumptions
  - *check:* A human should check whether `SMET` and `VMET` are explicitly self-conjugate in the implementation, since the paper only identifies them as neutral invisible bosonic states.
- **pSPSS** — Real versus complex active-sterile mixings
  - *check:* A human should check the actual implementation parameter declarations: if `theta1`, `theta2`, and `theta3` are real, the reconstruction is faithful to the implementation, but it is narrower than the complex notation used in the paper’s analytic equations.

### Index, flavour and generation labels

- **Wprime** — Reconstruction implements Eq. (2)’s factorized left-right form, while Eq. (1) allows fully arbitrary \(C^{R,L}_{f_i f_j}\) couplings that can differ by sector and flavor.
  - *check:* Check whether the implementation is intended to reproduce the paper’s Eq. (2) benchmark parameterization or the maximally general Eq. (1) coupling freedom.

### Normalisation and numeric factors

- **ChernSimonsPortal** — Paper’s Stückelberg mass-sector normalization is not reconstructed
  - *check:* A human should check whether the vector kinetic and mass normalization in the implementation matches the paper’s \( -|F_X|^2/(4g_X^2)+M_X^2|D\theta_X|^2/2\).
- **ChernSimonsPortal** — Higgs hypercharge normalization differs in presentation
  - *check:* A human should check that the implementation’s \(Y_H=1/2\) convention is consistently mapped to the paper’s charge normalization where \(Q_Y(H)=1\) appears in the UV charge tables.
- **topBSM** — Reconstruction uses \(m_t/v\) normalization for unrelated scalar-top resonance couplings.
  - *check:* Check whether this normalization was copied from another simplified model and not from the EFT paper.

### Other

- **DMsimp** — Real scalar dark matter \(X_r\)
  - *check:* A human should check whether the review target is the paper’s displayed study model, which uses Dirac \(\chi\), or the broader implementation alluded to by the paper as allowing real scalar dark matter.
- **EffLRSM** — SM Lagrangian absent from reconstruction
  - *check:* a human should check whether the reconstruction was meant to cover the full UFO/model implementation or only the additional effective LRSM interaction file.
- **GeneralU1** — Higgs VEV from Eq. (3) is omitted.
  - *check:* Check whether electroweak symmetry breaking is handled by an external SM model file.
- **GeneralU1** — \(Z'\) mass relation uses \(v_\Phi=M_{Z'}/(2g_X)\), dropping the \(x_H^2v^2/4\) contribution in Eq. (4).
  - *check:* Check whether the implementation is explicitly working in the paper’s \(v_\Phi^2\gg v^2\), \(x_\Phi=1\) approximation.
- **GeneralU1** — Reconstruction lists fixed benchmark parameters such as \(g_X=0.1\), \(x_H=0\), and \(m_{\phi_X}=1000\).
  - *check:* Check whether these are harmless numerical defaults or whether they restrict scans that the paper treats as free parameters.
- **HiggsCharacterisation** — Reconstruction sums spin-0, spin-1, and spin-2 sectors into one \(\mathcal L_{\rm HCNP}\), whereas the paper writes \(\mathcal L_{\mathrm{HC},J}\) for a chosen \(J\) sector in eq. (2.1).
  - *check:* Check whether the implementation file intentionally contains all hypotheses simultaneously with couplings used as switches.
- **HiggsCharacterisation** — Reconstruction retains only \(t,b,\tau\) mass-trace pieces in spin-2 fermion terms.
  - *check:* Check whether light-fermion masses are intentionally neglected in the implementation, as is common phenomenologically.
- **MSSMD** — Scalar-sector mismatch: `h0`, `H0`, `A0`, `Hp` versus paper’s \(h_1,h_2,a_1\)
  - *check:* Check whether `A0` is intended to represent \(a_1\), or whether this is a generic MSSM scaffold unrelated to the paper’s NMSSM benchmark.
- **MSSMD** — Large extra MSSM-like spectrum in reconstruction
  - *check:* Check whether these fields are inherited boilerplate from an MSSM/FeynRules template and unused in the actual generated process.
- **Monotops** — \(L_{\rm SM}\) omission
  - *check:* A human should check whether `reconstruction.md` intentionally reconstructs only the BSM FeynRules interactions or whether the full model file should include/import the Standard Model Lagrangian.
- **Sextets** — Three separate sextet masses instead of one generic \(m_D\)
  - *check:* A human should check whether analyses using the implementation set these masses consistently when comparing to the paper’s single-diquark production formulas.
- **Top-Philic-Zprime** — Below-threshold width set to zero
  - *check:* A human should check whether the implementation is intended only for \(M_{V_1}>2m_t\), since the paper explicitly points to possible sub-threshold decays but does not use them in the TeV analysis.
- **Top-Philic-Zprime** — Default numerical values \(M_{V_1}=1.5\) TeV, \(c_t=2\), \(\theta=\pi/2\)
  - *check:* A human should check that these are treated as benchmark/default parameter-card values, not as fixed model definitions, because the paper scans \(M_{V_1}\) and \(c_t\).

### Overall sign / term ordering

- **368sextets** — Fermion operators are written as \(\bar\Psi\,\Gamma\,q_R^c\) rather than the paper’s \((q_R^c\Gamma\Psi)\)
  - *check:* A human should check the Dirac-charge-conjugation convention used by the implementation, especially signs for tensor bilinears.
- **368sextets** — Color tensor \(\mathcal C\) is not named \(J\) and is expressed through \(K\)-type tensors
- **HeavyN** — The charged-current and neutral-current heavy-neutrino terms have the opposite displayed overall sign from Eq. (9).
  - *check:* Check the FeynRules sign convention, field ordering, and whether a field or mixing-parameter phase redefinition makes the signs equivalent in generated vertices.
- **MDMmodel** — Missing Eq. (5) scalar-parameter relations
  - *check:* A human should check the implementation definitions of \(\mu_S^2,\mu_H^2,\lambda_H,\lambda_S,\kappa\) against the paper’s formulas, especially the sign and absolute-value conventions.
- **MSSMD** — Majorana assignment for \(n_1\) and \(n_D\)
  - *check:* Check the underlying dark SUSY model reference or implementation, since the paper calls them neutralinos but does not explicitly state the Majorana convention in the supplied text.
- **Monotops** — Extra electroweak quantum numbers
  - *check:* A human should check the implementation file’s actual class declarations to confirm whether \(SU(2)_L\) singlet and hypercharge assignments were explicit model choices or inferred by the reconstruction.
- **NJLComposite** — Mass-term sign relative to Eq. (1)
  - *check:* A human should check the paper’s metric/sign convention and the FeynRules scalar mass convention before treating this as a physical mismatch.
- **SMWeinberg** — Charged-current overall sign, Eqs. (8) and (23)
- **SMWeinberg** — Neutral-current overall sign, Eq. (24)
- **Sextets** — \(DD\) hypercharge sign mismatch: paper Table 1 lists \(Y=+2/3\), reconstruction uses \(Y=-2/3\)
- **Triplets** — Other electroweak assignments omitted: convention/substantive depending on scope.** Table 1 includes \(QQ\) triplet, \(DD\), and \(UU\) singlet possibilities, but the reconstruction only implements the \(SU(2)_L\)-singlet \(QQ/UD\) case; a human should check whether the implementation target was the full table or one benchmark row.
  - *check:* a human should check whether the implementation target was the full table or one benchmark row.
- **VLQ** — Overall signs in the reconstructed Yukawa and Dirac mass terms differ from the signs printed in Eqs. (11)-(12).
  - *check:* Check the implementation’s Lagrangian sign convention; this likely has no physical effect if used consistently.

### Symbol naming and parameter labels

- **MDMmodel** — Top-partner mass mapping \(M\leftrightarrow M_\Delta=M_{T'}c_l\)

## Substantive disagreements (79)

### Chirality and projectors

- **MDMmodel** — Missing \(q^u_{3L}\) left-handed mixing relation from Eq. (9)
  - *check:* A human should check whether the implementation rotates the SM top component consistently with \(q^u_{3L}=c_Lt_L+s_Lt'_L\), not only the heavy \(T_L\) component.
- **NJLComposite** — Neutrino chirality in the \(Y=1/6\) leptoquark interactions
  - *check:* A human should check the implementation file’s chiral projectors for the neutrino vertices against Table I and Eq. (3), since the paper uses \(\bar\nu_R q_L\) for the positive-charge \(Y=1/6\) constituents while the reconstruction reports \(\bar\nu_L q_L\).
- **Triplets** — `LUDL` flavor symmetry: substantive if the paper’s antitriplet antisymmetry is meant to apply to all flavor matrices.** The reconstruction gives diagonal right-chiral \(UD\) couplings, while the paper says antitriplet couplings must be antisymmetric in flavor; a human should check how the implementation defines flavor indices for \(U\)-\(D\) couplings and whether antisymmetry is required for non-identical up/down species.
  - *check:* a human should check how the implementation defines flavor indices for \(U\)-\(D\) couplings and whether antisymmetry is required for non-identical up/down species.
- **VLQ** — The fourth-generation fields are listed as Dirac fields with no \(SU(2)_L\) representation, while the paper’s Sec. 2.2 implies a sequential chiral fourth generation.
  - *check:* Check the original implementation’s class declarations and gauge quantum numbers, especially whether left- and right-handed components are represented separately elsewhere.
- **VLQ** — `L4Mass` uses explicit Dirac mass terms for fourth-generation fermions.
  - *check:* Check whether these are merely post-EWSB physical mass terms in a phenomenological implementation, or intended as gauge-invariant pre-EWSB Lagrangian terms; the latter would not match a chiral sequential fourth generation.
- **topBSM** — Missing \(O^{(3,1)}_{u\phi}\), Eq. (5).
  - *check:* Check whether the implementation supports both \(t\to uh/ch\) chiralities.

### Gauge, metric and derivative convention

- **HiggsCharacterisation** — Reconstruction’s photon energy-momentum tensor omits derivative terms shown explicitly in paper eq. (2.18).
  - *check:* Check whether the implementation uses a simplified transverse/on-shell tensor or includes the omitted terms elsewhere through gauge-fixing conventions.
- **NJLComposite** — Missing \(SU(2)_L\) doublet structure and charged-\(W\) interactions
  - *check:* A human should check whether the actual implementation intentionally broke the paper’s Eq. (2) doublet structure into electroweak-component singlets, because this changes gauge interactions involving \(W^\pm\).
- **Wprime** — Reconstruction includes an explicit \(W'\) kinetic/mass term with an EM-only covariant derivative, which the paper does not specify.
  - *check:* Check whether photon interactions of \(W'\) generated by the EM covariant derivative are intended and whether they are used in processes beyond the paper’s \(s\)-channel charged-current calculation.
- **pSPSS** — Missing LNLS charges
  - *check:* A human should check whether the reconstruction is intended to document only FeynRules gauge content or also the symmetry structure of the pSPSS, because Eq. (4.1) is central to why the allowed terms have the displayed form.

### Hermitian conjugation and complex phases

- **ChernSimonsPortal** — Broken \(XW^+W^-\) term lacks an explicit antisymmetrized or Hermitian-conjugate contribution
  - *check:* A human should check the generated Feynman rule and confirm whether it produces the paper’s \((k_2-k_1)\) momentum structure in Eq. (28).
- **GeneralU1** — Dirac neutrino Yukawa uses \(H^\dagger\) in the reconstruction instead of the Higgs contraction appearing in Eq. (1).
  - *check:* Check the original implementation’s \(SU(2)\), hypercharge, and \(U(1)_X\) conventions, because with Table I charges the reconstructed \(H^\dagger\) term is not gauge invariant for general \(x_H\).
- **GeneralU1** — SM Higgs potential terms \(-m_h^2H^\dagger H+\lambda(H^\dagger H)^2\) from Eq. (2) are absent.
  - *check:* Check whether the base SM Higgs sector is imported elsewhere in the implementation or accidentally omitted.
- **HeavyN** — The reconstruction treats \(V_{\alpha i}\) as real, while the paper writes \(V^*_{\ell N}\).
  - *check:* Check whether the implementation is restricted to real active-heavy mixing or whether complex phases are supported elsewhere but lost in the reconstruction.
- **Monotops** — Self-conjugate invisible fermion \(\chi\)
  - *check:* A human should check whether `FMET` is declared self-conjugate in the implementation, because the paper’s Eq. (1) does not require \(\chi\) to be Majorana-like.
- **Triplets** — Named scalar charge and representation: substantive.** The reconstruction names the fundamental scalar \(S\) as a color triplet with \(Y=Q=-1/3\), while the paper’s \(QQ/UD\) diquark in Table 1 has \(Y=+1/3\) and color \(\bar3\) or \(6\); a human should check whether the implementation intentionally defines \(S^\dagger\) as the paper’s produced diquark \(D\).
  - *check:* a human should check whether the implementation intentionally defines \(S^\dagger\) as the paper’s produced diquark \(D\).
- **Triplets** — Sextet omission: substantive.** The paper’s model parameterization covers both color antitriplet and sextet diquarks, but the reconstruction only contains the antitriplet/conjugate-triplet epsilon structure; a human should check whether the implementation was intended to reproduce only the antitriplet benchmark rather than the full paper.
  - *check:* a human should check whether the implementation was intended to reproduce only the antitriplet benchmark rather than the full paper.
- **Wprime** — Reconstruction includes three Dirac-type right-handed neutrino fields with explicit kinetic and mass terms, while the paper only uses \(m_{\nu_R}\) as a kinematic condition for \(W'_R\) leptonic decays.
  - *check:* Check whether the implementation’s Dirac, non-self-conjugate \(\nu_R\) choice matches the target phenomenology, especially if neutrino-sector mixing or Majorana assumptions matter.
- **topBSM** — Missing \(O^{(3,1)}_{uG}\), Eq. (4).
  - *check:* Check whether chirality-flipped or conjugate flavor structures were intentionally omitted.
- **topBSM** — Reconstruction lacks the paper’s Hermitian-conjugate FCNC structure.
  - *check:* Check whether both decay and conjugate amplitudes are generated in the implementation.

### Index, flavour and generation labels

- **HiggsCharacterisation** — Spin-2 fermion sector introduces a separate \(k_{q3}\) third-generation quark coupling and extra mass-trace pieces not present in the compact paper eq. (2.15).
  - *check:* Check whether the implementation extends the paper’s displayed \(\kappa_q,\kappa_\ell\) structure or whether the paper’s \(\sum_f\) notation was intended to allow generation-dependent \(\kappa_f\).
- **MSSMD** — Missing \(\epsilon\)-dependent lifetime/width relation
  - *check:* Check whether the dark photon lifetime was imposed at event-generation level rather than derived from the model file.
- **NJLComposite** — Flavor-mixed Yukawa terms of Eq. (4) absent from the reconstruction
  - *check:* A human should check whether Eq. (4) was intended as part of the implemented model or only as a phenomenological possibility, because the reconstruction contains only generation-aligned couplings without explicit mixing-matrix factors.
- **VLQ** — The reconstruction includes a full vector-like \(b'\) model (`LyBP`, `LDBP`, `LWBP`, `LZBP`) while the paper only briefly comments on an analogous down-type case after Eq. (16).
  - *check:* Check whether the implementation intentionally bundled the paper’s aside as an additional optional model, or whether the target paper model should only include the vector-like up-type \(t'\) and fourth-generation cases.
- **VLQ** — The reconstruction omits explicit fourth-generation Yukawa interactions.
  - *check:* Check whether the implementation only works in the mass basis for phenomenology, or whether a gauge-invariant Lagrangian reconstruction was expected.
- **topBSM** — Missing \(O^{(1,3)}_{uG}\), Eq. (2).
  - *check:* Check for any hidden flavor-changing top-light-quark chromomagnetic operator in the original implementation.
- **topBSM** — Missing \(utg\) dipole interaction Eq. (30).
  - *check:* Check whether the implementation contains a flavor-changing \(t-u/c-g\) dipole vertex rather than only gluon-fusion resonance operators.
- **topBSM** — Extra \(S1\) flavor-diagonal quark and lepton currents.
  - *check:* Check whether a \(Z'\)-like model was accidentally reconstructed instead of the paper’s EFT.

### Normalisation and numeric factors

- **368sextets** — All higher-dimensional operator coefficients lack explicit EFT cutoff powers
  - *check:* A human should check whether \(C_{Fu},C_{Fd},C_{FBu},C_{FBd},C_{Su},C_{Sd}\) are intended to be dimensionful Wilson coefficients already including \(1/\Lambda\), \(1/\Lambda^2\), or \(1/\Lambda^3\).
- **DMsimp** — Independent gluon contact operators
  - *check:* A human should check whether the implementation intentionally extends the paper model with free \(g^S_g/\Lambda\) and \(g^P_g/\Lambda\) operators, or whether these were meant to reproduce Eq. (3), in which case the coefficient mapping is missing.
- **DMsimp** — Eq. (3) coefficient mismatch
  - *check:* A human should check whether \(g^S_g/\Lambda\) and \(g^P_g/\Lambda\) are externally constrained to \(\alpha_s g^S_t/(12\pi v)\) and \(\alpha_s g^P_t/(8\pi v)\); without that mapping, the reconstruction describes a more general EFT than the paper’s top-EFT approximation.
- **VLQ** — `t4` and `b4` both have listed \(Y=+1/6\), and `n4`/`e4` both have listed \(Y=-1/2\), without separating left doublets from right singlets.
  - *check:* Verify whether the reconstruction confused doublet hypercharge with full Dirac-field hypercharge, since right-handed fourth-generation singlets need different hypercharges.
- **topBSM** — Missing physical rotated \(tuh\) coupling Eq. (11).
  - *check:* Check whether the implementation uses the correct factor \(2y_t/\sqrt2\), not the pre-rotation factor \(3y_t/\sqrt2\).
- **topBSM** — Missing \(\mathcal L_{tu}+\mathcal L_{tuh}\) counterterm structure Eqs. (25)-(27).
  - *check:* Check whether NLO renormalization was implemented at all.
- **topBSM** — Missing EOM-vanishing counterterms Eqs. (33)-(34).
  - *check:* Check whether the implementation is intended only for tree level or includes the NLO operator-renormalization setup.
- **topBSM** — Missing renormalized Lagrangian Eq. (37).
  - *check:* Check whether Wilson-coefficient mixing \(C_{uG}\to C_{u\phi}\) is encoded elsewhere.

### Other

- **ChernSimonsPortal** — UV heavy fermion sector is absent
- **ChernSimonsPortal** — Heavy scalar \(\Phi\) and UV Yukawa terms are absent
  - *check:* A human should check whether the implementation intentionally integrates out \(\Phi\) and the heavy fermions, leaving only Eq. (5), or whether these fields were expected to be present.
- **GeneralU1** — SM quark and charged-lepton Yukawa terms from Eq. (1) are absent.
  - *check:* Check whether the implementation intentionally reconstructed only BSM additions or was meant to encode the full minimal \(U(1)_X\) Lagrangian.
- **HeavyN** — The paper specializes to one heavy mass eigenstate \(N\), while the reconstruction contains three \(N_i\).
  - *check:* Check whether `sanitized.fr` intentionally implements a three-state generalization of the public model file, or whether the paper comparison should be restricted to a single selected state such as `n2`.
- **HeavyN** — The reconstruction omits the explicit light-neutrino \(U_{\ell m}\) charged- and neutral-current terms from Eq. (9).
  - *check:* Check whether these terms are supplied by the imported SM/FeynRules base model or whether the implementation drops PMNS-rotated light-neutrino interactions.
- **HeavyN** — The reconstruction gives explicit masses and widths for three heavy states, while the paper discusses results as functions of a single \(m_N\).
  - *check:* Check whether the benchmark masses and widths are implementation defaults rather than part of the paper’s analytical model definition.
- **HiggsCharacterisation** — Reconstruction omits the SM-like spin-0 \(X_0ZZ\) and \(X_0W^+W^-\) mass terms proportional to \(c_\alpha\kappa_{\rm SM}\) in eq. (2.4).
  - *check:* Check whether those terms are present elsewhere in the implementation or whether `kSM` being unused is an extraction/reconstruction error.
- **HiggsCharacterisation** — Reconstruction’s fermion energy-momentum tensor differs from the explicit paper tensor in eq. (2.17), especially in \(g_{\mu\nu}\), mass, and total-derivative terms.
  - *check:* Check the exact FeynRules definition of `Tfermion` and whether equations of motion or on-shell simplifications were applied in the reconstruction.
- **LeptoQuark** — Missing \(U_1\) mass term
  - *check:* A human should check whether the implementation supplies the vector mass solely through particle declarations in a way that FeynRules/UFO treats equivalently, or whether the Lagrangian object itself is incomplete.
- **LeptoQuark** — Missing \(Z'\) kinetic term
  - *check:* A human should check whether a separate `LZpKin` exists outside the reconstructed `LLeptoQuark` sum or whether the reconstruction/implementation accidentally omits the propagating \(Z'\) kinetic term.
- **LeptoQuark** — Missing \(Z'\) mass term
  - *check:* A human should check whether the \(Z'\) mass is generated from particle metadata only, or whether the Lagrangian used for model export lacks the paper’s \(\frac12M_{Z'}^2Z'_\mu Z'^\mu\) term.
- **MDMmodel** — Missing full \(L_{\rm SM}\) content
  - *check:* A human should check whether the implementation intentionally imports the SM Lagrangian elsewhere, since the reconstruction itself only shows the BSM/Higgs-sector subset.
- **MSSMD** — Kinetic mixing replaced by direct muon coupling
  - *check:* Check whether `gd` was intended as an effective \(\epsilon e Q_\mu\) coupling after diagonalizing kinetic mixing, or whether the implementation incorrectly omitted photon/dark-photon mixing.
- **MSSMD** — Same `gd` used for dark-sector transition and muon coupling
  - *check:* Check the original implementation or model card to see whether two physically distinct couplings were collapsed into one parameter.
- **MSSMD** — Missing Higgs decay \(h\to2n_1\)
  - *check:* Check whether production and Higgs decay were intentionally handled externally by BRIDGE/Pythia rather than encoded in the FeynRules model.
- **MSSMD** — Missing NMSSM \(h_{1,2}\to2a_1\), \(a_1\to\mu^+\mu^-\) interactions
  - *check:* Check whether the reconstruction is only for the dark SUSY benchmark and not meant to cover the NMSSM benchmark also discussed in the paper.
- **Monotops** — Default mass values versus paper scenarios
  - *check:* A human should check whether the reconstruction is reporting arbitrary implementation defaults or the benchmark masses used for the paper’s five scenarios.
- **Sextets** — Missing antitriplet branch
  - *check:* A human should check whether the implementation was intended to reproduce the full paper parameterization or only the sextet specialization used in parts of the numerical study.
- **Sextets** — Universal default Yukawa values in reconstruction are broader than Eq. (2.2)
  - *check:* A human should check whether the implementation defaults were chosen merely as placeholders or are being interpreted as paper-derived constraints.
- **Sextets** — Higgs-portal and sextet scalar quartic potential terms are extra
  - *check:* A human should check whether these potential terms came from an implementation extension rather than from the paper.
- **Triplets** — Scalar potential terms: substantive relative to the paper text, likely harmless for production.** The reconstruction includes Higgs-portal and scalar self-quartic interactions not specified in the paper; a human should check whether these are implementation conveniences/default scalar potential terms or intended claims about the paper’s model.
  - *check:* a human should check whether these are implementation conveniences/default scalar potential terms or intended claims about the paper’s model.
- **Wprime** — Reconstruction declares a fixed \(W'\) width `WWp = 1.`, whereas the paper computes total widths from the coupling-dependent partial widths in Sec. II.
  - *check:* Check whether the width is recalculated elsewhere at runtime; if not, the implementation will not reproduce the paper’s width and branching-ratio predictions.
- **pNG** — The reconstruction does not include the full \(\mathcal L_{\rm SM}\) from eq. (2.1); a human should check whether the implementation file intentionally imports the SM separately or whether the reconstruction is incomplete.
  - *check:* a human should check whether the implementation file intentionally imports the SM separately or whether the reconstruction is incomplete.
- **pNG** — The reconstruction presents \(v_s=300\), \(\theta=0.7854\), \(M_{h_2}=300\), and \(m_X=100\) as table values, while the paper defines \(\{m_\chi,v_s,\theta,m_H\}\) as free parameters in eq. (2.17); a human should check whether these are merely default benchmark values in the implementation.
  - *check:* a human should check whether these are merely default benchmark values in the implementation.
- **pNG** — The reconstruction’s field table omits the SM-like Higgs mass eigenstate \(h\), even though \(h\) appears in the reconstructed field decompositions; a human should check whether the reconstruction table was intended to list only BSM/new classes or all scalar mass eigenstates.
  - *check:* a human should check whether the reconstruction table was intended to list only BSM/new classes or all scalar mass eigenstates.
- **pNG** — SM Yukawa interactions and the resulting \(h/H\)-fermion couplings in Appendix A, eqs. (A.7)-(A.8), are absent from the reconstruction; a human should check whether those are supplied by an external SM model file.
  - *check:* a human should check whether those are supplied by an external SM model file.
- **pSPSS** — Displayed total Lagrangian omits the SM-with-mixed-neutrinos part
  - *check:* A human should check whether `LTot` in the reconstruction is meant to be only the new-physics addition or the full `LpSPSS`; the paper’s Section 5.1 says the SM fermion Lagrangian is modified by replacing \(\nu\) with `UnCL nL`.
- **topBSM** — Reconstruction introduces \(S0,O0,S1,O1,S2\) resonance fields absent from the paper.
  - *check:* Check whether `reconstruction.md` came from a different model file than the paper, possibly a generic resonance implementation.
- **topBSM** — Paper’s EFT master Lagrangian Eq. (1) is not reproduced.
  - *check:* Verify whether the implementation was supposed to encode the paper’s dimension-six EFT or a separate phenomenological model.
- **topBSM** — Missing paper’s tree-level \(tuh\) interaction Eq. (8).
  - *check:* Check generated Feynman rules for a \(t-u/c-h\) vertex.
- **topBSM** — Missing field rotations Eqs. (9)-(10).
  - *check:* Check whether mass diagonalization or equivalent counterterms are implemented.
- **topBSM** — Missing counterterm-subtracted \(O_{u\phi}\) form Eq. (12).
  - *check:* Check whether vev-induced \(u_L-t_R\) mixing is removed consistently.
- **topBSM** — Extra \(S0\bar tt\), \(S0GG\), and \(S0G\tilde G\) terms.
  - *check:* Check whether the source implementation is for a scalar resonance model, not this FCNC Higgs EFT paper.
- **topBSM** — Extra \(O0\bar tT^at\), \(O0GG\), and \(O0G\tilde G\) terms.
  - *check:* Check whether color-octet scalar resonance interactions belong to another paper or benchmark.
- **topBSM** — Extra \(O1\) color-octet vector quark currents.
  - *check:* Check whether an axigluon/coloron model was mixed into the reconstruction.
- **topBSM** — Extra inert spin-2 field \(S2\).
  - *check:* Check whether the implementation file contains unused benchmark particles unrelated to the paper.

### Overall sign / term ordering

- **368sextets** — Missing scalar and fermion lepton numbers
  - *check:* A human should check whether the implementation tracks the accidental lepton-number assignments in Table X or intentionally omits them because they do not affect generated vertices.
- **HiggsCharacterisation** — Spin-1 \(W1\) term has the opposite sign relative to eq. (2.11) if \(k_{w1}=\kappa_{W1}\).
  - *check:* Check the charged-\(W\) field naming and sign convention in the implementation, including the definition of \(W^\pm_{\mu\nu}\).
- **HiggsCharacterisation** — Spin-1 \(W2\) term has the opposite sign relative to eq. (2.11) because the charged fields carry swapped Lorentz indices contracted with antisymmetric \(X_1^{\mu\nu}\).
  - *check:* Check whether the implementation defines `kw2` with an implicit minus sign relative to the paper.
- **HiggsCharacterisation** — Spin-1 \(W4\) term has the opposite sign relative to eq. (2.11) for the same antisymmetric-index reason as \(W2\).
  - *check:* Check whether the implementation defines `kw4` with an implicit minus sign relative to the paper.
- **LeptoQuark** — Missing \(G'\) mass term
  - *check:* A human should check whether the coloron mass is included elsewhere in the implementation or only assigned as a particle property.
- **Sextets** — Missing \(SU(2)_L\) triplet \(QQ\) electroweak option
  - *check:* A human should check whether Table 1 is meant as required model content for this implementation or only a catalogue of possible diquark assignments.

### Symbol naming and parameter labels

- **topBSM** — Missing \(O^{(1,3)}_{u\phi}\), Eq. (3).
  - *check:* Check whether the implementation contains a \(tuh\) FCNC Yukawa vertex under another name.

## Cosmetic disagreements (13)

### Gauge, metric and derivative convention

- **GeneralU1** — Reconstruction includes explicit \(G_{Z'}\) and unphysical \(\Phi_X\) fields not shown in the paper’s Eq. (3).
  - *check:* Check the gauge choice in the implementation; this is likely just an implementation-basis detail.

### Index, flavour and generation labels

- **Top-Philic-Zprime** — Extra Proca kinetic/mass term
  - *check:* A human should check whether the review target is the paper’s displayed interaction-only Lagrangian or the full FeynRules implementation, because the extra term is standard and physically expected for event generation.

### Other

- **368sextets** — Implementation default masses \(500\) appear in the reconstruction
  - *check:* A human should check whether these are merely UFO/FeynRules benchmark defaults rather than claims about the paper’s physical model.
- **ChernSimonsPortal** — Implementation benchmark values \(c_1=c_2=0.001\), \(M_X=1.0\), width \(=1.0\) are not paper definitions
  - *check:* A human should check whether these are harmless simulation defaults rather than claimed physical predictions from the paper.
- **DMsimp** — Default masses and widths
  - *check:* A human should check whether the reconstruction is reporting UFO/FeynRules default parameter values, because the paper’s physical benchmarks use different mass and width choices.
- **GeneralU1** — Full SM field representation table from Table I is not reproduced.
  - *check:* Check whether the reconstruction was intended to document only new fields and derived \(U(1)_X\) charges rather than the full model content.
- **LeptoQuark** — Implementation-only unphysical alias `U` for `VLQ`
  - *check:* A human should check that the alias is not exported as an additional physical vector state.
- **Top-Philic-Zprime** — Contact operator Eq. (2.3) absent
  - *check:* A human should check whether the reconstruction is meant to include derived EFT limits; it is not necessary for reproducing the simplified model Lagrangian Eq. (2.1).
- **VLQ** — The reconstruction’s vector-like top charged current omits unchanged \(u,c\) SM charged currents from Eq. (7).
  - *check:* Check whether the reconstruction is intentionally listing only modified/new interactions rather than the full SM charged-current Lagrangian.
- **pNG** — The reconstruction uses \(h_2\) and \(X\), while the paper uses \(H\) and \(\chi\); a human should confirm that all downstream files consistently identify \(h_2\equiv H\) and \(X\equiv\chi\).

### Overall sign / term ordering

- **HeavyN** — The Goldstone terms are reconstructed explicitly, but the paper only states that Goldstone couplings are included in Feynman gauge.
  - *check:* Check the actual model file or generated Feynman rules if an exact sign-level validation of Goldstone vertices is required.
- **LeptoQuark** — Implementation-only lepton-number assignment for `VLQ`
  - *check:* A human should check that this bookkeeping charge does not enforce unintended selection rules or conflict with the intended \(U_1\) interactions.

### Symbol naming and parameter labels

- **Monotops** — Notation swap \(V/X\)
  - *check:* A human should check any downstream comparison carefully because the reconstruction uses \(X_\mu\) for the paper’s neutral vector \(V_\mu\), and \(V_\mu^a\) for the paper’s colored vector \(X_{\mu,i}\).

## Per-model row counts

| model | convention | substantive | cosmetic | unclassified |
|---|---:|---:|---:|---:|
| 368sextets | 3 | 2 | 1 | 0 |
| ChernSimonsPortal | 4 | 3 | 1 | 0 |
| DMsimp | 3 | 2 | 1 | 0 |
| EffLRSM | 2 | 0 | 0 | 0 |
| GeneralU1 | 3 | 3 | 2 | 0 |
| HeavyN | 2 | 4 | 1 | 0 |
| HiggsCharacterisation | 3 | 7 | 0 | 0 |
| LeptoQuark | 0 | 4 | 2 | 0 |
| MDMmodel | 4 | 2 | 0 | 0 |
| MSSMD | 3 | 5 | 0 | 0 |
| Monotops | 3 | 2 | 1 | 0 |
| NJLComposite | 1 | 3 | 0 | 0 |
| SMWeinberg | 2 | 0 | 0 | 0 |
| Sextets | 3 | 4 | 0 | 0 |
| Top-Philic-Zprime | 2 | 0 | 2 | 0 |
| Triplets | 1 | 4 | 0 | 0 |
| VLQ | 1 | 5 | 1 | 0 |
| Wprime | 2 | 3 | 0 | 0 |
| pNG | 1 | 4 | 1 | 0 |
| pSPSS | 1 | 2 | 0 | 0 |
| topBSM | 1 | 20 | 0 | 0 |
