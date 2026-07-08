#!/usr/bin/env bash
# run_demo.sh — Route B: ask the agent to RESEARCH a paper, then build the model.
#
# A frontier coding-agent harness (OpenAI Codex, using YOUR Codex subscription)
# is given only a goal — "build a FeynRules model for the scalar leptoquark S1,
# grounded in the literature" — plus the HEPTAPOD tools over MCP (INSPIRE + arXiv
# search, source fetch, the deterministic .fr generator, and the audit ledger).
# It searches the literature, reads a real paper's source, extracts the model,
# generates model/S1_research.fr, and records a provenance trail. Then run
# ./verify.py to independently check the output.
#
# Contrast with Route A (../demo_codex_excerpt) where we hand the agent the
# paper excerpt directly instead of asking it to find the paper.
#
# Usage:  ./run_demo.sh      Requires: codex CLI (logged in), `pip install mcp`, network for INSPIRE.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
PY="$REPO/.venv/bin/python"
SERVE="$REPO/scripts/serve_lagrangian_mcp.py"

rm -rf "$HERE/model" "$HERE/source" "$HERE/text" "$HERE"/audit.* 2>/dev/null || true

codex exec \
  --cd "$REPO" \
  --sandbox workspace-write \
  --skip-git-repo-check \
  -c 'approval_policy="never"' \
  -c "mcp_servers.heptapod.command=\"$PY\"" \
  -c "mcp_servers.heptapod.args=[\"$SERVE\",\"--only\",\"inspire,literature,extract,frgen,logging\"]" \
  -c "mcp_servers.heptapod.env.HEPTAPOD_BASE_DIR=\"$HERE\"" \
  --json \
  -o "$HERE/codex_report.md" \
  "$(cat "$HERE/prompt.txt")" | tee "$HERE/codex_events.jsonl"

echo
echo "=== Generated artifacts ==="
ls -1 "$HERE/model" "$HERE"/audit.* 2>/dev/null
echo
echo "Now verify independently:  $PY $HERE/verify.py"
