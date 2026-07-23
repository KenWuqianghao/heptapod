# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: removed `QuantumNumbers` from the self-conjugate Majorana `nH` class, replaced the zero-padded `N1L` mixing sum with the equivalent explicit `n4/n5` combination to prevent zero-strength `CC[vebar]` artifacts leaking into the UFO, changed the sterile Yukawa Higgs insertion from `PhiNPbar` to `PhiNP` to restore charge-consistent Goldstone couplings, removed the model-local `LSM` inclusion from the BSM Lagrangian, and made the final top-level assignment `LTot := LKineticSterile + LNP;` as required so the validator can add the SM separately.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=43.7

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=selfconjugate_quantum_numbers, hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=214.2
