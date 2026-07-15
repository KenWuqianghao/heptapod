# Validation-augmented benchmark — agent .fr → FeynRules/Wolfram UFO → MadGraph

Each agent-generated `.fr` (from the field-content benchmark) is compiled to a UFO with the free Wolfram Engine + FeynRules, physics-checked, and imported into MadGraph 3.7.2. This measures whether the agent's model **actually works in the real tool chain**, not just whether its field content matches a reference.

**Aggregate over 28 models:** compiled **23/28** (82%); Hermiticity-pass 20/23; MadGraph-import-ok 16/23; compile-failed 4, timeout 1.

| Model | Lag symbol | Compile | Herm | Kin | Mass | UFO parts | MG5 load | LNV | secs | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 331 | LScalarFermion331 | ✗ | — | — | — | — | — | — | 9.2 | compile_failed |
| ALRM_general | LeffALRM | ✓ | ✓ | ✓ | ✓ | 40 | ✗ | ✗ | 60.4 | compiled |
| topBSM | LO1 | ✓ | ✓ | ✓ | ✓ | 29 | ✓ | ✗ | 34.3 | compiled |
| ChernSimonsPortal | LChernSimonsPortalBroken | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✗ | 29.4 | compiled |
| DMsimp | L1DM | ✓ | ✓ | ✓ | ✓ | 29 | ✓ | ✗ | 42.4 | compiled |
| EffLRSM | LBSM | ✓ | ✓ | ✓ | ✓ | 29 | ✗ | ✗ | 366.2 | compiled |
| GeneralU1 | LGeneralU1 | ✗ | — | — | — | — | — | — | 8.3 | compile_failed |
| HeavyN | LFull | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✓ | 128.5 | compiled |
| HNLs | LHadrSemileptonic | ✗ | — | — | — | — | — | — | 5.9 | compile_failed |
| B-L-SM | LBSM | ✓ | ✗ | ✗ | ✗ | 30 | ✗ | ✗ | 67.7 | compiled |
| MDMmodel | LMDMNP | ✓ | ✗ | ✓ | ✓ | 26 | ✓ | ✗ | 48.5 | compiled |
| Monotops | LMono | ✓ | ✓ | ✓ | ✓ | 30 | ✓ | ✗ | 66.2 | compiled |
| pNG | LScalarPng | ✓ | ✓ | ✓ | ✓ | 24 | ✓ | ✗ | 33.6 | compiled |
| Sextets | LSextet | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✗ | 55.1 | compiled |
| 368sextets | LSextet | ✓ | ✓ | ✓ | ✓ | 28 | ✗ | ✗ | 159.6 | compiled |
| SLQrules | LBSM | ✗ | — | — | — | — | — | — | 6.6 | compile_failed |
| pSPSS | LpSPSS | ✓ | ✗ | ✓ | ✓ | 26 | ✗ | ✗ | 212.2 | compiled |
| SMWeinberg | LFull | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✓ | 116.0 | compiled |
| Top-Philic-Zprime | LBSM | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✗ | 24.3 | compiled |
| Triplets | LTrip | ✓ | ✓ | ✓ | ✓ | 25 | ✓ | ✗ | 29.8 | compiled |
| VLQ | L4Mass | ✓ | ✓ | ✓ | ✓ | 30 | ✓ | ✗ | 23.6 | compiled |
| LeptoQuark | LLeptoQuark | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✗ | 40.7 | compiled |
| Wprime | LBSM | ✓ | ✓ | ✓ | ✓ | 28 | ✓ | ✗ | 82.5 | compiled |
| MSSMD | Lag | ✓ | ✓ | ✓ | ✓ | 58 | ✗ | ✗ | 40.7 | compiled |
| CHEIDI | LHEIDIggHeavyTop | ✓ | ✓ | ✓ | ✓ | 34 | ✗ | ✗ | 25.2 | compiled |
| HiggsCharacterisation | LHCNP | ✓ | ✓ | ✓ | ✓ | 27 | ✓ | ✗ | 40.0 | compiled |
| NJLComposite | LBSM | ✓ | ✓ | ✓ | ✓ | 36 | ✓ | ✗ | 41.1 | compiled |
| VLC_LN | LVLCNP | ✗ | — | — | — | — | — | — | 600.1 | compile_timeout |

## Notes
- `Compile` = FeynRules `WriteUFO` produced `particles.py` and printed Done.
- Physics checks (Herm/Kin/Mass) are FeynRules' own consistency routines, parsed from the run log; `—` means the check did not emit a verdict.
- `MG5 load` = MadGraph `import model` succeeded (UFO auto-converted to Python3 as needed) and reported a particle count with no fatal error.
- `LNV` = MadGraph flagged a lepton-number-violating interaction (expected/correct for leptoquark and Majorana-neutrino models).
- `AddDecays=False`: FeynRules' auto-decay routine is disabled (broken under Wolfram ≥ 15); decay widths are left to MadGraph's `compute_widths`.
