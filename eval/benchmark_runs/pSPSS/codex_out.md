```json
{
  "model_name": "pSPSS_gen",
  "info": {
    "authors": [
      "Stefan Antusch",
      "Jan Hajer",
      "Johannes Rosskopp"
    ],
    "version": "1.0",
    "date": "2023-10-05",
    "institutions": [
      "Universitaet Basel",
      "Centro de Fisica Teorica de Particulas, Instituto Superior Tecnico"
    ],
    "emails": [
      "stefan.antusch@unibas.ch",
      "jan.hajer@tecnico.ulisboa.pt",
      "johannes.rosskopp@unibas.ch"
    ]
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
      "name": "Neutrino",
      "range_kind": "NoUnfold",
      "size": 5,
      "style_symbol": "n"
    },
    {
      "name": "HNL",
      "range_kind": "NoUnfold",
      "size": 2,
      "style_symbol": "N"
    }
  ],
  "parameters": [
    {
      "name": "Mmaj",
      "parameter_type": "External",
      "value": "1.000000e+02",
      "complex": false,
      "block_name": "PSPSS",
      "order_block": 1,
      "tex": "Subscript[m,M]",
      "description": "pSPSS heavy-neutrino Majorana mass parameter"
    },
    {
      "name": "deltaM",
      "parameter_type": "External",
      "value": "1.000000e-12",
      "complex": false,
      "block_name": "PSPSS",
      "order_block": 2,
      "tex": "\\[CapitalDelta]m",
      "description": "pSPSS heavy-neutrino mass splitting"
    },
    {
      "name": "theta1",
      "parameter_type": "External",
      "value": "0.000000e+00",
      "complex": false,
      "block_name": "PSPSS",
      "order_block": 3,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "Subscript[\\[Theta],e]",
      "description": "electron active-sterile mixing parameter"
    },
    {
      "name": "theta2",
      "parameter_type": "External",
      "value": "1.000000e-03",
      "complex": false,
      "block_name": "PSPSS",
      "order_block": 4,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "Subscript[\\[Theta],\\[Mu]]",
      "description": "muon active-sterile mixing parameter"
    },
    {
      "name": "theta3",
      "parameter_type": "External",
      "value": "0.000000e+00",
      "complex": false,
      "block_name": "PSPSS",
      "order_block": 5,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "Subscript[\\[Theta],\\[Tau]]",
      "description": "tau active-sterile mixing parameter"
    },
    {
      "name": "damping",
      "parameter_type": "External",
      "value": "0.000000e+00",
      "complex": false,
      "block_name": "PSPSS",
      "order_block": 6,
      "description": "pSPSS neutrino-antineutrino oscillation damping parameter"
    },
    {
      "name": "thetaSq",
      "parameter_type": "Internal",
      "value": "theta1^2 + theta2^2 + theta3^2",
      "complex": false,
      "description": "absolute square of active-sterile mixing vector"
    },
    {
      "name": "vevNP",
      "parameter_type": "Internal",
      "value": "vev",
      "complex": false,
      "interaction_order": [
        "NP",
        -1
      ],
      "description": "Higgs vev with NP interaction order"
    },
    {
      "name": "Mn4",
      "parameter_type": "Internal",
      "value": "Mmaj*(1 + thetaSq/2) - deltaM/2",
      "complex": false,
      "description": "pSPSS mass of n4"
    },
    {
      "name": "Mn5",
      "parameter_type": "Internal",
      "value": "Mmaj*(1 + thetaSq/2) + deltaM/2",
      "complex": false,
      "description": "pSPSS mass of n5"
    },
    {
      "name": "yvn",
      "parameter_type": "Internal",
      "indices": [
        "Generation"
      ],
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "value_rules": [
        {
          "lhs": "yvn[1]",
          "rhs": "Mmaj*theta1/vevNP"
        },
        {
          "lhs": "yvn[2]",
          "rhs": "Mmaj*theta2/vevNP"
        },
        {
          "lhs": "yvn[3]",
          "rhs": "Mmaj*theta3/vevNP"
        }
      ],
      "description": "sterile-neutrino Yukawa vector y_{alpha 1}"
    },
    {
      "name": "UnCL",
      "parameter_type": "Internal",
      "indices": [
        "Generation",
        "Neutrino"
      ],
      "complex": true,
      "value_rules": [
        {
          "lhs": "UnCL[1,1]",
          "rhs": "1 - theta1^2/2"
        },
        {
          "lhs": "UnCL[1,2]",
          "rhs": "-theta1*theta2/2"
        },
        {
          "lhs": "UnCL[1,3]",
          "rhs": "-theta1*theta3/2"
        },
        {
          "lhs": "UnCL[1,4]",
          "rhs": "-I*theta1/Sqrt[2]"
        },
        {
          "lhs": "UnCL[1,5]",
          "rhs": "theta1/Sqrt[2]"
        },
        {
          "lhs": "UnCL[2,1]",
          "rhs": "-theta2*theta1/2"
        },
        {
          "lhs": "UnCL[2,2]",
          "rhs": "1 - theta2^2/2"
        },
        {
          "lhs": "UnCL[2,3]",
          "rhs": "-theta2*theta3/2"
        },
        {
          "lhs": "UnCL[2,4]",
          "rhs": "-I*theta2/Sqrt[2]"
        },
        {
          "lhs": "UnCL[2,5]",
          "rhs": "theta2/Sqrt[2]"
        },
        {
          "lhs": "UnCL[3,1]",
          "rhs": "-theta3*theta1/2"
        },
        {
          "lhs": "UnCL[3,2]",
          "rhs": "-theta3*theta2/2"
        },
        {
          "lhs": "UnCL[3,3]",
          "rhs": "1 - theta3^2/2"
        },
        {
          "lhs": "UnCL[3,4]",
          "rhs": "-I*theta3/Sqrt[2]"
        },
        {
          "lhs": "UnCL[3,5]",
          "rhs": "theta3/Sqrt[2]"
        }
      ],
      "description": "upper 3 x 5 charged-lepton block of the pSPSS neutrino mixing matrix"
    },
    {
      "name": "Un",
      "parameter_type": "Internal",
      "indices": [
        "Neutrino",
        "Neutrino"
      ],
      "complex": true,
      "value_rules": [
        {
          "lhs": "Un[1,1]",
          "rhs": "1 - theta1^2/2"
        },
        {
          "lhs": "Un[1,2]",
          "rhs": "-theta1*theta2/2"
        },
        {
          "lhs": "Un[1,3]",
          "rhs": "-theta1*theta3/2"
        },
        {
          "lhs": "Un[1,4]",
          "rhs": "-I*theta1/Sqrt[2]"
        },
        {
          "lhs": "Un[1,5]",
          "rhs": "theta1/Sqrt[2]"
        },
        {
          "lhs": "Un[2,1]",
          "rhs": "-theta2*theta1/2"
        },
        {
          "lhs": "Un[2,2]",
          "rhs": "1 - theta2^2/2"
        },
        {
          "lhs": "Un[2,3]",
          "rhs": "-theta2*theta3/2"
        },
        {
          "lhs": "Un[2,4]",
          "rhs": "-I*theta2/Sqrt[2]"
        },
        {
          "lhs": "Un[2,5]",
          "rhs": "theta2/Sqrt[2]"
        },
        {
          "lhs": "Un[3,1]",
          "rhs": "-theta3*theta1/2"
        },
        {
          "lhs": "Un[3,2]",
          "rhs": "-theta3*theta2/2"
        },
        {
          "lhs": "Un[3,3]",
          "rhs": "1 - theta3^2/2"
        },
        {
          "lhs": "Un[3,4]",
          "rhs": "-I*theta3/Sqrt[2]"
        },
        {
          "lhs": "Un[3,5]",
          "rhs": "theta3/Sqrt[2]"
        },
        {
          "lhs": "Un[4,1]",
          "rhs": "0"
        },
        {
          "lhs": "Un[4,2]",
          "rhs": "0"
        },
        {
          "lhs": "Un[4,3]",
          "rhs": "0"
        },
        {
          "lhs": "Un[4,4]",
          "rhs": "I/Sqrt[2]"
        },
        {
          "lhs": "Un[4,5]",
          "rhs": "1/Sqrt[2]"
        },
        {
          "lhs": "Un[5,1]",
          "rhs": "-theta1"
        },
        {
          "lhs": "Un[5,2]",
          "rhs": "-theta2"
        },
        {
          "lhs": "Un[5,3]",
          "rhs": "-theta3"
        },
        {
          "lhs": "Un[5,4]",
          "rhs": "-I*(1 - thetaSq/2)/Sqrt[2]"
        },
        {
          "lhs": "Un[5,5]",
          "rhs": "(1 - thetaSq/2)/Sqrt[2]"
        }
      ],
      "description": "pSPSS neutrino mixing matrix through second order in theta"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "nH",
      "self_conjugate": true,
      "indices": [
        "HNL"
      ],
      "flavor_index": "HNL",
      "class_members": [
        "n4",
        "n5"
      ],
      "mass": {
        "sym": "MN",
        "members": [
          [
            "Mn4",
            "Internal"
          ],
          [
            "Mn5",
            "Internal"
          ]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          [
            "Wn4",
            "Automatic"
          ],
          [
            "Wn5",
            "Automatic"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": [
        9900012,
        9900014
      ],
      "particle_name": [
        "n4",
        "n5"
      ],
      "full_name": [
        "Heavy Majorana neutrino n4",
        "Heavy Majorana neutrino n5"
      ],
      "propagator_label": [
        "n4",
        "n5"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "W",
      "class_index": 100,
      "class_name": "N1L",
      "self_conjugate": false,
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "unphysical": true,
      "definitions": [
        "N1L[sp1_] :> Module[{nn}, Sum[Un[4, nn] nL[sp1, nn], {nn, 1, 5}]]"
      ],
      "chirality": "Left"
    },
    {
      "spin_type": "W",
      "class_index": 101,
      "class_name": "N2L",
      "self_conjugate": false,
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "unphysical": true,
      "definitions": [
        "N2L[sp1_] :> Module[{nn}, Sum[Un[5, nn] nL[sp1, nn], {nn, 1, 5}]]"
      ],
      "chirality": "Left"
    }
  ],
  "raw_blocks": [
    "RemoveHigherOrder[expr_] := Module[{eps}, Normal[Series[expr /. {theta1 -> eps theta1, theta2 -> eps theta2, theta3 -> eps theta3}, {eps, 0, 2}]] /. eps -> 1]",
    "PhiNP[i_] := Phi[i] /. vev -> vevNP",
    "PhiNPbar[i_] := Phibar[i] /. vev -> vevNP",
    "nL[sp_, 1] := vl[sp, 1]; nL[sp_, 2] := vl[sp, 2]; nL[sp_, 3] := vl[sp, 3]; nL[sp_, 4] := n4[sp]; nL[sp_, 5] := n5[sp]",
    "MR$Definitions = Join[MR$Definitions, {LL[sp1_, 1, ff_] :> Module[{sp2, nn}, ProjM[sp1, sp2] Sum[UnCL[ff, nn] nL[sp2, nn], {nn, 1, 5}]]}]"
  ],
  "lagrangian_terms": [
    {
      "name": "LKineticSterile",
      "expression": "Block[{mu}, I (N1Lbar.Ga[mu].del[N1L, mu] + N2Lbar.Ga[mu].del[N2L, mu])]",
      "delayed": false
    },
    {
      "name": "LNP",
      "expression": "Block[{sp1, ff1, ii, jj}, - Mmaj CC[N1Lbar[sp1]].N2L[sp1] + yvn[ff1] (CC[N1Lbar[sp1]].LL[sp1, ii, ff1] PhiNPbar[jj] Eps[ii, jj]) + HC[- Mmaj CC[N1Lbar[sp1]].N2L[sp1] + yvn[ff1] (CC[N1Lbar[sp1]].LL[sp1, ii, ff1] PhiNPbar[jj] Eps[ii, jj])]]",
      "delayed": false
    },
    {
      "name": "LpSPSS",
      "expression": "RemoveHigherOrder[LSM + LKineticSterile + LNP]",
      "delayed": false
    }
  ]
}
```