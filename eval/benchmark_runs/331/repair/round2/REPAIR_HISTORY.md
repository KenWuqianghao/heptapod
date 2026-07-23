# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: removed `QuantumNumbers` from the neutral self-conjugate fields `H2`, `H3`, `H0`, and `Zp`; changed all `Mix[...]` identifiers to strings as FeynRules requires; renamed numeric-leading SLHA block symbols `331INPUTS` and `331SCALAR` to valid Wolfram symbols; and added the required final `LTot := ...;` assignment using the BSM Lagrangian terms defined above it. I could not run the Wolfram validation locally because `wolframscript` is present but has no configured kernel path.

Validation outcome AFTER that change: status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=mixing_declaration_error, wolfram_aborted, compile_seconds=5.7

## For reference — the ORIGINAL model's outcome before any repair:
status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=mixing_declaration_error, selfconjugate_quantum_numbers, wolfram_aborted, compile_seconds=5.4
