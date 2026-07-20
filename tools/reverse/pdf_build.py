"""
# pdf_build.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Compile the reverse-check review package to a LaTeX PDF.

The review content is Markdown with embedded LaTeX math (the blank-slate
agent writes \\( \\) / \\[ \\] inline), so pandoc is the converter and a real
LaTeX engine (xelatex — Unicode-safe for agent-written prose) does the
typesetting. Binaries are resolved to absolute paths with fallbacks beyond
$PATH because the detached job runner inherits a minimal environment where
neither Homebrew's pandoc nor MacTeX's /Library/TeX/texbin may be visible.

compile_review_pdf never raises: a missing converter or a LaTeX failure is
reported in the returned dict and the Markdown source remains authoritative.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from typing import Optional

# Searched after $PATH; covers Homebrew (Apple Silicon + Intel), MacTeX and
# common Linux TeX Live installs.
_FALLBACK_DIRS = (
    "/opt/homebrew/bin",
    "/usr/local/bin",
    "/Library/TeX/texbin",
    "/usr/local/texlive/bin",
)


def _find_binary(name: str) -> Optional[str]:
    """Absolute path of ``name`` from $PATH, then the fallback dirs."""
    found = shutil.which(name)
    if found:
        return found
    for d in _FALLBACK_DIRS:
        cand = os.path.join(d, name)
        if os.path.isfile(cand) and os.access(cand, os.X_OK):
            return cand
    return None


def compile_review_pdf(
    md_path: str,
    pdf_path: Optional[str] = None,
    timeout_sec: int = 300,
    pandoc: Optional[str] = None,
    engine: Optional[str] = None,
) -> dict:
    """Compile ``md_path`` to ``pdf_path`` (default: same stem, .pdf).

    Returns ``{"ok", "pdf_path", "pandoc", "engine", "seconds", "error"}``.
    ``pandoc``/``engine`` args override binary discovery (used by tests).
    """
    t0 = time.time()
    pdf_path = pdf_path or os.path.splitext(md_path)[0] + ".pdf"

    def _fail(msg: str) -> dict:
        return {"ok": False, "pdf_path": None, "pandoc": pandoc,
                "engine": engine, "seconds": round(time.time() - t0, 1),
                "error": msg}

    if not os.path.isfile(md_path):
        return _fail(f"markdown source not found: {md_path}")
    pandoc = pandoc or _find_binary("pandoc")
    if not pandoc or not os.path.isfile(pandoc):
        return _fail("pandoc not found (install: brew install pandoc)")
    engine = engine or _find_binary("xelatex")
    if not engine or not os.path.isfile(engine):
        return _fail("xelatex not found (install MacTeX / TeX Live)")

    # tex_math_single_backslash: the agents write \( \) / \[ \] math, which
    # must parse as math (not raw text) inside table cells and prose.
    cmd = [
        pandoc, md_path, "-o", pdf_path,
        "--from", "markdown+raw_tex+tex_math_single_backslash+tex_math_dollars",
        "--pdf-engine", engine,
        "-V", "geometry:margin=2.2cm",
        "-V", "fontsize=10pt",
        "-V", "colorlinks=true",
        # Wrap long verbatim lines (FeynRules terms overflow the margin
        # otherwise). fvextra ships with MacTeX/TeX Live.
        "-V", "header-includes=\\usepackage{fvextra}"
              "\\DefineVerbatimEnvironment{Highlighting}{Verbatim}"
              "{breaklines,breakanywhere,commandchars=\\\\\\{\\}}"
              "\\fvset{breaklines,breakanywhere}",
    ]
    env = dict(os.environ)
    env["PATH"] = os.pathsep.join(
        [os.path.dirname(engine), os.path.dirname(pandoc)]
        + env.get("PATH", "").split(os.pathsep)
    )
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout_sec, env=env,
        )
    except subprocess.TimeoutExpired:
        return _fail(f"pandoc/LaTeX timed out after {timeout_sec}s")
    except OSError as e:  # engine binary broken, etc.
        return _fail(f"failed to launch pandoc: {e}")

    if proc.returncode != 0 or not os.path.isfile(pdf_path):
        tail = (proc.stderr or proc.stdout or "").strip()[-500:]
        return _fail(f"pandoc exit {proc.returncode}: {tail}")
    return {"ok": True, "pdf_path": pdf_path, "pandoc": pandoc,
            "engine": engine, "seconds": round(time.time() - t0, 1),
            "error": None}
