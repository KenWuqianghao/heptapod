# Correction to the repair-loop and validation results

**Supersedes the headline figures in `REPAIR_BENCHMARK_ANALYSIS.md` and
`validation_benchmark_report.md`.** Those documents are kept unedited as the
record of what was originally measured; this file states what was wrong and
what replaces it.

## The defect

`validation_benchmark.total_lag_symbol` chose each model's grand-total
Lagrangian by **file position** — the last line matching `^L<name> =`. The
chosen symbol was passed to `UFO_generator.wl` as `LagName`, which compiles
`LSM + <symbol>`.

That is a guess about file order. For 11 of the 28 models it selected a
sub-Lagrangian, so FeynRules compiled a **fragment** of the model. A fragment
is usually easier to satisfy than the whole: it can be Hermitian when the
full Lagrangian is not, and it can carry a clean mass spectrum simply by
omitting most fields. Those models then passed every check and imported into
MadGraph, and were counted as passing.

The worst cases:

| model | compiled | of | via symbol |
|---|---:|---:|---|
| `VLQ` | 1 | 11 | `L4Mass` |
| `topBSM` | 5 | 23 | `LO1` |
| `331` | 2 | 5 | `LTot`, itself `:= LGaugeSelf331` |
| `CHEIDI` | 4 | 12 | `LTot` |

`VLQ` was recorded as clearing the full chain having compiled its
fourth-generation mass term and none of the vector-like quark interactions.

## What changed

The total is now resolved by **reference analysis**: the term no other term
refers to. Roots that are pure aliases — a sum of terms another root already
reaches — are dropped as redundant, which resolves `Sextets` (`LD`) and
`MDMmodel` (a duplicated `LMDMNP`) without any judgement call.

Where one root survives it is the total. Where several survive, the model
never declared a total and the harness **refuses to guess**: status
`ambiguous_lagrangian_symbol`, and the model is left unscored.

Summing the surviving roots was considered and rejected. Roots are
independent as symbols, not as physics: `ChernSimonsPortal` defines the same
operator twice, once in the symmetric phase and once expanded in mass
eigenstates, so adding them double-counts the interaction.

## What this does to the numbers

**Unscoreable is not failed.** A model with no declared total may be
perfectly correct; the harness simply has nothing defensible to compile.

The whole benchmark was re-run against the corrected resolver, using the same
`.fr` files the review bundle ships:

| | before | after |
|---|---:|---:|
| confirmed to clear the full chain | 25 | **18** |
| confirmed to fail | 3 | **1** (`SLQrules`) |
| unscoreable — no declared total | 0 | **9** |
| total | 28 | 28 |

Of the 19 scoreable models, **18 clear the full chain**. The single failure,
`SLQrules`, fails exactly as before: a syntax error at line 660 of the
one-shot `.fr` stops FeynRules loading the model at all, so `LBSM` is never
defined. It has no repaired `final.fr` because the repair loop never
succeeded on it.

Seven models that were previously counted as passing are now unscoreable:
`331`, `CHEIDI`, `ChernSimonsPortal`, `DMsimp`, `VLC_LN`, `VLQ`, `topBSM`.
Two previously-failing models, `ALRM_general` and `HNLs`, are also
unscoreable rather than failing — their failures were measured on fragments
too, so those verdicts do not stand either.

- 19 of 28 models are scoreable. 9 are not, and are listed with their
  competing roots in `LAGRANGIAN_AMBIGUITY.md`.
- Of the 10 models previously reported as recovered by the repair loop,
  **7 remain verifiable**. `331`, `CHEIDI` and `VLC_LN` were all scored
  `pass_repaired` in phase 2 against a fragment, so those three repair claims
  cannot be evaluated as they stand.
- `331`'s recorded repair — a coupling named `e` colliding with the electron
  field, clearing Hermiticity — was measured on `LGaugeSelf331` alone. A
  Hermiticity check passing on a single gauge self-interaction term carries
  little information.

Three of those same models (`331`, `CHEIDI`, `VLC_LN`) are also among the
four whose blank-slate reverse check never completed. They are weak on both
axes independently.

## What did not change

The 19 scoreable models all resolve to the **same symbol the old rule
picked**, and all 19 reproduced their previous verdict on re-run. The
positional rule was right wherever it could score a model at all; the damage
was entirely in the models it should have refused.

So the corrected picture is not that the pipeline got worse. It is that 9
models were never really measured, and 18 confirmed passes are 18 real ones.

The error taxonomy in `REPAIR_BENCHMARK_ANALYSIS.md` — namespace collisions,
UFO-serialization leaks, Hermiticity residuals, generator-structure defects —
is unaffected. So is the central finding that diagnostic signal, not agent
capability, was the binding constraint.

## Reproducing

```bash
python eval/benchmark_runs/revalidate_affected.py     # scoreable models
```

Declare a total for an ambiguous model in `lag_overrides.json` to score it;
`LAGRANGIAN_AMBIGUITY.md` sets out what each one defines and which choices
are genuine physics decisions rather than clerical ones.
