# Route B — ask the agent to research the paper (Codex → HEPTAPOD MCP)

**One of two demo routes.** Route A
([`../demo_codex_excerpt`](../demo_codex_excerpt)): *we* supply the paper text.
Route B (this dir): the agent *researches* the paper itself via INSPIRE/arXiv,
then builds the model. Same tools, same deterministic generator, same
verification — two levels of autonomy.

A frontier coding-agent harness (**OpenAI Codex**, on the user's subscription) is
given only a goal — *"build a FeynRules model for the scalar leptoquark S1,
grounded in the literature"* — and the HEPTAPOD tools over **MCP**. With no
orchestration code, it **researches the literature** (INSPIRE + arXiv), reads a
real paper's source, extracts the model, generates a FeynRules `.fr` with the
deterministic generator, and records a provenance ledger — then reports.

## What the harness actually did

Full flight recorder: [`TRANSCRIPT.md`](TRANSCRIPT.md) — every reasoning step,
shell command, and MCP call with arguments + results. Summary:

- **18 MCP tool calls** — `Inspiresearch`×5, `Arxivsearch`×6, `Arxivsource`×1,
  `Inspirepaper`×1, `Generatefeynrulesmodel`×1, `Audittrail`×4 — plus 15 shell
  reads and 18 reasoning steps.
- **Real literature research (INSPIRE), with citation counts:**
  - Doršner et al., *Physics of leptoquarks…*, arXiv:1603.04993 — 766 cites
  - Buchmüller, Rückl, Wyler, *Leptoquarks in Lepton–Quark Collisions* — 999 cites
  - Dumont, Nishiwaki, Watanabe, *LHC constraints… S1…B anomaly*, arXiv:1603.05248 — 113 cites
  - Bigaran, Volkas, *Getting chirality right…*, arXiv:2002.12544 — 107 cites
- **A scholarly judgment:** picked Doršner et al. as canonical (modern review that
  explicitly lists `S1` and the `y_RR u_R^C S1 e_R` interaction), noting BRW is
  the older, more-cited foundational classification.
- **Read the source:** fetched arXiv:1603.04993's TeX via `Arxivsource` and caught
  a real convention subtlety — Doršner writes `S1 = (3̄, 1, 1/3)`, so the requested
  `S1 ~ (3, 1, −1/3)` is the conjugate → the Yukawa is implemented with `HC[S1]`.
- **Honesty:** `Arxivsearch` hit arXiv 429/timeout errors; the agent recorded that
  in the audit trail "rather than papering over it."

## Result (independently verified)

Generated [`model/S1_research.fr`](model/S1_research.fr) — accepted by the
generator on the first attempt. Re-parsed by HEPTAPOD's parser (not the generator):

```
$ ../../.venv/bin/python verify.py
  [PASS] parses · S1 present · Q=-1/3 · Colour · SelfConjugate→False · MS1 · yRR · HC[…] · no doubled operator
[OK] all checks passed
```

Provenance: [`audit.json`](audit.json) / [`audit.md`](audit.md) — 3 events
(search → extract → generate_fr), written via the `Audittrail` MCP tool.

## Files

| File | What it is |
|---|---|
| [`TRANSCRIPT.md`](TRANSCRIPT.md) | **The full log** — reasoning + every tool/MCP call (args + results) |
| [`codex_report.md`](codex_report.md) | Codex's own end-of-run summary (literature, model, .fr) |
| [`codex_events.jsonl`](codex_events.jsonl) | Raw `codex exec --json` event stream |
| [`model/S1_research.fr`](model/S1_research.fr) | The generated FeynRules model |
| [`audit.json`](audit.json) / [`audit.md`](audit.md) | Provenance ledger (via `Audittrail`) |
| [`text/1603.04993_source.tex`](text/) | Fetched source of the Doršner review |
| [`verify.py`](verify.py) / [`prompt.txt`](prompt.txt) | Independent verifier / the task given to Codex |

## Reproduce

```bash
cd examples/demo_codex_research
codex exec --cd ../.. --sandbox workspace-write --skip-git-repo-check \
  -c 'approval_policy="never"' \
  -c 'mcp_servers.heptapod.command="../../.venv/bin/python"' \
  -c 'mcp_servers.heptapod.args=["../../scripts/serve_lagrangian_mcp.py","--only","inspire,literature,extract,frgen,logging"]' \
  -c "mcp_servers.heptapod.env.HEPTAPOD_BASE_DIR=\"$(pwd)\"" \
  --json -o codex_report.md "$(cat prompt.txt)" | tee codex_events.jsonl
../../.venv/bin/python verify.py
```

Prereqs: `codex` CLI logged in; `pip install mcp` in the heptapod `.venv`; network
for INSPIRE/arXiv. Note: the INSPIRE keyword search needed a fix (general search,
not title-only — see `tools/inspire/query_builder.py`) for multi-token queries
like "scalar leptoquark S1" to return hits; that fix is included.
