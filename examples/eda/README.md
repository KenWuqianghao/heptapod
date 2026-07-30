# EDA (Exact Diagrammatic Analysis) Example

Exact tree-level calculations via FeynCalc code generation and Mathematica.

## What this toolkit does

The EDA toolkit computes **exact symbolic partial decay widths and squared
amplitudes** for tree-level processes. It generates FeynCalc/Mathematica
scripts from a diagram specification, executes them via `wolframscript`, and
converts results to Python callables.

**Requires:** Mathematica with FeynCalc installed.

## Quick start

### 1. Install the toolkit and point it at Mathematica

From a clone of this repo (see the top-level [README](../../README.md) for the
full install story):

```bash
pip install toolbase
tb install . --bundle eda --bundle nda --bundle pdg   # or plain `tb install .` for every bundle

# The eda bundle is gated on wolframscript: its tools stay hidden until this
# is set, since they cannot run without it.
tb config set heptapod wolframscript_path /path/to/wolframscript
```

`tb install` builds an isolated environment for the toolkit and resolves each
bundle's dependencies into it — nothing lands in your own environment.

### 2. Serve the tools to your agent

The quickest path is the launcher, which does everything the manual steps below
do — creates a numbered sandbox, writes the system prompt as the file your
harness reads, activates the bundles, and wires the MCP server:

```bash
python examples/eda/launch.py --harness claude-code    # or codex, opencode
```

It replaces itself with the agent, so you land in a session already scoped to
the sandbox. Pass `--no-launch` to set the sandbox up and stop.

The rest of this section is what the launcher automates, if you would rather do
it by hand.

#### Claude Code

```bash
mkdir my_eda_session && cd my_eda_session

# Claude Code reads CLAUDE.md
cp ../prompts/system_prompt.md CLAUDE.md

tb activate heptapod/eda      # one item per invocation
tb activate heptapod/nda
tb activate heptapod/pdg

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
mkdir my_eda_session && cd my_eda_session

# Codex reads AGENTS.md
cp ../prompts/system_prompt.md AGENTS.md

tb activate heptapod/eda
tb activate heptapod/nda
tb activate heptapod/pdg
printf 'default:\n  bare: true\n' > .toolbase/serve.yaml

tb connect codex
codex                                                # type /mcp to confirm
```

OpenCode works the same way — `tb connect opencode` writes `opencode.json`.

#### Orchestral

```bash
python examples/eda/eda_demo.py
```

The demo pulls its tools through toolbase (so the bundle dependencies stay in
the toolkit environment) and launches a web UI on `http://127.0.0.1:8000`. The
tool set comes from the `eda-demo` profile in `.toolbase/profiles/`; edit that
file to change what the agent can reach. It takes `wolframscript_path` from
this repo's `config.py`, which also unlocks the gated `eda` bundle — so for the
demo path, setting it in `config.py` is enough on its own. Needs an LLM API key
— see [Configuration](../../README.md#configuration) — and orchestral's UI
extra:

```bash
pip install 'orchestral-ai[ui]'
```

## Bundles: `eda`, `nda`, `pdg`

Together these give the EDA symbolic tools with NDA cross-checks and PDG
reference values:

| Tool | Purpose |
|------|---------|
| ComputeSymbolicAmplitude | Generate FeynCalc script from diagram spec |
| RunWolframScript | Execute a Mathematica script |
| RunWolframScriptBatch | Execute multiple scripts concurrently |
| SimplifyResult | Apply substitutions, limits, simplifications |
| SimplifyResultBatch | Batch simplification |
| ConvertToPython | Convert symbolic result to Python callable |
| EstimateDecayWidthNDA | NDA cross-check |
| EstimateDecayWidthFormulaNDA | NDA formula cross-check |
| PDGDatabase | Reference experimental values |

## Worked example

See `task_prompt.md` for the prompt and `transcripts/` for the full
conversation and agent outputs. The system prompt used is at
`examples/eda/prompts/system_prompt.md`.

**Task:** Systematically compute all tree-level 1->2 decay widths across
spins {0, 1/2, 1}, all vertex types, both coupling bases (vector-axial
and chiral), with SM validation.

**Deliverables** (in `transcripts/sandbox/`):
- `summary/decay_catalog.pdf` -- Complete reference table of decay-width formulas
- `scripts/` -- 40 Wolfram scripts + result sidecars for each process
- `scripts/*.py` -- Python figure-generation scripts
- SM validation figures

**Session stats:** 73 minutes, 28.6 min LLM inference time.
