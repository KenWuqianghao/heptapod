#!/usr/bin/env python3
"""
# build_ian_bundle.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Build the physicist review bundle: for every benchmark model that passes the
full validation chain, run the blank-slate reverse check (sanitize -> blind
reconstruction -> paper cross-check -> REVIEW.pdf) against the model's own
paper, then assemble ian_review_bundle/<model>/{<model>.fr, REVIEW.pdf} plus
a README inventory, and zip it.

Resumable: models whose <page>/review/*/REVIEW.pdf already exists are skipped
on re-run. Reverse checks run serially (each spawns two codex instances).

Usage:
    python eval/benchmark_runs/build_ian_bundle.py            # run + assemble
    python eval/benchmark_runs/build_ian_bundle.py --assemble # bundle only
"""

from __future__ import annotations

import glob
import json
import shutil
import sys
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

import config  # noqa: E402
from tools.reverse.reverse_tool import ReverseLagrangianTool  # noqa: E402

BUNDLE = HERE / "ian_review_bundle"
DEFAULT_AGENT = ("codex exec --sandbox read-only --skip-git-repo-check "
                 "--model gpt-5.5 -c model_reasoning_effort=medium "
                 "--output-last-message {output}")


def passing_models() -> list[tuple[str, Path, str]]:
    """(page, final .fr path, provenance) for every full-chain-passing model."""
    out: list[tuple[str, Path, str]] = []
    rep = json.loads((HERE / "validation_benchmark_report.json").read_text())
    for r in rep["rows"]:
        c = r.get("checks", {})
        if (r.get("status") == "compiled" and r.get("madgraph_import_ok")
                and all(c.get(k) is True for k in ("hermiticity", "kinetic_terms",
                                                   "mass_spectrum"))):
            out.append((r["page"], HERE / r["page"] / "model" / f"{r['page']}_gen.fr",
                        "passed one-shot"))
    for fn, sub, tag in (("repair_benchmark_report.json", "repair", "repaired (phase 1)"),
                         ("repair_benchmark_phase2_report.json", "repair2", "repaired (phase 2)"),
                         ("repair_benchmark_phase3_report.json", "repair3", "repaired (phase 3)")):
        p = HERE / fn
        if not p.is_file():
            continue
        for r in json.loads(p.read_text())["results"]:
            if r.get("final_status") == "pass_repaired":
                out.append((r["page"], HERE / r["page"] / sub / "final.fr", tag))
    return out


def paper_for(page: str) -> Path | None:
    hits = sorted(glob.glob(str(HERE / page / "text" / "*.txt")))
    return Path(hits[0]) if hits else None


def _reviews(page: str, name: str) -> list[Path]:
    """REVIEW.* both directly under <page>/review/ and one level deeper."""
    outdir = HERE / page / "review"
    return sorted(outdir.glob(name)) + sorted(outdir.glob(f"*/{name}"))


def run_reverse(page: str, fr: Path) -> dict:
    existing = _reviews(page, "REVIEW.pdf")
    if existing:
        return {"skipped": True, "review_package": str(existing[0].relative_to(HERE))}
    paper = paper_for(page)
    tool = ReverseLagrangianTool(
        base_directory=str(HERE),
        blank_agent_cmd=getattr(config, "blank_agent_cmd", DEFAULT_AGENT),
        model_path=str(fr.relative_to(HERE)),
        action="full" if paper else "reconstruct",
        paper_tex_path=str(paper.relative_to(HERE)) if paper else None,
        output_dir=str(Path(page) / "review"),
        timeout_sec=900,
    )
    raw = tool._run()
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return {"raw": str(raw)[-800:]}


def assemble(results: dict[str, dict]) -> Path:
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir()
    rows = []
    for page, fr, tag in passing_models():
        dst = BUNDLE / page
        dst.mkdir()
        shutil.copy2(fr, dst / f"{page}.fr")
        pdfs = _reviews(page, "REVIEW.pdf")
        mds = _reviews(page, "REVIEW.md")
        status = "no review generated"
        if pdfs:
            shutil.copy2(pdfs[0], dst / "REVIEW.pdf")
            status = "REVIEW.pdf"
        elif mds:
            shutil.copy2(mds[0], dst / "REVIEW.md")
            status = "REVIEW.md (PDF compile failed)"
        paper = paper_for(page)
        arxiv = paper.stem if paper else "—"
        rows.append((page, arxiv, tag, status))

    lines = [
        "# Review bundle — agent-extracted FeynRules models",
        "",
        "One directory per model that passes the full validation chain "
        "(FeynRules/Wolfram UFO compile, Hermiticity / kinetic-term / mass-spectrum "
        "checks, MadGraph import):",
        "",
        "- `<model>.fr` — the validated FeynRules file (agent-extracted; where noted, "
        "self-repaired by the closed validation loop with no human input).",
        "- `REVIEW.pdf` — the blank-slate reverse-check package: a fresh agent that saw "
        "ONLY the sanitized `.fr` (no paper, no metadata) reconstructs the physics in "
        "LaTeX; a second fresh agent compares that reconstruction against the paper "
        "term by term and grades every disagreement (convention / substantive / "
        "cosmetic). The final page is a sign-off block — **the tooling never declares "
        "the physics correct; that verdict is yours.**",
        "",
        "Validation means the tool chain accepts the model. It does not certify the "
        "physics — that is exactly what these review packages are for.",
        "",
        "| model | paper (arXiv) | provenance | review |",
        "|---|---|---|---|",
    ]
    for page, arxiv, tag, status in rows:
        lines.append(f"| {page} | {arxiv} | {tag} | {status} |")
    lines += [
        "",
        "Benchmark context: 28 models attempted; 15 passed one-shot; the closed "
        "repair loop recovered 10 more (25/28). Full analysis is included as "
        "REPAIR_BENCHMARK_ANALYSIS.md.",
        "",
    ]
    (BUNDLE / "README.md").write_text("\n".join(lines))
    shutil.copy2(HERE / "REPAIR_BENCHMARK_ANALYSIS.md", BUNDLE / "REPAIR_BENCHMARK_ANALYSIS.md")

    zpath = HERE / "ian_review_bundle.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BUNDLE.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(HERE))
    return zpath


def main() -> int:
    models = passing_models()
    print(f"[bundle] {len(models)} full-chain-passing models", flush=True)
    results: dict[str, dict] = {}
    if "--assemble" not in sys.argv:
        for i, (page, fr, tag) in enumerate(models, 1):
            if not fr.is_file():
                print(f"[bundle] ({i}/{len(models)}) {page}: MISSING {fr}", flush=True)
                continue
            t0 = time.time()
            print(f"[bundle] ({i}/{len(models)}) {page} [{tag}] reverse check ...", flush=True)
            res = run_reverse(page, fr)
            dt = round(time.time() - t0, 1)
            note = ("skipped (already done)" if res.get("skipped")
                    else res.get("review_package") or res.get("status")
                    or list(res)[:3])
            print(f"[bundle]     -> {note} ({dt}s)", flush=True)
            results[page] = res
    z = assemble(results)
    print(f"[bundle] wrote {z} ({z.stat().st_size // 1024} KB)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
