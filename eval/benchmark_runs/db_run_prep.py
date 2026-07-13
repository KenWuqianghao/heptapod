#!/usr/bin/env python3
"""Fetch each runnable candidate's paper (PDF -> text) and write its Codex
prompt. Architecture: Codex only EXTRACTS (reads the local paper text and
emits a fenced model_json); the deterministic GenerateFeynRulesModelTool runs
locally afterwards (db_collect.py), so schema validation genuinely executes and
no MCP write-approval gating is involved. Codex runs read-only.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

from tools.literature.literature_tools import FetchPaperPDFTool, ExtractPaperTextTool  # noqa: E402

PROMPT = """You are benchmarking automated extraction of a BSM physics model from its paper, to be compared against the physicist's own FeynRules implementation.

MODEL: {page} ({category}) — FeynRules DB entry based on arXiv:{arxiv}.
PAPER: full text at "{text_path}" (read it with sed/cat; it is authoritative).
SCHEMA: read tools/frgen/frmodel.py (pydantic FeynRulesModel).

TASK — extract the COMPLETE new-physics content:
1. Read the paper. Identify EVERY new particle beyond the Standard Model: spin (S/F/V), colour rep (singlet/triplet/sextet/octet), SU(2) rep, electric charge Q and/or hypercharge Y, mass parameter. COMPLETENESS IS SCORED — a model with several new states (multiplets, mass eigenstates, generations) must include all of them as separate ParticleClass entries (or class_members).
2. Identify the new coupling/mass/mixing parameters (External unless clearly derived).
3. Include the main new-physics lagrangian_terms (verbatim Mathematica strings, FeynRules idioms).

SCHEMA RULES: all numeric physics values are STRINGS ("-1/3", "1500."); SM add-on => gauge_groups []; indices Colour/Gluon/Generation/SU2D/SU2W need NO declaration; any OTHER index (e.g. a colour-sextet index, a new-generation index) NEEDS an index_decls entry (range_kind "NoUnfold", correct size); every particle needs a unique class_index; self_conjugate=false for complex fields (distinct antiparticle), true for real/Majorana fields.

OUTPUT: your FINAL message must contain exactly one fenced code block tagged json containing ONLY the FeynRulesModel JSON object (no commentary inside the fences). Set model_name to "{page}_gen".
"""


def main() -> int:
    cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
    ok, fail = 0, []
    for c in cands:
        page, aid = c["page"], c["arxiv_id"]
        rdir = HERE / page
        rdir.mkdir(exist_ok=True)
        # paper text (cached if already fetched)
        txts = list((rdir / "text").glob("*.txt")) if (rdir / "text").is_dir() else []
        if not txts:
            raw = FetchPaperPDFTool(arxiv_id=aid, base_directory=str(rdir))._run()
            if not raw.lstrip().startswith("{"):
                fail.append((page, aid, raw.splitlines()[0][:90]))
                print(f"  {page:26} PDF FAIL: {raw.splitlines()[0][:70]}", flush=True)
                time.sleep(4)
                continue
            pdf = json.loads(raw)["pdf_path"]
            tr = ExtractPaperTextTool(pdf_path=pdf, base_directory=str(rdir))._run()
            if not tr.lstrip().startswith("{"):
                fail.append((page, aid, tr.splitlines()[0][:90]))
                continue
            txts = [rdir / json.loads(tr)["text_path"]]
            time.sleep(4)
        text_rel = txts[0].relative_to(REPO)
        (rdir / "prompt.txt").write_text(PROMPT.format(
            page=page, category=c["category"], arxiv=aid, text_path=text_rel))
        ok += 1
        print(f"  {page:26} ready  (paper {aid}, {txts[0].stat().st_size//1000}K chars)", flush=True)

    print(f"\nREADY: {ok} / {len(cands)}   paper-fetch failures: {len(fail)}")
    for p, a, e in fail:
        print(f"  RETRY LATER: {p} ({a}): {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
