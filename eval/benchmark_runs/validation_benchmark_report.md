# Validation-augmented benchmark — agent .fr → FeynRules/Wolfram UFO → MadGraph

Each agent-generated `.fr` (from the field-content benchmark) is compiled to a UFO with the free Wolfram Engine + FeynRules, physics-checked, and imported into MadGraph 3.7.2. This measures whether the agent's model **actually works in the real tool chain**, not just whether its field content matches a reference.

**Aggregate over 28 models:** compiled **23/28** (82%); Hermiticity-pass 20/23; MadGraph-import-ok 16/23; compile-failed 4, timeout 1.

| Model | Lag symbol | Compile | Herm | Kin | Mass | UFO parts | MG5 load | LNV | secs | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 331 | LScalarFermion331 | ✗ | — | — | — | — | — | — | 7.4 | compile_failed |
| ALRM_general | LeffALRM | ✓ | ✓ | ✓ | ✓ | 40 | ✗ | ✗ | 37.7 | compiled |
| topBSM | LO1 | ✓ | ✓ | ✓ | ✓ | 29 | ✓ | ✗ | 25.8 | compiled |
| ChernSimonsPortal | LChernSimonsPortalBroken | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✗ | 23.7 | compiled |
| DMsimp | L1DM | ✓ | ✓ | ✓ | ✓ | 29 | ✓ | ✗ | 35.1 | compiled |
| EffLRSM | LBSM | ✓ | ✓ | ✓ | ✓ | 29 | ✗ | ✗ | 296.6 | compiled |
| GeneralU1 | LGeneralU1 | ✗ | — | — | — | — | — | — | 7.2 | compile_failed |
| HeavyN | LFull | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✓ | 126.3 | compiled |
| HNLs | LHadrSemileptonic | ✗ | — | — | — | — | — | — | 7.0 | compile_failed |
| B-L-SM | LBSM | ✓ | ✗ | ✗ | ✗ | 30 | ✗ | ✗ | 70.8 | compiled |
| MDMmodel | LMDMNP | ✓ | ✗ | ✓ | ✓ | 26 | ✓ | ✗ | 50.9 | compiled |
| Monotops | LMono | ✓ | ✓ | ✓ | ✓ | 30 | ✓ | ✗ | 69.4 | compiled |
| pNG | LScalarPng | ✓ | ✓ | ✓ | ✓ | 24 | ✓ | ✗ | 34.5 | compiled |
| Sextets | LSextet | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✗ | 57.4 | compiled |
| 368sextets | LSextet | ✓ | ✓ | ✓ | ✓ | 28 | ✗ | ✗ | 160.1 | compiled |
| SLQrules | LBSM | ✗ | — | — | — | — | — | — | 6.9 | compile_failed |
| pSPSS | LpSPSS | ✓ | ✗ | ✓ | ✓ | 26 | ✗ | ✗ | 213.1 | compiled |
| SMWeinberg | LFull | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✓ | 117.2 | compiled |
| Top-Philic-Zprime | LBSM | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✗ | 24.8 | compiled |
| Triplets | LTrip | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✗ | 31.4 | compiled |
| VLQ | L4Mass | ✓ | ✓ | ✓ | ✓ | 30 | ✓ | ✗ | 24.7 | compiled |
| LeptoQuark | LLeptoQuark | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✗ | 42.9 | compiled |
| Wprime | LBSM | ✓ | ✓ | ✓ | ✓ | 28 | ✓ | ✗ | 85.7 | compiled |
| MSSMD | Lag | ✓ | ✓ | ✓ | ✓ | 58 | ✗ | ✗ | 42.5 | compiled |
| CHEIDI | LHEIDIggHeavyTop | ✓ | ✓ | ✓ | ✓ | 34 | ✗ | ✗ | 26.2 | compiled |
| HiggsCharacterisation | LHCNP | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✗ | 40.9 | compiled |
| NJLComposite | LBSM | ✓ | ✓ | ✓ | ✓ | 36 | ✓ | ✗ | 41.6 | compiled |
| VLC_LN | LVLCNP | ✗ | — | — | — | — | — | — | 420.0 | compile_timeout |

## Notes
- `Compile` = FeynRules `WriteUFO` produced `particles.py` and printed Done.
- Physics checks (Herm/Kin/Mass) are FeynRules' own consistency routines, parsed from the run log; `—` means the check did not emit a verdict.
- `MG5 load` = MadGraph `import model` succeeded (UFO auto-converted to Python3 as needed) and reported a particle count with no fatal error.
- `LNV` = MadGraph flagged a lepton-number-violating interaction (expected/correct for leptoquark and Majorana-neutrino models).
- `AddDecays=False`: FeynRules' auto-decay routine is disabled (broken under Wolfram ≥ 15); decay widths are left to MadGraph's `compute_widths`.
