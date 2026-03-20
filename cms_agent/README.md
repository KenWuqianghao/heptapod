# `cms_agent` — CMS-focused agent layout

This directory is a **scaffold** for agentic CMS analyses. It does **not** replace upstream `tools/`; it shows how to organize prompts, configs, workflows, and CMS-specific adapters when HEPTAPOD is used alongside a full reconstruction/analysis stack.

Unlike a pure sketch, the scaffold now includes:

- a minimal **working histogram adapter** for nano-like column mappings
- a **run-card schema** for validating planner outputs
- example **evaluation fixtures** so the proposal can be exercised without a full CMS software stack

## Layout

```
cms_agent/
├── README.md                 # (this file)
├── TOOL_INVENTORY.md         # Tool manifest tied to linked ecosystem repos
├── agents/                   # Planner / router contracts & stubs
├── workflows/                # Example workflow graphs and run-card templates
├── tools/                    # CMS adapter interfaces (call into CMSSW, coffea, etc.)
├── configs/                  # Model + tool allowlists + safety boundaries
├── knowledge/                # Curated CMS text snippets & RAG manifests
└── eval/                     # Golden tasks and regression prompts
```

## Consuming upstream HEPTAPOD tools

Reuse the existing packages under repository root `tools/` for cross-domain steps (PDG look-ups, literature via INSPIRE, unit conversions, generic `analysis/kinematics.py`). `cms_agent/tools/` should remain **thin**: validate inputs, call CMSSW/ROOT/coffea, normalize outputs to HEPTAPOD-friendly JSON or Apache Arrow batches.

## Safety

Agent-facing tools should declare **filesystem sandboxes**, **maximum runtime**, and **disallow arbitrary shell** unless explicitly enabled in `configs/*.yaml`.

## Minimal validation workflow

1. Build or receive a run card matching `workflows/run_card_schema.json`.
2. Restrict the agent to `configs/default_allowlist.yaml`.
3. Exercise at least one adapter locally, for example `tools/adapters/cms_histograms.py`, before wiring in heavier CMSSW or coffea dependencies.
