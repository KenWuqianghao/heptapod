# Planner contract (stub)

The planner agent converts **physics intent** into a **directed acyclic workflow** of tool calls with:

1. **Inputs** — dataset identifiers, era, luminosity, object definitions.
2. **Tool allowlist** — subset of `cms_agent/TOOL_INVENTORY.md`.
3. **Acceptance checks** — e.g., event count stability, expected histogram integrals.
4. **Artifacts** — plots, trimmed ROOT/Parquet, run card JSON.

The planner must **refuse** to execute tools outside the allowlist and must attach **provenance** (model id, temperature, timestamps) to every run card.
