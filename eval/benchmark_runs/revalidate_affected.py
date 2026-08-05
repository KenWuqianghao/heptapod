#!/usr/bin/env python3
"""
# revalidate_affected.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Re-run the full validation chain after the total-Lagrangian fix.

`validation_benchmark.total_lag_symbol` used to pick a model's grand-total
Lagrangian by file position (the last `^L... =` line). For 11 of the 28
benchmark models that selected a sub-Lagrangian, so FeynRules compiled a
fragment which then passed every check and imported into MadGraph. It is now
resolved by reference analysis.

This re-validates the affected models against the SAME `.fr` the review
bundle ships — `<phase>/final.fr` where the repair loop produced one, else the
one-shot extraction — so the numbers describe the artifacts a reviewer holds.

The pass rate may fall. A fragment can be Hermitian when the whole Lagrangian
is not, so models that passed on a fragment may now legitimately fail. That
is the point of the fix.

Usage:
    python eval/benchmark_runs/revalidate_affected.py [page,...]
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent))

import validation_benchmark as vb  # noqa: E402

OUT = HERE / "revalidation_report.json"

def scoreable_pages() -> tuple[list[str], list[str]]:
    """(scoreable, ambiguous) over every model directory here.

    Derived, not hardcoded: the resolver decides, so this list cannot drift
    away from what the harness actually does.
    """
    scoreable, ambiguous = [], []
    for d in sorted(p for p in HERE.iterdir() if p.is_dir()):
        fr, _ = bundle_fr(d.name)
        if not fr:
            continue
        sym, _info = vb.total_lag_symbol(fr)
        (scoreable if sym else ambiguous).append(d.name)
    return scoreable, ambiguous


def bundle_fr(page: str) -> tuple[Path | None, str]:
    """The .fr the review bundle ships for this model."""
    for phase in ("repair3", "repair2", "repair"):
        f = HERE / page / phase / "final.fr"
        if f.is_file():
            return f, f"{phase}/final.fr"
    g = HERE / page / "model" / f"{page}_gen.fr"
    return (g, "one-shot") if g.is_file() else (None, "")


def run_one(page: str) -> dict:
    fr, src = bundle_fr(page)
    row: dict = {"page": page, "fr_source": src}
    if not fr:
        row["status"] = "missing_fr"
        return row

    lag, info = vb.total_lag_symbol(fr)
    row["lag_symbol"] = lag
    row["lag_resolution"] = info
    if not lag:
        row["status"] = "no_lagrangian_symbol"
        return row

    outdir = vb.OUTROOT / "revalidate" / page / f"{page}_UFO"
    comp = vb.compile_to_ufo(page, fr, lag, outdir)
    row.update(comp)
    if comp["compile_ok"]:
        row["n_particles_ufo"] = vb.count_new_particles(outdir)
        row.update(vb.madgraph_import(
            outdir, vb.OUTROOT / "revalidate" / page / "mg5run"))
        row["status"] = "compiled"
    else:
        row["status"] = "compile_timeout" if comp["timed_out"] else "compile_failed"
    return row


def full_chain_ok(row: dict) -> bool:
    c = row.get("checks", {}) or {}
    return bool(
        row.get("status") == "compiled"
        and row.get("madgraph_import_ok")
        and all(c.get(k) is True for k in
                ("hermiticity", "kinetic_terms", "mass_spectrum"))
    )


def main() -> int:
    argv = [p for a in sys.argv[1:] for p in a.split(",") if p]
    if argv:
        pages, ambiguous = argv, []
    else:
        pages, ambiguous = scoreable_pages()
    print(f"[revalidate] {len(pages)} scoreable models, compile budget "
          f"{vb.COMPILE_TIMEOUT}s, out={vb.OUTROOT}", flush=True)
    if ambiguous:
        print(f"[revalidate] {len(ambiguous)} unscoreable (no declared total "
              f"Lagrangian): {', '.join(ambiguous)}", flush=True)
        print("[revalidate] declare them in lag_overrides.json to score them "
              "— see LAGRANGIAN_AMBIGUITY.md", flush=True)

    rows = []
    t0 = time.time()
    for i, page in enumerate(pages, 1):
        t1 = time.time()
        print(f"[revalidate] ({i}/{len(pages)}) {page} ...", flush=True)
        row = run_one(page)
        row["full_chain_ok"] = full_chain_ok(row)
        rows.append(row)
        c = row.get("checks", {}) or {}
        print(f"[revalidate]   -> {row.get('status')} "
              f"herm={c.get('hermiticity')} kin={c.get('kinetic_terms')} "
              f"mass={c.get('mass_spectrum')} "
              f"mg5={row.get('madgraph_import_ok')} "
              f"FULL={row['full_chain_ok']} ({round(time.time()-t1,1)}s)",
              flush=True)
        OUT.write_text(json.dumps(
            {"rows": rows, "seconds": round(time.time() - t0, 1)}, indent=1))

    n_ok = sum(1 for r in rows if r["full_chain_ok"])
    print(f"[revalidate] done in {round(time.time()-t0,1)}s: "
          f"{n_ok}/{len(rows)} of the scoreable models pass the full chain",
          flush=True)
    if ambiguous:
        print(f"[revalidate] {len(ambiguous)} models remain unscored — "
              f"neither passed nor failed", flush=True)
    print(f"[revalidate] wrote {OUT.name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
