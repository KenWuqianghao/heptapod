```json
{
  "model_name": "331_gen",
  "info": {
    "authors": [
      "Codex extraction from Cao and Zhang, arXiv:1611.09337"
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
      2
    ]
  ],
  "interaction_order_limit": [
    [
      "NP",
      99
    ]
  ],
  "feynman_gauge": false,
  "vevs": [
    [
      "rho[2]",
      "v1/Sqrt[2]"
    ],
    [
      "eta[1]",
      "v2/Sqrt[2]"
    ],
    [
      "chi[3]",
      "v3/Sqrt[2]"
    ]
  ],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "FirstTwoGeneration",
      "range_kind": "NoUnfold",
      "size": 2,
      "style_symbol": "i2"
    },
    {
      "name": "SU3L",
      "range_kind": "NoUnfold",
      "size": 3,
      "style_symbol": "a3"
    }
  ],
  "parameters": [
    {
      "name": "beta331",
      "parameter_type": "External",
      "value": "1/Sqrt[3]",
      "complex": false,
      "block_name": "331INPUTS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "beta331",
      "tex": "\\\\beta",
      "description": "331 embedding parameter beta; benchmark values are +/-Sqrt[3], +/-1/Sqrt[3]"
    },
    {
      "name": "v1",
      "parameter_type": "External",
      "value": "200.",
      "complex": false,
      "block_name": "331INPUTS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "v1",
      "tex": "v_1",
      "description": "rho triplet vacuum expectation value"
    },
    {
      "name": "v2",
      "parameter_type": "Internal",
      "value": "Sqrt[vev^2 - v1^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "v2",
      "tex": "v_2",
      "description": "eta triplet vacuum expectation value, with v1^2+v2^2=vev^2"
    },
    {
      "name": "v3",
      "parameter_type": "External",
      "value": "2000.",
      "complex": false,
      "block_name": "331INPUTS",
      "order_block": 3,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "v3",
      "tex": "v_3",
      "description": "chi triplet vacuum expectation value"
    },
    {
      "name": "f331",
      "parameter_type": "External",
      "value": "2000.",
      "complex": false,
      "block_name": "331INPUTS",
      "order_block": 4,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "f331",
      "tex": "f",
      "description": "dimensionful trilinear scalar potential parameter"
    },
    {
      "name": "k331",
      "parameter_type": "Internal",
      "value": "f331/v3",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "k331",
      "tex": "k",
      "description": "dimensionless ratio f/v3"
    },
    {
      "name": "QY331",
      "parameter_type": "Internal",
      "value": "(Sqrt[3]*beta331 + 1)/2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "QY331",
      "tex": "Q_Y",
      "description": "electric charge of Y boson and H^QY scalar"
    },
    {
      "name": "QV331",
      "parameter_type": "Internal",
      "value": "(Sqrt[3]*beta331 - 1)/2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "QV331",
      "tex": "Q_V",
      "description": "electric charge of V boson and H^QV scalar"
    },
    {
      "name": "QD331",
      "parameter_type": "Internal",
      "value": "1/6 - Sqrt[3]*beta331/2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "QD331",
      "tex": "Q_D",
      "description": "electric charge of D and S exotic quarks"
    },
    {
      "name": "QT331",
      "parameter_type": "Internal",
      "value": "1/6 + Sqrt[3]*beta331/2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "QT331",
      "tex": "Q_T",
      "description": "electric charge of T exotic quark"
    },
    {
      "name": "QE331",
      "parameter_type": "Internal",
      "value": "-1/2 + Sqrt[3]*beta331/2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "QE331",
      "tex": "Q_E",
      "description": "electric charge of heavy leptons"
    },
    {
      "name": "lam1",
      "parameter_type": "External",
      "value": "0.13",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 1,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lam1",
      "tex": "\\\\lambda_1",
      "description": "rho quartic scalar coupling"
    },
    {
      "name": "lam2",
      "parameter_type": "External",
      "value": "0.13",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 2,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lam2",
      "tex": "\\\\lambda_2",
      "description": "eta quartic scalar coupling"
    },
    {
      "name": "lam3",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 3,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lam3",
      "tex": "\\\\lambda_3",
      "description": "chi quartic scalar coupling"
    },
    {
      "name": "lam12",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 4,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lam12",
      "tex": "\\\\lambda_{12}",
      "description": "rho-eta scalar quartic coupling"
    },
    {
      "name": "lam13",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 5,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lam13",
      "tex": "\\\\lambda_{13}",
      "description": "rho-chi scalar quartic coupling"
    },
    {
      "name": "lam23",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 6,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lam23",
      "tex": "\\\\lambda_{23}",
      "description": "eta-chi scalar quartic coupling"
    },
    {
      "name": "lamp12",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 7,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lamp12",
      "tex": "\\\\lambda'_{12}",
      "description": "rho-eta primed quartic scalar coupling"
    },
    {
      "name": "lamp13",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 8,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lamp13",
      "tex": "\\\\lambda'_{13}",
      "description": "rho-chi primed quartic scalar coupling"
    },
    {
      "name": "lamp23",
      "parameter_type": "External",
      "value": "0.10",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 9,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "lamp23",
      "tex": "\\\\lambda'_{23}",
      "description": "eta-chi primed quartic scalar coupling"
    },
    {
      "name": "mu1sq",
      "parameter_type": "External",
      "value": "-10000.",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 10,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "mu1sq",
      "tex": "\\\\mu_1^2",
      "description": "rho scalar potential mass-squared parameter"
    },
    {
      "name": "mu2sq",
      "parameter_type": "External",
      "value": "-10000.",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 11,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "mu2sq",
      "tex": "\\\\mu_2^2",
      "description": "eta scalar potential mass-squared parameter"
    },
    {
      "name": "mu3sq",
      "parameter_type": "External",
      "value": "-1000000.",
      "complex": false,
      "block_name": "331SCALAR",
      "order_block": 12,
      "interaction_order": [
        "NP",
        2
      ],
      "parameter_name": "mu3sq",
      "tex": "\\\\mu_3^2",
      "description": "chi scalar potential mass-squared parameter"
    },
    {
      "name": "s12",
      "parameter_type": "Internal",
      "value": "v2/vev",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "s12",
      "tex": "s_{12}",
      "description": "charged scalar mixing sine in eta-rho sector"
    },
    {
      "name": "c12",
      "parameter_type": "Internal",
      "value": "v1/vev",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "c12",
      "tex": "c_{12}",
      "description": "charged scalar mixing cosine in eta-rho sector"
    },
    {
      "name": "s13",
      "parameter_type": "Internal",
      "value": "v3/Sqrt[v1^2 + v3^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "s13",
      "tex": "s_{13}",
      "description": "charged scalar mixing sine in chi-rho sector"
    },
    {
      "name": "c13",
      "parameter_type": "Internal",
      "value": "v1/Sqrt[v1^2 + v3^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "c13",
      "tex": "c_{13}",
      "description": "charged scalar mixing cosine in chi-rho sector"
    },
    {
      "name": "s23",
      "parameter_type": "Internal",
      "value": "v3/Sqrt[v2^2 + v3^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "s23",
      "tex": "s_{23}",
      "description": "charged scalar mixing sine in chi-eta sector"
    },
    {
      "name": "c23",
      "parameter_type": "Internal",
      "value": "v2/Sqrt[v2^2 + v3^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "c23",
      "tex": "c_{23}",
      "description": "charged scalar mixing cosine in chi-eta sector"
    },
    {
      "name": "a0",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - (1 + beta331^2)*sw^2]",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "a0",
      "tex": "a_0",
      "description": "331 neutral gauge shorthand from Appendix A"
    },
    {
      "name": "ap",
      "parameter_type": "Internal",
      "value": "Sqrt[3]*beta331 + 1",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "ap",
      "tex": "a_+",
      "description": "331 charge shorthand Sqrt[3] beta + 1"
    },
    {
      "name": "am",
      "parameter_type": "Internal",
      "value": "Sqrt[3]*beta331 - 1",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "am",
      "tex": "a_-",
      "description": "331 charge shorthand Sqrt[3] beta - 1"
    },
    {
      "name": "bp",
      "parameter_type": "Internal",
      "value": "Sqrt[3]*beta331 + 2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "bp",
      "tex": "b_+",
      "description": "331 charge shorthand Sqrt[3] beta + 2"
    },
    {
      "name": "bm",
      "parameter_type": "Internal",
      "value": "Sqrt[3]*beta331 - 2",
      "complex": false,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "bm",
      "tex": "b_-",
      "description": "331 charge shorthand Sqrt[3] beta - 2"
    },
    {
      "name": "MH2",
      "parameter_type": "External",
      "value": "1500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000002,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MH2",
      "tex": "M_{H_2}",
      "description": "mass of CP-even neutral scalar H2"
    },
    {
      "name": "MH3",
      "parameter_type": "External",
      "value": "2000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000003,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MH3",
      "tex": "M_{H_3}",
      "description": "mass of CP-even neutral scalar H3"
    },
    {
      "name": "MH0",
      "parameter_type": "External",
      "value": "1500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000004,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MH0",
      "tex": "M_{H_0}",
      "description": "mass of CP-odd neutral scalar H0"
    },
    {
      "name": "MHp",
      "parameter_type": "External",
      "value": "1500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000005,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MHp",
      "tex": "M_{H^+}",
      "description": "mass of singly charged scalar H+"
    },
    {
      "name": "MHQY",
      "parameter_type": "External",
      "value": "1400.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000006,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MHQY",
      "tex": "M_{H^{Q_Y}}",
      "description": "mass of scalar with electric charge QY"
    },
    {
      "name": "MHQV",
      "parameter_type": "External",
      "value": "1300.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000007,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MHQV",
      "tex": "M_{H^{Q_V}}",
      "description": "mass of scalar with electric charge QV"
    },
    {
      "name": "MZp",
      "parameter_type": "External",
      "value": "4000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000010,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MZp",
      "tex": "M_{Z'}",
      "description": "mass of the new neutral gauge boson Z'"
    },
    {
      "name": "MY",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000011,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MY",
      "tex": "M_Y",
      "description": "mass of the new charged gauge boson Y"
    },
    {
      "name": "MV",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000012,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MV",
      "tex": "M_V",
      "description": "mass of the new charged gauge boson V"
    },
    {
      "name": "MD",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000021,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MD",
      "tex": "M_D",
      "description": "mass of exotic quark D"
    },
    {
      "name": "MSq",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000022,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MSq",
      "tex": "M_S",
      "description": "mass of exotic quark S"
    },
    {
      "name": "MT",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000023,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MT",
      "tex": "M_T",
      "description": "mass of exotic quark T"
    },
    {
      "name": "MEe",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000031,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MEe",
      "tex": "M_{E_e}",
      "description": "mass of heavy lepton Ee"
    },
    {
      "name": "MEmu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000032,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MEmu",
      "tex": "M_{E_\\\\mu}",
      "description": "mass of heavy lepton Emu"
    },
    {
      "name": "MEtau",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000033,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MEtau",
      "tex": "M_{E_\\\\tau}",
      "description": "mass of heavy lepton Etau"
    },
    {
      "name": "U331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "U331",
      "interaction_order": [
        "NP",
        0
      ],
      "indices": [
        "SU3L",
        "SU3L"
      ],
      "parameter_name": "U331",
      "tex": "U",
      "description": "CP-even neutral scalar rotation matrix"
    },
    {
      "name": "O331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "O331",
      "interaction_order": [
        "NP",
        0
      ],
      "indices": [
        "SU3L",
        "SU3L"
      ],
      "parameter_name": "O331",
      "tex": "O",
      "description": "CP-odd neutral scalar rotation matrix"
    },
    {
      "name": "yU331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "YU331",
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "yU331",
      "tex": "y^u",
      "description": "up-type quark Yukawa matrix"
    },
    {
      "name": "yD331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "YD331",
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "yD331",
      "tex": "y^d",
      "description": "down-type quark Yukawa matrix"
    },
    {
      "name": "yJ331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "YJ331",
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "FirstTwoGeneration",
        "FirstTwoGeneration"
      ],
      "parameter_name": "yJ331",
      "tex": "y^J",
      "description": "Yukawa matrix for D and S exotic quarks"
    },
    {
      "name": "yT331",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YJ331",
      "order_block": 33,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "yT331",
      "tex": "y^J_{33}",
      "description": "Yukawa coupling for T exotic quark"
    },
    {
      "name": "yE331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "YE331",
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "yE331",
      "tex": "y^E",
      "description": "heavy lepton Yukawa matrix"
    },
    {
      "name": "yL331",
      "parameter_type": "External",
      "value_rules": [],
      "complex": false,
      "block_name": "YL331",
      "interaction_order": [
        "NP",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "parameter_name": "yL331",
      "tex": "y^e",
      "description": "charged lepton Yukawa matrix"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "H2",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MH2",
        "value": "1500."
      },
      "width": {
        "sym": "WH2",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000002,
      "particle_name": "H2",
      "full_name": "CP-even heavy neutral scalar H2",
      "propagator_label": "H2",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "H3",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MH3",
        "value": "2000."
      },
      "width": {
        "sym": "WH3",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000003,
      "particle_name": "H3",
      "full_name": "CP-even heavy neutral scalar H3",
      "propagator_label": "H3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "H0",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MH0",
        "value": "1500."
      },
      "width": {
        "sym": "WH0",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000004,
      "particle_name": "H0",
      "full_name": "CP-odd neutral scalar H0",
      "propagator_label": "H0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "Hp",
      "self_conjugate": false,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MHp",
        "value": "1500."
      },
      "width": {
        "sym": "WHp",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "1",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000005,
      "particle_name": "H+",
      "antiparticle_name": "H-",
      "full_name": "singly charged scalar H+",
      "propagator_label": "H+",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "HQY",
      "self_conjugate": false,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MHQY",
        "value": "1400."
      },
      "width": {
        "sym": "WHQY",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "(Sqrt[3]*beta331 + 1)/2",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000006,
      "particle_name": "HqY",
      "antiparticle_name": "HqY~",
      "full_name": "charged scalar with charge QY",
      "propagator_label": "HQY",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "HQV",
      "self_conjugate": false,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MHQV",
        "value": "1300."
      },
      "width": {
        "sym": "WHQV",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "(Sqrt[3]*beta331 - 1)/2",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000007,
      "particle_name": "HqV",
      "antiparticle_name": "HqV~",
      "full_name": "charged scalar with charge QV",
      "propagator_label": "HQV",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Zp",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MZp",
        "value": "4000."
      },
      "width": {
        "sym": "WZp",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "0",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000010,
      "particle_name": "Zp",
      "full_name": "new neutral gauge boson Z'",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "Yp",
      "self_conjugate": false,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MY",
        "value": "1000."
      },
      "width": {
        "sym": "WY",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "(Sqrt[3]*beta331 + 1)/2",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000011,
      "particle_name": "Y",
      "antiparticle_name": "Y~",
      "full_name": "new gauge boson Y with charge QY",
      "propagator_label": "Y",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 103,
      "class_name": "Vp",
      "self_conjugate": false,
      "indices": [],
      "class_members": [],
      "mass": {
        "sym": "MV",
        "value": "1000."
      },
      "width": {
        "sym": "WV",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "(Sqrt[3]*beta331 - 1)/2",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": 9000012,
      "particle_name": "V",
      "antiparticle_name": "V~",
      "full_name": "new gauge boson V with charge QV",
      "propagator_label": "V",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "DQ",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "class_members": [],
      "mass": {
        "sym": "MD",
        "value": "1000."
      },
      "width": {
        "sym": "WD",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "1/6 - Sqrt[3]*beta331/2",
        "ColourRep": "3",
        "SU2Rep": "1"
      },
      "pdg": 9000021,
      "particle_name": "D",
      "antiparticle_name": "D~",
      "full_name": "exotic quark D",
      "propagator_label": "D",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "SQ",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "class_members": [],
      "mass": {
        "sym": "MSq",
        "value": "1000."
      },
      "width": {
        "sym": "WSq",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "1/6 - Sqrt[3]*beta331/2",
        "ColourRep": "3",
        "SU2Rep": "1"
      },
      "pdg": 9000022,
      "particle_name": "S",
      "antiparticle_name": "S~",
      "full_name": "exotic quark S",
      "propagator_label": "S",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 103,
      "class_name": "TQ",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "class_members": [],
      "mass": {
        "sym": "MT",
        "value": "1000."
      },
      "width": {
        "sym": "WT",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "1/6 + Sqrt[3]*beta331/2",
        "ColourRep": "3",
        "SU2Rep": "1"
      },
      "pdg": 9000023,
      "particle_name": "T",
      "antiparticle_name": "T~",
      "full_name": "exotic quark T",
      "propagator_label": "T",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 104,
      "class_name": "EL",
      "self_conjugate": false,
      "indices": [
        "Generation"
      ],
      "flavor_index": "Generation",
      "class_members": [
        "Ee",
        "Emu",
        "Etau"
      ],
      "mass": {
        "sym": "ME",
        "members": [
          [
            "MEe",
            "1000."
          ],
          [
            "MEmu",
            "1000."
          ],
          [
            "MEtau",
            "1000."
          ]
        ]
      },
      "width": {
        "sym": "WE",
        "members": [
          [
            "WEe",
            "Automatic"
          ],
          [
            "WEmu",
            "Automatic"
          ],
          [
            "WEtau",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "-1/2 + Sqrt[3]*beta331/2",
        "ColourRep": "1",
        "SU2Rep": "1"
      },
      "pdg": [
        9000031,
        9000032,
        9000033
      ],
      "particle_name": [
        "Ee",
        "Emu",
        "Etau"
      ],
      "antiparticle_name": [
        "Ee~",
        "Emu~",
        "Etau~"
      ],
      "full_name": [
        "heavy electron partner",
        "heavy muon partner",
        "heavy tau partner"
      ],
      "propagator_label": [
        "Ee",
        "Emu",
        "Etau"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "VHiggs331",
      "expression": "mu1sq HC[rho].rho + mu2sq HC[eta].eta + mu3sq HC[chi].chi + lam1 (HC[rho].rho)^2 + lam2 (HC[eta].eta)^2 + lam3 (HC[chi].chi)^2 + lam12 (HC[rho].rho) (HC[eta].eta) + lam13 (HC[rho].rho) (HC[chi].chi) + lam23 (HC[eta].eta) (HC[chi].chi) + lamp12 (HC[rho].eta) (HC[eta].rho) + lamp13 (HC[rho].chi) (HC[chi].rho) + lamp23 (HC[eta].chi) (HC[chi].eta) + Sqrt[2] f331 (Eps[i,j,k] rho[i] eta[j] chi[k] + HC[Eps[i,j,k] rho[i] eta[j] chi[k]])",
      "delayed": false
    },
    {
      "name": "LHiggs331",
      "expression": "HC[DC[rho, mu]].DC[rho, mu] + HC[DC[eta, mu]].DC[eta, mu] + HC[DC[chi, mu]].DC[chi, mu] - VHiggs331",
      "delayed": false
    },
    {
      "name": "LGauge331Mass",
      "expression": "1/4 gw^2 vev^2 W[mu] HC[W[mu]] + 1/4 gw^2 (v3^2 + v2^2) Yp[mu] HC[Yp[mu]] + 1/4 gw^2 (v3^2 + v1^2) Vp[mu] HC[Vp[mu]] + 1/2 MZp^2 Zp[mu] Zp[mu]",
      "delayed": false
    },
    {
      "name": "LYukawaQuark331",
      "expression": "-(yU331[i,j] HC[qL[i]].eta.uR[j] + yU331[3,j] HC[qL[3]].HC[rho].uR[j] + yD331[i,j] HC[qL[i]].rho.dR[j] + yD331[3,j] HC[qL[3]].HC[eta].dR[j] + yJ331[i,k] HC[qL[i]].chi.JR[k] + yT331 HC[qL[3]].HC[chi].TR + HC[yU331[i,j] HC[qL[i]].eta.uR[j] + yU331[3,j] HC[qL[3]].HC[rho].uR[j] + yD331[i,j] HC[qL[i]].rho.dR[j] + yD331[3,j] HC[qL[3]].HC[eta].dR[j] + yJ331[i,k] HC[qL[i]].chi.JR[k] + yT331 HC[qL[3]].HC[chi].TR])",
      "delayed": false
    },
    {
      "name": "LYukawaLepton331",
      "expression": "-(yL331[m,n] HC[lL[m]].HC[eta].eR[n] + yE331[m,n] HC[lL[m]].HC[chi].ER[n] + HC[yL331[m,n] HC[lL[m]].HC[eta].eR[n] + yE331[m,n] HC[lL[m]].HC[chi].ER[n]])",
      "delayed": false
    },
    {
      "name": "LFermionGauge331",
      "expression": "I HC[psi[a]].Ga[mu].DC[psi[a], mu]",
      "delayed": false
    },
    {
      "name": "LZpFermions331",
      "expression": "Zp[mu] (GHZpL[f] HC[f].Ga[mu].ProjM.f + GHZpR[f] HC[f].Ga[mu].ProjP.f)",
      "delayed": false
    },
    {
      "name": "LGaugeSelf331",
      "expression": "(-I e) A[mu] W[nu] HC[W[rho]] VVV[mu,nu,rho] + (I am e/2) A[mu] Vp[nu] HC[Vp[rho]] VVV[mu,nu,rho] + (I ap e/2) A[mu] Yp[nu] HC[Yp[rho]] VVV[mu,nu,rho] - I Sqrt[3] e a0/(2 cw sw) Zp[mu] (Vp[nu] HC[Vp[rho]] + Yp[nu] HC[Yp[rho]]) VVV[mu,nu,rho]",
      "delayed": false
    },
    {
      "name": "LScalarFermion331",
      "expression": "H0 (O331[3,1] ME[ll]/v3 HC[EL[ll]].EL[ll] + O331[2,1] Ml[ll]/v2 HC[LL[ll]].LL[ll]) - I H2 (U331[3,2] ME[ll]/v3 HC[EL[ll]].EL[ll]) - I H3 (U331[3,3] ME[ll]/v3 HC[EL[ll]].EL[ll]) - I H2 (U331[1,2] Md[q]/v1 HC[d[q]].d[q] + U331[2,2] Mu[q]/v2 HC[u[q]].u[q]) - I H3 (U331[1,3] Md[q]/v1 HC[d[q]].d[q] + U331[2,3] Mu[q]/v2 HC[u[q]].u[q])",
      "delayed": false
    }
  ],
  "raw_preamble": [
    "M$Restrictions = {};",
    "FR$LoopSwitches = {};",
    "IndexStyle[FirstTwoGeneration, i2];",
    "IndexStyle[SU3L, a3];",
    "(* Gauge structure of the underlying theory is SU(3)C x SU(3)L x U(1)X, with Q = T3 + beta331 T8 + X. This file is encoded as an SM add-on after symmetry breaking. *)",
    "(* Scalar triplets: rho = {rhoP, rho0, rhoMQV}, eta = {eta0, etaM, etaMQY}, chi = {chiQY, chiQV, chi0}. *)",
    "(* Fermion multiplets: q1L={u,d,D}, q2L={c,s,S}, q3L={b,-t,T}; lL={e,-nu,E}. *)"
  ],
  "raw_blocks": [
    "M$MixingsDescription = { Mix[Hneutral331] == { GaugeBasis -> {xirho, xieta, xichi}, MassBasis -> {h, H2, H3}, MixingMatrix -> U331 }, Mix[Aneutral331] == { GaugeBasis -> {zetarho, zetaeta, zetachi}, MassBasis -> {H0, G0, G0p}, MixingMatrix -> O331 }, Mix[Hcharged331] == { GaugeBasis -> {etaP, rhoP}, MassBasis -> {Hp, GP}, MixingMatrix -> {{c12, -s12}, {s12, c12}} }, Mix[HQY331] == { GaugeBasis -> {chiQY, etaQY}, MassBasis -> {HQY, GY}, MixingMatrix -> {{c23, -s23}, {s23, c23}} }, Mix[HQV331] == { GaugeBasis -> {chiQV, rhoQV}, MassBasis -> {HQV, GV}, MixingMatrix -> {{c13, -s13}, {s13, c13}} } };",
    "M$Definitions = { QY331 -> (Sqrt[3] beta331 + 1)/2, QV331 -> (Sqrt[3] beta331 - 1)/2, QD331 -> 1/6 - Sqrt[3] beta331/2, QT331 -> 1/6 + Sqrt[3] beta331/2, QE331 -> -1/2 + Sqrt[3] beta331/2 };",
    "(* Decoupling-limit masses from the paper: MH2^2 = vev^2 f331 v3/(v1 v2); MH3^2 = 2 lam3 v3^2; MH0^2 = f331 (v1 v2/v3 + v1 v3/v2 + v2 v3/v1); MHp^2 = ((2 f331 v3 + lamp12 v1 v2)/(2 v1 v2)) vev^2; MHQY^2 = ((2 f331 v1 + lamp23 v2 v3)/(2 v2 v3)) (v2^2 + v3^2); MHQV^2 = ((2 f331 v2 + lamp13 v1 v3)/(2 v1 v3)) (v1^2 + v3^2); MY^2 = gw^2 (v3^2 + v2^2)/4; MV^2 = gw^2 (v3^2 + v1^2)/4; MZp^2 = cw^2 gw^2 v3^2/(3 (1 - (1 + beta331^2) sw^2)). *)"
  ]
}
```