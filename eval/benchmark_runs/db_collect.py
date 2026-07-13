#!/usr/bin/env python3
"""Collect fleet outputs: recover each model_json, run the DETERMINISTIC
GenerateFeynRulesModelTool on it (real schema validation), then score the
resulting .fr against the physicist's reference with eval.reference_bench.

Emits db_benchmark_report.{json,md} with per-model rows and aggregates, and a
per-model breakdown of the funnel/validation/scoring outcome. Honest by
construction: extraction failures, validation failures, and scoring artifacts
are all rows, not omissions.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

from tools.frgen.frgen_tool import GenerateFeynRulesModelTool  # noqa: E402
from eval.reference_bench import score  # noqa: E402

SM_FR = str(REPO / "tools" / "feynrules" / "test_files" / "models" / "SM.fr")


def recover_json(report: Path):
    if not report.is_file():
        return None, "no codex output"
    txt = report.read_text()
    blocks = re.findall(r"```json\s*\n(.*?)```", txt, re.S)
    if not blocks:
        blocks = re.findall(r"```\s*\n(\{.*?\})\s*```", txt, re.S)
    if not blocks:
        return None, "no fenced json block"
    try:
        return json.loads(blocks[-1]), None
    except json.JSONDecodeError as e:
        return None, f"json parse error: {e}"


def main() -> int:
    cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
    rows = []
    for c in cands:
        page = c["page"]
        rdir = HERE / page
        row = {"page": page, "category": c["category"], "arxiv": c["arxiv_id"],
               "reference_fr": c["reference_fr"], "n_ref_new_fields": c["n_new_fields"]}
        mj, err = recover_json(rdir / "codex_out.md")
        if mj is None:
            row["status"] = f"extraction_failed: {err}"
            rows.append(row); continue
        gen_raw = GenerateFeynRulesModelTool(
            model_json=json.dumps(mj), output_path=f"model/{page}_gen.fr",
            base_directory=str(rdir))._run()
        if not gen_raw.lstrip().startswith("{"):
            row["status"] = "schema_validation_failed"
            row["validation_error"] = gen_raw.splitlines()[1][:200] if "\n" in gen_raw else gen_raw[:200]
            rows.append(row); continue
        gen = json.loads(gen_raw)
        row["generated_fr"] = f"eval/benchmark_runs/{page}/{gen['fr_path']}"
        try:
            s = score(str(rdir / gen["fr_path"]), str(REPO / c["reference_fr"]), sm_fr=SM_FR)
        except Exception as e:  # noqa: BLE001
            row["status"] = f"scoring_failed: {type(e).__name__}: {str(e)[:120]}"
            rows.append(row); continue
        row["status"] = "scored"
        row["sm_subtracted"] = s["sm_subtracted"]
        row["fields"] = s["n_fields"]
        row["field_f1"] = s["field_signature"]["f1"]
        row["field_precision"] = s["field_signature"]["precision"]
        row["field_recall"] = s["field_signature"]["recall"]
        row["qn_f1"] = s["quantum_number_values"]["f1"]
        row["param_jaccard"] = s["parameter_name_jaccard"]
        row["n_params"] = s["n_parameters"]
        row["detail"] = {"missed": [x for x in s["reference_field_signatures"]
                                     if x not in s["generated_field_signatures"]],
                         "extra": [x for x in s["generated_field_signatures"]
                                    if x not in s["reference_field_signatures"]]}
        rows.append(row)

    scored = [r for r in rows if r["status"] == "scored"]
    agg = {}
    if scored:
        agg = {
            "n_scored": len(scored),
            "n_extraction_failed": sum(1 for r in rows if r["status"].startswith("extraction")),
            "n_validation_failed": sum(1 for r in rows if r["status"].startswith("schema")),
            "mean_field_f1": round(sum(r["field_f1"] for r in scored) / len(scored), 3),
            "mean_field_precision": round(sum(r["field_precision"] for r in scored) / len(scored), 3),
            "mean_field_recall": round(sum(r["field_recall"] for r in scored) / len(scored), 3),
            "mean_qn_f1": round(sum(r["qn_f1"] for r in scored) / len(scored), 3),
            "median_field_f1": sorted(r["field_f1"] for r in scored)[len(scored) // 2],
            "perfect_f1": sum(1 for r in scored if r["field_f1"] == 1.0),
        }
    (HERE / "db_benchmark_report.json").write_text(json.dumps({"aggregate": agg, "rows": rows}, indent=2))

    lines = ["# FeynRules model-database benchmark — Codex gpt-5.5 (medium)", "",
             "Pipeline: paper (local text) → Codex extraction → deterministic "
             "generator (schema-validated) → scored vs the physicist's reference "
             "`.fr` (name-independent field signatures; SM baseline subtracted "
             "for standalone references).", "",
             f"**Aggregate over {agg.get('n_scored', 0)} scored models:** "
             f"mean field F1 **{agg.get('mean_field_f1', '—')}** "
             f"(P {agg.get('mean_field_precision', '—')} / R {agg.get('mean_field_recall', '—')}), "
             f"median {agg.get('median_field_f1', '—')}, perfect {agg.get('perfect_f1', 0)}; "
             f"extraction failures {agg.get('n_extraction_failed', 0)}, "
             f"validation failures {agg.get('n_validation_failed', 0)}.", "",
             "| Model | Category | Ref new fields | Gen fields | Field P | R | F1 | QN F1 | Param Jacc | Status |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda x: -(x.get("field_f1") or -1)):
        if r["status"] == "scored":
            lines.append(f"| {r['page']} | {r['category']} | {r['fields']['reference']} | "
                         f"{r['fields']['generated']} | {r['field_precision']} | {r['field_recall']} | "
                         f"**{r['field_f1']}** | {r['qn_f1']} | {r['param_jaccard']} | scored |")
        else:
            lines.append(f"| {r['page']} | {r['category']} | {r['n_ref_new_fields']} | — | — | — | — | — | — | {r['status'][:60]} |")
    lines += ["", "## Caveats", "",
              "1. **Training-data confound:** every reference implementation is public and "
              "predates the model's training; high scores partly reflect recall of known "
              "implementations, not only paper extraction. A confound-free test needs papers "
              "with no public implementation.",
              "2. **No compilation check:** no Mathematica license — scores measure extraction "
              "fidelity of field/parameter content, not UFO-compilability.",
              "3. Reference choice for multi-file models is heuristic (name-similarity, then "
              "size); the chosen file is recorded per row.",
              "4. Signature matching is name-independent (spin, colour rep, Q/Y). Fields "
              "differing only by chirality/mass-basis conventions can collide (see TypeIIISeeSaw "
              "in the gated-out list).",
              "5. **LeptoQuark's F1=0 is a reference artifact, not an extraction failure**: the "
              "extraction recovered the paper's vector leptoquark + coloron + Z' (visible as "
              "'extra' signatures), but the multi-file heuristic picked the bundle's vector-like-"
              "fermion component (`VLferm.fr`) as the reference. Multi-file bundles need "
              "per-component references."]
    (HERE / "db_benchmark_report.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(agg, indent=2))
    print(f"\nreport: eval/benchmark_runs/db_benchmark_report.{{json,md}}  ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
