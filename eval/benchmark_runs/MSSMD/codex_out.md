```json
{
  "model_name": "MSSMD_gen",
  "info": {
    "authors": [
      "Wei Shi",
      "CMS Collaboration"
    ],
    "version": "1",
    "date": "03.21.2018",
    "institutions": [
      "Rice University",
      "CERN"
    ],
    "emails": [
      "weishi@rice.edu"
    ]
  },
  "interaction_order_hierarchy": [
    [
      "QCD",
      1
    ],
    [
      "NP",
      2
    ],
    [
      "QED",
      2
    ]
  ],
  "interaction_order_limit": [
    [
      "NP",
      4
    ]
  ],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "NEU",
      "range_kind": "Range",
      "size": 4,
      "style_symbol": "i"
    },
    {
      "name": "CHA",
      "range_kind": "Range",
      "size": 2,
      "style_symbol": "i"
    },
    {
      "name": "SCA",
      "range_kind": "Range",
      "size": 6,
      "style_symbol": "i"
    }
  ],
  "parameters": [
    {
      "name": "gd",
      "parameter_type": "External",
      "value": "0.001",
      "complex": false,
      "block_name": "DARK",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "Subscript[g,d]",
      "description": "U1D coupling"
    },
    {
      "name": "MAD",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 3000022,
      "description": "Dark photon mass; benchmark scan 0.25 to 8.5 GeV"
    },
    {
      "name": "WAD",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 3000022,
      "description": "Dark photon width"
    },
    {
      "name": "MneuD",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 3000001,
      "description": "Dark neutralino mass"
    },
    {
      "name": "WneuD",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 3000001,
      "description": "Dark neutralino width"
    },
    {
      "name": "Mneu1",
      "parameter_type": "External",
      "value": "10.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000022,
      "description": "Lightest neutralino mass"
    },
    {
      "name": "Mneu2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000023,
      "description": "Second neutralino mass"
    },
    {
      "name": "Mneu3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000025,
      "description": "Third neutralino mass"
    },
    {
      "name": "Mneu4",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000035,
      "description": "Fourth neutralino mass"
    },
    {
      "name": "Wneu1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000022,
      "description": "Lightest neutralino width"
    },
    {
      "name": "Wneu2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000023,
      "description": "Second neutralino width"
    },
    {
      "name": "Wneu3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000025,
      "description": "Third neutralino width"
    },
    {
      "name": "Wneu4",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000035,
      "description": "Fourth neutralino width"
    },
    {
      "name": "Mch1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000024,
      "description": "Light chargino mass"
    },
    {
      "name": "Mch2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000037,
      "description": "Heavy chargino mass"
    },
    {
      "name": "Wch1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000024,
      "description": "Light chargino width"
    },
    {
      "name": "Wch2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000037,
      "description": "Heavy chargino width"
    },
    {
      "name": "Mgo",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000021,
      "description": "Gluino mass"
    },
    {
      "name": "Wgo",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000021,
      "description": "Gluino width"
    },
    {
      "name": "MH01",
      "parameter_type": "External",
      "value": "125.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 25,
      "description": "Light CP-even Higgs mass"
    },
    {
      "name": "WH01",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 25,
      "description": "Light CP-even Higgs width"
    },
    {
      "name": "MH02",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 35,
      "description": "Heavy CP-even Higgs mass"
    },
    {
      "name": "WH02",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 35,
      "description": "Heavy CP-even Higgs width"
    },
    {
      "name": "MA0",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 36,
      "description": "CP-odd Higgs mass"
    },
    {
      "name": "WA0",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 36,
      "description": "CP-odd Higgs width"
    },
    {
      "name": "MH",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 37,
      "description": "Charged Higgs mass"
    },
    {
      "name": "WH",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 37,
      "description": "Charged Higgs width"
    },
    {
      "name": "Msn1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000012,
      "description": "Sneutrino 1 mass"
    },
    {
      "name": "Msn2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000014,
      "description": "Sneutrino 2 mass"
    },
    {
      "name": "Msn3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000016,
      "description": "Sneutrino 3 mass"
    },
    {
      "name": "Wsn1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000012,
      "description": "Sneutrino 1 width"
    },
    {
      "name": "Wsn2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000014,
      "description": "Sneutrino 2 width"
    },
    {
      "name": "Wsn3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 1000016,
      "description": "Sneutrino 3 width"
    },
    {
      "name": "Msl1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000011,
      "description": "Charged slepton 1 mass"
    },
    {
      "name": "Msl2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000013,
      "description": "Charged slepton 2 mass"
    },
    {
      "name": "Msl3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000015,
      "description": "Charged slepton 3 mass"
    },
    {
      "name": "Msl4",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000011,
      "description": "Charged slepton 4 mass"
    },
    {
      "name": "Msl5",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000013,
      "description": "Charged slepton 5 mass"
    },
    {
      "name": "Msl6",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000015,
      "description": "Charged slepton 6 mass"
    },
    {
      "name": "Msu1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000002,
      "description": "Up squark 1 mass"
    },
    {
      "name": "Msu2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000004,
      "description": "Up squark 2 mass"
    },
    {
      "name": "Msu3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000006,
      "description": "Up squark 3 mass"
    },
    {
      "name": "Msu4",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000002,
      "description": "Up squark 4 mass"
    },
    {
      "name": "Msu5",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000004,
      "description": "Up squark 5 mass"
    },
    {
      "name": "Msu6",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000006,
      "description": "Up squark 6 mass"
    },
    {
      "name": "Msd1",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000001,
      "description": "Down squark 1 mass"
    },
    {
      "name": "Msd2",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000003,
      "description": "Down squark 2 mass"
    },
    {
      "name": "Msd3",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 1000005,
      "description": "Down squark 3 mass"
    },
    {
      "name": "Msd4",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000001,
      "description": "Down squark 4 mass"
    },
    {
      "name": "Msd5",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000003,
      "description": "Down squark 5 mass"
    },
    {
      "name": "Msd6",
      "parameter_type": "External",
      "complex": false,
      "block_name": "MASS",
      "order_block": 2000005,
      "description": "Down squark 6 mass"
    },
    {
      "name": "RNN",
      "parameter_type": "External",
      "complex": false,
      "block_name": "NMIX",
      "indices": [
        "NEU",
        "NEU"
      ],
      "description": "Neutralino mixing matrix real part"
    },
    {
      "name": "INN",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMNMIX",
      "indices": [
        "NEU",
        "NEU"
      ],
      "description": "Neutralino mixing matrix imaginary part"
    },
    {
      "name": "RUU",
      "parameter_type": "External",
      "complex": false,
      "block_name": "UMIX",
      "indices": [
        "CHA",
        "CHA"
      ],
      "description": "Chargino U mixing matrix real part"
    },
    {
      "name": "IUU",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMUMIX",
      "indices": [
        "CHA",
        "CHA"
      ],
      "description": "Chargino U mixing matrix imaginary part"
    },
    {
      "name": "RVV",
      "parameter_type": "External",
      "complex": false,
      "block_name": "VMIX",
      "indices": [
        "CHA",
        "CHA"
      ],
      "description": "Chargino V mixing matrix real part"
    },
    {
      "name": "IVV",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMVMIX",
      "indices": [
        "CHA",
        "CHA"
      ],
      "description": "Chargino V mixing matrix imaginary part"
    },
    {
      "name": "RRn",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SNUMIX",
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Sneutrino mixing matrix real part"
    },
    {
      "name": "IRn",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMSNUMIX",
      "indices": [
        "Generation",
        "Generation"
      ],
      "description": "Sneutrino mixing matrix imaginary part"
    },
    {
      "name": "RRl",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SELMIX",
      "indices": [
        "SCA",
        "SCA"
      ],
      "description": "Slepton mixing matrix real part"
    },
    {
      "name": "IRl",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMSELMIX",
      "indices": [
        "SCA",
        "SCA"
      ],
      "description": "Slepton mixing matrix imaginary part"
    },
    {
      "name": "RRu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "USQMIX",
      "indices": [
        "SCA",
        "SCA"
      ],
      "description": "Up squark mixing matrix real part"
    },
    {
      "name": "IRu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMUSQMIX",
      "indices": [
        "SCA",
        "SCA"
      ],
      "description": "Up squark mixing matrix imaginary part"
    },
    {
      "name": "RRd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "DSQMIX",
      "indices": [
        "SCA",
        "SCA"
      ],
      "description": "Down squark mixing matrix real part"
    },
    {
      "name": "IRd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "IMDSQMIX",
      "indices": [
        "SCA",
        "SCA"
      ],
      "description": "Down squark mixing matrix imaginary part"
    },
    {
      "name": "alp",
      "parameter_type": "External",
      "complex": false,
      "block_name": "FRALPHA",
      "tex": "\\[Alpha]",
      "description": "Neutral Higgs mixing angle"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "AD",
      "self_conjugate": true,
      "mass": {
        "sym": "MAD"
      },
      "width": {
        "sym": "WAD"
      },
      "quantum_numbers": {
        "Q": "0",
        "X": "0"
      },
      "pdg": 3000022,
      "particle_name": "ad",
      "full_name": "dark photon",
      "propagator_label": "AD",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "neu",
      "self_conjugate": true,
      "indices": [
        "NEU"
      ],
      "flavor_index": "NEU",
      "class_members": [
        "neu1",
        "neu2",
        "neu3",
        "neu4"
      ],
      "mass": {
        "sym": "Mneu",
        "members": [
          [
            "Mneu1",
            "10."
          ],
          [
            "Mneu2",
            null
          ],
          [
            "Mneu3",
            null
          ],
          [
            "Mneu4",
            null
          ]
        ]
      },
      "width": {
        "sym": "Wneu",
        "members": [
          [
            "Wneu1",
            null
          ],
          [
            "Wneu2",
            null
          ],
          [
            "Wneu3",
            null
          ],
          [
            "Wneu4",
            null
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": [
        1000022,
        1000023,
        1000025,
        1000035
      ],
      "particle_name": [
        "n1",
        "n2",
        "n3",
        "n4"
      ],
      "full_name": [
        "neutralino 1",
        "neutralino 2",
        "neutralino 3",
        "neutralino 4"
      ],
      "propagator_label": [
        "neu",
        "neu1",
        "neu2",
        "neu3",
        "neu4"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "ch",
      "self_conjugate": false,
      "indices": [
        "CHA"
      ],
      "flavor_index": "CHA",
      "class_members": [
        "ch1",
        "ch2"
      ],
      "mass": {
        "sym": "Mch",
        "members": [
          [
            "Mch1",
            null
          ],
          [
            "Mch2",
            null
          ]
        ]
      },
      "width": {
        "sym": "Wch",
        "members": [
          [
            "Wch1",
            null
          ],
          [
            "Wch2",
            null
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": [
        1000024,
        1000037
      ],
      "particle_name": [
        "x1+",
        "x2+"
      ],
      "antiparticle_name": [
        "x1-",
        "x2-"
      ],
      "full_name": [
        "chargino 1",
        "chargino 2"
      ],
      "propagator_label": [
        "ch",
        "ch1",
        "ch2"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 103,
      "class_name": "go",
      "self_conjugate": true,
      "indices": [
        "Gluon"
      ],
      "mass": {
        "sym": "Mgo"
      },
      "width": {
        "sym": "Wgo"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 1000021,
      "particle_name": "go",
      "full_name": "gluino",
      "propagator_label": "go",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 104,
      "class_name": "neuD",
      "self_conjugate": true,
      "mass": {
        "sym": "MneuD",
        "value": "1."
      },
      "width": {
        "sym": "WneuD",
        "value": "0."
      },
      "quantum_numbers": {
        "Q": "0",
        "X": "0"
      },
      "pdg": 3000001,
      "particle_name": "nD",
      "full_name": "dark neutralino",
      "propagator_label": "neuD",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 201,
      "class_name": "h0",
      "self_conjugate": true,
      "mass": {
        "sym": "MH01",
        "value": "125."
      },
      "width": {
        "sym": "WH01"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 25,
      "particle_name": "h",
      "full_name": "light CP-even Higgs",
      "propagator_label": "h0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 202,
      "class_name": "H0",
      "self_conjugate": true,
      "mass": {
        "sym": "MH02"
      },
      "width": {
        "sym": "WH02"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 35,
      "particle_name": "h02",
      "full_name": "heavy CP-even Higgs",
      "propagator_label": "H0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 203,
      "class_name": "A0",
      "self_conjugate": true,
      "mass": {
        "sym": "MA0"
      },
      "width": {
        "sym": "WA0"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 36,
      "particle_name": "A0",
      "full_name": "CP-odd Higgs",
      "propagator_label": "A0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 204,
      "class_name": "H",
      "self_conjugate": false,
      "mass": {
        "sym": "MH"
      },
      "width": {
        "sym": "WH"
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": 37,
      "particle_name": "H+",
      "antiparticle_name": "H-",
      "full_name": "charged Higgs",
      "propagator_label": "H",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 205,
      "class_name": "sn",
      "self_conjugate": false,
      "indices": [
        "Generation"
      ],
      "flavor_index": "Generation",
      "class_members": [
        "sn1",
        "sn2",
        "sn3"
      ],
      "mass": {
        "sym": "Msn",
        "members": [
          [
            "Msn1",
            null
          ],
          [
            "Msn2",
            null
          ],
          [
            "Msn3",
            null
          ]
        ]
      },
      "width": {
        "sym": "Wsn",
        "members": [
          [
            "Wsn1",
            null
          ],
          [
            "Wsn2",
            null
          ],
          [
            "Wsn3",
            null
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": [
        1000012,
        1000014,
        1000016
      ],
      "particle_name": [
        "sv1",
        "sv2",
        "sv3"
      ],
      "antiparticle_name": [
        "sv1~",
        "sv2~",
        "sv3~"
      ],
      "full_name": [
        "sneutrino 1",
        "sneutrino 2",
        "sneutrino 3"
      ],
      "propagator_label": [
        "sn",
        "sn1",
        "sn2",
        "sn3"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 206,
      "class_name": "sl",
      "self_conjugate": false,
      "indices": [
        "SCA"
      ],
      "flavor_index": "SCA",
      "class_members": [
        "sl1",
        "sl2",
        "sl3",
        "sl4",
        "sl5",
        "sl6"
      ],
      "mass": {
        "sym": "Msl",
        "members": [
          [
            "Msl1",
            null
          ],
          [
            "Msl2",
            null
          ],
          [
            "Msl3",
            null
          ],
          [
            "Msl4",
            null
          ],
          [
            "Msl5",
            null
          ],
          [
            "Msl6",
            null
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "-1"
      },
      "pdg": [
        1000011,
        1000013,
        1000015,
        2000011,
        2000013,
        2000015
      ],
      "particle_name": [
        "sl1-",
        "sl2-",
        "sl3-",
        "sl4-",
        "sl5-",
        "sl6-"
      ],
      "antiparticle_name": [
        "sl1+",
        "sl2+",
        "sl3+",
        "sl4+",
        "sl5+",
        "sl6+"
      ],
      "full_name": [
        "charged slepton 1",
        "charged slepton 2",
        "charged slepton 3",
        "charged slepton 4",
        "charged slepton 5",
        "charged slepton 6"
      ],
      "propagator_label": [
        "sl",
        "sl1",
        "sl2",
        "sl3",
        "sl4",
        "sl5",
        "sl6"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 207,
      "class_name": "su",
      "self_conjugate": false,
      "indices": [
        "SCA",
        "Colour"
      ],
      "flavor_index": "SCA",
      "class_members": [
        "su1",
        "su2",
        "su3",
        "su4",
        "su5",
        "su6"
      ],
      "mass": {
        "sym": "Msu",
        "members": [
          [
            "Msu1",
            null
          ],
          [
            "Msu2",
            null
          ],
          [
            "Msu3",
            null
          ],
          [
            "Msu4",
            null
          ],
          [
            "Msu5",
            null
          ],
          [
            "Msu6",
            null
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "2/3"
      },
      "pdg": [
        1000002,
        1000004,
        1000006,
        2000002,
        2000004,
        2000006
      ],
      "particle_name": [
        "su1",
        "su2",
        "su3",
        "su4",
        "su5",
        "su6"
      ],
      "antiparticle_name": [
        "su1~",
        "su2~",
        "su3~",
        "su4~",
        "su5~",
        "su6~"
      ],
      "full_name": [
        "up squark 1",
        "up squark 2",
        "up squark 3",
        "up squark 4",
        "up squark 5",
        "up squark 6"
      ],
      "propagator_label": [
        "su",
        "su1",
        "su2",
        "su3",
        "su4",
        "su5",
        "su6"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 208,
      "class_name": "sd",
      "self_conjugate": false,
      "indices": [
        "SCA",
        "Colour"
      ],
      "flavor_index": "SCA",
      "class_members": [
        "sd1",
        "sd2",
        "sd3",
        "sd4",
        "sd5",
        "sd6"
      ],
      "mass": {
        "sym": "Msd",
        "members": [
          [
            "Msd1",
            null
          ],
          [
            "Msd2",
            null
          ],
          [
            "Msd3",
            null
          ],
          [
            "Msd4",
            null
          ],
          [
            "Msd5",
            null
          ],
          [
            "Msd6",
            null
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "-1/3"
      },
      "pdg": [
        1000001,
        1000003,
        1000005,
        2000001,
        2000003,
        2000005
      ],
      "particle_name": [
        "sd1",
        "sd2",
        "sd3",
        "sd4",
        "sd5",
        "sd6"
      ],
      "antiparticle_name": [
        "sd1~",
        "sd2~",
        "sd3~",
        "sd4~",
        "sd5~",
        "sd6~"
      ],
      "full_name": [
        "down squark 1",
        "down squark 2",
        "down squark 3",
        "down squark 4",
        "down squark 5",
        "down squark 6"
      ],
      "propagator_label": [
        "sd",
        "sd1",
        "sd2",
        "sd3",
        "sd4",
        "sd5",
        "sd6"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LN1NDAD",
      "expression": "I*gd*(neu1bar.Ga[mu].neuD)*AD[mu]",
      "delayed": true
    },
    {
      "name": "LADMuMu",
      "expression": "gd*(mbar.Ga[mu].m)*AD[mu]",
      "delayed": true
    },
    {
      "name": "Lag",
      "expression": "LN1NDAD + LADMuMu",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "$CKMDiag = False;",
    "$MNSDiag = True;",
    "M$InteractionOrderLimit = {{NP, 4}};",
    "M$InteractionOrderHierarchy = {{QCD, 1}, {NP, 2}, {QED, 2}};"
  ],
  "raw_blocks": [
    "(* Dark SUSY benchmark: h -> 2 n1, n1 -> nD + AD, AD -> mu- mu+.  The reference implementation adds the explicit n1-nD-AD and AD-muon vertices to the MSSM Lagrangian. *)"
  ]
}
```