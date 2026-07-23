# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: fixed the `NR`/`NL` unphysical field definitions to explicitly sum over the four neutrino mass eigenstates, removed unused full-SM/Majorana assignments that could leak undefined or unintended symbols, made charged pseudoscalar/vector/semileptonic hadronic operators Hermitian with `HC[...]` while keeping charged vector kinetic/mass terms undoubled, and changed `LTot` to the BSM interaction piece only so the declared physical mass spectrum is not reintroduced as non-diagonal mass terms. Static checks pass for balanced Mathematica delimiters and `LTot` is the last top-level assignment; I could not rerun Wolfram validation here because `wolframscript` has no configured kernel path in this sandbox.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=402.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=264.2
