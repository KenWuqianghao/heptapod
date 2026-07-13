```json
{
  "model_name": "SMWeinberg_gen",
  "info": {
    "authors": [
      "Benjamin Fuks",
      "Jonas Neundorf",
      "Krisztian Peters",
      "Richard Ruiz",
      "Matthias Saimpert"
    ],
    "version": "1.0.0",
    "date": "2026-07-13",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lambda",
      "parameter_type": "External",
      "value": "200000.",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 1,
      "tex": "\\[CapitalLambda]",
      "description": "EFT cutoff scale [GeV]"
    },
    {
      "name": "Cee",
      "parameter_type": "External",
      "value": "1.1",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 2,
      "tex": "Subscript[C,ee]",
      "description": "Cee Wilson coefficient"
    },
    {
      "name": "Cem",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 3,
      "tex": "Subscript[C,e\\[Mu]]",
      "description": "Cemu Wilson coefficient"
    },
    {
      "name": "Cet",
      "parameter_type": "External",
      "value": "1.3",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 4,
      "tex": "Subscript[C,e\\[Tau]]",
      "description": "Cetau Wilson coefficient"
    },
    {
      "name": "Cmm",
      "parameter_type": "External",
      "value": "1.4",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 5,
      "tex": "Subscript[C,\\[Mu]\\[Mu]]",
      "description": "Cmumu Wilson coefficient"
    },
    {
      "name": "Cmt",
      "parameter_type": "External",
      "value": "1.5",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 6,
      "tex": "Subscript[C,\\[Mu]\\[Tau]]",
      "description": "Cmutau Wilson coefficient"
    },
    {
      "name": "Ctt",
      "parameter_type": "External",
      "value": "1.6",
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 7,
      "tex": "Subscript[C,\\[Tau]\\[Tau]]",
      "description": "Ctautau Wilson coefficient"
    },
    {
      "name": "mN1",
      "parameter_type": "Internal",
      "value": "vev*vev*Abs[Cee+Cem+Cet+Cmm+Cmt+Ctt]/Lambda",
      "complex": false,
      "tex": "Subscript[m,\"N\"]",
      "description": "Auxiliary Majorana-neutrino mass mN = |sum C5| v^2/Lambda [GeV]"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 131,
      "class_name": "N1",
      "self_conjugate": true,
      "indices": [],
      "flavor_index": null,
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "mN1",
        "value": "Internal",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "WN1",
        "value": "0",
        "members": []
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 9900012,
      "particle_name": "N1",
      "antiparticle_name": null,
      "full_name": "N1",
      "propagator_label": "N1",
      "propagator_type": "Straight",
      "propagator_arrow": "False",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNKin",
      "expression": "I/2 N1bar[s1].Ga[v,s1,s2].del[N1[s2],v] - 1/2 mN1 N1bar[s1].N1[s1]",
      "delayed": true
    },
    {
      "name": "LNCCbare",
      "expression": "gw/Sqrt[2] * N1bar.W[m].ProjM[m].e + gw/Sqrt[2] * N1bar.W[m].ProjM[m].mu + gw/Sqrt[2] * N1bar.W[m].ProjM[m].ta",
      "delayed": true
    },
    {
      "name": "LNCC",
      "expression": "LNCCbare + HC[LNCCbare]",
      "delayed": true
    },
    {
      "name": "LNNCbare",
      "expression": "1/2 * gw/cw * N1bar.Z[m].ProjM[m].ve + 1/2 * gw/cw * N1bar.Z[m].ProjM[m].vm + 1/2 * gw/cw * N1bar.Z[m].ProjM[m].vt",
      "delayed": true
    },
    {
      "name": "LNNC",
      "expression": "LNNCbare + HC[LNNCbare]",
      "delayed": true
    },
    {
      "name": "LNHbare",
      "expression": "- gw*mN1/(2*MW) * (1 + H*gw/(4*MW)) * N1bar.ProjM.ve H - gw*mN1/(2*MW) * (1 + H*gw/(4*MW)) * N1bar.ProjM.vm H - gw*mN1/(2*MW) * (1 + H*gw/(4*MW)) * N1bar.ProjM.vt H",
      "delayed": true
    },
    {
      "name": "LNHX",
      "expression": "LNHbare + HC[LNHbare]",
      "delayed": true
    },
    {
      "name": "LNGbare",
      "expression": "I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * ebar.ProjP.N1 GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * mubar.ProjP.N1 GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * tabar.ProjP.N1 GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * N1bar.ProjP.CC[e] GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * N1bar.ProjP.CC[mu] GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * N1bar.ProjP.CC[ta] GPbar + I *gw*mN1/(2*MW) * (1 + H*gw/(2*MW)) * vebar.ProjP.N1 G0 + I *gw*mN1/(2*MW) * (1 + H*gw/(2*MW)) * vmbar.ProjP.N1 G0 + I *gw*mN1/(2*MW) * (1 + H*gw/(2*MW)) * vtbar.ProjP.N1 G0",
      "delayed": true
    },
    {
      "name": "LNGX",
      "expression": "LNGbare + HC[LNGbare]",
      "delayed": true
    },
    {
      "name": "LNGGbare",
      "expression": "gw*gw*mN1/(4*MW*MW) * ebar.ProjP.CC[e] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * mubar.ProjP.CC[e] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * tabar.ProjP.CC[e] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * ebar.ProjP.CC[mu] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * mubar.ProjP.CC[mu] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * tabar.ProjP.CC[mu] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * ebar.ProjP.CC[ta] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * mubar.ProjP.CC[ta] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * tabar.ProjP.CC[ta] GPbar GPbar + gw*gw*mN1/(8*MW*MW) * vebar.ProjP.N1 G0 G0 + gw*gw*mN1/(8*MW*MW) * vmbar.ProjP.N1 G0 G0 + gw*gw*mN1/(8*MW*MW) * vtbar.ProjP.N1 G0 G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * ebar.ProjP.N1 GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * mubar.ProjP.N1 GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * tabar.ProjP.N1 GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * N1bar.ProjP.CC[e] GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * N1bar.ProjP.CC[mu] GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * N1bar.ProjP.CC[ta] GPbar G0",
      "delayed": true
    },
    {
      "name": "LNGGX",
      "expression": "LNGGbare + HC[LNGGbare]",
      "delayed": true
    },
    {
      "name": "LD5",
      "expression": "LNKin + LNCC + LNNC + LNHX + LNGX + LNGGX",
      "delayed": true
    },
    {
      "name": "LFull",
      "expression": "LSM + LD5",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```