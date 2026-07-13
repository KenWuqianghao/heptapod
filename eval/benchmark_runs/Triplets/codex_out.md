```json
{
  "model_name": "Triplets_gen",
  "info": {
    "authors": [
      "Codex extraction from Han, Lewis and McElmurry, arXiv:0909.2666"
    ],
    "version": "1.0.0",
    "date": "2026-07-13",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "QCD",
      1
    ],
    [
      "QED",
      2
    ],
    [
      "NP",
      3
    ]
  ],
  "interaction_order_limit": [
    [
      "QCD",
      99
    ],
    [
      "QED",
      99
    ],
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
      "name": "Mtrip1",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000001,
      "description": "Mass of the scalar colour-antitriplet diquark trip1"
    },
    {
      "name": "Wtrip1",
      "parameter_type": "External",
      "value": "4.4108",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9000001,
      "description": "Width of the scalar colour-antitriplet diquark trip1"
    },
    {
      "name": "LQQRR",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "LQQRR[1, 2]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[2, 1]",
          "rhs": "-0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[1, 3]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[3, 1]",
          "rhs": "-0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[2, 3]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[3, 2]",
          "rhs": "-0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[i_, i_]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Real part of the left-chiral QQ coupling matrix for the colour-antitriplet scalar; antisymmetric in flavour"
    },
    {
      "name": "LQQRI",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "LQQRI[_, _]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Imaginary part of the left-chiral QQ coupling matrix for the colour-antitriplet scalar"
    },
    {
      "name": "LUDLR",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "LUDLR[1, 1]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUDLR[2, 2]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUDLR[3, 3]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUDLR[i_, j_]",
          "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)",
          "delayed": true
        }
      ],
      "complex": false,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Real part of the right-chiral UD coupling matrix for the colour-antitriplet scalar"
    },
    {
      "name": "LUDLI",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "LUDLI[_, _]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Imaginary part of the right-chiral UD coupling matrix for the colour-antitriplet scalar"
    },
    {
      "name": "LHS1",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "interaction_order": [
        "QED",
        2
      ],
      "description": "Higgs portal coupling Phibar Phi trip1bar trip1"
    },
    {
      "name": "LSS11",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "interaction_order": [
        "QCD",
        2
      ],
      "description": "Quartic self-coupling of the colour-antitriplet scalar"
    },
    {
      "name": "LQQR",
      "parameter_type": "Internal",
      "value_rules": [
        {
          "lhs": "LQQR[i_, j_]",
          "rhs": "LQQRR[i, j] + I LQQRI[i, j]",
          "delayed": true
        }
      ],
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Complex left-chiral QQ coupling matrix"
    },
    {
      "name": "LUDL",
      "parameter_type": "Internal",
      "value_rules": [
        {
          "lhs": "LUDL[i_, j_]",
          "rhs": "LUDLR[i, j] + I LUDLI[i, j]",
          "delayed": true
        }
      ],
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Complex right-chiral UD coupling matrix"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "trip1",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "Mtrip1",
        "value": "500.",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "Wtrip1",
        "value": "4.4108",
        "members": []
      },
      "quantum_numbers": {
        "Q": "-1/3",
        "Y": "-1/3"
      },
      "pdg": 9000001,
      "particle_name": "trip1",
      "antiparticle_name": "trip1~",
      "full_name": "Scalar colour-antitriplet diquark, SU(2) singlet, Q=-1/3",
      "propagator_label": "trip1",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LTripKin",
      "expression": "DC[trip1bar[k], mu] DC[trip1[k], mu] - Mtrip1^2 trip1bar[k] trip1[k]",
      "delayed": true
    },
    {
      "name": "LD11",
      "expression": "2 (Eps[k, i, j] trip1bar[k] LQQR[n, m] ProjP[s, r] dqbar[s, n, i].CC[uq][r, m, j] + Eps[k, i, j] trip1bar[k] LUDL[n, m] ProjM[s, r] dqbar[s, n, i].CC[uq][r, m, j])",
      "delayed": true
    },
    {
      "name": "LD1",
      "expression": "LD11 + HC[LD11]",
      "delayed": true
    },
    {
      "name": "LPot",
      "expression": "ExpandIndices[LHS1 Phibar[ii] Phi[ii] trip1bar[k] trip1[k] + LSS11 trip1bar[k1] trip1[k1] trip1bar[k2] trip1[k2], FlavorExpand -> {SU2W, SU2D}]",
      "delayed": true
    },
    {
      "name": "LTrip",
      "expression": "LTripKin + LD1 + LPot",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "SetAttributes[LQQR, Orderless];",
    "SetAttributes[LUDL, Orderless];"
  ],
  "raw_blocks": []
}
```