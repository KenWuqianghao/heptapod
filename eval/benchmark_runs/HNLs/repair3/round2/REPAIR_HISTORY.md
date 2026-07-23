# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: fixed the `N4` mass declaration to use the existing `MassN4` parameter, added explicit sums over neutrino mass eigenstates in the `NR`/`NL` unphysical field definitions to prevent FeynRules internals from leaking into UFO Python, corrected the internal `yN` convention to match the declared heavy-neutrino rotation and remove off-diagonal mass residues, removed the unused `LagHeavyN` assignment, and added missing `HC[...]` conjugates for charged pseudoscalar, charged vector interaction, and semileptonic hadronic terms so `LTot` remains the final BSM-only assignment and is Hermitian. Static checks passed for balanced delimiters, final `LTot`, and absence of source-level leaked constructs; I could not run the full Wolfram validation because `wolframscript` has no configured kernel path in this environment.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=4276.7

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=380.2
