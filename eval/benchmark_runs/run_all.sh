#!/usr/bin/env bash
# Drive Codex over each benchmark model sequentially (no API contention).
# Each run: research/read the local paper text -> generate a .fr via the
# heptapod MCP generator. Artifacts land in eval/benchmark_runs/<model>/.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$REPO/.venv/bin/python"
SERVE="$REPO/scripts/serve_lagrangian_mcp.py"

for m in SLQrules SMScalars Sextets; do
  HERE="$REPO/eval/benchmark_runs/$m"
  echo "======== $m ========"
  codex exec \
    --cd "$REPO" --sandbox workspace-write --skip-git-repo-check \
    --model gpt-5.5 \
    -c 'model_reasoning_effort="medium"' \
    -c 'approval_policy="never"' \
    -c "mcp_servers.heptapod.command=\"$PY\"" \
    -c "mcp_servers.heptapod.args=[\"$SERVE\",\"--only\",\"extract,frgen,logging,literature\"]" \
    -c "mcp_servers.heptapod.env.HEPTAPOD_BASE_DIR=\"$HERE\"" \
    --json -o "$HERE/codex_report.md" \
    "$(cat "$HERE/prompt.txt")" > "$HERE/codex_events.jsonl" 2>&1
  echo "  $m exit=$? ; generated:"; ls "$HERE/model/" 2>/dev/null || echo "  (no model/ dir)"
done
echo "ALL BENCHMARK RUNS DONE"
