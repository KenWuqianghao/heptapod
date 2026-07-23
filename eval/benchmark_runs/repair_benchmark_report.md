# Repair-loop benchmark — failing models through the agentic self-correction loop

Each one-shot validation failure is re-validated, then handed to an isolated repair agent (codex exec, workspace-write sandbox, **no network, no reference files, no model name**) together with the real FeynRules/MadGraph error output; the harness re-validates after each edit, up to 3 rounds.

| Model | Round-0 tags | Rounds | Final | Round-by-round |
|---|---|---|---|---|
| 331 | mixing_declaration_error, selfconjugate_quantum_numbers, wolfram_aborted | 3 | fail_after_repair | compile_failed → compile_failed → compile_failed → compiled[H✗K✓M✓G✗] |
| ALRM_general | selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓K✓M✓G✗] → compile_timeout → compile_failed → compile_timeout |
| EffLRSM | builtin_symbol_collision, selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 2 | pass_repaired | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → PASS |
| GeneralU1 | lag_symbol_undefined, fr_syntax_error, builtin_symbol_collision, selfconjugate_quantum_numbers | 3 | pass_repaired | compile_failed → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → PASS |
| HNLs | lag_symbol_undefined, fr_syntax_error, duplicate_particle_names, selfconjugate_quantum_numbers | 3 | fail_after_repair | compile_failed → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] |
| B-L-SM | builtin_symbol_collision, selfconjugate_quantum_numbers, hermiticity_fail, kinetic_terms_fail, mass_spectrum_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✗K✗M✗G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] |
| MDMmodel | duplicate_particle_names, selfconjugate_quantum_numbers, hermiticity_fail | 1 | pass_repaired | compiled[H✗K✓M✓G✓] → PASS |
| 368sextets | mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 2 | pass_repaired | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → PASS |
| SLQrules | lag_symbol_undefined, fr_syntax_error | 3 | fail_after_repair | compile_failed → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] |
| pSPSS | selfconjugate_quantum_numbers, hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] → compiled[H✗K✓M✓G✗] |
| MSSMD | duplicate_particle_names, selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback | 1 | pass_repaired | compiled[H✓K✓M✓G✗] → PASS |
| CHEIDI | selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] |
| VLC_LN | compile_timeout | 3 | fail_after_repair | compile_timeout → compiled[H✗K✓M✓G✗] → compiled[H✓K✓M✓G✗] → compiled[H✓K✓M✓G✗] |

**Aggregate:** {"n_models": 13, "pass_oneshot": 0, "pass_repaired": 5, "fail_after_repair": 8, "agent_no_change": 0, "max_rounds": 3}
