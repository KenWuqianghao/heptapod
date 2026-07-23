# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: renamed the heavy Majorana neutrino class from Mathematica built-in `N` to `HN` and changed the corresponding `bar[...]` interaction terms to use `HN[...]`, removed `Q -> 0` quantum-number declarations from the self-conjugate neutral `ZR` and `HN` classes, and replaced the final `LBSM = ...` assignment with the required last top-level `LTot := LWRQuarks + LWRLeptons + LZRQuarks + LZRLeptons;`. These are technical FeynRules/UFO fixes for the reported built-in-symbol collision, self-conjugate quantum-number issue, and expected total-Lagrangian symbol without changing fields, masses, couplings, or operator structure.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=222.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=builtin_symbol_collision, selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=279.9
