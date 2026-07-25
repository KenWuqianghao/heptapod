# Reverse-check review package — `pNG_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `pNG/model/pNG_gen.fr` |
| original model name | `pNG_gen` (hidden from the agent) |
| paper | pNG/text/1912.04008.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LHiggsPng` (`:=`)

```mathematica
Block[{ii, mu, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; ExpandIndices[DC[Phibar[ii], mu] DC[Phi[ii], mu] + muPsq/2 Phibar[ii] Phi[ii] - lambdaP/2 Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand -> {SU2D, SU2W}]/.feynmangaugerules]
```

### `LS` (`:=`)

```mathematica
del[Sbar, mu] del[S, mu] + muSsq/2 Sbar S - lambdaS/2 (Sbar S)^2
```

### `Lint` (`:=`)

```mathematica
Block[{ii, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; ExpandIndices[-lambdaPS Phibar[ii] Phi[ii] Sbar S, FlavorExpand -> {SU2D}]/.feynmangaugerules]
```

### `Lsoft` (`:=`)

```mathematica
muSpsq/4 (S^2 + Sbar^2)
```

### `LpNG` (`:=`)

```mathematica
LS + Lint + Lsoft
```

### `LScalarPng` (`:=`)

```mathematica
LHiggsPng + LpNG
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

The scalar doublet is declared as
\[
\Phi_i =
\begin{pmatrix}
-i\,G^+\\[2pt]
\dfrac{v_h+c_\theta h+s_\theta h_2+iG^0}{\sqrt2}
\end{pmatrix}_i,
\qquad
c_\theta=\cos\theta,\quad s_\theta=\sin\theta ,
\]
with hypercharge \(Y_\Phi=1/2\). The complex singlet is
\[
S=\frac{v_s-s_\theta h+c_\theta h_2+iX}{\sqrt2}.
\]

The covariant derivative acting on \(\Phi\) is
\[
D_\mu \Phi_i
=
\partial_\mu \Phi_i
+i g\, W^a_\mu (T^a)_{ij}\Phi_j
+i g' Y_\Phi B_\mu \Phi_i,
\qquad Y_\Phi=\frac12,
\]
with no \(SU(3)_c\) coupling. The singlet \(S\) uses an ordinary derivative,
\[
\partial_\mu S,
\]
because it is neutral under \(SU(3)_c\times SU(2)_L\times U(1)_Y\).

The file sets `FeynmanGauge = False`, so Goldstone fields are removed by
\[
G^0=G^+=G^-=0
\]
inside `LHiggsPng` and `Lint`.

### `LHiggsPng`

\[
\mathcal L_{\texttt{LHiggsPng, kin}}
=
(D_\mu\Phi)^\dagger_i(D^\mu\Phi)_i .
\]

\[
\mathcal L_{\texttt{LHiggsPng, mass}}
=
\frac{\mu_\Phi^2}{2}\,\Phi_i^\dagger\Phi_i .
\]

\[
\mathcal L_{\texttt{LHiggsPng, quartic}}
=
-\frac{\lambda_\Phi}{2}
(\Phi_i^\dagger\Phi_i)
(\Phi_j^\dagger\Phi_j).
\]

### `LS`

\[
\mathcal L_{\texttt{LS, kin}}
=
(\partial_\mu S^\dagger)(\partial^\mu S).
\]

\[
\mathcal L_{\texttt{LS, mass}}
=
\frac{\mu_S^2}{2}\,S^\dagger S .
\]

\[
\mathcal L_{\texttt{LS, quartic}}
=
-\frac{\lambda_S}{2}(S^\dagger S)^2 .
\]

### `Lint`

\[
\mathcal L_{\texttt{Lint}}
=
-\lambda_{\Phi S}
(\Phi_i^\dagger\Phi_i)(S^\dagger S).
\]

### `Lsoft`

\[
\mathcal L_{\texttt{Lsoft}}
=
\frac{\mu_S^{\prime 2}}{4}
\left(S^2+S^{\dagger 2}\right).
\]

### Composite Symbols

\[
\mathcal L_{\texttt{LpNG}}
=
\mathcal L_{\texttt{LS}}
+
\mathcal L_{\texttt{Lint}}
+
\mathcal L_{\texttt{Lsoft}} .
\]

\[
\mathcal L_{\texttt{LScalarPng}}
=
\mathcal L_{\texttt{LHiggsPng}}
+
\mathcal L_{\texttt{LpNG}} .
\]

The internal parameter definitions are
\[
\lambda_\Phi
=
\frac{M_h^2 c_\theta^2+M_{h_2}^2 s_\theta^2}{v_h^2},
\]
\[
\lambda_S
=
\frac{M_h^2 s_\theta^2+M_{h_2}^2 c_\theta^2}{v_s^2},
\]
\[
\lambda_{\Phi S}
=
\frac{(M_{h_2}^2-M_h^2)s_\theta c_\theta}{v_h v_s},
\]
\[
\mu_S^{\prime 2}=m_X^2,
\]
\[
\mu_\Phi^2
=
\lambda_\Phi v_h^2+\lambda_{\Phi S}v_s^2,
\]
\[
\mu_S^2
=
\lambda_S v_s^2+\lambda_{\Phi S}v_h^2-\mu_S^{\prime 2}.
\]

## Field Table

| `.fr` class | Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)_Y\) / charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---|---|---|
| `S[2]` | `h2` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | \(M_{h_2}=\texttt{Mh2}=300\) |
| `S[3]` | `X` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | \(m_X=\texttt{mX}=100\) |
| `S[11]` | `Phi[i]` | 0 | singlet | doublet | \(Y=1/2\) | no | unphysical field, no mass declared |
| `S[12]` | `S` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | no | unphysical complex field, no mass declared |

## External Parameters

| Parameter | Value | Appears in / multiplies | Physical meaning |
|---|---:|---|---|
| `vs` | 300 | Singlet field shift \(S=(v_s-s_\theta h+c_\theta h_2+iX)/\sqrt2\); also enters \(\lambda_S\), \(\lambda_{\Phi S}\), and \(\mu_S^2\) | Vacuum expectation value of the complex gauge-singlet scalar |
| `theta` | 0.7854 | Defines \(c_\theta=\cos\theta\), \(s_\theta=\sin\theta\), which enter the scalar-field rotations and the derived quartic couplings | Mixing angle between the neutral doublet scalar excitation and the real singlet scalar excitation |

## Physics Summary

The file encodes a scalar extension of the electroweak Higgs sector by one complex gauge-singlet scalar \(S\), whose real component mixes with the neutral Higgs excitation to form \(h\) and \(h_2\), while its imaginary component is the real scalar \(X\). The soft term \(\mu_S^{\prime 2}(S^2+S^{\dagger2})/4\) gives \(X\) a mass and explicitly breaks the phase symmetry of the complex singlet down to a residual symmetry that keeps \(X\) self-conjugate. The interactions mediate Higgs-portal processes through \((\Phi^\dagger\Phi)(S^\dagger S)\), including scalar mixing, couplings of \(h\) and \(h_2\) to Standard Model electroweak states through the doublet component, and portal production or annihilation involving pairs of \(X\).

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper locations

The model is defined in section 2, “Pseudo-Nambu-Goldstone Dark Matter.” The central Lagrangian is eq. (2.1),
\[
\mathcal L=\mathcal L_{\rm SM}+\mathcal L_S+\mathcal L_{\rm soft},
\]
with the singlet-sector terms in eqs. (2.2) and (2.3). The SM scalar potential is eq. (2.7). The field decomposition is given in eq. (2.8), the stationary-point relations in eqs. (2.9)-(2.10), the CP-even mass matrix and rotation in eqs. (2.11)-(2.15), and the physical parameter map in eqs. (2.17)-(2.20). Appendix A, especially eqs. (A.1)-(A.9), fixes the mass-eigenstate coupling and rotation conventions.

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Full model \(\mathcal L=\mathcal L_{\rm SM}+\mathcal L_S+\mathcal L_{\rm soft}\), section 2, eq. (2.1) | Composite `LScalarPng = LHiggsPng + LpNG`, with `LpNG = LS + Lint + Lsoft` | disagree | The reconstruction captures the scalar/Higgs-portal part, but it does not reconstruct the full \(\mathcal L_{\rm SM}\). It includes the Higgs doublet kinetic and potential but omits SM gauge kinetic terms, fermion kinetic terms, and Yukawa terms. |
| \(\mathcal L_{\rm SM}\), eq. (2.1), with \(\Phi\) the SM Higgs doublet | `LHiggsPng, kin = (D_\mu\Phi)^\dagger_i(D^\mu\Phi)_i` | agree | This is the SM Higgs doublet kinetic term contained in \(\mathcal L_{\rm SM}\). The reconstruction’s covariant derivative with \(SU(2)_L\) and \(U(1)_Y\), no \(SU(3)_c\), and \(Y_\Phi=1/2\) is the standard Higgs-doublet assignment. |
| SM scalar potential \(V_{\rm SM}= -\mu_\Phi^2\Phi^\dagger\Phi/2+\lambda_\Phi(\Phi^\dagger\Phi)^2/2\), eq. (2.7) | `LHiggsPng, mass = +\mu_\Phi^2 \Phi^\dagger\Phi/2`; `quartic = -\lambda_\Phi(\Phi^\dagger\Phi)^2/2` | agree | Since the Lagrangian contains \(-V_{\rm SM}\), the reconstruction’s signs and factors match the paper. |
| Remaining SM terms in \(\mathcal L_{\rm SM}\), eq. (2.1); Yukawa convention appears explicitly in Appendix A, eqs. (A.7)-(A.8) | No SM gauge kinetic, fermion kinetic, or SM Yukawa sector reconstructed | missing-in-reconstruction | This is a scope gap if the reconstruction is meant to reproduce the full paper Lagrangian. Appendix A uses the Yukawa couplings \(\kappa_{hff}=m_f\cos\theta/v_h\), \(\kappa_{Hff}=m_f\sin\theta/v_h\), which require the SM Yukawa sector. |
| Complex scalar singlet \(S\), section 2 before eq. (2.1) | `S` is complex, spin-0, \(SU(3)_c\) singlet, \(SU(2)_L\) singlet, \(Y=0\) | agree | The field representation and gauge neutrality match the paper’s “new complex scalar field \(S\)” and ordinary derivative in eq. (2.2). |
| Singlet kinetic term \((\partial_\mu S)^*(\partial^\mu S)\), eq. (2.2) | `LS, kin = (\partial_\mu S^\dagger)(\partial^\mu S)` | agree | Same physics content. |
| Singlet mass term \(+\mu_S^2 |S|^2/2\), eq. (2.2) | `LS, mass = +\mu_S^2 S^\dagger S/2` | agree | Same sign and factor. |
| Higgs portal term \(-\lambda_{\Phi S}\Phi^\dagger\Phi |S|^2\), eq. (2.2) | `Lint = -\lambda_{\Phi S}(\Phi_i^\dagger\Phi_i)(S^\dagger S)` | agree | Same operator, sign, and coefficient. |
| Singlet quartic term \(-\lambda_S |S|^4/2\), eq. (2.2) | `LS, quartic = -\lambda_S(S^\dagger S)^2/2` | agree | Same operator, sign, and coefficient. |
| Soft breaking term \(\mathcal L_{\rm soft}=\mu_S'^2(S^2+S^{*2})/4\), eq. (2.3) | `Lsoft = \mu_S'^2(S^2+S^{\dagger2})/4` | agree | Same soft \(U(1)\)-breaking term and coefficient. |
| Dark \(U(1)\): \(S\to e^{i\alpha}S\), eq. (2.4); soft breaking by \(\mu_S'^2\), text after eq. (2.4) | Reconstruction says the soft term breaks the phase symmetry and gives \(X\) a mass | agree | Correct. The paper further states the residual symmetry as \(Z_2\otimes CP\). |
| Dark CP \(S\to S^*\), eq. (2.5), with \(\chi\to-\chi\) after eq. (2.8) | \(X\) is real, self-conjugate, stable pNG component | agree | Reconstruction’s \(X\) corresponds to paper’s \(\chi\). |
| Unit-gauge decomposition \(\Phi=\frac1{\sqrt2}(0,\ v_h+\phi)^T\), \(S=(v_s+s+i\chi)/\sqrt2\), eq. (2.8) | \(\Phi=(-iG^+,\ (v_h+c_\theta h+s_\theta h_2+iG^0)/\sqrt2)^T\), \(S=(v_s-s_\theta h+c_\theta h_2+iX)/\sqrt2\), with Goldstones removed for `FeynmanGauge=False` | agree | After setting Goldstones to zero and identifying \(h_2\equiv H\), \(X\equiv\chi\), the reconstruction implements \(\phi=c_\theta h+s_\theta H\), \(s=-s_\theta h+c_\theta H\), matching eq. (A.3). The explicit Goldstone fields are gauge-completion details not present in the paper’s unitary-gauge display. |
| Physical \(\chi\) mass \(m_\chi^2=\mu_S'^2\), text after eq. (2.8), and \(\mu_S'^2=m_\chi^2\), eq. (2.18) | \(\mu_S'^2=m_X^2\) | agree | Same relation with \(X\equiv\chi\). |
| Stationary condition \(\mu_\Phi^2=\lambda_\Phi v_h^2+\lambda_{\Phi S}v_s^2\), eq. (2.9) | Same internal parameter definition | agree | Matches exactly. |
| Stationary condition \(\mu_S^2=\lambda_Sv_s^2+\lambda_{\Phi S}v_h^2-\mu_S'^2\), eq. (2.10) | Same internal parameter definition | agree | Matches exactly. |
| CP-even mass matrix \(M^2=\begin{pmatrix}\lambda_\Phi v_h^2&\lambda_{\Phi S}v_hv_s\\ \lambda_{\Phi S}v_hv_s&\lambda_Sv_s^2\end{pmatrix}\), eq. (2.11) | Not explicitly listed, but implied by the field rotation and parameter definitions | agree | The reconstruction’s mixing convention and parameter map are consistent with this matrix. |
| Rotation \(O=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix}\), eq. (2.13), and \((\phi,s)^T=O(h,H)^T\), Appendix A eq. (A.3) | \(\Phi\) neutral component contains \(c_\theta h+s_\theta h_2\); \(S\) real part contains \(-s_\theta h+c_\theta h_2\) | agree | Correct if \(h_2\) is identified with the paper’s \(H\). |
| Free physical parameters \(\{m_\chi,v_s,\theta,m_H\}\), eq. (2.17) | External parameters table lists `vs = 300`, `theta = 0.7854`; field table lists \(M_{h_2}=300\), \(m_X=100\) | disagree | The paper treats these as free model parameters, not fixed physical predictions. These look like implementation defaults or benchmark values, but the reconstruction does not clearly distinguish defaults from the model definition. |
| \(\lambda_\Phi=(m_h^2\cos^2\theta+m_H^2\sin^2\theta)/v_h^2\), eq. (2.18) | Same with \(M_{h_2}\) for \(m_H\) | agree | Matches after \(h_2\equiv H\). |
| \(\lambda_S=(m_h^2\sin^2\theta+m_H^2\cos^2\theta)/v_s^2\), eq. (2.19) | Same with \(M_{h_2}\) for \(m_H\) | agree | Matches. |
| \(\lambda_{\Phi S}=(m_H^2-m_h^2)\sin\theta\cos\theta/(v_hv_s)\), eq. (2.20) | Same with \(M_{h_2}\) for \(m_H\) | agree | Matches sign and coefficient. |
| \(m_h=125\ \mathrm{GeV}\), \(v_h=246\ \mathrm{GeV}\), eq. (2.16) | Reconstruction includes \(h\) in the doublet rotation but does not list the \(h\) field or its fixed mass in the field table | missing-in-reconstruction | The reconstruction’s field table lists `h2` and `X`, but not the SM-like mass eigenstate \(h\), even though \(h\) appears in the reconstructed field definitions. |
| DM-scalar couplings \(\mathcal L_S\supset-\frac12\chi^2(\kappa_{\chi\chi h}h+\kappa_{\chi\chi H}H)\), eq. (A.4), with \(\kappa_{\chi\chi h}=-m_h^2\sin\theta/v_s\), \(\kappa_{\chi\chi H}=+m_H^2\cos\theta/v_s\), eqs. (A.5)-(A.6) | Not explicitly reconstructed as couplings, but implied by the same scalar potential and rotation | agree | No contradiction; the reconstructed potential and rotation generate the Appendix A couplings. |
| SM fermion couplings after mixing, \(\kappa_{hff}=m_f\cos\theta/v_h\), \(\kappa_{Hff}=m_f\sin\theta/v_h\), eqs. (A.7)-(A.8) | Not reconstructed | missing-in-reconstruction | These follow from \(\mathcal L_{\rm SM}\), which is not included except for selected Higgs terms. |
| Boundedness conditions \(\lambda_\Phi>0\), \(\lambda_S>0\), \(\lambda_{\Phi S}>-\sqrt{\lambda_\Phi\lambda_S}\), eq. (3.1) | Not reconstructed | missing-in-reconstruction | These are theoretical constraints rather than Lagrangian terms, but they are part of the paper’s model setup for scans. |
| Perturbative unitarity bound \(\lambda_S<8\pi/3\), eq. (3.2) | Not reconstructed | missing-in-reconstruction | Also a scan/model constraint rather than a term. |

## Disagreements and checks

- **Substantive:** The reconstruction does not include the full \(\mathcal L_{\rm SM}\) from eq. (2.1); a human should check whether the implementation file intentionally imports the SM separately or whether the reconstruction is incomplete.
- **Substantive:** The reconstruction presents \(v_s=300\), \(\theta=0.7854\), \(M_{h_2}=300\), and \(m_X=100\) as table values, while the paper defines \(\{m_\chi,v_s,\theta,m_H\}\) as free parameters in eq. (2.17); a human should check whether these are merely default benchmark values in the implementation.
- **Convention:** The reconstruction includes Goldstone fields in \(\Phi\), including a \(-iG^+\) convention, while the paper writes the decomposition in unitary gauge in eq. (2.8); a human should check the FeynRules gauge convention, but this does not change the physical scalar sector if Goldstones are removed.
- **Cosmetic:** The reconstruction uses \(h_2\) and \(X\), while the paper uses \(H\) and \(\chi\); a human should confirm that all downstream files consistently identify \(h_2\equiv H\) and \(X\equiv\chi\).
- **Substantive:** The reconstruction’s field table omits the SM-like Higgs mass eigenstate \(h\), even though \(h\) appears in the reconstructed field decompositions; a human should check whether the reconstruction table was intended to list only BSM/new classes or all scalar mass eigenstates.
- **Substantive:** SM Yukawa interactions and the resulting \(h/H\)-fermion couplings in Appendix A, eqs. (A.7)-(A.8), are absent from the reconstruction; a human should check whether those are supplied by an external SM model file.

## Overall assessment

The reconstructed singlet and Higgs-portal scalar sector agrees well with the paper’s core pNG dark matter model in section 2: the \(S\) kinetic term, mass term, quartic, portal interaction, soft \(U(1)\)-breaking term, mixing convention, and physical parameter relations all match once \(X\equiv\chi\) and \(h_2\equiv H\) are identified. The main caveat is scope: the paper’s model is \(\mathcal L_{\rm SM}\) plus the singlet sector, whereas the reconstruction only spells out selected Higgs/scalar pieces and omits most of the SM content and the mixed SM couplings used later in Appendix A. The fixed numerical entries in the reconstruction should be treated cautiously, since the paper defines those quantities as free scan parameters rather than fixed model values.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 12 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

