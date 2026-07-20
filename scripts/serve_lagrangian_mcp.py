#!/usr/bin/env python3
"""
# serve_lagrangian_mcp.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Serve HEPTAPOD tools (including the Lagrangian-extraction pipeline) over MCP.

This is a thin, toolkit.yaml-driven stdio MCP host: it reads toolkit.yaml,
imports every registered tool whose Python dependencies are installed, fills
their StateFields from config.py (or env/defaults), and serves them via
orchestral.mcp.server.MCPServer. Tools whose optional deps are missing (e.g.
`pdg`, `numpy`, `feyngraph`) are skipped with a note to stderr rather than
taking down the whole server — so the pure-python extraction pipeline
(literature / extract / frgen / validate / logging) serves even on a minimal
install.

Requires: `pip install mcp` (the MCP transport SDK).

Register with Claude Code:
    claude mcp add --scope user heptapod-lagrangian -- \\
        /path/to/heptapod/.venv/bin/python \\
        /path/to/heptapod/scripts/serve_lagrangian_mcp.py

Register with Codex:
    codex mcp add heptapod-lagrangian -- \\
        /path/to/heptapod/.venv/bin/python \\
        /path/to/heptapod/scripts/serve_lagrangian_mcp.py

Inspect without an MCP client:
    python scripts/serve_lagrangian_mcp.py --list
    python scripts/serve_lagrangian_mcp.py --only literature,extract,frgen,validate,logging --list
"""

from __future__ import annotations

import argparse
import importlib
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# StateFields the host knows how to fill (mirrors toolkit.yaml `config:`).
_STATE_KEYS = (
    "base_directory",
    "feynrules_path",
    "wolframscript_path",
    "mg5_path",
    "cache_enabled",
    "blank_agent_cmd",
)

_DEFAULT_BLANK_AGENT_CMD = (
    "codex exec --sandbox read-only --skip-git-repo-check --model gpt-5.5 "
    "-c model_reasoning_effort=medium --output-last-message {output}"
)


def _load_config() -> dict:
    cfg = {
        "base_directory": os.environ.get("HEPTAPOD_BASE_DIR", os.getcwd()),
        "feynrules_path": "",
        "wolframscript_path": "",
        "mg5_path": "",
        "cache_enabled": False,
        # real default, not "" — _instantiate passes every _STATE_KEYS entry
        # found in model_fields, so an empty string would clobber the tool's
        # own StateField default.
        "blank_agent_cmd": _DEFAULT_BLANK_AGENT_CMD,
    }
    try:
        import config as _c  # user's gitignored config.py at repo root
        for k in list(cfg):
            if hasattr(_c, k) and getattr(_c, k) is not None:
                cfg[k] = getattr(_c, k)
    except Exception:  # noqa: BLE001 — config.py is optional
        pass
    for k in ("feynrules_path", "wolframscript_path", "mg5_path", "blank_agent_cmd"):
        v = os.environ.get(k.upper())
        if v:
            cfg[k] = v
    return cfg


def _read_tool_specs() -> list:
    import yaml

    data = yaml.safe_load((REPO_ROOT / "toolkit.yaml").read_text())
    return data.get("tools", [])


def _bundles(spec: dict) -> list:
    b = spec.get("bundle")
    if isinstance(b, list):
        return b
    return [b] if b else []


def _instantiate(spec: dict, cfg: dict):
    mod = importlib.import_module(spec["module"])
    cls = getattr(mod, spec["name"])
    fields = getattr(cls, "model_fields", {})
    kwargs = {k: cfg[k] for k in _STATE_KEYS if k in fields}
    return cls(**kwargs)


def build_tools(cfg: dict, only: set | None):
    tools, skipped = [], []
    for spec in _read_tool_specs():
        if only and not (only & set(_bundles(spec))):
            continue
        try:
            tools.append(_instantiate(spec, cfg))
        except Exception as e:  # noqa: BLE001 — skip tools with missing deps
            first = (str(e).splitlines() or [""])[0]
            skipped.append((spec["name"], type(e).__name__, first))
    return tools, skipped


def main() -> int:
    ap = argparse.ArgumentParser(description="Serve HEPTAPOD tools over MCP (stdio)")
    ap.add_argument("--only", help="comma-separated bundles to serve (default: all importable)")
    ap.add_argument("--name", default="heptapod-lagrangian", help="MCP server name")
    ap.add_argument("--list", action="store_true", help="print served/skipped tools and exit")
    args = ap.parse_args()

    cfg = _load_config()
    only = set(args.only.split(",")) if args.only else None
    tools, skipped = build_tools(cfg, only)

    print("=" * 60, file=sys.stderr)
    print(f"  HEPTAPOD MCP — {args.name}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"base_directory:    {cfg['base_directory']}", file=sys.stderr)
    print(f"feynrules_path:    {cfg['feynrules_path'] or '(unset)'}", file=sys.stderr)
    print(f"wolframscript_path:{cfg['wolframscript_path'] or ' (unset)'}", file=sys.stderr)
    print(f"serving {len(tools)} tools:", file=sys.stderr)
    for t in tools:
        print(f"  + {t.get_name()}", file=sys.stderr)
    if skipped:
        print(f"skipped {len(skipped)} (missing optional deps):", file=sys.stderr)
        for n, etype, msg in skipped:
            print(f"  - {n}: {etype}: {msg}", file=sys.stderr)

    if args.list:
        return 0

    from orchestral.mcp.server import MCPServer

    print("\nServer starting on STDIO... (Ctrl+C to stop)", file=sys.stderr)
    server = MCPServer(tools=tools, name=args.name, version="2.2.0")
    try:
        server.run()
    except KeyboardInterrupt:
        print("\nServer stopped.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
