"""
# launch.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""

"""Launch a coding agent on the EDA tools (the MCP counterpart to eda_demo.py).

Usage:
    python examples/eda/launch.py --harness claude-code
    python examples/eda/launch.py --harness codex
    python examples/eda/launch.py --harness opencode
"""

# Setup repository path for imports
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'shared'))

from harness_launch import main

main(
    example='eda',
    bundles=['eda', 'nda', 'pdg'],
    prompt_path=Path(__file__).resolve().parent / 'prompts' / 'system_prompt.md',
    sandbox_dir=Path(__file__).resolve().parent,
    mode='explorer',
    config_keys=['wolframscript_path'],
)
