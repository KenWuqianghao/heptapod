# Pipeline Audit Trail

_schema `audit-1.0` — 3 event(s) — created 2026-07-08T19:42:05+00:00._

| # | time (UTC) | stage | status | summary |
|---|---|---|---|---|
| 1 | 2026-07-08T19:42:05+00:00 | search | ✓ ok | Searched INSPIRE and arXiv for scalar leptoquark S1 references; INSPIRE identified Doršner et al. 1603.04993 and BRW, while arXiv search endpoint returned timeout/429 errors. |
| 2 | 2026-07-08T19:42:14+00:00 | extract | ✓ ok | Extracted S1 representation and right-handed Yukawa from Doršner et al. arXiv:1603.04993 source TeX. |
| 3 | 2026-07-08T19:42:32+00:00 | generate_fr | ✓ ok | Generated deterministic FeynRules add-on model for S1 right-handed leptoquark coupling. |

## Details

### 1. search
```json
{
  "inspire_queries": [
    {
      "query": "scalar leptoquark S1",
      "sort": "mostcited",
      "top_arxiv_ids": [
        "2104.03691",
        "1603.05248",
        "2002.12544",
        "2006.11624",
        "1910.03877"
      ]
    },
    {
      "query": "leptoquark S1 R2 review",
      "sort": "mostcited",
      "top_arxiv_ids": []
    },
    {
      "query": "leptoquark standard model extension",
      "sort": "mostcited",
      "top_arxiv_ids": [
        "2009.07294",
        "2103.16558",
        "1708.06350",
        "1807.02068",
        "hep-ex/9903037"
      ]
    },
    {
      "query": "Physics of leptoquarks in precision experiments and at particle colliders",
      "sort": "mostcited",
      "top_arxiv_ids": [
        "1603.04993"
      ]
    },
    {
      "query": "Buchmuller Ruckl Wyler leptoquarks",
      "sort": "mostcited",
      "top_recids": [
        "235471"
      ],
      "top_arxiv_ids": [
        null
      ]
    }
  ],
  "arxivsearch_queries": [
    {
      "query": "all:\"scalar leptoquark\" AND all:\"S1\"",
      "status": "error",
      "reason": "timeout"
    },
    {
      "query": "all:leptoquark AND all:S1",
      "status": "error",
      "reason": "timeout"
    },
    {
      "query": "cat:hep-ph AND ti:leptoquark",
      "status": "error",
      "reason": "429"
    },
    {
      "query": "id:1603.04993",
      "status": "error",
      "reason": "429"
    },
    {
      "query": "cat:hep-ph AND (ti:\"scalar leptoquark\" OR abs:\"scalar leptoquark\") AND (abs:\"S1\" OR abs:\"right-handed\")",
      "status": "error",
      "reason": "429"
    }
  ],
  "found_arxiv_ids": [
    "1603.04993",
    "1603.05248",
    "2002.12544",
    "2006.11624",
    "1910.03877",
    "2104.03691"
  ],
  "canonical_choice": {
    "arxiv_id": "1603.04993",
    "recid": "1428667",
    "title": "Physics of leptoquarks in precision experiments and at particle colliders",
    "citation_count": 766
  },
  "foundational_choice": {
    "recid": "235471",
    "title": "Leptoquarks in Lepton - Quark Collisions",
    "citation_count": 999,
    "arxiv_id": null
  }
}
```

### 2. extract
```json
{
  "source_tool": "Arxivsource",
  "arxiv_id": "1603.04993",
  "tex_path": "text/1603.04993_source.tex",
  "local_tex_path": "examples/demo_codex_research/text/1603.04993_source.tex",
  "evidence": {
    "table_lines": "S1 listed as (anti-3,1,1/3), spin 0, with RR type",
    "lagrangian_lines": "L contains y^{RR}_{1 ij} \\bar{u}_R^{C i} S_1 e_R^j + h.c."
  },
  "model_convention": "Generated FeynRules field S1 is the conjugate colour triplet with Q=-1/3, so the RR Yukawa is implemented with HC[S1]."
}
```

### 3. generate_fr
```json
{
  "tool": "Generatefeynrulesmodel",
  "status": "ok",
  "schema": "feynrules-model-1.0",
  "model_name": "S1_research",
  "fr_path": "model/S1_research.fr",
  "n_particles": 1,
  "n_parameters": 1,
  "attempts": 1
}
```
