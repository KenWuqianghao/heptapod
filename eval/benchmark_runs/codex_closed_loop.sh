#!/usr/bin/env bash
# Codex closed-loop: the agent drives generate -> compile -> validate -> repair
# using the live heptapod MCP tools, reading each validatemodel result and
# editing the model until it passes (compile + Hermiticity/kinetic/mass +
# MadGraph import).
#
# Runs Codex with --dangerously-bypass-approvals-and-sandbox. This is REQUIRED:
# Codex CLI 0.143.0 cancels MCP tool calls ("user cancelled MCP tool call") under
# every other mode, including --full-auto (approval=never + workspace-write) — the
# bypass flag is the only one that lets the agent call the heptapod MCP write-tools
# unattended. Run this yourself in a terminal you trust; a supervised agent harness
# will refuse to launch Codex with approvals/sandbox off.
#
# Usage:
#   ./codex_closed_loop.sh demo          # seed a deliberately non-Hermitian S1 and let Codex fix it
#   ./codex_closed_loop.sh <Page>        # copy eval/benchmark_runs/<Page>/model/<Page>_gen.fr and let Codex repair it
#
# Requires: `codex mcp add heptapod -- <repo>/.venv/bin/python <repo>/scripts/serve_lagrangian_mcp.py`
# and a config.py with feynrules_path / wolframscript_path / mg5_path set.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
TARGET="${1:-demo}"
WD="$(mktemp -d "${TMPDIR:-/tmp}/codex_loop.XXXXXX")"
mkdir -p "$WD/model"

if [ "$TARGET" = "demo" ]; then
  # Seed a broken (non-Hermitian) S1: drop the Hermitian-conjugate Yukawa term.
  sed 's/L1YukRR := L1YukRRNonHC + HC\[L1YukRRNonHC\];/L1YukRR := L1YukRRNonHC;/' \
    "$REPO/tools/feynrules/test_files/models/S1_LQ_RR.fr" > "$WD/model/S1.fr"
  MODEL="model/S1.fr"
else
  cp "$REPO/eval/benchmark_runs/$TARGET/model/${TARGET}_gen.fr" "$WD/model/${TARGET}.fr" \
    || { echo "no such model: $TARGET"; exit 1; }
  MODEL="model/${TARGET}.fr"
fi

cat > "$WD/prompt.txt" <<EOF
You are debugging a FeynRules BSM model with the heptapod MCP tools available to you
(validatemodel, generatefeynrulesmodel, feynrulestoufo, and more). Wolfram/FeynRules and
MadGraph paths are configured server-side; you only pass run arguments.

The model is at $MODEL (relative to your working directory). GOAL: make it PASS validation,
using the tools' own output to guide every fix.

Loop up to 5 times:
  1. Call validatemodel with: model_path="$MODEL", physics_checks=true, madgraph_check=true.
  2. Read the returned JSON: "passed" and the "checks" array (name / passed / detail).
  3. If passed is true, STOP.
  4. Otherwise diagnose the failing check(s) from their detail text, EDIT $MODEL to fix, and repeat.

Physics notes:
  - A FeynRules Lagrangian must be Hermitian: a non-self-conjugate interaction term needs
    its Hermitian conjugate added as "+ HC[<term>]".
  - MadGraph rejects UFOs with undefined symbols, duplicate parameter names, or names that
    are not valid Python identifiers (e.g. a "\$" in a parameter name).
  - Change only what the failing checks require.

FINAL MESSAGE: number of validatemodel calls, each failing check + your diagnosis + the exact
edit you applied, and the final all-passed summary.
EOF

echo "[loop] working dir: $WD"
echo "[loop] target: $MODEL"
cd "$WD"
HEPTAPOD_BASE_DIR="$WD" codex exec \
  --cd "$WD" --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox \
  --model gpt-5.5 -c 'model_reasoning_effort="medium"' \
  "$(cat "$WD/prompt.txt")"
echo "[loop] done. Final model: $WD/$MODEL"
