#!/usr/bin/env python3
"""
# validation_benchmark.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Validation-augmented benchmark.

The prior db_benchmark scored agent-generated .fr files ONLY on field-content
fidelity vs the physicist's reference (name-independent signatures). It never
compiled anything. This benchmark runs each agent-generated .fr through the
REAL downstream tool chain now that a licence-free Wolfram Engine + FeynRules +
MadGraph are available:

    agent .fr  --(FeynRules/Wolfram)-->  UFO  --(MadGraph)-->  import model

and reports, per model and in aggregate:
  * compile_ok            : did FeynRules WriteUFO produce a UFO?
  * hermiticity/kinetic/mass : FeynRules symmetry checks (parsed from the log)
  * n_new_particles       : new (BSM) particle classes that reached the UFO
  * madgraph_import_ok    : does MadGraph load the generated UFO?

This is a strictly stronger signal than field F1: a model can have the right
field content yet fail to compile (bad FeynRules syntax) or fail to load in
MadGraph (malformed UFO). Failures are rows, not omissions.

Usage:
    python eval/benchmark_runs/validation_benchmark.py [page1,page2,...]
    python eval/benchmark_runs/validation_benchmark.py --all
"""

from __future__ import annotations

import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

import config  # noqa: E402
from tools.feynrules.wl_checks import parse_check_blocks  # noqa: E402
from tools.frgen.fr_parser import parse_lagrangian_terms  # noqa: E402

DRIVER = REPO / "tools" / "feynrules" / "UFO_generator.wl"
MG5 = Path(config.mg5_path) / "bin" / "mg5_aMC"
SM_FR = REPO / "tools" / "feynrules" / "test_files" / "models" / "SM.fr"
OUTROOT = Path(os.environ.get("VBENCH_OUT", "/tmp/vbench"))

COMPILE_TIMEOUT = int(os.environ.get("VBENCH_COMPILE_TIMEOUT", "420"))
MG5_TIMEOUT = int(os.environ.get("VBENCH_MG5_TIMEOUT", "240"))

# A diverse default subset spanning colour reps, spins, and gauge extensions.
DEFAULT_SUBSET = [
    "LeptoQuark", "DMsimp", "B-L-SM", "HeavyN", "Sextets",
    "Top-Philic-Zprime", "Triplets", "VLQ", "Wprime", "GeneralU1",
]


_IDENT_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9$]*)\b")


def total_lag_symbol(fr_path: Path) -> tuple[str | None, dict]:
    """The model's grand-total Lagrangian, resolved by reference analysis.

    This used to take the LAST top-level ``L... =`` line in the file. That is
    a guess about file order, and it was wrong for 11 of the 28 benchmark
    models: it selected a sub-Lagrangian, FeynRules compiled that fragment
    alone, and the fragment still passed every Hermiticity / kinetic / mass
    check and imported into MadGraph. Models counted as passing with most of
    their physics missing — VLQ compiled 1 of its 11 Lagrangian terms.

    Instead: build the reference graph over top-level ``L*`` assignments and
    take the **roots**, the terms no other term refers to.

    Exactly one root is the normal case, and it is the total.

    Several roots means the model never declared a single total, and the
    harness genuinely cannot know which is intended. Summing them is NOT a
    safe fallback: roots are independent only as *symbols*, not as physics.
    ChernSimonsPortal defines `LChernSimonsPortal` (symmetric phase, in H and
    the B/Wi field strengths) and `LChernSimonsPortalBroken` (the same
    operator expanded in Z/A/W mass eigenstates) — adding them double-counts
    the interaction. So ambiguity is reported, not resolved, and the model is
    left unscored until someone declares the total. `lag_overrides.json` maps
    page -> symbol for exactly that purpose.

    Returns ``(symbol_or_None, info)``; a None symbol with ``ambiguous`` set
    means "unscoreable", which is different from "failed".
    """
    text = fr_path.read_text(errors="replace")
    try:
        terms = parse_lagrangian_terms(text)
    except Exception as e:                                    # noqa: BLE001
        return None, {"roots": [], "ambiguous": False, "parse_error": str(e)}
    body = {t["name"]: t["expression"] for t in terms if t["name"].startswith("L")}
    if not body:
        return None, {"roots": [], "ambiguous": False}

    referenced: set[str] = set()
    for name, expr in body.items():
        for tok in _IDENT_RE.findall(expr):
            if tok in body and tok != name:
                referenced.add(tok)
    roots = [n for n in body if n not in referenced]

    # what the old positional rule would have picked, kept for the report
    legacy = None
    for line in text.splitlines():
        m = re.match(r"^(L[A-Za-z0-9]*)\s*:?=", line)
        if m:
            legacy = m.group(1)

    roots, dropped = _drop_redundant_roots(roots, body)
    info = {"roots": roots, "legacy_symbol": legacy,
            "n_terms_defined": len(body), "ambiguous": False}
    if dropped:
        info["redundant_roots"] = dropped

    if not roots:                        # every term referenced => cycle
        info.update({"ambiguous": True, "cyclic": True})
        return None, info

    # An explicit human declaration always wins.
    override = _lag_override(fr_path)
    if override:
        info.update({"override": override,
                     "changed_from_legacy": override != legacy})
        return override, info

    if len(roots) > 1:
        info["ambiguous"] = True
        return None, info

    info["changed_from_legacy"] = roots[0] != legacy
    return roots[0], info


_ALIAS_LEFTOVER_RE = re.compile(r"[\s+\-()]")
_ROOT_NAME_PREFERENCE = ("LTot", "LFull", "LBSM", "LTotal")


def _reach(start: str, body: dict) -> set:
    seen, stack = set(), [start]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        for tok in _IDENT_RE.findall(body.get(cur, "")):
            if tok in body:
                stack.append(tok)
    return seen


def _is_pure_alias(name: str, body: dict) -> bool:
    """True when a term is only a sum of other terms, contributing no physics.

    ``LD := LD1 + LD2 + LD3`` is a pure alias. ``LSextet := LSextetKin + LD1 +
    ... + LPot`` is too. Anything with real operators left over after removing
    term names and ``+ - ( )`` is not.
    """
    expr = body.get(name, "")
    for tok in sorted(set(_IDENT_RE.findall(expr)), key=len, reverse=True):
        if tok in body:
            expr = expr.replace(tok, "")
    return not _ALIAS_LEFTOVER_RE.sub("", expr)


def _drop_redundant_roots(roots: list, body: dict) -> tuple[list, list]:
    """Remove roots that are pure aliases adding nothing another root lacks.

    Two real cases in the benchmark, neither of them a guess:
      Sextets   `LD := LD1+LD2+LD3` while `LSextet` already reaches LD1..LD3
      MDMmodel  `LMDMNP` and `LTot` are the same sum written twice
    Dropping these leaves a single genuine total. Roots that carry physics of
    their own, or reach terms no other root reaches, are always kept.
    """
    if len(roots) < 2:
        return roots, []
    reach = {r: _reach(r, body) - {r} for r in roots}
    kept, dropped = list(roots), []
    for r in roots:
        if not _is_pure_alias(r, body):
            continue
        others = [s for s in kept if s != r]
        # covered by a single other root that we are keeping
        covering = next((s for s in others if reach[r] <= reach[s]), None)
        if covering is None:
            continue
        # mutual duplicates: keep the preferred name, drop the other
        if reach[covering] <= reach[r]:
            pref = next((p for p in _ROOT_NAME_PREFERENCE if p in (r, covering)), None)
            if pref == r:
                continue
        kept.remove(r)
        dropped.append({"root": r, "covered_by": covering})
    return (kept or roots), dropped


def _lag_override(fr_path: Path) -> str | None:
    """Human-declared total for a model, from lag_overrides.json.

    Shape: ``{"<page>": "LTot", ...}``. The page is the benchmark directory
    name, i.e. the first path component under this file's directory.
    """
    path = HERE / "lag_overrides.json"
    if not path.is_file():
        return None
    try:
        table = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    try:
        page = fr_path.resolve().relative_to(HERE.resolve()).parts[0]
    except ValueError:
        return None
    val = table.get(page)
    return val if isinstance(val, str) and val else None


def _kill_stale_kernels() -> None:
    subprocess.run(["pkill", "-9", "-f", "Wolfram Player.app/Contents/MacOS/WolframKernel"],
                   capture_output=True)


def compile_to_ufo(page: str, fr: Path, lag: str, outdir: Path) -> dict:
    outdir.parent.mkdir(parents=True, exist_ok=True)
    if outdir.exists():
        subprocess.run(["rm", "-rf", str(outdir)], capture_output=True)
    cmd = [
        config.wolframscript_path, "-f", str(DRIVER),
        f"ModelPath={fr}", f"FeynRulesPath={config.feynrules_path}",
        f"OutputDir={outdir}", "Checks=true", "AddDecays=false", f"LagName={lag}",
    ]
    t0 = time.time()
    # Popen + process-group kill: subprocess.run(timeout=) only kills
    # wolframscript, then blocks in communicate() until the orphaned
    # WolframKernel children release the output pipe (observed 85 min hang).
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, stdin=subprocess.DEVNULL, start_new_session=True)
    try:
        out, _ = p.communicate(timeout=COMPILE_TIMEOUT)
        rc = p.returncode
        timed_out = False
    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(p.pid), signal.SIGKILL)
        try:
            out, _ = p.communicate(timeout=30)
        except Exception:
            out = ""
        rc = -1
        timed_out = True
    finally:
        _kill_stale_kernels()
    out = out or ""
    dt = round(time.time() - t0, 1)
    (outdir.parent / "compile.log").write_text(out)
    ufo_files = [f for f in ("particles.py", "parameters.py", "couplings.py",
                             "vertices.py", "lorentz.py")
                 if (outdir / f).is_file()]
    compile_ok = ("[INFO] Done." in out) and (outdir / "particles.py").is_file()
    checks = {c["name"]: c["passed"] for c in parse_check_blocks(out)}
    protected_errs = len(re.findall(r"ISUMObject|IndexRange\[Index\[Spin\]\]", out))
    return {
        "compile_ok": compile_ok,
        "timed_out": timed_out,
        "exit": rc,
        "seconds": dt,
        "ufo_files": ufo_files,
        "checks": checks,
        "protected_symbol_errors": protected_errs,
        "log_tail": out[-1200:] if not compile_ok else "",
    }


def count_new_particles(outdir: Path) -> int:
    """Particles in the generated UFO minus the plain-SM baseline count."""
    pf = outdir / "particles.py"
    if not pf.is_file():
        return 0
    txt = pf.read_text(errors="replace")
    total = len(re.findall(r"=\s*Particle\(", txt))
    # SM UFO has ~ (17 physical + goldstones/ghosts). Report raw; SM baseline
    # subtraction is approximate, so we also keep the raw count in the row.
    return total


def madgraph_import(outdir: Path, workdir: Path) -> dict:
    if not MG5.is_file():
        return {"madgraph_import_ok": False, "reason": "mg5_aMC not found"}
    workdir.mkdir(parents=True, exist_ok=True)
    cmdfile = workdir / "mg5_import.txt"
    cmdfile.write_text(f"import model {outdir}\ndisplay particles\n")
    try:
        p = subprocess.run([str(MG5), str(cmdfile)], capture_output=True, text=True,
                           timeout=MG5_TIMEOUT, stdin=subprocess.DEVNULL, cwd=str(workdir))
        out = (p.stdout or "") + "\n" + (p.stderr or "")
        (workdir / "mg5.log").write_text(out)
    except subprocess.TimeoutExpired:
        return {"madgraph_import_ok": False, "reason": "timeout"}
    fatal = ("Traceback (most recent call last)" in out
             or "InvalidCmd" in out
             or re.search(r"Command \".*\" interrupted with error", out))
    loaded = re.search(r"Current model contains (\d+) particles", out)
    ok = bool(loaded) and not fatal
    return {
        "madgraph_import_ok": ok,
        "mg5_particles": int(loaded.group(1)) if loaded else None,
        "lepton_number_violation": "violating the charge: LeptonNumber" in out,
        "mg5_tail": out[-800:] if not ok else "",
    }


def run_one(page: str) -> dict:
    fr = HERE / page / "model" / f"{page}_gen.fr"
    row: dict = {"page": page, "fr": str(fr.relative_to(REPO)) if fr.is_file() else None}
    if not fr.is_file():
        row["status"] = "missing_fr"
        return row
    lag, lag_info = total_lag_symbol(fr)
    row["lag_symbol"] = lag
    row["lag_resolution"] = lag_info
    if not lag:
        # Unscoreable is not the same as failed: the model may be perfectly
        # good, but it never says which symbol is its total Lagrangian, so
        # there is nothing defensible to compile.
        row["status"] = ("ambiguous_lagrangian_symbol" if lag_info.get("ambiguous")
                         else "no_lagrangian_symbol")
        return row
    outdir = OUTROOT / page / f"{page}_UFO"
    comp = compile_to_ufo(page, fr, lag, outdir)
    row.update(comp)
    if comp["compile_ok"]:
        row["n_particles_ufo"] = count_new_particles(outdir)
        row.update(madgraph_import(outdir, OUTROOT / page / "mg5run"))
        row["status"] = "compiled"
    else:
        row["status"] = "compile_failed" if not comp["timed_out"] else "compile_timeout"
    return row


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] == "--all":
        cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
        pages = [c["page"] for c in cands]
    elif argv:
        pages = [p for a in argv for p in a.split(",") if p]
    else:
        pages = DEFAULT_SUBSET

    print(f"[vbench] {len(pages)} models | compile_timeout={COMPILE_TIMEOUT}s "
          f"mg5_timeout={MG5_TIMEOUT}s | out={OUTROOT}", flush=True)
    rows = []
    for i, page in enumerate(pages, 1):
        print(f"[vbench] ({i}/{len(pages)}) {page} ...", flush=True)
        row = run_one(page)
        tag = row.get("status")
        extra = ""
        if tag == "compiled":
            extra = (f"  checks={row.get('checks')}  parts={row.get('n_particles_ufo')}"
                     f"  mg5={row.get('madgraph_import_ok')}  ({row.get('seconds')}s)")
        print(f"[vbench]     -> {tag}{extra}", flush=True)
        rows.append(row)
        (HERE / "validation_benchmark_report.json").write_text(
            json.dumps({"rows": rows}, indent=2))

    # Aggregates
    n = len(rows)
    compiled = [r for r in rows if r.get("status") == "compiled"]
    def _rate(pred):
        m = [r for r in compiled if pred(r)]
        return (len(m), len(compiled))
    herm = _rate(lambda r: r.get("checks", {}).get("hermiticity"))
    mg5ok = _rate(lambda r: r.get("madgraph_import_ok"))
    agg = {
        "n_models": n,
        "n_compiled": len(compiled),
        "compile_rate": round(len(compiled) / n, 3) if n else 0,
        "hermiticity_pass": herm[0],
        "madgraph_import_ok": mg5ok[0],
        "n_compile_failed": sum(1 for r in rows if r.get("status") == "compile_failed"),
        "n_compile_timeout": sum(1 for r in rows if r.get("status") == "compile_timeout"),
    }
    report = {"aggregate": agg, "rows": rows}
    (HERE / "validation_benchmark_report.json").write_text(json.dumps(report, indent=2))

    lines = [
        "# Validation-augmented benchmark — agent .fr → FeynRules/Wolfram UFO → MadGraph",
        "",
        "Each agent-generated `.fr` (from the field-content benchmark) is compiled "
        "to a UFO with the free Wolfram Engine + FeynRules, physics-checked, and "
        "imported into MadGraph 3.7.2. This measures whether the agent's model "
        "**actually works in the real tool chain**, not just whether its field "
        "content matches a reference.",
        "",
        f"**Aggregate over {n} models:** compiled **{agg['n_compiled']}/{n}** "
        f"({agg['compile_rate']:.0%}); Hermiticity-pass {herm[0]}/{herm[1]}; "
        f"MadGraph-import-ok {mg5ok[0]}/{mg5ok[1]}; "
        f"compile-failed {agg['n_compile_failed']}, timeout {agg['n_compile_timeout']}.",
        "",
        "| Model | Lag symbol | Compile | Herm | Kin | Mass | UFO parts | MG5 load | LNV | secs | Status |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    def _b(v):
        return "✓" if v is True else ("✗" if v is False else "—")
    for r in rows:
        c = r.get("checks", {})
        lines.append(
            f"| {r['page']} | {r.get('lag_symbol','—')} | {_b(r.get('compile_ok'))} | "
            f"{_b(c.get('hermiticity'))} | {_b(c.get('kinetic_terms'))} | "
            f"{_b(c.get('mass_spectrum'))} | {r.get('n_particles_ufo','—')} | "
            f"{_b(r.get('madgraph_import_ok'))} | {_b(r.get('lepton_number_violation'))} | "
            f"{r.get('seconds','—')} | {r.get('status')} |")
    lines += [
        "",
        "## Notes",
        "- `Compile` = FeynRules `WriteUFO` produced `particles.py` and printed Done.",
        "- Physics checks (Herm/Kin/Mass) are FeynRules' own consistency routines, "
        "parsed from the run log; `—` means the check did not emit a verdict.",
        "- `MG5 load` = MadGraph `import model` succeeded (UFO auto-converted to "
        "Python3 as needed) and reported a particle count with no fatal error.",
        "- `LNV` = MadGraph flagged a lepton-number-violating interaction "
        "(expected/correct for leptoquark and Majorana-neutrino models).",
        "- `AddDecays=False`: FeynRules' auto-decay routine is disabled (broken "
        "under Wolfram ≥ 15); decay widths are left to MadGraph's `compute_widths`.",
    ]
    (HERE / "validation_benchmark_report.md").write_text("\n".join(lines) + "\n")
    print("\n[vbench] " + json.dumps(agg), flush=True)
    print("[vbench] report: eval/benchmark_runs/validation_benchmark_report.{json,md}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
