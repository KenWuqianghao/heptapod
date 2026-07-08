# Route A — hand over the excerpt (Codex → HEPTAPOD MCP)

**One of two demo routes.** Route A (this dir): *we* supply the paper text. Route B
([`../demo_codex_research`](../demo_codex_research)): the agent *researches* the
paper itself via INSPIRE/arXiv. Same tools, same deterministic generator, same
verification — two levels of autonomy.

A frontier coding-agent harness (**OpenAI Codex**, on the user's own subscription)
is handed a BSM paper excerpt and the HEPTAPOD physics tools over **MCP**. With no
custom orchestration code, it reads the `FeynRulesModel` schema, extracts the
model, calls the **deterministic** `Generatefeynrulesmodel` MCP tool to write a
FeynRules `.fr`, and records a provenance ledger via the `Audittrail` MCP tool.

This is the **license-free first half** of the pipeline (paper → structured model
→ `.fr`); the Mathematica/UFO/validation second half is not exercised here.

## What ran

- **Harness:** `codex exec` (Codex CLI 0.142.x), model = your Codex subscription's default.
- **Tools (over MCP):** served by [`scripts/serve_lagrangian_mcp.py`](../../scripts/serve_lagrangian_mcp.py)
  — `Generatefeynrulesmodel`, `Audittrail`, `Extractlagrangian`, plus literature tools.
- **Input:** the S1 scalar-leptoquark excerpt in [`prompt.txt`](prompt.txt).
- **Orchestration code written by us:** none. Codex plans and calls the tools itself.

## Result (verified)

Codex read the schema (`frmodel.py`, `render.py`, the reference `S1_LQ_RR.fr`),
built a schema-valid `FeynRulesModel`, and the generator accepted it on the
**first attempt** — no repair needed. Output: [`model/S1_codex.fr`](model/S1_codex.fr).

Independent verification (round-trips the `.fr` through HEPTAPOD's *parser*, not
the generator that wrote it):

```
$ ../../.venv/bin/python verify.py
  [PASS] file parses (round-trips through fr_parser)
  [PASS] S1 class present
  [PASS] electric charge Q = -1/3 (string-preserved)
  [PASS] colour triplet (Index[Colour])
  [PASS] complex scalar (SelfConjugate -> False)
  [PASS] distinct antiparticle (S1~)
  [PASS] mass parameter MS1
  [PASS] right-handed Yukawa coupling yRR
  [PASS] hermitian-conjugated Yukawa term (HC[...])
  [PASS] no doubled assignment operator
[OK] all checks passed — 10/10
```

## Why this matters (harness-agnostic thesis)

The same deterministic HEPTAPOD tools are driven here by Codex; they work
identically from Claude Code or Orchestral (any MCP client). The *harness's*
model does the reasoning and the repair loop; HEPTAPOD supplies deterministic,
physics-correct tools. Contrast on the same task:

| Harness brain | Generate attempts | `SelfConjugate` | Yukawa `yRR` | Result |
|---|---|---|---|---|
| **Codex (frontier)** | **1, no repair** | correct (`False`) | captured | correct `.fr`, 10/10 |
| Ollama `qwen2.5:14b` (local) | looped / partial | wrong (`True`) | missed | incomplete |

Frontier harness = high extraction fidelity; a small local model can do the
single-shot extraction but is unreliable as the *orchestrator*.

## Files

| File | What it is |
|---|---|
| [`prompt.txt`](prompt.txt) | The task handed to Codex |
| [`model/S1_codex.fr`](model/S1_codex.fr) | The generated FeynRules model (the artifact) |
| [`S1_codex_audit.json`](S1_codex_audit.json) / [`.md`](S1_codex_audit.md) | Provenance ledger (via `Audittrail` MCP tool) |
| [`codex_report.md`](codex_report.md) | Codex's own end-of-run summary |
| [`codex_events.jsonl`](codex_events.jsonl) | Full Codex event/tool-call transcript |
| [`verify.py`](verify.py) | Independent verifier (10 physics/round-trip checks) |
| [`run_demo.sh`](run_demo.sh) | One command to reproduce the whole run live |

## Reproduce / verify

```bash
# from this directory:
./run_demo.sh              # frontier harness re-runs the extraction → .fr
../../.venv/bin/python verify.py   # independent 10-point verification
```

Prereqs: `codex` CLI logged in; `pip install mcp` in the heptapod `.venv`.
The same pipeline is available to **Claude Code** — register the server with
`claude mcp add heptapod -- <venv>/python scripts/serve_lagrangian_mcp.py`.
