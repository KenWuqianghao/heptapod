# Setup — Agentic Lagrangian Extraction (HEPTAPOD fork)

Branch: `feature/lagrangian-extraction`. Python 3.12 or 3.13 (a 3.14 venv works
for the pure-Python tools, but stick to 3.12/3.13 for the MC bundles).

## 1. Python environment

```bash
cd /Users/kenwu/Documents/Github/heptapod
python3.13 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt          # orchestral-ai + requests (base)

# This project's tool bundles:
pip install "jinja2>=3.1"  "pymupdf>=1.24"   # frgen (.fr generation) + literature (PDF)

# LLM providers (pick what you'll use for extraction; these came with orchestral-ai
# but install explicitly if missing): openai, anthropic, ollama, python-dotenv
pip install openai anthropic ollama python-dotenv

# Web UI (Orchestral run_server) — NOT pulled by the base install:
pip install fastapi uvicorn "websockets<13"

# Optional: PDG bundle for spectrum/known-width checks, Gemini provider
pip install "pdg>=0.2.0"
pip install google-genai        # only if you use the Gemini provider
```

Verify the tools load and pass their offline suites:

```bash
python test_runner.py --only literature
python test_runner.py --only frgen
python test_runner.py --only extract
python test_runner.py --only validate
python test_runner.py --only eval
```

## 2. `config.py`

```bash
cp config.example.py config.py     # config.py is gitignored
```

Edit `config.py`:

```python
# --- External HEP tools (validation / event generation) ---
# Verified on this machine:
wolframscript_path = "/Applications/Wolfram.app/Contents/MacOS/wolframscript"

# You must point these at YOUR installs (see §4 to obtain them):
feynrules_path = "/Users/kenwu/hep/FeynRules_v2.3.49"   # dir containing FeynRules.m + Models/
mg5_path       = "/Users/kenwu/hep/MG5_aMC_v3.6.6"       # dir containing bin/mg5_aMC

# --- LLM for extraction (ExtractLagrangianTool). Pick ONE path ---
# Local open model (recommended for reproducibility):
ollama_host  = None                 # localhost:11434
ollama_model = "gpt-oss:20b"        # or another pulled model
# Cloud instead: leave ollama as-is and set a key in .env (below), then run the
# demo with LLM = GPT() / Claude(); ExtractLagrangianTool defaults to Ollama, so
# pass llm_provider="litellm"/"vllm" or configure vllm_host/model to route cloud.
```

Then `.env` (also gitignored) for cloud keys:

```bash
cp .env.example .env
# edit:
# ANTHROPIC_API_KEY=sk-ant-...
# OPENAI_API_KEY=sk-...
```

## 3. Run it

**A) Orchestral web UI (recommended — this is the chat frontend):**

```bash
source .venv/bin/activate
python examples/workflows/lagrangian_extraction_demo.py
# opens http://127.0.0.1:8000 ; then type e.g.
#   "Build and validate a scalar leptoquark S1 ~ (3,1,-1/3) model, first generation."
```

**B) From a coding-agent harness (Claude Code / Codex) via MCP:**

```bash
# The MCP server currently lives under _legacy_mcp/
claude mcp add --scope user heptapod -- "$(pwd)/.venv/bin/python" "$(pwd)/_legacy_mcp/heptapod_server_stdio.py"
# then in Claude Code, load the system prompt:
cp prompts/examples/lagrangian_extraction/system/lagrangian_extraction_prompt.md CLAUDE.md
```

**C) Benchmark:**

```bash
EVAL_PROVIDER=ollama python eval/run_eval.py     # writes examples/eval_sandbox/eval_report.{json,md}
```

## 4. Obtaining FeynRules and MadGraph (if not already installed)

```bash
# FeynRules (needs Mathematica/Wolfram Engine — you have Wolfram.app):
#   https://feynrules.irmp.ucl.ac.be/  -> download FeynRules_v2.3.49, unzip, set feynrules_path
#   In the container/host, authenticate once: wolframscript -authenticate

# MadGraph5_aMC@NLO:
wget https://launchpad.net/mg5amcnlo/3.0/3.6.x/+download/MG5_aMC_v3.6.6.tar.gz
tar -xzf MG5_aMC_v3.6.6.tar.gz     # set mg5_path to the extracted dir
```

Once `config.py` points at real FeynRules + wolframscript, the **gated live
tests run for real**:

```bash
python tools/frgen/test_frgen.py --keep-files        # includes .fr -> UFO
python tools/validate/test_validate.py --keep-files  # live .fr -> UFO validation
```
