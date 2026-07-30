# S1 Leptoquark Simulation Pipeline

End-to-end simulation of pair-produced $S_1$ leptoquarks with right-handed
couplings: BSM model definition through event generation, showering, and
analysis.

## What this example does

The full chain, one agent driving it:

1. **FeynRules** — build the $S_1$ model and convert it to UFO
2. **MadGraph5** — generate parton-level $pp \to \mathrm{LQ}\,\mathrm{LQ}$ events
3. **Pythia / Sherpa** — shower, hadronize, cluster jets
4. **Analysis** — cuts, kinematics, resonance reconstruction, cutflows, yields

**Requires:** MadGraph5, and Mathematica with FeynRules for the model-building
step. See [External Dependencies](../../../README.md#external-dependencies).

## Quick start

### 1. Install the toolkit

```bash
pip install toolbase
tb install . --bundle feynrules --bundle mg5 --bundle event_gen --bundle analysis   # or plain `tb install .`
```

The `feynrules` and `mg5` bundles are gated on external software, so their
tools stay hidden until the paths are set — either in this repo's `config.py`
(which the launcher and demo both read) or with `tb config set`.

### 2. Serve the tools to your agent

```bash
python examples/sim/s1_lq_rr/launch.py --harness claude-code   # or codex, opencode
```

The launcher creates a numbered sandbox with the run cards from `template/`,
writes the system prompt as the file your harness reads, activates the bundles,
applies `config.py`'s external-software paths, and wires the MCP server — then
starts the agent in the sandbox. `--no-launch` stops after setup.

Under Orchestral instead, with a web UI on `http://127.0.0.1:8000`:

```bash
python examples/sim/s1_lq_rr/s1_lq_rr_demo.py
```

Both paths serve the same 23 tools from the same profile.

### 3. Pick a mode

`--mode` selects how much structure the agent is given:

| Mode | Sandbox contents | Prompt |
|------|------------------|--------|
| `explorer` (default) | run-card templates | interactive; waits for you |
| `plan` | run-card templates | agent writes its own plan first |
| `todo` | templates + `todos.md` | works a supplied task list |

## Layout

```
template/                 copied into each new sandbox
  feynrules/models/       S1_LQ_RR.fr
  madgraph/cards/         S1_LQ_RR_pp_lqlq_scan.mg5
  pythia/cards/           S1_LQ_RR_pp_ljlj.cmnd
todos/s1_lq/              task list for --mode todo
sandbox001/, sandbox002/  generated per run (gitignored)
```

## Bundles: `feynrules`, `mg5`, `event_gen`, `analysis`

| Tool | Purpose |
|------|---------|
| FeynRulesToUFO | BSM Lagrangian to UFO model |
| MadGraphFromRunCard | Parton-level generation |
| ValidateProcess | Fast process check before a full run |
| PythiaFromRunCard | Showering and hadronization |
| SherpaFromRunCard | Showering, alternative generator |
| JetClusterSlowJet | Particle-level jet clustering |
| LHEToJSONL / EventJSONLToNumpy / JetsJSONLToNumpy | Format conversion |
| CalculateInvariantMass / CalculateTransverseMomentum / CalculateDeltaR | Kinematics |
| ApplyCuts / FilterByPDGID / FilterByDeltaR / SortByPt | Event selection |
| GetHardestN / GetHardestNJets / MergeObjectCollections | Object handling |
| ResonanceReconstruction | Reconstruct the LQ candidates |
| Cutflow / NormalizeYield / RecastLinter | Selection bookkeeping and yields |

## Tutorial

`s1_lq_rr_tutorial.ipynb` walks the same pipeline cell by cell, with the agent
conversation inline.
