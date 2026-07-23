# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: fixed the syntax error in `LZpF` by removing the extra closing parenthesis, renamed the Majorana class from Mathematica built-in `N` to `NR` and updated all corresponding field/bar-field uses, removed `QuantumNumbers` from self-conjugate classes, expanded the `yNu` wildcard tensor value into explicit zero 3x3 entries, and replaced the final `LGeneralU1` assignment with the required final `LTot := ...` BSM Lagrangian assignment. Local delimiter and symbol-collision checks pass; I did not run the full FeynRules/MadGraph chain because the prompt forbids reading files outside this directory.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, compile_seconds=50.3

## Attempt 2
What was changed (the agent's own summary):
Changed `model.fr` only by correcting `M$InteractionOrderHierarchy` from `{{QCD, 1}, {QED, 2}, {NP, 3}}` to the standard FeynRules rule syntax `{QCD -> 1, QED -> 2, NP -> 3}`. This preserves all physics content but prevents FeynRules from emitting a malformed UFO coupling order named `1`, which matches the MadGraph import failure in `VALIDATION_REPORT.md`; `LTot` remains the final top-level assignment.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, compile_seconds=80.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=lag_symbol_undefined, fr_syntax_error, builtin_symbol_collision, selfconjugate_quantum_numbers, compile_seconds=6.2
