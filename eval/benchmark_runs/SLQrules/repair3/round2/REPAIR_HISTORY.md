# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` to add hermitian-conjugation rules for the chiral projectors: `ProjL /: HC[ProjL] = ProjL;` and `ProjR /: HC[ProjR] = ProjR;`. The validation failure showed leftover `HC[ProjL]`/`HC[ProjR]` inside the nonzero `L - HC[L]` vertices, so this is a technical FeynRules simplification fix that preserves the fields, parameters, quantum numbers, and operator structure; `LTot` remains the final top-level assignment. I could not rerun the full Wolfram check locally because `wolframscript` is installed but no Wolfram kernel path is configured.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=True, tags=hermiticity_fail, compile_seconds=3563.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=True, tags=hermiticity_fail, compile_seconds=2623.3
