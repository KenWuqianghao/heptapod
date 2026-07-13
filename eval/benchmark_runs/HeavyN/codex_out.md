```json
{
  "model_name": "HeavyN_gen",
  "info": {
    "authors": [
      "Celine Degrande",
      "Olivier Mattelaer",
      "Richard Ruiz",
      "Jessica Turner"
    ],
    "version": "1.0.0",
    "date": "2026-07-13",
    "institutions": [
      "Institute for Particle Physics Phenomenology, Durham University"
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
    ],
    [
      "NP",
      1
    ]
  ],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "VeN1",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 1,
      "tex": "Subscript[V,eN1]",
      "description": "Mixing between electron-neutrino flavor state and N1 mass state"
    },
    {
      "name": "VeN2",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 2,
      "tex": "Subscript[V,eN2]",
      "description": "Mixing between electron-neutrino flavor state and N2 mass state"
    },
    {
      "name": "VeN3",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 3,
      "tex": "Subscript[V,eN3]",
      "description": "Mixing between electron-neutrino flavor state and N3 mass state"
    },
    {
      "name": "VmuN1",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 4,
      "tex": "Subscript[V,muN1]",
      "description": "Mixing between muon-neutrino flavor state and N1 mass state"
    },
    {
      "name": "VmuN2",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 5,
      "tex": "Subscript[V,muN2]",
      "description": "Mixing between muon-neutrino flavor state and N2 mass state"
    },
    {
      "name": "VmuN3",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 6,
      "tex": "Subscript[V,muN3]",
      "description": "Mixing between muon-neutrino flavor state and N3 mass state"
    },
    {
      "name": "VtaN1",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 7,
      "tex": "Subscript[V,taN1]",
      "description": "Mixing between tau-neutrino flavor state and N1 mass state"
    },
    {
      "name": "VtaN2",
      "parameter_type": "External",
      "value": "0.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 8,
      "tex": "Subscript[V,taN2]",
      "description": "Mixing between tau-neutrino flavor state and N2 mass state"
    },
    {
      "name": "VtaN3",
      "parameter_type": "External",
      "value": "1.0",
      "complex": false,
      "block_name": "NUMIXING",
      "order_block": 9,
      "tex": "Subscript[V,taN3]",
      "description": "Mixing between tau-neutrino flavor state and N3 mass state"
    },
    {
      "name": "gN",
      "parameter_type": "Internal",
      "complex": false,
      "definitions": [
        {
          "lhs": "gN",
          "rhs": "ee/sw",
          "delayed": false
        }
      ],
      "interaction_order": [
        "NP",
        1
      ],
      "tex": "Subscript[g,N]",
      "description": "Weak coupling used in heavy-neutrino interactions, equal to ee/sw"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 131,
      "class_name": "N1",
      "self_conjugate": true,
      "mass": {
        "sym": "mN1",
        "value": "300."
      },
      "width": {
        "sym": "WN1",
        "value": "0.303"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 9900012,
      "particle_name": "N1",
      "full_name": "Heavy Majorana neutrino N1, colour singlet and SU(2)L singlet",
      "propagator_label": "N1",
      "propagator_type": "Straight",
      "propagator_arrow": "False"
    },
    {
      "spin_type": "F",
      "class_index": 132,
      "class_name": "N2",
      "self_conjugate": true,
      "mass": {
        "sym": "mN2",
        "value": "500."
      },
      "width": {
        "sym": "WN2",
        "value": "1.50"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 9900014,
      "particle_name": "N2",
      "full_name": "Heavy Majorana neutrino N2, colour singlet and SU(2)L singlet",
      "propagator_label": "N2",
      "propagator_type": "Straight",
      "propagator_arrow": "False"
    },
    {
      "spin_type": "F",
      "class_index": 133,
      "class_name": "N3",
      "self_conjugate": true,
      "mass": {
        "sym": "mN3",
        "value": "1000."
      },
      "width": {
        "sym": "WN3",
        "value": "12.3"
      },
      "quantum_numbers": {
        "Q": "0",
        "Y": "0"
      },
      "pdg": 9900016,
      "particle_name": "N3",
      "full_name": "Heavy Majorana neutrino N3, colour singlet and SU(2)L singlet",
      "propagator_label": "N3",
      "propagator_type": "Straight",
      "propagator_arrow": "False"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNKin",
      "expression": "I/2 N1bar[s1].Ga[v,s1,s2].del[N1[s2],v] - 1/2 mN1 N1bar[s1] N1[s1] + I/2 N2bar[s1].Ga[v,s1,s2].del[N2[s2],v] - 1/2 mN2 N2bar[s1] N2[s1] + I/2 N3bar[s1].Ga[v,s1,s2].del[N3[s2],v] - 1/2 mN3 N3bar[s1] N3[s1]",
      "delayed": true
    },
    {
      "name": "LNCCbare",
      "expression": "gN/Sqrt[2]*(VeN1*N1bar.W[m].ProjM[m].e + VmuN1*N1bar.W[m].ProjM[m].mu + VtaN1*N1bar.W[m].ProjM[m].ta) + gN/Sqrt[2]*(VeN2*N2bar.W[m].ProjM[m].e + VmuN2*N2bar.W[m].ProjM[m].mu + VtaN2*N2bar.W[m].ProjM[m].ta) + gN/Sqrt[2]*(VeN3*N3bar.W[m].ProjM[m].e + VmuN3*N3bar.W[m].ProjM[m].mu + VtaN3*N3bar.W[m].ProjM[m].ta)",
      "delayed": true
    },
    {
      "name": "LNCC",
      "expression": "LNCCbare + HC[LNCCbare]",
      "delayed": true
    },
    {
      "name": "LNNCBare",
      "expression": "1/2*gN/cw*(VeN1*N1bar.Z[m].ProjM[m].ve + VmuN1*N1bar.Z[m].ProjM[m].vm + VtaN1*N1bar.Z[m].ProjM[m].vt) + 1/2*gN/cw*(VeN2*N2bar.Z[m].ProjM[m].ve + VmuN2*N2bar.Z[m].ProjM[m].vm + VtaN2*N2bar.Z[m].ProjM[m].vt) + 1/2*gN/cw*(VeN3*N3bar.Z[m].ProjM[m].ve + VmuN3*N3bar.Z[m].ProjM[m].vm + VtaN3*N3bar.Z[m].ProjM[m].vt)",
      "delayed": true
    },
    {
      "name": "LNNC",
      "expression": "LNNCBare + HC[LNNCBare]",
      "delayed": true
    },
    {
      "name": "LNHbare",
      "expression": "-gN*mN1/(2*MW)*(VeN1*N1bar.ProjM.ve H + VmuN1*N1bar.ProjM.vm H + VtaN1*N1bar.ProjM.vt H) - gN*mN2/(2*MW)*(VeN2*N2bar.ProjM.ve H + VmuN2*N2bar.ProjM.vm H + VtaN2*N2bar.ProjM.vt H) - gN*mN3/(2*MW)*(VeN3*N3bar.ProjM.ve H + VmuN3*N3bar.ProjM.vm H + VtaN3*N3bar.ProjM.vt H)",
      "delayed": true
    },
    {
      "name": "LNH",
      "expression": "LNHbare + HC[LNHbare]",
      "delayed": true
    },
    {
      "name": "LNGbare",
      "expression": "I*gN*mN1/(2*MW)*(VeN1*vebar.ProjP.N1 G0 + VmuN1*vmbar.ProjP.N1 G0 + VtaN1*vtbar.ProjP.N1 G0) + I*gN*mN2/(2*MW)*(VeN2*vebar.ProjP.N2 G0 + VmuN2*vmbar.ProjP.N2 G0 + VtaN2*vtbar.ProjP.N2 G0) + I*gN*mN3/(2*MW)*(VeN3*vebar.ProjP.N3 G0 + VmuN3*vmbar.ProjP.N3 G0 + VtaN3*vtbar.ProjP.N3 G0) + I*gN*mN1/(Sqrt[2]*MW)*(VeN1*ebar.ProjP.N1 GPbar + VmuN1*mubar.ProjP.N1 GPbar + VtaN1*tabar.ProjP.N1 GPbar) + I*gN*mN2/(Sqrt[2]*MW)*(VeN2*ebar.ProjP.N2 GPbar + VmuN2*mubar.ProjP.N2 GPbar + VtaN2*tabar.ProjP.N2 GPbar) + I*gN*mN3/(Sqrt[2]*MW)*(VeN3*ebar.ProjP.N3 GPbar + VmuN3*mubar.ProjP.N3 GPbar + VtaN3*tabar.ProjP.N3 GPbar)",
      "delayed": true
    },
    {
      "name": "LNG",
      "expression": "LNGbare + HC[LNGbare]",
      "delayed": true
    },
    {
      "name": "LN",
      "expression": "LNKin + LNCC + LNNC + LNH + LNG",
      "delayed": true
    },
    {
      "name": "LFull",
      "expression": "LSM + LN",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```