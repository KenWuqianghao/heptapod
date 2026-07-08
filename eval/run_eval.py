"""
# run_eval.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Benchmark runner for the Lagrangian-extraction pipeline.

Runs each benchmark case through the full chain — extract -> generate -> validate
— scores extraction against the expected model, and aggregates headline metrics
(extraction score, particle recall, end-to-end validation pass rate). A live run
needs a configured LLM provider (extraction) and FeynRules + wolframscript
(validation); the scoring itself (eval/scoring.py) is deterministic and unit
tested. Import-safe: config is only read in main().
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from eval.scoring import aggregate, score_case
from tools.extract.extract_tool import ExtractLagrangianTool
from tools.frgen.frgen_tool import GenerateFeynRulesModelTool
from tools.literature.literature_tools import (
    ArxivSourceTool,
    ExtractPaperTextTool,
    FetchPaperPDFTool,
)
from tools.validate.validate_tool import ValidateModelTool


def _try_json(raw: str) -> Optional[Dict[str, Any]]:
    try:
        obj = json.loads(raw)
        return obj if isinstance(obj, dict) else None
    except (json.JSONDecodeError, TypeError):
        return None


def _first_line(raw: str) -> str:
    return raw.strip().splitlines()[0] if raw and raw.strip() else ""


def _resolve_paper_text(case: Dict[str, Any], base_directory: str) -> Dict[str, Any]:
    """Return {paper_text|text_path} for a case.

    Preference order: inline text -> arXiv LaTeX source (equations survive
    exactly) -> PDF text extraction as the fallback.
    """
    if case.get("paper_text"):
        return {"paper_text": case["paper_text"]}
    arxiv_id = case.get("arxiv_id")
    if not arxiv_id:
        return {}

    # Primary: LaTeX e-print source.
    src = _try_json(
        ArxivSourceTool(arxiv_id=arxiv_id, base_directory=base_directory)._run()
    )
    if src and src.get("status") == "ok" and src.get("tex_path"):
        return {"text_path": src["tex_path"]}

    # Fallback: PDF -> plain text.
    fr = _try_json(FetchPaperPDFTool(arxiv_id=arxiv_id, base_directory=base_directory)._run())
    if not fr or fr.get("status") != "ok":
        return {}
    ex = _try_json(
        ExtractPaperTextTool(pdf_path=fr["pdf_path"], base_directory=base_directory)._run()
    )
    if not ex or ex.get("status") != "ok":
        return {}
    return {"text_path": ex["text_path"]}


def run_case(
    case: Dict[str, Any],
    base_directory: str,
    feynrules_path: str,
    wolframscript_path: str,
    provider: str = "ollama",
    model: Optional[str] = None,
) -> Dict[str, Any]:
    """Run one benchmark case through extract -> generate -> validate + score."""
    name = case["name"]
    record: Dict[str, Any] = {
        "name": name,
        "extracted": False,
        "generated": False,
        "validated": False,
        "score": None,
        "errors": [],
    }

    text_kwargs = _resolve_paper_text(case, base_directory)
    if not text_kwargs:
        record["errors"].append("no paper text (missing paper_text and arXiv fetch failed)")
        return record

    ex_raw = ExtractLagrangianTool(
        scenario=case.get("scenario"),
        llm_provider=provider,
        model=model,
        base_directory=base_directory,
        output_path=f"models/{name}.json",
        **text_kwargs,
    )._run()
    ex_res = _try_json(ex_raw)
    if not ex_res or ex_res.get("status") != "ok" or "model" not in ex_res:
        record["errors"].append(f"extraction: {_first_line(ex_raw)}")
        return record
    model_dict = ex_res["model"]
    record["extracted"] = True
    record["score"] = score_case(model_dict, case.get("expected", {}))

    gen_raw = GenerateFeynRulesModelTool(
        model_json=json.dumps(model_dict),
        output_path=f"models/{name}.fr",
        base_directory=base_directory,
    )._run()
    gen_res = _try_json(gen_raw)
    if not gen_res or gen_res.get("status") != "ok":
        record["errors"].append(f"generation: {_first_line(gen_raw)}")
        return record
    record["generated"] = True

    val_raw = ValidateModelTool(
        model_path=gen_res["fr_path"],
        feynrules_model_json=json.dumps(model_dict),
        output_dir=f"UFO_{name}",
        base_directory=base_directory,
        feynrules_path=feynrules_path,
        wolframscript_path=wolframscript_path,
    )._run()
    val_res = _try_json(val_raw)
    if val_res is None:
        record["errors"].append(f"validation: {_first_line(val_raw)}")
    else:
        record["validated"] = bool(val_res.get("passed"))
        record["validation_checks"] = val_res.get("checks")
    return record


def _render_report_md(report: Dict[str, Any]) -> str:
    agg = report["aggregate"]
    lines = ["# Lagrangian-extraction benchmark report", ""]
    lines.append(f"- cases: {agg.get('n_cases', 0)}")
    lines.append(f"- extraction rate: {agg.get('extraction_rate', 0):.2f}")
    lines.append(f"- generation rate: {agg.get('generation_rate', 0):.2f}")
    lines.append(f"- validation pass rate: {agg.get('validation_pass_rate', 0):.2f}")
    lines.append(f"- mean extraction score: {agg.get('mean_extraction_score', 0):.2f}")
    lines.append(f"- mean particle recall: {agg.get('mean_particle_recall', 0):.2f}")
    lines.append("")
    lines.append("| case | extracted | generated | validated | extraction score |")
    lines.append("|---|---|---|---|---|")
    for r in report["cases"]:
        s = r["score"]["extraction_score"] if r.get("score") else 0.0
        lines.append(
            f"| {r['name']} | {r['extracted']} | {r['generated']} "
            f"| {r['validated']} | {s:.2f} |"
        )
    return "\n".join(lines) + "\n"


def run_benchmark(
    cases: List[Dict[str, Any]],
    base_directory: str,
    feynrules_path: str,
    wolframscript_path: str,
    provider: str = "ollama",
    model: Optional[str] = None,
) -> Dict[str, Any]:
    """Run all cases, aggregate, and write eval_report.json / .md into the sandbox."""
    os.makedirs(base_directory, exist_ok=True)
    results = [
        run_case(c, base_directory, feynrules_path, wolframscript_path, provider, model)
        for c in cases
    ]
    report = {"aggregate": aggregate(results), "cases": results}
    with open(os.path.join(base_directory, "eval_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    with open(os.path.join(base_directory, "eval_report.md"), "w", encoding="utf-8") as fh:
        fh.write(_render_report_md(report))
    return report


def main() -> int:
    from eval.benchmarks import BENCHMARKS

    try:
        from config import feynrules_path, wolframscript_path
    except Exception as e:  # noqa: BLE001
        print(f"config.py not set up ({e}); cannot run the live benchmark.")
        return 1

    provider = os.environ.get("EVAL_PROVIDER", "ollama")
    model = os.environ.get("EVAL_MODEL") or None
    base_directory = str(REPO_ROOT / "examples" / "eval_sandbox")

    report = run_benchmark(
        BENCHMARKS, base_directory, feynrules_path, wolframscript_path, provider, model
    )
    print(_render_report_md(report))
    print(f"Report written to {base_directory}/eval_report.{{json,md}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
