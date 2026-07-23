# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: removed the neutral `QuantumNumbers -> {Q -> 0, Y -> 0}` from the self-conjugate `Hh` scalar class to eliminate the FeynRules self-conjugate quantum-number warning, changed both HEIDI gluon-coupling mode sums from `Range[Heidi$nmodes]` to the explicit generated ten-mode range `Range[10]` so Mathematica does not evaluate an external parameter as a range bound, and added the required final top-level `LTot := LHEIDIggHeavyTop;` assignment so the BSM Lagrangian is defined cleanly for the tool chain.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=28.0

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` in place: the HEIDI scalar-gluon operators now divide by the declared real `Heidi$v` parameter instead of the SM `v` symbol, which removes the `v - HC[v]` hermiticity artifact without changing the operator structure or values; I also added a pre-`LTot` UFO Python 3 compatibility hook that patches generated UFO `.py` files from Python-2 `raise/except` syntax so MadGraph can import them. `LTot := LHEIDIggHeavyTop;` remains the final top-level assignment. I could not run the full validation locally because `wolframscript` is installed but cannot locate a Wolfram kernel in this environment.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=26.5

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=25.4
