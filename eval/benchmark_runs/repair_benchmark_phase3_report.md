# Repair-loop benchmark — failing models through the agentic self-correction loop

Each one-shot validation failure is re-validated, then handed to an isolated repair agent (codex exec, workspace-write sandbox, **no network, no reference files, no model name**) together with the real FeynRules/MadGraph error output; the harness re-validates after each edit, up to 3 rounds.

| Model | Round-0 tags | Rounds | Final | Round-by-round |
|---|---|---|---|---|
| ALRM_general | selfconjugate_quantum_numbers, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓K✓M✓G✗] → compile_timeout → compile_timeout → compile_timeout |
| HNLs | duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] |
| SLQrules | hermiticity_fail | 3 | fail_after_repair | compiled[H✗K✓M✓G✓] → compiled[H✗K✓M✓G✓] → compiled[H✗K✓M✓G✓] → compiled[H✗K✓M✓G✓] |
| pSPSS | mg5_import_fail, ufo_semantic_error, mg5_python_traceback, mg5_invalid_cmd | 1 | pass_repaired | compiled[H✓K✓M✓G✗] → PASS |

**Aggregate:** {"n_models": 4, "pass_oneshot": 0, "pass_repaired": 1, "fail_after_repair": 3, "agent_no_change": 0, "max_rounds": 3}
