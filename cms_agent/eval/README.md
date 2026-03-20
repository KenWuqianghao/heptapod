# Evaluation harness

Suggested contents:

- **Golden prompts** — short user intents with expected tool sequences.
- **Numerical checks** — compare histogram integrals against reference Parquet fixtures.
- **Regression transcripts** — anonymized LLM transcripts committed after human redaction.

This folder now includes a tiny JSON fixture (`example_histogram_fixture.json`) that can be used to sanity-check the histogram adapter contract without requiring coffea, ROOT, or CMSSW.
