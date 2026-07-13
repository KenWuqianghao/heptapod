```json
{
  "model_name": "DMsimp_gen",
  "info": {
    "authors": [
      "O. Mattelaer",
      "E. Vryonidou"
    ],
    "version": "1.0",
    "date": "2015-08-03",
    "institutions": [
      "Institute for Particle Physics Phenomenology, Durham University",
      "Centre for Cosmology, Particle Physics and Phenomenology, Universite catholique de Louvain"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "QCD",
      1
    ],
    [
      "DMS",
      2
    ],
    [
      "DMV",
      2
    ],
    [
      "QED",
      2
    ]
  ],
  "interaction_order_limit": [
    [
      "DMS",
      2
    ],
    [
      "DMV",
      2
    ]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "MXr",
      "parameter_type": "External",
      "value": "10.",
      "block_name": "MASS",
      "order_block": 5000511,
      "parameter_name": "MXr",
      "tex": "M_{X_r}",
      "description": "real scalar dark matter mass"
    },
    {
      "name": "MXc",
      "parameter_type": "External",
      "value": "10.",
      "block_name": "MASS",
      "order_block": 5000512,
      "parameter_name": "MXc",
      "tex": "M_{X_c}",
      "description": "complex scalar dark matter mass"
    },
    {
      "name": "MXd",
      "parameter_type": "External",
      "value": "10.",
      "block_name": "MASS",
      "order_block": 5000521,
      "parameter_name": "MXd",
      "tex": "M_{X_d}",
      "description": "Dirac dark matter mass"
    },
    {
      "name": "MY0",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "MASS",
      "order_block": 5000002,
      "parameter_name": "MY0",
      "tex": "M_{Y_0}",
      "description": "spin-0 mediator mass"
    },
    {
      "name": "MY1",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "MASS",
      "order_block": 5000003,
      "parameter_name": "MY1",
      "tex": "M_{Y_1}",
      "description": "spin-1 mediator mass"
    },
    {
      "name": "WY0",
      "parameter_type": "External",
      "value": "10.",
      "block_name": "DECAY",
      "order_block": 5000002,
      "parameter_name": "WY0",
      "tex": "\\Gamma_{Y_0}",
      "description": "spin-0 mediator width"
    },
    {
      "name": "WY1",
      "parameter_type": "External",
      "value": "10.",
      "block_name": "DECAY",
      "order_block": 5000003,
      "parameter_name": "WY1",
      "tex": "\\Gamma_{Y_1}",
      "description": "spin-1 mediator width"
    },
    {
      "name": "gSXr",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 1,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gSXr",
      "tex": "g_{S X_r}",
      "description": "real scalar DM coupling to Y0"
    },
    {
      "name": "gSXc",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 2,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gSXc",
      "tex": "g_{S X_c}",
      "description": "complex scalar DM coupling to Y0"
    },
    {
      "name": "gSXd",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 3,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gSXd",
      "tex": "g^S_{DM}",
      "description": "Dirac DM scalar coupling to Y0"
    },
    {
      "name": "gPXd",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 4,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gPXd",
      "tex": "g^P_{DM}",
      "description": "Dirac DM pseudoscalar coupling to Y0"
    },
    {
      "name": "gSt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 5,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gSt",
      "tex": "g^S_t",
      "description": "top scalar coupling to Y0"
    },
    {
      "name": "gPt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 6,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gPt",
      "tex": "g^P_t",
      "description": "top pseudoscalar coupling to Y0"
    },
    {
      "name": "Lambda",
      "parameter_type": "External",
      "value": "10000.",
      "block_name": "DMINPUTS",
      "order_block": 7,
      "parameter_name": "Lambda",
      "tex": "\\Lambda",
      "description": "cutoff scale for effective gluon coupling"
    },
    {
      "name": "gSg",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 8,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gSg",
      "tex": "g^S_g",
      "description": "effective scalar gluon coupling to Y0"
    },
    {
      "name": "gPg",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 9,
      "interaction_order": [
        "DMS",
        1
      ],
      "parameter_name": "gPg",
      "tex": "g^P_g",
      "description": "effective pseudoscalar gluon coupling to Y0"
    },
    {
      "name": "gVXc",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 10,
      "interaction_order": [
        "DMV",
        1
      ],
      "parameter_name": "gVXc",
      "tex": "g_{V X_c}",
      "description": "complex scalar DM derivative coupling to Y1"
    },
    {
      "name": "gVXd",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 11,
      "interaction_order": [
        "DMV",
        1
      ],
      "parameter_name": "gVXd",
      "tex": "g^V_{DM}",
      "description": "Dirac DM vector coupling to Y1"
    },
    {
      "name": "gAXd",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 12,
      "interaction_order": [
        "DMV",
        1
      ],
      "parameter_name": "gAXd",
      "tex": "g^A_{DM}",
      "description": "Dirac DM axial-vector coupling to Y1"
    },
    {
      "name": "gVt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 13,
      "interaction_order": [
        "DMV",
        1
      ],
      "parameter_name": "gVt",
      "tex": "g^V_t",
      "description": "top vector coupling to Y1"
    },
    {
      "name": "gAt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 14,
      "interaction_order": [
        "DMV",
        1
      ],
      "parameter_name": "gAt",
      "tex": "g^A_t",
      "description": "top axial-vector coupling to Y1; bottom axial coupling is fixed to -gAt"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 7,
      "class_name": "Xr",
      "self_conjugate": true,
      "mass": {
        "sym": "MXr",
        "value": "10."
      },
      "width": {
        "massless": true
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000511,
      "particle_name": "xr",
      "full_name": "Real scalar dark matter",
      "propagator_label": "Xr",
      "propagator_type": "ScalarDash"
    },
    {
      "spin_type": "S",
      "class_index": 8,
      "class_name": "Xc",
      "self_conjugate": false,
      "mass": {
        "sym": "MXc",
        "value": "10."
      },
      "width": {
        "massless": true
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000512,
      "particle_name": "xc",
      "antiparticle_name": "xc~",
      "full_name": "Complex scalar dark matter",
      "propagator_label": "Xc",
      "propagator_type": "ScalarDash"
    },
    {
      "spin_type": "F",
      "class_index": 7,
      "class_name": "Xd",
      "self_conjugate": false,
      "mass": {
        "sym": "MXd",
        "value": "10."
      },
      "width": {
        "massless": true
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000521,
      "particle_name": "xd",
      "antiparticle_name": "xd~",
      "full_name": "Dirac dark matter",
      "propagator_label": "Xd",
      "propagator_type": "Straight"
    },
    {
      "spin_type": "S",
      "class_index": 9,
      "class_name": "Y0",
      "self_conjugate": true,
      "mass": {
        "sym": "MY0",
        "value": "1000."
      },
      "width": {
        "sym": "WY0",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000002,
      "particle_name": "y0",
      "full_name": "Scalar mediator",
      "propagator_label": "Y0",
      "propagator_type": "ScalarDash"
    },
    {
      "spin_type": "V",
      "class_index": 7,
      "class_name": "Y1",
      "self_conjugate": true,
      "mass": {
        "sym": "MY1",
        "value": "1000."
      },
      "width": {
        "sym": "WY1",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000003,
      "particle_name": "y1",
      "full_name": "Spin-1 mediator",
      "propagator_label": "Y1",
      "propagator_type": "Sine"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "L0X",
      "expression": "1/2 MXr gSXr Xr Xr Y0 + MXc gSXc Xcbar Xc Y0 + Xdbar.(gSXd + I gPXd Ga[5]).Xd Y0",
      "delayed": true
    },
    {
      "name": "L0SM",
      "expression": "1/Sqrt[2] yt tbar.(gSt + I gPt Ga[5]).t Y0",
      "delayed": true
    },
    {
      "name": "L0SMg",
      "expression": "1/Lambda FS[G,mu,nu,a] (gSg FS[G,mu,nu,a] + gPg Dual[FS][G,mu,nu,a]) Y0",
      "delayed": true
    },
    {
      "name": "L0DM",
      "expression": "L0X + L0SM + L0SMg",
      "delayed": true
    },
    {
      "name": "L1X",
      "expression": "I gVXc/2 (Xcbar del[Xc,mu] - del[Xcbar,mu] Xc) Y1[mu] + Xdbar.Ga[mu].(gVXd + gAXd Ga[5]).Xd Y1[mu]",
      "delayed": true
    },
    {
      "name": "L1SM",
      "expression": "tbar.Ga[mu].(gVt + gAt Ga[5]).t Y1[mu] + bbar.Ga[mu].(-gAt Ga[5]).b Y1[mu]",
      "delayed": true
    },
    {
      "name": "L1DM",
      "expression": "L1X + L1SM",
      "delayed": true
    }
  ]
}
```