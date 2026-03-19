# `cms_agent` — CMS-focused agent layout

This directory is a **scaffold** for agentic CMS analyses. It does **not** replace upstream `tools/`; it shows how to organize prompts, configs, workflows, and CMS-specific adapters when HEPTAPOD is used alongside a full reconstruction/analysis stack.

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
