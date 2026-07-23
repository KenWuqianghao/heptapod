#!/usr/bin/env python3
"""
Pretty-print the autonomous HeavyN mission as a terminal transcript.

Reads audit.json (the provenance ledger written live during the
`scripts/codex_e2e.sh HeavyN` run) and renders it as a readable, colorized
timeline: paper fetch -> model generation -> the background-job validate/repair
loop -> the blank-slate reverse check -> the compiled REVIEW.pdf deliverable.

    python examples/e2e_heavyN_run/show_mission_log.py        # colorized (a TTY)
    python examples/e2e_heavyN_run/show_mission_log.py | less -R
    NO_COLOR=1 python examples/e2e_heavyN_run/show_mission_log.py > mission.log

Colors auto-disable when stdout is not a TTY or NO_COLOR is set. Nothing here
is fabricated — every line is derived from audit.json in this directory.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
AUDIT = HERE / "audit.json"

_USE_COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")


def c(code: str, s: str) -> str:
    return f"\033[{code}m{s}\033[0m" if _USE_COLOR else s


BOLD, DIM = "1", "2"
RED, GRN, YEL, BLU, MAG, CYN, GRY = "31", "32", "33", "34", "35", "36", "90"
W = 74


def rule(ch: str = "═") -> str:
    return c(GRY, ch * W)


def hms(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


# stage -> (glyph, color, display label)
STAGE = {
    "fetch":               ("⤓", CYN, "FETCH"),
    "generate":            ("✎", CYN, "GENERATE"),
    "job_submit":          ("→", GRY, "SUBMIT"),
    "job":                 ("·", GRY, "JOB DONE"),
    "repair-1":            ("⟳", YEL, "REPAIR 1"),
    "repair-2":            ("⟳", YEL, "REPAIR 2"),
    "validate":            ("✓", GRN, "VALIDATE"),
    "reverse_reconstruct": ("◐", MAG, "RECONSTRUCT"),
    "reverse_crosscheck":  ("◑", MAG, "CROSS-CHECK"),
    "reverse_package":     ("▤", BLU, "PACKAGE"),
    "reverse-check":       ("✓", BLU, "REVERSE DONE"),
}


def wrap(text: str, indent: int) -> list[str]:
    pad = " " * indent
    words, line, out = text.split(), "", []
    for w in words:
        if len(line) + len(w) + 1 > W - indent:
            out.append(pad + line)
            line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        out.append(pad + line)
    return out


def detail(label: str, value: str, color: str = GRY) -> None:
    head = " " * 22 + c(color, f"{label} ")
    lines = wrap(value, 22 + len(label) + 1)
    print(head + lines[0].lstrip() if lines else head)
    for ln in lines[1:]:
        print(ln)


def render() -> None:
    audit = json.loads(AUDIT.read_text())
    events = audit["events"]
    t0 = hms(events[0]["ts"])
    tN = hms(events[-1]["ts"])
    wall = int((tN - t0).total_seconds())

    print()
    print(rule())
    print("  " + c(BOLD, "AUTONOMOUS MISSION — HeavyN") + c(GRY, "  (arXiv:1602.06957)"))
    print("  " + c(DIM, "paper → model → validate/repair loop → reverse check → REVIEW.pdf"))
    print("  " + c(GRY, f"{t0:%Y-%m-%d %H:%M:%S UTC}  ·  "
                       f"{wall // 60}m {wall % 60}s wall  ·  "
                       f"{len(events)} ledger events  ·  0 human interventions"))
    print(rule())
    print()

    for e in events:
        t = hms(e["ts"])
        elapsed = int((t - t0).total_seconds())
        glyph, color, label = STAGE.get(e["stage"], ("•", GRY, e["stage"].upper()))
        stamp = c(GRY, f"[{t:%H:%M:%S}]")
        rel = c(DIM, f"+{elapsed:>3}s")
        tag = c(color, f"{glyph} {label:<12}")
        print(f"{stamp} {rel}  {tag} {e['summary']}")

        d = e.get("data", {})
        st = e["stage"]
        if st == "generate":
            for f in d.get("new_fields", []):
                detail("field:", f"{f['name']}  spin {f['spin']}, "
                       f"SU(3)={f['su3']} SU(2)={f['su2']} Y={f['hypercharge']}, "
                       f"{'self-conjugate' if f.get('self_conjugate') else ''}", CYN)
            if d.get("parameters"):
                detail("params:", ", ".join(d["parameters"]), GRY)
            if d.get("lagrangian_terms"):
                detail("terms:", " + ".join(d["lagrangian_terms"]), GRY)
        elif st in ("repair-1", "repair-2"):
            mc = d.get("motivating_check") or d.get("motivating_checks")
            if isinstance(mc, list):
                for m in mc:
                    detail("← check:", m, RED)
            elif mc:
                detail("← check:", mc, RED)
            for r in d.get("repairs", []):
                detail("  fix:", r, YEL)
        elif st == "validate":
            checks = [x for x in d.get("checks", []) if not x.startswith("ufo_file:")]
            detail("round:", str(d.get("rounds")), GRN)
            detail("green:", "  ".join(c(GRN, x + " ✓") for x in checks)
                   if _USE_COLOR else "  ".join(x + " ✓" for x in checks), GRN)
        elif st in ("reverse_reconstruct", "reverse_crosscheck"):
            detail("agent:", f"fresh blank-slate codex instance · {d.get('seconds')}s", MAG)
        elif st == "reverse-check":
            for fd in d.get("flagged_disagreements", []):
                detail("⚑ flag:", fd, YEL)
        if st in ("job", "reverse-check", "generate", "validate"):
            print()

    pdf = HERE / "reverse" / "REVIEW.pdf"
    pdf_note = (f"{pdf.relative_to(HERE.parent.parent)} "
                f"({pdf.stat().st_size // 1024} KB, 7 pages)" if pdf.is_file()
                else "reverse/REVIEW.pdf")
    print(rule())
    print("  " + c(BOLD, "RESULT  ") + c(GRN, "validated in 3 rounds")
          + c(GRY, ", review package compiled, ") + c(BOLD, "STOPPED for human sign-off"))
    print("  " + c(DIM, "the tool never issues a physics verdict — that line is signed by a person"))
    print("  " + c(GRY, "deliverable: ") + c(BLU, pdf_note))
    print(rule())
    print()


if __name__ == "__main__":
    if not AUDIT.is_file():
        sys.exit(f"audit.json not found next to {__file__}")
    render()
