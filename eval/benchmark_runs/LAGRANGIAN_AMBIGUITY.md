# Nine models that never declare a total Lagrangian

**A decision list, not a report.** Nine of the 28 benchmark models define
several independent top-level Lagrangians and never say which one — or which
sum — is the model. The harness now refuses to guess and leaves them
unscored. Declaring the total in `lag_overrides.json` scores them.

## Why this exists

`validation_benchmark.total_lag_symbol` used to take the **last** `^L... =`
line in the file. That is a guess about file order, and it was wrong for 11
of 28 models: it picked a sub-Lagrangian, FeynRules compiled that fragment,
and the fragment passed every Hermiticity / kinetic / mass check and imported
into MadGraph. `VLQ` was scored as passing on 1 of its 11 Lagrangian terms.

It now resolves the total by reference analysis — the term no other term
refers to. Redundant aliases are dropped (a root that is only a sum of terms
another root already reaches contributes nothing). Where one root survives,
it is the total. Where several do, the model is unscoreable until a human
declares the total.

**Summing the surviving roots is not a safe default.** Roots are independent
as *symbols*, not as physics. `ChernSimonsPortal` defines the same operator
twice — once in the symmetric phase and once expanded in mass eigenstates —
so adding them double-counts the interaction.

## Two kinds of ambiguity

### A. Complementary sectors — the sum is very likely right

The roots look like different parts of one model. A sum is the natural
reading, but it is still a physics judgement, so it is not applied.

| model | roots | proposed total | why |
|---|---|---|---|
| `331` | `LHiggs331`, `LGauge331Mass`, `LScalarFermion331`, `LTot` | `LHiggs331+LGauge331Mass+LGaugeSelf331+LScalarFermion331` | `LTot := LGaugeSelf331` alone, which looks like an agent slip: the other three sectors are defined and then never used. Note the proposed total pulls in `LGaugeSelf331` directly rather than via `LTot`. |
| `VLQ` | `LyTP`, `LDTP`, `LWTP`, `LZTP`, `LHTP`, `LyBP`, `LDBP`, `LWBP`, `LZBP`, `L4CKM`, `L4Mass` | sum of all 11 | These are the distinct couplings of the T' and B' quarks (Yukawa, W, Z, H) plus CKM and mass terms. Nothing here is an alternative to anything else. |
| `HNLs` | `LagHeavyN`, `LHeavyNDiracMass`, `LHeavyNEW`, and four hadronic-channel terms | sum of all 8 | The hadronic terms are separate decay channels, not competing parameterisations. |
| `ALRM_general` | `LYALRM`, `LSALRM`, `LFALRM`, `LeffALRM` | probably `LYALRM+LSALRM+LFALRM`, with `LeffALRM` checked | Yukawa, scalar and fermion sectors are complementary. `LeffALRM` may be an effective rewrite of some of them — please confirm it is not double-counting. |
| `VLC_LN` | `LChiralFull`, `LEDM`, `LTot` | probably `LTot` | `LTot` is already an explicit 9-term sum. `LChiralFull` and `LEDM` read as alternative parameterisations left in the file. |

### B. Genuine alternatives — someone must choose

These define mutually exclusive versions. Summing them is physically wrong.

| model | roots | the choice |
|---|---|---|
| `ChernSimonsPortal` | `LChernSimonsPortal`, `LChernSimonsPortalBroken` | Symmetric phase (Higgs doublet, `B`/`Wi` field strengths) versus the same operator expanded in `Z`/`A`/`W` mass eigenstates. Pick one. |
| `DMsimp` | `L0DM`, `L1DM` | Spin-0 mediator versus spin-1 mediator. Published as separate models. |
| `topBSM` | `LS0`, `LO0`, `LS1`, `LO1` | Colour-singlet versus colour-octet, spin 0 versus spin 1 — four separate simplified models in one file. |
| `CHEIDI` | `LHEIDI`, `LHEIDIgg`, `LTot` | `LHEIDI` is the SM piece and is complementary. But `LHEIDIgg` (full top loop) and `LHEIDIggHeavyTop` (heavy-top limit, which is what `LTot` selects) are alternatives. Likely `LHEIDI+LHEIDIgg` **or** `LHEIDI+LHEIDIggHeavyTop`. |

## How to apply a decision

```jsonc
// lag_overrides.json
{ "VLQ": "LyTP+LDTP+LWTP+LZTP+LHTP+LyBP+LDBP+LWBP+LZBP+L4CKM+L4Mass" }
```

The value is passed to `UFO_generator.wl` as `LagName` and evaluated as
Wolfram, so sums are fine. Then:

```bash
python eval/benchmark_runs/revalidate_affected.py 331,VLQ,...
```

## What this means for the numbers

The headline pass rate covers only models the harness can score. Anything
here is neither a pass nor a failure — it is a model that has not said what
it is. Two of the original 11 were resolved automatically as redundant
aliases (`Sextets` dropped `LD`; `MDMmodel` dropped the duplicate `LMDMNP`),
which is why nine remain rather than eleven.
