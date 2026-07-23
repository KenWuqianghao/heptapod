# Repair-loop benchmark — full analysis

One-shot agent-generated FeynRules models from the 28-model FeynRules-DB benchmark are pushed through the closed repair loop: full validation (FeynRules/Wolfram UFO compile → Hermiticity/kinetic/mass checks → MadGraph import) → isolated repair agent (codex exec, workspace-write sandbox, **network off, no reference files, no model name**) → re-validate, up to 3 rounds per phase. Later phases restart from the best earlier state with strictly better diagnostics:

- **Phase 1** — raw validation log tail + repair history.
- **Phase 2** — + per-check block extraction (head-first, so Hermiticity's offending vertices survive), + `py_compile` pinpointing of malformed UFO files, + the generated UFO visible in the agent workdir.
- **Phase 3** — + direct UFO import check (catches semantic leaks like `mass = Param.N4` vs `MN4` that MadGraph misreports), 1500 s compile budget.

## Pass-rate funnel (full chain: compile + all checks + MadGraph import)

| Stage | Models passing | Rate |
|---|---|---|
| one-shot | 15/28 | 54% |
| phase1 | 20/28 | 71% |
| phase2 | 24/28 | 86% |
| phase3 | 25/28 | 89% |

## Per-model progression (the 13 one-shot failures)

| Model | One-shot failure | P1 | P2 | P3 | Root cause(s) |
|---|---|---|---|---|---|
| 331 | compile_failed | fail | **PASS** (r2) | — | coupling named `e` = electron field under HC[] (Hermiticity); string-valued mixing declaration; symbolic benchmark values in UFO |
| ALRM_general | mg5 import | fail | fail | fail | multi-member scalar classes (ClassMembers) serialize to invalid UFO Python (2D-typeset exponents, PRIVATE`* leaks); restructure attempts re-break/time out the compile |
| EffLRSM | mg5 import | **PASS** (r2) | — | — | ClassName `N` Mathematica built-in collision; Q->0 on self-conjugate field; missing Generation index |
| GeneralU1 | compile_failed | **PASS** (r3) | — | — | stray parenthesis (syntax); ClassName `N` collision; M$InteractionOrderHierarchy syntax |
| HNLs | compile_failed | fail | fail | fail | syntax + duplicate names + Majorana QNs; coupling-orders Part[[..]] leak; SM-neutrino class collision; layered semantic UFO leaks (Mass->N4 vs MN4, NoUnfold[..] in index ranges, bare NP order) — each fixed when named, out of rounds before the stack emptied (open) |
| B-L-SM | checks | fail | **PASS** (r3) | — | ClassName `N` collision (caused herm/kin/mass fails); indexed Yukawa Value leaked `p /. ynu` parameter names into UFO; missing InteractionOrder on lambda2BL |
| MDMmodel | checks | **PASS** (r1) | — | — | duplicate SM Higgs declaration; zero QNs on self-conjugate real scalars |
| 368sextets | mg5 import | **PASS** (r2) | — | — | interaction-order bookkeeping (Part::partw) leaked into coupling_orders.py; InteractionOrder metadata on sextet couplings |
| SLQrules | compile_failed | fail | fail | fail | malformed component-only classes (syntax, line 660); eager FlavorExpand (timeouts); Sqrt[] mass leak; residual SU(2)-multiplet covariant-derivative Hermiticity violation (open) |
| pSPSS | checks | fail | fail | **PASS** (r1) | self-conjugate QNs; Hermiticity residual (cleared with vertex-level signal in P2); C-style float literals `1.000000e+02` leaked a bare `e` NameError into the UFO (found by import check, fixed in P3) |
| MSSMD | mg5 import | **PASS** (r1) | — | — | light Higgs ParticleName `h` collided with SM; self-conjugate QNs |
| CHEIDI | mg5 import | fail | **PASS** (r1) | — | `$` in symbol names (Heidi$v — legal WL, invalid Python UFO); non-numeric derived defaults |
| VLC_LN | compile_timeout | fail | **PASS** (r2) | — | index named `HC` collided with FeynRules HC[] (caused the >900s compile timeout); Phi/Phibar leakage; UFO syntax leak |

## Agent effort (all phases)

- Repair rounds executed: **63**
- Repair-agent wall time: **10.8 h** (validation compiles excluded)
- Total diff size: **2144 lines** across all attempts
- Codex tokens: **4,049,973**

## Error taxonomy

1. **Reliably repairable from the FeynRules log** — `.fr` syntax errors, undefined total-Lagrangian symbol, self-conjugate fields with quantum numbers, duplicate/SM-colliding particle names, interaction-order syntax, and above all **namespace collisions**: `ClassName -> N` (4 models), a coupling named `e` (electron field), an index named `HC` (Hermitian conjugate). The loop cleared every instance once the error text was in its report.
2. **UFO-serialization leaks** — WriteUFO silently emits unevaluated Wolfram expressions into UFO Python (ReplaceAll parameter names, `[[..]]` Part syntax, `PRIVATE`*` internals, 2D-typeset exponents, `$` in symbol names, `Sqrt[]` in masses, `mass = Param.X` with undefined X). FeynRules checks pass; MadGraph fails with a constant misleading message. Blind agents cannot fix these (phase 1: 0 fixed); with `py_compile` pinpointing + the UFO in the workdir + a direct-import check they become routine (phases 2-3).
3. **Hard physics residuals** — SU(2)-multiplet covariant-derivative Hermiticity violations (SLQrules). Vertex-level check output helps (pSPSS's cleared in phase 2) but does not guarantee convergence.
4. **Generator-structure defects** — multi-member `ClassMembers` scalar classes (ALRM_general) whose faithful restructuring exceeds the compile budget; best fixed deterministically in the .fr generator, not by the repair agent.

## Caveats

- The repair agent is isolated (no network, no references, anonymous model), but the underlying LLM may have seen the public FeynRules-DB models in training.
- Pass = the tool chain accepts the model; it does NOT certify the physics. Repaired models still need the blank-slate reverse check + human review (the pipeline's normal deliverable).
- Repairs that replace symbolic values with numerics (331, CHEIDI, SLQrules masses) preserve tool-chain validity but should be flagged to the reviewer; they narrow the model's parameter generality.
- One harness defect found and fixed mid-run: `subprocess.run(timeout=)` cannot kill orphaned Wolfram kernels (85 min hang); now a process-group kill.
