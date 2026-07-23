# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: commented the stray prose that caused the Mathematica syntax abort, renamed the charged kaon class from built-in-colliding `K` to `Kp` and updated its field references, removed neutral quantum-number declarations from self-conjugate mesons, fixed the `HEAVR` typo to use the declared `HEAV` matrix, added missing semileptonic form-factor tensor declarations, localized missing dummy indices, corrected the neutrino propagator-label list length, and added the required final BSM-only `LTot := ...;` assignment. I could not run the full FeynRules/MadGraph chain here because `wolframscript` cannot find a Wolfram kernel in this shell.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=265.7

## For reference — the ORIGINAL model's outcome before any repair:
status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=lag_symbol_undefined, fr_syntax_error, duplicate_particle_names, selfconjugate_quantum_numbers, compile_seconds=6.3
