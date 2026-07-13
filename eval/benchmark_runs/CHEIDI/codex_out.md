```json
{
  "model_name": "CHEIDI_gen",
  "info": {
    "authors": [
      "C. Speckner"
    ],
    "version": "0.1",
    "date": "30.07.2010",
    "institutions": [
      "Universitaet Freiburg"
    ],
    "emails": [
      "Christian.Speckner@physik.uni-freiburg.de"
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
      1
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": false,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Heidi",
      "range_kind": "NoUnfold",
      "size": 10,
      "style_symbol": "k"
    }
  ],
  "parameters": [
    {
      "name": "Heidi$v",
      "parameter_type": "External",
      "value": "246.22",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 1,
      "tex": "v",
      "description": "Higgs vacuum expectation value used for the HEIDI spectrum"
    },
    {
      "name": "Heidi$mh",
      "parameter_type": "External",
      "value": "120.",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 2,
      "tex": "m_h",
      "description": "Unmixed Higgs mass parameter used for the HEIDI spectrum"
    },
    {
      "name": "Heidi$cs",
      "parameter_type": "External",
      "value": "100.",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 3,
      "tex": "M_c",
      "description": "Compactification scale"
    },
    {
      "name": "Heidi$mb",
      "parameter_type": "External",
      "value": "100.",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 4,
      "tex": "m_b",
      "description": "Bulk scalar mass"
    },
    {
      "name": "Heidi$g2",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 5,
      "interaction_order": [
        "NP",
        2
      ],
      "tex": "g_5^2",
      "description": "Five-dimensional trilinear mixing coupling squared"
    },
    {
      "name": "Heidi$cutoff",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 6,
      "tex": "\\Lambda",
      "description": "Cutoff scale determining the number of HEIDI modes"
    },
    {
      "name": "Heidi$nmodes",
      "parameter_type": "External",
      "value": "10",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 7,
      "tex": "N_H",
      "description": "Number of HEIDI scalar mass eigenstates retained when no cutoff is used"
    },
    {
      "name": "xi",
      "parameter_type": "External",
      "complex": false,
      "indices": [
        "Heidi"
      ],
      "value_rules": [
        {
          "lhs": "xi[n_]",
          "rhs": "HeidiWavefunction[n - 1, 0]",
          "delayed": false
        }
      ],
      "tex": "\\xi",
      "description": "Higgs wave function component of each HEIDI mass eigenstate",
      "allow_summation": true
    },
    {
      "name": "kggh",
      "parameter_type": "External",
      "value": "1",
      "complex": false,
      "block_name": "HEIDI",
      "order_block": 8,
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "K_{ggh}",
      "description": "K factor for the optional effective scalar-gluon-gluon coupling"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "Hh",
      "self_conjugate": true,
      "indices": [
        "Heidi"
      ],
      "flavor_index": "Heidi",
      "class_members": [
        "Hh1",
        "Hh2",
        "Hh3",
        "Hh4",
        "Hh5",
        "Hh6",
        "Hh7",
        "Hh8",
        "Hh9",
        "Hh10"
      ],
      "mass": {
        "sym": "mhh",
        "members": [
          [
            "mhh1",
            "HeidiMass[0]"
          ],
          [
            "mhh2",
            "HeidiMass[1]"
          ],
          [
            "mhh3",
            "HeidiMass[2]"
          ],
          [
            "mhh4",
            "HeidiMass[3]"
          ],
          [
            "mhh5",
            "HeidiMass[4]"
          ],
          [
            "mhh6",
            "HeidiMass[5]"
          ],
          [
            "mhh7",
            "HeidiMass[6]"
          ],
          [
            "mhh8",
            "HeidiMass[7]"
          ],
          [
            "mhh9",
            "HeidiMass[8]"
          ],
          [
            "mhh10",
            "HeidiMass[9]"
          ]
        ]
      },
      "width": {
        "sym": "whh",
        "members": [
          [
            "whh1",
            "HeidiWidth[0]"
          ],
          [
            "whh2",
            "HeidiWidth[1]"
          ],
          [
            "whh3",
            "HeidiWidth[2]"
          ],
          [
            "whh4",
            "HeidiWidth[3]"
          ],
          [
            "whh5",
            "HeidiWidth[4]"
          ],
          [
            "whh6",
            "HeidiWidth[5]"
          ],
          [
            "whh7",
            "HeidiWidth[6]"
          ],
          [
            "whh8",
            "HeidiWidth[7]"
          ],
          [
            "whh9",
            "HeidiWidth[8]"
          ],
          [
            "whh10",
            "HeidiWidth[9]"
          ]
        ]
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0",
        "Colour": "1",
        "SU2": "1"
      },
      "pdg": [
        990001,
        990002,
        990003,
        990004,
        990005,
        990006,
        990007,
        990008,
        990009,
        990010
      ],
      "particle_name": [
        "Hh1",
        "Hh2",
        "Hh3",
        "Hh4",
        "Hh5",
        "Hh6",
        "Hh7",
        "Hh8",
        "Hh9",
        "Hh10"
      ],
      "full_name": [
        "HEIDI scalar mode 1",
        "HEIDI scalar mode 2",
        "HEIDI scalar mode 3",
        "HEIDI scalar mode 4",
        "HEIDI scalar mode 5",
        "HEIDI scalar mode 6",
        "HEIDI scalar mode 7",
        "HEIDI scalar mode 8",
        "HEIDI scalar mode 9",
        "HEIDI scalar mode 10"
      ],
      "propagator_label": [
        "Hh1",
        "Hh2",
        "Hh3",
        "Hh4",
        "Hh5",
        "Hh6",
        "Hh7",
        "Hh8",
        "Hh9",
        "Hh10"
      ],
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LHEIDI",
      "expression": "(LSM /. {muH -> 0, \\[Lambda] -> 0}) /. H -> (Hh[n]*xi[n])",
      "delayed": true
    },
    {
      "name": "LHEIDIgg",
      "expression": "Block[{fun, piece, tt, mm, hh}, tt[m_] := 4*MT^2/m^2; fun[tau_] := tau*(1 + (1 - tau)*If[NumericalValue[tau] > 1, ArcSin[Sqrt[1/tau]]^2, -1/4*(Log[(1 + Sqrt[1 + tau])/(1 - Sqrt[1 - tau])] - I*Pi)^2]); mm[n_] := Symbol[\"mhh\" <> ToString[n]]; hh[n_] := Symbol[\"Hh\" <> ToString[n]]; piece[n_] := Sqrt[kggh]*gs^2/32/Pi^2/v*fun[tt[mm[n]]]*xi[n]*hh[n]*(del[G[mu, a], nu] - del[G[nu, a], mu])^2; Plus @@ (piece /@ Range[Heidi$nmodes])]",
      "delayed": true
    },
    {
      "name": "LHEIDIggHeavyTop",
      "expression": "Block[{piece, mm, hh}, mm[n_] := Symbol[\"mhh\" <> ToString[n]]; hh[n_] := Symbol[\"Hh\" <> ToString[n]]; piece[n_] := Sqrt[kggh]*gs^2/32/Pi^2/v*(2/3)*xi[n]*hh[n]*(del[G[mu, a], nu] - del[G[nu, a], mu])^2; Plus @@ (piece /@ Range[Heidi$nmodes])]",
      "delayed": true
    }
  ],
  "raw_preamble": [
    "Needs[\"Heidi`\"];",
    "InitHeidi[Heidi$v, Heidi$mh, Heidi$cs, Heidi$mb, Heidi$g2];",
    "If[NumericQ[Heidi$cutoff], Heidi$nmodes = FixedPoint[If[HeidiMass[#] < Heidi$cutoff, # + 1, #]&, 0]];"
  ],
  "raw_blocks": [
    "LHEIDI::usage = \"LHEIDI: HEIDI lagrangian\";",
    "LHEIDIgg::usage = \"LHEIDIgg[mode]: HEIDI effective scalar-gluon-gluon couplings; mode may be \\\"heavytop\\\"\";"
  ]
}
```