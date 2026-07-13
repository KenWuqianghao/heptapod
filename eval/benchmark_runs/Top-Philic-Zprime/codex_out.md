```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": [
      "Jeong Han Kim",
      "Kyoungchul Kong",
      "Seung J. Lee",
      "Gopolang Mohlabeng"
    ],
    "version": "1.0.0",
    "date": "November 3, 2016",
    "institutions": [
      "KAIST",
      "University of Kansas",
      "Korea University",
      "KIAS",
      "Fermilab"
    ],
    "emails": [
      "jeonghan.kim@kaist.ac.kr",
      "kckong@ku.edu",
      "sjjlee@korea.edu",
      "gopolang.mohlabeng@ku.edu"
    ]
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
      2
    ]
  ],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "MV1",
      "parameter_type": "External",
      "value": "1500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000047,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "MV1",
      "tex": "M_{V_1}",
      "description": "Mass of the top-philic color-singlet vector resonance V1"
    },
    {
      "name": "ct",
      "parameter_type": "External",
      "value": "2.",
      "complex": false,
      "block_name": "TPZPINPUTS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "ct",
      "tex": "c_t",
      "description": "Overall V1 coupling strength to top quarks"
    },
    {
      "name": "thetaV1",
      "parameter_type": "External",
      "value": "1.5707963267948966",
      "complex": false,
      "block_name": "TPZPINPUTS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "thetaV1",
      "tex": "\\theta",
      "description": "Chirality angle tan(theta)=cR/cL for the V1 top coupling"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "definitions": [
        {
          "lhs": "cL",
          "rhs": "ct Cos[thetaV1]",
          "delayed": false
        }
      ],
      "tex": "c_L",
      "description": "Left-handed V1 top coupling"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "definitions": [
        {
          "lhs": "cR",
          "rhs": "ct Sin[thetaV1]",
          "delayed": false
        }
      ],
      "tex": "c_R",
      "description": "Right-handed V1 top coupling"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "complex": false,
      "definitions": [
        {
          "lhs": "WV1",
          "rhs": "If[NumericalValue[MV1] > 2 NumericalValue[MT], (ct^2 MV1)/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2] (1 - MT^2/MV1^2 (1 - 3 Sin[2 thetaV1])), 0]",
          "delayed": true
        }
      ],
      "tex": "\\Gamma_{V_1}",
      "description": "Tree-level V1 width into top-antitop"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "sym": "WV1",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 9000047,
      "particle_name": "V1",
      "full_name": "Top-philic color-singlet vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LV1kin",
      "expression": "-1/4 (del[V1[nu], mu] - del[V1[mu], nu]) (del[V1[nu], mu] - del[V1[mu], nu]) + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": false
    },
    {
      "name": "LV1intL",
      "expression": "Block[{sp1, sp2, cc}, cL V1[mu] QLbar[sp1, 1, 3, cc] Ga[mu, sp1, sp2] QL[sp2, 1, 3, cc]]",
      "delayed": false
    },
    {
      "name": "LV1intR",
      "expression": "Block[{sp1, sp2, cc}, cR V1[mu] uRbar[sp1, 3, cc] Ga[mu, sp1, sp2] uR[sp2, 3, cc]]",
      "delayed": false
    },
    {
      "name": "LV1int",
      "expression": "LV1intL + LV1intR",
      "delayed": false
    },
    {
      "name": "LBSM",
      "expression": "LV1kin + LV1int",
      "delayed": false
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```