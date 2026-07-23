# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: removed `QuantumNumbers` from the neutral self-conjugate fields `H2`, `H3`, `H0`, and `Zp`; changed all `Mix[...]` identifiers to strings as FeynRules requires; renamed numeric-leading SLHA block symbols `331INPUTS` and `331SCALAR` to valid Wolfram symbols; and added the required final `LTot := ...;` assignment using the BSM Lagrangian terms defined above it. I could not run the Wolfram validation locally because `wolframscript` is present but has no configured kernel path.

Validation outcome AFTER that change: status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=mixing_declaration_error, wolfram_aborted, compile_seconds=5.7

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` in place by adding the missing unphysical scalar triplet declarations for `rho`, `eta`, and `chi`, adding the non-SM Goldstone fields `G0p`, `GY`, and `GV` needed by the existing mixing declarations, changing the CP-even neutral mixing mass basis from undefined `h` to the SM Higgs class `H`, reformatting the mixing declarations with string identifiers intact, and renaming the dummy Lorentz index `rho` in `LGaugeSelf331` to `sig` so it no longer collides with the newly declared `rho` scalar multiplet. These are technical fixes for the reported FeynRules mixing/load abort while preserving the existing fields, charges, parameters, and operator terms.

Validation outcome AFTER that change: status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=mixing_declaration_error, wolfram_aborted, compile_seconds=5.5

## For reference — the ORIGINAL model's outcome before any repair:
status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=mixing_declaration_error, selfconjugate_quantum_numbers, wolfram_aborted, compile_seconds=5.4
