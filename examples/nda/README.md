# NDA (Naive Dimensional Analysis) Example

Order-of-magnitude decay width and branching ratio estimation with automatic
diagram enumeration.

## What this toolkit does

The NDA toolkit provides **fast order-of-magnitude estimates** of partial
decay widths and cross sections using dimensional analysis and phase space
scaling. Combined with FeynGraph diagram enumeration, it can systematically
survey multi-body decay channels and rank them by importance.

**No external software required** -- runs with Python only.

## Quick start

### 1. Install the toolkit

From a clone of this repo (see the top-level [README](../../README.md) for the
full install story):

```bash
pip install toolbase
tb install . --bundle nda --bundle pdg --bundle mg5   # or plain `tb install .` for every bundle
```

`tb install` builds an isolated environment for the toolkit and resolves each
bundle's dependencies into it — nothing lands in your own environment.

### 2. Serve the tools to your agent

The quickest path is the launcher, which does everything the manual steps below
do — creates a numbered sandbox, writes the system prompt as the file your
harness reads, activates the bundles, and wires the MCP server:

```bash
python examples/nda/launch.py --harness claude-code    # or codex, opencode
```

It replaces itself with the agent, so you land in a session already scoped to
the sandbox. Pass `--no-launch` to set the sandbox up and stop.

The rest of this section is what the launcher automates, if you would rather do
it by hand.

#### Claude Code

```bash
mkdir my_nda_session && cd my_nda_session

# Claude Code reads CLAUDE.md
cp ../prompts/system_prompt.md CLAUDE.md

tb activate heptapod/nda      # one item per invocation
tb activate heptapod/pdg
tb activate heptapod/mg5

# Serve tool names un-namespaced, as the system prompt refers to them
printf 'default:\n  bare: true\n' > .toolbase/serve.yaml

tb connect claude-code                               # this directory's .mcp.json
claude                                               # type /mcp to confirm
```

The `serve.yaml` step matters: the system prompts refer to tools by their bare
names (`EnumerateDiagrams`), but toolbase namespaces them as
`heptapod__EnumerateDiagrams` by default. Without it the prompt describes tools
the agent cannot see under those names.

Add `-g` to `tb connect` to wire it user-level (`~/.claude.json`) instead, so
the tools are available in every session rather than just this directory.

#### OpenAI Codex

```bash
mkdir my_nda_session && cd my_nda_session

# Codex reads AGENTS.md
cp ../prompts/system_prompt.md AGENTS.md

tb activate heptapod/nda
tb activate heptapod/pdg
tb activate heptapod/mg5
printf 'default:\n  bare: true\n' > .toolbase/serve.yaml

tb connect codex
codex                                                # type /mcp to confirm
```

OpenCode works the same way — `tb connect opencode` writes `opencode.json`.

#### Orchestral

```bash
python examples/nda/nda_demo.py
```

The demo pulls its tools through toolbase (so the bundle dependencies stay in
the toolkit environment) and launches a web UI on `http://127.0.0.1:8000`. The
tool set comes from the `nda-demo` profile in `.toolbase/profiles/`; edit that
file to change what the agent can reach. Needs an LLM API key — see
[Configuration](../../README.md#configuration) — and orchestral's UI extra:

```bash
pip install 'orchestral-ai[ui]'
```

## Bundles: `nda`, `pdg`, `mg5`

Together these give NDA estimation with diagram enumeration, PDG reference
values, and optional MadGraph cross-checks:

| Tool | Purpose |
|------|---------|
| EstimateDecayWidthNDA | NDA width from a numerical diagram |
| EstimateDecayWidthFormulaNDA | NDA scaling formula (no numerics) |
| EstimateBranchingRatioNDA | Branching ratios from diagram classes |
| EstimatePhaseSpace | n-body phase space volume |
| EnumerateDiagrams | Auto-enumerate Feynman diagrams |
| VisualizeDiagrams | SVG/TikZ diagram rendering |
| PDGDatabase | Reference experimental values |
| PDGSearch | Search for particles by name |
| MadGraphFromRunCard | Exact cross-check (requires MadGraph) |

## Worked example

See `task_prompt.md` for the prompt and `transcripts/` for the full
conversation and agent outputs. The system prompt used is at
`examples/nda/prompts/system_prompt.md`.

**Task:** Determine the maximum number of $e^+e^-$ pairs in muon decay
observable at current/planned experiments, using diagram enumeration + NDA
scaling + MadGraph validation.

**Deliverables** (in `transcripts/sandbox/`):
- `summary/multipair_muon_decay.pdf` -- Complete analysis report
- `scripts/plot_*.py` -- Figure generation scripts
- `nda_br_summary_*.md` -- NDA branching ratio estimates per multiplicity
- `diagrams_*/` -- Representative diagrams per channel
- Figure PDFs: branching ratio scaling, diagram metadata, suppression analysis

**Session stats:** 64 minutes, 37.7 min LLM inference time.
