ClearAll["Global`*"];

jsonMarker = "HEPTAPOD_WL_JSON:";

allChecks = {
  "kinetic_term_normalisation",
  "mass_spectrum",
  "hermiticity",
  "numeric_coupling_probe_efflrsm_zr"
};

skipCheck[name_, reason_] := <|
  "name" -> name,
  "passed" -> Null,
  "detail" -> reason
|>;

failCheck[name_, reason_] := <|
  "name" -> name,
  "passed" -> False,
  "detail" -> reason
|>;

passCheck[name_, detail_, value_: Null] := <|
  "name" -> name,
  "passed" -> True,
  "detail" -> detail,
  "value" -> value
|>;

safeString[value_] := ToString[value, InputForm];

runFRCheck[name_, fn_, lagExpr_] := Module[{res},
  res = Quiet @ Check[fn[lagExpr], $Failed];
  If[res === $Failed || MatchQ[res, _[lagExpr]],
    failCheck[name, "FeynRules check evaluation failed"],
    passCheck[name, "FeynRules check evaluated", safeString[res]]
  ]
];

runNumericCouplingProbe[couplings_Association, benchmark_Association] := Module[
  {hasQuark, hasLepton, sw2, kappaR, swVal, cwVal, rules, qExpr, lExpr, qVal, lVal, qOk, lOk},
  hasQuark = KeyExistsQ[couplings, "gZRq"];
  hasLepton = KeyExistsQ[couplings, "gZRl"];
  If[!(hasQuark && hasLepton),
    Return[skipCheck["numeric_coupling_probe_efflrsm_zr", "gZRq/gZRl are not present"]];
  ];

  sw2 = N @ Lookup[benchmark, "sw2", 0.2312];
  kappaR = N @ Lookup[benchmark, "kappa_R", 1.0];
  swVal = Sqrt[sw2];
  cwVal = Sqrt[1 - sw2];

  rules = {
    HoldPattern[sw] -> swVal,
    HoldPattern[cw] -> cwVal,
    HoldPattern[ee] -> 1.0,
    HoldPattern[kappa_R] -> kappaR,
    HoldPattern[kappaR] -> kappaR,
    HoldPattern[kRquark] -> kappaR,
    HoldPattern[kRlepton] -> kappaR,
    HoldPattern[kRq] -> kappaR,
    HoldPattern[kRl] -> kappaR
  };

  qExpr = Lookup[couplings, "gZRq"];
  lExpr = Lookup[couplings, "gZRl"];

  qVal = Quiet @ Check[N[ToExpression[qExpr] /. rules], $Failed];
  lVal = Quiet @ Check[N[ToExpression[lExpr] /. rules], $Failed];
  qOk = NumericQ[qVal] && Chop[Im[qVal]] == 0;
  lOk = NumericQ[lVal] && Chop[Im[lVal]] == 0;

  If[qOk && lOk,
    passCheck[
      "numeric_coupling_probe_efflrsm_zr",
      "numeric probe evaluated at benchmark point",
      <|"gZRq" -> N[qVal], "gZRl" -> N[lVal], "kappa_R" -> kappaR, "sw2" -> sw2|>
    ],
    failCheck[
      "numeric_coupling_probe_efflrsm_zr",
      "could not evaluate gZRq/gZRl numerically at benchmark point"
    ]
  ]
];

result = <|
  "schema_version" -> "wolfram-validation-1.0",
  "checks" -> (skipCheck[#, "uninitialized"] & /@ allChecks)
|>;

params = Association @ Map[
  Rule @@ StringSplit[#, "="] &,
  Rest[$ScriptCommandLine]
];

payloadPath = Lookup[params, "PayloadPath", Missing["not-found"]];
If[payloadPath === Missing["not-found"] || !FileExistsQ[payloadPath],
  result["checks"] = (failCheck[#, "PayloadPath is missing"] & /@ allChecks);
  Print[jsonMarker <> ExportString[result, "JSON", "Compact" -> True]];
  Quit[0];
];

payload = Quiet @ Check[Import[payloadPath, "RawJSON"], $Failed];
If[payload === $Failed || !AssociationQ[payload],
  result["checks"] = (failCheck[#, "payload JSON parse failed"] & /@ allChecks);
  Print[jsonMarker <> ExportString[result, "JSON", "Compact" -> True]];
  Quit[0];
];

modelPath = Lookup[payload, "model_path", ""];
feynrulesPath = Lookup[payload, "feynrules_path", ""];
lagName = Lookup[payload, "lagrangian_symbol", "LBSM"];
couplings = Lookup[payload, "coupling_expressions", <||>];
benchmark = Lookup[payload, "benchmark", <||>];

checksByName = Association[
  "kinetic_term_normalisation" -> skipCheck["kinetic_term_normalisation", "FeynRules not loaded"],
  "mass_spectrum" -> skipCheck["mass_spectrum", "FeynRules not loaded"],
  "hermiticity" -> skipCheck["hermiticity", "FeynRules not loaded"],
  "numeric_coupling_probe_efflrsm_zr" -> runNumericCouplingProbe[couplings, benchmark]
];

frReady = False;
lagExpr = $Failed;

If[StringLength[ToString[feynrulesPath]] > 0 && DirectoryQ[feynrulesPath] && FileExistsQ[modelPath],
  frm = FileNameJoin[{feynrulesPath, "FeynRules.m"}];
  loadRes = Quiet @ Check[
    If[FileExistsQ[frm],
      Get[frm],
      If[!MemberQ[$Path, feynrulesPath], AppendTo[$Path, feynrulesPath]];
      Needs["FeynRules`"]
    ],
    $Failed
  ];
  If[loadRes =!= $Failed,
    smFR = FileNameJoin[{feynrulesPath, "Models", "SM", "SM.fr"}];
    modelLoadRes = Quiet @ Check[
      If[FileExistsQ[smFR],
        LoadModel[smFR, modelPath],
        LoadModel[modelPath]
      ],
      $Failed
    ];
    If[modelLoadRes =!= $Failed,
      frReady = True;
    ];
  ];
];

If[frReady,
  lagExpr = Quiet @ Check[ToExpression[lagName], $Failed];
  If[lagExpr === $Failed,
    lagExpr = Quiet @ Check[ToExpression["LSM + LBSM"], $Failed];
  ];
  If[lagExpr === $Failed,
    checksByName["kinetic_term_normalisation"] = failCheck["kinetic_term_normalisation", "Lagrangian symbol not found"];
    checksByName["mass_spectrum"] = failCheck["mass_spectrum", "Lagrangian symbol not found"];
    checksByName["hermiticity"] = failCheck["hermiticity", "Lagrangian symbol not found"],
    checksByName["kinetic_term_normalisation"] = runFRCheck["kinetic_term_normalisation", CheckKineticTermNormalisation, lagExpr];
    checksByName["mass_spectrum"] = runFRCheck["mass_spectrum", CheckMassSpectrum, lagExpr];
    checksByName["hermiticity"] = runFRCheck["hermiticity", CheckHermiticity, lagExpr];
  ],
  checksByName["kinetic_term_normalisation"] = skipCheck["kinetic_term_normalisation", "FeynRules path/model unavailable or load failed"];
  checksByName["mass_spectrum"] = skipCheck["mass_spectrum", "FeynRules path/model unavailable or load failed"];
  checksByName["hermiticity"] = skipCheck["hermiticity", "FeynRules path/model unavailable or load failed"];
];

result["checks"] = (checksByName[#] & /@ allChecks);
result["meta"] = <|
  "model_path" -> modelPath,
  "feynrules_path" -> feynrulesPath,
  "lagrangian_symbol" -> lagName
|>;

Print[jsonMarker <> ExportString[result, "JSON", "Compact" -> True]];
Quit[0];
