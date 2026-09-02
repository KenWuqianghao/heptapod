#!/usr/bin/env python3
"""
# test_limits.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Tests for the ADS client and the experimental-limit extraction.

No network and no ADS token: the client is exercised against a stub session,
and the extraction is pure text work. Run directly, like the other suites:

    python tools/literature/test_limits.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(TOOL_DIR))
sys.path.insert(0, REPO_ROOT)

from tools.literature.ads_interface import (  # noqa: E402
    AdsError, AdsInterface, arxiv_id_of, resolve_token, summarize,
)
from tools.literature.constraints import (  # noqa: E402
    build_limit_queries, extract_limits, model_keywords, summarize_limits,
)

_PASSED = 0
_FAILED = 0


def check(cond: bool, label: str) -> None:
    global _PASSED, _FAILED
    if cond:
        _PASSED += 1
        print(f"[✓] {label}")
    else:
        _FAILED += 1
        print(f"[✗] {label}")


class _StubResponse:
    def __init__(self, payload, status=200):
        self._payload = payload
        self.status_code = status
        self.text = json.dumps(payload) if isinstance(payload, dict) else str(payload)

    def json(self):
        if isinstance(self._payload, dict):
            return self._payload
        raise ValueError("not json")


class _StubSession:
    """Records calls and replays canned responses; no network."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = []

    def get(self, url, params=None, headers=None, timeout=None):
        self.calls.append({"url": url, "params": params, "headers": headers})
        return self._responses.pop(0) if self._responses else _StubResponse({}, 200)


def _docs(*titles):
    return {"response": {"numFound": len(titles), "docs": [
        {"bibcode": f"2020PhRvD..{i:03d}X", "title": [t], "author": ["A. Author", "B."],
         "year": "2020", "pub": "Phys. Rev. D", "citation_count": 10 * (i + 1),
         "identifier": [f"arXiv:2001.{i:05d}"], "abstract": "abs"}
        for i, t in enumerate(titles)]}}


# --------------------------------------------------------------------- ADS
def test_token_resolution() -> None:
    """Precedence is argument -> config.ads_token -> ADS_API_TOKEN.

    The config leg has to be neutralised explicitly: on a machine where
    config.ads_token is set, config wins and the environment leg is never
    reached, so asserting on the env var alone makes the test pass or fail
    depending on whose laptop it runs on.
    """
    print("\n>> ADS token resolution...")
    old_env = os.environ.pop("ADS_API_TOKEN", None)
    try:
        import config as _cfg
    except Exception:                                      # noqa: BLE001
        _cfg = None
    had_cfg = _cfg is not None and hasattr(_cfg, "ads_token")
    old_cfg = getattr(_cfg, "ads_token", None) if _cfg else None
    try:
        check(resolve_token("explicit") == "explicit", "explicit argument wins")

        if _cfg is not None:
            _cfg.ads_token = "from-config"
            os.environ["ADS_API_TOKEN"] = "from-env"
            check(resolve_token() == "from-config", "config beats the environment")
            del _cfg.ads_token
        else:
            os.environ["ADS_API_TOKEN"] = "from-env"

        check(resolve_token() == "from-env", "falls back to ADS_API_TOKEN")
        os.environ.pop("ADS_API_TOKEN", None)
        check(resolve_token() is None, "no token configured resolves to None")
    finally:
        if old_env is not None:
            os.environ["ADS_API_TOKEN"] = old_env
        if _cfg is not None:
            if had_cfg:
                _cfg.ads_token = old_cfg
            elif hasattr(_cfg, "ads_token"):
                del _cfg.ads_token


def test_ads_requires_token() -> None:
    print("\n>> ADS refuses to call without a token...")
    old = os.environ.pop("ADS_API_TOKEN", None)
    try:
        ads = AdsInterface(token=None, session=_StubSession([]))
        # config.ads_token might be set on a dev machine; only assert when not.
        if ads.has_token:
            check(True, "token present from config; skipped no-token assertion")
            return
        try:
            ads.search("abs:test")
            check(False, "should have raised AdsError")
        except AdsError as e:
            check("token" in str(e).lower(), "AdsError names the missing token")
    finally:
        if old is not None:
            os.environ["ADS_API_TOKEN"] = old


def test_ads_search_and_summary() -> None:
    print("\n>> ADS search, headers and summary...")
    sess = _StubSession([_StubResponse(_docs("Search for leptoquarks",
                                             "Limits on Z prime"))])
    ads = AdsInterface(token="tok", session=sess)
    docs = ads.search('abs:"leptoquark"', rows=5)
    check(len(docs) == 2, "returns both docs")
    hdr = sess.calls[0]["headers"]["Authorization"]
    check(hdr == "Bearer tok", "sends bearer token")
    check(sess.calls[0]["params"]["rows"] == 5, "passes rows through")

    s = summarize(docs[0])
    check(s["title"] == "Search for leptoquarks", "title unwrapped from list")
    check(s["arxiv_id"] == "arXiv:2001.00000".split(":", 1)[1],
          "arXiv id pulled from identifiers")
    check(s["n_authors"] == 2, "author count")


def test_ads_row_cap_and_errors() -> None:
    print("\n>> ADS row cap and error mapping...")
    sess = _StubSession([_StubResponse(_docs("x"))])
    AdsInterface(token="t", session=sess).search("q", rows=9999)
    check(sess.calls[0]["params"]["rows"] == 200, "rows capped at 200")

    for code, word in ((401, "token"), (429, "rate limit")):
        s = _StubSession([_StubResponse({"err": 1}, status=code)])
        try:
            AdsInterface(token="t", session=s).search("q")
            check(False, f"{code} should raise")
        except AdsError as e:
            check(word in str(e).lower(), f"{code} maps to a clear message")


def test_arxiv_id_extraction() -> None:
    print("\n>> arXiv id extraction from ADS docs...")
    check(arxiv_id_of({"identifier": ["2020PhRvD", "arXiv:2103.02708"]})
          == "2103.02708", "finds arXiv id")
    check(arxiv_id_of({"identifier": ["doi:10.1000/x"]}) is None,
          "None when absent")


# ------------------------------------------------------------- query building
def test_model_keywords() -> None:
    print("\n>> model name -> physics vocabulary...")
    check("leptoquark" in model_keywords("S1_LQ_RR", ["S1"]),
          "LQ in the model name reaches leptoquark")
    check("Z prime" in model_keywords("Top-Philic-Zprime", ["Zp"]),
          "Zprime reaches Z prime")
    check(any("neutral lepton" in k for k in model_keywords("HeavyN", ["N1"])),
          "HeavyN reaches heavy neutral lepton")
    check(model_keywords("Wprime") != model_keywords("HeavyN"),
          "different models give different vocabulary")
    check("my term" in model_keywords("Unknown", None, ["my term"]),
          "extra terms are carried through")


def test_build_queries() -> None:
    print("\n>> limit queries...")
    qs = build_limit_queries("S1_LQ_RR", ["S1"], year_from=2015)
    check(len(qs) > 0, "produces queries")
    check(all({"label", "ads", "inspire"} <= set(q) for q in qs),
          "every query has ads and inspire forms")
    check(any("leptoquark" in q["ads"] for q in qs), "searches for leptoquark")
    check(any("2015-" in q["ads"] for q in qs), "honours year_from")
    check(build_limit_queries("", None) == [], "no model, no queries")


# ------------------------------------------------------------ limit extraction
def test_extract_exclusion_phrases() -> None:
    print("\n>> 'masses below X are excluded'...")
    recs = extract_limits(
        "Scalar leptoquark masses below 1.7 TeV are excluded at 95% CL.")
    check(len(recs) >= 1, "finds a record")
    r = recs[0]
    check(r["value"] == 1.7 and r["unit"] == "TeV", "value and unit parsed")
    check(r["relation"] == ">", "exclusion below X becomes a lower bound")
    check("95" in (r["confidence_level"] or ""), "confidence level captured")
    check("excluded" in r["sentence"], "keeps the source sentence")


def test_extract_excluded_range() -> None:
    """'between X and Y are excluded' is a band, not a single bound.

    Collaboration abstracts phrase exclusions this way constantly. The
    single-sided pattern also matches the upper number, so without explicit
    range handling the band would be recorded as a plain lower bound and the
    lower edge would be silently lost.
    """
    print("\n>> excluded ranges...")
    recs = extract_limits(
        "Leptoquark masses between 1.5 and 3.0 TeV are excluded at 95% CL.")
    check(len(recs) == 1, f"one record, not two (got {len(recs)})")
    r = recs[0]
    check(r["kind"] == "exclusion_range", "recorded as a range")
    check(r["range_low"] == 1.5 and r["range_high"] == 3.0, "both edges kept")
    check(r["unit"] == "TeV", "unit parsed")

    dashed = extract_limits("Masses in the range 0.5-1.2 TeV are excluded.")
    check(dashed and dashed[0]["range_low"] == 0.5, "hyphenated range form")


def test_extract_inequalities() -> None:
    print("\n>> inequalities only inside result sentences...")
    recs = extract_limits("We exclude the region with M_{Zp} > 4.5 TeV.")
    check(any(r["value"] == 4.5 for r in recs), "reads M > 4.5 TeV")

    noise = extract_limits("The index i > 3 runs over generations.")
    check(noise == [], "a bare inequality is not a limit")


def test_extract_upper_limit_of() -> None:
    print("\n>> 'an upper limit of X fb'...")
    recs = extract_limits(
        "The analysis sets an upper limit of 0.12 fb on the production "
        "cross section at 95% CL.")
    check(len(recs) >= 1, "finds the limit")
    r = [x for x in recs if x["unit"] == "fb"][0]
    check(r["relation"] == "<", "upper limit is an upper bound")
    check(abs(r["value"] - 0.12) < 1e-9, "value parsed")


def test_scientific_notation() -> None:
    print("\n>> scientific notation...")
    recs = extract_limits(
        r"We constrain the mixing to |V|^2 < 3.2\times10^{-5} at 90% CL.")
    check(any(abs((r["value"] or 0) - 3.2e-5) < 1e-12 for r in recs),
          r"parses 3.2\times10^{-5}")


def test_dedupe_and_summary() -> None:
    print("\n>> dedup and summary...")
    text = ("Masses below 1.5 TeV are excluded. "
            "Masses below 1.5 TeV are excluded. "
            "Masses below 900 GeV are excluded.")
    recs = extract_limits(text)
    vals = sorted({r["value"] for r in recs})
    check(vals == [900.0, 1500.0] or vals == [900.0, 1.5] or len(recs) == 2,
          f"identical records collapse (got {vals})")

    s = summarize_limits(recs)
    check(s["n_records"] == len(recs), "summary counts records")
    check(s["strongest_mass_lower_bound"] is not None, "reports strongest bound")
    check("caveat" in s, "summary carries the caveat")


def test_empty_and_garbage() -> None:
    print("\n>> empty and non-physics input...")
    check(extract_limits("") == [], "empty text")
    check(extract_limits("The quick brown fox jumps over the lazy dog.") == [],
          "prose with no limits")


def test_extract_tool_sandbox() -> None:
    print("\n>> ExtractConstraintsTool path safety...")
    from tools.literature.limits_tools import ExtractConstraintsTool
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "paper.txt")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("Masses below 2.1 TeV are excluded at 95% CL.")
        out = json.loads(ExtractConstraintsTool(
            text_path="paper.txt", base_directory=td)._run())
        check(out["status"] == "ok" and out["n_records"] >= 1,
              "reads a file in the sandbox")

        esc = json.loads(ExtractConstraintsTool(
            text_path="../../../etc/passwd", base_directory=td)._run())
        check(esc["status"] == "error", "refuses to escape the sandbox")

        none = json.loads(ExtractConstraintsTool(base_directory=td)._run())
        check(none["status"] == "error", "errors when given no text")


def test_find_limits_without_token() -> None:
    print("\n>> FindExperimentalLimitsTool degrades without a token...")
    from tools.literature.limits_tools import FindExperimentalLimitsTool
    old = os.environ.pop("ADS_API_TOKEN", None)
    try:
        out = json.loads(FindExperimentalLimitsTool(
            model_name="S1_LQ_RR", particle_names=["S1"])._run())
        check(out["status"] == "ok", "still succeeds")
        check(len(out["queries"]) > 0, "returns queries to run by hand")
        check("caveat" in out, "carries the caveat")
    finally:
        if old is not None:
            os.environ["ADS_API_TOKEN"] = old


def main() -> int:
    print("=" * 66)
    print("ADS client + experimental-limit extraction")
    print("=" * 66)
    for fn in (test_token_resolution, test_ads_requires_token,
               test_ads_search_and_summary, test_ads_row_cap_and_errors,
               test_arxiv_id_extraction, test_model_keywords,
               test_build_queries, test_extract_exclusion_phrases,
               test_extract_excluded_range, test_extract_inequalities,
               test_extract_upper_limit_of,
               test_scientific_notation, test_dedupe_and_summary,
               test_empty_and_garbage, test_extract_tool_sandbox,
               test_find_limits_without_token):
        try:
            fn()
        except Exception as e:                             # noqa: BLE001
            global _FAILED
            _FAILED += 1
            print(f"[✗] {fn.__name__} raised {type(e).__name__}: {e}")
    print("\n" + "=" * 66)
    print(f"Total: {_PASSED}/{_PASSED + _FAILED} checks passed")
    if _FAILED:
        print("Test suite completed with failures! [✗]")
        return 1
    print("[✓] All tests passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
