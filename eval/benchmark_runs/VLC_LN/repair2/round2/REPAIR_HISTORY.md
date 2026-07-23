# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: changed eta-prime’s UFO particle name from `eta'` to `etaP` to stop the generated Python string/object-name breakage, and replaced raw `Wi`/`FS[Wi]`/`FS[B]` usage in the exported electroweak scalar kinetic and anomaly terms with explicit physical-field component helpers for `W`, `Wbar`, `A`, and `Z`, preventing unevaluated `Wi` symbols from leaking into UFO vertices. `LTot` remains the final top-level assignment and still uses only defined BSM terms; I could not rerun the full validation because `wolframscript` is installed but has no configured Wolfram kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, compile_seconds=76.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=82.8
