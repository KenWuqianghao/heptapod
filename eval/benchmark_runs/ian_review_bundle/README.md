# Review bundle — agent-extracted FeynRules models

One directory per model that passes the full validation chain (FeynRules/Wolfram UFO compile, Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import):

- `<model>.fr` — the validated FeynRules file (agent-extracted; where noted, self-repaired by the closed validation loop with no human input).
- `REVIEW.pdf` — the blank-slate reverse-check package: a fresh agent that saw ONLY the sanitized `.fr` (no paper, no metadata) reconstructs the physics in LaTeX; a second fresh agent compares that reconstruction against the paper term by term and grades every disagreement (convention / substantive / cosmetic). The final page is a sign-off block — **the tooling never declares the physics correct; that verdict is yours.**

Validation means the tool chain accepts the model. It does not certify the physics — that is exactly what these review packages are for.

| model | paper (arXiv) | provenance | review |
|---|---|---|---|
| topBSM | 1305.7386 | passed one-shot | REVIEW.pdf |
| ChernSimonsPortal | 0901.0639 | passed one-shot | REVIEW.pdf |
| DMsimp | 1508.00564 | passed one-shot | REVIEW.pdf |
| HeavyN | 1602.06957 | passed one-shot | REVIEW.pdf |
| Monotops | 1106.6199 | passed one-shot | REVIEW.pdf |
| pNG | 1912.04008 | passed one-shot | REVIEW.pdf |
| Sextets | 0909.2666 | passed one-shot | REVIEW.pdf |
| SMWeinberg | 2012.09882 | passed one-shot | REVIEW.pdf |
| Top-Philic-Zprime | 1604.07421 | passed one-shot | REVIEW.pdf |
| Triplets | 0909.2666 | passed one-shot | REVIEW.pdf |
| VLQ | hep-ph_0607115 | passed one-shot | REVIEW.pdf |
| LeptoQuark | 1901.10480 | passed one-shot | REVIEW.pdf |
| Wprime | hep-ph_0207290 | passed one-shot | REVIEW.pdf |
| HiggsCharacterisation | 1306.6464 | passed one-shot | REVIEW.pdf |
| NJLComposite | 2311.18472 | passed one-shot | REVIEW.pdf |
| EffLRSM | 1610.08985 | repaired (phase 1) | REVIEW.pdf |
| GeneralU1 | 2104.10902 | repaired (phase 1) | REVIEW.pdf |
| MDMmodel | 1311.6661 | repaired (phase 1) | REVIEW.pdf |
| 368sextets | 2110.11359 | repaired (phase 1) | REVIEW.pdf |
| MSSMD | 1812.00380 | repaired (phase 1) | REVIEW.pdf |
| 331 | 1611.09337 | repaired (phase 2) | REVIEW.pdf |
| B-L-SM | 1811.11452 | repaired (phase 2) | REVIEW.pdf |
| CHEIDI | 1010.3251 | repaired (phase 2) | REVIEW.pdf |
| VLC_LN | 1508.01112 | repaired (phase 2) | REVIEW.pdf |
| pSPSS | 2210.10738 | repaired (phase 3) | REVIEW.pdf |

Benchmark context: 28 models attempted; 15 passed one-shot; the closed repair loop recovered 10 more (25/28). Full analysis is included as REPAIR_BENCHMARK_ANALYSIS.md.
