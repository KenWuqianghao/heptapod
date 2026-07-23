# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: I replaced the broken component-only class block with FeynRules classes for the actual leptoquark multiplets used in the operators, added charge-component `ClassMembers` for the weak doublets/triplet, removed the invalid `HC[...]` and `HC[%]` placeholders by writing explicit Hermitian conjugates, renamed protected-style weak adjoint dummy indices away from `D/E/F`, rewrote the malformed quartic shorthand into explicit FeynRules expressions over declared fields, and changed the final assignment to the required `LTot := LQ2Phi + LQkin + LQf + LQ3Phi + LQ4Phi;`. I also confirmed statically that the original failure signatures (`HC[...]`, `HC[%]`, undefined `LBSM`, shorthand `Phia`/`Ya1` symbols, forbidden class-name collisions, and decay declarations) are gone; I could not run the full Wolfram/FeynRules chain here because `wolframscript` is installed but has no configured kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=514.6

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` in place by replacing the automatic `HC[...]` wrapper around the full fermion interaction block in `LQf` with explicit Hermitian-conjugate fermion chains using the conjugate fields and flipped chiral projectors. This preserves the same leptoquark operator content and parameters, but removes the reported `HC[ProjL]`/fermion-chain remnants that were corrupting UFO generation and should give the Hermiticity check explicit matching terms; `LTot` remains the final top-level BSM assignment. I could not run the full FeynRules validation locally because `wolframscript` still has no configured Wolfram kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=545.9

## For reference — the ORIGINAL model's outcome before any repair:
status=compile_failed, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=lag_symbol_undefined, fr_syntax_error, compile_seconds=6.1
