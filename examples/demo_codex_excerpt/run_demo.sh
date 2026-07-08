#!/usr/bin/env bash
# run_demo.sh — reproduce the agentic Lagrangian-extraction demo live.
#
# A frontier coding-agent harness (OpenAI Codex, using YOUR Codex subscription)
# is handed a BSM paper excerpt and the HEPTAPOD tools over MCP. It reads the
# FeynRulesModel schema, extracts the model, calls the DETERMINISTIC
# `Generatefeynrulesmodel` MCP tool to write a .fr, and records a provenance
# ledger via the `Audittrail` MCP tool. No Mathematica/UFO step (license-free
# first half). Then run ./verify.py to independently check the output.
#
# Usage:  ./run_demo.sh
# Requires: codex CLI (logged in), and `pip install mcp` in the heptapod venv.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
PY="$REPO/.venv/bin/python"
SERVE="$REPO/scripts/serve_lagrangian_mcp.py"

rm -rf "$HERE/model" "$HERE"/S1_codex_audit.* 2>/dev/null || true

codex exec \
  --cd "$REPO" \
  --sandbox workspace-write \
  --skip-git-repo-check \
  -c 'approval_policy="never"' \
  -c "mcp_servers.heptapod.command=\"$PY\"" \
  -c "mcp_servers.heptapod.args=[\"$SERVE\",\"--only\",\"extract,frgen,logging,literature\"]" \
  -c "mcp_servers.heptapod.env.HEPTAPOD_BASE_DIR=\"$HERE\"" \
  --json \
  -o "$HERE/codex_report.md" \
  "$(cat "$HERE/prompt.txt")" | tee "$HERE/codex_events.jsonl"

echo
echo "=== Generated artifacts ==="
ls -1 "$HERE/model" "$HERE"/S1_codex_audit.* 2>/dev/null
echo
echo "Now verify independently:  $PY $HERE/verify.py"
