"""
# harness_launch.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""

"""Set up a sandbox and launch a coding agent against HEPTAPOD's tools.

The per-example `launch.py` scripts call `main()` with their bundles, prompt and
sandbox dir. This is the MCP counterpart to the Orchestral `*_demo.py` scripts:
same sandbox, same tools, same system prompt — the agent comes from the harness
instead of being built in Python.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Per-harness differences: the instruction file it reads, the `tb connect`
# target, and the command that starts it.
HARNESSES = {
    'claude-code': {'instructions': 'CLAUDE.md', 'command': 'claude'},
    'codex':       {'instructions': 'AGENTS.md', 'command': 'codex'},
    'opencode':    {'instructions': 'AGENTS.md', 'command': 'opencode'},
}


def _toolbase() -> str:
    """Locate the toolbase CLI, preferring the short `tb` alias."""
    for name in ('tb', 'toolbase'):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("toolbase not found on PATH. Install it with: pip install toolbase")


def _run(argv, cwd):
    """Run a toolbase command, surfacing its output only on failure."""
    r = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(argv)}\n{r.stdout}{r.stderr}")
    return r


def main(*, example, bundles, prompt_path, sandbox_dir, mode='explorer',
         config_keys=()):
    """Create a sandbox, wire a harness to HEPTAPOD's tools, and launch it.

    Args:
        example: short name, used in messages only.
        bundles: bundle names to activate, e.g. ['nda', 'pdg'].
        prompt_path: system prompt copied in as the harness's instruction file.
            Either one path, or a dict keyed by mode when the example ships a
            prompt per mode.
        sandbox_dir: directory the numbered sandbox is created under.
        mode: sandbox mode passed to create_new_sandbox.
        config_keys: heptapod config fields this example needs (e.g.
            'mg5_path'), read from the repo's config.py. Bundles gated on a
            key stay hidden until it is set, so this is what makes eda / mg5 /
            feynrules tools show up.
    """
    ap = argparse.ArgumentParser(description=f'Launch a coding agent on the {example} tools.')
    ap.add_argument('--harness', required=True, choices=sorted(HARNESSES),
                    help='which coding agent to wire up and start')
    ap.add_argument('--mode', default=mode, choices=('todo', 'plan', 'explorer'),
                    help='sandbox mode (default: %(default)s)')
    ap.add_argument('--no-launch', action='store_true',
                    help='set the sandbox up but do not start the agent')
    args = ap.parse_args()

    harness = HARNESSES[args.harness]
    tb = _toolbase()

    from sandbox_utils import create_new_sandbox
    sandbox = Path(create_new_sandbox(Path(sandbox_dir), mode=args.mode)).resolve()

    prompt = prompt_path[args.mode] if isinstance(prompt_path, dict) else prompt_path
    (sandbox / harness['instructions']).write_text(Path(prompt).read_text())
    print(f"  wrote {harness['instructions']} from {Path(prompt).name}")

    for b in bundles:
        _run([tb, 'activate', f'heptapod/{b}'], cwd=sandbox)
    print(f"  activated: {', '.join(bundles)}")

    # The system prompts name tools bare (EnumerateDiagrams), but toolbase
    # namespaces them as heptapod__* by default.
    # .toolbase/ already exists: tb activate created it above.
    (sandbox / '.toolbase' / 'serve.yaml').write_text('default:\n  bare: true\n')
    print('  wrote .toolbase/serve.yaml (bare tool names)')

    if config_keys:
        import config
        for key in config_keys:
            value = getattr(config, key, None)
            if not value:
                print(f"  skipped {key}: not set in config.py")
                continue
            _run([tb, 'config', 'set', 'heptapod', key, str(value)], cwd=sandbox)
            print(f"  set {key} = {value}")

    _run([tb, 'connect', args.harness], cwd=sandbox)
    print(f"  wired {args.harness}")

    if args.no_launch:
        print(f"\nSandbox ready: {sandbox}\nStart the agent with: cd {sandbox} && {harness['command']}")
        return

    cmd = shutil.which(harness['command'])
    if not cmd:
        sys.exit(f"\nSandbox ready at {sandbox}, but '{harness['command']}' is not on PATH. "
                 f"Install it, then run: cd {sandbox} && {harness['command']}")

    print(f"\nLaunching {harness['command']} in {sandbox.name} ...")
    os.chdir(sandbox)
    os.execvp(cmd, [cmd])
