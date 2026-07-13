```json
{
  "model_name": "SLQrules_gen",
  "info": {
    "authors": [
      "Andreas Crivellin",
      "Luc Schnell"
    ],
    "version": "1.0",
    "date": "2026-07-12",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "NP",
      2
    ]
  ],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "LQTwo",
      "range_kind": "NoUnfold",
      "size": 2,
      "style_symbol": "n2"
    }
  ],
  "parameters": [
    {
      "name": "m12",
      "parameter_type": "External",
      "value": "1500.^2",
      "complex": false,
      "block_name": "M12",
      "interaction_order": [
        "NP",
        2
      ],
      "description": "Phi1 mass-squared parameter"
    },
    {
      "name": "m1t2",
      "parameter_type": "External",
      "value": "1500.^2",
      "complex": false,
      "block_name": "M1T2",
      "interaction_order": [
        "NP",
        2
      ],
      "description": "PhiTilde1 mass-squared parameter"
    },
    {
      "name": "m22",
      "parameter_type": "External",
      "value": "1500.^2",
      "complex": false,
      "block_name": "M22",
      "interaction_order": [
        "NP",
        2
      ],
      "description": "Phi2 mass-squared parameter"
    },
    {
      "name": "m2t2",
      "parameter_type": "External",
      "value": "1500.^2",
      "complex": false,
      "block_name": "M2T2",
      "interaction_order": [
        "NP",
        2
      ],
      "description": "PhiTilde2 mass-squared parameter"
    },
    {
      "name": "m32",
      "parameter_type": "External",
      "value": "1500.^2",
      "complex": false,
      "block_name": "M32",
      "interaction_order": [
        "NP",
        2
      ],
      "description": "Phi3 mass-squared parameter"
    },
    {
      "name": "Y1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y1t",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1T",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y2",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y2t",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2T",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y3",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y3",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y22",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y22",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y2t2t",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2T2T",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y33",
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "A1t2",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "At23",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y2t2",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Yt13",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "Y13",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        2
      ]
    },
    {
      "name": "W13mat",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "unitary": true,
      "description": "unitary mixing matrix W^-1/3"
    },
    {
      "name": "W23mat",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "unitary": true,
      "description": "unitary mixing matrix W^+2/3"
    },
    {
      "name": "W43mat",
      "parameter_type": "Internal",
      "indices": [
        "LQTwo",
        "LQTwo"
      ],
      "complex": true,
      "unitary": true,
      "description": "unitary mixing matrix W^-4/3"
    },
    {
      "name": "Y1RR",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1LL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1QLL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "symmetric diquark matrix"
    },
    {
      "name": "Y1QRR",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1tRR",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1tQRR",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "antisymmetric diquark matrix"
    },
    {
      "name": "Y2RL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y2LR",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y2tRL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y3LL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y3QLL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Generation"
      ],
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "antisymmetric diquark matrix"
    },
    {
      "name": "A1t2t2",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "At12t2",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1t12",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y123",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1t23",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Yt123",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y233",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Yt233",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ]
    },
    {
      "name": "Y1x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1X1"
    },
    {
      "name": "Y1tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1TX1"
    },
    {
      "name": "Y2x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2X1"
    },
    {
      "name": "Y2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2TX1"
    },
    {
      "name": "Y3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y3X1"
    },
    {
      "name": "Y2x3",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2X3"
    },
    {
      "name": "Y2tx3",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2TX3"
    },
    {
      "name": "Y3x3",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y3X3"
    },
    {
      "name": "Y3x5",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y3X5"
    },
    {
      "name": "Y1x1tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1X1TX1"
    },
    {
      "name": "Yprime1x1tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1X1TX1"
    },
    {
      "name": "Y1x2x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1X2X1"
    },
    {
      "name": "Yprime1x2x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1X2X1"
    },
    {
      "name": "Y1x2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1X2TX1"
    },
    {
      "name": "Yprime1x2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1X2TX1"
    },
    {
      "name": "Y1x3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1X3X1"
    },
    {
      "name": "Yprime1x3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1X3X1"
    },
    {
      "name": "Y1tx2x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1TX2X1"
    },
    {
      "name": "Yprime1tx2x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1TX2X1"
    },
    {
      "name": "Y1tx2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1TX2TX1"
    },
    {
      "name": "Yprime1tx2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1TX2TX1"
    },
    {
      "name": "Y1tx3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y1TX3X1"
    },
    {
      "name": "Yprime1tx3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP1TX3X1"
    },
    {
      "name": "Y2x2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2X2TX1"
    },
    {
      "name": "Yprime2x2tx1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP2X2TX1"
    },
    {
      "name": "Y2x3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2X3X1"
    },
    {
      "name": "Yprime2x3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP2X3X1"
    },
    {
      "name": "Y2tx3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "Y2TX3X1"
    },
    {
      "name": "Yprime2tx3x1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "YP2TX3X1"
    },
    {
      "name": "Y2t2x3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime2t2x3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y23x3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime23x3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y2t3x3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime2t3x3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y1223",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime1223",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y1t2t23",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime1t2t23",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y1t1t22",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime1t1t22",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y1t22t3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Yprime1t22t3",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y1313",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    },
    {
      "name": "Y1333",
      "parameter_type": "Internal",
      "value": "1.0",
      "complex": true
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "S1m13hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "m1m13hat",
        "value": "Internal"
      },
      "width": {
        "sym": "W1m13hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "-1/3"
      },
      "particle_name": "S1m13hat",
      "antiparticle_name": "S1m13hat~",
      "full_name": "mass eigenstate from Phi1: scalar colour triplet, SU(2) singlet, Y=-1/3, Q=-1/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "R2tm13hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mR2tm13hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WR2tm13hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "-1/3"
      },
      "particle_name": "R2tm13hat",
      "antiparticle_name": "R2tm13hat~",
      "full_name": "mass eigenstate from lower component of PhiTilde2: scalar colour triplet, SU(2) doublet, Y=1/6, Q=-1/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "S3m13hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mS3m13hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WS3m13hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "-1/3"
      },
      "particle_name": "S3m13hat",
      "antiparticle_name": "S3m13hat~",
      "full_name": "mass eigenstate from Phi3 component: scalar colour triplet, SU(2) triplet, Y=-1/3, Q=-1/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "R2p23hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mR2p23hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WR2p23hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "2/3"
      },
      "particle_name": "R2p23hat",
      "antiparticle_name": "R2p23hat~",
      "full_name": "mass eigenstate from lower component of Phi2: scalar colour triplet, SU(2) doublet, Y=7/6, Q=2/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "R2tp23hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mR2tp23hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WR2tp23hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "2/3"
      },
      "particle_name": "R2tp23hat",
      "antiparticle_name": "R2tp23hat~",
      "full_name": "mass eigenstate from upper component of PhiTilde2: scalar colour triplet, SU(2) doublet, Y=1/6, Q=2/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "S3p23hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mS3p23hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WS3p23hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "2/3"
      },
      "particle_name": "S3p23hat",
      "antiparticle_name": "S3p23hat~",
      "full_name": "mass eigenstate from Phi3 component: scalar colour triplet, SU(2) triplet, Y=-1/3, Q=2/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "S1tm43hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mS1tm43hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WS1tm43hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "-4/3"
      },
      "particle_name": "S1tm43hat",
      "antiparticle_name": "S1tm43hat~",
      "full_name": "mass eigenstate from PhiTilde1: scalar colour triplet, SU(2) singlet, Y=-4/3, Q=-4/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 107,
      "class_name": "S3m43hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mS3m43hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WS3m43hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "-4/3"
      },
      "particle_name": "S3m43hat",
      "antiparticle_name": "S3m43hat~",
      "full_name": "mass eigenstate from Phi3 component: scalar colour triplet, SU(2) triplet, Y=-1/3, Q=-4/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 108,
      "class_name": "R2p53hat",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "mR2p53hat",
        "value": "Internal"
      },
      "width": {
        "sym": "WR2p53hat",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "5/3"
      },
      "particle_name": "R2p53hat",
      "antiparticle_name": "R2p53hat~",
      "full_name": "mass eigenstate from upper component of Phi2: scalar colour triplet, SU(2) doublet, Y=7/6, Q=5/3",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LQ2Phi",
      "delayed": true,
      "expression": "-(m12 + Y1 HC[Phi].Phi) HC[S1].S1 - (m1t2 + Y1t HC[Phi].Phi) HC[S1t].S1t - (m22 + Y2 HC[Phi].Phi) HC[R2].R2 - (m2t2 + Y2t HC[Phi].Phi) HC[R2t].R2t - (m32 + Y3 HC[Phi].Phi) HC[S3].S3 - Y22 HC[Phi.Eps.R2] Phi.Eps.R2 - Y2t2t HC[Phi.Eps.R2t] Phi.Eps.R2t - I Y33 Eps[D,E,F] HC[Phi].Ta[D].Phi HC[S3[E]].S3[F] - (A1t2 HC[R2t].Phi.S1 + At23 HC[R2t].Ta[D].S3[D].Phi + Y2t2 HC[R2].Phi Phi.Eps.R2t + Yt13 Phi.Eps.HC[Ta[D].S3[D]].Phi S1t + Y13 HC[Phi].Ta[D].S3[D].Phi HC[S1] + HC[...])"
    },
    {
      "name": "LQkin",
      "delayed": true,
      "expression": "ExpandIndices[DC[HC[S1], mu] DC[S1, mu] + DC[HC[S1t], mu] DC[S1t, mu] + DC[HC[R2], mu] DC[R2, mu] + DC[HC[R2t], mu] DC[R2t, mu] + DC[HC[S3], mu] DC[S3, mu], FlavorExpand -> {SU2D, SU2W}]"
    },
    {
      "name": "LQf",
      "delayed": true,
      "expression": "Module[{i,j,a,b,c,aa,bb,cc}, ExpandIndices[Y1RR[i,j] uqbarC[i,aa].ProjR.l[j] HC[S1[aa]] + Y1LL[i,j] QbarC[i,a,aa].ProjL.Eps[a,b].LL[j,b] HC[S1[aa]] + Y1QLL[i,j] QbarC[i,a,aa].ProjL.Eps[a,b].Q[j,b,bb] S1[cc] Eps[aa,bb,cc] + Y1QRR[i,j] uqbarC[i,aa].ProjR.dq[j,bb] S1[cc] Eps[aa,bb,cc] + Y1tRR[i,j] dqbarC[i,aa].ProjR.l[j] HC[S1t[aa]] + Y1tQRR[i,j] uqbarC[i,aa].ProjR.uq[j,bb] S1t[cc] Eps[aa,bb,cc] + Y2RL[i,j] HC[R2[a,aa]].uqbar[i,aa].ProjL.Eps[a,b].LL[j,b] + Y2LR[i,j] Qbar[i,a,aa].ProjR.l[j] R2[a,aa] + Y2tRL[i,j] HC[R2t[a,aa]].dqbar[i,aa].ProjL.Eps[a,b].LL[j,b] + Y3LL[i,j] QbarC[i,a,aa].ProjL.Eps[a,b].Ta[D,b,c].LL[j,c] HC[S3[D,aa]] + Y3QLL[i,j] QbarC[i,a,aa].ProjL.Eps[a,b].Ta[D,b,c].Q[j,c,bb] S3[D,cc] Eps[aa,bb,cc] + HC[...], FlavorExpand -> {SU2D, SU2W, Generation}]]"
    },
    {
      "name": "LQ3Phi",
      "delayed": true,
      "expression": "Module[{a,b,c,D,E,F,aa,bb,cc}, ExpandIndices[A1t2t2 S1[aa] R2t[a,bb] Eps[a,b] R2t[b,cc] Eps[aa,bb,cc] + At12t2 S1t[aa] R2[a,bb] Eps[a,b] R2t[b,cc] Eps[aa,bb,cc] + Y1t12 S1[aa] S1t[bb] R2[a,cc] Eps[a,b] Phi[b] Eps[aa,bb,cc] + Y123 S1[aa] HC[Phi[a]] Ta[D,a,b] S3[D,cc] R2[b,bb] Eps[aa,bb,cc] + Y1t23 S1[aa] R2t[a,bb] Eps[a,b] Ta[D,b,c] S3[D,cc] Phi[c] Eps[aa,bb,cc] + Yt123 S1t[aa] R2[a,bb] Eps[a,b] Ta[D,b,c] S3[D,cc] Phi[c] Eps[aa,bb,cc] + Y233 HC[Phi[a]] Ta[D,a,b] R2[b,aa] S3[E,bb] I Eps[D,E,F] S3[F,cc] Eps[aa,bb,cc] + Yt233 R2t[a,aa] Eps[a,b] Ta[D,b,c] Phi[c] S3[E,bb] I Eps[D,E,F] S3[F,cc] Eps[aa,bb,cc], FlavorExpand -> {SU2D, SU2W}]] + HC[%]"
    },
    {
      "name": "LQ4Phi",
      "delayed": true,
      "expression": "Module[{a,b,D,E,F,aa,bb,cc,dd}, ExpandIndices[1/2 Sum[Ya1 HC[Phia[aa]].Phia[aa] HC[Phia[bb]].Phia[bb], a] + 1/2 (Y2x3 HC[R2[a,aa]] R2[a,bb] HC[R2[b,bb]] R2[b,aa] + Y2tx3 HC[R2t[a,aa]] R2t[a,bb] HC[R2t[b,bb]] R2t[b,aa] + Y3x3 HC[S3[D,aa]] S3[D,bb] HC[S3[E,bb]] S3[E,aa]) + 1/2 Y3x5 HC[S3[D,aa]] S3[E,aa] HC[S3[D,bb]] S3[E,bb] + Sum[(Yab1 del[aa,bb] del[cc,dd] + Yprimeab1 del[aa,dd] del[bb,cc]) HC[Phia[aa]] Phia[bb] HC[Phib[cc]] Phib[dd], {a,b}] + (Y2t2x3 del[aa,bb] del[cc,dd] + Yprime2t2x3 del[aa,dd] del[bb,cc]) HC[R2[a,aa]] R2t[a,bb] HC[R2t[b,cc]] R2[b,dd] + Sum[(Ya3x3 del[aa,bb] del[cc,dd] + Yprimea3x3 del[aa,dd] del[bb,cc]) HC[PhiA[a,aa]] Ta[D,a,b] PhiA[b,bb] HC[S3[E,cc]] I Eps[D,E,F] S3[F,dd], A] + ((Y1223 del[aa,bb] del[cc,dd] + Yprime1223 del[aa,dd] del[bb,cc]) HC[S1[aa]] HC[R2[a,cc]] Ta[D,a,b] S3[D,dd] R2[b,bb] + (Y1t2t23 del[aa,bb] del[cc,dd] + Yprime1t2t23 del[aa,dd] del[bb,cc]) HC[S1[aa]] HC[R2t[a,cc]] Ta[D,a,b] S3[D,dd] R2t[b,bb] + (Y1t22t3 del[aa,bb] del[cc,dd] + Yprime1t22t3 del[aa,dd] del[bb,cc]) HC[S1t[aa]] HC[R2[a,cc]] Ta[D,a,b] S3[D,dd] R2t[b,bb] + (Y1t1t22 del[aa,bb] del[cc,dd] + Yprime1t1t22 del[aa,dd] del[bb,cc]) HC[S1[aa]] S1t[bb] HC[R2t[a,cc]] R2[a,dd] + 1/2 Y1313 HC[S1[aa]] S3[D,bb] HC[S1[cc]] S3[D,dd] + Y1333 HC[S1[aa]] S3[D,bb] HC[S3[E,cc]] I Eps[D,E,F] S3[F,dd] + HC[...]), FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "LBSM",
      "expression": "LQ2Phi + LQkin + LQf + LQ3Phi + LQ4Phi"
    }
  ]
}
```