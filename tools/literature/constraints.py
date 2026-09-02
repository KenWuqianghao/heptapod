"""
# constraints.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Find and read the experimental limits on a BSM model.

Two halves, both pure text work with no network:

  ``build_limit_queries``  a model's field content -> literature queries aimed
                           at papers that report exclusion limits on it
  ``extract_limits``       a paper's text -> the numeric bounds it reports,
                           as structured records

This asks "is the model the .fr describes already excluded by measurement?"
— a model can be a faithful transcription of its paper and still sit in a
region ruled out years ago.

**These are search aids and a first-pass reading, not a statistical
statement.** A limit means nothing without its context: the assumed
production mode, the branching fractions, the confidence level, and whether
the analysis applies to this model at all. Every extracted record therefore
carries the sentence it came from, so a physicist can check it.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Optional

# ---------------------------------------------------------------------------
# Model vocabulary -> the words experimenters actually use in a title/abstract.
# Keyed by a token that shows up in FeynRules field names, class names or the
# model name. Deliberately broad: a missed query costs a search, a wrong one
# costs a physicist's afternoon.
# ---------------------------------------------------------------------------
PARTICLE_VOCAB: Dict[str, List[str]] = {
    "leptoquark": ["leptoquark", "LQ"],
    "lq": ["leptoquark"],
    "sextet": ["colour sextet", "color sextet", "diquark"],
    "zp": ["Z prime", "Z'", "heavy neutral gauge boson"],
    "zprime": ["Z prime", "Z'", "heavy neutral gauge boson"],
    "wp": ["W prime", "W'", "heavy charged gauge boson"],
    "wprime": ["W prime", "W'"],
    "heavyn": ["heavy neutral lepton", "sterile neutrino", "heavy neutrino"],
    "hnl": ["heavy neutral lepton", "sterile neutrino"],
    "nr": ["right-handed neutrino", "sterile neutrino"],
    "vlq": ["vector-like quark", "vectorlike quark"],
    "vectorlike": ["vector-like quark", "vector-like lepton"],
    "dm": ["dark matter", "WIMP"],
    "darkmatter": ["dark matter", "relic abundance", "direct detection"],
    "axion": ["axion", "axion-like particle", "ALP"],
    "alp": ["axion-like particle", "ALP"],
    "monotop": ["monotop"],
    "diquark": ["diquark"],
    "seesaw": ["seesaw", "neutrino mass"],
    "triplet": ["scalar triplet", "type-II seesaw", "doubly charged"],
    "doublycharged": ["doubly charged scalar", "type-II seesaw"],
    "stop": ["top squark", "stop"],
    "squark": ["squark"],
    "gluino": ["gluino"],
    "neutralino": ["neutralino"],
    "higgs": ["extended Higgs sector", "heavy Higgs"],
    "chargedhiggs": ["charged Higgs"],
    "composite": ["composite Higgs", "vector resonance"],
    "technicolor": ["technicolour", "technicolor"],
}

# Phrases that mark a paper as reporting a limit rather than proposing a model.
_LIMIT_PHRASES = [
    '"exclusion limit"', '"upper limit"', '"lower limit"',
    '"excluded at 95"', '"95% CL"', '"confidence level"',
]

# Matched as AUTHORS, not affiliations or abstract words. ADS indexes
# collaboration papers under "<NAME> Collaboration", which is the only
# reliable way to separate an experimental analysis from the many theory
# papers that merely mention ATLAS. Searching abs:"ATLAS" returns
# phenomenology; author:"ATLAS Collaboration" returns the search itself.
_COLLABORATIONS = [
    "ATLAS Collaboration", "CMS Collaboration", "LHCb Collaboration",
    "Belle Collaboration", "BaBar Collaboration", "XENON Collaboration",
    "LZ Collaboration", "IceCube Collaboration", "Fermi-LAT Collaboration",
    "Planck Collaboration",
]


def _tokens(*sources: Optional[Iterable[str]]) -> List[str]:
    """Lowercase alphanumeric tokens from field/class/model names."""
    out: List[str] = []
    for src in sources:
        for s in src or []:
            if not s:
                continue
            out += re.findall(r"[A-Za-z]+", str(s).lower())
    return out


def model_keywords(model_name: str = "",
                   particle_names: Optional[Iterable[str]] = None,
                   extra: Optional[Iterable[str]] = None) -> List[str]:
    """Physics search terms implied by a model's names.

    Matches vocabulary keys as substrings of the tokens, so ``S1LQ``,
    ``LQ_RR`` and ``leptoquark`` all reach the leptoquark vocabulary.
    """
    toks = _tokens([model_name], particle_names, extra)
    joined = " ".join(toks) + " " + (model_name or "").lower()
    hits: List[str] = []
    for key, words in PARTICLE_VOCAB.items():
        if key in joined or any(key in t for t in toks):
            for w in words:
                if w not in hits:
                    hits.append(w)
    for e in extra or []:
        if e and e not in hits:
            hits.append(str(e))
    return hits


def build_limit_queries(model_name: str = "",
                        particle_names: Optional[Iterable[str]] = None,
                        extra_terms: Optional[Iterable[str]] = None,
                        year_from: int = 2010) -> List[Dict[str, str]]:
    """Literature queries aimed at experimental limits on this model.

    Returns ``[{"label", "ads", "inspire", "sort"}]`` — the same intent
    expressed for both back ends, because ADS reaches astrophysical bounds and
    full text while INSPIRE is better on collider analyses.

    Each query carries its own ``sort``, which matters more than it looks.
    Ranking limit papers by citation count surfaces famous theory reviews,
    because a review of a model is cited far more than the experimental
    analysis that constrains it. Collaboration searches are therefore sorted
    newest-first: a 2026 limit supersedes the 2015 one, and the recent paper
    is the one worth reading.
    """
    kws = model_keywords(model_name, particle_names, extra_terms)
    if not kws:
        # Nothing recognised: fall back to the model's own name so the caller
        # still gets a usable starting query rather than an empty list.
        kws = [model_name] if model_name else []
    if not kws:
        return []

    queries: List[Dict[str, str]] = []
    phrase_or = " OR ".join(_LIMIT_PHRASES)

    collabs = " OR ".join(f'"{c}"' for c in _COLLABORATIONS)

    for kw in kws[:6]:                       # keep the fan-out sane
        q = f'"{kw}"'
        # The experimental analyses themselves: newest first, because a later
        # limit supersedes an earlier one.
        queries.append({
            "label": f"{kw} — experimental searches",
            "ads": f'abs:{q} AND author:({collabs}) AND year:{year_from}-',
            "inspire": f'abstract "{kw}" and (cn ATLAS or cn CMS or cn LHCb)',
            "sort": "date desc",
        })
        # Anything reporting a bound, including phenomenology recasts and the
        # astrophysical literature that no collaboration authors. Most-cited
        # first here, since this is the orientation query.
        queries.append({
            "label": f"{kw} — papers reporting a bound",
            "ads": f'abs:{q} AND full:({phrase_or}) AND year:{year_from}-',
            "inspire": f'title "{kw}" or abstract "{kw}" and (t exclusion or t limit)',
            "sort": "citation_count desc",
        })
    return queries


# ---------------------------------------------------------------------------
# Reading limits out of text.
# ---------------------------------------------------------------------------

# A number in prose or TeX: 1.5, 1500, 3.2\times10^{-4}, 10^{-9}, 1.2e-3
_NUM = r"[-+]?\d+(?:\.\d+)?(?:\s*(?:\\times|x|\*)\s*10\^?\{?-?\d+\}?|[eE][-+]?\d+)?"

_UNITS = r"(?:TeV|GeV|MeV|keV|eV|fb|pb|nb|ab|cm\^?2|cm2|s\^?-1|yr|GeV\^?-?\d*)"

_CL = r"(?:9[0-9](?:\.\d+)?)\s*%?\s*(?:C\.?L\.?|confidence level)"

# "masses below 1.5 TeV are excluded", "excluded up to 4.5 TeV"
_RE_EXCLUDED_BELOW = re.compile(
    rf"(?P<what>[^.;]{{0,80}}?)\b(?:below|less than|up to)\s+(?P<val>{_NUM})\s*"
    rf"(?P<unit>{_UNITS})\b[^.;]{{0,60}}?\bexclud",
    re.I)

# "m_LQ > 1.7 TeV", "M_{Z'} > 4.5 TeV at 95% CL", "|V_{eN}|^2 < 1e-5"
# The quantity may be a bare symbol or a bracketed/absolute-value expression,
# so the class allows | [ ] , alongside the usual TeX punctuation. It must
# still START with a letter or a bar, which keeps prose like "below 3" out.
_RE_INEQUALITY = re.compile(
    rf"(?P<what>[A-Za-z|][\w\\{{}}\[\]|^_,'’\-\(\)]{{0,40}})\s*"
    rf"(?P<rel>[<>]|&[gl]t;|\\[gl]eq?|\\l[et]|\\g[et])\s*"
    rf"(?P<val>{_NUM})\s*(?P<unit>{_UNITS})?",
    re.I)

# "upper limit of 0.1 fb", "lower limit on the mass of 1.2 TeV"
_RE_LIMIT_OF = re.compile(
    rf"\b(?P<kind>upper|lower)\s+limits?\s+(?:on\s+(?P<what>[^.;]{{0,60}}?)\s+)?"
    rf"(?:of|is|are|at)\s+(?P<val>{_NUM})\s*(?P<unit>{_UNITS})?",
    re.I)

# "masses between 1.5 and 3.0 TeV are excluded", "excluded in the range
# 0.5-1.2 TeV". A very common collaboration phrasing, and the excluded band
# is two-sided, so it is recorded as a range rather than a single bound.
_RE_EXCLUDED_RANGE = re.compile(
    rf"(?P<what>[^.;]{{0,80}}?)\b(?:between|in the range(?:\s+of)?|from)\s+"
    rf"(?P<lo>{_NUM})\s*(?:{_UNITS})?\s*(?:and|to|[-–])\s*"
    rf"(?P<hi>{_NUM})\s*(?P<unit>{_UNITS})\b[^.;]{{0,60}}?\bexclud",
    re.I)

_RE_CL = re.compile(_CL, re.I)

_EXCLUDE_NOISE = re.compile(r"^\s*(?:eq|equation|fig|figure|table|ref)\b", re.I)


def _sentences(text: str) -> List[str]:
    """Rough sentence split that survives TeX; good enough for provenance."""
    flat = re.sub(r"\s+", " ", text or "")
    return [s.strip() for s in re.split(r"(?<=[.;])\s+(?=[A-Z\\$])", flat) if s.strip()]


def _norm_number(raw: str) -> Optional[float]:
    """Parse the numeric forms above into a float; None if it will not parse."""
    s = (raw or "").strip()
    m = re.match(rf"^([-+]?\d+(?:\.\d+)?)\s*(?:\\times|x|\*)\s*10\^?\{{?(-?\d+)\}}?$",
                 s, re.I)
    if m:
        try:
            return float(m.group(1)) * (10 ** int(m.group(2)))
        except ValueError:
            return None
    try:
        return float(s.replace("^", "e").replace("{", "").replace("}", ""))
    except ValueError:
        return None


def extract_limits(text: str, max_records: int = 60) -> List[Dict[str, Any]]:
    """Numeric bounds reported in ``text``, with the sentence each came from.

    Recognises the three ways a limit is normally written:
      * "masses below X TeV are excluded"
      * "m > X TeV"  /  "sigma < X fb"
      * "an upper limit of X fb"

    Every record keeps ``sentence`` verbatim. The parser is a reading aid: it
    finds candidate numbers, it does not decide whether a bound applies to
    the model in hand. Treat the output as a list to check, never as a
    verdict.

    Known limitation: the confidence level is attached per sentence, so a
    sentence carrying two bounds and one "at 90% CL" gives that CL to both.
    ``sentence`` is kept precisely so this is visible rather than silent.
    """
    records: List[Dict[str, Any]] = []
    for sent in _sentences(text):
        if len(records) >= max_records:
            break
        if _EXCLUDE_NOISE.match(sent):
            continue
        cl = None
        mcl = _RE_CL.search(sent)
        if mcl:
            cl = mcl.group(0)

        def add(kind: str, what: str, rel: str, val: str,
                unit: Optional[str]) -> None:
            value = _norm_number(val)
            if value is None:
                return
            records.append({
                "kind": kind,
                "quantity": (what or "").strip(" ,:$\\") or None,
                "relation": rel,
                "value": value,
                "value_raw": val.strip(),
                "unit": (unit or "").strip() or None,
                "confidence_level": cl,
                "sentence": sent[:400],
            })

        # Ranges first: "between 1.5 and 3.0 TeV are excluded" also matches the
        # single-sided pattern on its upper number, which would report the band
        # as a plain lower bound and quietly lose the lower edge.
        matched_range = False
        for m in _RE_EXCLUDED_RANGE.finditer(sent):
            lo, hi = _norm_number(m.group("lo")), _norm_number(m.group("hi"))
            if lo is None or hi is None:
                continue
            matched_range = True
            records.append({
                "kind": "exclusion_range",
                "quantity": (m.group("what") or "").strip(" ,:$\\") or None,
                "relation": "excluded in",
                "value": hi,
                "value_raw": f"{m.group('lo')}-{m.group('hi')}",
                "range_low": lo,
                "range_high": hi,
                "unit": (m.group("unit") or "").strip() or None,
                "confidence_level": cl,
                "sentence": sent[:400],
            })

        if not matched_range:
            for m in _RE_EXCLUDED_BELOW.finditer(sent):
                add("exclusion", m.group("what"), ">", m.group("val"),
                    m.group("unit"))

        for m in _RE_LIMIT_OF.finditer(sent):
            rel = "<" if m.group("kind").lower() == "upper" else ">"
            add("limit", m.group("what") or "", rel, m.group("val"), m.group("unit"))

        # Inequalities only count when the sentence looks like a result,
        # otherwise every index range in the paper becomes a "limit".
        if re.search(r"exclud|limit|constrain|bound|rule[sd]? out", sent, re.I):
            for m in _RE_INEQUALITY.finditer(sent):
                rel = m.group("rel")
                rel = ">" if rel.startswith((">", "\\g", "&g")) else "<"
                add("inequality", m.group("what"), rel, m.group("val"),
                    m.group("unit"))

    return _dedupe(records)


def _dedupe(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    out = []
    for r in records:
        key = (r["kind"], r["quantity"], r["relation"], r["value"], r["unit"])
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def summarize_limits(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Counts and the strongest mass bound, for a quick orientation."""
    mass = [r for r in records
            if (r.get("unit") or "").lower() in ("tev", "gev", "mev")
            and r.get("relation") == ">"]
    strongest = None
    if mass:
        def tev(r: Dict[str, Any]) -> float:
            u = (r["unit"] or "").lower()
            return r["value"] * {"tev": 1.0, "gev": 1e-3, "mev": 1e-6}.get(u, 0.0)
        strongest = max(mass, key=tev)
    return {
        "n_records": len(records),
        "by_kind": {k: sum(1 for r in records if r["kind"] == k)
                    for k in {r["kind"] for r in records}},
        "strongest_mass_lower_bound": strongest,
        "caveat": "Candidate bounds parsed from prose. Each needs its "
                  "assumptions checked before it constrains anything.",
    }
