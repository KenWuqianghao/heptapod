# FeynRules convention catalog

_Generated 2026-07-08T06:18:47+00:00 by `scripts/build_fr_convention_catalog.py`._

Survey of conventions across reference FeynRules model files, used to inform Lagrangian-extraction prompts and `.fr` generator defaults.

## Sources

- **SM** (in-tree fixture) — Christensen, Duhr, Fuks — FeynRules Standard Model
- **S1_LQ_RR** (in-tree fixture) — Menzo — scalar leptoquark S1 add-on (HEPTAPOD example)

## Conventions

- **Spin types**: {'V': 6, 'U': 7, 'F': 9, 'S': 5}
- **Index conventions**: {'Gluon': 2, 'SU2W': 2, 'Generation': 9, 'Colour': 6, 'SU2D': 3}
- **Quantum-number keys**: {'Q': 8, 'GhostNumber': 5, 'LeptonNumber': 2, 'Y': 6}
- **Parameter types**: {'External': 14, 'Internal': 16}
- **LHA block names**: {'SMINPUTS': 3, 'YUKAWA': 9, 'CKMBLOCK': 1, 'BSMINPUTS': 1}
- **Value formats**: {'integer': 14, 'rational': 8, 'decimal': 9, 'scientific': 4, 'symbolic_or_expr': 10, 'list': 4} (rationals like `-1/3` must be preserved as strings)

## Models

| Model | classes | parameters | gauge groups |
|---|---|---|---|
| SM (Standard Model) | 26 | 29 | U1Y, SU2L, SU3C |
| S1_LQ_RR (S1_LQ_RR) | 1 | 1 | — |
