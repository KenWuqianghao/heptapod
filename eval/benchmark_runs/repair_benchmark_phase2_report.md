# Repair-loop benchmark — failing models through the agentic self-correction loop

Each one-shot validation failure is re-validated, then handed to an isolated repair agent (codex exec, workspace-write sandbox, **no network, no reference files, no model name**) together with the real FeynRules/MadGraph error output; the harness re-validates after each edit, up to 3 rounds.

| Model | Round-0 tags | Rounds | Final | Round-by-round |
|---|---|---|---|---|
| 331 | hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 2 | pass_repaired | compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → PASS |
| ALRM_general | selfconjugate_quantum_numbers, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓K✓M✓G✗] → compile_timeout → compile_failed → compile_timeout |
| HNLs | duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] |
| B-L-SM | mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | pass_repaired | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → PASS |
| SLQrules | hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✓] |
| pSPSS | selfconjugate_quantum_numbers, hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✓K✓M✓G✗] |
| CHEIDI | selfconjugate_quantum_numbers, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 1 | pass_repaired | compiled[H✓K✓M✓G✗] → PASS |
| VLC_LN | mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 2 | pass_repaired | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → PASS |

**Aggregate:** {"n_models": 8, "pass_oneshot": 0, "pass_repaired": 4, "fail_after_repair": 4, "agent_no_change": 0, "max_rounds": 3}
