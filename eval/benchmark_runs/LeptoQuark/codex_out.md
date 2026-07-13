```json
{
  "model_name": "LeptoQuark_gen",
  "info": {
    "authors": [
      "Michael J. Baker",
      "Javier Fuentes-Martin",
      "Gino Isidori",
      "Matthias Koenig"
    ],
    "version": "1.1",
    "date": "07.04.2021",
    "institutions": [
      "University of Zurich",
      "Johannes Gutenberg University Mainz"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [
    [
      "QCD",
      1
    ],
    [
      "NP",
      1
    ],
    [
      "QED",
      2
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": false,
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "MVLQ",
      "parameter_type": "External",
      "value": "3000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 42,
      "parameter_name": "MVLQ",
      "tex": "M_U",
      "description": "Vector leptoquark U1 mass"
    },
    {
      "name": "WVLQ",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 42,
      "parameter_name": "WVLQ",
      "tex": "\\Gamma_U",
      "description": "Vector leptoquark U1 width"
    },
    {
      "name": "MZp",
      "parameter_type": "External",
      "value": "3000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 43,
      "parameter_name": "MZp",
      "tex": "M_{Z'}",
      "description": "Zprime mass"
    },
    {
      "name": "WZp",
      "parameter_type": "External",
      "value": "600.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 43,
      "parameter_name": "WZp",
      "tex": "\\Gamma_{Z'}",
      "description": "Zprime width"
    },
    {
      "name": "MGp",
      "parameter_type": "External",
      "value": "4000.",
      "complex": false,
      "block_name": "MASS",
      "order_block": 44,
      "parameter_name": "MGp",
      "tex": "M_{G'}",
      "description": "Coloron mass"
    },
    {
      "name": "WGp",
      "parameter_type": "External",
      "value": "800.",
      "complex": false,
      "block_name": "DECAY",
      "order_block": 44,
      "parameter_name": "WGp",
      "tex": "\\Gamma_{G'}",
      "description": "Coloron width"
    },
    {
      "name": "gU",
      "parameter_type": "External",
      "value": "3.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gU",
      "tex": "g_U",
      "description": "Overall U1 leptoquark coupling strength"
    },
    {
      "name": "betaL33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 2,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "betaL33",
      "tex": "\\beta^L_{33}",
      "description": "U1 left-handed b tau coupling"
    },
    {
      "name": "betaRd33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 3,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "betaRd33",
      "tex": "\\beta^R_{33}",
      "description": "U1 right-handed b tau coupling"
    },
    {
      "name": "betaL23",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 4,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "betaL23",
      "tex": "\\beta^L_{23}",
      "description": "U1 left-handed s tau coupling"
    },
    {
      "name": "betaL32",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 5,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "betaL32",
      "tex": "\\beta^L_{32}",
      "description": "U1 left-handed b mu coupling"
    },
    {
      "name": "kappaU",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 6,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaU",
      "tex": "\\kappa_U",
      "description": "Non-minimal U1 coupling to gluons"
    },
    {
      "name": "kappaUtilde",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPLQCOUP",
      "order_block": 7,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaUtilde",
      "tex": "\\tilde{\\kappa}_U",
      "description": "Non-minimal U1 coupling to hypercharge"
    },
    {
      "name": "gZp",
      "parameter_type": "External",
      "value": "3.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gZp",
      "tex": "g_{Z'}",
      "description": "Overall Zprime coupling strength"
    },
    {
      "name": "zetaq33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 2,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaq33",
      "tex": "\\zeta^q_{33}",
      "description": "Zprime left-handed third-generation quark coupling"
    },
    {
      "name": "zetal33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 3,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetal33",
      "tex": "\\zeta^\\ell_{33}",
      "description": "Zprime left-handed third-generation lepton coupling"
    },
    {
      "name": "zetaRu33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 4,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaRu33",
      "tex": "\\zeta^u_{33}",
      "description": "Zprime right-handed top coupling"
    },
    {
      "name": "zetaRd33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 5,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaRd33",
      "tex": "\\zeta^d_{33}",
      "description": "Zprime right-handed bottom coupling"
    },
    {
      "name": "zetaRe33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 6,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaRe33",
      "tex": "\\zeta^e_{33}",
      "description": "Zprime right-handed tau coupling"
    },
    {
      "name": "zetaqll",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 7,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaqll",
      "tex": "\\zeta^q_{ll}",
      "description": "Zprime left-handed light-quark coupling"
    },
    {
      "name": "zetal22",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 8,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetal22",
      "tex": "\\zeta^\\ell_{22}",
      "description": "Zprime left-handed muon-doublet coupling"
    },
    {
      "name": "zetal23",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 9,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetal23",
      "tex": "\\zeta^\\ell_{23}",
      "description": "Zprime left-handed mu-tau flavour-violating coupling"
    },
    {
      "name": "zetaRull",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 10,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaRull",
      "tex": "\\zeta^u_{ll}",
      "description": "Zprime right-handed light up-quark coupling"
    },
    {
      "name": "zetaRdll",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 11,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaRdll",
      "tex": "\\zeta^d_{ll}",
      "description": "Zprime right-handed light down-quark coupling"
    },
    {
      "name": "zetaRe22",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPZPCOUP",
      "order_block": 12,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "zetaRe22",
      "tex": "\\zeta^e_{22}",
      "description": "Zprime right-handed muon coupling"
    },
    {
      "name": "gGp",
      "parameter_type": "External",
      "value": "3.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 1,
      "interaction_order": [
        "NP",
        1
      ],
      "parameter_name": "gGp",
      "tex": "g_{G'}",
      "description": "Overall coloron coupling strength"
    },
    {
      "name": "kappaq33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 2,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaq33",
      "tex": "\\kappa^q_{33}",
      "description": "Coloron left-handed third-generation quark coupling"
    },
    {
      "name": "kappaRu33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 3,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaRu33",
      "tex": "\\kappa^u_{33}",
      "description": "Coloron right-handed top coupling"
    },
    {
      "name": "kappaRd33",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 4,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaRd33",
      "tex": "\\kappa^d_{33}",
      "description": "Coloron right-handed bottom coupling"
    },
    {
      "name": "kappaqll",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 5,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaqll",
      "tex": "\\kappa^q_{ll}",
      "description": "Coloron left-handed light-quark coupling"
    },
    {
      "name": "kappaRull",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 6,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaRull",
      "tex": "\\kappa^u_{ll}",
      "description": "Coloron right-handed light up-quark coupling"
    },
    {
      "name": "kappaRdll",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 7,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaRdll",
      "tex": "\\kappa^d_{ll}",
      "description": "Coloron right-handed light down-quark coupling"
    },
    {
      "name": "kappaG1",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 8,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaG1",
      "tex": "\\kappa_{G'}",
      "description": "Coloron kinetic mixing with the gluon field strength"
    },
    {
      "name": "kappaG2",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NPGPCOUP",
      "order_block": 9,
      "interaction_order": [
        "NP",
        0
      ],
      "parameter_name": "kappaG2",
      "tex": "\\tilde{\\kappa}_{G'}",
      "description": "Non-minimal coloron coupling to gluons"
    },
    {
      "name": "newCKM",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "unitary": true,
      "value_rules": [
        {
          "lhs": "newCKM[1,1]",
          "rhs": "0.97431"
        },
        {
          "lhs": "newCKM[1,2]",
          "rhs": "0.22514"
        },
        {
          "lhs": "newCKM[1,3]",
          "rhs": "0.00371*Exp[-68.8*I*Pi/180]"
        },
        {
          "lhs": "newCKM[2,1]",
          "rhs": "-0.22504*Exp[0.0341*I*Pi/180]"
        },
        {
          "lhs": "newCKM[2,2]",
          "rhs": "0.97353*Exp[-0.00182*I*Pi/180]"
        },
        {
          "lhs": "newCKM[2,3]",
          "rhs": "0.0397"
        },
        {
          "lhs": "newCKM[3,1]",
          "rhs": "0.00837*Exp[-23.6*I*Pi/180]"
        },
        {
          "lhs": "newCKM[3,2]",
          "rhs": "-0.0390*Exp[1.137*I*Pi/180]"
        },
        {
          "lhs": "newCKM[3,3]",
          "rhs": "0.999200"
        }
      ],
      "tex": "V_{CKM}'",
      "description": "CKM matrix in the down-aligned basis"
    },
    {
      "name": "betaL",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [
        {
          "lhs": "betaL[1,2]",
          "rhs": "0",
          "delayed": true
        },
        {
          "lhs": "betaL[i_?NumericQ,1]",
          "rhs": "0",
          "delayed": true
        },
        {
          "lhs": "betaL[2,2]",
          "rhs": "0"
        }
      ],
      "value_rules": [
        {
          "lhs": "betaL[1,3]",
          "rhs": "Conjugate[newCKM[3,1]/newCKM[3,2]]*betaL23"
        },
        {
          "lhs": "betaL[2,3]",
          "rhs": "betaL23"
        },
        {
          "lhs": "betaL[3,2]",
          "rhs": "betaL32"
        },
        {
          "lhs": "betaL[3,3]",
          "rhs": "betaL33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\beta_L",
      "description": "U1 left-handed coupling matrix"
    },
    {
      "name": "betaRd",
      "parameter_type": "Internal",
      "complex": false,
      "indices": [
        "Generation",
        "Generation"
      ],
      "definitions": [
        {
          "lhs": "betaRd[1,j_?NumericQ]",
          "rhs": "0",
          "delayed": true
        },
        {
          "lhs": "betaRd[i_?NumericQ,1]",
          "rhs": "0",
          "delayed": true
        },
        {
          "lhs": "betaRd[2,i_?NumericQ]",
          "rhs": "0",
          "delayed": true
        },
        {
          "lhs": "betaRd[i_?NumericQ,2]",
          "rhs": "0",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "betaRd[3,3]",
          "rhs": "betaRd33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\beta_R^d",
      "description": "U1 right-handed down-lepton coupling matrix"
    },
    {
      "name": "zetaq",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "zetaq[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "zetaq[1,1]",
          "rhs": "zetaqll"
        },
        {
          "lhs": "zetaq[2,2]",
          "rhs": "zetaqll"
        },
        {
          "lhs": "zetaq[3,3]",
          "rhs": "zetaq33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\zeta_q",
      "description": "Zprime left-handed quark coupling matrix"
    },
    {
      "name": "zetal",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "zetal[i_?NumericQ,1]",
          "rhs": "0",
          "delayed": true
        },
        {
          "lhs": "zetal[1,i_?NumericQ]",
          "rhs": "0",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "zetal[2,2]",
          "rhs": "zetal22"
        },
        {
          "lhs": "zetal[3,3]",
          "rhs": "zetal33"
        },
        {
          "lhs": "zetal[2,3]",
          "rhs": "zetal23"
        },
        {
          "lhs": "zetal[3,2]",
          "rhs": "Conjugate[zetal23]"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\zeta_\\ell",
      "description": "Zprime left-handed lepton coupling matrix"
    },
    {
      "name": "zetaRu",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "zetaRu[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "zetaRu[1,1]",
          "rhs": "zetaRull"
        },
        {
          "lhs": "zetaRu[2,2]",
          "rhs": "zetaRull"
        },
        {
          "lhs": "zetaRu[3,3]",
          "rhs": "zetaRu33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\zeta_u",
      "description": "Zprime right-handed up-quark coupling matrix"
    },
    {
      "name": "zetaRd",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "zetaRd[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "zetaRd[1,1]",
          "rhs": "zetaRdll"
        },
        {
          "lhs": "zetaRd[2,2]",
          "rhs": "zetaRdll"
        },
        {
          "lhs": "zetaRd[3,3]",
          "rhs": "zetaRd33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\zeta_d",
      "description": "Zprime right-handed down-quark coupling matrix"
    },
    {
      "name": "zetaRe",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "zetaRe[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        },
        {
          "lhs": "zetaRe[1,1]",
          "rhs": "0",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "zetaRe[2,2]",
          "rhs": "zetaRe22"
        },
        {
          "lhs": "zetaRe[3,3]",
          "rhs": "zetaRe33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\zeta_e",
      "description": "Zprime right-handed charged-lepton coupling matrix"
    },
    {
      "name": "kappaL",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "kappaL[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "kappaL[1,1]",
          "rhs": "kappaqll"
        },
        {
          "lhs": "kappaL[2,2]",
          "rhs": "kappaqll"
        },
        {
          "lhs": "kappaL[3,3]",
          "rhs": "kappaq33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\kappa_q",
      "description": "Coloron left-handed quark coupling matrix"
    },
    {
      "name": "kappaRu",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "kappaRu[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "kappaRu[1,1]",
          "rhs": "kappaRull"
        },
        {
          "lhs": "kappaRu[2,2]",
          "rhs": "kappaRull"
        },
        {
          "lhs": "kappaRu[3,3]",
          "rhs": "kappaRu33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\kappa_u",
      "description": "Coloron right-handed up-quark coupling matrix"
    },
    {
      "name": "kappaRd",
      "parameter_type": "Internal",
      "complex": true,
      "indices": [
        "Generation",
        "Generation"
      ],
      "hermitian": true,
      "definitions": [
        {
          "lhs": "kappaRd[i_?NumericQ,j_?NumericQ]",
          "rhs": "0 /; (i =!= j)",
          "delayed": true
        }
      ],
      "value_rules": [
        {
          "lhs": "kappaRd[1,1]",
          "rhs": "kappaRdll"
        },
        {
          "lhs": "kappaRd[2,2]",
          "rhs": "kappaRdll"
        },
        {
          "lhs": "kappaRd[3,3]",
          "rhs": "kappaRd33"
        }
      ],
      "interaction_order": [
        "NP",
        0
      ],
      "tex": "\\kappa_d",
      "description": "Coloron right-handed down-quark coupling matrix"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "VLQ",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "sym": "MVLQ",
        "value": "3000."
      },
      "width": {
        "sym": "WVLQ",
        "value": "600."
      },
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "2/3",
        "Colour": "3",
        "SU2": "1",
        "LeptonNumber": "-1"
      },
      "pdg": 42,
      "particle_name": "VLQ",
      "antiparticle_name": "VLQ~",
      "full_name": "Vector leptoquark U1",
      "propagator_label": "VLQ",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "U",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "quantum_numbers": {
        "Q": "2/3",
        "Y": "2/3",
        "Colour": "3",
        "SU2": "1"
      },
      "unphysical": true,
      "definitions": [
        "U[mu_,cc_] -> VLQ[mu,cc]"
      ]
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "Zp",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "sym": "MZp",
        "value": "3000."
      },
      "width": {
        "sym": "WZp",
        "value": "600."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1"
      },
      "pdg": 43,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 103,
      "class_name": "Gp",
      "self_conjugate": true,
      "indices": [
        "Gluon"
      ],
      "mass": {
        "sym": "MGp",
        "value": "4000."
      },
      "width": {
        "sym": "WGp",
        "value": "800."
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "8",
        "SU2": "1"
      },
      "pdg": 44,
      "particle_name": "Gp",
      "full_name": "Color-octet coloron",
      "propagator_label": "Gp",
      "propagator_type": "C",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LVLQKin",
      "expression": "Block[{mu,nu,cc1}, -1/2*(DC[Ubar[mu,cc1],nu] - DC[Ubar[nu,cc1],mu])*(DC[U[mu,cc1],nu] - DC[U[nu,cc1],mu])]",
      "delayed": true
    },
    {
      "name": "LVLQF",
      "expression": "Block[{ff1,ff2,ff3,s1,s2,s3,cc1,mu}, gU/Sqrt[2]*VLQ[mu,cc1]*(betaL[ff1,ff2]*newCKM[ff3,ff1]*uqbar[s1,ff3,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*vl[s3,ff2] + betaL[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*l[s3,ff2] + betaRd[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjP[s2,s3]*l[s3,ff2])]",
      "delayed": true
    },
    {
      "name": "LVLQG",
      "expression": "Block[{cc1,cc2,aa1,mu,nu}, -I*gs*(1 - kappaU)*Ubar[mu,cc1]*T[aa1,cc1,cc2]*U[nu,cc2]*FS[G,mu,nu,aa1] - I*2/3*g1*(1 - kappaUtilde)*Ubar[mu,cc1]*U[nu,cc1]*FS[B,mu,nu]]",
      "delayed": true
    },
    {
      "name": "LZpF",
      "expression": "Block[{ff1,ff2,ff3,ff4,s1,s2,s3,mu,cc1}, gZp/(2*Sqrt[6])*Zp[mu]*(zetaq[ff1,ff2]*newCKM[ff3,ff1]*uqbar[s1,ff3,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*Conjugate[newCKM[ff4,ff2]]*uq[s3,ff4,cc1] + zetaq[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*dq[s3,ff2,cc1] - 3*zetal[ff1,ff2]*lbar[s1,ff1]*Ga[mu,s1,s2]*ProjM[s2,s3]*l[s3,ff2] - 3*zetal[ff1,ff2]*vlbar[s1,ff1]*Ga[mu,s1,s2]*ProjM[s2,s3]*vl[s3,ff2] + zetaRu[ff1,ff2]*uqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjP[s2,s3]*uq[s3,ff2,cc1] + zetaRd[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjP[s2,s3]*dq[s3,ff2,cc1] - 3*zetaRe[ff1,ff2]*lbar[s1,ff1]*Ga[mu,s1,s2]*ProjP[s2,s3]*l[s3,ff2])]",
      "delayed": true
    },
    {
      "name": "LGpKin",
      "expression": "Block[{mu,nu,aa1}, -1/4*(DC[Gp[mu,aa1],nu] - DC[Gp[nu,aa1],mu])*(DC[Gp[mu,aa1],nu] - DC[Gp[nu,aa1],mu])]",
      "delayed": true
    },
    {
      "name": "LGpF",
      "expression": "Block[{ff1,ff2,ff3,ff4,s1,s2,s3,aa1,cc1,cc2,mu}, gGp*Gp[mu,aa1]*(kappaL[ff1,ff2]*newCKM[ff3,ff1]*uqbar[s1,ff3,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjM[s2,s3]*Conjugate[newCKM[ff4,ff2]]*uq[s3,ff4,cc2] + kappaL[ff1,ff2]*dqbar[s1,ff1,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjM[s2,s3]*dq[s3,ff2,cc2] + kappaRu[ff1,ff2]*uqbar[s1,ff1,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjP[s2,s3]*uq[s3,ff2,cc2] + kappaRd[ff1,ff2]*dqbar[s1,ff1,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjP[s2,s3]*dq[s3,ff2,cc2])]",
      "delayed": true
    },
    {
      "name": "LGpG",
      "expression": "Block[{aa1,aa2,aa3,mu,nu}, 1/2*kappaG1*(DC[Gp[nu,aa1],mu] - DC[Gp[mu,aa1],nu])*FS[G,mu,nu,aa1] + gs*kappaG2*f[aa1,aa2,aa3]*Gp[mu,aa1]*Gp[nu,aa2]*FS[G,mu,nu,aa3]]",
      "delayed": true
    },
    {
      "name": "LLeptoQuark",
      "expression": "LVLQKin + LVLQF + HC[LVLQF] + LVLQG + LZpF + LGpKin + LGpF + LGpG",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```