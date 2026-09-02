"""
# ads_interface.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

NASA ADS (Astrophysics Data System) API interface.

Complements the INSPIRE and arXiv interfaces. INSPIRE indexes HEP theory and
experiment well; arXiv serves preprints. ADS adds two things neither has:

  * published-literature coverage beyond hep-ph/hep-ex, which is where the
    astrophysical and cosmological bounds on a BSM model live (relic density,
    direct detection, supernova cooling, BBN, CMB);
  * full-text search over the body of a paper, not just title and abstract,
    which is how a numeric limit buried in a results section is found at all.

Auth: ADS requires a token. Resolution order is the ``token`` argument, then
``config.ads_token``, then the ``ADS_API_TOKEN`` environment variable. Register
for one at https://ui.adsabs.harvard.edu/user/settings/token — the API is free
but rate-limited per token.
"""

from __future__ import annotations

import os
import threading
import time
from typing import Any, Dict, List, Optional

import requests

ADS_API_URL = "https://api.adsabs.harvard.edu/v1"

# ADS publishes a per-token daily quota and returns the remaining allowance in
# response headers. Keep a courteous floor between calls regardless.
_MIN_REQUEST_INTERVAL = 1.0

# Fields worth having back for every hit. `citation_count` and `year` drive the
# ranking of which limit paper to read first; `esources` says whether full text
# is reachable at all.
DEFAULT_FIELDS = (
    "bibcode,title,author,year,pub,doi,arxiv_class,identifier,"
    "citation_count,abstract,esources,doctype"
)

_MAX_ROWS = 200


class AdsError(RuntimeError):
    """ADS refused the request, or no token is configured."""


def resolve_token(token: Optional[str] = None) -> Optional[str]:
    """Token from the argument, then config.ads_token, then ADS_API_TOKEN."""
    if token:
        return token.strip()
    try:
        import config  # local machine config, gitignored
        cfg = getattr(config, "ads_token", None)
        if cfg:
            return str(cfg).strip()
    except Exception:                                     # noqa: BLE001
        pass
    env = os.environ.get("ADS_API_TOKEN")
    return env.strip() if env else None


class AdsInterface:
    """Thin ADS client: search, full-text search, and metadata by bibcode.

    Deliberately not a general ADS wrapper. It exposes the queries the
    experimental-limits workflow needs, with the token handling and rate
    limiting in one place.
    """

    def __init__(self, token: Optional[str] = None,
                 timeout: int = 90,
                 session: Optional[requests.Session] = None) -> None:
        self._token = resolve_token(token)
        self._timeout = timeout
        self._session = session or requests.Session()
        self._lock = threading.Lock()
        self._last_request = 0.0

    # ---------------------------------------------------------------- auth
    @property
    def has_token(self) -> bool:
        return bool(self._token)

    def _headers(self) -> Dict[str, str]:
        if not self._token:
            raise AdsError(
                "no ADS API token: set config.ads_token or ADS_API_TOKEN "
                "(register at https://ui.adsabs.harvard.edu/user/settings/token)"
            )
        return {"Authorization": f"Bearer {self._token}"}

    # --------------------------------------------------------------- rate
    def _throttle(self) -> None:
        with self._lock:
            gap = time.time() - self._last_request
            if gap < _MIN_REQUEST_INTERVAL:
                time.sleep(_MIN_REQUEST_INTERVAL - gap)
            self._last_request = time.time()

    def _get(self, path: str, params: Dict[str, Any],
             _attempt: int = 0) -> Dict[str, Any]:
        self._throttle()
        try:
            r = self._session.get(f"{ADS_API_URL}{path}", params=params,
                                  headers=self._headers(), timeout=self._timeout)
        except (requests.Timeout, requests.ConnectionError) as e:
            # Full-text ADS queries (`full:"..."`) routinely take tens of
            # seconds, and a timeout here loses the whole query rather than
            # degrading. One retry costs little and recovers the common case.
            if _attempt < 1:
                time.sleep(2.0)
                return self._get(path, params, _attempt + 1)
            raise AdsError(
                f"ADS request timed out after {self._timeout}s (retried once): "
                f"{type(e).__name__}") from e
        except requests.RequestException as e:
            raise AdsError(f"ADS request failed: {type(e).__name__}: {e}") from e
        if r.status_code == 401:
            raise AdsError("ADS rejected the token (401)")
        if r.status_code == 429:
            raise AdsError("ADS rate limit exhausted for this token (429)")
        if r.status_code >= 400:
            raise AdsError(f"ADS returned {r.status_code}: {r.text[:200]}")
        try:
            return r.json()
        except ValueError as e:
            raise AdsError(f"ADS returned non-JSON: {r.text[:200]}") from e

    # ------------------------------------------------------------- search
    def search(self, query: str, rows: int = 20, start: int = 0,
               sort: str = "citation_count desc",
               fields: str = DEFAULT_FIELDS) -> List[Dict[str, Any]]:
        """Run a Solr query against ADS and return the docs.

        ``query`` is ADS query syntax, e.g.
        ``abs:"leptoquark" AND full:"exclusion limit" AND year:2015-2026``.
        """
        rows = max(1, min(int(rows), _MAX_ROWS))
        payload = self._get("/search/query", {
            "q": query, "rows": rows, "start": max(0, int(start)),
            "sort": sort, "fl": fields,
        })
        return list((payload.get("response") or {}).get("docs") or [])

    def count(self, query: str) -> int:
        """How many records match, without pulling them."""
        payload = self._get("/search/query", {"q": query, "rows": 0})
        return int((payload.get("response") or {}).get("numFound") or 0)

    def by_bibcode(self, bibcode: str,
                   fields: str = DEFAULT_FIELDS) -> Optional[Dict[str, Any]]:
        docs = self.search(f'bibcode:"{bibcode}"', rows=1, sort="score desc",
                           fields=fields)
        return docs[0] if docs else None

    def citations(self, bibcode: str, rows: int = 20) -> List[Dict[str, Any]]:
        """Papers citing this one — how a limit gets superseded by a newer one."""
        return self.search(f'citations(bibcode:"{bibcode}")', rows=rows)


def arxiv_id_of(doc: Dict[str, Any]) -> Optional[str]:
    """Pull an arXiv id out of an ADS doc's identifier list, if present.

    Lets an ADS hit hand off to ArxivSourceTool for the LaTeX source, which is
    what the limit extraction actually wants to read.
    """
    for ident in doc.get("identifier") or []:
        s = str(ident)
        if s.lower().startswith("arxiv:"):
            return s.split(":", 1)[1]
    return None


def summarize(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Compact, agent-friendly view of an ADS doc."""
    title = doc.get("title")
    authors = doc.get("author") or []
    return {
        "bibcode": doc.get("bibcode"),
        "title": (title[0] if isinstance(title, list) and title else title) or "",
        "first_author": authors[0] if authors else None,
        "n_authors": len(authors),
        "year": doc.get("year"),
        "publication": doc.get("pub"),
        "doi": (doc.get("doi") or [None])[0] if isinstance(doc.get("doi"), list)
               else doc.get("doi"),
        "arxiv_id": arxiv_id_of(doc),
        "citation_count": doc.get("citation_count"),
        "doctype": doc.get("doctype"),
        "abstract": doc.get("abstract"),
    }
