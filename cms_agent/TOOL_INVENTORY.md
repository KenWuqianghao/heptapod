# Tool inventory (linked ecosystem → CMS analysis steps)

Each entry names a **purpose**, **primary dependency**, **inputs/outputs**, and **failure modes**. Dependencies align with repositories or standards cited in HEPTAPOD’s README and common CMS + agentic stacks.

| Tool surface | Dependency / link | CMS mapping | Inputs → outputs | Failure modes |
| ------------ | ----------------- | ----------- | ---------------- | ------------- |
| `plan_workflow` | [Orchestral AI](https://orchestral-ai.com) (runtime referenced by HEPTAPOD) | Turn physics intent into reproducible steps | Natural language intent → structured run card (JSON) | Ambiguous selections; missing dataset era |
| `mcp_tool_bridge` | [Model Context Protocol](https://modelcontextprotocol.io) (see `examples/mcp/`) | Same tools for IDE assistants and batch runners | Schema-validated calls ↔ stdout/stderr + artifacts | Schema drift; long-running jobs timing out |
| `pdg_lookup` | `tools/pdg/` in this repo | SM parameters for generator cards | Particle name / PDG id → masses, widths | Unknown alias; stale local cache |
| `inspire_search` | `tools/inspire/` | Literature grounding for analysis notes | Query string → BibTeX snippets | Network/API errors |
| `kinematics_core` | `tools/analysis/kinematics.py` | Common HEP kinematics outside CMSSW | Four-vectors → ΔR, invariant mass | Unit mismatches (GeV vs MeV) |
| `cms_run_cmsDriver` | CMSSW (Docker image per GSoC sibling tasks) | Build cfg.py for RAW/RECO/AOD chains | Dataset key + era → `cmsDriver` command | Missing global tag; deprecated release |
| `cms_edm_audit` | CMSSW / EDMTools | Verify event counts & product consistency | ROOT/EDM file list → compliance report | Corrupt file; missing branch |
| `cms_histogram_task` | `coffea`, `hist`, `dask-awkward` | Prototype analysis without full framework | Parquet/awkward table → histogram JSON + PNG | Branch schema changes across datasets |
| `systematics_card_writer` | Human + templating | Record JES/JER/norm uncertainties | YAML template + measured stat → LaTeX/snippet | Manual formula mistakes |
| `repro_bundle_packager` | Idea from HEPTAPOD paper ([arXiv:2512.15867](https://arxiv.org/abs/2512.15867)) | Ship code + env + pins for reviewers | Git SHA + container digest → tarball | Non-reproducible random seeds |

## Adapter stubs

Python stubs under `cms_agent/tools/adapters/` document function signatures only; real installs belong in user-controlled environments (CVMFS, Apptainer, conda).
