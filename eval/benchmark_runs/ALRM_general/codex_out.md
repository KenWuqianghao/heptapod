```json
{
  "model_name": "ALRM_general_gen",
  "info": {
    "authors": [
      "Mariana Frank",
      "Benjamin Fuks",
      "Ozer Ozdal"
    ],
    "version": "1.0",
    "date": "2026-07-13",
    "institutions": [
      "Concordia University",
      "LPTHE"
    ],
    "emails": [
      "mariana.frank@concordia.ca",
      "fuks@lpthe.jussieu.fr",
      "ozer.ozdal@concordia.ca"
    ]
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
      "NP",
      99
    ]
  ],
  "feynman_gauge": true,
  "vevs": [
    [
      "Phi[2,2]",
      "kALR/Sqrt[2]"
    ],
    [
      "chiL[2]",
      "vLALR/Sqrt[2]"
    ],
    [
      "chiR[2]",
      "vRALR/Sqrt[2]"
    ]
  ],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Scalar4",
      "range_kind": "NoUnfold",
      "size": 4
    },
    {
      "name": "Scalar2",
      "range_kind": "NoUnfold",
      "size": 2
    }
  ],
  "parameters": [
    {
      "name": "tb",
      "parameter_type": "External",
      "value": "4.58",
      "block_name": "SMINPUTS",
      "order_block": 5,
      "parameter_name": "tb",
      "tex": "t_\\beta",
      "description": "tan beta = k/vL"
    },
    {
      "name": "gR",
      "parameter_type": "External",
      "value": "0.374",
      "block_name": "SMINPUTS",
      "order_block": 6,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gR",
      "tex": "g_R"
    },
    {
      "name": "vevp",
      "parameter_type": "External",
      "value": "7799.",
      "block_name": "SMINPUTS",
      "order_block": 7,
      "parameter_name": "vevp",
      "tex": "v'"
    },
    {
      "name": "lam2",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HPOTINPUTS",
      "order_block": 1,
      "parameter_name": "lam2",
      "tex": "\\lambda_2"
    },
    {
      "name": "lam3",
      "parameter_type": "External",
      "value": "0.0196",
      "block_name": "HPOTINPUTS",
      "order_block": 2,
      "parameter_name": "lam3",
      "tex": "\\lambda_3"
    },
    {
      "name": "alp1",
      "parameter_type": "External",
      "value": "0.0144",
      "block_name": "HPOTINPUTS",
      "order_block": 3,
      "parameter_name": "alp1",
      "tex": "\\alpha_1"
    },
    {
      "name": "alp2",
      "parameter_type": "External",
      "value": "0.0144",
      "block_name": "HPOTINPUTS",
      "order_block": 4,
      "parameter_name": "alp2",
      "tex": "\\alpha_2"
    },
    {
      "name": "alp3",
      "parameter_type": "External",
      "value": "0.0144",
      "block_name": "HPOTINPUTS",
      "order_block": 5,
      "parameter_name": "alp3",
      "tex": "\\alpha_3"
    },
    {
      "name": "kap",
      "parameter_type": "External",
      "value": "-31.08",
      "block_name": "HPOTINPUTS",
      "order_block": 6,
      "parameter_name": "kap",
      "tex": "\\kappa"
    },
    {
      "name": "Ghgg",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "EFFECTIVEHIGGS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "Ghgg",
      "tex": "a_H^g"
    },
    {
      "name": "Ghaa",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "EFFECTIVEHIGGS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "Ghaa",
      "tex": "a_H^\\gamma"
    },
    {
      "name": "Mve",
      "parameter_type": "External",
      "value": "1.*^-12",
      "block_name": "MASS",
      "order_block": 12,
      "parameter_name": "Mve"
    },
    {
      "name": "Mvm",
      "parameter_type": "External",
      "value": "1.*^-12",
      "block_name": "MASS",
      "order_block": 14,
      "parameter_name": "Mvm"
    },
    {
      "name": "Mvt",
      "parameter_type": "External",
      "value": "1.*^-12",
      "block_name": "MASS",
      "order_block": 16,
      "parameter_name": "Mvt"
    },
    {
      "name": "Mne",
      "parameter_type": "External",
      "value": "750.",
      "block_name": "MASS",
      "order_block": 6000012,
      "parameter_name": "Mne"
    },
    {
      "name": "Mnm",
      "parameter_type": "External",
      "value": "900.",
      "block_name": "MASS",
      "order_block": 6000014,
      "parameter_name": "Mnm"
    },
    {
      "name": "Mnt",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "MASS",
      "order_block": 6000016,
      "parameter_name": "Mnt"
    },
    {
      "name": "MDP",
      "parameter_type": "External",
      "value": "1500.",
      "block_name": "MASS",
      "order_block": 6000001,
      "parameter_name": "MDP"
    },
    {
      "name": "MSP",
      "parameter_type": "External",
      "value": "1700.",
      "block_name": "MASS",
      "order_block": 6000003,
      "parameter_name": "MSP"
    },
    {
      "name": "MBP",
      "parameter_type": "External",
      "value": "2000.",
      "block_name": "MASS",
      "order_block": 6000005,
      "parameter_name": "MBP"
    },
    {
      "name": "CKMlam",
      "parameter_type": "External",
      "value": "0.22537",
      "block_name": "CKMBLOCK",
      "order_block": 1,
      "parameter_name": "CKMlam"
    },
    {
      "name": "CKMA",
      "parameter_type": "External",
      "value": "0.814",
      "block_name": "CKMBLOCK",
      "order_block": 2,
      "parameter_name": "CKMA"
    },
    {
      "name": "CKMrho",
      "parameter_type": "External",
      "value": "0.117",
      "block_name": "CKMBLOCK",
      "order_block": 3,
      "parameter_name": "CKMrho"
    },
    {
      "name": "CKMeta",
      "parameter_type": "External",
      "value": "0.353",
      "block_name": "CKMBLOCK",
      "order_block": 4,
      "parameter_name": "CKMeta"
    },
    {
      "name": "CKMps12",
      "parameter_type": "External",
      "value": "0.22537",
      "block_name": "CKMBLOCK",
      "order_block": 11,
      "parameter_name": "CKMps12"
    },
    {
      "name": "CKMps23",
      "parameter_type": "External",
      "value": "0.041",
      "block_name": "CKMBLOCK",
      "order_block": 12,
      "parameter_name": "CKMps23"
    },
    {
      "name": "CKMps13",
      "parameter_type": "External",
      "value": "0.0035",
      "block_name": "CKMBLOCK",
      "order_block": 13,
      "parameter_name": "CKMps13"
    },
    {
      "name": "CKMpdel",
      "parameter_type": "External",
      "value": "1.20",
      "block_name": "CKMBLOCK",
      "order_block": 14,
      "parameter_name": "CKMpdel"
    },
    {
      "name": "PMNSs12",
      "parameter_type": "External",
      "value": "0.551",
      "block_name": "PMNSBLOCK",
      "order_block": 1,
      "parameter_name": "PMNSs12"
    },
    {
      "name": "PMNSs23",
      "parameter_type": "External",
      "value": "0.757",
      "block_name": "PMNSBLOCK",
      "order_block": 2,
      "parameter_name": "PMNSs23"
    },
    {
      "name": "PMNSs13",
      "parameter_type": "External",
      "value": "0.149",
      "block_name": "PMNSBLOCK",
      "order_block": 3,
      "parameter_name": "PMNSs13"
    },
    {
      "name": "PMNSdel",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PMNSBLOCK",
      "order_block": 4,
      "parameter_name": "PMNSdel"
    },
    {
      "name": "PMNSps12",
      "parameter_type": "External",
      "value": "0.551",
      "block_name": "PMNSBLOCK",
      "order_block": 11,
      "parameter_name": "PMNSps12"
    },
    {
      "name": "PMNSps23",
      "parameter_type": "External",
      "value": "0.757",
      "block_name": "PMNSBLOCK",
      "order_block": 12,
      "parameter_name": "PMNSps23"
    },
    {
      "name": "PMNSps13",
      "parameter_type": "External",
      "value": "0.149",
      "block_name": "PMNSBLOCK",
      "order_block": 13,
      "parameter_name": "PMNSps13"
    },
    {
      "name": "PMNSpdel",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PMNSBLOCK",
      "order_block": 14,
      "parameter_name": "PMNSpdel"
    },
    {
      "name": "vALR",
      "parameter_type": "Internal",
      "value": "1/Sqrt[Sqrt[2] Gf]",
      "parameter_name": "vALR"
    },
    {
      "name": "kALR",
      "parameter_type": "Internal",
      "value": "vALR tb/Sqrt[1 + tb^2]",
      "parameter_name": "kALR"
    },
    {
      "name": "vLALR",
      "parameter_type": "Internal",
      "value": "vALR/Sqrt[1 + tb^2]",
      "parameter_name": "vLALR"
    },
    {
      "name": "vRALR",
      "parameter_type": "Internal",
      "value": "Sqrt[vevp^2 - kALR^2]",
      "parameter_name": "vRALR"
    },
    {
      "name": "sPhiW",
      "parameter_type": "Internal",
      "value": "g1/gR",
      "parameter_name": "sPhiW"
    },
    {
      "name": "cPhiW",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - sPhiW^2]",
      "parameter_name": "cPhiW"
    },
    {
      "name": "gBL",
      "parameter_type": "Internal",
      "value": "gR g1/Sqrt[gR^2 - g1^2]",
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gBL"
    },
    {
      "name": "alp12",
      "parameter_type": "Internal",
      "value": "alp1 + alp2",
      "parameter_name": "alp12"
    },
    {
      "name": "mu1sq",
      "parameter_type": "Internal",
      "value": "alp12 (vLALR^2 + vRALR^2) + kALR^2 lam1 + kap vLALR vRALR/(Sqrt[2] kALR)",
      "parameter_name": "mu1sq"
    },
    {
      "name": "mu2sq",
      "parameter_type": "Internal",
      "value": "alp12 kALR^2 + lam3 (vLALR^2 + vRALR^2)",
      "parameter_name": "mu2sq"
    },
    {
      "name": "lam4",
      "parameter_type": "Internal",
      "value": "lam3 - kap kALR/(Sqrt[2] vLALR vRALR)",
      "parameter_name": "lam4"
    },
    {
      "name": "lam1",
      "parameter_type": "Internal",
      "value": "Internal",
      "parameter_name": "lam1",
      "description": "Derived from the SM-like Higgs mass MH0 by eq. (A.10)"
    },
    {
      "name": "MWp",
      "parameter_type": "Internal",
      "value": "1/2 gR Sqrt[kALR^2 + vRALR^2]",
      "parameter_name": "MWp"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "1/2 Sqrt[(gBL^2 sPhiW^2 vLALR^2 + gR^2 (cPhiW^4 kALR^2 + vRALR^2))/cPhiW^2]",
      "parameter_name": "MZp"
    },
    {
      "name": "MH01",
      "parameter_type": "Internal",
      "value": "Sqrt[-(alp2 - alp3) (vLALR^2 + vRALR^2) - kap vLALR vRALR/(Sqrt[2] kALR) + 2 kALR^2 lam2]",
      "parameter_name": "MH01"
    },
    {
      "name": "MA01",
      "parameter_type": "Internal",
      "value": "MH01",
      "parameter_name": "MA01"
    },
    {
      "name": "MH02",
      "parameter_type": "Internal",
      "value": "Internal",
      "parameter_name": "MH02",
      "description": "Second CP-even scalar mass from eq. (A.11)"
    },
    {
      "name": "MH03",
      "parameter_type": "Internal",
      "value": "Internal",
      "parameter_name": "MH03",
      "description": "Third CP-even scalar mass from eq. (A.11)"
    },
    {
      "name": "MA02",
      "parameter_type": "Internal",
      "value": "Sqrt[-kap (vLALR^2 vRALR^2 + kALR^2 (vLALR^2 + vRALR^2))/(Sqrt[2] kALR vLALR vRALR)]",
      "parameter_name": "MA02"
    },
    {
      "name": "MHP1",
      "parameter_type": "Internal",
      "value": "Sqrt[(kALR^2 + vLALR^2)/(2 kALR vLALR) (-2 (alp2 - alp3) kALR vLALR - Sqrt[2] kap vRALR)]",
      "parameter_name": "MHP1"
    },
    {
      "name": "MHP2",
      "parameter_type": "Internal",
      "value": "Sqrt[(kALR^2 + vRALR^2)/(2 kALR vRALR) (-2 (alp2 - alp3) kALR vRALR - Sqrt[2] kap vLALR)]",
      "parameter_name": "MHP2"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 31,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {
        "sym": "MZp",
        "value": "Internal"
      },
      "width": {
        "sym": "WZp",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "Z-prime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 32,
      "class_name": "Wp",
      "self_conjugate": false,
      "mass": {
        "sym": "MWp",
        "value": "Internal"
      },
      "width": {
        "sym": "WWp",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": 34,
      "particle_name": "Wp+",
      "antiparticle_name": "Wp-",
      "full_name": "W-prime",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 31,
      "class_name": "nl",
      "self_conjugate": false,
      "indices": [
        "Generation"
      ],
      "flavor_index": "Generation",
      "class_members": [
        "ne",
        "nm",
        "nt"
      ],
      "mass": {
        "sym": "Mnl",
        "members": [
          [
            "Mne",
            "750."
          ],
          [
            "Mnm",
            "900."
          ],
          [
            "Mnt",
            "1000."
          ]
        ]
      },
      "width": {
        "sym": "Wnl",
        "members": [
          [
            "Wne",
            "Automatic"
          ],
          [
            "Wnm",
            "Automatic"
          ],
          [
            "Wnt",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": [
        6000012,
        6000014,
        6000016
      ],
      "particle_name": [
        "ne",
        "nm",
        "nt"
      ],
      "antiparticle_name": [
        "ne~",
        "nm~",
        "nt~"
      ],
      "full_name": [
        "electron scotino",
        "muon scotino",
        "tau scotino"
      ],
      "propagator_label": "n",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 32,
      "class_name": "dqp",
      "self_conjugate": false,
      "indices": [
        "Colour",
        "Generation"
      ],
      "flavor_index": "Generation",
      "class_members": [
        "dqp",
        "sqp",
        "bqp"
      ],
      "mass": {
        "sym": "Mdqp",
        "members": [
          [
            "MDP",
            "1500."
          ],
          [
            "MSP",
            "1700."
          ],
          [
            "MBP",
            "2000."
          ]
        ]
      },
      "width": {
        "sym": "Wdqp",
        "members": [
          [
            "WDP",
            "Automatic"
          ],
          [
            "WSP",
            "Automatic"
          ],
          [
            "WBP",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "-1/3"
      },
      "pdg": [
        6000001,
        6000003,
        6000005
      ],
      "particle_name": [
        "dqp",
        "sqp",
        "bqp"
      ],
      "antiparticle_name": [
        "dqp~",
        "sqp~",
        "bqp~"
      ],
      "full_name": [
        "exotic down quark",
        "exotic strange quark",
        "exotic bottom quark"
      ],
      "propagator_label": "d'",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 31,
      "class_name": "h0",
      "self_conjugate": true,
      "flavor_index": "Scalar4",
      "class_members": [
        "h0",
        "h01",
        "h02",
        "h03"
      ],
      "mass": {
        "sym": "Mh0",
        "members": [
          [
            "MH",
            "125."
          ],
          [
            "MH01",
            "Internal"
          ],
          [
            "MH02",
            "Internal"
          ],
          [
            "MH03",
            "Internal"
          ]
        ]
      },
      "width": {
        "sym": "Wh0",
        "members": [
          [
            "WH",
            "Automatic"
          ],
          [
            "WH01",
            "Automatic"
          ],
          [
            "WH02",
            "Automatic"
          ],
          [
            "WH03",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": [
        25,
        25,
        45,
        55
      ],
      "particle_name": [
        "h0",
        "h01",
        "h02",
        "h03"
      ],
      "full_name": [
        "SM-like CP-even Higgs",
        "CP-even Higgs 1",
        "CP-even Higgs 2",
        "CP-even Higgs 3"
      ],
      "propagator_label": [
        "h0",
        "h1",
        "h2",
        "h3"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 32,
      "class_name": "A0",
      "self_conjugate": true,
      "flavor_index": "Scalar2",
      "class_members": [
        "A01",
        "A02"
      ],
      "mass": {
        "sym": "MA0",
        "members": [
          [
            "MA01",
            "Internal"
          ],
          [
            "MA02",
            "Internal"
          ]
        ]
      },
      "width": {
        "sym": "WA0",
        "members": [
          [
            "WA01",
            "Automatic"
          ],
          [
            "WA02",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": [
        36,
        46
      ],
      "particle_name": [
        "A01",
        "A02"
      ],
      "full_name": [
        "CP-odd Higgs 1",
        "CP-odd Higgs 2"
      ],
      "propagator_label": [
        "A1",
        "A2"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 33,
      "class_name": "Hp",
      "self_conjugate": false,
      "flavor_index": "Scalar2",
      "class_members": [
        "Hp1",
        "Hp2"
      ],
      "mass": {
        "sym": "MHp",
        "members": [
          [
            "MHP1",
            "Internal"
          ],
          [
            "MHP2",
            "Internal"
          ]
        ]
      },
      "width": {
        "sym": "WHp",
        "members": [
          [
            "WHP1",
            "Automatic"
          ],
          [
            "WHP2",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": [
        37,
        47
      ],
      "particle_name": [
        "Hp1",
        "Hp2"
      ],
      "antiparticle_name": [
        "Hm1",
        "Hm2"
      ],
      "full_name": [
        "charged Higgs 1",
        "charged Higgs 2"
      ],
      "propagator_label": [
        "H+1",
        "H+2"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LYALRM",
      "expression": "Yu[i,j] HC[QL[i]].Phihat.QR[j] - Yd[i,j] HC[QL[i]].chiL.dR[j] - Ydp[i,j] HC[QR[i]].chiR.dPL[j] - Ye[i,j] HC[LL[i]].Phi.LR[j] + Ynu[i,j] HC[LL[i]].chiLhat.nuR[j] + Yn[i,j] HC[LR[i]].chiRhat.nL[j] + HC[Yu[i,j] HC[QL[i]].Phihat.QR[j] - Yd[i,j] HC[QL[i]].chiL.dR[j] - Ydp[i,j] HC[QR[i]].chiR.dPL[j] - Ye[i,j] HC[LL[i]].Phi.LR[j] + Ynu[i,j] HC[LL[i]].chiLhat.nuR[j] + Yn[i,j] HC[LR[i]].chiRhat.nL[j]]"
    },
    {
      "name": "VHALRM",
      "expression": "-mu1sq Tr[HC[Phi].Phi] - mu2sq (HC[chiL].chiL + HC[chiR].chiR) + lam1 Tr[HC[Phi].Phi]^2 + lam2 (Phi.phihat) (HC[phihat].HC[Phi]) + lam3 ((HC[chiL].chiL)^2 + (HC[chiR].chiR)^2) + 2 lam4 (HC[chiL].chiL) (HC[chiR].chiR) + 2 alp1 Tr[HC[Phi].Phi] (HC[chiL].chiL + HC[chiR].chiR) + 2 alp2 ((HC[chiL].Phi) (chiL.HC[Phi]) + (HC[Phi].HC[chiR]) (Phi.chiR)) + 2 alp3 ((HC[chiL].HC[phihat]) (chiL.phihat) + (phihat.HC[chiR]) (HC[phihat].chiR)) + kap (HC[chiL].Phi.chiR + HC[chiR].HC[Phi].chiL)"
    },
    {
      "name": "LSALRM",
      "expression": "DC[Phi,mu] HC[DC[Phi,mu]] + DC[chiL,mu] HC[DC[chiL,mu]] + DC[chiR,mu] HC[DC[chiR,mu]] - VHALRM"
    },
    {
      "name": "LFALRM",
      "expression": "I HC[nl].Ga[mu].DC[nl,mu] + I HC[dqp].Ga[mu].DC[dqp,mu]"
    },
    {
      "name": "LeffALRM",
      "expression": "-1/4 Ghgg h0 FS[G,mu,nu,a] FS[G,mu,nu,a] - 1/4 Ghaa h0 FS[A,mu,nu] FS[A,mu,nu]"
    }
  ],
  "raw_blocks": [
    "phihat = sig2.Phi.sig2; chiLhat = I sig2.chiL; chiRhat = I sig2.chiR;",
    "(* Neutral scalar mixing: Im[{phi01,phi02,chiL0,chiR0}] = {{1,0,0,0},{0,UA[1,1],UA[1,2],UA[1,3]},{0,UA[2,1],UA[2,2],UA[2,3]},{0,UA[3,1],UA[3,2],UA[3,3]}}.{A01,G01,G02,A02}; Re[{phi01,phi02,chiL0,chiR0}] = {{1,0,0,0},{0,UH[1,1],UH[1,2],UH[1,3]},{0,UH[2,1],UH[2,2],UH[2,3]},{0,UH[3,1],UH[3,2],UH[3,3]}}.{h01,h0,h02,h03}. *)",
    "(* Charged scalar mixing: {phi2p,chiLp} = {{Cos[beta],Sin[beta]},{-Sin[beta],Cos[beta]}}.{Hp1,Gp}; {phi1p,chiRp} = {{Cos[zeta],Sin[zeta]},{-Sin[zeta],Cos[zeta]}}.{Hp2,Gpp}. *)",
    "(* Neutral gauge mixing follows eq. (2.12): {B,WL3,WR3}=Rphi.Rtheta.Rvartheta.{A,Z,Zp}. Charged W and Wp do not mix. *)"
  ]
}
```