# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: fixed the `N4` mass declaration to use the existing `MassN4` parameter, added explicit sums over neutrino mass eigenstates in the `NR`/`NL` unphysical field definitions to prevent FeynRules internals from leaking into UFO Python, corrected the internal `yN` convention to match the declared heavy-neutrino rotation and remove off-diagonal mass residues, removed the unused `LagHeavyN` assignment, and added missing `HC[...]` conjugates for charged pseudoscalar, charged vector interaction, and semileptonic hadronic terms so `LTot` remains the final BSM-only assignment and is Hermitian. Static checks passed for balanced delimiters, final `LTot`, and absence of source-level leaked constructs; I could not run the full Wolfram validation because `wolframscript` has no configured kernel path in this environment.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=4276.7

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` to remove the failed `MassN4` alias path: `FR$RmDblExt` no longer remaps `MN4`, the unused internal `MassN4` parameter was removed, and the `N4` class mass now uses the existing external `MN4` directly so the UFO should not emit `value = MassN4`. I also kept the old gauge-basis Dirac block defined above but removed it from final `LTot`, replacing it with a mass-basis `LHeavyNMass := -MN4 N4bar.N4`; this preserves the heavy-neutrino mass while preventing unreduced `LLbar`/`Phibar` and FeynRules `PRIVATE` expressions from leaking into UFO Python. `LTot` remains the last top-level assignment, and I verified balanced delimiters plus no remaining `MassN4` references; full FeynRules validation could not be run because `wolframscript` still has no configured Wolfram kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=1842.0

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=380.2
