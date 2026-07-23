#!/usr/bin/env python3
"""
# repair_benchmark.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Repair-loop benchmark: does the agentic self-correction loop turn one-shot
validation failures into passing models?

For each model page the harness re-runs the FULL validation chain
(FeynRules/Wolfram UFO compile + Hermiticity/kinetic/mass checks + MadGraph
import) on the agent-generated .fr, and on failure hands an ISOLATED repair
agent (codex exec, workspace-write sandbox, network off) a workdir containing
ONLY the failing model.fr and a VALIDATION_REPORT.md with the real tool
output — never the physicist's reference .fr, never the model/paper name in
the prompt. The agent edits model.fr in place; the harness re-validates.
Up to REPAIR_MAX_ROUNDS rounds (default 3).

This measures the same closed loop the e2e mission uses, at benchmark scale,
without the training-data confound (the HeavyN demo agent could consult the
cached reference; here the sandbox has nothing to consult).

Usage:
    python eval/benchmark_runs/repair_benchmark.py [page1,page2,...]
    python eval/benchmark_runs/repair_benchmark.py --failing   # all rows in
        validation_benchmark_report.json that do not pass the full chain

Outputs (durable, committable):
    eval/benchmark_runs/<page>/repair/round<N>/model.fr, VALIDATION_REPORT.md,
        codex_stdout.txt, codex_notes.md, compile.log, mg5.log
    eval/benchmark_runs/repair_benchmark_report.{json,md}
Scratch (UFO dirs, MG5 runs): $REPAIR_OUT (default /tmp/repair_bench).
"""

from __future__ import annotations

import difflib
import hashlib
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

os.environ.setdefault("VBENCH_COMPILE_TIMEOUT", "600")
os.environ.setdefault("VBENCH_OUT", os.environ.get("REPAIR_OUT", "/tmp/repair_bench"))

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE))

import validation_benchmark as vb  # noqa: E402
from tools.feynrules.wl_checks import _BLOCK_RE  # noqa: E402

MAX_ROUNDS = int(os.environ.get("REPAIR_MAX_ROUNDS", "3"))
AGENT_TIMEOUT = int(os.environ.get("REPAIR_AGENT_TIMEOUT", "1200"))
AGENT_CMD = shlex.split(os.environ.get(
    "REPAIR_AGENT_CMD",
    "codex exec --sandbox workspace-write --skip-git-repo-check "
    "--model gpt-5.5 -c model_reasoning_effort=medium",
))
OUTROOT = Path(os.environ["VBENCH_OUT"])
REPORT_JSON = HERE / "repair_benchmark_report.json"
REPORT_MD = HERE / "repair_benchmark_report.md"

REPAIR_PROMPT = """\
You are a FeynRules / Mathematica / MadGraph expert. This directory contains:

  - model.fr              : a FeynRules model file that FAILS the validation tool chain
  - VALIDATION_REPORT.md  : the exact failing output (FeynRules under Wolfram Engine, then MadGraph)
  - REPAIR_HISTORY.md     : (if present) previous repair attempts on this model and the
    validation outcome after each one. Do NOT repeat an approach that already failed;
    if a previous edit made the outcome worse (e.g. introduced a compile timeout),
    prefer reverting that change.
  - UFO/                  : (if present) the UFO the failing tool chain generated FROM
    this model.fr. Inspect it to diagnose MadGraph import failures — e.g. a Python
    syntax error in parameters.py/couplings.py/coupling_orders.py means some .fr
    declaration leaked an unevaluated Wolfram expression (a ReplaceAll `/.`, a `$` in a
    symbol name, Part `[[..]]` syntax, FeynRules-internal `PRIVATE` symbols) into the
    UFO. You must fix the CAUSE in model.fr — the UFO is regenerated from scratch each
    round, so never edit UFO/ files.

Fix model.fr IN PLACE so the tool chain passes:
  1. FeynRules WriteUFO produces a UFO (no $Aborted, no syntax errors, no undefined
     total-Lagrangian symbol);
  2. the FeynRules consistency checks pass: Hermiticity of the Lagrangian,
     correctly diagonalized/normalized kinetic terms, consistent mass spectrum;
  3. MadGraph `import model` of the generated UFO succeeds.

Hard rules:
  - Work ONLY from the files in this directory. Do not read files outside it and do not
    use the network.
  - Preserve the physics content: keep the fields, their quantum numbers, the operator
    structure, and parameter values. Fix TECHNICAL defects only, e.g.: FeynRules or
    Mathematica syntax errors; class/parameter names that collide with Mathematica
    built-ins (never use N, C, D, E, I, K, O as a ClassName or parameter); symbols used
    before they are defined; malformed class or parameter declarations; wrong or missing
    index declarations; a non-Hermitian Lagrangian missing its `+ HC[...]` conjugate (or
    double-counting one); self-conjugate (Majorana/real) fields declared with quantum
    numbers; duplicate ParticleName/AntiParticleName entries; mixing declarations whose
    identifier is not a string.
  - The total Lagrangian must be the LAST top-level assignment in the file, of the form
    `LTot := Lterm1 + Lterm2 + ...;`, built only from symbols defined above it. It is the
    BSM piece only — the tool chain adds the Standard Model Lagrangian itself.
  - Do not add particle Decay declarations.
  - If a check failure is inherently physical (e.g. Hermiticity genuinely violated by a
    term as extracted), make the minimal correction that restores consistency and note it.

When done, write a one-paragraph summary of exactly what you changed and why as your
final message.
"""


# ---------------------------------------------------------------- validation

def full_pass(row: dict) -> bool:
    c = row.get("checks", {})
    return bool(row.get("compile_ok")) and bool(row.get("madgraph_import_ok")) \
        and all(c.get(k) is True for k in ("hermiticity", "kinetic_terms", "mass_spectrum"))


def validate(page: str, fr: Path, round_no: int) -> dict:
    """Full chain on one .fr; mirrors validation_benchmark.run_one but for an
    arbitrary file path, and preserves the full logs next to the round dir."""
    row: dict = {"round": round_no, "fr": str(fr)}
    lag = vb.total_lag_symbol(fr)
    row["lag_symbol"] = lag
    if not lag:
        row.update({"compile_ok": False, "status": "no_lagrangian_symbol", "checks": {}})
        return row
    outdir = OUTROOT / page / f"round{round_no}" / "UFO"
    comp = vb.compile_to_ufo(page, fr, lag, outdir)
    row.update(comp)
    if comp["compile_ok"]:
        row["n_particles_ufo"] = vb.count_new_particles(outdir)
        mgdir = OUTROOT / page / f"round{round_no}" / "mg5run"
        row.update(vb.madgraph_import(outdir, mgdir))
        dbg = mgdir / "MG5_debug"
        row["mg5_debug_tail"] = dbg.read_text(errors="replace")[-3000:] if dbg.is_file() else ""
        row["status"] = "compiled"
        if not row.get("madgraph_import_ok"):
            row["ufo_syntax_errors"] = ufo_syntax_check(outdir)
            row["ufo_import_error"] = ufo_import_check(outdir)
        row["ufo_dir"] = str(outdir)
    else:
        row["status"] = "compile_timeout" if comp["timed_out"] else "compile_failed"
    row["compile_log"] = str(outdir.parent / "compile.log")
    row["full_pass"] = full_pass(row)
    row["error_tags"] = classify(row)
    return row


def ufo_import_check(outdir: Path) -> str | None:
    """Import the UFO exactly the way MadGraph does (UFO dir on sys.path) in a
    throwaway subprocess. Catches SEMANTIC leaks py_compile cannot — e.g. a
    particle declaring `mass = Param.N4` when parameters.py only defines MN4.
    MadGraph itself reports these as an unrelated constant line in
    object_library.py, so this is the only readable signal. Returns the
    traceback tail on failure, None on success."""
    code = (
        "import sys, traceback\n"
        f"d = {str(outdir)!r}\n"
        "sys.path = [d.rsplit('/', 1)[0], d] + sys.path\n"
        "try:\n"
        f"    __import__({outdir.name!r})\n"
        "    print('UFO-IMPORT-OK')\n"
        "except BaseException:\n"
        "    traceback.print_exc()\n"
    )
    try:
        p = subprocess.run([sys.executable, "-c", code], capture_output=True,
                           text=True, timeout=120)
        out = (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return "UFO import check timed out after 120 s"
    return None if "UFO-IMPORT-OK" in out else out[-1500:]


def ufo_syntax_check(outdir: Path) -> list[dict]:
    """Compile every generated UFO .py; report exact file/line/context of any
    Python syntax error (WriteUFO can leak unevaluated Wolfram expressions)."""
    errs = []
    for f in sorted(outdir.glob("*.py")):
        src = f.read_text(errors="replace")
        try:
            compile(src, f.name, "exec")
        except SyntaxError as e:
            lines = src.splitlines()
            lo, hi = max(0, (e.lineno or 1) - 3), min(len(lines), (e.lineno or 1) + 2)
            ctx = "\n".join(f"{i+1:5d} | {lines[i][:300]}" for i in range(lo, hi))
            errs.append({"file": f.name, "line": e.lineno, "msg": e.msg, "context": ctx})
    return errs


# ------------------------------------------------------------- error tagging

def classify(row: dict) -> list[str]:
    tags: list[str] = []
    log = ""
    lp = row.get("compile_log")
    if lp and Path(lp).is_file():
        log = Path(lp).read_text(errors="replace")
    c = row.get("checks", {})
    if row.get("status") == "no_lagrangian_symbol":
        tags.append("no_lagrangian_symbol")
    if row.get("timed_out"):
        tags.append("compile_timeout")
    if "is undefined in the model" in log:
        tags.append("lag_symbol_undefined")
    if re.search(r"\bSyntax::|\(line \d+ of ", log):
        tags.append("fr_syntax_error")
    if re.search(r"\b\w+::argt|PutIndices::NoIndexMath|Set::write|SetDelayed::write", log):
        tags.append("builtin_symbol_collision")
    if "MassDiag::" in log:
        tags.append("mixing_declaration_error")
    if "All particles should have different names" in log:
        tags.append("duplicate_particle_names")
    if "Selfconjugated fields should not carry quantumnumbers" in log:
        tags.append("selfconjugate_quantum_numbers")
    if "$Aborted" in log:
        tags.append("wolfram_aborted")
    if row.get("compile_ok"):
        if c.get("hermiticity") is False:
            tags.append("hermiticity_fail")
        if c.get("kinetic_terms") is False:
            tags.append("kinetic_terms_fail")
        if c.get("mass_spectrum") is False:
            tags.append("mass_spectrum_fail")
        if not row.get("madgraph_import_ok"):
            tags.append("mg5_import_fail")
            if row.get("ufo_syntax_errors"):
                tags.append("ufo_python_syntax_error")
            elif row.get("ufo_import_error"):
                tags.append("ufo_semantic_error")
            mg = (row.get("mg5_tail") or "") + (row.get("mg5_debug_tail") or "")
            if "Traceback" in mg:
                tags.append("mg5_python_traceback")
            if "InvalidCmd" in mg:
                tags.append("mg5_invalid_cmd")
    return tags


# ------------------------------------------------------------- repair agent

def build_report_md(row: dict, workdir: Path) -> str:
    c = row.get("checks", {})
    log = ""
    lp = row.get("compile_log")
    if lp and Path(lp).is_file():
        log = Path(lp).read_text(errors="replace")
    parts = [
        "# Validation report — model.fr FAILED the tool chain",
        "",
        f"- FeynRules UFO compile: {'OK' if row.get('compile_ok') else 'FAILED'}"
        + (" (TIMED OUT — the compile exceeded the time limit; the model may need "
           "simplification of redundant/expanded terms, without changing the physics)"
           if row.get("timed_out") else ""),
        f"- Hermiticity check: {c.get('hermiticity', 'not reached')}",
        f"- Kinetic-terms check: {c.get('kinetic_terms', 'not reached')}",
        f"- Mass-spectrum check: {c.get('mass_spectrum', 'not reached')}",
        f"- MadGraph import: {row.get('madgraph_import_ok', 'not reached')}",
        f"- Heuristic error tags: {', '.join(row.get('error_tags') or []) or 'none'}",
    ]
    # Each consistency-check block, head-first: FeynRules prints the offending
    # vertices/terms at the START of a block, so a blind tail loses the signal.
    for m in _BLOCK_RE.finditer(log):
        body = m.group("body").strip()
        clipped = body[:3500] + ("\n[... block truncated ...]" if len(body) > 3500 else "")
        parts += ["", f"## FeynRules check `{m.group('name')}` output", "```", clipped, "```"]
    parts += ["", "## FeynRules / Wolfram Engine output (tail)", "```",
              log[-5000:] or "(no compile log)", "```"]
    if row.get("compile_ok") and not row.get("madgraph_import_ok"):
        parts += ["", "## MadGraph import output (tail)", "```",
                  (row.get("mg5_tail") or "")[-4000:] or "(none)", "```"]
        if row.get("mg5_debug_tail"):
            parts += ["", "## MG5_debug (the real MadGraph error)", "```",
                      row["mg5_debug_tail"], "```"]
        for e in row.get("ufo_syntax_errors") or []:
            parts += ["", f"## UFO Python syntax error — `UFO/{e['file']}` line {e['line']}: "
                          f"{e['msg']}",
                      "This generated file is not valid Python, which is why MadGraph's "
                      "import fails. Find the .fr declaration that produced it and fix "
                      "THAT (the UFO is regenerated each round).",
                      "```", e["context"], "```"]
        if row.get("ufo_import_error"):
            parts += ["", "## UFO direct-import error (the REAL reason MadGraph rejects "
                          "this UFO — MadGraph's own message misreports the location)",
                      "Fix the .fr declaration that produced this; the UFO is "
                      "regenerated from model.fr each round.",
                      "```", row["ufo_import_error"], "```"]
    md = "\n".join(parts) + "\n"
    (workdir / "VALIDATION_REPORT.md").write_text(md)
    return md


def run_repair_agent(workdir: Path) -> dict:
    notes = workdir / "codex_notes.md"
    cmd = AGENT_CMD + ["--cd", str(workdir), "--output-last-message", str(notes),
                       REPAIR_PROMPT]
    t0 = time.time()
    stdout_path = workdir / "codex_stdout.txt"
    with open(stdout_path, "w") as fh:
        try:
            p = subprocess.Popen(cmd, stdout=fh, stderr=subprocess.STDOUT,
                                 stdin=subprocess.DEVNULL, start_new_session=True,
                                 cwd=str(workdir))
            rc = p.wait(timeout=AGENT_TIMEOUT)
            timed_out = False
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(p.pid), signal.SIGKILL)
            rc, timed_out = -9, True
    return {
        "exit": rc, "timed_out": timed_out,
        "seconds": round(time.time() - t0, 1),
        "notes": notes.read_text(errors="replace")[-2000:] if notes.is_file() else "",
    }


# ------------------------------------------------------------------ per page

def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _difflines(a: Path, b: Path) -> int:
    d = difflib.unified_diff(a.read_text(errors="replace").splitlines(),
                             b.read_text(errors="replace").splitlines(), lineterm="")
    return sum(1 for ln in d if ln[:1] in "+-" and ln[:3] not in ("+++", "---"))


def run_page(page: str, seed: Path | None = None, subdir: str = "repair") -> dict:
    src = seed or (HERE / page / "model" / f"{page}_gen.fr")
    result: dict = {"page": page, "seed": str(src), "rounds": [], "agent_runs": []}
    if not src.is_file():
        result["final_status"] = "missing_fr"
        return result
    rdir = HERE / page / subdir
    if rdir.exists():
        shutil.rmtree(rdir)

    def _round_dir(i: int) -> Path:
        d = rdir / f"round{i}"
        d.mkdir(parents=True, exist_ok=True)
        return d

    # round 0: the one-shot model, revalidated for reproducibility
    cur = _round_dir(0) / "model.fr"
    shutil.copy2(src, cur)
    row = validate(page, cur, 0)
    _persist_logs(row, cur.parent)
    result["rounds"].append(row)
    if row["full_pass"]:
        result["final_status"], result["rounds_used"] = "pass_oneshot", 0
        return result

    for i in range(1, MAX_ROUNDS + 1):
        wd = _round_dir(i)
        nxt = wd / "model.fr"
        shutil.copy2(cur, nxt)
        build_report_md(row, wd)
        _write_history(result, wd)
        ufo_src = row.get("ufo_dir")
        if ufo_src and Path(ufo_src).is_dir() and not row.get("madgraph_import_ok"):
            shutil.copytree(ufo_src, wd / "UFO", dirs_exist_ok=True)
        before = _sha(nxt)
        agent = run_repair_agent(wd)
        shutil.rmtree(wd / "UFO", ignore_errors=True)  # regenerated artifact; keep workdir lean
        agent["round"] = i
        agent["changed"] = _sha(nxt) != before
        agent["diff_lines"] = _difflines(cur, nxt) if agent["changed"] else 0
        result["agent_runs"].append(agent)
        if not agent["changed"]:
            result["final_status"] = "agent_no_change"
            result["rounds_used"] = i
            best = max(result["rounds"], key=_score)
            result["best_round"] = best["round"]
            result["best_round_summary"] = _round_summary(best)
            return result
        row = validate(page, nxt, i)
        _persist_logs(row, wd)
        result["rounds"].append(row)
        cur = nxt
        if row["full_pass"]:
            result["final_status"], result["rounds_used"] = "pass_repaired", i
            shutil.copy2(cur, rdir / "final.fr")
            return result

    result["final_status"], result["rounds_used"] = "fail_after_repair", MAX_ROUNDS
    best = max(result["rounds"], key=_score)
    result["best_round"] = best["round"]
    result["best_round_summary"] = _round_summary(best)
    return result


def _round_summary(row: dict) -> str:
    c = row.get("checks", {})
    return (f"status={row.get('status')}, hermiticity={c.get('hermiticity')}, "
            f"kinetic={c.get('kinetic_terms')}, mass={c.get('mass_spectrum')}, "
            f"madgraph_import={row.get('madgraph_import_ok')}, "
            f"tags={', '.join(row.get('error_tags') or []) or 'none'}, "
            f"compile_seconds={row.get('seconds')}")


def _write_history(result: dict, wd: Path) -> None:
    if not result["agent_runs"]:
        return
    parts = ["# Repair history — previous attempts on this model", ""]
    for a in result["agent_runs"]:
        after = next((rr for rr in result["rounds"] if rr["round"] == a["round"]), None)
        parts += [f"## Attempt {a['round']}",
                  "What was changed (the agent's own summary):",
                  a.get("notes") or "(no summary)",
                  "",
                  "Validation outcome AFTER that change: "
                  + (_round_summary(after) if after else "(not validated)"),
                  ""]
    baseline = result["rounds"][0]
    parts += ["## For reference — the ORIGINAL model's outcome before any repair:",
              _round_summary(baseline), ""]
    (wd / "REPAIR_HISTORY.md").write_text("\n".join(parts))


def _score(row: dict) -> tuple:
    c = row.get("checks", {})
    return (int(bool(row.get("compile_ok"))),
            sum(1 for k in ("hermiticity", "kinetic_terms", "mass_spectrum")
                if c.get(k) is True),
            int(bool(row.get("madgraph_import_ok"))))


def _persist_logs(row: dict, dest: Path) -> None:
    lp = row.get("compile_log")
    if lp and Path(lp).is_file():
        shutil.copy2(lp, dest / "compile.log")
        mg = Path(lp).parent / "mg5run" / "mg5.log"
        if mg.is_file():
            shutil.copy2(mg, dest / "mg5.log")
        row["compile_log"] = str(dest / "compile.log")


# ----------------------------------------------------------------- reporting

def failing_pages() -> list[str]:
    rep = json.loads((HERE / "validation_benchmark_report.json").read_text())
    bad = []
    for r in rep["rows"]:
        c = r.get("checks", {})
        ok = (r.get("status") == "compiled" and r.get("madgraph_import_ok")
              and all(c.get(k) is True for k in ("hermiticity", "kinetic_terms",
                                                 "mass_spectrum")))
        if not ok:
            bad.append(r["page"])
    return bad


def continuation_seeds(report_json: Path, prior_subdir: str) -> list[tuple[str, Path]]:
    """(page, best-round model.fr) for every fail_after_repair row of a prior
    phase — each next phase reruns the loop from the best state reached so far,
    with whatever signal upgrades the harness has gained since."""
    rep = json.loads(report_json.read_text())
    seeds = []
    for r in rep["results"]:
        if r.get("final_status") != "fail_after_repair":
            continue
        best = r.get("best_round", r["rounds"][-1]["round"] if r["rounds"] else 0)
        seeds.append((r["page"],
                      HERE / r["page"] / prior_subdir / f"round{best}" / "model.fr"))
    return seeds


def write_reports(results: list[dict],
                  json_path: Path = REPORT_JSON, md_path: Path = REPORT_MD) -> dict:
    n = len(results)
    agg = {
        "n_models": n,
        "pass_oneshot": sum(1 for r in results if r["final_status"] == "pass_oneshot"),
        "pass_repaired": sum(1 for r in results if r["final_status"] == "pass_repaired"),
        "fail_after_repair": sum(1 for r in results if r["final_status"] == "fail_after_repair"),
        "agent_no_change": sum(1 for r in results if r["final_status"] == "agent_no_change"),
        "max_rounds": MAX_ROUNDS,
    }
    json_path.write_text(json.dumps({"aggregate": agg, "results": results}, indent=2))

    def _b(v):
        return "✓" if v is True else ("✗" if v is False else "—")

    lines = [
        "# Repair-loop benchmark — failing models through the agentic self-correction loop",
        "",
        "Each one-shot validation failure is re-validated, then handed to an isolated "
        "repair agent (codex exec, workspace-write sandbox, **no network, no reference "
        "files, no model name**) together with the real FeynRules/MadGraph error output; "
        f"the harness re-validates after each edit, up to {MAX_ROUNDS} rounds.",
        "",
        "| Model | Round-0 tags | Rounds | Final | Round-by-round |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        r0 = r["rounds"][0] if r["rounds"] else {}
        prog = " → ".join(
            ("PASS" if rr["full_pass"] else (rr.get("status") or "?")
             + ("" if rr.get("status") != "compiled" else
                f"[H{_b(rr.get('checks', {}).get('hermiticity'))}"
                f"K{_b(rr.get('checks', {}).get('kinetic_terms'))}"
                f"M{_b(rr.get('checks', {}).get('mass_spectrum'))}"
                f"G{_b(rr.get('madgraph_import_ok'))}]"))
            for rr in r["rounds"])
        lines.append(f"| {r['page']} | {', '.join(r0.get('error_tags', []) or ['—'])} | "
                     f"{r.get('rounds_used', '—')} | {r['final_status']} | {prog} |")
    lines += ["", f"**Aggregate:** {json.dumps(agg)}", ""]
    md_path.write_text("\n".join(lines))
    return agg


def main() -> int:
    global OUTROOT
    argv = sys.argv[1:]
    subdir, jp, mp = "repair", REPORT_JSON, REPORT_MD
    if argv and argv[0] == "--failing":
        jobs = [(p, None) for p in failing_pages()]
    elif argv and argv[0] in ("--phase2", "--phase3"):
        n = argv[0][-1]
        prior = REPORT_JSON if n == "2" else HERE / "repair_benchmark_phase2_report.json"
        jobs = continuation_seeds(prior, "repair" if n == "2" else "repair2")
        if len(argv) > 1:  # optional page filter, e.g. --phase3 HNLs,VLC_LN
            keep = {p for a in argv[1:] for p in a.split(",") if p}
            jobs = [j for j in jobs if j[0] in keep]
        subdir = f"repair{n}"
        jp = HERE / f"repair_benchmark_phase{n}_report.json"
        mp = HERE / f"repair_benchmark_phase{n}_report.md"
        OUTROOT = Path(str(OUTROOT) + n)
    elif argv:
        jobs = [(p, None) for a in argv for p in a.split(",") if p]
    else:
        print("usage: repair_benchmark.py --failing | --phase2 | page1,page2,...")
        return 2
    print(f"[repair] {len(jobs)} models, max {MAX_ROUNDS} repair rounds, "
          f"agent={' '.join(AGENT_CMD[:2])}..., out={OUTROOT}, subdir={subdir}", flush=True)
    results: list[dict] = []
    for i, (page, seed) in enumerate(jobs, 1):
        print(f"[repair] ({i}/{len(jobs)}) {page} ...", flush=True)
        res = run_page(page, seed=seed, subdir=subdir)
        tags0 = res["rounds"][0]["error_tags"] if res.get("rounds") else []
        print(f"[repair]     -> {res['final_status']} "
              f"(rounds={res.get('rounds_used', '—')}, round0_tags={tags0})", flush=True)
        results.append(res)
        write_reports(results, jp, mp)
    agg = write_reports(results, jp, mp)
    print("[repair] " + json.dumps(agg), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
