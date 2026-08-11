"""
# launch.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""

"""Launch a coding agent on the NDA tools (the MCP counterpart to nda_demo.py).

Usage:
    python examples/nda/launch.py --harness claude-code
    python examples/nda/launch.py --harness codex
    python examples/nda/launch.py --harness opencode
"""

# Setup repository path for imports
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'shared'))

from harness_launch import main

main(
    example='nda',
    bundles=['nda', 'pdg', 'mg5'],
    prompt_path=Path(__file__).resolve().parent / 'prompts' / 'system_prompt.md',
    sandbox_dir=Path(__file__).resolve().parent,
    mode='explorer',
    config_keys=['mg5_path'],
)
