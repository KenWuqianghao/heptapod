```json
{
  "model_name": "VLC_LN_gen",
  "info": {
    "authors": [
      "Oleg Antipin",
      "Michele Redi"
    ],
    "version": "1.0",
    "date": "2018-06-08",
    "institutions": [
      "INFN, Sezione di Firenze"
    ],
    "emails": [
      "oleg.antipin@fi.infn.it"
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
      "NP",
      2
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "HC",
      "range_kind": "NoUnfold",
      "size": 3,
      "style_symbol": "h"
    }
  ],
  "parameters": [
    {
      "name": "NHC",
      "parameter_type": "External",
      "value": "3.",
      "complex": false,
      "block_name": "VLCPARAM",
      "order_block": 1,
      "description": "Number of colors of the new confining SU(N)"
    },
    {
      "name": "grho",
      "parameter_type": "External",
      "value": "7.0",
      "complex": false,
      "block_name": "VLCPARAM",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Strong-sector coupling g_rho"
    },
    {
      "name": "fpi",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "VLCPARAM",
      "order_block": 3,
      "description": "Pion decay constant of the confining sector"
    },
    {
      "name": "mL",
      "parameter_type": "External",
      "value": "100.",
      "complex": false,
      "block_name": "VLCPARAM",
      "order_block": 4,
      "description": "Vectorlike mass of the L doublet fermion"
    },
    {
      "name": "mN",
      "parameter_type": "External",
      "value": "100.",
      "complex": false,
      "block_name": "VLCPARAM",
      "order_block": 5,
      "description": "Vectorlike mass of the N singlet fermion"
    },
    {
      "name": "thetaH",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "VLCPARAM",
      "order_block": 6,
      "description": "Topological angle of the new confining gauge theory"
    },
    {
      "name": "yre",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "VLCYUK",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Real part of y in H L N^c"
    },
    {
      "name": "yim",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "VLCYUK",
      "order_block": 2,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Imaginary part of y in H L N^c"
    },
    {
      "name": "ytre",
      "parameter_type": "External",
      "value": "0.1",
      "complex": false,
      "block_name": "VLCYUK",
      "order_block": 3,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Real part of ytilde in Hdag L^c N"
    },
    {
      "name": "ytim",
      "parameter_type": "External",
      "value": "0.",
      "complex": false,
      "block_name": "VLCYUK",
      "order_block": 4,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Imaginary part of ytilde in Hdag L^c N"
    },
    {
      "name": "mPi3",
      "parameter_type": "External",
      "value": "300.",
      "complex": false,
      "block_name": "VLCMASS",
      "order_block": 1,
      "description": "Mass of the SU(2)L triplet pions"
    },
    {
      "name": "mK2",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "VLCMASS",
      "order_block": 2,
      "description": "Mass of the composite Kaon Higgs doublet"
    },
    {
      "name": "mEta",
      "parameter_type": "External",
      "value": "300.",
      "complex": false,
      "block_name": "VLCMASS",
      "order_block": 3,
      "description": "Mass of the composite eta singlet"
    },
    {
      "name": "mEtaP",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "VLCMASS",
      "order_block": 4,
      "description": "Mass of the anomalous eta-prime singlet"
    },
    {
      "name": "mrho",
      "parameter_type": "External",
      "value": "2000.",
      "complex": false,
      "block_name": "VLCMASS",
      "order_block": 5,
      "description": "Mass of the lightest spin-1 vector resonance"
    },
    {
      "name": "wPi0",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLCWIDTH",
      "order_block": 1,
      "description": "Width of neutral triplet pion"
    },
    {
      "name": "wPiP",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLCWIDTH",
      "order_block": 2,
      "description": "Width of charged triplet pion"
    },
    {
      "name": "wK2",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLCWIDTH",
      "order_block": 3,
      "description": "Width of the composite Kaon doublet"
    },
    {
      "name": "wEta",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLCWIDTH",
      "order_block": 4,
      "description": "Width of eta"
    },
    {
      "name": "wEtaP",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLCWIDTH",
      "order_block": 5,
      "description": "Width of eta-prime"
    },
    {
      "name": "wrho",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "VLCWIDTH",
      "order_block": 6,
      "description": "Width of the rho vector resonances"
    },
    {
      "name": "y",
      "parameter_type": "Internal",
      "value": "yre + I yim",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Complex Yukawa y"
    },
    {
      "name": "yt",
      "parameter_type": "Internal",
      "value": "ytre + I ytim",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Complex Yukawa ytilde"
    },
    {
      "name": "Acoup",
      "parameter_type": "Internal",
      "value": "y + Conjugate[yt]",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "A = y + ytilde*"
    },
    {
      "name": "Bcoup",
      "parameter_type": "Internal",
      "value": "y - Conjugate[yt]",
      "complex": true,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "B = y - ytilde*"
    },
    {
      "name": "epsK",
      "parameter_type": "Internal",
      "value": "I Sqrt[2] Bcoup grho fpi^2/mK2^2",
      "complex": true,
      "description": "Composite-Higgs mixing parameter epsilon"
    },
    {
      "name": "mRhoDerived",
      "parameter_type": "Internal",
      "value": "grho fpi",
      "complex": false,
      "description": "Parametric vector-resonance scale m_rho = g_rho f_pi"
    },
    {
      "name": "gV",
      "parameter_type": "Internal",
      "value": "gw^2/grho",
      "complex": false,
      "interaction_order": [
        "NP",
        1
      ],
      "description": "Coupling of rho vector resonances to SM weak currents"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "Lvlc",
      "self_conjugate": false,
      "indices": [
        "HC",
        "SU2D"
      ],
      "flavor_index": "SU2D",
      "class_members": [
        "L0",
        "Lm"
      ],
      "mass": {
        "sym": "ML",
        "value": "100."
      },
      "width": {
        "sym": "WL",
        "value": "1."
      },
      "quantum_numbers": {
        "Y": "-1/2"
      },
      "particle_name": [
        "L0",
        "L-"
      ],
      "antiparticle_name": [
        "L0~",
        "L+"
      ],
      "full_name": [
        "Vectorlike neutral component of L",
        "Vectorlike charged component of L"
      ],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "Nvlc",
      "self_conjugate": false,
      "indices": [
        "HC"
      ],
      "mass": {
        "sym": "MN",
        "value": "100."
      },
      "width": {
        "sym": "WN",
        "value": "1."
      },
      "quantum_numbers": {
        "Y": "0"
      },
      "particle_name": "N",
      "antiparticle_name": "N~",
      "full_name": "Vectorlike singlet fermion N",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "pi0",
      "self_conjugate": true,
      "mass": {
        "sym": "mPi3",
        "value": "300."
      },
      "width": {
        "sym": "wPi0",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 10001,
      "particle_name": "pi0",
      "full_name": "Neutral component of the composite SU(2)L triplet pion",
      "propagator_label": "pi0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "pip",
      "self_conjugate": false,
      "mass": {
        "sym": "mPi3",
        "value": "300."
      },
      "width": {
        "sym": "wPiP",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": 10002,
      "particle_name": "pi+",
      "antiparticle_name": "pi-",
      "full_name": "Charged components of the composite SU(2)L triplet pion",
      "propagator_label": "pi+",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "K2",
      "self_conjugate": false,
      "indices": [
        "SU2D"
      ],
      "flavor_index": "SU2D",
      "class_members": [
        "Kp",
        "K0"
      ],
      "mass": {
        "sym": "mK2",
        "value": "500."
      },
      "width": {
        "sym": "wK2",
        "value": "1."
      },
      "quantum_numbers": {
        "Y": "1/2"
      },
      "pdg": [
        10003,
        10004
      ],
      "particle_name": [
        "K+",
        "K0"
      ],
      "antiparticle_name": [
        "K-",
        "K0~"
      ],
      "full_name": [
        "Charged component of the composite Kaon Higgs doublet",
        "Neutral component of the composite Kaon Higgs doublet"
      ],
      "propagator_label": [
        "K+",
        "K0"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "eta",
      "self_conjugate": true,
      "mass": {
        "sym": "mEta",
        "value": "300."
      },
      "width": {
        "sym": "wEta",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 10005,
      "particle_name": "eta",
      "full_name": "Composite singlet eta",
      "propagator_label": "eta",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "etaP",
      "self_conjugate": true,
      "mass": {
        "sym": "mEtaP",
        "value": "1000."
      },
      "width": {
        "sym": "wEtaP",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 10006,
      "particle_name": "eta'",
      "full_name": "Anomalous axial singlet eta-prime",
      "propagator_label": "etaP",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "rho0",
      "self_conjugate": true,
      "mass": {
        "sym": "mrho",
        "value": "2000."
      },
      "width": {
        "sym": "wrho",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 20001,
      "particle_name": "rho0",
      "full_name": "Neutral spin-1 vector resonance",
      "propagator_label": "rho0",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "rhop",
      "self_conjugate": false,
      "mass": {
        "sym": "mrho",
        "value": "2000."
      },
      "width": {
        "sym": "wrho",
        "value": "1."
      },
      "quantum_numbers": {
        "Q": "1"
      },
      "pdg": 20002,
      "particle_name": "rho+",
      "antiparticle_name": "rho-",
      "full_name": "Charged spin-1 vector resonances",
      "propagator_label": "rho+",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "raw_preamble": [
    "FR$LoopSwitches = {{Gf, MW}};",
    "FR$RmDblExt = {ymb -> MB, ymc -> MC, ymdo -> MD, yme -> Me, ymm -> MMU, yms -> MS, ymt -> MT, ymtau -> MTA, ymup -> MU};"
  ],
  "raw_blocks": [
    "PiMat = {{pi0/Sqrt[2] + eta/Sqrt[6] + etaP/Sqrt[3], pip, Kp}, {pipbar, -pi0/Sqrt[2] + eta/Sqrt[6] + etaP/Sqrt[3], K0}, {Kpbar, K0bar, -2 eta/Sqrt[6] + etaP/Sqrt[3]}};",
    "Umat := MatrixExp[I Sqrt[2] PiMat/fpi];",
    "Mmat = {{mL, 0, y Phi[1]}, {0, mL, y Phi[2]}, {Conjugate[yt] Phibar[1], Conjugate[yt] Phibar[2], mN}};",
    "PiTriplet[a_] := { (pip + pipbar)/Sqrt[2], I (pip - pipbar)/Sqrt[2], pi0 }[[a]];"
  ],
  "lagrangian_terms": [
    {
      "name": "LUVVLC",
      "expression": "Block[{mu,sp,aa,ii}, I Lvlcbar[sp,aa,ii].Ga[mu].DC[Lvlc[sp,aa,ii],mu] + I Nvlcbar[sp,aa].Ga[mu].DC[Nvlc[sp,aa],mu] - mL Lvlcbar[sp,aa,ii].Lvlc[sp,aa,ii] - mN Nvlcbar[sp,aa].Nvlc[sp,aa] + y Phi[ii] Lvlcbar[sp,aa,ii].ProjM.Nvlc[sp,aa] + yt Phibar[ii] Lvlcbar[sp,aa,ii].ProjP.Nvlc[sp,aa] + HC[y Phi[ii] Lvlcbar[sp,aa,ii].ProjM.Nvlc[sp,aa] + yt Phibar[ii] Lvlcbar[sp,aa,ii].ProjP.Nvlc[sp,aa]]]",
      "delayed": true
    },
    {
      "name": "LChiralFull",
      "expression": "Block[{mu,i}, fpi^2/4 Tr[DC[Umat,mu].DC[HC[Umat],mu]] + (grho fpi^3 Tr[Mmat.Umat] + HC[grho fpi^3 Tr[Mmat.Umat]]) + fpi^2/16 (mEtaP^2/3) (Log[Det[Umat]] - Log[Det[HC[Umat]]])^2 + 3 gw^2 grho^2 fpi^4/(2 (4 Pi)^2) Sum[Tr[Umat.Ta[i].HC[Umat].Ta[i]], {i,1,3}]]",
      "delayed": true
    },
    {
      "name": "LMExpanded",
      "expression": "Block[{a,ii,jj}, -mK2^2 (Kpbar Kp + K0bar K0) - mPi3^2/2 (pi0^2 + 2 pip pipbar) - mEta^2/2 eta^2 - I Sqrt[2] grho fpi^2 Bcoup (Kpbar Phi[1] + K0bar Phi[2]) - grho/Sqrt[2] Acoup fpi ((Kpbar PauliSigma[a,1,jj] + K0bar PauliSigma[a,2,jj]) Phi[jj] PiTriplet[a] - eta (Kpbar Phi[1] + K0bar Phi[2])/Sqrt[3]) + HC[- I Sqrt[2] grho fpi^2 Bcoup (Kpbar Phi[1] + K0bar Phi[2]) - grho/Sqrt[2] Acoup fpi ((Kpbar PauliSigma[a,1,jj] + K0bar PauliSigma[a,2,jj]) Phi[jj] PiTriplet[a] - eta (Kpbar Phi[1] + K0bar Phi[2])/Sqrt[3])]]",
      "delayed": true
    },
    {
      "name": "LKinTriplet",
      "expression": "(I del[pipbar, mu] gw pi0 Wi[mu, 1])/(2 Sqrt[2]) - (I del[pip, mu] gw pi0 Wi[mu, 1])/(2 Sqrt[2]) - (I del[pi0, mu] gw pipbar Wi[mu, 1])/(2 Sqrt[2]) + (I del[pi0, mu] gw pip Wi[mu, 1])/(2 Sqrt[2]) + (del[pipbar, mu] gw pi0 Wi[mu, 2])/(2 Sqrt[2]) + (del[pip, mu] gw pi0 Wi[mu, 2])/(2 Sqrt[2]) - (del[pi0, mu] gw pipbar Wi[mu, 2])/(2 Sqrt[2]) - (del[pi0, mu] gw pip Wi[mu, 2])/(2 Sqrt[2]) + 1/2 I del[pip, mu] gw pipbar Wi[mu, 3] - 1/2 I del[pipbar, mu] gw pip Wi[mu, 3]",
      "delayed": true
    },
    {
      "name": "LKinK2",
      "expression": "Block[{mu,ii}, ExpandIndices[DC[HC[K2[ii]],mu] DC[K2[ii],mu], FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LAnomalyTriplet",
      "expression": "Block[{mu,nu,rho,sig,a}, ExpandIndices[NHC g1 gw/(32 Pi^2 fpi) Eps[mu,nu,rho,sig] FS[B,rho,sig] Sum[PiTriplet[a] FS[Wi,mu,nu,a], {a,1,3}]]]",
      "delayed": true
    },
    {
      "name": "LAnomalyEta",
      "expression": "Block[{mu,nu,rho,sig,a}, -NHC eta/(32 Sqrt[3] Pi^2 fpi) Eps[mu,nu,rho,sig] (gw^2 Sum[FS[Wi,mu,nu,a] FS[Wi,rho,sig,a], {a,1,3}] + g1^2 FS[B,mu,nu] FS[B,rho,sig])]",
      "delayed": true
    },
    {
      "name": "LEDM",
      "expression": "Block[{mu,nu,rho,sig,a}, -mPi3^2/2 Sum[PiTriplet[a]^2,{a,1,3}] - mEta^2/2 eta^2 + 4 Im[y yt] grho^2 fpi^3/mK2^2 (Sum[Phibar[i] PauliSigma[a,i,j] Phi[j] PiTriplet[a],{a,1,3},{i,1,2},{j,1,2}] - eta Phibar[i] Phi[i]/Sqrt[3]) + NHC g1 gw/(32 Pi^2 fpi) Eps[mu,nu,rho,sig] FS[B,rho,sig] Sum[PiTriplet[a] FS[Wi,mu,nu,a], {a,1,3}] - NHC eta/(32 Sqrt[3] Pi^2 fpi) Eps[mu,nu,rho,sig] (gw^2 Sum[FS[Wi,mu,nu,a] FS[Wi,rho,sig,a], {a,1,3}] + g1^2 FS[B,mu,nu] FS[B,rho,sig])]",
      "delayed": true
    },
    {
      "name": "LRhoff",
      "expression": "1/Sqrt[2] gV (rhop[mu] (vlbar.Ga[mu].ProjM.l + ubar.Ga[mu].ProjM.d + cbar.Ga[mu].ProjM.s + tbar.Ga[mu].ProjM.b) + rhopbar[mu] (lbar.Ga[mu].ProjM.vl + dbar.Ga[mu].ProjM.u + sbar.Ga[mu].ProjM.c + bbar.Ga[mu].ProjM.t)) + 1/2 gV rho0[mu] (vlbar.Ga[mu].ProjM.vl + ubar.Ga[mu].ProjM.u + cbar.Ga[mu].ProjM.c + tbar.Ga[mu].ProjM.t - lbar.Ga[mu].ProjM.l - dbar.Ga[mu].ProjM.d - sbar.Ga[mu].ProjM.s - bbar.Ga[mu].ProjM.b)",
      "delayed": true
    },
    {
      "name": "LRhoTriplet",
      "expression": "grho 1/2 I del[pip, mu] pipbar rho0[mu] - grho 1/2 I del[pipbar, mu] pip rho0[mu] - grho 1/2 I del[pip, mu] pi0 rhopbar[mu] + grho 1/2 I del[pi0, mu] pip rhopbar[mu] + grho 1/2 I del[pipbar, mu] pi0 rhop[mu] - grho 1/2 I del[pi0, mu] pipbar rhop[mu]",
      "delayed": true
    },
    {
      "name": "LVLCNP",
      "expression": "LUVVLC + LChiralFull + LMExpanded + LKinTriplet + LKinK2 + LAnomalyTriplet + LAnomalyEta + LRhoff + LRhoTriplet",
      "delayed": true
    }
  ]
}
```