```json
{
  "model_name": "HiggsCharacterisation_gen",
  "info": {
    "authors": [
      "P. Artoisenet",
      "P. de Aquino",
      "F. Demartin",
      "R. Frederix",
      "S. Frixione",
      "S. Maltoni",
      "K. Mawatari"
    ],
    "version": "1.0",
    "date": "2026-07-13",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "QNP",
      2
    ]
  ],
  "interaction_order_limit": [
    [
      "QNP",
      2
    ]
  ],
  "feynman_gauge": false,
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lambda",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 1,
      "description": "cut-off scale"
    },
    {
      "name": "ca",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 2,
      "description": "cosine of scalar mixing angle between 0+ and 0-"
    },
    {
      "name": "sa",
      "parameter_type": "Internal",
      "value": "Sqrt[1-ca^2]",
      "complex": false,
      "description": "sine of scalar mixing angle between 0+ and 0-"
    },
    {
      "name": "kSM",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 3,
      "description": "SM-like X0ZZ and X0WW coupling modifier"
    },
    {
      "name": "kHtt",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 4,
      "description": "CP-even X0 top Yukawa modifier"
    },
    {
      "name": "kAtt",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 5,
      "description": "CP-odd X0 top Yukawa modifier"
    },
    {
      "name": "kHbb",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 6,
      "description": "CP-even X0 bottom Yukawa modifier"
    },
    {
      "name": "kAbb",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 7,
      "description": "CP-odd X0 bottom Yukawa modifier"
    },
    {
      "name": "kHll",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 8,
      "description": "CP-even X0 tau Yukawa modifier"
    },
    {
      "name": "kAll",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 9,
      "description": "CP-odd X0 tau Yukawa modifier"
    },
    {
      "name": "kHaa",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 10,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-even X0 gamma gamma coupling modifier"
    },
    {
      "name": "kAaa",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 11,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-odd X0 gamma gamma coupling modifier"
    },
    {
      "name": "kHza",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 12,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-even X0 Z gamma coupling modifier"
    },
    {
      "name": "kAza",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 13,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-odd X0 Z gamma coupling modifier"
    },
    {
      "name": "kHgg",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 14,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-even X0 gluon gluon coupling modifier"
    },
    {
      "name": "kAgg",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 15,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-odd X0 gluon gluon coupling modifier"
    },
    {
      "name": "kHzz",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 16,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "dimension-six CP-even X0ZZ field-strength coupling"
    },
    {
      "name": "kAzz",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 17,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "dimension-six CP-odd X0ZZ field-strength coupling"
    },
    {
      "name": "kHww",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 18,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "dimension-six CP-even X0WW field-strength coupling"
    },
    {
      "name": "kAww",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 19,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "dimension-six CP-odd X0WW field-strength coupling"
    },
    {
      "name": "kHda",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 20,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-even derivative X0 Z dA coupling"
    },
    {
      "name": "kHdz",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 21,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "CP-even derivative X0 Z dZ coupling"
    },
    {
      "name": "kHdwR",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 22,
      "description": "real part of CP-even derivative X0 W dW coupling"
    },
    {
      "name": "kHdwI",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 23,
      "description": "imaginary part of CP-even derivative X0 W dW coupling"
    },
    {
      "name": "kHdw",
      "parameter_type": "Internal",
      "value": "kHdwR+I*kHdwI",
      "complex": true,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "complex CP-even derivative X0 W dW coupling"
    },
    {
      "name": "kqa",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 24,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1 quark vector coupling modifier"
    },
    {
      "name": "kqb",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 25,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1 quark axial-vector coupling modifier"
    },
    {
      "name": "kla",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 26,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1 lepton vector coupling modifier"
    },
    {
      "name": "klb",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 27,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1 lepton axial-vector coupling modifier"
    },
    {
      "name": "kw1",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 28,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1WW coupling kappa 1"
    },
    {
      "name": "kw2",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 29,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1WW coupling kappa 2"
    },
    {
      "name": "kw3",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 30,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1WW coupling kappa 3"
    },
    {
      "name": "kw4",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 31,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1WW coupling kappa 4"
    },
    {
      "name": "kw5",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 32,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1WW coupling kappa 5"
    },
    {
      "name": "kz1",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 33,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1ZZ coupling kappa 1"
    },
    {
      "name": "kz3",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 34,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1ZZ coupling kappa 3"
    },
    {
      "name": "kz5",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 35,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X1ZZ coupling kappa 5"
    },
    {
      "name": "kq",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 36,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 light-quark energy-momentum tensor coupling"
    },
    {
      "name": "kq3",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 37,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 third-generation quark energy-momentum tensor coupling"
    },
    {
      "name": "kl",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 38,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 lepton energy-momentum tensor coupling"
    },
    {
      "name": "kg",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 39,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 gluon energy-momentum tensor coupling"
    },
    {
      "name": "ka",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 40,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 photon energy-momentum tensor coupling"
    },
    {
      "name": "kz",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 41,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 Z energy-momentum tensor coupling"
    },
    {
      "name": "kw",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "BSMINPUTS",
      "order_block": 42,
      "interaction_order": [
        "QNP",
        1
      ],
      "description": "X2 W energy-momentum tensor coupling"
    },
    {
      "name": "gHaa",
      "parameter_type": "Internal",
      "value": "ee^2/(4*Pi)/(Pi*vev)*(47/18)",
      "complex": false,
      "description": "SM-normalised CP-even X0 gamma gamma coupling"
    },
    {
      "name": "gAaa",
      "parameter_type": "Internal",
      "value": "ee^2/(4*Pi)/(Pi*vev)*(4/3)",
      "complex": false,
      "description": "2HDM tan beta=1 CP-odd X0 gamma gamma coupling"
    },
    {
      "name": "gHza",
      "parameter_type": "Internal",
      "value": "Sqrt[ee^2/(4*Pi)*Gf*MZ^2/(8*Sqrt[2]*Pi)]*(94*cw^2-13)/(9*Pi*vev)",
      "complex": false,
      "description": "SM-normalised CP-even X0 Z gamma coupling"
    },
    {
      "name": "gAza",
      "parameter_type": "Internal",
      "value": "2*Sqrt[ee^2/(4*Pi)*Gf*MZ^2/(8*Sqrt[2]*Pi)]*(8*cw^2-5)/(3*Pi*vev)",
      "complex": false,
      "description": "2HDM tan beta=1 CP-odd X0 Z gamma coupling"
    },
    {
      "name": "gHgg",
      "parameter_type": "Internal",
      "value": "-gs^2/(4*Pi)/(3*Pi*vev)",
      "complex": false,
      "description": "SM-normalised CP-even X0 gluon gluon coupling"
    },
    {
      "name": "gAgg",
      "parameter_type": "Internal",
      "value": "gs^2/(4*Pi)/(2*Pi*vev)",
      "complex": false,
      "description": "2HDM tan beta=1 CP-odd X0 gluon gluon coupling"
    },
    {
      "name": "au",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(1/2-4/3 sw2)",
      "complex": false,
      "description": "SM vector coupling for up-type quarks"
    },
    {
      "name": "bu",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(1/2)",
      "complex": false,
      "description": "SM axial-vector coupling for up-type quarks"
    },
    {
      "name": "ad",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(-1/2+2/3 sw2)",
      "complex": false,
      "description": "SM vector coupling for down-type quarks"
    },
    {
      "name": "bd",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(-1/2)",
      "complex": false,
      "description": "SM axial-vector coupling for down-type quarks"
    },
    {
      "name": "an",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(1/2)",
      "complex": false,
      "description": "SM vector coupling for neutrinos"
    },
    {
      "name": "bn",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(1/2)",
      "complex": false,
      "description": "SM axial-vector coupling for neutrinos"
    },
    {
      "name": "al",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(-1/2+2 sw2)",
      "complex": false,
      "description": "SM vector coupling for charged leptons"
    },
    {
      "name": "bl",
      "parameter_type": "Internal",
      "value": "ee/(2 sw cw)*(-1/2)",
      "complex": false,
      "description": "SM axial-vector coupling for charged leptons"
    },
    {
      "name": "gwwz",
      "parameter_type": "Internal",
      "value": "-ee*cw/sw",
      "complex": false,
      "description": "WWZ gauge coupling"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "X0",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MX0",
        "value": "125.0"
      },
      "width": {
        "sym": "WX0",
        "value": "0.00407"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 5000000,
      "particle_name": "X0",
      "full_name": "neutral spin-0 Higgs-characterisation resonance",
      "propagator_label": "X0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "X1",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MX1",
        "value": "125.0"
      },
      "width": {
        "sym": "WX1",
        "value": "0.00407"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 5000001,
      "particle_name": "X1",
      "full_name": "neutral spin-1 Higgs-characterisation resonance",
      "propagator_label": "X1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "T",
      "class_index": 102,
      "class_name": "X2",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MX2",
        "value": "125.0"
      },
      "width": {
        "sym": "WX2",
        "value": "0.00407"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 5000002,
      "particle_name": "X2",
      "full_name": "neutral spin-2 Higgs-characterisation resonance",
      "propagator_label": "X2",
      "propagator_arrow": "None"
    }
  ],
  "raw_blocks": [
    "TFq[mu_,nu_] := Sum[Tfermion[q,mu,nu], {q,{u,d,c,s}}]; TFq3[mu_,nu_] := Tfermion[t,mu,nu] + Tfermion[b,mu,nu]; TFl[mu_,nu_] := Sum[Tfermion[lep,mu,nu], {lep,{ve,vm,vt,e,muon,ta}}]; TYq[mu_,nu_] := -ME[mu,nu] (-MT tbar.t - MB bbar.b); TYl[mu_,nu_] := -ME[mu,nu] (-MTA tabar.ta); TGg[mu_,nu_] := -ME[mu,nu] (-1/4 FS[G,rho,sig,a] FS[G,rho,sig,a]) - FS[G,mu,rho,a] FS[G,nu,rho,a]; TGa[mu_,nu_] := -ME[mu,nu] (-1/4 FS[A,rho,sig] FS[A,rho,sig]) - FS[A,mu,rho] FS[A,nu,rho]; TGz[mu_,nu_] := -ME[mu,nu] (-1/4 FS[Z,rho,sig] FS[Z,rho,sig] + 1/2 MZ^2 Z[rho] Z[rho]) - (FS[Z,mu,rho] FS[Z,nu,rho] - MZ^2 Z[mu] Z[nu]); TGw[mu_,nu_] := -ME[mu,nu] (-1/2 FS[Wbar,rho,sig] FS[W,rho,sig] + MW^2 Wbar[rho] W[rho]) - (FS[Wbar,mu,rho] FS[W,nu,rho] - MW^2 Wbar[mu] W[nu] + FS[Wbar,nu,rho] FS[W,mu,rho] - MW^2 Wbar[nu] W[mu])"
  ],
  "lagrangian_terms": [
    {
      "name": "L0f",
      "expression": "-(ca (kHtt MT/vev tbar.t + kHbb MB/vev bbar.b + kHll MTA/vev tabar.ta) + I sa (kAtt MT/vev tbar.Ga[5].t + kAbb MB/vev bbar.Ga[5].b + kAll MTA/vev tabar.Ga[5].ta)) X0",
      "delayed": true
    },
    {
      "name": "L0v",
      "expression": "(-1/4 (ca kHaa gHaa FS[A,mu,nu] FS[A,mu,nu] + sa kAaa gAaa FS[A,mu,nu] Dual[FS][A,mu,nu]) - 1/2 (ca kHza gHza FS[Z,mu,nu] FS[A,mu,nu] + sa kAza gAza FS[Z,mu,nu] Dual[FS][A,mu,nu]) - 1/4 (ca kHgg gHgg FS[G,mu,nu,a] FS[G,mu,nu,a] + sa kAgg gAgg FS[G,mu,nu,a] Dual[FS][G,mu,nu,a]) - 1/4/Lambda (ca kHzz FS[Z,mu,nu] FS[Z,mu,nu] + sa kAzz FS[Z,mu,nu] Dual[FS][Z,mu,nu]) - 1/2/Lambda (ca kHww FS[Wbar,mu,nu] FS[W,mu,nu] + sa kAww FS[Wbar,mu,nu] Dual[FS][W,mu,nu]) - 1/Lambda (ca kHda Z[nu] del[FS[A,mu,nu],mu] + ca kHdz Z[nu] del[FS[Z,mu,nu],mu] + ca (kHdw Wbar[nu] del[FS[W,mu,nu],mu] + HC[kHdw Wbar[nu] del[FS[W,mu,nu],mu]]))) X0",
      "delayed": true
    },
    {
      "name": "L1f",
      "expression": "(kqa au uqbar[s,n,i].Ga[mu,s,t].uq[t,n,i] + kqa ad dqbar[s,n,i].Ga[mu,s,t].dq[t,n,i] + kla an vlbar[s,n].Ga[mu,s,t].vl[t,n] + kla al lbar[s,n].Ga[mu,s,t].l[t,n] - kqb bu uqbar[s,n,i].Ga[mu,s,t].Ga[5,t,u].uq[u,n,i] - kqb bd dqbar[s,n,i].Ga[mu,s,t].Ga[5,t,u].dq[u,n,i] - klb bn vlbar[s,n].Ga[mu,s,t].Ga[5,t,u].vl[u,n] - klb bl lbar[s,n].Ga[mu,s,t].Ga[5,t,u].l[u,n]) X1[mu]",
      "delayed": true
    },
    {
      "name": "L1w",
      "expression": "I kw1 gwwz (FS[Wbar,mu,nu] W[mu] - FS[W,mu,nu] Wbar[mu]) X1[nu] + I kw2 gwwz Wbar[mu] W[nu] FS[X1,mu,nu] - kw3 Wbar[mu] W[nu] (del[X1[nu],mu] + del[X1[mu],nu]) + I kw4 Wbar[mu] W[nu] Dual[FS][X1,mu,nu] - kw5 Eps[mu,nu,rho,sig] (Wbar[mu] del[W[nu],rho] - del[Wbar[mu],rho] W[nu]) X1[sig]",
      "delayed": true
    },
    {
      "name": "L1z",
      "expression": "-kz1 FS[Z,mu,nu] Z[mu] X1[nu] - kz3 X1[mu] del[Z[mu],nu] Z[nu] - kz5 Eps[mu,nu,rho,sig] X1[mu] Z[nu] del[Z[sig],rho]",
      "delayed": true
    },
    {
      "name": "L1",
      "expression": "L1f + L1w + L1z",
      "delayed": true
    },
    {
      "name": "L2f",
      "expression": "-1/Lambda (kq TFq[mu,nu] + kq3 (TFq3[mu,nu] + TYq[mu,nu]) + kl (TFl[mu,nu] + TYl[mu,nu])) X2[mu,nu]",
      "delayed": true
    },
    {
      "name": "L2v",
      "expression": "-1/Lambda (kg TGg[mu,nu] + ka TGa[mu,nu] + kz TGz[mu,nu] + kw TGw[mu,nu]) X2[mu,nu]",
      "delayed": true
    },
    {
      "name": "L2",
      "expression": "L2f + L2v",
      "delayed": true
    },
    {
      "name": "LHCNP",
      "expression": "L0f + L0v + L1 + L2",
      "delayed": true
    }
  ]
}
```