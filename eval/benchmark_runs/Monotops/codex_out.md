```json
{
  "model_name": "Monotops_gen",
  "info": {
    "authors": [
      "J. Andrea",
      "B. Fuks",
      "F. Maltoni"
    ],
    "version": "1.0.0",
    "date": "05.07.11",
    "institutions": [
      "IPHC Strasbourg / University of Strasbourg",
      "CP3 / Universite Catholique de Louvain"
    ],
    "emails": [
      "fuks@cern.ch"
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
      "MT1",
      3
    ],
    [
      "MT2",
      3
    ],
    [
      "MT3",
      3
    ],
    [
      "MT4",
      3
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "A0FC",
      "parameter_type": "External",
      "complex": false,
      "block_name": "A0FC",
      "interaction_order": [
        "MT1",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "A0FC[1,1]",
          "rhs": "0."
        },
        {
          "lhs": "A0FC[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "A0FC[1,3]",
          "rhs": "0.1"
        },
        {
          "lhs": "A0FC[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "A0FC[2,2]",
          "rhs": "0."
        },
        {
          "lhs": "A0FC[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "A0FC[3,1]",
          "rhs": "0.1"
        },
        {
          "lhs": "A0FC[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "A0FC[3,3]",
          "rhs": "0."
        }
      ],
      "tex": "Subsuperscript[A,FC,0]",
      "description": "FCNC scalar quark-quark couplings"
    },
    {
      "name": "B0FC",
      "parameter_type": "External",
      "complex": false,
      "block_name": "B0FC",
      "interaction_order": [
        "MT1",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "B0FC[_,_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[B,FC,0]",
      "description": "FCNC pseudoscalar quark-quark couplings"
    },
    {
      "name": "A1FC",
      "parameter_type": "External",
      "complex": false,
      "block_name": "A1FC",
      "interaction_order": [
        "MT2",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "A1FC[1,1]",
          "rhs": "0."
        },
        {
          "lhs": "A1FC[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "A1FC[1,3]",
          "rhs": "0.1"
        },
        {
          "lhs": "A1FC[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "A1FC[2,2]",
          "rhs": "0."
        },
        {
          "lhs": "A1FC[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "A1FC[3,1]",
          "rhs": "0.1"
        },
        {
          "lhs": "A1FC[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "A1FC[3,3]",
          "rhs": "0."
        }
      ],
      "tex": "Subsuperscript[A,FC,1]",
      "description": "FCNC vector quark-quark couplings"
    },
    {
      "name": "B1FC",
      "parameter_type": "External",
      "complex": false,
      "block_name": "B1FC",
      "interaction_order": [
        "MT2",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "B1FC[_,_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[B,FC,1]",
      "description": "FCNC pseudovector quark-quark couplings"
    },
    {
      "name": "A12S",
      "parameter_type": "External",
      "complex": false,
      "block_name": "A12S",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "A12S[1]",
          "rhs": "0."
        },
        {
          "lhs": "A12S[2]",
          "rhs": "0."
        },
        {
          "lhs": "A12S[3]",
          "rhs": "0.1"
        }
      ],
      "tex": "Subsuperscript[A,S,12]",
      "description": "Colored scalar resonance couplings to quark-FMET"
    },
    {
      "name": "B12S",
      "parameter_type": "External",
      "complex": false,
      "block_name": "B12S",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "B12S[_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[B,S,12]",
      "description": "Colored scalar resonance couplings to quark-FMET"
    },
    {
      "name": "tA12S",
      "parameter_type": "External",
      "complex": false,
      "block_name": "tA12S",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "tA12S[1]",
          "rhs": "0.1"
        },
        {
          "lhs": "tA12S[2]",
          "rhs": "0.1"
        },
        {
          "lhs": "tA12S[3]",
          "rhs": "0."
        }
      ],
      "tex": "Subsuperscript[tA,S,12]",
      "description": "t-channel and u-channel scalar couplings to d-FMET"
    },
    {
      "name": "tB12S",
      "parameter_type": "External",
      "complex": false,
      "block_name": "tB12S",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "tB12S[_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[tB,S,12]",
      "description": "t-channel and u-channel pseudoscalar couplings to d-FMET"
    },
    {
      "name": "AQS",
      "parameter_type": "External",
      "complex": false,
      "block_name": "AQS",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "AQS[1,1]",
          "rhs": "0."
        },
        {
          "lhs": "AQS[1,2]",
          "rhs": "0.1"
        },
        {
          "lhs": "AQS[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "AQS[2,1]",
          "rhs": "-0.1"
        },
        {
          "lhs": "AQS[2,2]",
          "rhs": "0."
        },
        {
          "lhs": "AQS[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "AQS[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "AQS[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "AQS[3,3]",
          "rhs": "0."
        }
      ],
      "tex": "Subsuperscript[A,RS,Q]",
      "description": "Colored scalar resonance couplings to down-type quarks"
    },
    {
      "name": "BQS",
      "parameter_type": "External",
      "complex": false,
      "block_name": "BQS",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "BQS[_,_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[B,RS,Q]",
      "description": "Colored scalar pseudoscalar couplings to down-type quarks"
    },
    {
      "name": "tAQS",
      "parameter_type": "External",
      "complex": false,
      "block_name": "tAQS",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "tAQS[1,1]",
          "rhs": "0."
        },
        {
          "lhs": "tAQS[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "tAQS[1,3]",
          "rhs": "0.1"
        },
        {
          "lhs": "tAQS[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "tAQS[2,2]",
          "rhs": "0."
        },
        {
          "lhs": "tAQS[2,3]",
          "rhs": "0.1"
        },
        {
          "lhs": "tAQS[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "tAQS[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "tAQS[3,3]",
          "rhs": "0."
        }
      ],
      "tex": "Subsuperscript[tA,RS,Q]",
      "description": "Additional scalar four-fermion couplings to d-u"
    },
    {
      "name": "tBQS",
      "parameter_type": "External",
      "complex": false,
      "block_name": "tBQS",
      "interaction_order": [
        "MT3",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "tBQS[_,_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[tB,RS,Q]",
      "description": "Additional scalar four-fermion axial couplings to d-u"
    },
    {
      "name": "A12V",
      "parameter_type": "External",
      "complex": false,
      "block_name": "A12V",
      "interaction_order": [
        "MT4",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "A12V[1]",
          "rhs": "0."
        },
        {
          "lhs": "A12V[2]",
          "rhs": "0."
        },
        {
          "lhs": "A12V[3]",
          "rhs": "0.1"
        }
      ],
      "tex": "Subsuperscript[A,V,12]",
      "description": "Colored vector resonance couplings to quark-FMET"
    },
    {
      "name": "B12V",
      "parameter_type": "External",
      "complex": false,
      "block_name": "B12V",
      "interaction_order": [
        "MT4",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "B12V[_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[B,V,12]",
      "description": "Colored vector axial couplings to quark-FMET"
    },
    {
      "name": "AQV",
      "parameter_type": "External",
      "complex": false,
      "block_name": "AQV",
      "interaction_order": [
        "MT4",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "AQV[1,1]",
          "rhs": "0.1"
        },
        {
          "lhs": "AQV[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[2,2]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "AQV[3,3]",
          "rhs": "0."
        }
      ],
      "tex": "Subsuperscript[A,RV,Q]",
      "description": "Colored vector resonance couplings to down-type quarks"
    },
    {
      "name": "BQV",
      "parameter_type": "External",
      "complex": false,
      "block_name": "BQV",
      "interaction_order": [
        "MT4",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "BQV[_,_]",
          "rhs": "0"
        }
      ],
      "tex": "Subsuperscript[B,RV,Q]",
      "description": "Colored vector axial couplings to down-type quarks"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "FMET",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MFM",
        "value": "50"
      },
      "width": {
        "sym": "WFM",
        "value": "10"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "SU2": "1",
        "ColourRep": "1"
      },
      "pdg": 9000003,
      "particle_name": "fmet",
      "full_name": "Invisible Majorana fermion",
      "propagator_label": "FMET",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 7,
      "class_name": "VMET",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MVM",
        "value": "50."
      },
      "width": {
        "sym": "WVM",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "SU2": "1",
        "ColourRep": "1"
      },
      "pdg": 9000002,
      "particle_name": "vmet",
      "full_name": "Invisible neutral vector",
      "propagator_label": "VMET",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 8,
      "class_name": "VC",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MVC",
        "value": "500"
      },
      "width": {
        "sym": "WVC",
        "value": "10"
      },
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "2/3",
        "SU2": "1",
        "ColourRep": "3"
      },
      "pdg": 9000005,
      "particle_name": "vc",
      "antiparticle_name": "vc~",
      "full_name": "Colored vector monotop resonance",
      "propagator_label": "VC",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "SMET",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MSM",
        "value": "50"
      },
      "width": {
        "sym": "WSM",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "SU2": "1",
        "ColourRep": "1"
      },
      "pdg": 9000001,
      "particle_name": "smet",
      "full_name": "Invisible neutral scalar",
      "propagator_label": "SMET",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "phiC",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MSC",
        "value": "1000"
      },
      "width": {
        "sym": "WSC",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "2/3",
        "SU2": "1",
        "ColourRep": "3"
      },
      "pdg": 9000004,
      "particle_name": "phic",
      "antiparticle_name": "phic~",
      "full_name": "Colored scalar monotop resonance",
      "propagator_label": "phiC",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 6,
      "class_name": "tphiC",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "tMSC",
        "value": "1000"
      },
      "width": {
        "sym": "tWSC",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "-1/3",
        "Y": "-1/3",
        "SU2": "1",
        "ColourRep": "3"
      },
      "pdg": 9000006,
      "particle_name": "tphic",
      "antiparticle_name": "tphic~",
      "full_name": "Additional colored scalar four-fermion mediator",
      "propagator_label": "tphiC",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LMono",
      "expression": "Module[{L0,L1,L120,L121,L120p,sp,sp1,sp2,f1,f2,c1,c2,c3,mu}, L0 := SMET (uqbar[sp1,f1,c1].uq[sp1,f2,c1] A0FC[f1,f2] + uqbar[sp1,f1,c1].Ga[5,sp1,sp2].uq[sp2,f2,c1] B0FC[f1,f2]); L1 := VMET[mu] (uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].uq[sp2,f2,c1] A1FC[f1,f2] + uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].Ga[5,sp2,sp].uq[sp,f2,c1] B1FC[f1,f2]); L120 := phiC[c3] Eps[c1,c2,c3] (CC[dqbar][sp1,f1,c1].dq[sp1,f2,c2] AQS[f1,f2] + CC[dqbar][sp1,f1,c1].Ga[5,sp1,sp2].dq[sp2,f2,c2] BQS[f1,f2]) + phiC[c1] (uqbar[sp1,f1,c1].FMET[sp1] A12S[f1] + uqbar[sp1,f1,c1].Ga[5,sp1,sp2].FMET[sp2] B12S[f1]); L120p := tphiC[c3] Eps[c1,c2,c3] (CC[dqbar][sp1,f1,c1].uq[sp1,f2,c2] tAQS[f1,f2] + CC[dqbar][sp1,f1,c1].Ga[5,sp1,sp2].uq[sp2,f2,c2] tBQS[f1,f2]) + tphiC[c1] (dqbar[sp1,f1,c1].FMET[sp1] tA12S[f1] + dqbar[sp1,f1,c1].Ga[5,sp1,sp2].FMET[sp2] tB12S[f1]); L121 := VC[mu,c3] Eps[c1,c2,c3] (CC[dqbar][sp1,f1,c1].Ga[mu,sp1,sp2].dq[sp2,f2,c2] AQV[f1,f2] + CC[dqbar][sp1,f1,c1].Ga[mu,sp1,sp2].Ga[5,sp2,sp].dq[sp,f2,c2] BQV[f1,f2]) + VC[mu,c1] (uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].FMET[sp2] A12V[f1] + uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].Ga[5,sp2,sp].FMET[sp] B12V[f1]); L0 + L1 + L120 + L121 + $Flag4F*L120p + HC[L0 + L1 + L120 + L121 + $Flag4F*L120p]]",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "$Flag4F = 1;"
  ],
  "raw_blocks": []
}
```