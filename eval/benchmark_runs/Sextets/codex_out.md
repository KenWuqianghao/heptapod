```json
{
  "model_name": "Sextets_gen",
  "info": {
    "authors": [
      "C. Duhr",
      "Codex extraction from Han, Lewis and McElmurry, arXiv:0909.2666"
    ],
    "version": "1.0",
    "date": "2026-07-13",
    "institutions": [
      "IPPP, Durham"
    ],
    "emails": [
      "claude.duhr@durham.ac.uk"
    ]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "u"
    }
  ],
  "parameters": [
    {
      "name": "LQQRR",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LQQRR[1,1]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[2,2]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[3,3]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LQQRR[i_, j_]",
          "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)",
          "delayed": true
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Real part of symmetric sextet QQ coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LQQRI",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LQQRI[_, _]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Imaginary part of symmetric sextet QQ coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LUDLR",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LUDLR[1,1]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUDLR[2,2]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUDLR[3,3]",
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
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Real part of sextet UD coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LUDLI",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LUDLI[_, _]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Imaginary part of sextet UD coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LUULR",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LUULR[1,1]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUULR[2,2]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUULR[3,3]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LUULR[i_, j_]",
          "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)",
          "delayed": true
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Real part of symmetric sextet UU coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LUULI",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LUULI[_, _]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Imaginary part of symmetric sextet UU coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LDDLR",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LDDLR[1,1]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LDDLR[2,2]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LDDLR[3,3]",
          "rhs": "0.1",
          "delayed": false
        },
        {
          "lhs": "LDDLR[i_, j_]",
          "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)",
          "delayed": true
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Real part of symmetric sextet DD coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LDDLI",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "LDDLI[_, _]",
          "rhs": "0",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Imaginary part of symmetric sextet DD coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LHS1",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QED",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Higgs portal coupling for six1",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LHS2",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QED",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Higgs portal coupling for six2",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LHS3",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QED",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Higgs portal coupling for six3",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS11",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six1 quartic self-coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS121",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six1-six2 quartic coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS122",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six1-six2 crossed quartic coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS131",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six1-six3 quartic coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS132",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six1-six3 crossed quartic coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS22",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six2 quartic self-coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS231",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six2-six3 quartic coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS232",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six2-six3 crossed quartic coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LSS33",
      "parameter_type": "External",
      "value": "0.1",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        2
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "six3 quartic self-coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LQQR",
      "parameter_type": "Internal",
      "value": null,
      "value_rules": [
        {
          "lhs": "LQQR[i_, j_]",
          "rhs": "LQQRR[i, j] + I LQQRI[i, j]",
          "delayed": true
        }
      ],
      "complex": true,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Complex symmetric sextet QQ coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LUDL",
      "parameter_type": "Internal",
      "value": null,
      "value_rules": [
        {
          "lhs": "LUDL[i_, j_]",
          "rhs": "LUDLR[i, j] + I LUDLI[i, j]",
          "delayed": true
        }
      ],
      "complex": true,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Complex sextet UD coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LUUL",
      "parameter_type": "Internal",
      "value": null,
      "value_rules": [
        {
          "lhs": "LUUL[i_, j_]",
          "rhs": "LUULR[i, j] + I LUULI[i, j]",
          "delayed": true
        }
      ],
      "complex": true,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Complex symmetric sextet UU coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "LDDL",
      "parameter_type": "Internal",
      "value": null,
      "value_rules": [
        {
          "lhs": "LDDL[i_, j_]",
          "rhs": "LDDLR[i, j] + I LDDLI[i, j]",
          "delayed": true
        }
      ],
      "complex": true,
      "block_name": null,
      "order_block": null,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": null,
      "tex": null,
      "description": "Complex symmetric sextet DD coupling matrix",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "six1",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "flavor_index": null,
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "MSIX1",
        "value": "500",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "WSIX1",
        "value": "4.4108",
        "members": []
      },
      "quantum_numbers": {
        "Q": "1/3",
        "Y": "1/3"
      },
      "pdg": null,
      "particle_name": "six1",
      "antiparticle_name": "six1~",
      "full_name": "Scalar colour-sextet diquark six1, SU(2) singlet, Y=1/3",
      "propagator_label": "six1",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    },
    {
      "spin_type": "S",
      "class_index": 200,
      "class_name": "six2",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "flavor_index": null,
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "MSIX2",
        "value": "500",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "WSIX2",
        "value": "4.7740",
        "members": []
      },
      "quantum_numbers": {
        "Q": "-2/3",
        "Y": "-2/3"
      },
      "pdg": null,
      "particle_name": "six2",
      "antiparticle_name": "six2~",
      "full_name": "Scalar colour-sextet diquark six2, SU(2) singlet, Y=-2/3",
      "propagator_label": "six2",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    },
    {
      "spin_type": "S",
      "class_index": 300,
      "class_name": "six3",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "flavor_index": null,
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "MSIX3",
        "value": "500",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "WSIX3",
        "value": "4.0647",
        "members": []
      },
      "quantum_numbers": {
        "Q": "4/3",
        "Y": "4/3"
      },
      "pdg": null,
      "particle_name": "six3",
      "antiparticle_name": "six3~",
      "full_name": "Scalar colour-sextet diquark six3, SU(2) singlet, Y=4/3",
      "propagator_label": "six3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LSextetKin",
      "expression": "DC[six1bar[k], mu] DC[six1[k], mu] - MSIX1^2 six1bar[k] six1[k] + DC[six2bar[k], mu] DC[six2[k], mu] - MSIX2^2 six2bar[k] six2[k] + DC[six3bar[k], mu] DC[six3[k], mu] - MSIX3^2 six3bar[k] six3[k]",
      "delayed": true
    },
    {
      "name": "LD11",
      "expression": "2 Sqrt[2] (K6bar[k, i, j] six1[k] LQQR[n, m] ProjP[s, r] dqbar[s, n, i].CC[uq][r, m, j] + K6bar[k, i, j] six1[k] LUDL[n, m] ProjM[s, r] dqbar[s, n, i].CC[uq][r, m, j])",
      "delayed": true
    },
    {
      "name": "LD1",
      "expression": "LD11 + HC[LD11]",
      "delayed": true
    },
    {
      "name": "LD21",
      "expression": "2 Sqrt[2] K6bar[k, i, j] six2[k] LDDL[n, m] ProjM[s, r] dqbar[s, n, i].CC[dq][r, m, j]",
      "delayed": true
    },
    {
      "name": "LD2",
      "expression": "LD21 + HC[LD21]",
      "delayed": true
    },
    {
      "name": "LD31",
      "expression": "2 Sqrt[2] K6bar[k, i, j] six3[k] LUUL[n, m] ProjM[s, r] uqbar[s, n, i].CC[uq][r, m, j]",
      "delayed": true
    },
    {
      "name": "LD3",
      "expression": "LD31 + HC[LD31]",
      "delayed": true
    },
    {
      "name": "LD",
      "expression": "LD1 + LD2 + LD3",
      "delayed": true
    },
    {
      "name": "LPot",
      "expression": "ExpandIndices[LHS1 Phibar[ii] Phi[ii] six1bar[k] six1[k] + LHS2 Phibar[ii] Phi[ii] six2bar[k] six2[k] + LHS3 Phibar[ii] Phi[ii] six3bar[k] six3[k] + LSS11 six1bar[k1] six1[k1] six1bar[k2] six1[k2] + LSS121 six1bar[k1] six1[k1] six2bar[k2] six2[k2] + LSS122 six1bar[k1] six1[k2] six2bar[k2] six2[k1] + LSS131 six1bar[k1] six1[k1] six3bar[k2] six3[k2] + LSS132 six1bar[k1] six1[k2] six3bar[k2] six3[k1] + LSS22 six2bar[k1] six2[k1] six2bar[k2] six2[k2] + LSS231 six2bar[k1] six2[k1] six3bar[k2] six3[k2] + LSS232 six2bar[k1] six2[k2] six3bar[k2] six3[k1] + LSS33 six3bar[k1] six3[k1] six3bar[k2] six3[k2], FlavorExpand -> {SU2W, SU2D}]",
      "delayed": true
    },
    {
      "name": "LSextet",
      "expression": "LSextetKin + LD1 + LD2 + LD3 + LPot",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "AddGaugeRepresentation[SU3C -> {T6, Sextet}];",
    "SetAttributes[LQQR, Orderless];",
    "SetAttributes[LUDL, Orderless];",
    "SetAttributes[LUUL, Orderless];",
    "SetAttributes[LDDL, Orderless];"
  ],
  "raw_blocks": []
}
```