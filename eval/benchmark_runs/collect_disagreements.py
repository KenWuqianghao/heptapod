#!/usr/bin/env python3
"""
# collect_disagreements.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Collect every graded disagreement from the blank-slate reverse-check packages
into one reviewer document.

Each review package holds a `crosscheck.md` written by a fresh agent that
compared the blank-slate reconstruction against the paper. Near the end it
grades every disagreement as convention / substantive / cosmetic. The reports
are agent-authored markdown, so the section heading and the table columns vary
per model. This parser is deliberately tolerant:

- the section heading may be `## Disagreements and Checks`, `## Disagreements
  and Severity`, `## Disagreements to Check`, `## Disagreements and Human
  Checks`, or the bold-line form `**Disagreements And Checks**`;
- the body may be a markdown table or a bullet list;
- the table's first column may be `issue`, `disagreement`, or `item`;
- the severity word is found by column name, and if that fails, by scanning
  the row's cells.

Outputs, next to this file:
    CONVENTION_DISAGREEMENTS.md   reviewer document
    disagreements.json            same data, for the dashboard artifact

Usage:
    python eval/benchmark_runs/collect_disagreements.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
MD_OUT = HERE / "CONVENTION_DISAGREEMENTS.md"
JSON_OUT = HERE / "disagreements.json"

SEVERITIES = ("convention", "substantive", "cosmetic")

# `## Disagreements ...` or a bold line `**Disagreements ...**`
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6}\s*|\*\*)disagreement", re.I)
# any heading that closes the section
ANY_HEADING_RE = re.compile(r"^\s{0,3}(#{1,6}\s|\*\*[A-Z][^*]{2,}\*\*\s*$)")

# Theme tagging is keyword-based, so a physicist can regroup it by hand.
THEMES: list[tuple[str, tuple[str, ...]]] = [
    ("Overall sign / term ordering",
     ("sign", "opposite", "minus", "ordering", "order of fields")),
    ("Hermitian conjugation and complex phases",
     ("conjug", "h.c.", "hermitian", "complex", "phase", "dagger", "^*", "star")),
    ("Majorana / self-conjugate field convention",
     ("majorana", "self-conjugate", "n^c", "psi^c", "charge conjugat")),
    ("Normalisation and numeric factors",
     ("normali", "factor of", "1/2", "sqrt", "prefactor", "coefficient")),
    ("Chirality and projectors",
     ("chiral", "p_l", "p_r", "gamma_5", "gamma5", "left-handed", "right-handed")),
    ("Index, flavour and generation labels",
     ("index", "indices", "flavour", "flavor", "generation", "contraction")),
    ("Symbol naming and parameter labels",
     ("name", "label", "symbol", "notation", "denote")),
    ("Gauge, metric and derivative convention",
     ("gauge", "metric", "covariant derivative", "signature", "feynman gauge")),
]


def _split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_separator(line: str) -> bool:
    return bool(re.fullmatch(r"[\s|:\-]+", line.strip())) and "-" in line


def _classify(text: str) -> str:
    low = text.lower()
    for s in SEVERITIES:
        if s in low:
            return s
    return "unclassified"


def _theme(text: str) -> str:
    low = text.lower()
    for name, keys in THEMES:
        if any(k in low for k in keys):
            return name
    return "Other"


def _section(lines: list[str]) -> list[str]:
    """Lines of the disagreements section, empty if the report has none."""
    start = None
    for i, line in enumerate(lines):
        if HEADING_RE.match(line):
            start = i + 1
            break
    if start is None:
        return []
    out = []
    for line in lines[start:]:
        if ANY_HEADING_RE.match(line):
            break
        out.append(line)
    return out


BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d{1,2}[.)])\s+(.*)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
GRADE_PREFIX_RE = re.compile(r"^(?:\*\*)?(?:convention|substantive|cosmetic)\b[:\s*]*", re.I)
CHECK_RE = re.compile(
    r"(?:a human should check|human should check|check(?:\s+whether|\s+that|\s+the|\s+if))\b.*",
    re.I | re.S)


def _bullets(body: list[str]) -> list[str]:
    """Bullet items, each joined with its continuation lines."""
    items: list[str] = []
    current: list[str] | None = None
    for line in body:
        m = BULLET_RE.match(line)
        if m:
            if current:
                items.append(" ".join(current))
            current = [m.group(1).strip()]
        elif current is not None and line.strip():
            current.append(line.strip())
        elif current is not None and not line.strip():
            items.append(" ".join(current))
            current = None
    if current:
        items.append(" ".join(current))
    return [i for i in items if i]


def _parse_bullets(body: list[str]) -> list[dict]:
    rows: list[dict] = []
    for text in _bullets(body):
        sev = _classify(text)
        bold = BOLD_RE.search(text)
        issue = bold.group(1).strip() if bold else text.split(".")[0].strip()
        if _classify(issue) != "unclassified":
            # the first bold span was the grade, not the title
            issue = text.split("severity")[0].strip(" -—:*")
        issue = GRADE_PREFIX_RE.sub("", issue).strip(" -—:*")
        check_m = CHECK_RE.search(text)
        check = check_m.group(0).strip() if check_m else ""
        rows.append({"issue": issue, "severity": sev, "check": check,
                     "theme": _theme(text)})
    return rows


def parse_report(path: Path) -> list[dict]:
    """Graded rows from one crosscheck report."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    body = _section(lines)
    table = [ln for ln in body if ln.strip().startswith("|")]
    if not table:
        return _parse_bullets(body)

    header = _split_row(table[0])
    low_header = [h.lower() for h in header]
    sev_col = next((i for i, h in enumerate(low_header)
                    if "severity" in h or "verdict" in h or "grade" in h), None)
    check_col = next((i for i, h in enumerate(low_header)
                      if "check" in h or "action" in h or "note" in h), None)

    rows: list[dict] = []
    for line in table[1:]:
        if _is_separator(line):
            continue
        cells = _split_row(line)
        if not any(cells):
            continue
        issue = cells[0]
        if not issue or issue.lower() in ("issue", "disagreement", "item"):
            continue
        sev = "unclassified"
        if sev_col is not None and sev_col < len(cells):
            sev = _classify(cells[sev_col])
        if sev == "unclassified":
            # header names varied; fall back to scanning the whole row
            sev = _classify(" ".join(cells[1:]))
        check = cells[check_col] if check_col is not None and check_col < len(cells) else ""
        rows.append({"issue": issue, "severity": sev, "check": check,
                     "theme": _theme(issue + " " + check)})
    return rows


def _crosscheck_files() -> dict[str, Path]:
    """model -> crosscheck.md, searching review/ and review/*/."""
    found: dict[str, Path] = {}
    for model_dir in sorted(p for p in HERE.iterdir() if p.is_dir()):
        review = model_dir / "review"
        if not review.is_dir():
            continue
        hits = sorted(review.glob("crosscheck.md")) + sorted(review.glob("*/crosscheck.md"))
        if hits:
            found[model_dir.name] = hits[0]
    return found


def _reviewed_models() -> list[str]:
    """Models that have a review package at all (crosscheck run or not)."""
    return sorted(p.name for p in HERE.iterdir()
                  if p.is_dir() and (p / "review").is_dir())


def collect() -> dict:
    files = _crosscheck_files()
    per_model = {model: parse_report(path) for model, path in files.items()}
    missing = [m for m in _reviewed_models() if m not in files]
    counts = {s: 0 for s in SEVERITIES + ("unclassified",)}
    for rows in per_model.values():
        for r in rows:
            counts[r["severity"]] += 1
    return {
        "models_with_crosscheck": sorted(per_model),
        "models_without_crosscheck": missing,
        "counts": counts,
        "per_model": per_model,
    }


def _by_theme(data: dict, severity: str) -> dict[str, list[tuple[str, dict]]]:
    out: dict[str, list[tuple[str, dict]]] = {}
    for model, rows in sorted(data["per_model"].items()):
        for r in rows:
            if r["severity"] == severity:
                out.setdefault(r["theme"], []).append((model, r))
    return dict(sorted(out.items()))


def render(data: dict) -> str:
    c = data["counts"]
    n_cc = len(data["models_with_crosscheck"])
    n_missing = len(data["models_without_crosscheck"])
    L: list[str] = [
        "# Graded disagreements — agent reconstruction vs. paper",
        "",
        "Every model in this bundle passed the tool chain (FeynRules compile, "
        "Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import). "
        "That says the tools accept the model. It does not say the physics is "
        "right. To test the physics, a second fresh agent — which saw only the "
        "sanitized `.fr`, with no paper and no model name — reconstructed the "
        "Lagrangian in LaTeX. A third fresh agent then compared that "
        "reconstruction against the paper term by term and graded every "
        "difference.",
        "",
        "This file collects those grades across all models. The grades come "
        "from the agent, not from a physicist. **They are the question list, "
        "not the answer.**",
        "",
        "Grade meanings, as the cross-check agent used them:",
        "",
        "- **convention** — the two forms are probably the same physics written "
        "differently (sign convention, field ordering, `N` vs `N^c`). Confirm "
        "the convention, then dismiss.",
        "- **substantive** — a real difference in content. Read this one.",
        "- **cosmetic** — presentation only.",
        "- **unclassified** — the agent gave no grade this parser could read; "
        "treat as unreviewed.",
        "",
        "## Counts",
        "",
        "| grade | rows |",
        "|---|---:|",
        f"| convention | {c['convention']} |",
        f"| substantive | {c['substantive']} |",
        f"| cosmetic | {c['cosmetic']} |",
        f"| unclassified | {c['unclassified']} |",
        "",
        f"Parsed from {n_cc} cross-check reports.",
        "",
    ]

    if n_missing:
        L += [
            f"## {n_missing} models have no cross-check to report",
            "",
            "These models are in the bundle with a `.fr` and a `REVIEW.pdf`, but "
            "the reverse check did not finish, so their review package holds no "
            "term-by-term comparison. The cause was agent-transport failure "
            "during the run, not a physics result. Treat them as **not yet "
            "reviewed**:",
            "",
        ]
        L += [f"- `{m}`" for m in data["models_without_crosscheck"]]
        L.append("")

    order = [("convention", "Convention disagreements"),
             ("substantive", "Substantive disagreements"),
             ("cosmetic", "Cosmetic disagreements"),
             ("unclassified", "Ungraded rows")]
    for sev, title in order:
        if c[sev] == 0:
            continue
        L += [f"## {title} ({c[sev]})", ""]
        for theme, items in _by_theme(data, sev).items():
            L += [f"### {theme}", ""]
            for model, r in items:
                L.append(f"- **{model}** — {r['issue']}")
                if r["check"]:
                    L.append(f"  - *check:* {r['check']}")
            L.append("")

    L += [
        "## Per-model row counts",
        "",
        "| model | convention | substantive | cosmetic | unclassified |",
        "|---|---:|---:|---:|---:|",
    ]
    for model, rows in sorted(data["per_model"].items()):
        n = {s: sum(1 for r in rows if r["severity"] == s)
             for s in SEVERITIES + ("unclassified",)}
        L.append(f"| {model} | {n['convention']} | {n['substantive']} | "
                 f"{n['cosmetic']} | {n['unclassified']} |")
    L.append("")
    return "\n".join(L)


def main() -> int:
    data = collect()
    JSON_OUT.write_text(json.dumps(data, indent=1), encoding="utf-8")
    MD_OUT.write_text(render(data), encoding="utf-8")
    c = data["counts"]
    print(f"[disagreements] {len(data['models_with_crosscheck'])} reports parsed, "
          f"{len(data['models_without_crosscheck'])} without cross-check")
    print(f"[disagreements] convention={c['convention']} substantive={c['substantive']} "
          f"cosmetic={c['cosmetic']} unclassified={c['unclassified']}")
    print(f"[disagreements] wrote {MD_OUT.name}, {JSON_OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
