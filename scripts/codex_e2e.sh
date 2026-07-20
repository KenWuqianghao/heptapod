#!/usr/bin/env bash
# End-to-end agentic run: hand Codex the FULL problem — read the paper,
# extract the model, generate the .fr, validate through the real chain
# (FeynRules/Wolfram compile + physics checks + MadGraph import) using
# BACKGROUND JOBS so long runs never block, iterate until validation passes,
# then run the blank-slate reverse check and stop for human review.
#
# Runs Codex with --dangerously-bypass-approvals-and-sandbox. This is
# REQUIRED: Codex CLI 0.143.0 cancels MCP tool calls ("user cancelled MCP
# tool call") under every other mode, including --full-auto. Run this
# yourself in a terminal you trust; a supervised agent harness will refuse
# to launch Codex with approvals/sandbox off.
#
# Usage:
#   ./scripts/codex_e2e.sh <page|arxiv_id>
#     <page>      a model page from eval/benchmark_runs/db_candidates.json
#                 (its arxiv_id is looked up), e.g. HeavyN
#     <arxiv_id>  any arXiv id, e.g. 1603.04993
#
# Requires: `codex mcp add heptapod -- <repo>/.venv/bin/python
#           <repo>/scripts/serve_lagrangian_mcp.py` and a config.py with
#           feynrules_path / wolframscript_path / mg5_path set.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:?usage: codex_e2e.sh <page|arxiv_id>}"

ARXIV_ID="$(cd "$REPO" && python3 - "$TARGET" <<'PY'
import json, sys
target = sys.argv[1]
try:
    data = json.load(open("eval/benchmark_runs/db_candidates.json"))
    for c in data["candidates"]:
        if c["page"] == target:
            print(c["arxiv_id"]); break
    else:
        print(target)
except FileNotFoundError:
    print(target)
PY
)"

WD="$(mktemp -d "${TMPDIR:-/tmp}/codex_e2e.XXXXXX")"
mkdir -p "$WD/model"
echo "[e2e] target: $TARGET  arxiv: $ARXIV_ID"
echo "[e2e] workdir: $WD"

cat > "$WD/prompt.txt" <<EOF
You are running the FULL agentic Lagrangian-extraction pipeline with the
heptapod MCP tools. Your working directory is your sandbox; all tool paths
are relative to it. Record an audittrail event after each stage.

MISSION — from paper to a human-reviewable, validated FeynRules model:

1. FETCH: call arxivsource with arxiv_id="$ARXIV_ID". Read the LaTeX source
   it writes (text/${ARXIV_ID}_source.tex). Identify the BSM model: every new
   field (spin, SU(3)/SU(2)/U(1) reps and charges, masses), new parameters,
   and the new-physics Lagrangian terms.

2. GENERATE: build the FeynRulesModel JSON (schema: read tools/frgen/frmodel.py
   in the heptapod repo if needed — numbers as strings like "-1/3"; SM add-on
   => gauge_groups []; unique class_index per particle; self_conjugate=false
   for complex fields) and call generatefeynrulesmodel to render
   model/${ARXIV_ID}.fr.

3. VALIDATE — use BACKGROUND JOBS, never block on long calls:
     - submitjob with tool_name="validatemodel" and tool_args JSON
       {"model_path":"model/${ARXIV_ID}.fr","physics_checks":true,"madgraph_check":true}
     - it returns a job_id immediately. While it runs, KEEP WORKING: re-read
       the paper for anything you missed, double-check quantum numbers.
       Poll jobstatus(job_id=...) every ~60s; when state=done call
       jobresult(job_id=...) and read passed + checks[].
     - If passed=false: diagnose from the failing checks' detail text
       (Hermiticity => a non-self-conjugate term needs "+ HC[<term>]";
       MadGraph rejects undefined symbols, duplicate parameter names, and
       names that aren't valid Python identifiers), FIX the model, and
       resubmit. Up to 6 rounds.

4. REVERSE CHECK (after validation passes): submitjob with
   tool_name="reverselagrangian" and tool_args
   {"model_path":"model/${ARXIV_ID}.fr","action":"full","paper_tex_path":"text/${ARXIV_ID}_source.tex"}
   Poll to completion and read the result. This spawns an independent
   blank-slate instance that reconstructs the Lagrangian from the sanitized
   .fr alone and compares it against the paper.

5. STOP for the human. Your final message must contain:
   - the validation verdict and every repair you made (with the check that
     motivated it),
   - the reverse-check summary (any disagreements it flagged),
   - the ABSOLUTE path to the compiled review PDF reported by the
     reverselagrangian result (review_package, normally
     reverse/${ARXIV_ID}/REVIEW.pdf; REVIEW.md if PDF compilation failed),
   - the sentence: "Human review required — the physics verdict belongs to
     the reviewer."
   Do NOT declare the physics correct yourself.
EOF

HEPTAPOD_BASE_DIR="$WD" codex exec \
  --cd "$WD" --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox \
  --model gpt-5.5 -c 'model_reasoning_effort="medium"' \
  "$(cat "$WD/prompt.txt")"
rc=$?
echo "[e2e] codex exit: $rc"
echo "[e2e] review package (if reached): $WD/reverse/${ARXIV_ID}/REVIEW.pdf"
echo "[e2e] audit ledger: $WD/audit.json"
exit $rc
