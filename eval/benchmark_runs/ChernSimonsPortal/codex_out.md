```json
{
  "model_name": "ChernSimonsPortal_gen",
  "info": {
    "authors": [
      "Codex extraction from Antoniadis, Boyarsky, Espahbodi, Ruchayskiy and Wells, arXiv:0901.0639"
    ],
    "version": "1.0",
    "date": "2026-07-13",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "NP",
      1
    ]
  ],
  "interaction_order_limit": [
    [
      "NP",
      99
    ]
  ],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Mxb",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1234567,
      "description": "Mass of the Chern-Simons portal X boson"
    },
    {
      "name": "Wxb",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1234567,
      "description": "Width of the Chern-Simons portal X boson"
    },
    {
      "name": "c1",
      "parameter_type": "External",
      "value": "0.001",
      "complex": false,
      "block_name": "CHERNSIMONS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Coefficient of the hypercharge D'Hoker-Farhi operator"
    },
    {
      "name": "c2",
      "parameter_type": "External",
      "value": "0.001",
      "complex": false,
      "block_name": "CHERNSIMONS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Coefficient of the SU(2) D'Hoker-Farhi operator"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 92,
      "class_name": "xb",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "Mxb",
        "value": "1.",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "Wxb",
        "value": "1.",
        "members": []
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 1234567,
      "particle_name": "xb",
      "full_name": "Chern-Simons portal X boson",
      "propagator_label": "xb",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LChernSimonsPortal",
      "expression": "c1 HC[H].DC[H, mu]/(HC[H].H) xb[nu] FS[B, la, ro] Eps[mu, nu, la, ro] + c2 HC[H].Ta[aa].DC[H, mu]/(HC[H].H) xb[nu] FS[Wi, la, ro, aa] Eps[mu, nu, la, ro]",
      "delayed": true
    },
    {
      "name": "LChernSimonsPortalBroken",
      "expression": "1/2 c1 sw xb[mu] Z[nu] del[Z[ro], la] Eps[mu, nu, la, ro] + c1 cw xb[mu] Z[nu] del[A[ro], la] Eps[mu, nu, la, ro] + c2 xb[mu] W[nu] HC[del[W[ro], la]] Eps[mu, nu, la, ro]",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```