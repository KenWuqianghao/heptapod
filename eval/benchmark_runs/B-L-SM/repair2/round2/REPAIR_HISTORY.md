# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Changed `model.fr` in place by renaming the internal Yukawa tensors `yM` and `ynu` to `YMR` and `YNU` throughout their parameter declarations and neutrino Yukawa terms, which should prevent FeynRules from exporting malformed UFO parameter names like `yM1x2 /. yM`. I also added `LScalarDiag` just before the final `LTot` assignment and included it in `LTot` to cancel the reported residual `H`/`H2` kinetic and mass mixing terms, keeping the declared scalar mass basis diagonal. I could not run the full validation locally because `wolframscript` cannot find a Wolfram kernel here and MadGraph is not on `PATH`.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=76.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=67.4
