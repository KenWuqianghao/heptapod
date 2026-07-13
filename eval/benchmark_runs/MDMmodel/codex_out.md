```json
{
  "model_name": "MDMmodel_gen",
  "info": {
    "authors": [
      "Junjie Cao",
      "Yangle He",
      "Peiwen Wu",
      "Mengchao Zhang",
      "Jingya Zhu"
    ],
    "version": "1.0",
    "date": "10 Jan 2014",
    "institutions": [
      "Henan Normal University",
      "Peking University",
      "Institute of Theoretical Physics, Academia Sinica"
    ],
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
    ]
  ],
  "feynman_gauge": true,
  "vevs": [
    [
      "Phi[2]",
      "vev"
    ],
    [
      "S",
      "vevf"
    ]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "eta",
      "parameter_type": "External",
      "value": "0.33",
      "block_name": "MDMINPUTS",
      "order_block": 1,
      "tex": "\\[Eta]",
      "description": "v/f for one T field in the Minimal Dilaton Model"
    },
    {
      "name": "ts",
      "parameter_type": "External",
      "value": "-0.23",
      "block_name": "MDMINPUTS",
      "order_block": 2,
      "tex": "Subscript[tan\\[Theta],S]",
      "description": "tangent of scalar mixing angle theta_S"
    },
    {
      "name": "sl",
      "parameter_type": "External",
      "value": "0.12",
      "block_name": "MDMINPUTS",
      "order_block": 3,
      "tex": "Subscript[sin\\[Theta],L]",
      "description": "sine of left-handed top-partner mixing angle theta_L"
    },
    {
      "name": "MsDM",
      "parameter_type": "External",
      "value": "173.2",
      "block_name": "MASS",
      "order_block": 6000011,
      "description": "dilaton mass"
    },
    {
      "name": "MTP",
      "parameter_type": "External",
      "value": "1670.3",
      "block_name": "MASS",
      "order_block": 6000001,
      "description": "top-partner mass"
    },
    {
      "name": "WsDM",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DECAY",
      "order_block": 6000011,
      "description": "dilaton width"
    },
    {
      "name": "WTP",
      "parameter_type": "External",
      "value": "37.8",
      "block_name": "DECAY",
      "order_block": 6000001,
      "description": "top-partner width"
    },
    {
      "name": "vevf",
      "parameter_type": "Internal",
      "value": "vev/eta",
      "interaction_order": [
        "QED",
        -1
      ],
      "description": "dilaton vacuum expectation value f"
    },
    {
      "name": "ss",
      "parameter_type": "Internal",
      "value": "ts/Sqrt[1 + ts^2]",
      "tex": "Subscript[sin\\[Theta],S]",
      "description": "sine of scalar mixing angle"
    },
    {
      "name": "cs",
      "parameter_type": "Internal",
      "value": "1/Sqrt[1 + ts^2]",
      "tex": "Subscript[cos\\[Theta],S]",
      "description": "cosine of scalar mixing angle"
    },
    {
      "name": "cl",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - sl^2]",
      "tex": "Subscript[cos\\[Theta],L]",
      "description": "cosine of left-handed top-partner mixing angle"
    },
    {
      "name": "sr",
      "parameter_type": "Internal",
      "value": "MT sl/(MTP cl)",
      "tex": "Subscript[sin\\[Theta],R]",
      "description": "right-handed top-partner mixing angle in the mtp >> mt limit"
    },
    {
      "name": "cr",
      "parameter_type": "Internal",
      "value": "1",
      "tex": "Subscript[cos\\[Theta],R]",
      "description": "cosine of right-handed top-partner mixing angle"
    },
    {
      "name": "dkappa",
      "parameter_type": "Internal",
      "value": "Abs[Mh^2 - MsDM^2]/vev^2 Abs[eta ts]/(1 + ts^2)",
      "interaction_order": [
        "QED",
        2
      ],
      "tex": "\\[Kappa]",
      "description": "S^2 |H|^2 scalar portal coupling"
    },
    {
      "name": "dlamh",
      "parameter_type": "Internal",
      "value": "Abs[Mh^2 - MsDM^2]/vev^2 (Abs[(Mh^2 + MsDM^2)/(Mh^2 - MsDM^2)] + Abs[2 cs ss]/(2 cs ss) (cs^2 - ss^2))",
      "interaction_order": [
        "QED",
        2
      ],
      "tex": "Subscript[\\[Lambda],H]",
      "description": "Higgs quartic coupling in the MDM potential"
    },
    {
      "name": "dlams",
      "parameter_type": "Internal",
      "value": "3 Abs[Mh^2 - MsDM^2]/(2 vevf^2) (Abs[(Mh^2 + MsDM^2)/(Mh^2 - MsDM^2)] - Abs[2 cs ss]/(2 cs ss) (cs^2 - ss^2))",
      "interaction_order": [
        "QED",
        2
      ],
      "tex": "Subscript[\\[Lambda],S]",
      "description": "dilaton quartic coupling"
    },
    {
      "name": "muS2",
      "parameter_type": "Internal",
      "value": "-dlams/6 vevf^2 - dkappa vev^2/2",
      "tex": "Superscript[Subscript[m,S],2]",
      "description": "quadratic S potential coefficient"
    },
    {
      "name": "muH2",
      "parameter_type": "Internal",
      "value": "-dkappa vevf^2/2 - dlamh vev^2/4",
      "tex": "Superscript[Subscript[m,H],2]",
      "description": "quadratic Higgs potential coefficient"
    },
    {
      "name": "yp",
      "parameter_type": "Internal",
      "value": "Sqrt[2]/vev MTP sl",
      "interaction_order": [
        "QED",
        1
      ],
      "parameter_name": "yp",
      "tex": "Superscript[y,\\[Prime]]",
      "description": "Yukawa coupling y' between T_R and q3L.H"
    },
    {
      "name": "Mdltn",
      "parameter_type": "Internal",
      "value": "MTP cl",
      "description": "coefficient M in the dilaton-top-partner mass term"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 1,
      "class_name": "h",
      "self_conjugate": true,
      "mass": {
        "sym": "Mh",
        "value": "125.6"
      },
      "width": {
        "sym": "Wh",
        "value": "0.00407"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 25,
      "particle_name": "h",
      "full_name": "SM-like Higgs mass eigenstate",
      "propagator_label": "h",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 21,
      "class_name": "sDM",
      "self_conjugate": true,
      "mass": {
        "sym": "MsDM",
        "value": "173.2"
      },
      "width": {
        "sym": "WsDM",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 6000011,
      "particle_name": "sDM",
      "full_name": "dilaton",
      "propagator_label": "sDM",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 7,
      "class_name": "tp",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MTP",
        "value": "1670.3"
      },
      "width": {
        "sym": "WTP",
        "value": "37.8"
      },
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "2/3"
      },
      "pdg": 6000001,
      "particle_name": "tp",
      "antiparticle_name": "tp~",
      "full_name": "top partner",
      "propagator_label": "tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 31,
      "class_name": "S",
      "self_conjugate": true,
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "unphysical": true,
      "definitions": [
        "S -> vevf + h ss + sDM cs"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 11,
      "class_name": "Phi",
      "self_conjugate": false,
      "indices": [
        "SU2D"
      ],
      "flavor_index": "SU2D",
      "quantum_numbers": {
        "Y": "1/2"
      },
      "unphysical": true,
      "definitions": [
        "Phi[1] -> -I GP",
        "Phi[2] -> (vev + h cs - sDM ss + I G0)/Sqrt[2]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 26,
      "class_name": "TR",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "quantum_numbers": {
        "Y": "2/3",
        "Q": "2/3"
      },
      "unphysical": true,
      "definitions": [
        "TR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] (-sr t[sp2, cc] + cr tp[sp2, cc])]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 27,
      "class_name": "TL",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "quantum_numbers": {
        "Y": "2/3",
        "Q": "2/3"
      },
      "unphysical": true,
      "definitions": [
        "TL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] (-sl t[sp2, cc] + cl tp[sp2, cc])]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LFermionsDM",
      "expression": "Block[{mu, sp, cc}, ExpandIndices[I TLbar.Ga[mu].DC[TL, mu] + I TLbar.Ga[mu].DC[TR, mu] + I TRbar.Ga[mu].DC[TL, mu] + I TRbar.Ga[mu].DC[TR, mu] - Mdltn/vevf S (TLbar[sp, cc].TL[sp, cc] + TLbar[sp, cc].TR[sp, cc] + TRbar[sp, cc].TL[sp, cc] + TRbar[sp, cc].TR[sp, cc]), FlavorExpand -> {SU2W, SU2D}]/.{CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}]",
      "delayed": true
    },
    {
      "name": "LHiggsMDM",
      "expression": "Block[{ii, jj, mu, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 | GP | GPbar -> 0}, {}]; ExpandIndices[DC[Phibar[ii], mu] DC[Phi[ii], mu] - 1/2 del[S, mu] del[S, mu] - muS2/2 S^2 - dlams/24 S^4 - dkappa/2 S^2 Phibar[ii] Phi[ii] - muH2 Phibar[ii] Phi[ii] - dlamh/4 Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand -> {SU2D, SU2W}]/.feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LYukawaDM",
      "expression": "Block[{sp, ii, jj, cc, ff1, ff2, ff3, yuk, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 | GP | GPbar -> 0}, {}]; yuk = ExpandIndices[-yp QLb[sp, ii, 3, cc].TR[sp, cc] Phibar[jj] Eps[ii, jj] - Conjugate[yp] TRbar[sp, cc].QL[sp, ii, 3, cc] Phi[jj] Conjugate[Eps[ii, jj]], FlavorExpand -> SU2D]; yuk = yuk /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}; yuk/.feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LMDMNP",
      "expression": "LFermionsDM + LHiggsMDM + LYukawaDM",
      "delayed": true
    }
  ]
}
```