#!/usr/bin/env python3
"""
# repair_summary.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Merge the one-shot validation benchmark with all repair-benchmark phases into
REPAIR_BENCHMARK_ANALYSIS.md — the per-model progression, the pass-rate
funnel, agent-effort stats, and the error taxonomy.

Usage: python eval/benchmark_runs/repair_summary.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent

# Root causes established during the 2026-07-22 runs (verified by inspecting
# round logs, generated UFOs, and direct-import reproductions).
ROOT_CAUSE = {
    "331": "coupling named `e` = electron field under HC[] (Hermiticity); "
           "string-valued mixing declaration; symbolic benchmark values in UFO",
    "ALRM_general": "multi-member scalar classes (ClassMembers) serialize to "
                    "invalid UFO Python (2D-typeset exponents, PRIVATE`* leaks); "
                    "restructure attempts re-break/time out the compile",
    "EffLRSM": "ClassName `N` Mathematica built-in collision; Q->0 on "
               "self-conjugate field; missing Generation index",
    "GeneralU1": "stray parenthesis (syntax); ClassName `N` collision; "
                 "M$InteractionOrderHierarchy syntax",
    "HNLs": "syntax + duplicate names + Majorana QNs; coupling-orders Part[[..]] "
            "leak; SM-neutrino class collision; layered semantic UFO leaks "
            "(Mass->N4 vs MN4, NoUnfold[..] in index ranges, bare NP order) — "
            "each fixed when named, out of rounds before the stack emptied (open)",
    "B-L-SM": "ClassName `N` collision (caused herm/kin/mass fails); indexed "
              "Yukawa Value leaked `p /. ynu` parameter names into UFO; missing "
              "InteractionOrder on lambda2BL",
    "MDMmodel": "duplicate SM Higgs declaration; zero QNs on self-conjugate "
                "real scalars",
    "Monotops": "-", "pNG": "-", "Sextets": "-",
    "368sextets": "interaction-order bookkeeping (Part::partw) leaked into "
                  "coupling_orders.py; InteractionOrder metadata on sextet couplings",
    "SLQrules": "malformed component-only classes (syntax, line 660); eager "
                "FlavorExpand (timeouts); Sqrt[] mass leak; residual SU(2)-"
                "multiplet covariant-derivative Hermiticity violation (open)",
    "pSPSS": "self-conjugate QNs; Hermiticity residual (cleared with vertex-level "
             "signal in P2); C-style float literals `1.000000e+02` leaked a bare "
             "`e` NameError into the UFO (found by import check, fixed in P3)",
    "MSSMD": "light Higgs ParticleName `h` collided with SM; self-conjugate QNs",
    "CHEIDI": "`$` in symbol names (Heidi$v — legal WL, invalid Python UFO); "
              "non-numeric derived defaults",
    "VLC_LN": "index named `HC` collided with FeynRules HC[] (caused the >900s "
              "compile timeout); Phi/Phibar leakage; UFO syntax leak",
}

PHASES = [
    ("phase1", "repair_benchmark_report.json"),
    ("phase2", "repair_benchmark_phase2_report.json"),
    ("phase3", "repair_benchmark_phase3_report.json"),
]


def load(name: str):
    p = HERE / name
    return json.loads(p.read_text()) if p.is_file() else None


def agent_stats(res: dict) -> tuple[int, float, int]:
    runs = res.get("agent_runs") or []
    return (len(runs), sum(a.get("seconds") or 0 for a in runs),
            sum(a.get("diff_lines") or 0 for a in runs))


def codex_tokens(page: str, subdir: str) -> int:
    """Sum 'tokens used' from codex stdout logs of one phase's rounds."""
    tot = 0
    for f in sorted((HERE / page / subdir).glob("round*/codex_stdout.txt")):
        m = re.findall(r"tokens used\s*\n?\s*([\d,]+)", f.read_text(errors="replace"))
        if m:
            tot += int(m[-1].replace(",", ""))
    return tot


def main() -> int:
    oneshot = load("validation_benchmark_report.json")
    phases = {tag: load(fn) for tag, fn in PHASES}
    n_all = oneshot["aggregate"]["n_models"]
    oneshot_pass = [r["page"] for r in oneshot["rows"]
                    if r.get("status") == "compiled" and r.get("madgraph_import_ok")
                    and all(r.get("checks", {}).get(k) is True
                            for k in ("hermiticity", "kinetic_terms", "mass_spectrum"))]

    # Per-page progression over phases.
    prog: dict[str, dict] = {}
    for tag, rep in phases.items():
        if not rep:
            continue
        for res in rep["results"]:
            d = prog.setdefault(res["page"], {})
            d[tag] = res

    passed_by = {}   # page -> phase tag where it first passed
    for page, d in prog.items():
        for tag, _fn in PHASES:
            if tag in d and d[tag]["final_status"] == "pass_repaired":
                passed_by[page] = tag
                break

    funnel = [("one-shot", len(oneshot_pass))]
    cum = len(oneshot_pass)
    for tag, _fn in PHASES:
        if phases[tag]:
            cum += sum(1 for p, t in passed_by.items() if t == tag)
            funnel.append((tag, cum))

    lines = [
        "# Repair-loop benchmark — full analysis",
        "",
        "One-shot agent-generated FeynRules models from the 28-model FeynRules-DB "
        "benchmark are pushed through the closed repair loop: full validation "
        "(FeynRules/Wolfram UFO compile → Hermiticity/kinetic/mass checks → MadGraph "
        "import) → isolated repair agent (codex exec, workspace-write sandbox, "
        "**network off, no reference files, no model name**) → re-validate, up to 3 "
        "rounds per phase. Later phases restart from the best earlier state with "
        "strictly better diagnostics:",
        "",
        "- **Phase 1** — raw validation log tail + repair history.",
        "- **Phase 2** — + per-check block extraction (head-first, so Hermiticity's "
        "offending vertices survive), + `py_compile` pinpointing of malformed UFO "
        "files, + the generated UFO visible in the agent workdir.",
        "- **Phase 3** — + direct UFO import check (catches semantic leaks like "
        "`mass = Param.N4` vs `MN4` that MadGraph misreports), 1500 s compile budget.",
        "",
        "## Pass-rate funnel (full chain: compile + all checks + MadGraph import)",
        "",
        "| Stage | Models passing | Rate |",
        "|---|---|---|",
    ]
    for tag, n in funnel:
        lines.append(f"| {tag} | {n}/{n_all} | {n/n_all:.0%} |")

    lines += [
        "",
        "## Per-model progression (the 13 one-shot failures)",
        "",
        "| Model | One-shot failure | P1 | P2 | P3 | Root cause(s) |",
        "|---|---|---|---|---|---|",
    ]
    def cell(page, tag):
        d = prog.get(page, {})
        if tag not in d:
            return "—"
        res = d[tag]
        s = {"pass_repaired": f"**PASS** (r{res.get('rounds_used')})",
             "fail_after_repair": "fail",
             "agent_no_change": "no-change"}.get(res["final_status"], res["final_status"])
        return s
    oneshot_by_page = {r["page"]: r for r in oneshot["rows"]}
    for page in prog:
        r0 = oneshot_by_page.get(page, {})
        c = r0.get("checks", {})
        if r0.get("status") != "compiled":
            fail = r0.get("status", "?")
        elif not all(c.get(k) is True for k in ("hermiticity", "kinetic_terms", "mass_spectrum")):
            fail = "checks"
        else:
            fail = "mg5 import"
        lines.append(f"| {page} | {fail} | {cell(page,'phase1')} | {cell(page,'phase2')} | "
                     f"{cell(page,'phase3')} | {ROOT_CAUSE.get(page,'')} |")

    # Agent effort.
    tot_rounds = tot_sec = tot_diff = tot_tok = 0
    for tag, rep in phases.items():
        if not rep:
            continue
        sub = {"phase1": "repair", "phase2": "repair2", "phase3": "repair3"}[tag]
        for res in rep["results"]:
            n, s, d = agent_stats(res)
            tot_rounds += n; tot_sec += s; tot_diff += d
            tot_tok += codex_tokens(res["page"], sub)
    lines += [
        "",
        "## Agent effort (all phases)",
        "",
        f"- Repair rounds executed: **{tot_rounds}**",
        f"- Repair-agent wall time: **{tot_sec/3600:.1f} h** "
        f"(validation compiles excluded)",
        f"- Total diff size: **{tot_diff} lines** across all attempts",
        f"- Codex tokens: **{tot_tok:,}**" if tot_tok else "- Codex tokens: (not recorded)",
        "",
        "## Error taxonomy",
        "",
        "1. **Reliably repairable from the FeynRules log** — `.fr` syntax errors, "
        "undefined total-Lagrangian symbol, self-conjugate fields with quantum "
        "numbers, duplicate/SM-colliding particle names, interaction-order syntax, "
        "and above all **namespace collisions**: `ClassName -> N` (4 models), a "
        "coupling named `e` (electron field), an index named `HC` (Hermitian "
        "conjugate). The loop cleared every instance once the error text was in "
        "its report.",
        "2. **UFO-serialization leaks** — WriteUFO silently emits unevaluated "
        "Wolfram expressions into UFO Python (ReplaceAll parameter names, "
        "`[[..]]` Part syntax, `PRIVATE`*` internals, 2D-typeset exponents, `$` in "
        "symbol names, `Sqrt[]` in masses, `mass = Param.X` with undefined X). "
        "FeynRules checks pass; MadGraph fails with a constant misleading message. "
        "Blind agents cannot fix these (phase 1: 0 fixed); with `py_compile` "
        "pinpointing + the UFO in the workdir + a direct-import check they become "
        "routine (phases 2-3).",
        "3. **Hard physics residuals** — SU(2)-multiplet covariant-derivative "
        "Hermiticity violations (SLQrules). Vertex-level check output helps "
        "(pSPSS's cleared in phase 2) but does not guarantee convergence.",
        "4. **Generator-structure defects** — multi-member `ClassMembers` scalar "
        "classes (ALRM_general) whose faithful restructuring exceeds the compile "
        "budget; best fixed deterministically in the .fr generator, not by the "
        "repair agent.",
        "",
        "## Caveats",
        "",
        "- The repair agent is isolated (no network, no references, anonymous "
        "model), but the underlying LLM may have seen the public FeynRules-DB "
        "models in training.",
        "- Pass = the tool chain accepts the model; it does NOT certify the "
        "physics. Repaired models still need the blank-slate reverse check + "
        "human review (the pipeline's normal deliverable).",
        "- Repairs that replace symbolic values with numerics (331, CHEIDI, "
        "SLQrules masses) preserve tool-chain validity but should be flagged to "
        "the reviewer; they narrow the model's parameter generality.",
        "- One harness defect found and fixed mid-run: `subprocess.run(timeout=)` "
        "cannot kill orphaned Wolfram kernels (85 min hang); now a process-group "
        "kill.",
        "",
    ]
    out = HERE / "REPAIR_BENCHMARK_ANALYSIS.md"
    out.write_text("\n".join(lines))
    print(f"[summary] wrote {out}")
    print(json.dumps({"funnel": funnel, "passed_by": passed_by}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
