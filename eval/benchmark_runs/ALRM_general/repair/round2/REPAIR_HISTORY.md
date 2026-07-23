# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: scalar flavor index ranges now use plain `Range[...]`, the scalar multiplets now declare their matching `Indices`, neutral self-conjugate `Zp`, `h0`, and `A0` no longer carry explicit `Q -> 0` quantum-number declarations, and the file now ends with `LTot := LSALRM + LFALRM + LYALRM + LeffALRM;`. These are technical FeynRules/UFO export fixes for the reported malformed indexed scalar vertices and self-conjugate quantum-number issue, without changing the fields, couplings, operator content, or parameter values. I could not rerun the full Wolfram validation here because `wolframscript` is present but has no configured kernel path.

Validation outcome AFTER that change: status=compile_timeout, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=compile_timeout, compile_seconds=900.0

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=37.1
