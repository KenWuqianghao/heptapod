```json
{
  "model_name": "Wprime_gen",
  "info": {
    "authors": [
      "Zack Sullivan"
    ],
    "version": "1.0",
    "date": "23.07.2002",
    "institutions": [
      "Fermi National Accelerator Laboratory"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "NP",
      1
    ],
    [
      "QCD",
      2
    ],
    [
      "QED",
      3
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "MWp",
      "parameter_type": "External",
      "value": "1000.",
      "value_rules": [],
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900024,
      "interaction_order": null,
      "indices": [],
      "definitions": [],
      "parameter_name": "MWp",
      "tex": "M_{W'}",
      "description": "W-prime mass",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "gWpL",
      "parameter_type": "External",
      "value": "0.653",
      "value_rules": [],
      "complex": false,
      "block_name": "WPRIME",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": "gWpL",
      "tex": "g_L",
      "description": "Left-handed W-prime gauge coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "gWpR",
      "parameter_type": "External",
      "value": "0.653",
      "value_rules": [],
      "complex": false,
      "block_name": "WPRIME",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [],
      "definitions": [],
      "parameter_name": "gWpR",
      "tex": "g_R",
      "description": "Right-handed W-prime gauge coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "zetaWp",
      "parameter_type": "External",
      "value": "0.",
      "value_rules": [],
      "complex": false,
      "block_name": "WPRIME",
      "order_block": 3,
      "interaction_order": null,
      "indices": [],
      "definitions": [],
      "parameter_name": "zetaWp",
      "tex": "\\zeta",
      "description": "W-Wprime left-right mixing angle",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "omegaWp",
      "parameter_type": "External",
      "value": "0.",
      "value_rules": [],
      "complex": false,
      "block_name": "WPRIME",
      "order_block": 4,
      "interaction_order": null,
      "indices": [],
      "definitions": [],
      "parameter_name": "omegaWp",
      "tex": "\\omega",
      "description": "CP-violating phase in the right-handed W-prime coupling",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "MvR",
      "parameter_type": "External",
      "value": "100.",
      "value_rules": [],
      "complex": false,
      "block_name": "WPRIME",
      "order_block": 5,
      "interaction_order": null,
      "indices": [],
      "definitions": [],
      "parameter_name": "MvR",
      "tex": "m_{\\nu_R}",
      "description": "Right-handed neutrino mass",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "VpLQ",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "VpLQ[1,1]",
          "rhs": "0.9751",
          "delayed": false
        },
        {
          "lhs": "VpLQ[1,2]",
          "rhs": "0.2215",
          "delayed": false
        },
        {
          "lhs": "VpLQ[1,3]",
          "rhs": "0.0035",
          "delayed": false
        },
        {
          "lhs": "VpLQ[2,1]",
          "rhs": "0.2210",
          "delayed": false
        },
        {
          "lhs": "VpLQ[2,2]",
          "rhs": "0.9743",
          "delayed": false
        },
        {
          "lhs": "VpLQ[2,3]",
          "rhs": "0.0410",
          "delayed": false
        },
        {
          "lhs": "VpLQ[3,1]",
          "rhs": "0.0090",
          "delayed": false
        },
        {
          "lhs": "VpLQ[3,2]",
          "rhs": "0.0400",
          "delayed": false
        },
        {
          "lhs": "VpLQ[3,3]",
          "rhs": "1.0000",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": "VPLQ",
      "order_block": null,
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": "VpLQ",
      "tex": "V^{L,q}",
      "description": "Left-handed generalized CKM matrix for W-prime quark couplings",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "VpRQ",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "VpRQ[1,1]",
          "rhs": "0.9751",
          "delayed": false
        },
        {
          "lhs": "VpRQ[1,2]",
          "rhs": "0.2215",
          "delayed": false
        },
        {
          "lhs": "VpRQ[1,3]",
          "rhs": "0.0035",
          "delayed": false
        },
        {
          "lhs": "VpRQ[2,1]",
          "rhs": "0.2210",
          "delayed": false
        },
        {
          "lhs": "VpRQ[2,2]",
          "rhs": "0.9743",
          "delayed": false
        },
        {
          "lhs": "VpRQ[2,3]",
          "rhs": "0.0410",
          "delayed": false
        },
        {
          "lhs": "VpRQ[3,1]",
          "rhs": "0.0090",
          "delayed": false
        },
        {
          "lhs": "VpRQ[3,2]",
          "rhs": "0.0400",
          "delayed": false
        },
        {
          "lhs": "VpRQ[3,3]",
          "rhs": "1.0000",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": "VPRQ",
      "order_block": null,
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": "VpRQ",
      "tex": "V^{R,q}",
      "description": "Right-handed generalized CKM matrix for W-prime quark couplings",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "VpLL",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "VpLL[1,1]",
          "rhs": "1.",
          "delayed": false
        },
        {
          "lhs": "VpLL[1,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpLL[1,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpLL[2,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpLL[2,2]",
          "rhs": "1.",
          "delayed": false
        },
        {
          "lhs": "VpLL[2,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpLL[3,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpLL[3,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpLL[3,3]",
          "rhs": "1.",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": "VPLL",
      "order_block": null,
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": "VpLL",
      "tex": "V^{L,\\ell}",
      "description": "Left-handed generalized lepton mixing matrix for W-prime couplings",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    },
    {
      "name": "VpRL",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {
          "lhs": "VpRL[1,1]",
          "rhs": "1.",
          "delayed": false
        },
        {
          "lhs": "VpRL[1,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpRL[1,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpRL[2,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpRL[2,2]",
          "rhs": "1.",
          "delayed": false
        },
        {
          "lhs": "VpRL[2,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpRL[3,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpRL[3,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "VpRL[3,3]",
          "rhs": "1.",
          "delayed": false
        }
      ],
      "complex": false,
      "block_name": "VPRL",
      "order_block": null,
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [],
      "parameter_name": "VpRL",
      "tex": "V^{R,\\ell}",
      "description": "Right-handed generalized lepton mixing matrix for W-prime couplings",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Wp",
      "self_conjugate": false,
      "indices": [],
      "flavor_index": null,
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "MWp",
        "value": "1000.",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "WWp",
        "value": "Automatic",
        "members": []
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": 9900024,
      "particle_name": "W+prime",
      "antiparticle_name": "W-prime",
      "full_name": "charged W-prime boson",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "vR",
      "self_conjugate": false,
      "indices": [
        "Generation"
      ],
      "flavor_index": "Generation",
      "class_members": [
        "veR",
        "vmR",
        "vtR"
      ],
      "mass": {
        "massless": false,
        "sym": "MvR",
        "value": "100.",
        "members": []
      },
      "width": {
        "massless": true,
        "sym": null,
        "value": null,
        "members": []
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": [
        9900012,
        9900014,
        9900016
      ],
      "particle_name": [
        "veR",
        "vmR",
        "vtR"
      ],
      "antiparticle_name": [
        "veR~",
        "vmR~",
        "vtR~"
      ],
      "full_name": [
        "right-handed electron neutrino",
        "right-handed muon neutrino",
        "right-handed tau neutrino"
      ],
      "propagator_label": [
        "veR",
        "vmR",
        "vtR"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": "R"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LkinWp",
      "expression": "Block[{mu,nu}, -1/2 DC[HC[Wp[nu]],mu] DC[Wp[nu],mu] + 1/2 DC[HC[Wp[nu]],mu] DC[Wp[mu],nu] + MWp^2 HC[Wp[mu]] Wp[mu]]",
      "delayed": false
    },
    {
      "name": "LkinNuR",
      "expression": "Block[{mu,sp1,sp2,i}, Sum[I bar[vR][sp1,i].Ga[mu,sp1,sp2].del[vR[sp2,i],mu] - MvR bar[vR][sp1,i].vR[sp1,i], {i,1,3}]]",
      "delayed": false
    },
    {
      "name": "LWpQuarkNonHC",
      "expression": "Block[{mu,sp1,sp2,sp3,i,j,aa}, Sum[1/Sqrt[2] Wp[mu] (gWpR Exp[I omegaWp] Cos[zetaWp] VpRQ[i,j] bar[uq][sp1,i,aa].Ga[mu,sp1,sp2].ProjP[sp2,sp3].dq[sp3,j,aa] + gWpL Sin[zetaWp] VpLQ[i,j] bar[uq][sp1,i,aa].Ga[mu,sp1,sp2].ProjM[sp2,sp3].dq[sp3,j,aa]), {i,1,3}, {j,1,3}, {aa,1,3}]]",
      "delayed": true
    },
    {
      "name": "LWpLeptonNonHC",
      "expression": "Block[{mu,sp1,sp2,sp3,i,j}, Sum[1/Sqrt[2] Wp[mu] (gWpR Exp[I omegaWp] Cos[zetaWp] VpRL[i,j] bar[vR][sp1,i].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,j] + gWpL Sin[zetaWp] VpLL[i,j] bar[vl][sp1,i].Ga[mu,sp1,sp2].ProjM[sp2,sp3].l[sp3,j]), {i,1,3}, {j,1,3}]]",
      "delayed": true
    },
    {
      "name": "LWpFermions",
      "expression": "LWpQuarkNonHC + LWpLeptonNonHC + HC[LWpQuarkNonHC + LWpLeptonNonHC]",
      "delayed": true
    },
    {
      "name": "LBSM",
      "expression": "LkinWp + LkinNuR + LWpFermions",
      "delayed": false
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```