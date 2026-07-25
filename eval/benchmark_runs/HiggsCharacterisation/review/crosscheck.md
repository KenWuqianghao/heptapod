# Comparison of `reconstruction.md` Against the Paper Model

## Paper Locations

The model is defined in **Section 2, “Effective lagrangian”**. The paper states
\[
\mathcal L_{\mathrm{HC},J}=\mathcal L_{\mathrm{SM}-H}+\mathcal L_J
\]
in **eq. (2.1)**, where \(\mathcal L_J\) contains the kinetic and interaction terms of the new bosonic state \(X(J^P)\).

Relevant definitions:

- **Spin/parity content:** Section 2, before eq. (2.1): \(J^P=0^+,0^-,1^+,1^-,2^+\).
- **Spin-0 fermion Lagrangian:** **eq. (2.2)**, with \(c_\alpha,s_\alpha\) defined in **eq. (2.3)**.
- **Spin-0 vector Lagrangian:** **eq. (2.4)**.
- **Field strengths and duals:** **eqs. (2.5)-(2.7)**.
- **Spin-1 fermion Lagrangian:** **eq. (2.8)**; quark vector/axial coefficients in **eqs. (2.9)-(2.10)**, with analogous lepton coefficients stated in prose.
- **Spin-1 \(WW\) Lagrangian:** **eq. (2.11)**.
- **Spin-1 \(ZZ\) Lagrangian:** **eq. (2.12)**.
- **Spin-1 parity restrictions:** **eqs. (2.13)-(2.14)**.
- **Spin-2 fermion Lagrangian:** **eq. (2.15)**.
- **Spin-2 vector Lagrangian:** **eq. (2.16)**.
- **Explicit QED fermion/photon energy-momentum tensors:** **eqs. (2.17)-(2.18)**.
- **Universal RS-like spin-2 limit:** **eq. (2.19)**.
- **Non-universal spin-2 quark/gluon example:** **Section 4.1, eq. (4.1)**.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| \(\mathcal L_{\mathrm{HC},J}=\mathcal L_{\mathrm{SM}-H}+\mathcal L_J\), one chosen \(J\) sector, eq. (2.1) | \(\mathcal L_{\rm HCNP}=\mathcal L_{0f}+\mathcal L_{0v}+\mathcal L_1+\mathcal L_{2f}+\mathcal L_{2v}\) | disagree | The paper presents a model for a new state \(X(J^P)\) with a chosen spin/parity sector; the reconstruction sums spin-0, spin-1, and spin-2 sectors simultaneously. This may reflect implementation packaging, but it is not how eq. (2.1) is written. |
| New bosonic state \(X(J^P)\), \(J^P=0^+,0^-,1^+,1^-,2^+\), Section 2 | Separate \(X_0,X_{1\mu},X_{2\mu\nu}\) fields | agree | Physics content matches the spin assignments, though the paper phrases this as alternative hypotheses rather than necessarily simultaneous particles. |
| Below-EWSB physical-field EFT; no required \(SU(2)_L\times U(1)_Y\) assignment for spin-1, Section 2.2 | \(X_0,X_1,X_2\) listed as neutral color/electroweak singlets | agree | For spin-2 the paper explicitly says color, weak, and electromagnetic singlet before eq. (2.15). For spin-1 the paper explicitly avoids specifying EW representation; neutral physical \(X_1\) is consistent with the written \(ZZ/WW\) interactions. |
| Spin-0 Yukawa: \(-\sum_{f=t,b,\tau}\bar\psi_f(c_\alpha\kappa_{Hff}g_{Hff}+is_\alpha\kappa_{Aff}g_{Aff}\gamma_5)\psi_fX_0\), eq. (2.2) | \(-X_0c_\alpha[k_{Htt}m_t/v\,\bar tt+k_{Hbb}m_b/v\,\bar bb+k_{H\ell\ell}m_\tau/v\,\bar\tau\tau]\) plus \(-iX_0s_\alpha[\cdots\bar f\gamma^5f]\) | agree | Same third-generation scalar and pseudoscalar Yukawa structures, with \(g_{Hff}=g_{Aff}=m_f/v\). |
| \(c_\alpha=\cos\alpha,\ s_\alpha=\sin\alpha\), eq. (2.3) | \(c_\alpha=\texttt{ca},\ s_\alpha=\sqrt{1-c_\alpha^2}\) | agree | Equivalent only if the implementation restricts to the principal positive \(s_\alpha\). The paper treats \(s_\alpha\) as \(\sin\alpha\). |
| SM-like spin-0 vector mass terms \(c_\alpha\kappa_{\rm SM}[\frac12 g_{HZZ}Z_\mu Z^\mu+g_{HWW}W^+_\mu W^{-\mu}]X_0\), eq. (2.4) | `kSM` declared but “unused”; no \(X_0ZZ\) or \(X_0W^+W^-\) mass term listed | missing-in-reconstruction | This is a central term in eq. (2.4), needed to recover the SM limit with \(c_\alpha=1,\kappa_{\rm SM}=1\). |
| \(-\frac14[c_\alpha\kappa_{H\gamma\gamma}g_{H\gamma\gamma}A_{\mu\nu}A^{\mu\nu}+s_\alpha\kappa_{A\gamma\gamma}g_{A\gamma\gamma}A_{\mu\nu}\tilde A^{\mu\nu}]X_0\), eq. (2.4) | \(-\frac14X_0c_\alpha k_{Haa}g_{Haa}F^AF^A\), \(-\frac14X_0s_\alpha k_{Aaa}g_{Aaa}F^A\tilde F^A\) | agree | Same CP-even and CP-odd \(\gamma\gamma\) structures. |
| \(-\frac12[c_\alpha\kappa_{HZ\gamma}g_{HZ\gamma}Z_{\mu\nu}A^{\mu\nu}+s_\alpha\kappa_{AZ\gamma}g_{AZ\gamma}Z_{\mu\nu}\tilde A^{\mu\nu}]X_0\), eq. (2.4) | \(-\frac12X_0c_\alpha k_{Hza}g_{Hza}F^ZF^A\), \(-\frac12X_0s_\alpha k_{Aza}g_{Aza}F^Z\tilde F^A\) | agree | Same \(Z\gamma\) field-strength structures. |
| \(-\frac14[c_\alpha\kappa_{Hgg}g_{Hgg}G^a_{\mu\nu}G^{a\mu\nu}+s_\alpha\kappa_{Agg}g_{Agg}G^a_{\mu\nu}\tilde G^{a\mu\nu}]X_0\), eq. (2.4) | \(-\frac14X_0c_\alpha k_{Hgg}g_{Hgg}GG\), \(-\frac14X_0s_\alpha k_{Agg}g_{Agg}G\tilde G\) | agree | Same gluonic CP-even and CP-odd structures. |
| \(-\frac1{4\Lambda}[c_\alpha\kappa_{HZZ}Z_{\mu\nu}Z^{\mu\nu}+s_\alpha\kappa_{AZZ}Z_{\mu\nu}\tilde Z^{\mu\nu}]X_0\), eq. (2.4) | \(-\frac1{4\Lambda}X_0c_\alpha k_{Hzz}F^ZF^Z\), \(-\frac1{4\Lambda}X_0s_\alpha k_{Azz}F^Z\tilde F^Z\) | agree | Same higher-dimensional \(ZZ\) field-strength terms. |
| \(-\frac1{2\Lambda}[c_\alpha\kappa_{HWW}W^+_{\mu\nu}W^{-\mu\nu}+s_\alpha\kappa_{AWW}W^+_{\mu\nu}\tilde W^{-\mu\nu}]X_0\), eq. (2.4) | \(-\frac1{2\Lambda}X_0c_\alpha k_{Hww}F^{W^-}F^{W^+}\), \(-\frac1{2\Lambda}X_0s_\alpha k_{Aww}F^{W^-}\tilde F^{W^+}\) | agree | Same \(W^+W^-\) field-strength content; charge ordering is immaterial for these bilinears. |
| \(-\frac{c_\alpha}{\Lambda}[\kappa_{H\partial\gamma}Z_\nu\partial_\mu A^{\mu\nu}+\kappa_{H\partial Z}Z_\nu\partial_\mu Z^{\mu\nu}+\kappa_{H\partial W}W^+_\nu\partial_\mu W^{-\mu\nu}+\mathrm{h.c.}]X_0\), eq. (2.4) | \(-\frac{c_\alpha}{\Lambda}X_0[k_{Hda}Z_\nu\partial F_A+k_{Hdz}Z_\nu\partial F_Z+k_{Hdw}W^-_\nu\partial F_{W^+}+k_{Hdw}^*W^+_\nu\partial F_{W^-}]\) | disagree | Neutral derivative terms agree. The charged \(W\) term uses the complex coefficient on the charge-conjugate structure relative to the paper, so the imaginary part has the opposite convention unless \(k_{Hdw}\) is defined as \(\kappa_{H\partial W}^*\). |
| Field strengths \(V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu\), \(G^a_{\mu\nu}=\partial G+g_sf^{abc}G^bG^c\), dual \(\tilde V_{\mu\nu}=\frac12\epsilon_{\mu\nu\rho\sigma}V^{\rho\sigma}\), eqs. (2.5)-(2.7) | Same definitions for physical \(A,Z,W^\pm\), gluons, and duals | agree | Matches the paper definitions. |
| Spin-1 fermions \(\sum_{f=q,\ell}\bar\psi_f\gamma^\mu(\kappa_{fa}a_f-\kappa_{fb}b_f\gamma^5)\psi_fX_{1\mu}\), eq. (2.8) | Separate sums over \(u,d,\nu,\ell\) with \(k_{qa},k_{qb},k_{\ell a},k_{\ell b}\) and SM-like \(a_f,b_f\) | agree | Same vector/axial current structure; reconstruction makes generation and color sums explicit. |
| Quark coefficients \(a_u,b_u,a_d,b_d\), eqs. (2.9)-(2.10) | Same coefficients written with \(e/(s_wc_w)\) | agree | Since \(g=e/s_w\), the expressions match. |
| Lepton coefficients “similarly for the leptons,” after eq. (2.10) | Explicit \(a_\nu=b_\nu=e/(4s_wc_w)\), \(a_\ell=e( -1/2+2s_w^2)/(2s_wc_w)\), \(b_\ell=-e/(4s_wc_w)\) | agree | These are the standard SM \(Z\)-like vector/axial coefficients implied by the paper. |
| \(i\kappa_{W1}g_{WWZ}(W^+_{\mu\nu}W^{-\mu}-W^-_{\mu\nu}W^{+\mu})X_1^\nu\), eq. (2.11) | \(ik_{w1}g_{WWZ}(F^{W^-}_{\mu\nu}W^{+\mu}-F^{W^+}_{\mu\nu}W^{-\mu})X_1^\nu\) | disagree | This is the negative of the paper’s bracket if \(k_{w1}=\kappa_{W1}\) and the same \(g_{WWZ}\) convention is used. |
| \(i\kappa_{W2}g_{WWZ}W^+_\mu W^-_\nu X_1^{\mu\nu}\), eq. (2.11) | \(ik_{w2}g_{WWZ}W^-_\mu W^+_\nu F_{X_1}^{\mu\nu}\) | disagree | Because \(X_1^{\mu\nu}\) is antisymmetric, exchanging \(W^+\leftrightarrow W^-\) with the Lorentz indices gives an overall minus sign. |
| \(-\kappa_{W3}W^+_\mu W^-_\nu(\partial^\mu X_1^\nu+\partial^\nu X_1^\mu)\), eq. (2.11) | \(-k_{w3}W^-_\mu W^+_\nu(\partial^\mu X_1^\nu+\partial^\nu X_1^\mu)\) | agree | The derivative tensor is symmetric in \(\mu,\nu\), so the charge/index ordering is equivalent. |
| \(+i\kappa_{W4}W^+_\mu W^-_\nu\tilde X_1^{\mu\nu}\), eq. (2.11) | \(+ik_{w4}W^-_\mu W^+_\nu\tilde F_{X_1}^{\mu\nu}\) | disagree | Same antisymmetry issue as the \(W2\) term: the reconstruction has the opposite sign for equal coupling definitions. |
| \(-\kappa_{W5}\epsilon_{\mu\nu\rho\sigma}[W^{+\mu}\partial^\rho W^{-\nu}-(\partial^\rho W^{+\mu})W^{-\nu}]X_1^\sigma\), eq. (2.11) | \(-k_{w5}\epsilon_{\mu\nu\rho\sigma}[W^{-\mu}\partial^\rho W^{+\nu}-(\partial^\rho W^{-\mu})W^{+\nu}]X_1^\sigma\) | agree | After relabeling the antisymmetric \(\epsilon_{\mu\nu\rho\sigma}\) indices, this is equivalent. |
| \(g_{WWZ}=-e\cot\theta_W\), below eq. (2.11) | \(g_{WWZ}=-ec_w/s_w\) | agree | Same definition. |
| \(-\kappa_{Z1}Z_{\mu\nu}Z^\mu X_1^\nu\), eq. (2.12) | \(-k_{z1}F^Z_{\mu\nu}Z^\mu X_1^\nu\) | agree | Same structure. |
| \(-\kappa_{Z3}X_{1\mu}(\partial_\nu Z^\mu)Z^\nu\), eq. (2.12) | \(-k_{z3}X_{1\mu}(\partial_\nu Z^\mu)Z^\nu\) | agree | Same structure. |
| \(-\kappa_{Z5}\epsilon_{\mu\nu\rho\sigma}X_1^\mu Z^\nu\partial^\rho Z^\sigma\), eq. (2.12) | Same \(k_{z5}\epsilon XZZ\) structure | agree | Same structure. |
| No effective \(\mathcal L^\gamma_1\), after eq. (2.12) | No \(X_1\gamma\gamma\) or \(X_1gg\) term listed | agree | Matches the paper’s Landau-Yang discussion for on-shell spin-1. |
| Parity restrictions for pure \(1^-\) and \(1^+\), eqs. (2.13)-(2.14) | General \(X_1\) terms retained with independent coefficients | agree | The reconstruction describes the general implemented interaction set; the paper gives restrictions for pure-parity limits. |
| Spin-2 fermions \(-\frac1\Lambda\sum_{f=q,\ell}\kappa_fT^f_{\mu\nu}X_2^{\mu\nu}\), eq. (2.15) | \(-\frac1\Lambda X_2^{\mu\nu}[k_qT^q_{\mu\nu}+k_{q3}(T^{q_3}_{\mu\nu}+Y^q_{\mu\nu})+k_\ell(T^\ell_{\mu\nu}+Y^\ell_{\mu\nu})]\) | disagree | The paper’s eq. (2.15) uses \(\kappa_fT^f_{\mu\nu}\) for quarks/leptons; reconstruction introduces an explicit separate third-generation quark coefficient \(k_{q3}\) and separate mass-trace pieces \(Y^q,Y^\ell\). |
| Explicit QED fermion \(T^f_{\mu\nu}\), eq. (2.17), including \(-g_{\mu\nu}[\bar\psi(i\gamma^\rho D_\rho-m_f)\psi-\frac12\partial_\rho(\bar\psi i\gamma^\rho\psi)]\) and derivative terms | Symmetric kinetic tensor \(\frac i4[\bar f\gamma_\mu D_\nu f-(D_\nu\bar f)\gamma_\mu f+\mu\leftrightarrow\nu]\), plus separate mass traces for \(t,b,\tau\) | disagree | The reconstruction is not the same off-shell tensor as eq. (2.17); mass and total-derivative/\(g_{\mu\nu}\) pieces are treated differently and only some fermion masses are retained. |
| Spin-2 vectors \(-\frac1\Lambda\sum_{V=Z,W,\gamma,g}\kappa_VT^V_{\mu\nu}X_2^{\mu\nu}\), eq. (2.16) | \(-\frac1\Lambda X_2^{\mu\nu}[k_gT^g+k_aT^\gamma+k_zT^Z+k_wT^W]_{\mu\nu}\) | agree | Same coupling pattern to gluon, photon, \(Z\), and \(W\) energy-momentum tensors. |
| Explicit photon \(T^\gamma_{\mu\nu}\), eq. (2.18), containing \(\partial_\rho\partial_\sigma A^\sigma A^\rho\), \((\partial_\rho A^\rho)^2\), and \(\partial_\mu\partial_\rho A^\rho A_\nu\) terms | Maxwell form \(T^\gamma_{\mu\nu}=\frac14\eta_{\mu\nu}F^2-F_{\mu\rho}F_\nu{}^\rho\) | disagree | The reconstruction omits the derivative/gauge-fixing-like terms present in the paper’s explicit eq. (2.18). They may vanish under specific gauge/on-shell conditions but are part of the displayed paper tensor. |
| Spin-2 gluon tensor, implied by eq. (2.16) and standard E-M tensor | \(\frac14\eta_{\mu\nu}G^2-G_{\mu\rho}G_\nu{}^\rho\) | agree | This matches the standard gauge-field E-M tensor structure, up to metric-sign convention. |
| Spin-2 massive \(Z,W\) tensors, implied by eq. (2.16) and references | Proca-like \(Z\) and \(W^\pm\) stress tensors with mass terms | agree | The paper does not print these explicitly, but the reconstruction matches the expected massive-vector E-M tensor content. |
| Universal RS-like limit \(\kappa_f=\kappa_V\ \forall f,V\), eq. (2.19) | Independent \(k_q,k_{q3},k_\ell,k_g,k_a,k_z,k_w\) | agree | The reconstruction gives the general non-universal parameterization; the universal limit is obtained by setting all relevant couplings equal, modulo the extra \(k_{q3}\). |
| Non-universal quark/gluon example \(-\kappa_qT^qX_2/\Lambda-\kappa_gT^gX_2/\Lambda\), Section 4.1 eq. (4.1) | Independent \(k_q\) and \(k_g\) | agree | Matches the paper’s non-universal spin-2 discussion for quarks and gluons. |

## Disagreements and Severity

| disagreement | severity | what a human should check |
|---|---|---|
| Reconstruction sums spin-0, spin-1, and spin-2 sectors into one \(\mathcal L_{\rm HCNP}\), whereas the paper writes \(\mathcal L_{\mathrm{HC},J}\) for a chosen \(J\) sector in eq. (2.1). | convention | Check whether the implementation file intentionally contains all hypotheses simultaneously with couplings used as switches. |
| Reconstruction omits the SM-like spin-0 \(X_0ZZ\) and \(X_0W^+W^-\) mass terms proportional to \(c_\alpha\kappa_{\rm SM}\) in eq. (2.4). | substantive | Check whether those terms are present elsewhere in the implementation or whether `kSM` being unused is an extraction/reconstruction error. |
| Charged spin-0 derivative \(W\) term uses the complex coefficient on the charge-conjugate structure relative to eq. (2.4). | convention | Check the implementation’s definition of `kHdw`; it may be the complex conjugate of the paper’s \(\kappa_{H\partial W}\). |
| Spin-1 \(W1\) term has the opposite sign relative to eq. (2.11) if \(k_{w1}=\kappa_{W1}\). | substantive | Check the charged-\(W\) field naming and sign convention in the implementation, including the definition of \(W^\pm_{\mu\nu}\). |
| Spin-1 \(W2\) term has the opposite sign relative to eq. (2.11) because the charged fields carry swapped Lorentz indices contracted with antisymmetric \(X_1^{\mu\nu}\). | substantive | Check whether the implementation defines `kw2` with an implicit minus sign relative to the paper. |
| Spin-1 \(W4\) term has the opposite sign relative to eq. (2.11) for the same antisymmetric-index reason as \(W2\). | substantive | Check whether the implementation defines `kw4` with an implicit minus sign relative to the paper. |
| Spin-2 fermion sector introduces a separate \(k_{q3}\) third-generation quark coupling and extra mass-trace pieces not present in the compact paper eq. (2.15). | substantive | Check whether the implementation extends the paper’s displayed \(\kappa_q,\kappa_\ell\) structure or whether the paper’s \(\sum_f\) notation was intended to allow generation-dependent \(\kappa_f\). |
| Reconstruction’s fermion energy-momentum tensor differs from the explicit paper tensor in eq. (2.17), especially in \(g_{\mu\nu}\), mass, and total-derivative terms. | substantive | Check the exact FeynRules definition of `Tfermion` and whether equations of motion or on-shell simplifications were applied in the reconstruction. |
| Reconstruction’s photon energy-momentum tensor omits derivative terms shown explicitly in paper eq. (2.18). | substantive | Check whether the implementation uses a simplified transverse/on-shell tensor or includes the omitted terms elsewhere through gauge-fixing conventions. |
| Reconstruction retains only \(t,b,\tau\) mass-trace pieces in spin-2 fermion terms. | convention | Check whether light-fermion masses are intentionally neglected in the implementation, as is common phenomenologically. |

## Overall Assessment

The reconstruction captures the broad Higgs Characterisation model structure: a below-EWSB EFT for neutral spin-0, spin-1, and spin-2 resonance hypotheses, with scalar/pseudoscalar Yukawa and field-strength operators, vector/axial spin-1 fermion currents, anomalous \(X_1WW/X_1ZZ\) interactions, and spin-2 couplings to SM energy-momentum tensors. The main physics-level gaps are the missing SM-like scalar \(X_0ZZ/X_0WW\) mass terms, several charged \(X_1WW\) sign differences, and a spin-2 energy-momentum tensor reconstruction that is not identical to the explicit tensors printed in the paper. Some differences may be implementation conventions or on-shell simplifications, but they are important enough that a reviewer should inspect the original implementation definitions before treating the reconstruction as a faithful transcription of the paper.