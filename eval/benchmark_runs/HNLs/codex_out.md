```json
{
  "model_name": "HNLs_gen",
  "info": {
    "authors": [
      "P. Coloma",
      "E. Fernandez-Martinez",
      "M. Gonzalez-Lopez",
      "J. Hernandez-Garcia"
    ],
    "version": "1.0.0",
    "date": "06. 06. 2020",
    "institutions": [
      "Instituto de Fisica Corpuscular, Universidad de Valencia & CSIC, and Instituto de Fisica Teorica UAM/CSIC",
      "Departamento de Fisica Teorica & Instituto de Fisica Teorica, Universidad Autonoma de Madrid & CSIC",
      "Institute for Theoretical Physics, ELTE Eotvos Lorand University"
    ],
    "emails": [
      "pilar.coloma@ift.csic.es",
      "enrique.fernandez-martinez@uam.es",
      "manuel.gonzalezl@uam.es",
      "josu.hernandez@ttk.elte.hu"
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
      1
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Neutrinos",
      "range_kind": "NoUnfold",
      "size": 4,
      "style_symbol": "n"
    },
    {
      "name": "Heavynus",
      "range_kind": "NoUnfold",
      "size": 1,
      "style_symbol": "r"
    }
  ],
  "parameters": [
    {
      "name": "modthetae",
      "parameter_type": "External",
      "value": "0.00001",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 16,
      "description": "Heavy-nu-electron mixing modulus"
    },
    {
      "name": "argthetae",
      "parameter_type": "External",
      "value": "0",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 17,
      "description": "Heavy-nu-electron mixing argument in degrees"
    },
    {
      "name": "modthetamu",
      "parameter_type": "External",
      "value": "0.00001",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 18,
      "description": "Heavy-nu-muon mixing modulus"
    },
    {
      "name": "argthetamu",
      "parameter_type": "External",
      "value": "0",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 19,
      "description": "Heavy-nu-muon mixing argument in degrees"
    },
    {
      "name": "modthetatau",
      "parameter_type": "External",
      "value": "0.00001",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 20,
      "description": "Heavy-nu-tau mixing modulus"
    },
    {
      "name": "argthetatau",
      "parameter_type": "External",
      "value": "0",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 21,
      "description": "Heavy-nu-tau mixing argument in degrees"
    },
    {
      "name": "MN4",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YUKAWA",
      "order_block": 22,
      "description": "Heavy neutrino mass parameter"
    },
    {
      "name": "thetae",
      "parameter_type": "Internal",
      "value": "modthetae*Exp[I*Pi/180*argthetae]",
      "complex": true,
      "description": "Heavy-active electron mixing"
    },
    {
      "name": "thetamu",
      "parameter_type": "Internal",
      "value": "modthetamu*Exp[I*Pi/180*argthetamu]",
      "complex": true,
      "description": "Heavy-active muon mixing"
    },
    {
      "name": "thetatau",
      "parameter_type": "Internal",
      "value": "modthetatau*Exp[I*Pi/180*argthetatau]",
      "complex": true,
      "description": "Heavy-active tau mixing"
    },
    {
      "name": "MassN4",
      "parameter_type": "Internal",
      "value": "MN4",
      "complex": false,
      "description": "Heavy neutrino physical mass"
    },
    {
      "name": "thetatot",
      "parameter_type": "Internal",
      "value": "Sqrt[thetae*Conjugate[thetae]+thetamu*Conjugate[thetamu]+thetatau*Conjugate[thetatau]]",
      "complex": false,
      "description": "Total heavy-active mixing"
    },
    {
      "name": "thetas",
      "parameter_type": "Internal",
      "value": "thetae+thetamu+thetatau",
      "complex": true,
      "description": "Heavy-active mixing sum"
    },
    {
      "name": "r",
      "parameter_type": "Internal",
      "value": "1/Sqrt[1+thetatot^2]",
      "complex": false,
      "description": "Mixing normalization for the Dirac 3+1 case"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Heavynus"
      ],
      "value_rules": [
        {
          "lhs": "yN[1,1]",
          "rhs": "Sqrt[2] Conjugate[thetae] MN4/vev"
        },
        {
          "lhs": "yN[2,1]",
          "rhs": "Sqrt[2] Conjugate[thetamu] MN4/vev"
        },
        {
          "lhs": "yN[3,1]",
          "rhs": "Sqrt[2] Conjugate[thetatau] MN4/vev"
        }
      ],
      "interaction_order": [
        "QED",
        1
      ],
      "description": "Heavy neutrino Yukawa couplings"
    },
    {
      "name": "numass",
      "parameter_type": "Internal",
      "complex": false,
      "indices": [
        "Neutrinos",
        "Neutrinos"
      ],
      "value_rules": [
        {
          "lhs": "numass[4,4]",
          "rhs": "MN4",
          "delayed": true
        },
        {
          "lhs": "numass[ii_,jj_]",
          "rhs": "0",
          "delayed": true
        }
      ],
      "description": "Neutrino mass matrix in mass basis"
    },
    {
      "name": "fK",
      "parameter_type": "External",
      "value": "0.1556",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 2,
      "description": "Kaon decay constant"
    },
    {
      "name": "fpi",
      "parameter_type": "External",
      "value": "0.1302",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 3,
      "description": "Pion decay constant"
    },
    {
      "name": "feta",
      "parameter_type": "External",
      "value": "0.08159",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 4,
      "description": "Eta effective decay constant"
    },
    {
      "name": "fetap",
      "parameter_type": "External",
      "value": "-0.0946",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 5,
      "description": "Eta prime effective decay constant"
    },
    {
      "name": "fD",
      "parameter_type": "External",
      "value": "0.212",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 6,
      "description": "D decay constant"
    },
    {
      "name": "frho",
      "parameter_type": "External",
      "value": "0.17",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 7,
      "description": "rho decay constant"
    },
    {
      "name": "fDs",
      "parameter_type": "External",
      "value": "0.249",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 8,
      "description": "Ds decay constant"
    },
    {
      "name": "fomega",
      "parameter_type": "External",
      "value": "0.155",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 9,
      "description": "omega decay constant"
    },
    {
      "name": "fphi",
      "parameter_type": "External",
      "value": "0.232",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 10,
      "description": "phi decay constant"
    },
    {
      "name": "fB",
      "parameter_type": "External",
      "value": "0.190",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 11,
      "description": "B decay constant"
    },
    {
      "name": "fBs",
      "parameter_type": "External",
      "value": "0.230",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 12,
      "description": "Bs decay constant"
    },
    {
      "name": "fBc",
      "parameter_type": "External",
      "value": "0.190",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 13,
      "description": "Bc decay constant"
    },
    {
      "name": "fKstar",
      "parameter_type": "External",
      "value": "0.177",
      "complex": false,
      "block_name": "MESONBLOCK",
      "order_block": 34,
      "description": "Kstar decay constant"
    },
    {
      "name": "PMNS",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Neutrinos"
      ],
      "value_rules": [
        {
          "lhs": "PMNS[1,4]",
          "rhs": "If[thetae == 0 && thetamu == 0 && thetatau == 0, 0, thetae/r]"
        },
        {
          "lhs": "PMNS[2,4]",
          "rhs": "If[thetae == 0 && thetamu == 0 && thetatau == 0, 0, thetamu/r]"
        },
        {
          "lhs": "PMNS[3,4]",
          "rhs": "If[thetae == 0 && thetamu == 0 && thetatau == 0, 0, thetatau/r]"
        }
      ],
      "description": "Active-heavy leptonic mixing matrix"
    },
    {
      "name": "HEAV",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Heavynus",
        "Neutrinos"
      ],
      "value_rules": [
        {
          "lhs": "HEAV[1,1]",
          "rhs": "-Conjugate[thetae]/r"
        },
        {
          "lhs": "HEAV[1,2]",
          "rhs": "-Conjugate[thetamu]/r"
        },
        {
          "lhs": "HEAV[1,3]",
          "rhs": "-Conjugate[thetatau]/r"
        },
        {
          "lhs": "HEAV[1,4]",
          "rhs": "1/r"
        }
      ],
      "description": "Sterile-heavy mixing matrix for the Dirac scenario"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 1,
      "class_name": "vl",
      "self_conjugate": false,
      "indices": [
        "Neutrinos"
      ],
      "flavor_index": "Neutrinos",
      "class_members": [
        "v1",
        "v2",
        "v3",
        "N4"
      ],
      "mass": {
        "sym": "Mnu",
        "members": [
          [
            "v1",
            "0"
          ],
          [
            "v2",
            "0"
          ],
          [
            "v3",
            "0"
          ],
          [
            "N4",
            "Internal"
          ]
        ]
      },
      "width": {
        "sym": "Wnu",
        "members": [
          [
            "v1",
            "0"
          ],
          [
            "v2",
            "0"
          ],
          [
            "v3",
            "0"
          ],
          [
            "N4",
            "0"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "LeptonNumber": "1"
      },
      "pdg": [
        12000,
        14000,
        16000,
        18000
      ],
      "particle_name": [
        "v1",
        "v2",
        "v3",
        "N4"
      ],
      "antiparticle_name": [
        "v1~",
        "v2~",
        "v3~",
        "N4~"
      ],
      "full_name": [
        "neutrino1",
        "neutrino2",
        "neutrino3",
        "Heavy-neutrino"
      ],
      "propagator_label": [
        "v",
        "v1",
        "v2",
        "v3",
        "N4"
      ],
      "propagator_type": "S",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 16,
      "class_name": "NR",
      "self_conjugate": false,
      "indices": [
        "Heavynus"
      ],
      "flavor_index": "Heavynus",
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "unphysical": true,
      "definitions": [
        "NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAVR[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 17,
      "class_name": "NL",
      "self_conjugate": false,
      "indices": [
        "Heavynus"
      ],
      "flavor_index": "Heavynus",
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "unphysical": true,
      "definitions": [
        "NL[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "K",
      "self_conjugate": false,
      "mass": {
        "sym": "MK",
        "value": "0.493677"
      },
      "width": {
        "sym": "WK",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 321,
      "particle_name": "K+",
      "antiparticle_name": "K-",
      "full_name": "Charged Kaon",
      "propagator_label": "K",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "Pip",
      "self_conjugate": false,
      "mass": {
        "sym": "MPip",
        "value": "0.13957"
      },
      "width": {
        "sym": "WPip",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 211,
      "particle_name": "Pi+",
      "antiparticle_name": "Pi-",
      "full_name": "Charged Pion",
      "propagator_label": "Pi",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 6,
      "class_name": "Dd",
      "self_conjugate": false,
      "mass": {
        "sym": "MDd",
        "value": "1.869"
      },
      "width": {
        "sym": "WD",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 411,
      "particle_name": "D+",
      "antiparticle_name": "D-",
      "full_name": "Charged D",
      "propagator_label": "Dd",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 7,
      "class_name": "Pi0",
      "self_conjugate": true,
      "mass": {
        "sym": "MPi0",
        "value": "0.13498"
      },
      "width": {
        "sym": "WPi0",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 111,
      "particle_name": "Pi0",
      "full_name": "Neutral Pion",
      "propagator_label": "Pi0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 8,
      "class_name": "Eta",
      "self_conjugate": true,
      "mass": {
        "sym": "Meta",
        "value": "0.54786"
      },
      "width": {
        "sym": "Weta",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 221,
      "particle_name": "Eta",
      "full_name": "Eta",
      "propagator_label": "eta",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 9,
      "class_name": "Etap",
      "self_conjugate": true,
      "mass": {
        "sym": "Metap",
        "value": "0.9578"
      },
      "width": {
        "sym": "Wetap",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 331,
      "particle_name": "Etap",
      "full_name": "Eta Prime",
      "propagator_label": "etap",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 10,
      "class_name": "Ds",
      "self_conjugate": false,
      "mass": {
        "sym": "MDs",
        "value": "1.9683"
      },
      "width": {
        "sym": "WDs",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 431,
      "particle_name": "Ds+",
      "antiparticle_name": "Ds-",
      "full_name": "Charged Ds",
      "propagator_label": "Ds",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "K0",
      "self_conjugate": false,
      "mass": {
        "sym": "MK0",
        "value": "0.497611"
      },
      "width": {
        "sym": "WK0",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 311,
      "particle_name": "K0",
      "antiparticle_name": "K0bar",
      "full_name": "Neutral Kaon",
      "propagator_label": "K0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 13,
      "class_name": "D0",
      "self_conjugate": false,
      "mass": {
        "sym": "MD0",
        "value": "1.865"
      },
      "width": {
        "sym": "WD0",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 421,
      "particle_name": "D0",
      "antiparticle_name": "D0bar",
      "full_name": "Neutral D",
      "propagator_label": "D0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 15,
      "class_name": "Bu",
      "self_conjugate": false,
      "mass": {
        "sym": "MBu",
        "value": "5.279"
      },
      "width": {
        "sym": "WBu",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 521,
      "particle_name": "B+",
      "antiparticle_name": "B-",
      "full_name": "Charged B",
      "propagator_label": "Bu",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 16,
      "class_name": "Bc",
      "self_conjugate": false,
      "mass": {
        "sym": "MBc",
        "value": "6.275"
      },
      "width": {
        "sym": "WBc",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 541,
      "particle_name": "Bc+",
      "antiparticle_name": "Bc-",
      "full_name": "Charged Bc",
      "propagator_label": "Bc",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 17,
      "class_name": "B0",
      "self_conjugate": false,
      "mass": {
        "sym": "MB0",
        "value": "5.280"
      },
      "width": {
        "sym": "WB0",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 511,
      "particle_name": "B0",
      "antiparticle_name": "B0bar",
      "full_name": "Neutral B",
      "propagator_label": "B0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 18,
      "class_name": "B0s",
      "self_conjugate": false,
      "mass": {
        "sym": "MB0s",
        "value": "5.367"
      },
      "width": {
        "sym": "WB0s",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 531,
      "particle_name": "B0s",
      "antiparticle_name": "B0sbar",
      "full_name": "Neutral Bs",
      "propagator_label": "B0s",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 21,
      "class_name": "rho0",
      "self_conjugate": true,
      "mass": {
        "sym": "Mrho0",
        "value": "0.77526"
      },
      "width": {
        "sym": "Wrho0",
        "value": "0.1478"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 113,
      "particle_name": "rho0",
      "full_name": "rho 0",
      "propagator_label": "rho0",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 22,
      "class_name": "rho",
      "self_conjugate": false,
      "mass": {
        "sym": "Mrho",
        "value": "0.77511"
      },
      "width": {
        "sym": "Wrho",
        "value": "0.1491"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 213,
      "particle_name": "rho+",
      "antiparticle_name": "rho-",
      "full_name": "charged rho",
      "propagator_label": "rho",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 23,
      "class_name": "omega",
      "self_conjugate": true,
      "mass": {
        "sym": "Mom",
        "value": "0.78265"
      },
      "width": {
        "sym": "Wom",
        "value": "0.00849"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 223,
      "particle_name": "omega",
      "full_name": "Omega",
      "propagator_label": "omega",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 24,
      "class_name": "Kstar",
      "self_conjugate": false,
      "mass": {
        "sym": "MKstar",
        "value": "0.8917"
      },
      "width": {
        "sym": "WKstar",
        "value": "0.0508"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 323,
      "particle_name": "Kstar+",
      "antiparticle_name": "Kstar-",
      "full_name": "Charged Kstar",
      "propagator_label": "Kstar",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 25,
      "class_name": "phimeson",
      "self_conjugate": true,
      "mass": {
        "sym": "Mphi",
        "value": "1.019461"
      },
      "width": {
        "sym": "Wphi",
        "value": "0.004249"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 333,
      "particle_name": "phimeson",
      "full_name": "phi meson",
      "propagator_label": "phi",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 26,
      "class_name": "Bstar",
      "self_conjugate": false,
      "mass": {
        "sym": "MBstar",
        "value": "5.3247"
      },
      "width": {
        "sym": "WBstar",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "1",
        "Y": "0"
      },
      "pdg": 523,
      "particle_name": "Bstar+",
      "antiparticle_name": "Bstar-",
      "full_name": "Charged Bstar",
      "propagator_label": "Bstar",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LHeavyNMajoranaMass",
      "expression": "Block[{sp,ii,jj,ff1,ff2}, -Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}] - MN4/2 Sum[NRcbar[sp,ff1].NR[sp,ff1],{ff1,1,1}] + HC[-Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}]]]",
      "delayed": true
    },
    {
      "name": "LHeavyNDiracMass",
      "expression": "Block[{sp,ii,jj,ff1,ff2}, -Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}] - MN4 Sum[NLbar[sp,ff1].NR[sp,ff1],{ff1,1,1}] + HC[-Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}] - MN4 Sum[NLbar[sp,ff1].NR[sp,ff1],{ff1,1,1}]]]",
      "delayed": true
    },
    {
      "name": "LHeavyNEW",
      "expression": "Block[{mu,ii,jj,aa}, gw/Sqrt[2] W[mu] Sum[Conjugate[PMNS[aa,ii]] vlbar[jj,ii].Ga[mu,jj,kk].ProjM[kk,ll].l[ll,aa],{aa,1,3},{ii,1,4}] + gw/(4*cw) Z[mu] Sum[Sum[Conjugate[PMNS[aa,ii]] PMNS[aa,jj],{aa,1,3}] vlbar[sp,ii].Ga[mu,sp,sp2].ProjM[sp2,sp3].vl[sp3,jj],{ii,1,4},{jj,1,4}] + HC[gw/Sqrt[2] W[mu] Sum[Conjugate[PMNS[aa,ii]] vlbar[jj,ii].Ga[mu,jj,kk].ProjM[kk,ll].l[ll,aa],{aa,1,3},{ii,1,4}]]]",
      "delayed": true
    },
    {
      "name": "LHadrPseudoscalarCharged",
      "expression": "Block[{ii,jj,ff1,ff2}, Sum[I*Sqrt[2]*Gf*fpi*CKM[1,1] Pipbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fpi*CKM[1,1] Pipbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}] + Sum[I*Sqrt[2]*Gf*fK*CKM[1,2] Kbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fK*CKM[1,2] Kbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}] + Sum[I*Sqrt[2]*Gf*fD*CKM[2,1] Ddbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fD*CKM[2,1] Ddbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}] + Sum[I*Sqrt[2]*Gf*fDs*CKM[2,2] Dsbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fDs*CKM[2,2] Dsbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}]]",
      "delayed": true
    },
    {
      "name": "LHadrPseudoscalarNeutral",
      "expression": "Block[{ii,jj,ff1,ff2,ff3}, Sum[-I/2*Gf*fpi Pi0 Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff2,ff2] vlbar[ii,ff1].ProjP[ii,jj].vl[jj,ff2] + I/2*Gf*fpi Pi0 Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff1,ff1] vlbar[ii,ff1].ProjM[ii,jj].vl[jj,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] + Sum[-I/2*Gf*feta Eta Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff2,ff2] vlbar[ii,ff1].ProjP[ii,jj].vl[jj,ff2] + I/2*Gf*feta Eta Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff1,ff1] vlbar[ii,ff1].ProjM[ii,jj].vl[jj,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] + Sum[-I/2*Gf*fetap Etap Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff2,ff2] vlbar[ii,ff1].ProjP[ii,jj].vl[jj,ff2] + I/2*Gf*fetap Etap Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff1,ff1] vlbar[ii,ff1].ProjM[ii,jj].vl[jj,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}]]",
      "delayed": true
    },
    {
      "name": "LHadrVectorNeutral",
      "expression": "Block[{mu,ii,jj,kk,ff1,ff2,ff3}, -1/8 FS[rho0,mu,nu] FS[rho0,mu,nu] + Mrho0^2/4 rho0[mu] rho0[mu] - Sum[1/2*Gf*frho*(1-2*sw^2) rho0[mu] Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] vlbar[ii,ff1].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] -1/8 FS[omega,mu,nu] FS[omega,mu,nu] + Mom^2/4 omega[mu] omega[mu] + Sum[1/2*Gf*fomega*(2/3*sw^2) omega[mu] Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] vlbar[ii,ff1].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] -1/8 FS[phimeson,mu,nu] FS[phimeson,mu,nu] + Mphi^2/4 phimeson[mu] phimeson[mu] + Sum[1/2*Sqrt[2]*Gf*fphi*(1/2 - 2/3*sw^2) phimeson[mu] Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] vlbar[ii,ff1].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}]]",
      "delayed": true
    },
    {
      "name": "LHadrVectorCharged",
      "expression": "Block[{mu,ii,jj,kk,ff1,ff2}, -1/4 FS[rhobar,mu,nu] FS[rho,mu,nu] + Mrho^2/2 rhobar[mu] rho[mu] - Sum[Sqrt[2]*Gf*frho*CKM[1,1] PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1] rhobar[mu],{ff1,1,4},{ff2,1,3}] -1/4 FS[Kstarbar,mu,nu] FS[Kstar,mu,nu] + MKstar^2/2 Kstarbar[mu] Kstar[mu] - Sum[Sqrt[2]*Gf*fKstar*CKM[1,2] PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1] Kstarbar[mu],{ff1,1,4},{ff2,1,3}]]",
      "delayed": true
    },
    {
      "name": "LHadrSemileptonic",
      "expression": "Block[{mu,ii,jj,kk,ff1,ff2}, -Sum[2*Sqrt[2]*Gf*CKM[1,2]*fplusK0Pi[ff1,ff2]*I del[Pipbar,mu] K0bar PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1],{ff1,1,4},{ff2,1,2}] + Sum[Sqrt[2]*Gf*CKM[1,2]*(fplusK0Pi[ff1,ff2]-fminusK0Pi[ff1,ff2])*vev/Sqrt[2] Pipbar K0bar PMNS[ff2,ff1] yl[ff2,ff2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[Sqrt[2]*Gf*CKM[1,2]*(fplusK0Pi[ff1,ff2]-fminusK0Pi[ff1,ff2]) Pipbar K0bar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[2*Gf*CKM[1,2]*fplusKPi0[ff1,ff2]*I del[Pi0,mu] Kbar PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1],{ff1,1,4},{ff2,1,2}] + Sum[Gf*CKM[1,2]*(fplusKPi0[ff1,ff2]-fminusKPi0[ff1,ff2])*vev/Sqrt[2] Pi0 Kbar PMNS[ff2,ff1] yl[ff2,ff2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[Gf*CKM[1,2]*(fplusKPi0[ff1,ff2]-fminusKPi0[ff1,ff2]) Pi0 Kbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[2*Sqrt[2]*Gf*CKM[2,2]*fplusDK[ff1,ff2]*I del[Kbar,mu] D0bar PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1],{ff1,1,4},{ff2,1,2}] + Sum[Sqrt[2]*Gf*CKM[2,2]*(fplusDK[ff1,ff2]-fminusDK[ff1,ff2])*vev/Sqrt[2] Kbar D0bar PMNS[ff2,ff1] yl[ff2,ff2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[Sqrt[2]*Gf*CKM[2,2]*(fplusDK[ff1,ff2]-fminusDK[ff1,ff2]) Kbar D0bar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}]]",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "Mesons = True;",
    "FR$LoopSwitches = {{Gf, MW}};",
    "FR$RmDblExt = {ymb -> MB, ymc -> MC, ymdo -> MD, yme -> Me, ymm -> MMU, yms -> MS, ymt -> MT, ymtau -> MTA, ymup -> MU, MN4 -> MassN4};"
  ],
  "raw_blocks": [
    "LagHeavyN := LGauge + LFermions + LHiggs + LYukawa + LGhost + If[Mesons,LHadr,LQuarks];",
    "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r]."
  ]
}
```