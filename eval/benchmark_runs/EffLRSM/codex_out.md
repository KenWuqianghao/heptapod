```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": [
      "Codex extraction from arXiv:1610.08985"
    ],
    "version": "1.0.0",
    "date": "2026-07-13",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "NP",
      2
    ],
    [
      "QCD",
      1
    ],
    [
      "QED",
      2
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kRquark",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "kRquark",
      "tex": "\\kappa_R^q",
      "description": "Overall normalization of right-handed WR/ZR quark couplings"
    },
    {
      "name": "kRlepton",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "kRlepton",
      "tex": "\\kappa_R^\\ell",
      "description": "Overall normalization of right-handed WR/ZR lepton couplings"
    },
    {
      "name": "MWR",
      "parameter_type": "External",
      "value": "3000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900024,
      "parameter_name": "MWR",
      "tex": "M_{W_R}",
      "description": "Right-handed charged gauge boson mass"
    },
    {
      "name": "MZR",
      "parameter_type": "External",
      "value": "5070.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900032,
      "parameter_name": "MZR",
      "tex": "M_{Z_R}",
      "description": "Right-handed neutral gauge boson mass"
    },
    {
      "name": "MN1",
      "parameter_type": "External",
      "value": "173.3",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900012,
      "parameter_name": "MN1",
      "tex": "M_{N_1}",
      "description": "Heavy Majorana neutrino N1 mass"
    },
    {
      "name": "MN2",
      "parameter_type": "External",
      "value": "1.*^12",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900014,
      "parameter_name": "MN2",
      "tex": "M_{N_2}",
      "description": "Heavy Majorana neutrino N2 mass"
    },
    {
      "name": "MN3",
      "parameter_type": "External",
      "value": "1.*^12",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900016,
      "parameter_name": "MN3",
      "tex": "M_{N_3}",
      "description": "Heavy Majorana neutrino N3 mass"
    },
    {
      "name": "WWR",
      "parameter_type": "External",
      "value": "84.3",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900024,
      "parameter_name": "WWR",
      "tex": "\\Gamma_{W_R}",
      "description": "Right-handed charged gauge boson width"
    },
    {
      "name": "WZR",
      "parameter_type": "External",
      "value": "114.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900032,
      "parameter_name": "WZR",
      "tex": "\\Gamma_{Z_R}",
      "description": "Right-handed neutral gauge boson width"
    },
    {
      "name": "WN1",
      "parameter_type": "External",
      "value": "2.12*^-8",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900012,
      "parameter_name": "WN1",
      "tex": "\\Gamma_{N_1}",
      "description": "Heavy Majorana neutrino N1 width"
    },
    {
      "name": "WN2",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900014,
      "parameter_name": "WN2",
      "tex": "\\Gamma_{N_2}",
      "description": "Heavy Majorana neutrino N2 width"
    },
    {
      "name": "WN3",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900016,
      "parameter_name": "WN3",
      "tex": "\\Gamma_{N_3}",
      "description": "Heavy Majorana neutrino N3 width"
    },
    {
      "name": "CKMR",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "CKMR[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "CKMR[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "CKMR[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "CKMR[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "CKMR[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "CKMR[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "CKMR[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "CKMR[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "CKMR[3,3]",
          "rhs": "1."
        }
      ],
      "complex": false,
      "block_name": "CKMR",
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "CKMR",
      "tex": "V^{\\prime}_{CKM}",
      "description": "Right-handed CKM matrix, diagonal default"
    },
    {
      "name": "YR",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "YR[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "YR[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "YR[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "YR[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "YR[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "YR[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "YR[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "YR[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "YR[3,3]",
          "rhs": "1."
        }
      ],
      "complex": false,
      "block_name": "HNUMIX",
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "YR",
      "tex": "Y_{\\ell N}",
      "description": "Heavy-neutrino/right-handed-lepton mixing, diagonal default"
    },
    {
      "name": "XL",
      "parameter_type": "External",
      "value_rules": [
        {
          "lhs": "XL[1,1]",
          "rhs": "0."
        },
        {
          "lhs": "XL[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "XL[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "XL[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "XL[2,2]",
          "rhs": "0."
        },
        {
          "lhs": "XL[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "XL[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "XL[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "XL[3,3]",
          "rhs": "0."
        }
      ],
      "complex": false,
      "block_name": "LNUMIX",
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "XL",
      "tex": "X_{\\ell \\nu}",
      "description": "Light-neutrino/right-handed-lepton mixing, zero default"
    },
    {
      "name": "gWRq",
      "parameter_type": "Internal",
      "value": "kRquark*ee/(Sqrt[2]*sw)",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "g_{W_R q}"
    },
    {
      "name": "gWRl",
      "parameter_type": "Internal",
      "value": "kRlepton*ee/(Sqrt[2]*sw)",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "g_{W_R \\ell}"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "-kRquark*(ee/sw)*Sqrt[1 - (sw/(cw*kRquark))^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "g_{Z_R q}"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "-kRlepton*(ee/sw)*Sqrt[1 - (sw/(cw*kRlepton))^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "g_{Z_R \\ell}"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "(-1/6)*(sw/(cw*kRquark))^2",
      "complex": false
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*(sw/(cw*kRquark))^2",
      "complex": false
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "(-1/6)*(sw/(cw*kRquark))^2",
      "complex": false
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*(sw/(cw*kRquark))^2",
      "complex": false
    },
    {
      "name": "gZRnuL",
      "parameter_type": "Internal",
      "value": "(1/2)*(sw/(cw*kRlepton))^2",
      "complex": false
    },
    {
      "name": "gZRNR",
      "parameter_type": "Internal",
      "value": "1/2",
      "complex": false
    },
    {
      "name": "gZReL",
      "parameter_type": "Internal",
      "value": "(1/2)*(sw/(cw*kRlepton))^2",
      "complex": false
    },
    {
      "name": "gZReR",
      "parameter_type": "Internal",
      "value": "-1/2 + (sw/(cw*kRlepton))^2",
      "complex": false
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "WR",
      "self_conjugate": false,
      "mass": {
        "sym": "MWR",
        "value": "3000."
      },
      "width": {
        "sym": "WWR",
        "value": "84.3"
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "Right-handed charged gauge boson W_R+, colour singlet, SM SU(2)L singlet, Q=+1",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "ZR",
      "self_conjugate": true,
      "mass": {
        "sym": "MZR",
        "value": "5070."
      },
      "width": {
        "sym": "WZR",
        "value": "114."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 9900032,
      "particle_name": "zr",
      "full_name": "Right-handed neutral gauge boson Z_R, colour singlet, SM SU(2)L singlet, Q=0",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "N",
      "self_conjugate": true,
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
            "173.3"
          ],
          [
            "MN2",
            "1.*^12"
          ],
          [
            "MN3",
            "1.*^12"
          ]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          [
            "WN1",
            "2.12*^-8"
          ],
          [
            "WN2",
            "0."
          ],
          [
            "WN3",
            "0."
          ]
        ]
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
        "n1",
        "n2",
        "n3"
      ],
      "full_name": [
        "Heavy Majorana neutrino N1, colour singlet, SM SU(2)L singlet, Q=0",
        "Heavy Majorana neutrino N2, colour singlet, SM SU(2)L singlet, Q=0",
        "Heavy Majorana neutrino N3, colour singlet, SM SU(2)L singlet, Q=0"
      ],
      "propagator_label": [
        "N1",
        "N2",
        "N3"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "None",
      "majorana_phase": "1"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LWRQuarksNonHC",
      "expression": "Block[{mu,ii,jj,cc}, -gWRq Sum[CKMR[ii,jj] bar[u[ii,cc]].Ga[mu].ProjP.d[jj,cc] WR[mu], {ii,1,3}, {jj,1,3}, {cc,1,3}]]",
      "delayed": true
    },
    {
      "name": "LWRQuarks",
      "expression": "LWRQuarksNonHC + HC[LWRQuarksNonHC]",
      "delayed": true
    },
    {
      "name": "LWRLeptonsNonHC",
      "expression": "Block[{mu,ll,nn}, -gWRl Sum[YR[ll,nn] bar[N[nn]].Ga[mu].ProjP.l[ll] WR[mu], {ll,1,3}, {nn,1,3}]]",
      "delayed": true
    },
    {
      "name": "LWRLightNuNonHC",
      "expression": "Block[{mu,ll,nn}, -gWRl Sum[XL[ll,nn] bar[ve[nn]].Ga[mu].ProjP.l[ll] WR[mu], {ll,1,3}, {nn,1,3}]]",
      "delayed": true
    },
    {
      "name": "LWRLeptons",
      "expression": "LWRLeptonsNonHC + LWRLightNuNonHC + HC[LWRLeptonsNonHC + LWRLightNuNonHC]",
      "delayed": true
    },
    {
      "name": "LZRQuarks",
      "expression": "Block[{mu,ii,cc}, gZRq Sum[(bar[u[ii,cc]].Ga[mu].(gZRuL ProjM + gZRuR ProjP).u[ii,cc] + bar[d[ii,cc]].Ga[mu].(gZRdL ProjM + gZRdR ProjP).d[ii,cc]) ZR[mu], {ii,1,3}, {cc,1,3}]]",
      "delayed": true
    },
    {
      "name": "LZRLeptons",
      "expression": "Block[{mu,ii}, gZRl Sum[(bar[l[ii]].Ga[mu].(gZReL ProjM + gZReR ProjP).l[ii] + bar[ve[ii]].Ga[mu].gZRnuL ProjM.ve[ii] + bar[N[ii]].Ga[mu].gZRNR ProjP.N[ii]) ZR[mu], {ii,1,3}]]",
      "delayed": true
    },
    {
      "name": "LBSM",
      "expression": "LWRQuarks + LWRLeptons + LZRQuarks + LZRLeptons",
      "delayed": false
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```