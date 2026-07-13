#!/usr/bin/env python3
"""Download reference .fr files for every candidate model and apply the parse
gate, producing ``db_candidates.json`` — the runnable benchmark set.

Gates (all recorded, nothing silently dropped):
  G1  model page lists >=1 downloadable .fr           (from db_index.json)
  G2  model page cites >=1 arXiv paper                (from db_index.json)
  G3  a reference .fr downloads and parses            (fr_parser)
  G4  the parsed reference declares >=1 particle class (field-extraction
      benchmark is meaningless for pure-operator EFT files)

Multi-file models: the largest .fr that is not a plain SM.fr is taken as the
reference (recorded); the rest are downloaded alongside for completeness.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import requests

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

from tools.frgen.fr_parser import parse_fr_file  # noqa: E402
from eval.reference_bench import field_records, _field_sig, sm_baseline_sigs  # noqa: E402
from collections import Counter  # noqa: E402
from difflib import SequenceMatcher  # noqa: E402

CACHE = REPO / "eval" / "reference_cache"
SM_FR = REPO / "tools" / "feynrules" / "test_files" / "models" / "SM.fr"
session = requests.Session()
session.headers["User-Agent"] = "heptapod-benchmark/1.0 (GSoC HEPSIM5; polite)"


def download(url: str, dest: Path) -> bool:
    try:
        time.sleep(0.5)
        r = session.get(url, timeout=60)
        r.raise_for_status()
        dest.write_bytes(r.content)
        return True
    except Exception as e:  # noqa: BLE001
        print(f"    download FAIL {url.rsplit('/',1)[-1]}: {type(e).__name__}", flush=True)
        return False


def main() -> int:
    index = json.loads((HERE / "db_index.json").read_text())
    candidates, funnel = [], {"listed": len(index["models"]), "g1_fr": 0, "g2_paper": 0,
                              "g3_parses": 0, "g4_has_fields": 0}
    for m in index["models"]:
        if not m.get("fr_urls"):
            m["gate"] = "no_fr_attachment"; continue
        funnel["g1_fr"] += 1
        if not m.get("arxiv_ids"):
            m["gate"] = "no_arxiv_paper"; continue
        funnel["g2_paper"] += 1

        mdir = CACHE / m["page"]
        mdir.mkdir(parents=True, exist_ok=True)
        files = []
        for u in m["fr_urls"]:
            dest = mdir / u.rsplit("/", 1)[-1]
            if dest.exists() or download(u, dest):
                files.append(dest)
        nonsm = [f for f in files if f.name.lower() != "sm.fr"] or files
        if not nonsm:
            m["gate"] = "download_failed"; continue
        # Prefer the file whose name resembles the model page (avoids e.g. the
        # Triplets page's copy of SextetDiquarks.fr winning on size alone);
        # among similarly-named files take the largest.
        def _sim(f: Path) -> float:
            return SequenceMatcher(None, m["page"].lower(), f.stem.lower()).ratio()
        named = [f for f in nonsm if _sim(f) >= 0.5]
        ref = max(named or nonsm, key=lambda f: (round(_sim(f), 1), f.stat().st_size))

        try:
            parsed = parse_fr_file(str(ref))
        except Exception as e:  # noqa: BLE001
            m["gate"] = f"parse_failed: {type(e).__name__}: {str(e)[:80]}"
            print(f"  {m['page']:28} PARSE FAIL ({ref.name})", flush=True)
            continue
        funnel["g3_parses"] += 1
        ncls = len(parsed.get("classes", []))
        # New-physics field count. Subtract the SM baseline ONLY for
        # standalone-style references (>=10 signatures shared with the SM);
        # an add-on's Z'/W'-like fields legitimately share SM signatures and
        # must not be deleted. Zero new fields => operator-only benchmark.
        sigs = Counter(_field_sig(r) for r in field_records(parsed))
        base = sm_baseline_sigs(str(SM_FR))
        standalone = sum((sigs & base).values()) >= 10
        n_new = sum(((sigs - base) if standalone else sigs).values())
        if ncls == 0 or n_new == 0:
            m["gate"] = "no_new_fields (operator-only or pure-SM content)"
            print(f"  {m['page']:28} {ncls} classes but 0 new fields — funnel out", flush=True)
            continue
        funnel["g4_has_fields"] += 1
        m["gate"] = "RUNNABLE"
        rec = {"page": m["page"], "category": m["category"], "arxiv_id": m["arxiv_ids"][0],
               "all_arxiv": m["arxiv_ids"], "reference_fr": str(ref.relative_to(REPO)),
               "n_ref_classes": ncls, "n_new_fields": n_new,
               "n_ref_params": len(parsed.get("parameters", []))}
        candidates.append(rec)
        print(f"  {m['page']:28} OK  ref={ref.name:30} classes={ncls:3d} NEW={n_new:3d} params={rec['n_ref_params']}", flush=True)

    (HERE / "db_candidates.json").write_text(json.dumps(
        {"funnel": funnel, "candidates": candidates,
         "gated_out": [{"page": m["page"], "gate": m.get("gate")} for m in index["models"]
                       if m.get("gate") != "RUNNABLE"]}, indent=2))
    print(f"\nFUNNEL: listed={funnel['listed']}  +fr={funnel['g1_fr']}  +paper={funnel['g2_paper']}"
          f"  parses={funnel['g3_parses']}  has_fields={funnel['g4_has_fields']}  -> RUNNABLE={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
