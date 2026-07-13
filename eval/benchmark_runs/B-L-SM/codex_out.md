```json
{
  "model_name": "B-L-SM_gen",
  "info": {
    "authors": [
      "Codex extraction from arXiv:1811.11452"
    ],
    "version": "1.0.0",
    "date": "2026-07-13"
  },
  "interaction_order_hierarchy": [
    [
      "NP",
      2
    ]
  ],
  "interaction_order_limit": [
    [
      "NP",
      4
    ]
  ],
  "feynman_gauge": false,
  "vevs": [
    [
      "Chi",
      "xBL"
    ]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "g1p",
      "parameter_type": "External",
      "value": "0.2",
      "complex": false,
      "block_name": "BLINPUTS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "g1p",
      "tex": "g'_1",
      "description": "U(1)_{B-L} gauge coupling"
    },
    {
      "name": "gtilde",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BLINPUTS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gtilde",
      "tex": "\\tilde{g}",
      "description": "U(1)_Y-U(1)_{B-L} gauge mixing, set to zero in the minimal model"
    },
    {
      "name": "sa",
      "parameter_type": "External",
      "value": "0.2",
      "complex": false,
      "block_name": "BLINPUTS",
      "order_block": 3,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "sa",
      "tex": "\\sin\\alpha",
      "description": "Higgs-singlet mixing sine"
    },
    {
      "name": "MZp",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 32,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MZp",
      "tex": "M_{Z'}",
      "description": "Mass of the B-L gauge boson"
    },
    {
      "name": "WZp",
      "parameter_type": "External",
      "value": "Automatic",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 32,
      "parameter_name": "WZp",
      "tex": "\\Gamma_{Z'}",
      "description": "Width of the B-L gauge boson"
    },
    {
      "name": "MH2",
      "parameter_type": "External",
      "value": "200.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 35,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MH2",
      "tex": "M_{h_2}",
      "description": "Mass of the second neutral Higgs mass eigenstate"
    },
    {
      "name": "WH2",
      "parameter_type": "External",
      "value": "Automatic",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 35,
      "parameter_name": "WH2",
      "tex": "\\Gamma_{h_2}",
      "description": "Width of the second neutral Higgs mass eigenstate"
    },
    {
      "name": "MN1",
      "parameter_type": "External",
      "value": "200.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900012,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MN1",
      "tex": "M_{N_1}",
      "description": "Heavy Majorana neutrino mass, generation 1"
    },
    {
      "name": "MN2",
      "parameter_type": "External",
      "value": "200.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900014,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MN2",
      "tex": "M_{N_2}",
      "description": "Heavy Majorana neutrino mass, generation 2"
    },
    {
      "name": "MN3",
      "parameter_type": "External",
      "value": "200.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900016,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MN3",
      "tex": "M_{N_3}",
      "description": "Heavy Majorana neutrino mass, generation 3"
    },
    {
      "name": "WN1",
      "parameter_type": "External",
      "value": "Automatic",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900012,
      "parameter_name": "WN1",
      "tex": "\\Gamma_{N_1}",
      "description": "Heavy Majorana neutrino width, generation 1"
    },
    {
      "name": "WN2",
      "parameter_type": "External",
      "value": "Automatic",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900014,
      "parameter_name": "WN2",
      "tex": "\\Gamma_{N_2}",
      "description": "Heavy Majorana neutrino width, generation 2"
    },
    {
      "name": "WN3",
      "parameter_type": "External",
      "value": "Automatic",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900016,
      "parameter_name": "WN3",
      "tex": "\\Gamma_{N_3}",
      "description": "Heavy Majorana neutrino width, generation 3"
    },
    {
      "name": "VLN",
      "parameter_type": "External",
      "complex": false,
      "block_name": "VLNMIX",
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "VLN[1,1]",
          "rhs": "1.*^-6"
        },
        {
          "lhs": "VLN[2,2]",
          "rhs": "1.*^-6"
        },
        {
          "lhs": "VLN[3,3]",
          "rhs": "1.*^-6"
        },
        {
          "lhs": "VLN[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "VLN[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "VLN[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "VLN[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "VLN[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "VLN[3,2]",
          "rhs": "0."
        }
      ],
      "parameter_name": "VLN",
      "tex": "V_{lN}",
      "description": "Active-sterile neutrino mixing matrix"
    },
    {
      "name": "alpha",
      "parameter_type": "Internal",
      "value": "ArcSin[sa]",
      "complex": false,
      "parameter_name": "alpha",
      "tex": "\\alpha",
      "description": "Higgs-singlet mixing angle"
    },
    {
      "name": "ca",
      "parameter_type": "Internal",
      "value": "Cos[alpha]",
      "complex": false,
      "parameter_name": "ca",
      "tex": "\\cos\\alpha",
      "description": "Cosine of the Higgs-singlet mixing angle"
    },
    {
      "name": "xBL",
      "parameter_type": "Internal",
      "value": "MZp/(2*g1p)",
      "complex": false,
      "parameter_name": "xBL",
      "tex": "x",
      "description": "B-L breaking vacuum expectation value"
    },
    {
      "name": "lambda1BL",
      "parameter_type": "Internal",
      "value": "(MH^2*ca^2 + MH2^2*sa^2)/(2*vev^2)",
      "complex": false,
      "parameter_name": "lambda1BL",
      "tex": "\\lambda_1",
      "description": "Doublet quartic reconstructed from physical scalar masses and mixing"
    },
    {
      "name": "lambda2BL",
      "parameter_type": "Internal",
      "value": "(MH^2*sa^2 + MH2^2*ca^2)/(2*xBL^2)",
      "complex": false,
      "parameter_name": "lambda2BL",
      "tex": "\\lambda_2",
      "description": "Singlet quartic reconstructed from physical scalar masses and mixing"
    },
    {
      "name": "lambda3BL",
      "parameter_type": "Internal",
      "value": "(MH2^2 - MH^2)*sa*ca/(vev*xBL)",
      "complex": false,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lambda3BL",
      "tex": "\\lambda_3",
      "description": "Higgs portal quartic reconstructed from physical scalar masses and mixing"
    },
    {
      "name": "muChi2",
      "parameter_type": "Internal",
      "value": "-lambda2BL*xBL^2 - lambda3BL*vev^2/2",
      "complex": false,
      "parameter_name": "muChi2",
      "tex": "\\mu_\\chi^2",
      "description": "Singlet quadratic potential parameter from the minimum condition"
    },
    {
      "name": "yM",
      "parameter_type": "Internal",
      "complex": false,
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "yM[1,1]",
          "rhs": "MN1/(Sqrt[2]*xBL)"
        },
        {
          "lhs": "yM[2,2]",
          "rhs": "MN2/(Sqrt[2]*xBL)"
        },
        {
          "lhs": "yM[3,3]",
          "rhs": "MN3/(Sqrt[2]*xBL)"
        },
        {
          "lhs": "yM[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "yM[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "yM[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "yM[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "yM[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "yM[3,2]",
          "rhs": "0."
        }
      ],
      "parameter_name": "yM",
      "tex": "y_M",
      "description": "Majorana Yukawa matrix for right-handed neutrinos"
    },
    {
      "name": "ynu",
      "parameter_type": "Internal",
      "complex": false,
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "ynu[1,1]",
          "rhs": "Sqrt[2]*MN1*VLN[1,1]/vev"
        },
        {
          "lhs": "ynu[2,2]",
          "rhs": "Sqrt[2]*MN2*VLN[2,2]/vev"
        },
        {
          "lhs": "ynu[3,3]",
          "rhs": "Sqrt[2]*MN3*VLN[3,3]/vev"
        },
        {
          "lhs": "ynu[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "ynu[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "ynu[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "ynu[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "ynu[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "ynu[3,2]",
          "rhs": "0."
        }
      ],
      "parameter_name": "ynu",
      "tex": "y_\\nu",
      "description": "Neutrino Dirac Yukawa matrix"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {
        "sym": "MZp",
        "value": "1000."
      },
      "width": {
        "sym": "WZp",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "B-L gauge boson",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "H2",
      "self_conjugate": true,
      "mass": {
        "sym": "MH2",
        "value": "200."
      },
      "width": {
        "sym": "WH2",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 35,
      "particle_name": "h2",
      "full_name": "Second neutral Higgs mass eigenstate",
      "propagator_label": "h2",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "GZp",
      "self_conjugate": true,
      "mass": {
        "sym": "MZp",
        "value": "1000."
      },
      "width": {
        "massless": true
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 2500032,
      "particle_name": "GZp",
      "full_name": "B-L Goldstone boson",
      "propagator_label": "GZp",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "goldstone": "Zp"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "Chi",
      "self_conjugate": false,
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "BL": "2"
      },
      "unphysical": true,
      "definitions": [
        "Chi -> (xBL - sa H + ca H2 + I GZp)/Sqrt[2]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N",
      "self_conjugate": true,
      "indices": [
        "Generation"
      ],
      "flavor_index": "Generation",
      "class_members": [
        "N1",
        "N2",
        "N3"
      ],
      "mass": {
        "sym": "MN",
        "members": [
          [
            "MN1",
            "200."
          ],
          [
            "MN2",
            "200."
          ],
          [
            "MN3",
            "200."
          ]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          [
            "WN1",
            "Automatic"
          ],
          [
            "WN2",
            "Automatic"
          ],
          [
            "WN3",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "BL": "-1"
      },
      "pdg": [
        9900012,
        9900014,
        9900016
      ],
      "particle_name": [
        "N1",
        "N2",
        "N3"
      ],
      "full_name": [
        "Heavy Majorana neutrino 1",
        "Heavy Majorana neutrino 2",
        "Heavy Majorana neutrino 3"
      ],
      "propagator_label": [
        "N1",
        "N2",
        "N3"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "nuR",
      "self_conjugate": false,
      "indices": [
        "Generation"
      ],
      "flavor_index": "Generation",
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "BL": "-1"
      },
      "unphysical": true,
      "definitions": [
        "nuR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] N[sp2,ff]]"
      ]
    }
  ],
  "gauge_xi": [
    [
      "V[100]",
      "GaugeXi[Zp]"
    ],
    [
      "S[101]",
      "GaugeXi[Zp]"
    ]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "expression": "Block[{mu,nu}, -1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]",
      "delayed": true
    },
    {
      "name": "LChi",
      "expression": "Block[{mu,ii}, ExpandIndices[(del[HC[Chi],mu] - I*2*g1p*Zp[mu]*HC[Chi])*(del[Chi,mu] + I*2*g1p*Zp[mu]*Chi) - muChi2*HC[Chi]*Chi - lambda2BL*(HC[Chi]*Chi)^2 - lambda3BL*(Phibar[ii]*Phi[ii])*(HC[Chi]*Chi), FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LBLCurrent",
      "expression": "Block[{mu}, ExpandIndices[-g1p*Zp[mu]*(1/3 QLbar.Ga[mu].QL + 1/3 uRbar.Ga[mu].uR + 1/3 dRbar.Ga[mu].dR - LLbar.Ga[mu].LL - lRbar.Ga[mu].lR - nuRbar.Ga[mu].nuR), FlavorExpand -> {SU2D, Generation, Colour}]]",
      "delayed": true
    },
    {
      "name": "LNuYukNonHC",
      "expression": "Block[{sp,ii,jj,ff1,ff2}, ExpandIndices[-ynu[ff1,ff2] LLbar[sp,ii,ff1].nuR[sp,ff2] Phibar[jj] Eps[ii,jj] - yM[ff1,ff2] anti[CC[nuR]][sp,ff1].nuR[sp,ff2] Chi, FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LNuYuk",
      "expression": "LNuYukNonHC + HC[LNuYukNonHC]",
      "delayed": true
    },
    {
      "name": "LBSM",
      "expression": "LZpKin + LChi + LBLCurrent + LNuYuk",
      "delayed": false
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```