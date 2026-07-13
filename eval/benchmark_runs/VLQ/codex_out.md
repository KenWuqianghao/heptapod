```json
{
  "model_name": "VLQ_gen",
  "info": {
    "authors": [
      "J. Alwall",
      "R. Frederix",
      "J.-M. Gerard",
      "A. Giammanco",
      "M. Herquet",
      "S. Kalinin",
      "E. Kou",
      "V. Lemaitre",
      "F. Maltoni",
      "Codex extraction"
    ],
    "version": "1.0.0",
    "date": "2026-07-13",
    "institutions": [
      "CP3, Universite Catholique de Louvain"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "NP",
      1
    ]
  ],
  "interaction_order_limit": [
    [
      "NP",
      99
    ]
  ],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "thT",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "VLQINPUTS",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "thT",
      "tex": "\\theta_T",
      "description": "t-tprime mixing angle for the vector-like up-type singlet"
    },
    {
      "name": "MTP",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 6000006,
      "parameter_name": "MTP",
      "description": "vector-like up-type tprime mass"
    },
    {
      "name": "WTP",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 6000006,
      "parameter_name": "WTP",
      "description": "vector-like up-type tprime width"
    },
    {
      "name": "lamT",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLQYUKAWA",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "lamT",
      "tex": "\\lambda_T",
      "description": "SM top Yukawa coefficient in the tprime singlet weak-eigenstate Lagrangian"
    },
    {
      "name": "lamTp",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLQYUKAWA",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "lamTp",
      "tex": "\\lambda'_T",
      "description": "Yukawa coupling between the SM third-generation doublet and tprime_R^0"
    },
    {
      "name": "MT0",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "VLQMASSES",
      "order_block": 1,
      "parameter_name": "MT0",
      "description": "Dirac vector-like mass M for tprime_L^0 tprime_R^0"
    },
    {
      "name": "MTmix",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "VLQMASSES",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MTmix",
      "description": "Dirac mass mixing Mprime between tprime_L^0 and t_R^0"
    },
    {
      "name": "thB",
      "parameter_type": "External",
      "value": "0.01",
      "complex": false,
      "block_name": "VLQINPUTS",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "thB",
      "tex": "\\theta_B",
      "description": "b-bprime mixing angle for the analogous vector-like down-type singlet"
    },
    {
      "name": "MBP",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 6000007,
      "parameter_name": "MBP",
      "description": "vector-like down-type bprime mass"
    },
    {
      "name": "WBP",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 6000007,
      "parameter_name": "WBP",
      "description": "vector-like down-type bprime width"
    },
    {
      "name": "lamB",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLQYUKAWA",
      "order_block": 3,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "lamB",
      "tex": "\\lambda_B",
      "description": "bottom Yukawa coefficient in the bprime singlet weak-eigenstate Lagrangian"
    },
    {
      "name": "lamBp",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLQYUKAWA",
      "order_block": 4,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "lamBp",
      "tex": "\\lambda'_B",
      "description": "Yukawa coupling between the SM third-generation doublet and bprime_R^0"
    },
    {
      "name": "MB0",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "VLQMASSES",
      "order_block": 3,
      "parameter_name": "MB0",
      "description": "Dirac vector-like mass M for bprime_L^0 bprime_R^0"
    },
    {
      "name": "MBmix",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "VLQMASSES",
      "order_block": 4,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MBmix",
      "description": "Dirac mass mixing Mprime between bprime_L^0 and b_R^0"
    },
    {
      "name": "thU4",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "CKM4",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "thU4",
      "tex": "\\theta_u",
      "description": "fourth-generation 3-4 up-sector mixing angle"
    },
    {
      "name": "thV4",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "CKM4",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "thV4",
      "tex": "\\theta_v",
      "description": "fourth-generation 2-4 mixing angle"
    },
    {
      "name": "thW4",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "CKM4",
      "order_block": 3,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "thW4",
      "tex": "\\theta_w",
      "description": "fourth-generation 1-4 mixing angle"
    },
    {
      "name": "MT4",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 7000006,
      "parameter_name": "MT4",
      "description": "fourth-generation up-type quark mass"
    },
    {
      "name": "WT4",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 7000006,
      "parameter_name": "WT4",
      "description": "fourth-generation up-type quark width"
    },
    {
      "name": "MB4",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 7000007,
      "parameter_name": "MB4",
      "description": "fourth-generation down-type quark mass"
    },
    {
      "name": "WB4",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 7000007,
      "parameter_name": "WB4",
      "description": "fourth-generation down-type quark width"
    },
    {
      "name": "MN4",
      "parameter_type": "External",
      "value": "100.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 7000012,
      "parameter_name": "MN4",
      "description": "fourth-generation neutral lepton mass"
    },
    {
      "name": "WN4",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 7000012,
      "parameter_name": "WN4",
      "description": "fourth-generation neutral lepton width"
    },
    {
      "name": "ME4",
      "parameter_type": "External",
      "value": "100.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 7000011,
      "parameter_name": "ME4",
      "description": "fourth-generation charged lepton mass"
    },
    {
      "name": "WE4",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 7000011,
      "parameter_name": "WE4",
      "description": "fourth-generation charged lepton width"
    },
    {
      "name": "sT",
      "parameter_type": "Internal",
      "value": "Sin[thT]",
      "complex": false,
      "parameter_name": "sT",
      "description": "sine of vector-like t-tprime mixing angle"
    },
    {
      "name": "cT",
      "parameter_type": "Internal",
      "value": "Cos[thT]",
      "complex": false,
      "parameter_name": "cT",
      "description": "cosine of vector-like t-tprime mixing angle"
    },
    {
      "name": "sB",
      "parameter_type": "Internal",
      "value": "Sin[thB]",
      "complex": false,
      "parameter_name": "sB",
      "description": "sine of vector-like b-bprime mixing angle"
    },
    {
      "name": "cB",
      "parameter_type": "Internal",
      "value": "Cos[thB]",
      "complex": false,
      "parameter_name": "cB",
      "description": "cosine of vector-like b-bprime mixing angle"
    },
    {
      "name": "sU4",
      "parameter_type": "Internal",
      "value": "Sin[thU4]",
      "complex": false,
      "parameter_name": "sU4",
      "description": "sine of theta_u"
    },
    {
      "name": "cU4",
      "parameter_type": "Internal",
      "value": "Cos[thU4]",
      "complex": false,
      "parameter_name": "cU4",
      "description": "cosine of theta_u"
    },
    {
      "name": "sV4",
      "parameter_type": "Internal",
      "value": "Sin[thV4]",
      "complex": false,
      "parameter_name": "sV4",
      "description": "sine of theta_v"
    },
    {
      "name": "cV4",
      "parameter_type": "Internal",
      "value": "Cos[thV4]",
      "complex": false,
      "parameter_name": "cV4",
      "description": "cosine of theta_v"
    },
    {
      "name": "sW4",
      "parameter_type": "Internal",
      "value": "Sin[thW4]",
      "complex": false,
      "parameter_name": "sW4",
      "description": "sine of theta_w"
    },
    {
      "name": "cW4",
      "parameter_type": "Internal",
      "value": "Cos[thW4]",
      "complex": false,
      "parameter_name": "cW4",
      "description": "cosine of theta_w"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "tp",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MTP",
        "value": "600."
      },
      "width": {
        "sym": "WTP",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "2/3"
      },
      "pdg": 6000006,
      "particle_name": "tp",
      "antiparticle_name": "tp~",
      "full_name": "vector-like up-type tprime singlet",
      "propagator_label": "tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "bp",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MBP",
        "value": "600."
      },
      "width": {
        "sym": "WBP",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "-1/3",
        "Y": "-1/3"
      },
      "pdg": 6000007,
      "particle_name": "bp",
      "antiparticle_name": "bp~",
      "full_name": "vector-like down-type bprime singlet",
      "propagator_label": "bp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "t4",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MT4",
        "value": "600."
      },
      "width": {
        "sym": "WT4",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "1/6"
      },
      "pdg": 7000006,
      "particle_name": "t4",
      "antiparticle_name": "t4~",
      "full_name": "fourth-generation up-type quark",
      "propagator_label": "t4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 103,
      "class_name": "b4",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MB4",
        "value": "600."
      },
      "width": {
        "sym": "WB4",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "-1/3",
        "Y": "1/6"
      },
      "pdg": 7000007,
      "particle_name": "b4",
      "antiparticle_name": "b4~",
      "full_name": "fourth-generation down-type quark",
      "propagator_label": "b4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 104,
      "class_name": "n4",
      "self_conjugate": false,
      "indices": [],
      "mass": {
        "sym": "MN4",
        "value": "100."
      },
      "width": {
        "sym": "WN4",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "-1/2"
      },
      "pdg": 7000012,
      "particle_name": "n4",
      "antiparticle_name": "n4~",
      "full_name": "fourth-generation neutral lepton",
      "propagator_label": "n4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 105,
      "class_name": "e4",
      "self_conjugate": false,
      "indices": [],
      "mass": {
        "sym": "ME4",
        "value": "100."
      },
      "width": {
        "sym": "WE4",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "-1",
        "Y": "-1/2"
      },
      "pdg": 7000011,
      "particle_name": "e4",
      "antiparticle_name": "e4~",
      "full_name": "fourth-generation charged lepton",
      "propagator_label": "e4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LyTP",
      "expression": "-lamT (bar[Q3L].Phi.tR) - lamTp (bar[Q3L].Phi.tpR) + HC[-lamT (bar[Q3L].Phi.tR) - lamTp (bar[Q3L].Phi.tpR)]",
      "delayed": false
    },
    {
      "name": "LDTP",
      "expression": "-MT0 bar[tpL].tpR - MTmix bar[tpL].tR + HC[-MT0 bar[tpL].tpR - MTmix bar[tpL].tR]",
      "delayed": false
    },
    {
      "name": "LWTP",
      "expression": "-(gw/Sqrt[2]) (cT CKM[3, ff] bar[t].Ga[mu].ProjM.dq[ff] + sT CKM[3, ff] bar[tp].Ga[mu].ProjM.dq[ff]) W[mu] + HC[-(gw/Sqrt[2]) (cT CKM[3, ff] bar[t].Ga[mu].ProjM.dq[ff] + sT CKM[3, ff] bar[tp].Ga[mu].ProjM.dq[ff]) W[mu]]",
      "delayed": false
    },
    {
      "name": "LZTP",
      "expression": "-(gw/(2 cw)) (cT^2 bar[t].Ga[mu].ProjM.t + sT cT bar[t].Ga[mu].ProjM.tp + sT cT bar[tp].Ga[mu].ProjM.t + sT^2 bar[tp].Ga[mu].ProjM.tp) Z[mu]",
      "delayed": false
    },
    {
      "name": "LHTP",
      "expression": "(gw/(2 MW)) ((cT^2 MT bar[t].ProjP.t + sT cT MTP bar[t].ProjP.tp + sT cT MT bar[tp].ProjP.t + sT^2 MTP bar[tp].ProjP.tp) H + HC[(cT^2 MT bar[t].ProjP.t + sT cT MTP bar[t].ProjP.tp + sT cT MT bar[tp].ProjP.t + sT^2 MTP bar[tp].ProjP.tp) H])",
      "delayed": false
    },
    {
      "name": "LyBP",
      "expression": "-lamB (bar[Q3L].Phibar.bR) - lamBp (bar[Q3L].Phibar.bpR) + HC[-lamB (bar[Q3L].Phibar.bR) - lamBp (bar[Q3L].Phibar.bpR)]",
      "delayed": false
    },
    {
      "name": "LDBP",
      "expression": "-MB0 bar[bpL].bpR - MBmix bar[bpL].bR + HC[-MB0 bar[bpL].bpR - MBmix bar[bpL].bR]",
      "delayed": false
    },
    {
      "name": "LWBP",
      "expression": "-(gw/Sqrt[2]) (cB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.b + sB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.bp) W[mu] + HC[-(gw/Sqrt[2]) (cB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.b + sB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.bp) W[mu]]",
      "delayed": false
    },
    {
      "name": "LZBP",
      "expression": "-(gw/(2 cw)) (cB^2 bar[b].Ga[mu].ProjM.b + sB cB bar[b].Ga[mu].ProjM.bp + sB cB bar[bp].Ga[mu].ProjM.b + sB^2 bar[bp].Ga[mu].ProjM.bp) Z[mu]",
      "delayed": false
    },
    {
      "name": "L4CKM",
      "expression": "-(gw/Sqrt[2]) ((cU4 CKM[3, ff] - sU4 sV4 CKM[2, ff] - sU4 cV4 sW4 CKM[1, ff]) bar[t].Ga[mu].ProjM.dq[ff] + (sU4 CKM[3, ff] + cU4 sV4 CKM[2, ff] + cU4 cV4 sW4 CKM[1, ff]) bar[t4].Ga[mu].ProjM.dq[ff] + (cV4 CKM[2, ff] - sV4 sW4 CKM[1, ff]) bar[c].Ga[mu].ProjM.dq[ff] + cW4 CKM[1, ff] bar[u].Ga[mu].ProjM.dq[ff]) W[mu] + HC[-(gw/Sqrt[2]) ((cU4 CKM[3, ff] - sU4 sV4 CKM[2, ff] - sU4 cV4 sW4 CKM[1, ff]) bar[t].Ga[mu].ProjM.dq[ff] + (sU4 CKM[3, ff] + cU4 sV4 CKM[2, ff] + cU4 cV4 sW4 CKM[1, ff]) bar[t4].Ga[mu].ProjM.dq[ff] + (cV4 CKM[2, ff] - sV4 sW4 CKM[1, ff]) bar[c].Ga[mu].ProjM.dq[ff] + cW4 CKM[1, ff] bar[u].Ga[mu].ProjM.dq[ff]) W[mu]]",
      "delayed": false
    },
    {
      "name": "L4Mass",
      "expression": "-MT4 bar[t4].t4 - MB4 bar[b4].b4 - MN4 bar[n4].n4 - ME4 bar[e4].e4",
      "delayed": false
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```