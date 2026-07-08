"""
# lagrangian_extraction_demo.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Agentic Lagrangian Extraction demo.

Launches an Orchestral agent wired with the full literature-to-validated-model
pipeline: literature search (INSPIRE + arXiv) -> PDF fetch + text extraction ->
structured Lagrangian extraction -> FeynRules .fr generation -> UFO compilation
and MadGraph validation. Drop a BSM scenario into the chat (e.g. "Build and
validate a scalar leptoquark S1 ~ (3,1,-1/3) model") and let it run.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from dotenv import load_dotenv

load_dotenv(REPO_ROOT / ".env")

# Orchestral core.
from orchestral import Agent
from orchestral.tools import (
    RunCommandTool,
    RunPythonTool,
    WriteFileTool,
    ReadFileTool,
    EditFileTool,
    FileSearchTool,
    FindFilesTool,
    TodoWrite,
    TodoRead,
)
from orchestral.tools.hooks import TruncateOutputHook
# Default provider only; swap in Claude/Gemini/Groq or get_ollama/get_vllm/
# get_litellm below (each pulls its own optional SDK, so import lazily).
from orchestral.llm import GPT
from llm import get_ollama, get_vllm, get_litellm  # noqa: F401

# HEPTAPOD prompt + tools.
from prompts import LAGRANGIAN_EXTRACTION_PROMPT

# Literature retrieval (this project) + INSPIRE (existing).
from tools.inspire.inspire_tools import InspireSearchTool, InspirePaperTool
from tools.literature.literature_tools import (
    ArxivSearchTool,
    FetchPaperPDFTool,
    ExtractPaperTextTool,
)

# Extraction + generation (this project).
from tools.extract.extract_tool import ExtractLagrangianTool
from tools.frgen.frgen_tool import GenerateFeynRulesModelTool

# Validation chain (existing HEPTAPOD tools).
from tools.feynrules import FeynRulesToUFOTool
from tools.mg5 import MadGraphFromRunCardTool

from config import feynrules_path, mg5_path, wolframscript_path

import orchestral.ui.app.server as app_server

# Sandbox for all artifacts (PDFs, text, model JSON, .fr, UFO, audit trail).
base_directory = str(REPO_ROOT / "examples" / "lagrangian_extraction_sandbox")
Path(base_directory).mkdir(parents=True, exist_ok=True)

print("Using FeynRules path:", feynrules_path)
print("Using MG5 path:", mg5_path)
print("Using wolframscript path:", wolframscript_path)
print("Sandbox:", base_directory)

# PDG tools are optional (require the `pdg` package / bundle). Include them for
# spectrum / known-width cross-checks when available.
try:
    from tools.pdg.pdg_tool import PDGDatabaseTool, PDGSearchTool

    _pdg_tools = [
        PDGDatabaseTool(base_directory=base_directory),
        PDGSearchTool(base_directory=base_directory),
    ]
except Exception as _e:  # noqa: BLE001
    print(f"(PDG tools unavailable: {_e}; continuing without them)")
    _pdg_tools = []

tools = [
    # Core file/exec tools.
    RunCommandTool(base_directory=base_directory),
    RunPythonTool(base_directory=base_directory, timeout=1000),
    WriteFileTool(base_directory=base_directory),
    ReadFileTool(base_directory=base_directory, show_line_numbers=True),
    EditFileTool(base_directory=base_directory),
    FindFilesTool(base_directory=base_directory),
    FileSearchTool(base_directory=base_directory),
    # 1. Literature discovery.
    InspireSearchTool(base_directory=base_directory),
    InspirePaperTool(base_directory=base_directory),
    ArxivSearchTool(base_directory=base_directory),
    # 2. Full text.
    FetchPaperPDFTool(base_directory=base_directory),
    ExtractPaperTextTool(base_directory=base_directory),
    # 3. Extraction -> structured model.
    ExtractLagrangianTool(base_directory=base_directory),
    # 4. .fr generation.
    GenerateFeynRulesModelTool(base_directory=base_directory),
    # 5. Validation chain.
    FeynRulesToUFOTool(
        base_directory=base_directory,
        feynrules_path=feynrules_path,
        wolframscript_path=wolframscript_path,
    ),
    MadGraphFromRunCardTool(base_directory=base_directory, mg5_path=mg5_path),
    *_pdg_tools,
    # Planning.
    TodoRead(),
    TodoWrite(base_directory=base_directory),
]

hooks = [TruncateOutputHook(max_length=10000)]

# ============================================================ #
# Choose an LLM for the driving agent. The ExtractLagrangianTool
# uses its own provider (config.py; default Ollama) so extraction
# can run on a local open model regardless of this choice.
# ============================================================ #
LLM = GPT()          # or Claude(), Gemini(), Groq()
# LLM = get_ollama() # local/open model (uses config.py)
# LLM = get_vllm()   # self-hosted OpenAI-compatible server
# LLM = get_litellm()

# Demo addendum: keeps the live run on a single (cloud) LLM. If no local
# extraction model is configured, the driving agent extracts the Lagrangian
# itself into the FeynRulesModel JSON and calls GenerateFeynRulesModelTool
# directly instead of ExtractLagrangianTool (which spins its own provider) —
# so the whole run is visible in the UI and needs no Ollama.
DEMO_ADDENDUM = """

## Demo note
Keep the run tight and narrated. If a local extraction model is not configured,
do NOT call ExtractLagrangianTool: instead read the paper text yourself and
produce the FeynRulesModel JSON directly, then call GenerateFeynRulesModelTool
and ValidateModelTool. Announce each tool call in one short sentence before you
make it so the audience can follow the pipeline.
"""

agent = Agent(
    llm=LLM,
    tools=tools,
    tool_hooks=hooks,
    system_prompt=LAGRANGIAN_EXTRACTION_PROMPT + DEMO_ADDENDUM,
    debug=False,
)

if __name__ == "__main__":
    app_server.run_server(
        agent, host="127.0.0.1", port=8000, open_browser=True, max_tool_iterations=100
    )
