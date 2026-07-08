# Live Demo — Agentic Lagrangian Extraction (Orchestral UI)

**Goal:** show scientists what an agent *harness* is and how it drives real
physics tools — the agent reasons, calls tools, reads results, and repairs, all
visible in a ChatGPT-style UI. ~10 minutes.

## 0. Before the talk (do this the night before)

```bash
cd /Users/kenwu/Documents/Github/heptapod
source .venv/bin/activate
pip install "orchestral-ai[ui]"                 # FastAPI/uvicorn/websockets UI
pip install "jinja2>=3.1" "pymupdf>=1.24"       # our tool bundles
cp config.example.py config.py                  # then edit (below)
cp .env.example .env                            # add your API key
```

`config.py` — minimum for the demo:
```python
wolframscript_path = "/Applications/Wolfram.app/Contents/MacOS/wolframscript"
feynrules_path     = "/your/path/FeynRules_v2.3.49"   # optional for demo (see fallback)
mg5_path           = "/your/path/MG5_aMC_v3.6.6"      # optional for demo
ollama_model       = "gpt-oss:20b"                     # only if you keep ExtractLagrangianTool
```
`.env`: set `ANTHROPIC_API_KEY` (or `OPENAI_API_KEY`).

Driving LLM: open `examples/workflows/lagrangian_extraction_demo.py` and set
`LLM = Claude()` (or keep `GPT()`). The demo addendum makes the agent extract
the Lagrangian itself, so **you do NOT need Ollama running** — one cloud key
drives the whole thing.

**Smoke-test once, the night before:**
```bash
python examples/workflows/lagrangian_extraction_demo.py
# browser opens http://127.0.0.1:8000 ; run the scenario below once end-to-end.
```

## 1. Launch (at the talk)

```bash
source .venv/bin/activate
python examples/workflows/lagrangian_extraction_demo.py     # opens http://127.0.0.1:8000
```

## 2. The scenario (paste into the chat)

> Build and validate a FeynRules model for the **scalar leptoquark S1**, a color
> triplet, weak singlet with hypercharge giving electric charge **-1/3**, coupling
> a right-handed up quark to a right-handed charged lepton (first generation),
> mass 1500 GeV. Search the literature for the conventions, generate the `.fr`,
> validate it, and keep an audit trail.

(Scalar leptoquark is our tested case and ships as `S1_LQ_RR.fr`, so the output is
checkable live.)

## 3. What to narrate — the pipeline, tool by tool

As each tool call appears in the UI, point to it:

1. **`ArxivSearchTool` / `InspireSearchTool`** — "the agent searches the actual
   HEP literature — arXiv + INSPIRE — like a physicist would."
2. **`FetchPaperPDFTool` → `ExtractPaperTextTool`** — "it pulls the paper and
   reads the full text into its context."
3. **Extraction (agent reasoning → `FeynRulesModel` JSON)** — "here's the hard
   part nobody had automated: turning prose + equations into a *structured*
   Lagrangian — fields, quantum numbers like charge -1/3, couplings — with the
   schema guaranteeing it's well-formed."
4. **`GenerateFeynRulesModelTool`** — "deterministic Jinja2 turns that into a
   syntactically valid `.fr` file — the LLM never hand-writes Mathematica."
5. **`ValidateModelTool` (`.fr` → UFO)** — "and it *checks itself* against a real
   verifier — FeynRules/MadGraph — the deterministic ground truth."
6. **Repair loop** — if validation errors, "watch it read the concrete error and
   fix the model — this closed loop is why agent harnesses work for science."

**Harness capabilities to call out live** (the point of the demo):
- **Tool use** — every call + result is visible; the agent chooses tools.
- **Token/cost** — the UI tracks tokens and cost per run.
- **Intervention** — press **Esc to interrupt**; edit and resend to **steer**.
- **Provenance** — show the `audit.md` it writes: which paper, which
  conventions, which terms, and the validation result.
- **Model/harness-agnostic** — same tools run under Claude Code, Codex, or a
  local model; nothing is locked to one vendor.

## 4. Fallback (if FeynRules/Mathematica isn't ready)

The search → extract → **`.fr` generation** steps need only the cloud key and run
regardless. If `FeynRulesToUFOTool` can't compile (no Mathematica/FeynRules on
this machine), narrate: *"validation runs on our Fermilab/Mathematica machine;
here you see the generated `.fr` and the structural checks — the UFO compile is
the same tool HEPTAPOD already ships."* Then show the generated `.fr` file in the
UI (open it via the file tools) — it's the tangible artifact.

To rehearse the generation step deterministically without any LLM/UI:
```bash
python -c "import sys; sys.path.insert(0,'.'); \
from tools.frgen.test_frgen import _s1_model; from tools.frgen.render import render_model; \
print(render_model(_s1_model()))"
```

## 5. One-line framing for the audience

"A general agent harness + a handful of physics tools automates the
literature-to-simulation bottleneck — the agent finds the paper, extracts the
Lagrangian, writes the FeynRules model, and validates it against a real
verifier, with a full audit trail — and you can watch, stop, and steer it."
