# FeynRules model-database benchmark — Codex gpt-5.5 (medium)

Pipeline: paper (local text) → Codex extraction → deterministic generator (schema-validated) → scored vs the physicist's reference `.fr` (name-independent field signatures; SM baseline subtracted for standalone references).

**Aggregate over 28 scored models:** mean field F1 **0.748** (P 0.811 / R 0.748), median 0.857, perfect 12; extraction failures 0, validation failures 0.

| Model | Category | Ref new fields | Gen fields | Field P | R | F1 | QN F1 | Param Jacc | Status |
|---|---|---|---|---|---|---|---|---|---|
| topBSM | SimpleExtensions | 5 | 5 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| ChernSimonsPortal | SimpleExtensions | 1 | 1 | 1.0 | 1.0 | **1.0** | 1.0 | 0.0 | scored |
| EffLRSM | SimpleExtensions | 3 | 3 | 1.0 | 1.0 | **1.0** | 1.0 | 0.259 | scored |
| HeavyN | SimpleExtensions | 3 | 3 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| Monotops | SimpleExtensions | 6 | 6 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| Sextets | SimpleExtensions | 3 | 3 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| 368sextets | SimpleExtensions | 4 | 4 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| SMWeinberg | SimpleExtensions | 1 | 1 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| Top-Philic-Zprime | SimpleExtensions | 1 | 1 | 1.0 | 1.0 | **1.0** | 1.0 | 0.0 | scored |
| Triplets | SimpleExtensions | 1 | 1 | 1.0 | 1.0 | **1.0** | 1.0 | 1.0 | scored |
| CHEIDI | ExtraDimModels | 1 | 1 | 1.0 | 1.0 | **1.0** | 1.0 | 0.222 | scored |
| HiggsCharacterisation | EffectiveModels | 3 | 3 | 1.0 | 1.0 | **1.0** | 1.0 | 0.921 | scored |
| HNLs | SimpleExtensions | 21 | 22 | 0.955 | 1.0 | **0.977** | 0.977 | 0.242 | scored |
| pNG | SimpleExtensions | 3 | 4 | 0.75 | 1.0 | **0.857** | 0.857 | 0.27 | scored |
| NJLComposite | EffectiveModels | 18 | 12 | 1.0 | 0.667 | **0.8** | 0.8 | 0.0 | scored |
| SLQrules | SimpleExtensions | 14 | 9 | 1.0 | 0.643 | **0.783** | 0.783 | 0.19 | scored |
| DMsimp | SimpleExtensions | 4 | 5 | 0.6 | 0.75 | **0.667** | 0.889 | 0.042 | scored |
| Wprime | SimpleExtensions | 1 | 2 | 0.5 | 1.0 | **0.667** | 0.667 | 0.0 | scored |
| B-L-SM | SimpleExtensions | 10 | 6 | 0.833 | 0.5 | **0.625** | 0.75 | 0.019 | scored |
| MDMmodel | SimpleExtensions | 9 | 7 | 0.714 | 0.556 | **0.625** | 0.625 | 0.372 | scored |
| VLC_LN | EffectiveModels | 4 | 9 | 0.444 | 1.0 | **0.615** | 0.615 | 0.043 | scored |
| ALRM_general | SimpleExtensions | 16 | 7 | 0.857 | 0.375 | **0.522** | 0.471 | 0.276 | scored |
| GeneralU1 | SimpleExtensions | 15 | 5 | 1.0 | 0.333 | **0.5** | 0.5 | 0.026 | scored |
| MSSMD | SusyModels | 39 | 13 | 1.0 | 0.333 | **0.5** | 0.468 | 0.165 | scored |
| VLQ | SimpleExtensions | 4 | 6 | 0.333 | 0.5 | **0.4** | 0.0 | 0.0 | scored |
| pSPSS | SimpleExtensions | 6 | 3 | 0.333 | 0.167 | **0.222** | 0.667 | 0.208 | scored |
| 331 | SimpleExtensions | 38 | 13 | 0.385 | 0.132 | **0.196** | 0.196 | 0.063 | scored |
| LeptoQuark | SimpleExtensions | 6 | 4 | 0.0 | 0.0 | **0.0** | 0.4 | 0.0 | scored |

## Caveats

1. **Training-data confound:** every reference implementation is public and predates the model's training; high scores partly reflect recall of known implementations, not only paper extraction. A confound-free test needs papers with no public implementation.
2. **No compilation check:** no Mathematica license — scores measure extraction fidelity of field/parameter content, not UFO-compilability.
3. Reference choice for multi-file models is heuristic (name-similarity, then size); the chosen file is recorded per row.
4. Signature matching is name-independent (spin, colour rep, Q/Y). Fields differing only by chirality/mass-basis conventions can collide (see TypeIIISeeSaw in the gated-out list).
5. **LeptoQuark's F1=0 is a reference artifact, not an extraction failure**: the extraction recovered the paper's vector leptoquark + coloron + Z' (visible as 'extra' signatures), but the multi-file heuristic picked the bundle's vector-like-fermion component (`VLferm.fr`) as the reference. Multi-file bundles need per-component references.
