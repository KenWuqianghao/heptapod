# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Changed `model.fr` in place by renaming the internal Yukawa tensors `yM` and `ynu` to `YMR` and `YNU` throughout their parameter declarations and neutrino Yukawa terms, which should prevent FeynRules from exporting malformed UFO parameter names like `yM1x2 /. yM`. I also added `LScalarDiag` just before the final `LTot` assignment and included it in `LTot` to cancel the reported residual `H`/`H2` kinetic and mass mixing terms, keeping the declared scalar mass basis diagonal. I could not run the full validation locally because `wolframscript` cannot find a Wolfram kernel here and MadGraph is not on `PATH`.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=76.2

## Attempt 2
What was changed (the agent's own summary):
Changed `model.fr` to replace the problematic internal indexed Yukawa parameters `YMR` and `YNU` with explicit scalar internal component parameters (`YMR1x1` ... `YMR3x3`, `YNU1x1` ... `YNU3x3`) carrying the same formulas and zero entries, plus explicit `NP` interaction order. I then rewired `LNuYukNonHC` through local replacement rules so the operator structure is unchanged but FeynRules exports valid UFO identifiers instead of malformed Mathematica `ReplaceAll` names like `YMR1x2 /. YMR`. `LTot` remains the final top-level assignment. I did not run the full Wolfram/MadGraph validation because that would require tools outside the provided directory.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, compile_seconds=76.0

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=67.4
