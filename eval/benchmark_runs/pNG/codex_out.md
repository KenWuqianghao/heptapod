```json
{
  "model_name": "pNG_gen",
  "info": {
    "authors": [
      "Chiara Arina",
      "Ankit Beniwal",
      "Celine Degrande",
      "Jan Heisig",
      "Andre Scaffidi"
    ],
    "version": "1.0.0",
    "date": "April 2019",
    "institutions": [
      "Universite catholique de Louvain (CP3)",
      "University of Adelaide"
    ],
    "emails": [
      "chiara.arina@uclouvain.be",
      "ankit.beniwal@uclouvain.be",
      "celine.degrande@uclouvain.be",
      "jan.heisig@uclouvain.be",
      "andre.scaffidi@adelaide.edu.au"
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
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": false,
  "vevs": [
    [
      "Phi[2]",
      "vh"
    ],
    [
      "S",
      "vs"
    ]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "vs",
      "parameter_type": "External",
      "value": "300",
      "block_name": "PNGINPUTS",
      "order_block": 1,
      "interaction_order": [
        "QED",
        -1
      ],
      "parameter_name": "vs",
      "tex": "Subscript[v,s]",
      "description": "Second scalar VEV (GeV)"
    },
    {
      "name": "theta",
      "parameter_type": "External",
      "value": "0.7854",
      "block_name": "PNGINPUTS",
      "order_block": 2,
      "parameter_name": "theta",
      "tex": "theta",
      "description": "Mixing angle between the CP-even scalars"
    },
    {
      "name": "ct",
      "parameter_type": "Internal",
      "value": "Cos[theta]",
      "tex": "Cos[theta]",
      "description": "Cosine of theta"
    },
    {
      "name": "st",
      "parameter_type": "Internal",
      "value": "Sin[theta]",
      "tex": "Sin[theta]",
      "description": "Sine of theta"
    },
    {
      "name": "lambdaP",
      "parameter_type": "Internal",
      "value": "((Mh ct)^2 + (Mh2 st)^2)/(vh^2)",
      "interaction_order": [
        "QED",
        2
      ],
      "tex": "Subscript[lambda,Phi]",
      "description": "Higgs quartic coupling"
    },
    {
      "name": "lambdaS",
      "parameter_type": "Internal",
      "value": "((Mh st)^2 + (Mh2 ct)^2)/(vs^2)",
      "interaction_order": [
        "QED",
        2
      ],
      "tex": "Subscript[lambda,S]",
      "description": "Singlet scalar quartic coupling"
    },
    {
      "name": "lambdaPS",
      "parameter_type": "Internal",
      "value": "((Mh2^2 - Mh^2) st ct)/(vh vs)",
      "interaction_order": [
        "QED",
        2
      ],
      "tex": "Subscript[lambda,Phi S]",
      "description": "Higgs portal coupling"
    },
    {
      "name": "muSpsq",
      "parameter_type": "Internal",
      "value": "mX^2",
      "tex": "Subscript[mu,S]^prime^2",
      "description": "Soft U(1)-breaking mass-squared parameter"
    },
    {
      "name": "muPsq",
      "parameter_type": "Internal",
      "value": "lambdaP vh^2 + lambdaPS vs^2",
      "tex": "Subscript[mu,Phi]^2",
      "description": "Higgs bare mass squared"
    },
    {
      "name": "muSsq",
      "parameter_type": "Internal",
      "value": "lambdaS vs^2 + lambdaPS vh^2 - muSpsq",
      "tex": "Subscript[mu,S]^2",
      "description": "Singlet bare mass squared"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 2,
      "class_name": "h2",
      "self_conjugate": true,
      "mass": {
        "sym": "Mh2",
        "value": "300"
      },
      "width": {
        "sym": "wh2",
        "value": "1"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 29,
      "particle_name": "h2",
      "full_name": "Second scalar H",
      "propagator_label": "h2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 3,
      "class_name": "X",
      "self_conjugate": true,
      "mass": {
        "sym": "mX",
        "value": "100"
      },
      "width": {
        "sym": "wX",
        "value": "0"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 30,
      "particle_name": "~X",
      "full_name": "pNG DM chi",
      "propagator_label": "X",
      "propagator_type": "D",
      "propagator_arrow": "None"
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
        "Phi[2] -> (vh + (ct h + st h2) + I G0)/Sqrt[2]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "S",
      "self_conjugate": false,
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "unphysical": true,
      "definitions": [
        "S -> (vs + (-st h + ct h2) + I X)/Sqrt[2]"
      ]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LHiggsPng",
      "expression": "Block[{ii, mu, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; ExpandIndices[DC[Phibar[ii], mu] DC[Phi[ii], mu] + muPsq/2 Phibar[ii] Phi[ii] - lambdaP/2 Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand -> {SU2D, SU2W}]/.feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LS",
      "expression": "del[Sbar, mu] del[S, mu] + muSsq/2 Sbar S - lambdaS/2 (Sbar S)^2",
      "delayed": true
    },
    {
      "name": "Lint",
      "expression": "Block[{ii, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; ExpandIndices[-lambdaPS Phibar[ii] Phi[ii] Sbar S, FlavorExpand -> {SU2D}]/.feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "Lsoft",
      "expression": "muSpsq/4 (S^2 + Sbar^2)",
      "delayed": true
    },
    {
      "name": "LpNG",
      "expression": "LS + Lint + Lsoft",
      "delayed": true
    },
    {
      "name": "LScalarPng",
      "expression": "LHiggsPng + LpNG",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "FR$LoopSwitches = {{Gf, MW}};",
    "FR$RmDblExt = {ymb -> MB, ymc -> MC, ymdo -> MD, yme -> Me, ymm -> MMU, yms -> MS, ymt -> MT, ymtau -> MTA, ymup -> MU};"
  ],
  "raw_blocks": []
}
```