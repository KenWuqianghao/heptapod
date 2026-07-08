#!/usr/bin/env python3
"""
# build_fr_convention_catalog.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.

Build a FeynRules convention catalog from reference model files.

Parses .fr files with tools.frgen.fr_parser and emits docs/fr_convention_catalog
.{md,json}: a survey of naming/index/quantum-number/value-format conventions to
inform extraction prompts and generator defaults (GSoC HEPSIM5 task 1).

Offline by default it parses the in-tree models (SM.fr, S1_LQ_RR.fr). With
--download it fetches additional reference models from the FeynRules model
database into a git-ignored cache (sha256 recorded); those files are physicist-
published and are NOT redistributed in the repo.

Usage:
  python scripts/build_fr_convention_catalog.py                 # offline, in-tree
  python scripts/build_fr_convention_catalog.py --download      # + fetch DB models
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.frgen.fr_parser import parse_fr_file  # noqa: E402

MODELS_DIR = REPO_ROOT / "tools" / "feynrules" / "test_files" / "models"

# In-tree, always-available reference models (already committed as fixtures).
IN_TREE = [
    {"name": "SM", "path": MODELS_DIR / "SM.fr",
     "citation": "Christensen, Duhr, Fuks — FeynRules Standard Model"},
    {"name": "S1_LQ_RR", "path": MODELS_DIR / "S1_LQ_RR.fr",
     "citation": "Menzo — scalar leptoquark S1 add-on (HEPTAPOD example)"},
]

# Optional downloads (host-allowlisted). URLs are best-effort raw attachments on
# the FeynRules wiki; fix here if the wiki layout changes.
_ALLOWED_HOST = "feynrules.irmp.ucl.ac.be"
DOWNLOADS = [
    {"name": "SLQrules", "url": "https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/SLQrules/SLQrules.fr",
     "citation": "Dorsner, Greljo — Leptoquark toolbox (arXiv:1801.07641)"},
    {"name": "DMsimp_s_spin0", "url": "https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/DMsimp/dm_s_spin0.fr",
     "citation": "DMsimp — simplified dark matter (arXiv:1508.00564)"},
]


def _classify_value(v: str) -> str:
    v = (v or "").strip()
    if not v:
        return "empty"
    if re.fullmatch(r"-?\d+/\d+", v):
        return "rational"
    if "*^" in v or re.search(r"\d[eE][+-]?\d", v):
        return "scientific"
    if re.fullmatch(r"-?\d+\.\d*", v) or re.fullmatch(r"-?\.\d+", v):
        return "decimal"
    if re.fullmatch(r"-?\d+", v):
        return "integer"
    if v.startswith('"'):
        return "string"
    if v.startswith("{"):
        return "list"
    return "symbolic_or_expr"


def _summarize(models: dict) -> dict:
    class_labels: Counter = Counter()
    spin_types: Counter = Counter()
    indices: Counter = Counter()
    qn_keys: Counter = Counter()
    param_types: Counter = Counter()
    block_names: Counter = Counter()
    value_formats: Counter = Counter()
    for mdl in models.values():
        for c in mdl["classes"]:
            class_labels[c["label"]] += 1
            if c["spin_type"]:
                spin_types[c["spin_type"]] += 1
            if c["indices"]:
                for idx in re.findall(r"Index\[(\w+)\]", c["indices"]):
                    indices[idx] += 1
            for k, v in c["quantum_numbers"].items():
                qn_keys[k] += 1
                value_formats[_classify_value(v)] += 1
        for p in mdl["parameters"]:
            if p["parameter_type"]:
                param_types[p["parameter_type"]] += 1
            if p["block_name"]:
                block_names[p["block_name"]] += 1
            if p["value"]:
                value_formats[_classify_value(p["value"])] += 1
    return {
        "naming_patterns": {
            "class_label_examples": sorted(class_labels)[:20],
            "spin_types": dict(spin_types),
        },
        "index_conventions": dict(indices),
        "quantum_numbers_usage": dict(qn_keys),
        "parameter_types": dict(param_types),
        "block_names": dict(block_names),
        "value_formats": dict(value_formats),
    }


def _compact_model(parsed: dict) -> dict:
    return {
        "model_name": parsed["model_name"],
        "n_classes": len(parsed["classes"]),
        "n_parameters": len(parsed["parameters"]),
        "gauge_groups": [g["name"] for g in parsed["gauge_groups"]],
        "classes": [
            {
                "label": c["label"],
                "class_name": c["class_name"],
                "quantum_numbers": c["quantum_numbers"],
                "indices": c["indices"],
            }
            for c in parsed["classes"]
        ],
        "parameters": [
            {"name": p["name"], "type": p["parameter_type"], "block": p["block_name"]}
            for p in parsed["parameters"]
        ],
    }


def _download(cache_dir: Path) -> list:
    import requests

    cache_dir.mkdir(parents=True, exist_ok=True)
    got = []
    for d in DOWNLOADS:
        if urlparse(d["url"]).hostname != _ALLOWED_HOST:
            print(f"  skip {d['name']}: host not allowlisted")
            continue
        dest = cache_dir / f"{d['name']}.fr"
        try:
            resp = requests.get(d["url"], timeout=30)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            sha = hashlib.sha256(resp.content).hexdigest()
            got.append({"name": d["name"], "path": dest, "url": d["url"],
                        "sha256": sha, "citation": d["citation"]})
            print(f"  fetched {d['name']} ({len(resp.content)} B, sha256 {sha[:12]}…)")
        except Exception as e:  # noqa: BLE001
            print(f"  skip {d['name']}: {e}")
    return got


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the FeynRules convention catalog")
    ap.add_argument("--out", default=str(REPO_ROOT / "docs"))
    ap.add_argument("--cache-dir", default=str(REPO_ROOT / "eval" / "reference_cache"))
    ap.add_argument("--download", action="store_true", help="fetch DB models to the cache")
    args = ap.parse_args()

    sources = list(IN_TREE)
    if args.download:
        print("Downloading reference models…")
        for d in _download(Path(args.cache_dir)):
            sources.append({"name": d["name"], "path": d["path"], "citation": d["citation"],
                            "url": d["url"], "sha256": d["sha256"]})
    else:
        # Pick up any previously-cached models.
        cache = Path(args.cache_dir)
        if cache.is_dir():
            for fr in sorted(cache.glob("*.fr")):
                sources.append({"name": fr.stem, "path": fr,
                                "citation": "cached FeynRules DB model"})

    models = {}
    full = {}
    src_records = []
    for s in sources:
        p = Path(s["path"])
        if not p.is_file():
            print(f"  skip {s['name']}: missing {p}")
            continue
        parsed = parse_fr_file(str(p))
        full[s["name"]] = parsed
        models[s["name"]] = _compact_model(parsed)
        rec = {"name": s["name"], "citation": s.get("citation")}
        if "url" in s:
            rec["url"] = s["url"]
            rec["sha256"] = s.get("sha256")
        else:
            rec["source"] = "in-tree fixture"
        src_records.append(rec)

    catalog = {
        "generated_by": "scripts/build_fr_convention_catalog.py",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sources": src_records,
        "models": models,
        "conventions": _summarize(full),
    }

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "fr_convention_catalog.json").write_text(json.dumps(catalog, indent=2))
    (out_dir / "fr_convention_catalog.md").write_text(_render_md(catalog))
    print(f"Catalog written to {out_dir}/fr_convention_catalog.{{json,md}} "
          f"({len(models)} models)")
    return 0


def _render_md(cat: dict) -> str:
    conv = cat["conventions"]
    lines = [
        "# FeynRules convention catalog",
        "",
        f"_Generated {cat['generated_utc']} by `scripts/build_fr_convention_catalog.py`._",
        "",
        "Survey of conventions across reference FeynRules model files, used to "
        "inform Lagrangian-extraction prompts and `.fr` generator defaults.",
        "",
        "## Sources",
        "",
    ]
    for s in cat["sources"]:
        extra = f" — {s['citation']}" if s.get("citation") else ""
        loc = s.get("url") or s.get("source", "")
        lines.append(f"- **{s['name']}** ({loc}){extra}")
    lines += ["", "## Conventions", ""]
    lines.append(f"- **Spin types**: {conv['naming_patterns']['spin_types']}")
    lines.append(f"- **Index conventions**: {conv['index_conventions']}")
    lines.append(f"- **Quantum-number keys**: {conv['quantum_numbers_usage']}")
    lines.append(f"- **Parameter types**: {conv['parameter_types']}")
    lines.append(f"- **LHA block names**: {conv['block_names']}")
    lines.append(f"- **Value formats**: {conv['value_formats']} "
                 "(rationals like `-1/3` must be preserved as strings)")
    lines += ["", "## Models", "", "| Model | classes | parameters | gauge groups |",
              "|---|---|---|---|"]
    for name, m in cat["models"].items():
        lines.append(f"| {name} ({m['model_name']}) | {m['n_classes']} | "
                     f"{m['n_parameters']} | {', '.join(m['gauge_groups']) or '—'} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    raise SystemExit(main())
