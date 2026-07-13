```json
{
  "model_name": "topBSM_gen",
  "info": {
    "authors": [
      "Stefan Krastanov"
    ],
    "version": "0.1",
    "date": "August 1, 2013",
    "institutions": [
      "ENS Lyon",
      "UCL Belgium"
    ],
    "emails": [
      "stefan.krastanov@ens-lyon.fr"
    ]
  },
  "interaction_order_hierarchy": [
    [
      "QS0",
      8
    ],
    [
      "QO0",
      8
    ],
    [
      "QS1",
      8
    ],
    [
      "QO1",
      8
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "s0scalar",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S0PARAMS",
      "interaction_order": [
        "QS0",
        1
      ],
      "parameter_name": "s0scalar",
      "tex": "Subscript[s0, scalar]",
      "description": "S0 scalar coupling"
    },
    {
      "name": "s0axial",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S0PARAMS",
      "interaction_order": [
        "QS0",
        1
      ],
      "parameter_name": "s0axial",
      "tex": "Subscript[s0, axial]",
      "description": "S0 axial coupling"
    },
    {
      "name": "s0fusionScalar",
      "parameter_type": "Internal",
      "interaction_order": [
        "QS0",
        1
      ],
      "definitions": [
        {
          "lhs": "s0fusionScalar",
          "rhs": "If[NumericalValue[MS0] > 2 NumericalValue[MT], -s0scalar gs^2/(12 Pi^2 vev) sertHeavy[(2 MT/MS0)^2], -s0scalar gs^2/(12 Pi^2 vev) sertLight[(2 MT/MS0)^2]]",
          "delayed": true
        }
      ],
      "tex": "Subscript[s0, fusionScalar]",
      "description": "S0 effective coupling due to gluon fusion, scalar"
    },
    {
      "name": "s0fusionAxial",
      "parameter_type": "Internal",
      "interaction_order": [
        "QS0",
        1
      ],
      "definitions": [
        {
          "lhs": "s0fusionAxial",
          "rhs": "If[NumericalValue[MS0] > 2 NumericalValue[MT], -s0axial gs^2/(8 Pi^2 vev) serpHeavy[(2 MT/MS0)^2], -s0axial gs^2/(8 Pi^2 vev) serpLight[(2 MT/MS0)^2]]",
          "delayed": true
        }
      ],
      "tex": "Subscript[s0, fusionAxial]",
      "description": "S0 effective coupling due to gluon fusion, axial"
    },
    {
      "name": "WS0",
      "parameter_type": "Internal",
      "definitions": [
        {
          "lhs": "WS0",
          "rhs": "If[NumericalValue[MS0] > 2 NumericalValue[MT], (3 MT^2 Sqrt[MS0^4 - 4 MS0^2 MT^2] (-4 MT^2 s0scalar^2 + MS0^2 (s0axial^2 + s0scalar^2)))/(8 Pi vev^2 MS0^3) + (MS0^3 Abs[s0fusionScalar]^2)/(8 Pi), (MS0^3 Abs[s0fusionScalar]^2)/(8 Pi)]",
          "delayed": true
        }
      ],
      "description": "S0 width"
    },
    {
      "name": "o0scalar",
      "parameter_type": "External",
      "value": "1",
      "block_name": "O0PARAMS",
      "interaction_order": [
        "QO0",
        1
      ],
      "parameter_name": "o0scalar",
      "tex": "Subscript[o0, scalar]",
      "description": "O0 scalar coupling"
    },
    {
      "name": "o0axial",
      "parameter_type": "External",
      "value": "1",
      "block_name": "O0PARAMS",
      "interaction_order": [
        "QO0",
        1
      ],
      "parameter_name": "o0axial",
      "tex": "Subscript[o0, axial]",
      "description": "O0 axial coupling"
    },
    {
      "name": "o0fusionScalar",
      "parameter_type": "Internal",
      "interaction_order": [
        "QO0",
        1
      ],
      "definitions": [
        {
          "lhs": "o0fusionScalar",
          "rhs": "If[NumericalValue[MO0] > 2 NumericalValue[MT], -o0scalar gs^2/(12 Pi^2 vev) sertHeavy[(2 MT/MO0)^2], -o0scalar gs^2/(12 Pi^2 vev) sertLight[(2 MT/MO0)^2]]",
          "delayed": true
        }
      ],
      "tex": "Subscript[o0, fusionScalar]",
      "description": "O0 effective coupling due to gluon fusion, scalar"
    },
    {
      "name": "o0fusionAxial",
      "parameter_type": "Internal",
      "interaction_order": [
        "QO0",
        1
      ],
      "definitions": [
        {
          "lhs": "o0fusionAxial",
          "rhs": "If[NumericalValue[MO0] > 2 NumericalValue[MT], -o0axial gs^2/(8 Pi^2 vev) serpHeavy[(2 MT/MO0)^2], -o0axial gs^2/(8 Pi^2 vev) serpLight[(2 MT/MO0)^2]]",
          "delayed": true
        }
      ],
      "tex": "Subscript[o0, fusionAxial]",
      "description": "O0 effective coupling due to gluon fusion, axial"
    },
    {
      "name": "WO0",
      "parameter_type": "Internal",
      "definitions": [
        {
          "lhs": "WO0",
          "rhs": "If[NumericalValue[MO0] > 2 NumericalValue[MT], 1/6 (3 MT^2 Sqrt[MO0^4 - 4 MO0^2 MT^2] (-4 MT^2 o0scalar^2 + MO0^2 (o0axial^2 + o0scalar^2)))/(8 Pi vev^2 MO0^3) + 1/64 (MO0^3 Abs[o0fusionScalar]^2)/(8 Pi), 1/64 (MO0^3 Abs[o0fusionScalar]^2)/(8 Pi)]",
          "delayed": true
        }
      ],
      "description": "O0 width"
    },
    {
      "name": "s1uright",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1uright",
      "tex": "Subscript[s1, ur]",
      "description": "S1 right up quark coupling"
    },
    {
      "name": "s1uleft",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1uleft",
      "tex": "Subscript[s1, ul]",
      "description": "S1 left up quark coupling"
    },
    {
      "name": "s1dright",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1dright",
      "tex": "Subscript[s1, dr]",
      "description": "S1 right down quark coupling"
    },
    {
      "name": "s1dleft",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1dleft",
      "tex": "Subscript[s1, dl]",
      "description": "S1 left down quark coupling"
    },
    {
      "name": "s1eright",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1eright",
      "tex": "Subscript[s1, er]",
      "description": "S1 right electron coupling"
    },
    {
      "name": "s1eleft",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1eleft",
      "tex": "Subscript[s1, el]",
      "description": "S1 left electron coupling"
    },
    {
      "name": "s1nu",
      "parameter_type": "External",
      "value": "1",
      "block_name": "S1PARAMS",
      "interaction_order": [
        "QS1",
        1
      ],
      "parameter_name": "s1nu",
      "tex": "Subscript[s1, v]",
      "description": "S1 neutrino coupling"
    },
    {
      "name": "WS1",
      "parameter_type": "Internal",
      "definitions": [
        {
          "lhs": "WS1",
          "rhs": "1/(288*cw^2*Pi*sw^2*MS1^3)*ee^2*(+9*MS1^4*s1nu^2 +2*MS1^4*(16*s1uright^2*sw^4 + s1uleft^2*(3 - 4*sw^2)^2) +6*MS1^4*(4*s1eright^2*sw^4 + s1eleft^2*(1 - 2*sw^2)^2) +2*MS1^4*(4*s1dright^2*sw^4 + s1dleft^2*(3 - 2*sw^2)^2) +Sqrt[MS1^4 - 4*MS1^2*MT^2]*(+MT^2*(-9*s1uleft^2 +24*s1uleft*(s1uleft - 3*s1uright)*sw^2 -16*(s1uleft^2 - 6*s1uleft*s1uright + s1uright^2)*sw^4) +MS1^2*(16*s1uright^2*sw^4 + s1uleft^2*(3 - 4*sw^2)^2)) +3*Sqrt[MS1^4 - 4*MS1^2*MTA^2]*(-MTA^2*(+s1eleft^2 -4*s1eleft*(s1eleft - 3*s1eright)*sw^2 +4*(s1eleft^2 - 6*s1eleft*s1eright + s1eright^2)*sw^4) +MS1^2*(4*s1eright^2*sw^4 + s1eleft^2*(1 - 2*sw^2)^2)) +Sqrt[-4*MB^2*MS1^2 + MS1^4]*(+MB^2*(-9*s1dleft^2 +12*s1dleft*(s1dleft - 3*s1dright)*sw^2 -4*(s1dleft^2 - 6*s1dleft*s1dright + s1dright^2)*sw^4) +MS1^2*(4*s1dright^2*sw^4 + s1dleft^2*(3 - 2*sw^2)^2)))",
          "delayed": false
        }
      ],
      "description": "S1 width"
    },
    {
      "name": "o1uright",
      "parameter_type": "External",
      "value": "1",
      "block_name": "O1PARAMS",
      "interaction_order": [
        "QO1",
        1
      ],
      "parameter_name": "o1uright",
      "tex": "Subscript[o1, ur]",
      "description": "O1 right up quark coupling"
    },
    {
      "name": "o1uleft",
      "parameter_type": "External",
      "value": "1",
      "block_name": "O1PARAMS",
      "interaction_order": [
        "QO1",
        1
      ],
      "parameter_name": "o1uleft",
      "tex": "Subscript[o1, ul]",
      "description": "O1 left up quark coupling"
    },
    {
      "name": "o1dright",
      "parameter_type": "External",
      "value": "1",
      "block_name": "O1PARAMS",
      "interaction_order": [
        "QO1",
        1
      ],
      "parameter_name": "o1dright",
      "tex": "Subscript[o1, dr]",
      "description": "O1 right down quark coupling"
    },
    {
      "name": "o1dleft",
      "parameter_type": "External",
      "value": "1",
      "block_name": "O1PARAMS",
      "interaction_order": [
        "QO1",
        1
      ],
      "parameter_name": "o1dleft",
      "tex": "Subscript[o1, dl]",
      "description": "O1 left down quark coupling"
    },
    {
      "name": "WO1",
      "parameter_type": "Internal",
      "definitions": [
        {
          "lhs": "WO1",
          "rhs": "(gs^2/(48*Pi*MO1^3))*(+2*MO1^4*(o1dleft^2 + o1dright^2) +Sqrt[-4*MB^2*MO1^2 + MO1^4]*(MO1^2*(o1dleft^2 + o1dright^2) -MB^2*(o1dleft^2 - 6*o1dleft*o1dright + o1dright^2)) +2*MO1^4*(o1uleft^2 + o1uright^2) +Sqrt[MO1^4 - 4*MO1^2*MT^2]*(MO1^2*(o1uleft^2 + o1uright^2) -MT^2*(o1uleft^2 - 6*o1uleft*o1uright + o1uright^2)))",
          "delayed": false
        }
      ],
      "description": "O1 width"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 21,
      "class_name": "S0",
      "self_conjugate": true,
      "mass": {
        "sym": "MS0",
        "value": "400"
      },
      "width": {
        "sym": "WS0",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 6000045,
      "particle_name": "S0",
      "full_name": "S0",
      "propagator_label": "S0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 22,
      "class_name": "O0",
      "self_conjugate": true,
      "indices": [
        "Gluon"
      ],
      "mass": {
        "sym": "MO0",
        "value": "400"
      },
      "width": {
        "sym": "WO0",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 6000046,
      "particle_name": "O0",
      "full_name": "O0",
      "propagator_label": "O0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 7,
      "class_name": "S1",
      "self_conjugate": true,
      "mass": {
        "sym": "MS1",
        "value": "2000"
      },
      "width": {
        "sym": "WS1",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 6000047,
      "particle_name": "S1",
      "full_name": "S1",
      "propagator_label": "S1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 8,
      "class_name": "O1",
      "self_conjugate": true,
      "indices": [
        "Gluon"
      ],
      "mass": {
        "sym": "MO1",
        "value": "2000"
      },
      "width": {
        "sym": "WO1",
        "value": "Internal"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 6000048,
      "particle_name": "O1",
      "full_name": "O1",
      "propagator_label": "O1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "T",
      "class_index": 1,
      "class_name": "S2",
      "self_conjugate": true,
      "mass": {
        "sym": "MS2",
        "value": "500"
      },
      "width": {
        "sym": "WS2",
        "value": "2"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 6000049,
      "particle_name": "S2",
      "full_name": "S2",
      "propagator_label": "S2"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LS0top",
      "expression": "s0scalar MT/vev S0 tbar.t + I s0axial MT/vev S0 tbar.Ga[5].t"
    },
    {
      "name": "LS0ggfusionScalar",
      "expression": "-1/4 s0fusionScalar S0 FS[G,mu,nu,aa] FS[G,mu,nu,aa]"
    },
    {
      "name": "LS0ggfusionAxial",
      "expression": "-1/4 s0fusionAxial S0 FS[G,mu,nu,aa] Dual[FS][G,mu,nu,aa]"
    },
    {
      "name": "LS0ggfusion",
      "expression": "LS0ggfusionScalar + LS0ggfusionAxial"
    },
    {
      "name": "LS0",
      "expression": "LS0top + LS0ggfusion"
    },
    {
      "name": "LO0top",
      "expression": "o0scalar MT/vev tbar.T[a].t O0[a] + I o0axial MT/vev tbar.Ga[5].T[a].t O0[a]"
    },
    {
      "name": "LO0ggfusionScalar",
      "expression": "-1/4 o0fusionScalar dSUN[aa,bb,cc] O0[aa] FS[G,mu,nu,bb] FS[G,mu,nu,cc]"
    },
    {
      "name": "LO0ggfusionAxial",
      "expression": "-1/4 o0fusionAxial dSUN[aa,bb,cc] O0[aa] FS[G,mu,nu,bb] Dual[FS][G,mu,nu,cc]"
    },
    {
      "name": "LO0ggfusion",
      "expression": "LO0ggfusionScalar + LO0ggfusionAxial"
    },
    {
      "name": "LO0",
      "expression": "LO0top + LO0ggfusion"
    },
    {
      "name": "ez",
      "expression": "ee/(sw cw)"
    },
    {
      "name": "ey",
      "expression": "ee sw/cw"
    },
    {
      "name": "LS1ul",
      "expression": "- s1uleft S1[mu] QLbar[sp1,1,ff,cc] Ga[mu,sp1,sp2] QL[sp2,1,ff,cc] * ez (-1/2 + sw^2 2/3)"
    },
    {
      "name": "LS1dl",
      "expression": "- s1dleft S1[mu] QLbar[sp1,2,ff,cc] Ga[mu,sp1,sp2] QL[sp2,2,ff,cc] * ez (1/2 - sw^2/3)"
    },
    {
      "name": "LS1ur",
      "expression": "- s1uright S1[mu] uRbar.Ga[mu].uR * ey*2/3"
    },
    {
      "name": "LS1dr",
      "expression": "- s1dright S1[mu] dRbar.Ga[mu].dR * (-ey)/3"
    },
    {
      "name": "LS1el",
      "expression": "- s1eleft S1[mu] LLbar[sp1,2,ff] Ga[mu,sp1,sp2] LL[sp2,2,ff] * ez (1/2 - sw^2)"
    },
    {
      "name": "LS1nu",
      "expression": "- s1nu S1[mu] LLbar[sp1,1,ff] Ga[mu,sp1,sp2] LL[sp2,1,ff] * (-ez)/2"
    },
    {
      "name": "LS1er",
      "expression": "- s1eright S1[mu] lRbar.Ga[mu].lR * (-ey)"
    },
    {
      "name": "LS1",
      "expression": "LS1ul + LS1dl + LS1ur + LS1dr + LS1el + LS1er + LS1nu"
    },
    {
      "name": "LO1ul",
      "expression": "o1uleft gs O1[mu, a] QLbar[sp1,1,ff,cc1] Ga[mu,sp1,sp2] T[a,cc1,cc2] QL[sp2,1,ff,cc2]"
    },
    {
      "name": "LO1dl",
      "expression": "o1dleft gs O1[mu, a] QLbar[sp1,2,ff,cc1] Ga[mu,sp1,sp2] T[a,cc1,cc2] QL[sp2,2,ff,cc2]"
    },
    {
      "name": "LO1ur",
      "expression": "o1uright gs O1[mu, a] uRbar.Ga[mu].T[a].uR"
    },
    {
      "name": "LO1dr",
      "expression": "o1dright gs O1[mu, a] dRbar.Ga[mu].T[a].dR"
    },
    {
      "name": "LO1",
      "expression": "LO1ul + LO1dl + LO1ur + LO1dr"
    }
  ],
  "raw_preamble": [
    "sertLight[t_] := 3/2 t (1 + (1 - t) ArcSin[1/Sqrt[t]]^2);",
    "serpLight[t_] := t ArcSin[1/Sqrt[t]]^2;",
    "sertHeavy[t_] := 3/2 t (1 + 1/4 (t - 1) (Log[(Sqrt[1 - t] + 1)/(1 - Sqrt[1 - t])] - I Pi)^2);",
    "serpHeavy[t_] := -1/4 t (Log[(Sqrt[1 - t] + 1)/(1 - Sqrt[1 - t])] - I Pi)^2;",
    "bjzeros = Table[N[BesselJZero[1, x]], {x, 1, 10}]"
  ],
  "raw_blocks": []
}
```