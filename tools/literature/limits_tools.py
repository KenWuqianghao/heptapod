"""
# limits_tools.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Experimental-limit tools: what has been measured about this model?

These tools ask whether the model a .fr describes is already excluded by
experiment. A model can transcribe its source paper perfectly and still
describe a region ruled out years earlier.

  AdsSearchTool             search NASA ADS, including full text
  FindExperimentalLimitsTool  model -> ranked papers reporting limits on it
  ExtractConstraintsTool    paper text -> the numeric bounds it reports

None of these decide whether a bound applies. They surface candidates with the
sentence each came from, for a physicist to judge.
"""

from __future__ import annotations

import json
import os
from typing import List, Optional

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField

from .ads_interface import AdsError, AdsInterface, summarize
from .constraints import (
    build_limit_queries,
    extract_limits,
    model_keywords,
    summarize_limits,
)

SCHEMA_VERSION = "limits-1.0"


def _safe_join(base_directory: str, rel_or_abs: str) -> Optional[str]:
    """Resolve under ``base_directory``; None if it escapes the sandbox."""
    if not rel_or_abs:
        return None
    base = os.path.realpath(base_directory)
    full = os.path.realpath(os.path.join(base, rel_or_abs))
    if full != base and not full.startswith(base + os.sep):
        return None
    return full


def _err(msg: str, **extra) -> str:
    return json.dumps({"status": "error", "error": msg,
                       "schema_version": SCHEMA_VERSION, **extra}, indent=2)


class AdsSearchTool(BaseTool):
    """Search NASA ADS for papers, including full-text search.

    ADS reaches published literature beyond hep-ph/hep-ex — the astrophysical
    and cosmological bounds on a BSM model — and can search the body of a
    paper, not just title and abstract, which is where a numeric limit
    usually sits.

    Query syntax is ADS Solr, e.g.
    ``abs:"leptoquark" AND full:"exclusion limit" AND year:2015-``.
    Requires an ADS API token (config.ads_token or ADS_API_TOKEN).
    """

    name: str = "ads_search"
    description: str = (
        "Search NASA ADS for physics papers, with optional full-text search. "
        "Complements INSPIRE (HEP metadata) and arXiv (preprints) by covering "
        "published astrophysical and cosmological literature."
    )

    query: str = RuntimeField(description="ADS query, e.g. abs:\"Z prime\" AND full:\"exclusion\"")
    rows: Optional[int] = RuntimeField(default=20, description="Max results (1-200)")
    sort: Optional[str] = RuntimeField(
        default="citation_count desc",
        description="ADS sort, e.g. 'citation_count desc' or 'date desc'")

    ads_token: Optional[str] = StateField(
        default=None, description="ADS API token; falls back to ADS_API_TOKEN")

    def _run(self) -> str:
        try:
            ads = AdsInterface(token=self.ads_token)
            docs = ads.search(self.query, rows=self.rows or 20,
                              sort=self.sort or "citation_count desc")
        except AdsError as e:
            return _err(str(e))
        return json.dumps({
            "status": "ok",
            "schema_version": SCHEMA_VERSION,
            "query": self.query,
            "n_results": len(docs),
            "results": [summarize(d) for d in docs],
        }, indent=2)


class FindExperimentalLimitsTool(BaseTool):
    """Find papers reporting experimental limits on a BSM model.

    Turns the model's field content into searches aimed at limit papers, then
    runs them against ADS. Without a token it still returns the queries, so
    the search can be run by hand or through INSPIRE.

    The result is a reading list ranked by citation count, not a verdict on
    whether the model is excluded.
    """

    name: str = "find_experimental_limits"
    description: str = (
        "Given a BSM model's name and new particles, find published papers "
        "that report experimental limits on it. Returns a ranked reading list "
        "plus the queries used."
    )

    model_name: str = RuntimeField(description="Model name, e.g. 'S1_LQ_RR'")
    particle_names: Optional[List[str]] = RuntimeField(
        default=None, description="New particle/class names in the model")
    extra_terms: Optional[List[str]] = RuntimeField(
        default=None, description="Extra physics terms to search for")
    year_from: Optional[int] = RuntimeField(
        default=2010, description="Earliest publication year")
    rows_per_query: Optional[int] = RuntimeField(
        default=8, description="Results per query (1-50)")

    ads_token: Optional[str] = StateField(
        default=None, description="ADS API token; falls back to ADS_API_TOKEN")

    def _run(self) -> str:
        keywords = model_keywords(self.model_name, self.particle_names,
                                  self.extra_terms)
        queries = build_limit_queries(self.model_name, self.particle_names,
                                      self.extra_terms,
                                      year_from=self.year_from or 2010)
        out = {
            "status": "ok",
            "schema_version": SCHEMA_VERSION,
            "model_name": self.model_name,
            "keywords": keywords,
            "queries": queries,
            "caveat": "A reading list, not a verdict. Whether a limit applies "
                      "depends on production mode, branching fractions and the "
                      "analysis's own assumptions.",
        }
        if not keywords:
            out["note"] = ("No known BSM vocabulary matched this model's names. "
                           "Pass extra_terms with the physics terms to search.")

        ads = AdsInterface(token=self.ads_token)
        if not ads.has_token:
            out["papers"] = []
            out["note"] = ("No ADS token configured, so only the queries are "
                           "returned. Set config.ads_token or ADS_API_TOKEN, "
                           "or run these against INSPIRE.")
            return json.dumps(out, indent=2)

        rows = max(1, min(int(self.rows_per_query or 8), 50))
        papers, seen, errors = [], set(), []
        for q in queries:
            try:
                for doc in ads.search(q["ads"], rows=rows,
                                      sort=q.get("sort", "citation_count desc")):
                    bib = doc.get("bibcode")
                    if bib and bib not in seen:
                        seen.add(bib)
                        rec = summarize(doc)
                        rec["matched_query"] = q["label"]
                        papers.append(rec)
            except AdsError as e:
                errors.append({"query": q["label"], "error": str(e)})
        # Experimental analyses first, newest first within them, and citation
        # count only as the final tie-break. Sorting the whole list by
        # citations puts famous theory reviews on top, which is exactly the
        # wrong reading order for "what constrains this model".
        def rank(r: dict) -> tuple:
            experimental = "experimental searches" in (r.get("matched_query") or "")
            try:
                year = int(r.get("year") or 0)
            except (TypeError, ValueError):
                year = 0
            return (0 if experimental else 1, -year, -(r.get("citation_count") or 0))

        papers.sort(key=rank)
        out["papers"] = papers
        out["n_papers"] = len(papers)
        if errors:
            out["errors"] = errors
        return json.dumps(out, indent=2)


class ExtractConstraintsTool(BaseTool):
    """Pull the numeric bounds out of a paper's text.

    Reads the three ways a limit is normally written — "masses below X TeV are
    excluded", "m > X TeV", "an upper limit of X fb" — and returns each with
    the sentence it came from.

    Deliberately conservative: inequalities only count inside a sentence that
    also talks about excluding, limiting or constraining, so index ranges and
    kinematic cuts do not become "limits".
    """

    name: str = "extract_constraints"
    description: str = (
        "Extract reported experimental limits (mass, cross-section, coupling) "
        "from a paper's text, each with its source sentence for checking."
    )

    text: Optional[str] = RuntimeField(
        default=None, description="Paper text; use text_path instead for files")
    text_path: Optional[str] = RuntimeField(
        default=None, description="Path to a text file, relative to base_directory")
    max_records: Optional[int] = RuntimeField(
        default=60, description="Cap on returned records")

    base_directory: str = StateField(description="Base sandbox directory")

    def _run(self) -> str:
        body = self.text or ""
        if not body and self.text_path:
            path = _safe_join(self.base_directory, self.text_path)
            if not path:
                return _err(f"path escapes the sandbox: {self.text_path}")
            if not os.path.isfile(path):
                return _err(f"file not found: {self.text_path}")
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as fh:
                    body = fh.read()
            except OSError as e:
                return _err(f"could not read {self.text_path}: {e}")
        if not body.strip():
            return _err("no text supplied (pass text or text_path)")

        records = extract_limits(body, max_records=self.max_records or 60)
        return json.dumps({
            "status": "ok",
            "schema_version": SCHEMA_VERSION,
            "n_records": len(records),
            "summary": summarize_limits(records),
            "limits": records,
        }, indent=2)
