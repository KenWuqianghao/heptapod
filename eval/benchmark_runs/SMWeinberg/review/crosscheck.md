# Comparison of `reconstruction.md` Against the Paper Model

## Located Model Definitions

The paper defines the underlying dimension-five SMEFT model in **“The Standard Model at Dimension Five”**, with the Weinberg operator in **Eq. (2)**,
\[
\mathcal L_5=\frac{C^{\ell\ell'}_5}{\Lambda}[\Phi\cdot L^c_\ell][L_{\ell'}\cdot\Phi]+\text{H.c.},
\]
the effective Majorana mass in **Eq. (3)**,
\[
m_{\ell\ell'}=C^{\ell\ell'}_5v^2/\Lambda,
\]
and the EFT Lagrangian in **Eq. (4)**. In unitary gauge, the post-EWSB Weinberg terms are written in **Eq. (5)**. The collider prescription replaces the \((\nu_\ell\nu^c_{\ell'})\) current by an unphysical Majorana fermion \(N\), with the charged-current interaction in **Eq. (8)** and the implementation mass prescription in **Eq. (9)**.

The implementation-level field and interaction definitions are in the **Appendix: Technical details on methodology**. The generic-gauge Higgs/Goldstone definitions are in **Eqs. (16)-(17)**, the expanded Weinberg operator is in **Eqs. (18)-(22)**, the SMWeinberg UFO interaction Lagrangian is in **Eqs. (23)-(29)**, and the UFO parameter table is **Table II**.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---:|---|
| SMEFT Lagrangian \( \mathcal L_{\rm SMEFT}=\mathcal L_{\rm SM}+\mathcal L_5+\mathcal O(\Lambda^{-2})\), Eq. (4) | `LFull = LSM + LD5` | agree | The reconstruction mirrors the paper’s structure: SM plus the dimension-five/new-sector implementation. |
| Weinberg operator \(C^{\ell\ell'}_5[\Phi\cdot L^c_\ell][L_{\ell'}\cdot\Phi]/\Lambda+\text{H.c.}\), Eq. (2) | Replaced by \(N\)-mediated `LD5` terms | agree | The reconstruction does not keep the gauge-invariant operator literally; this matches the paper’s stated UFO prescription that models the current with an unphysical Majorana \(N\). |
| Effective mass \(m_{\ell\ell'}=C^{\ell\ell'}_5v^2/\Lambda\), Eq. (3) | \(m_N=(v^2/\Lambda)|C_{ee}+C_{e\mu}+C_{e\tau}+C_{\mu\mu}+C_{\mu\tau}+C_{\tau\tau}|\) | agree | This matches the paper’s implementation prescription in Eq. (9), not a single flavor-entry mass. |
| Unphysical Majorana neutrino \(N\) with mass \(m_N\), text before Eq. (9), Table II | Field table: \(N1\), Majorana, self-conjugate, neutral, mass `mN1` | agree | The paper calls \(N\) an unphysical Majorana neutrino and lists \(m_N\) as the internal mass parameter. Neutral singlet status is inferred consistently from the implementation. |
| \(m_N=|C^5_{ee}+C^5_{e\mu}+C^5_{e\tau}+C^5_{\mu\mu}+C^5_{\mu\tau}+C^5_{\tau\tau}|v^2/\Lambda\), Eq. (9) | Same expression with `Cee`, `Cem`, `Cet`, `Cmm`, `Cmt`, `Ctt` | agree | Same six independent symmetric flavor coefficients enter only through \(m_N\). |
| \(\Gamma_N\), Table II | \(\Gamma_N=\texttt{WN1}=0\) | agree | Table II identifies the width parameter; the reconstruction’s zero-width value is compatible with an internal unphysical mediator used for the prescription. |
| Generic-gauge Higgs doublet \(\sqrt2\Phi=(-i\sqrt2G^+,v+h+iG^0)^T\), Eqs. (16)-(17) | Uses \(H\), \(G^0\), \(G^-\)/\(G^+\) Goldstones in `LNHX`, `LNGX`, `LNGGX` | agree | The reconstruction uses the charge-conjugate Goldstone orientation for several “bare” terms, then adds H.c.; physics content matches. |
| Weinberg post-EWSB neutrino mass term \(-C^{\ell\ell'}_5v^2\nu^c_\ell\nu_{\ell'}/(2\Lambda)+\text{H.c.}\), Eq. (5), Eq. (18) | \(-\frac12m_N\bar NN\) in `LNKin` | agree | This is the \(N\)-mediated implementation of the mass insertion/current, with the implementation mass of Eq. (9). |
| Single-Higgs Weinberg term \(-C^{\ell\ell'}_5v\,h\,\nu^c_\ell\nu_{\ell'}/\Lambda+\text{H.c.}\), Eq. (5), Eq. (18) | \(-g_Wm_NH/(2M_W)\sum_i(\bar NP_L\nu_i+\bar\nu_iP_RN)\) in `LNHX` | agree | Using \(M_W=g_Wv/2\), the coefficient is \(-m_N/v\), matching the implementation form in Eq. (25). |
| Double-Higgs Weinberg term \(-C^{\ell\ell'}_5h h\,\nu^c_\ell\nu_{\ell'}/(2\Lambda)+\text{H.c.}\), Eq. (5), Eq. (18) | \(-g_W^2m_NH^2/(8M_W^2)\sum_i(\bar NP_L\nu_i+\bar\nu_iP_RN)\) in `LNHX` | agree | Coefficient equals \(-m_N/(2v^2)\), matching Eq. (25). |
| Charged current \(-g_W W^+_\mu\sum_\ell \bar N\gamma^\mu P_L\ell^-/\sqrt2+\text{H.c.}\), Eq. (8), Eq. (23) | \(+g_W W^+_\mu\sum_i\bar N\gamma^\mu P_L\ell_i/\sqrt2+\text{H.c.}\) in `LNCC` | disagree | Field content, chirality, flavor sum, and H.c. structure match, but the overall sign is opposite to Eqs. (8) and (23). |
| Neutral current \(-g_W Z_\mu\sum_\ell\bar N\gamma^\mu P_L\nu_\ell/(2\cos\theta_W)+\text{H.c.}\), Eq. (24) | \(+g_W Z_\mu\sum_i(\bar N\gamma^\mu P_L\nu_i+\bar\nu_i\gamma^\mu P_LN)/(2c_W)\) in `LNNC` | disagree | Same field content and chirality, but the coefficient sign is opposite to Eq. (24). |
| Higgs interaction \(-g_Wm_N h(1+g_Wh/(4m_W))\sum_\ell\bar NP_L\nu_\ell/(2m_W)+\text{H.c.}\), Eq. (25) | Same coefficient and H.c. in `LNHX` | agree | Matches coefficient, Higgs expansion, chirality, and flavor-universal implementation. |
| Charged-Goldstone term \(-i g_Wm_NG^+(1+g_Wh/(2m_W))\sum_\ell(\bar NP_L\ell+\bar\ell^cP_LN)/(2\sqrt2m_W)+\text{H.c.}\), Eq. (26) | \(+i g_Wm_NG^-(1+g_WH/(2M_W))\sum_i(\bar\ell_iP_RN+\bar NP_R\ell_i^c)/(2\sqrt2M_W)+\text{H.c.}\) in `LNGX` | agree | Reconstruction writes the charge-conjugate \(G^-\) piece as the bare term; with H.c., it matches Eq. (26). The \(P_R\) form is the conjugate bilinear of the paper’s \(P_L\) form. |
| Neutral-Goldstone term \(-i g_Wm_NG^0(1+g_Wh/(2m_W))\sum_\ell\bar NP_L\nu_\ell/(2m_W)+\text{H.c.}\), Eq. (27) | \(+i g_Wm_NG^0(1+g_WH/(2M_W))\sum_i\bar\nu_iP_RN/(2M_W)+\text{H.c.}\) in `LNGX` | agree | Reconstruction displays the Hermitian-conjugate bilinear as the bare term; with H.c., coefficient and chirality match Eq. (27). |
| \(G^+G^+\) contact term \(+g_W^2m_N\,2G^+G^+\sum_{\ell,\ell'}\bar\ell^cP_L\ell'/(8m_W^2)+\text{H.c.}\), Eq. (28) | \(+g_W^2m_N(G^-)^2\sum_{i,j}\bar\ell_iP_R\ell_j^c/(4M_W^2)+\text{H.c.}\) in `LNGGX` | agree | Reconstruction writes the H.c. \(G^-G^-\) orientation; coefficient and all ordered flavor combinations match. |
| \(G^0G^0\) contact term \(+g_W^2m_NG^0G^0\sum_\ell\bar NP_L\nu_\ell/(8m_W^2)+\text{H.c.}\), Eq. (28) | \(+g_W^2m_N(G^0)^2\sum_i\bar\nu_iP_RN/(8M_W^2)+\text{H.c.}\) in `LNGGX` | agree | Reconstruction writes the conjugate bilinear; H.c. completes the paper term. |
| Mixed \(G^0G^+\) contact term \(+g_W^2m_NG^0G^+\sum_\ell(\bar NP_L\ell+\bar\ell^cP_LN)/(4\sqrt2m_W^2)+\text{H.c.}\), Eq. (29) | \(+g_W^2m_NG^-G^0\sum_i(\bar\ell_iP_RN+\bar NP_R\ell_i^c)/(4\sqrt2M_W^2)+\text{H.c.}\) in `LNGGX` | agree | Reconstruction gives the charge-conjugate \(G^-G^0\) bare orientation; full H.c. agrees with Eq. (29). |
| Direct flavor-dependent vertices proportional to individual \(C^{\ell\ell'}_5\), Eqs. (18)-(22) | No independent \(C_{ij}\)-dependent vertices; coefficients enter only through \(m_N\) | agree | This matches the SMWeinberg UFO prescription described around Eq. (9), although it is not the literal flavor-basis Weinberg operator. |
| \(Z\), Higgs, and Goldstone interactions in the appendix, Eqs. (24)-(29) | Included in `LNNC`, `LNHX`, `LNGX`, `LNGGX` | agree | These terms would look extra if compared only to the main-text Eq. (8), but they are explicitly part of the appendix UFO Lagrangian. |
| \(N\) kinetic term | \(\frac{i}{2}\bar N\gamma^\mu\partial_\mu N\) in `LNKin` | agree | The paper does not print this term explicitly, but a single free Majorana field with mass \(m_N\) is required by the implementation. Ordinary derivative is consistent with \(N\) being neutral/singlet. |
| Gauge-covariant kinetic coupling of \(N\) | None | agree | The paper’s \(N\) is an unphysical Majorana neutrino with prescribed EW interactions, not a field carrying SM gauge indices. |

## Disagreements to Check

1. **Charged-current overall sign, Eqs. (8) and (23)** — severity: **convention**.  
   Human check: compare the original FeynRules/UFO vertex convention for \(W^+N\ell^-\) against the paper’s printed \(\Delta\mathcal L\), because the reconstruction has the same fields and chirality but the opposite Lagrangian sign.

2. **Neutral-current overall sign, Eq. (24)** — severity: **convention**.  
   Human check: verify whether the \(ZN\nu\) sign in the implementation is tied to the same convention as the charged-current sign or whether it is a transcription/sign error relative to the appendix.

No substantive mismatch was found in the mass prescription, flavor sums, Majorana nature of \(N\), Higgs terms, Goldstone terms, Hermitian-conjugate structure, or chirality assignments after accounting for charge-conjugate bilinears.

## Overall Assessment

The reconstruction closely matches the SMWeinberg implementation described in the paper’s appendix: it identifies the same unphysical neutral Majorana mediator \(N\), the same internally calculated mass \(m_N\), the same flavor-universal \(W/Z/H\) and Goldstone interactions, and the same replacement of explicit \(C^{\ell\ell'}_5\)-dependent Weinberg vertices by coefficients entering through \(m_N\). The main caveat is an apparent overall sign difference in the reconstructed \(W\) and \(Z\) interaction terms relative to the printed Eqs. (8), (23), and (24); this is likely convention-level but should be checked against the actual FeynRules/UFO vertex output before relying on relative signs in amplitudes involving interference.