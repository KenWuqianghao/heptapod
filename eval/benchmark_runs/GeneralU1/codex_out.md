```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": [
      "Arindam Das",
      "P. S. Bhupal Dev",
      "Yutaka Hosotani",
      "Sanjoy Mandal"
    ],
    "version": "1.0",
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
      3
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [
    [
      "PhiX[]",
      "vPhi/Sqrt[2]"
    ]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "GENERALU1",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gX",
      "tex": "g_X",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "GENERALU1",
      "order_block": 2,
      "parameter_name": "xH",
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet direction"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "GENERALU1",
      "order_block": 3,
      "parameter_name": "xPhi",
      "tex": "x_\\Phi",
      "description": "U(1)X charge normalization parameter"
    },
    {
      "name": "MZp",
      "parameter_type": "External",
      "value": "7500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 32,
      "parameter_name": "MZp",
      "tex": "M_{Z'}",
      "description": "Zprime mass"
    },
    {
      "name": "WZp",
      "parameter_type": "External",
      "value": "10.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 32,
      "parameter_name": "WZp",
      "tex": "\\Gamma_{Z'}",
      "description": "Zprime width"
    },
    {
      "name": "mPhiX",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000001,
      "parameter_name": "mPhiX",
      "tex": "m_\\phi",
      "description": "Physical U(1)X Higgs scalar mass"
    },
    {
      "name": "WPhiX",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9000001,
      "parameter_name": "WPhiX",
      "tex": "\\Gamma_\\phi",
      "description": "Physical U(1)X Higgs scalar width"
    },
    {
      "name": "mN1",
      "parameter_type": "External",
      "value": "10000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900012,
      "parameter_name": "mN1",
      "tex": "m_{N_1}",
      "description": "Heavy right-handed neutrino N1 mass"
    },
    {
      "name": "mN2",
      "parameter_type": "External",
      "value": "10000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900014,
      "parameter_name": "mN2",
      "tex": "m_{N_2}",
      "description": "Heavy right-handed neutrino N2 mass"
    },
    {
      "name": "mN3",
      "parameter_type": "External",
      "value": "10000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9900016,
      "parameter_name": "mN3",
      "tex": "m_{N_3}",
      "description": "Heavy right-handed neutrino N3 mass"
    },
    {
      "name": "WN1",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900012,
      "parameter_name": "WN1",
      "tex": "\\Gamma_{N_1}",
      "description": "Heavy right-handed neutrino N1 width"
    },
    {
      "name": "WN2",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900014,
      "parameter_name": "WN2",
      "tex": "\\Gamma_{N_2}",
      "description": "Heavy right-handed neutrino N2 width"
    },
    {
      "name": "WN3",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9900016,
      "parameter_name": "WN3",
      "tex": "\\Gamma_{N_3}",
      "description": "Heavy right-handed neutrino N3 width"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "GENERALU1",
      "order_block": 4,
      "parameter_name": "lamPhi",
      "tex": "\\lambda_\\Phi",
      "description": "Singlet scalar quartic coupling"
    },
    {
      "name": "lamHP",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "GENERALU1",
      "order_block": 5,
      "parameter_name": "lamHP",
      "tex": "\\lambda'",
      "description": "Higgs portal coupling lambda prime"
    },
    {
      "name": "mPhi2",
      "parameter_type": "External",
      "value": "1000000.",
      "complex": false,
      "block_name": "GENERALU1",
      "order_block": 6,
      "parameter_name": "mPhi2",
      "tex": "m_\\Phi^2",
      "description": "Quadratic singlet scalar potential parameter"
    },
    {
      "name": "vPhi",
      "parameter_type": "Internal",
      "value": "MZp/(2*gX)",
      "complex": false,
      "parameter_name": "vPhi",
      "tex": "v_\\Phi",
      "description": "U(1)X breaking vacuum expectation value in the vPhi >> vev approximation"
    },
    {
      "name": "qQLX",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "complex": false,
      "tex": "q^Q_X",
      "description": "U(1)X charge of left-handed quark doublets"
    },
    {
      "name": "qURX",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "complex": false,
      "tex": "q^u_X",
      "description": "U(1)X charge of right-handed up quarks"
    },
    {
      "name": "qDRX",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "complex": false,
      "tex": "q^d_X",
      "description": "U(1)X charge of right-handed down quarks"
    },
    {
      "name": "qLLX",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "complex": false,
      "tex": "q^L_X",
      "description": "U(1)X charge of left-handed lepton doublets"
    },
    {
      "name": "qERX",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "complex": false,
      "tex": "q^e_X",
      "description": "U(1)X charge of right-handed charged leptons"
    },
    {
      "name": "qNRX",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "complex": false,
      "tex": "q^N_X",
      "description": "U(1)X charge of right-handed neutrinos"
    },
    {
      "name": "qHX",
      "parameter_type": "Internal",
      "value": "-xH/2",
      "complex": false,
      "tex": "q^H_X",
      "description": "U(1)X charge of the SM Higgs doublet"
    },
    {
      "name": "qPhiX",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "complex": false,
      "tex": "q^\\Phi_X",
      "description": "U(1)X charge of the singlet scalar Phi"
    },
    {
      "name": "yNu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "YNU",
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "yNu[i_,j_]",
          "rhs": "0."
        }
      ],
      "tex": "Y_\\nu",
      "description": "Dirac neutrino Yukawa matrix"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "complex": false,
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "yN[1]",
          "rhs": "Sqrt[2]*mN1/vPhi"
        },
        {
          "lhs": "yN[2]",
          "rhs": "Sqrt[2]*mN2/vPhi"
        },
        {
          "lhs": "yN[3]",
          "rhs": "Sqrt[2]*mN3/vPhi"
        }
      ],
      "tex": "Y_N",
      "description": "Diagonal Majorana Yukawa couplings of right-handed neutrinos"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MZp",
        "value": "7500."
      },
      "width": {
        "sym": "WZp",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1"
      },
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
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
        "sym": "mN",
        "members": [
          [
            "mN1",
            "10000."
          ],
          [
            "mN2",
            "10000."
          ],
          [
            "mN3",
            "10000."
          ]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          [
            "WN1",
            "1."
          ],
          [
            "WN2",
            "1."
          ],
          [
            "WN3",
            "1."
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1",
        "X": "-xPhi"
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
        "RH neutrino 1",
        "RH neutrino 2",
        "RH neutrino 3"
      ],
      "propagator_label": [
        "N1",
        "N2",
        "N3"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "False"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "phiX",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "mPhiX",
        "value": "1000."
      },
      "width": {
        "sym": "WPhiX",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1"
      },
      "pdg": 9000001,
      "particle_name": "phiX",
      "full_name": "U1X Higgs scalar",
      "propagator_label": "phiX",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "GZp",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MZp",
        "value": "7500."
      },
      "width": {
        "sym": "WZp",
        "value": "10."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1"
      },
      "pdg": 9000002,
      "particle_name": "GZp",
      "full_name": "Zprime Goldstone",
      "propagator_label": "GZp",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "goldstone": "Zp"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "PhiX",
      "self_conjugate": false,
      "indices": [],
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1",
        "X": "2*xPhi"
      },
      "unphysical": true,
      "definitions": [
        "PhiX[] -> (vPhi + phiX + I GZp)/Sqrt[2]"
      ]
    }
  ],
  "gauge_xi": [
    [
      "V[100]",
      "GaugeXi[Zp]"
    ]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpF",
      "expression": "Block[{ff,sp1,sp2,sp3,mu,cc}, -gX Zp[mu] (qQLX uqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjM[sp2,sp3].uq[sp3,ff,cc] + qQLX dqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjM[sp2,sp3].dq[sp3,ff,cc] + qURX uqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].uq[sp3,ff,cc] + qDRX dqbar[sp1,ff,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].dq[sp3,ff,cc] + qLLX vlbar[sp1,ff].Ga[mu,sp1,sp2].ProjM[sp2,sp3].vl[sp3,ff] + qLLX lbar[sp1,ff].Ga[mu,sp1,sp2].ProjM[sp2,sp3].l[sp3,ff] + qERX lbar[sp1,ff].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,ff] + qNRX Nbar[sp1,ff].Ga[mu,sp1,sp2].ProjP[sp2,sp3].N[sp3,ff]))]",
      "delayed": true
    },
    {
      "name": "LPhiXKin",
      "expression": "Block[{mu}, del[PhiXbar[],mu] del[PhiX[],mu] + I*gX*qPhiX*Zp[mu]*(PhiXbar[] del[PhiX[],mu] - del[PhiXbar[],mu] PhiX[]) + gX^2*qPhiX^2 Zp[mu] Zp[mu] PhiXbar[] PhiX[]]",
      "delayed": true
    },
    {
      "name": "LHiggsX",
      "expression": "Block[{ii,mu}, ExpandIndices[I*gX*qHX*Zp[mu]*(Phibar[ii] DC[Phi[ii],mu] - DC[Phibar[ii],mu] Phi[ii]) + gX^2*qHX^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand->{SU2D,SU2W}]]",
      "delayed": true
    },
    {
      "name": "VPhiX",
      "expression": "Block[{ii}, ExpandIndices[mPhi2 PhiXbar[] PhiX[] + lamPhi (PhiXbar[] PhiX[])^2 + lamHP (Phibar[ii] Phi[ii]) (PhiXbar[] PhiX[]), FlavorExpand->{SU2D,SU2W}]]",
      "delayed": true
    },
    {
      "name": "LNuDiracYuk",
      "expression": "Block[{ff1,ff2,ii,sp1,sp2}, ExpandIndices[-yNu[ff1,ff2] LLbar[sp1,ii,ff1].ProjP[sp1,sp2].N[sp2,ff2] Phibar[ii], FlavorExpand->SU2D]]",
      "delayed": true
    },
    {
      "name": "LNuMajoranaYuk",
      "expression": "Block[{ff,sp1,sp2}, -1/2 yN[ff] PhiX[] Nbar[sp1,ff].ProjP[sp1,sp2].N[sp2,ff] - 1/2 yN[ff] PhiXbar[] Nbar[sp1,ff].ProjM[sp1,sp2].N[sp2,ff]]",
      "delayed": true
    },
    {
      "name": "LGeneralU1",
      "expression": "LZpF + LPhiXKin + LHiggsX - VPhiX + LNuDiracYuk + HC[LNuDiracYuk] + LNuMajoranaYuk",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```