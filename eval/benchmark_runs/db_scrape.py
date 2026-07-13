#!/usr/bin/env python3
"""Enumerate the FeynRules model database and build a benchmark index.

Walks the seven category pages, then each model's wiki page, recording every
directly-downloadable ``.fr`` attachment and the arXiv ids cited. Emits
``db_index.json`` with a per-model record and prints a coverage funnel — models
that ship only notebooks/tarballs, or cite no paper, are recorded and skipped,
not silently dropped.

Polite scraping: single host, ~0.7 s delay, plain GETs on a public Trac wiki.
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

BASE = "https://cp3.irmp.ucl.ac.be"
CATEGORIES = [
    "StandardModel",  # single model page, not a listing
    "SimpleExtensions",
    "SusyModels",
    "ExtraDimModels",
    "EffectiveModels",
    "MiscellaneousModels",
    "NLOModels",
]
_ALLOWED_HOSTS = {"cp3.irmp.ucl.ac.be", "feynrules.irmp.ucl.ac.be"}
DELAY = 0.7

session = requests.Session()
session.headers["User-Agent"] = "heptapod-benchmark/1.0 (GSoC HEPSIM5; polite)"


def get(url: str) -> str:
    assert requests.utils.urlparse(url).hostname in _ALLOWED_HOSTS, url
    time.sleep(DELAY)
    r = session.get(url, timeout=30)
    r.raise_for_status()
    return r.text


def model_links(category_html: str) -> list:
    """Wiki page names linked from a category listing table."""
    names = re.findall(r'href="/projects/feynrules/wiki/([A-Za-z0-9_\-.]+)"', category_html)
    skip = {"WikiStart", "TitleIndex", "TracWiki", "TracGuide", "ModelDatabaseMainPage",
            "StandardModel"} | set(CATEGORIES)
    seen, out = set(), []
    for n in names:
        if n in skip or n in seen or n.startswith(("Trac", "Wiki")):
            continue
        seen.add(n)
        out.append(n)
    return out


def scrape_model(page: str) -> dict:
    url = f"{BASE}/projects/feynrules/wiki/{page}"
    html = get(url)
    # .fr attachments (both view and raw links, either host)
    frs = set()
    for m in re.findall(r'href="([^"]*?(?:raw-)?attachment/wiki/[^"]+?\.fr)"', html):
        raw = m.replace("/attachment/wiki/", "/raw-attachment/wiki/")
        frs.add(urljoin(BASE, raw))
    arxiv = []
    for m in re.findall(r'arxiv\.org/(?:abs|pdf)/([a-z\-]+/\d{7}|\d{4}\.\d{4,5})', html, re.I):
        if m not in arxiv:
            arxiv.append(m)
    title = None
    tm = re.search(r"<h1[^>]*>(?:<a[^>]*>)?([^<]+)", html)
    if tm:
        title = tm.group(1).strip()
    return {"page": page, "url": url, "title": title,
            "fr_urls": sorted(frs), "arxiv_ids": arxiv}


def main() -> int:
    out_dir = Path(__file__).parent
    index = {"categories": {}, "models": []}
    pages: list = []
    for cat in CATEGORIES:
        if cat == "StandardModel":
            pages.append(("StandardModel", "StandardModel"))
            index["categories"][cat] = ["StandardModel"]
            continue
        html = get(f"{BASE}/projects/feynrules/wiki/{cat}")
        links = model_links(html)
        index["categories"][cat] = links
        pages += [(cat, p) for p in links]
        print(f"{cat}: {len(links)} models", flush=True)

    seen = set()
    for cat, page in pages:
        if page in seen:
            continue
        seen.add(page)
        try:
            rec = scrape_model(page)
        except Exception as e:  # noqa: BLE001
            rec = {"page": page, "url": f"{BASE}/projects/feynrules/wiki/{page}",
                   "error": f"{type(e).__name__}: {e}", "fr_urls": [], "arxiv_ids": []}
        rec["category"] = cat
        index["models"].append(rec)
        print(f"  {page:32} .fr={len(rec['fr_urls'])} arxiv={rec['arxiv_ids'][:2]}", flush=True)

    (out_dir / "db_index.json").write_text(json.dumps(index, indent=2))
    n = len(index["models"])
    with_fr = sum(1 for m in index["models"] if m["fr_urls"])
    with_paper = sum(1 for m in index["models"] if m["fr_urls"] and m["arxiv_ids"])
    print(f"\nFUNNEL: {n} models listed | {with_fr} with downloadable .fr | "
          f"{with_paper} with .fr AND an arXiv paper")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
