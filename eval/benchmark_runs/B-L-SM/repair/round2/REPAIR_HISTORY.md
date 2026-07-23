# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: renamed the heavy Majorana class from Mathematica’s built-in `N` to `Nheavy` and updated `nuR` accordingly, removed invalid `QuantumNumbers` from self-conjugate real/Majorana fields, removed the explicit `Zp` Proca mass so the mass comes from the `Chi` vev, added the missing `1/2` on the Majorana Yukawa to avoid double-counting the mass term, subtracted the neutrino-Yukawa vev insertion that was producing non-diagonal active-heavy neutrino masses, and replaced the old `LBSM` assignment with the required final `LTot := LZpKin + LChi + LBLCurrent + LNuYuk;`. I could not run the full toolchain from this directory because no validation harness is present here and the local `wolframscript` has no configured kernel.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=66.8

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=False, kinetic=False, mass=False, madgraph_import=False, tags=builtin_symbol_collision, selfconjugate_quantum_numbers, hermiticity_fail, kinetic_terms_fail, mass_spectrum_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=964.6
