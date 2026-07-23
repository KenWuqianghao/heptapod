# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: removed the neutral `QuantumNumbers` entry from the self-conjugate Majorana `nH` class, made the sterile kinetic term explicitly Hermitian with `1/2 (K + HC[K])`, split the sterile mass and Yukawa interactions into separately conjugated `LMassSterile` and `LYukawaSterile` terms, and replaced the SM-inclusive final `LpSPSS` assignment with the required BSM-only final `LTot := RemoveHigherOrder[LKineticSterile + LNP];`. I could not run the full chain here because `wolframscript` cannot locate a Wolfram kernel in this environment.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=68.0

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=selfconjugate_quantum_numbers, hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=212.4
