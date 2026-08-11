"""
# launch.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""

"""Launch a coding agent on the S1 leptoquark simulation pipeline (the MCP counterpart to s1_lq_rr_demo.py).

Usage:
    python examples/sim/s1_lq_rr/launch.py --harness claude-code
    python examples/sim/s1_lq_rr/launch.py --harness codex
    python examples/sim/s1_lq_rr/launch.py --harness opencode
"""

# Setup repository path for imports
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / 'examples' / 'shared'))

from harness_launch import main

main(
    example='s1_lq_rr',
    bundles=['feynrules', 'mg5', 'event_gen', 'analysis'],
    prompt_path={m: Path(__file__).resolve().parent / 'prompts' / f'{m}.md'
                 for m in ('explorer', 'plan', 'todo')},
    sandbox_dir=Path(__file__).resolve().parent,
    mode='explorer',
    config_keys=['feynrules_path', 'mg5_path', 'wolframscript_path'],
)
