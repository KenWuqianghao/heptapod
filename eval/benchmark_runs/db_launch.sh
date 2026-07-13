#!/usr/bin/env bash
# Launch the DB benchmark fleet: one read-only Codex run per candidate model
# (gpt-5.5, medium effort), 3-way parallel. Resume-safe: models whose output
# already contains a fenced json block are skipped.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO"

run_one() {
  page="$1"
  HERE="$REPO/eval/benchmark_runs/$page"
  out="$HERE/codex_out.md"
  if [ -s "$out" ] && grep -q '```json' "$out"; then
    echo "[skip] $page (already extracted)"; return 0
  fi
  echo "[start] $page"
  codex exec \
    --cd "$REPO" --sandbox read-only --skip-git-repo-check \
    --model gpt-5.5 -c 'model_reasoning_effort="medium"' \
    -c 'approval_policy="never"' \
    --json -o "$out" \
    "$(cat "$HERE/prompt.txt")" > "$HERE/codex_events.jsonl" 2>&1
  rc=$?
  if grep -q '```json' "$out" 2>/dev/null; then echo "[done] $page"; else echo "[FAIL] $page (exit $rc)"; fi
}
export -f run_one
export REPO

python3 - <<'PY' | xargs -P 3 -I{} bash -c 'run_one "$@"' _ {}
import json, pathlib
p = pathlib.Path("eval/benchmark_runs/db_candidates.json")
for c in json.loads(p.read_text())["candidates"]:
    print(c["page"])
PY
echo "FLEET COMPLETE"
