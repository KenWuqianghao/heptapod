```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": [
      "Linda M. Carpenter",
      "Taylor Murphy",
      "Tim M. P. Tait"
    ],
    "version": "1.0",
    "date": "2026-07-13",
    "institutions": [
      "The Ohio State University",
      "University of California, Irvine"
    ],
    "emails": [
      "lmc@physics.osu.edu",
      "murphy.1573@osu.edu",
      "ttait@uci.edu"
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
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "u"
    }
  ],
  "parameters": [
    {
      "name": "MFu",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000001,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MFu",
      "tex": "M_{\\Psi_u}",
      "description": "Mass of the up-type color-sextet Dirac fermion"
    },
    {
      "name": "WFu",
      "parameter_type": "External",
      "value": "4.7740",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9000001,
      "parameter_name": "WFu",
      "tex": "\\Gamma_{\\Psi_u}",
      "description": "Width of the up-type color-sextet Dirac fermion"
    },
    {
      "name": "MFd",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000002,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MFd",
      "tex": "M_{\\Psi_d}",
      "description": "Mass of the down-type color-sextet Dirac fermion"
    },
    {
      "name": "WFd",
      "parameter_type": "External",
      "value": "4.7740",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9000002,
      "parameter_name": "WFd",
      "tex": "\\Gamma_{\\Psi_d}",
      "description": "Width of the down-type color-sextet Dirac fermion"
    },
    {
      "name": "MSu",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000003,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MSu",
      "tex": "M_{\\Phi_u}",
      "description": "Mass of the up-type color-sextet scalar"
    },
    {
      "name": "WSu",
      "parameter_type": "External",
      "value": "4.4108",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9000003,
      "parameter_name": "WSu",
      "tex": "\\Gamma_{\\Phi_u}",
      "description": "Width of the up-type color-sextet scalar"
    },
    {
      "name": "MSd",
      "parameter_type": "External",
      "value": "500.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 9000004,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "MSd",
      "tex": "M_{\\Phi_d}",
      "description": "Mass of the down-type color-sextet scalar"
    },
    {
      "name": "WSd",
      "parameter_type": "External",
      "value": "4.0647",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 9000004,
      "parameter_name": "WSd",
      "tex": "\\Gamma_{\\Phi_d}",
      "description": "Width of the down-type color-sextet scalar"
    },
    {
      "name": "CFBuR",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFBUR",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFBuR[_]",
          "rhs": "0.1"
        }
      ],
      "description": "Real part of sextet fermion coupling to up-type quarks and hypercharge field strength"
    },
    {
      "name": "CFBuI",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFBUI",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFBuI[_]",
          "rhs": "0"
        }
      ],
      "description": "Imaginary part of sextet fermion coupling to up-type quarks and hypercharge field strength"
    },
    {
      "name": "CFBdR",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFBDR",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFBdR[_]",
          "rhs": "0.1"
        }
      ],
      "description": "Real part of sextet fermion coupling to down-type quarks and hypercharge field strength"
    },
    {
      "name": "CFBdI",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFBDI",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFBdI[_]",
          "rhs": "0"
        }
      ],
      "description": "Imaginary part of sextet fermion coupling to down-type quarks and hypercharge field strength"
    },
    {
      "name": "CFuR",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFUPR",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFuR[_]",
          "rhs": "0.1"
        }
      ],
      "description": "Real part of sextet fermion coupling to up-type quarks"
    },
    {
      "name": "CFuI",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFUPI",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFuI[_]",
          "rhs": "0"
        }
      ],
      "description": "Imaginary part of sextet fermion coupling to up-type quarks"
    },
    {
      "name": "CFdR",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFDOWNR",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFdR[_]",
          "rhs": "0.1"
        }
      ],
      "description": "Real part of sextet fermion coupling to down-type quarks"
    },
    {
      "name": "CFdI",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SFDOWNI",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFdI[_]",
          "rhs": "0"
        }
      ],
      "description": "Imaginary part of sextet fermion coupling to down-type quarks"
    },
    {
      "name": "CSuR",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SSUPR",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CSuR[_,_]",
          "rhs": "0.1"
        }
      ],
      "description": "Real part of sextet scalar coupling to up-type quarks and charged leptons"
    },
    {
      "name": "CSuI",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SSUPI",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CSuI[_,_]",
          "rhs": "0"
        }
      ],
      "description": "Imaginary part of sextet scalar coupling to up-type quarks and charged leptons"
    },
    {
      "name": "CSdR",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SSDOWNR",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CSdR[_,_]",
          "rhs": "0.1"
        }
      ],
      "description": "Real part of sextet scalar coupling to down-type quarks and charged leptons"
    },
    {
      "name": "CSdI",
      "parameter_type": "External",
      "complex": false,
      "block_name": "SSDOWNI",
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CSdI[_,_]",
          "rhs": "0"
        }
      ],
      "description": "Imaginary part of sextet scalar coupling to down-type quarks and charged leptons"
    },
    {
      "name": "CFBu",
      "parameter_type": "Internal",
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFBu[i_]",
          "rhs": "CFBuR[i] + I CFBuI[i]",
          "delayed": true
        }
      ],
      "description": "Complex sextet fermion coupling to up-type quarks and hypercharge field strength"
    },
    {
      "name": "CFBd",
      "parameter_type": "Internal",
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFBd[i_]",
          "rhs": "CFBdR[i] + I CFBdI[i]",
          "delayed": true
        }
      ],
      "description": "Complex sextet fermion coupling to down-type quarks and hypercharge field strength"
    },
    {
      "name": "CFu",
      "parameter_type": "Internal",
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFu[i_]",
          "rhs": "CFuR[i] + I CFuI[i]",
          "delayed": true
        }
      ],
      "description": "Complex sextet fermion coupling to up-type quarks"
    },
    {
      "name": "CFd",
      "parameter_type": "Internal",
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CFd[i_]",
          "rhs": "CFdR[i] + I CFdI[i]",
          "delayed": true
        }
      ],
      "description": "Complex sextet fermion coupling to down-type quarks"
    },
    {
      "name": "CSu",
      "parameter_type": "Internal",
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CSu[i_,j_]",
          "rhs": "CSuR[i,j] + I CSuI[i,j]",
          "delayed": true
        }
      ],
      "description": "Complex sextet scalar coupling to up-type quarks and charged leptons"
    },
    {
      "name": "CSd",
      "parameter_type": "Internal",
      "complex": true,
      "interaction_order": [
        "QCD",
        1
      ],
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "CSd[i_,j_]",
          "rhs": "CSdR[i,j] + I CSdI[i,j]",
          "delayed": true
        }
      ],
      "description": "Complex sextet scalar coupling to down-type quarks and charged leptons"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "sFu",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "mass": {
        "sym": "MFu",
        "value": "500."
      },
      "width": {
        "sym": "WFu",
        "value": "4.7740"
      },
      "quantum_numbers": {
        "Q": "-2/3",
        "Y": "-2/3"
      },
      "pdg": 9000001,
      "particle_name": "sFu",
      "antiparticle_name": "sFu~",
      "full_name": "Up-type color-sextet Dirac fermion",
      "propagator_label": "sFu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "sFd",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "mass": {
        "sym": "MFd",
        "value": "500."
      },
      "width": {
        "sym": "WFd",
        "value": "4.7740"
      },
      "quantum_numbers": {
        "Q": "1/3",
        "Y": "1/3"
      },
      "pdg": 9000002,
      "particle_name": "sFd",
      "antiparticle_name": "sFd~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "sFd",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "sSu",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "mass": {
        "sym": "MSu",
        "value": "500."
      },
      "width": {
        "sym": "WSu",
        "value": "4.4108"
      },
      "quantum_numbers": {
        "Q": "1/3",
        "Y": "1/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000003,
      "particle_name": "sSu",
      "antiparticle_name": "sSu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "sSu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "sSd",
      "self_conjugate": false,
      "indices": [
        "Sextet"
      ],
      "mass": {
        "sym": "MSd",
        "value": "500."
      },
      "width": {
        "sym": "WSd",
        "value": "4.0647"
      },
      "quantum_numbers": {
        "Q": "4/3",
        "Y": "4/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000004,
      "particle_name": "sSd",
      "antiparticle_name": "sSd~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "sSd",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetKin",
      "expression": "sFubar[ss,kk].(I Ga[mu,ss,rr].DC[sFu[rr,kk],mu] - MFu sFu[ss,kk]) + sFdbar[ss,kk].(I Ga[mu,ss,rr].DC[sFd[rr,kk],mu] - MFd sFd[ss,kk]) + DC[sSubar[kk], mu] DC[sSu[kk],mu] - MSu^2 sSubar[kk] sSu[kk] + DC[sSdbar[kk], mu] DC[sSd[kk],mu] - MSd^2 sSdbar[kk] sSd[kk]",
      "delayed": true
    },
    {
      "name": "LFu",
      "expression": "CFu[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFubar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CFu[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFubar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii]] FS[G,mu,nu,aa] + CFBu[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFubar[ss,kk].CC[uR][ss,mm,ii] FS[G,mu,nu,aa] FS[B,mu,nu] + HC[CFBu[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFubar[ss,kk].CC[uR][ss,mm,ii]] FS[G,mu,nu,aa] FS[B,mu,nu]",
      "delayed": true
    },
    {
      "name": "LFd",
      "expression": "CFd[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFdbar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CFd[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFdbar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii]] FS[G,mu,nu,aa] + CFBd[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFdbar[ss,kk].CC[dR][ss,mm,ii] FS[G,mu,nu,aa] FS[B,mu,nu] + HC[CFBd[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFdbar[ss,kk].CC[dR][ss,mm,ii]] FS[G,mu,nu,aa] FS[B,mu,nu]",
      "delayed": true
    },
    {
      "name": "LSu",
      "expression": "CSu[mm,ll] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sSubar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CSu[mm,ll]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sSubar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii] FS[G,mu,nu,aa]]",
      "delayed": true
    },
    {
      "name": "LSd",
      "expression": "CSd[mm,ll] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sSdbar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CSd[mm,ll]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sSdbar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii] FS[G,mu,nu,aa]]",
      "delayed": true
    },
    {
      "name": "LSextet",
      "expression": "LSextetKin + LFu + LFd + LSu + LSd",
      "delayed": false
    }
  ],
  "raw_preamble": [
    "AddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "raw_blocks": []
}
```