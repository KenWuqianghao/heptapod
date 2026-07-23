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


def total_lag_symbol(fr_path: Path) -> str | None:
    """The model's grand-total Lagrangian symbol = the last top-level `L... :=|=`
    assignment (the one that sums the sub-Lagrangians)."""
    sym = None
    for line in fr_path.read_text(errors="replace").splitlines():
        m = re.match(r"^(L[A-Za-z0-9]*)\s*:?=", line)
        if m:
            sym = m.group(1)
    return sym


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
    lag = total_lag_symbol(fr)
    row["lag_symbol"] = lag
    if not lag:
        row["status"] = "no_lagrangian_symbol"
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
