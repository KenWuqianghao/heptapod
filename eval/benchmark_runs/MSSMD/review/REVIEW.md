# Reverse-check review package — `MSSMD_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `MSSMD/repair/final.fr` |
| original model name | `MSSMD_gen` (hidden from the agent) |
| paper | MSSMD/text/1812.00380.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LN1NDAD` (`:=`)

```mathematica
I*gd*(neu1bar.Ga[mu].neuD)*AD[mu]
```

### `LADMuMu` (`:=`)

```mathematica
gd*(mbar.Ga[mu].m)*AD[mu]
```

### `LTot` (`:=`)

```mathematica
LN1NDAD + LADMuMu
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

No covariant derivatives `DC[...]` or field strengths `FS[...]` appear in this file. Therefore the file does not encode kinetic terms or gauge-covariant derivative structure. The only gauge/Lorentz content explicitly present is the vector field `AD[mu]` coupled to fermion vector currents through `Ga[mu] = \gamma^\mu`.

### `LN1NDAD`

\[
\mathcal{L}_{\texttt{LN1NDAD}}
=
i\,g_d\,
\bar{\tilde{\chi}}^0_1 \gamma^\mu \tilde{\chi}_D\,
A_{D\mu}
\]

Here `neu1bar.Ga[mu].neuD` is the spinor contraction
\(\bar{\tilde{\chi}}^0_1 \gamma^\mu \tilde{\chi}_D\). Both `neu1` and `neuD` are declared self-conjugate Majorana fermions. No chiral projectors appear, so this is a pure vector-current Lorentz structure as written in the file. The explicit factor of \(i\) is part of the `.fr` term.

### `LADMuMu`

\[
\mathcal{L}_{\texttt{LADMuMu}}
=
g_d\,
\bar{\mu}\gamma^\mu\mu\,
A_{D\mu}
\]

Here `mbar.Ga[mu].m` is the muon vector current. The muon field `m` is used but not declared in this file, so it is inherited from whatever base model this file was intended to extend.

### `LTot`

\[
\mathcal{L}_{\texttt{LTot}}
=
\mathcal{L}_{\texttt{LN1NDAD}}
+
\mathcal{L}_{\texttt{LADMuMu}}
\]

## Field Table

| `.fr` symbol | Members | Spin | SU(3) rep | SU(2) rep | U(1) / electric charge | Self-conjugate | Mass symbol and value |
|---|---:|---:|---|---|---|---|---|
| `AD` | `AD` | 1 | singlet, no color index | not declared | no `Q` declared, neutral by field usage | yes | `MAD`, no numeric value |
| `neu` | `neu1`, `neu2`, `neu3`, `neu4` | 1/2 | singlet, no color index | not declared | no `Q` declared, neutral by names/PDG | yes | `Mneu1 = 10.`, `Mneu2`, `Mneu3`, `Mneu4` |
| `ch` | `ch1`, `ch2` | 1/2 | singlet, no color index | not declared | `Q = +1` for particle, antiparticle has `Q = -1` | no | `Mch1`, `Mch2`, no numeric values |
| `go` | `go` | 1/2 | adjoint, `Index[Gluon]` | not declared | no `Q` declared | yes | `Mgo`, no numeric value |
| `neuD` | `neuD` | 1/2 | singlet, no color index | not declared | no `Q` declared, neutral by name/usage | yes | `MneuD = 1.` |
| `h0` | `h0` | 0 | singlet, no color index | not declared | no `Q` declared, neutral by name/PDG | yes | `MH01 = 125.` |
| `H0` | `H0` | 0 | singlet, no color index | not declared | no `Q` declared, neutral by name/PDG | yes | `MH02`, no numeric value |
| `A0` | `A0` | 0 | singlet, no color index | not declared | no `Q` declared, neutral by name/PDG | yes | `MA0`, no numeric value |
| `Hp` | `H+`, antiparticle `H-` | 0 | singlet, no color index | not declared | `Q = +1` for particle, antiparticle has `Q = -1` | no | `MHp`, no numeric value |
| `sn` | `sn1`, `sn2`, `sn3` | 0 | singlet, no color index | not declared | `Q = 0` | no | `Msn1`, `Msn2`, `Msn3`, no numeric values |
| `sl` | `sl1-` ... `sl6-` | 0 | singlet, no color index | not declared | `Q = -1` for particle, antiparticle has `Q = +1` | no | `Msl1` ... `Msl6`, no numeric values |
| `su` | `su1` ... `su6` | 0 | fundamental triplet, `Index[Colour]` | not declared | `Q = +2/3` for particle, antiparticle has `Q = -2/3` | no | `Msu1` ... `Msu6`, no numeric values |
| `sd` | `sd1` ... `sd6` | 0 | fundamental triplet, `Index[Colour]` | not declared | `Q = -1/3` for particle, antiparticle has `Q = +1/3` | no | `Msd1` ... `Msd6`, no numeric values |

## Parameters

| Parameter | Type | Appears in | Meaning from file content |
|---|---|---|---|
| `gd` | external real scalar, value `0.001` | Multiplies `LN1NDAD` and `LADMuMu` | New vector-current coupling of `AD` to \(\bar{\tilde{\chi}}^0_1\gamma^\mu\tilde{\chi}_D\) and \(\bar{\mu}\gamma^\mu\mu\) |
| `RNN[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of a neutral-fermion mixing matrix, block `NMIX` |
| `INN[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of a neutral-fermion mixing matrix, block `IMNMIX` |
| `RUU[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of chargino \(U\)-type mixing matrix, block `UMIX` |
| `IUU[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of chargino \(U\)-type mixing matrix, block `IMUMIX` |
| `RVV[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of chargino \(V\)-type mixing matrix, block `VMIX` |
| `IVV[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of chargino \(V\)-type mixing matrix, block `IMVMIX` |
| `RRn[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of sneutrino mixing matrix, block `SNUMIX` |
| `IRn[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of sneutrino mixing matrix, block `IMSNUMIX` |
| `RRl[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of charged-slepton mixing matrix, block `SELMIX` |
| `IRl[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of charged-slepton mixing matrix, block `IMSELMIX` |
| `RRu[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of up-squark mixing matrix, block `USQMIX` |
| `IRu[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of up-squark mixing matrix, block `IMUSQMIX` |
| `RRd[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Real part of down-squark mixing matrix, block `DSQMIX` |
| `IRd[i,j]` | external real matrix | Not used in any Lagrangian term in this file | Imaginary part of down-squark mixing matrix, block `IMDSQMIX` |
| `alp` | external real scalar | Not used in any Lagrangian term in this file | Scalar mixing angle or generic angle parameter, named \(\alpha\), block `FRALPHA` |

## Physics Summary

The file declares an MSSM-like spectrum of neutralinos, charginos, gluino, Higgs-sector scalars, sleptons, sneutrinos, and squarks, plus an additional neutral vector boson `AD` and a neutral Majorana fermion `neuD`. The only interactions actually encoded are vector-current couplings of `AD` to the muon current and to a mixed Majorana current involving `neu1` and `neuD`. This mediates processes such as \( \mu^+\mu^- \leftrightarrow A_D^\ast \leftrightarrow \tilde{\chi}^0_1 \tilde{\chi}_D \), as well as `AD` production or decay through muons and the neutral fermion pair when kinematically allowed.

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Located Paper Model Definitions

The paper does not provide a numbered Lagrangian or explicit symbolic field-representation table in the supplied `paper.tex`. The relevant model definitions are given in prose:

- **Section 1, Introduction:** dark SUSY benchmark: breaking of a new \(U(1)_D\) gives a massive dark photon \(\gamma_D\); \(\gamma_D\) couples to SM particles through kinetic mixing \(\epsilon\) with SM photons; topology \(h \to 2 n_1\), \(n_1 \to n_D+\gamma_D\), \(\gamma_D \to \mu^+\mu^-\).
- **Section 4, Signal modeling:** dark SUSY simulation choices: \(h\to 2n_1\), \(n_1\to n_D+\gamma_D\), \(m_{n_D}=1\) GeV, \(m_h=125\) GeV, \(m_{n_1}=10\) GeV, \(m_{\gamma_D}=0.25\)–\(8.5\) GeV, \(\gamma_D\to\mu^-\mu^+\) with 100% branching in the signal samples.
- **Section 7, Results / Figure 3 caption:** interpreted process \(pp\to h\to 2n_1\to 2\gamma_D+2n_D\to4\mu+X\), with \(m_{n_1}=10\) GeV and \(m_{n_D}=1\) GeV; limits shown in the \((\epsilon,m_{\gamma_D})\) plane.
- **NMSSM benchmark, Sections 1 and 4:** \(h_{1,2}\to 2a_1\), followed by \(a_1\to\mu^+\mu^-\), with \(h_{1,2}\) CP-even and \(a_1\) CP-odd.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Massive dark photon \(\gamma_D\) from broken \(U(1)_D\) (Section 1) | `AD`, spin-1, self-conjugate neutral vector, mass `MAD` | agree | The neutral massive vector field matches the paper’s \(\gamma_D\) at the level of particle content. The reconstruction does not encode the \(U(1)_D\) gauge origin or symmetry breaking. |
| Kinetic mixing of \(\gamma_D\) with SM photons via \(\epsilon\) (Section 1; Section 7) | Direct coupling \(g_d\,\bar\mu\gamma^\mu\mu\,A_{D\mu}\) | disagree | The paper defines the SM coupling mechanism as photon kinetic mixing controlled by \(\epsilon\), while the reconstruction has a direct muon-only vector coupling with coefficient \(g_d\). This may be an effective vertex, but it omits the photon mixing structure and expected coupling relation to electric charge. |
| Dark photon decay \(\gamma_D\to\mu^-\mu^+\), set to 100% in signal samples (Section 4) | `LADMuMu`: \(g_d\,\bar\mu\gamma^\mu\mu A_{D\mu}\) | agree | This term supports \(\gamma_D\to\mu^+\mu^-\). The paper does not give the Lorentz structure explicitly, but a vector dark photon coupled to the electromagnetic current is consistent with a vector muon current. |
| Higgs cascade \(h\to 2n_1\) (Sections 1 and 4; Figure 3 caption) | No \(h\,n_1 n_1\) term | missing-in-reconstruction | The paper’s dark SUSY topology requires Higgs decay to two lightest non-dark neutralinos. Reconstruction has scalar fields including `h0`, but no Higgs-neutralino interaction. |
| Neutralino transition \(n_1\to n_D+\gamma_D\) (Sections 1 and 4; Figure 3 caption) | `LN1NDAD`: \(i g_d\,\bar{\tilde\chi}^0_1\gamma^\mu\tilde\chi_D A_{D\mu}\) | agree | This is the only reconstruction term matching the required \(n_1 n_D \gamma_D\) transition. The paper does not specify chirality, phase convention, or coefficient structure, so the vector-current form cannot be fully validated from the paper text alone. |
| Dark neutralino \(n_D\), stable/undetected, \(m_{n_D}=1\) GeV (Section 4; Figure 3 caption) | `neuD`, self-conjugate neutral fermion, `MneuD = 1.` | agree | Mass and neutral invisible role match. The paper does not specify Majorana versus Dirac, so self-conjugacy is not confirmed by the paper text. |
| Lightest non-dark neutralino \(n_1\), \(m_{n_1}=10\) GeV (Sections 1 and 4; Figure 3 caption) | `neu1`, self-conjugate neutral fermion, `Mneu1 = 10.` | agree | Mass and neutralino role match. As with \(n_D\), the paper does not explicitly state Majorana conventions. |
| Dark photon mass range \(m_{\gamma_D}=0.25\)–\(8.5\) GeV (Section 4; Section 7) | `MAD`, no numeric value | missing-in-reconstruction | The reconstruction identifies a dark-vector mass parameter but does not encode the simulated mass range. |
| Dark photon lifetime controlled by \(\epsilon\) and \(m_{\gamma_D}\), \(c\tau_{\gamma_D}=0\)–100 mm (Sections 1, 4, 7) | No lifetime or \(\epsilon\)-dependent width structure | missing-in-reconstruction | The implementation reconstruction lacks the kinetic-mixing parameter and the lifetime relation \(\tau_{\gamma_D}(\epsilon,m_{\gamma_D})=\epsilon^{-2}f(m_{\gamma_D})\). |
| NMSSM process \(h_{1,2}\to2a_1\), \(a_1\to\mu^+\mu^-\) (Sections 1 and 4) | No \(h_{1,2}a_1a_1\) or \(a_1\mu\mu\) terms; scalar table has `h0`, `H0`, `A0`, `Hp` | missing-in-reconstruction | The reconstruction does not encode the NMSSM benchmark interactions. `A0` could be a generic CP-odd scalar, but the paper’s \(a_1\) decay and Higgs cascade are absent. |
| CP-even Higgs bosons \(h_1,h_2\) and CP-odd \(a_1\) in NMSSM benchmark (Section 1) | `h0`, `H0`, `A0`, `Hp` scalar spectrum | disagree | The broad scalar spectrum resembles a two-Higgs-sector/MSSM-style list, but the paper specifically discusses NMSSM \(h_1,h_2,a_1\), not charged Higgs phenomenology or the full scalar sector in the benchmark implementation. |
| Pair production of identical light bosons \(pp\to 2a+X\to4\mu+X\), model-independent framing (Section 1; Section 8) | `LTot = LN1NDAD + LADMuMu` only | missing-in-reconstruction | The reconstruction provides vertices for one dark SUSY decay chain but no production mechanism or generic pair-production operator. |
| Full MSSM-like neutralinos `neu1`–`neu4`, charginos, gluino, sfermions, extra Higgs states | Reconstruction field table lists many MSSM-like fields | extra-in-reconstruction | The paper’s dark SUSY interpretation only needs \(h\), \(n_1\), \(n_D\), and \(\gamma_D\), while the NMSSM benchmark needs \(h_{1,2}\) and \(a_1\). The extra MSSM-like spectrum is not defined in the paper’s benchmark description. |
| Direct muon-only dark-vector coupling \(g_d\,\bar\mu\gamma^\mu\mu A_{D\mu}\) | `LADMuMu` | extra-in-reconstruction | The paper states coupling to SM particles via kinetic mixing with photons, not a standalone muon-specific interaction. As an effective decay vertex it is useful, but as a model definition it is narrower than the paper. |
| Common coupling \(g_d\) for \(A_D\bar\mu\mu\) and \(A_D\tilde\chi_1^0\tilde\chi_D\) | `gd` multiplies both `LN1NDAD` and `LADMuMu` | disagree | The paper distinguishes dark-sector dynamics from SM coupling through kinetic mixing \(\epsilon\). It does not imply the same coefficient controls the neutralino transition and the muon coupling. |

## Disagreements and Human Checks

- **Kinetic mixing replaced by direct muon coupling** — **substantive**. Check whether `gd` was intended as an effective \(\epsilon e Q_\mu\) coupling after diagonalizing kinetic mixing, or whether the implementation incorrectly omitted photon/dark-photon mixing.

- **Same `gd` used for dark-sector transition and muon coupling** — **substantive**. Check the original implementation or model card to see whether two physically distinct couplings were collapsed into one parameter.

- **Missing Higgs decay \(h\to2n_1\)** — **substantive**. Check whether production and Higgs decay were intentionally handled externally by BRIDGE/Pythia rather than encoded in the FeynRules model.

- **Missing \(\epsilon\)-dependent lifetime/width relation** — **substantive**. Check whether the dark photon lifetime was imposed at event-generation level rather than derived from the model file.

- **Missing NMSSM \(h_{1,2}\to2a_1\), \(a_1\to\mu^+\mu^-\) interactions** — **substantive**. Check whether the reconstruction is only for the dark SUSY benchmark and not meant to cover the NMSSM benchmark also discussed in the paper.

- **Scalar-sector mismatch: `h0`, `H0`, `A0`, `Hp` versus paper’s \(h_1,h_2,a_1\)** — **convention/substantive**. Check whether `A0` is intended to represent \(a_1\), or whether this is a generic MSSM scaffold unrelated to the paper’s NMSSM benchmark.

- **Large extra MSSM-like spectrum in reconstruction** — **convention**. Check whether these fields are inherited boilerplate from an MSSM/FeynRules template and unused in the actual generated process.

- **Majorana assignment for \(n_1\) and \(n_D\)** — **convention**. Check the underlying dark SUSY model reference or implementation, since the paper calls them neutralinos but does not explicitly state the Majorana convention in the supplied text.

## Overall Assessment

The reconstruction captures the core dark SUSY decay-chain fields \(n_1\), \(n_D\), and \(\gamma_D\), including the benchmark masses \(m_{n_1}=10\) GeV and \(m_{n_D}=1\) GeV, and it includes vertices that can realize \(n_1\to n_D+\gamma_D\) and \(\gamma_D\to\mu^+\mu^-\). However, it is not a faithful full representation of the model as described in the paper: the paper’s defining SM portal is kinetic mixing through \(\epsilon\), not a direct muon-only coupling; the Higgs production/decay step \(h\to2n_1\) is absent; the \(\epsilon\)-dependent lifetime structure is absent; and the NMSSM benchmark terms are not represented. The extra MSSM-like field content appears mostly unused and may be implementation scaffold rather than physics used in the paper’s interpreted signal.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 23 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

