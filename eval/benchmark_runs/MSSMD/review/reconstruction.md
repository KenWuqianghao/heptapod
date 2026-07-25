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