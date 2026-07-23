# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: selfconjugate_quantum_numbers, hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
93 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 93.

Part::pkspec1: The expression Index[Spin, Ext[1]] cannot be used as a part specification.

Part::pkspec1: The expression Index[Spin, a] cannot be used as a part specification.

Part::pkspec1: The expression Index[Spin, Ext[2]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Q not conserved in vertex {ebar, n4, GP}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {ebar, n4, GP}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Q not conserved in vertex {ebar, n5, GP}.
Quantum number LeptonNumber not conserved in vertex {ebar, n5, GP}.
Quantum number Q not conserved in vertex {ebar, vebar, GP}.
Quantum number LeptonNumber not conserved in vertex {ebar, vebar, GP}.
Quantum number Q not conserved in vertex {ebar, vmbar, GP}.
Quantum number LeptonNumber not conserved in vertex {ebar, vmbar, GP}.
Quantum number Q not conserved in vertex {ebar, vtbar, GP}.
Quantum number LeptonNumber not conserved in vertex {ebar, vtbar, GP}.
Quantum number LeptonNumber not conserved in vertex {vebar, n4, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, n4, H}.
Quantum number LeptonNumber not conserved in vertex {vebar, n5, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, n5, H}.
Quantum number LeptonNumber not conserved in vertex {vebar, vebar, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, vebar, H}.
Quantum number LeptonNumber not conserved in vertex {vebar, vmbar, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, vmbar, H}.
Quantum number LeptonNumber not conserved in vertex {vebar, vtbar, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, vtbar, H}.
Quantum number Q not conserved in vertex {ve, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {ve, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {ve, ve, G0}.
Quantum number LeptonNumber not conserved in vertex {ve, ve, H}.
Quantum number Q not conserved in vertex {vm, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vm, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vm, ve, G0}.
Quantum number LeptonNumber not conserved in vertex {vm, ve, H}.
Quantum number Q not conserved in vertex {vt, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vt, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vt, ve, G0}.
Quantum number LeptonNumber not conserved in vertex {vt, ve, H}.
Quantum number Q not conserved in vertex {n4, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {n4, e, GPbar}.
Quantum number LeptonNumber not conserved in vertex {n4, ve, G0}.
Quantum number LeptonNumber not conserved in vertex {n4, ve, H}.
Quantum number Q not conserved
[... block truncated ...]
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$3085]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3085, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29010], Index[Spin, j$29010]]*Un[Index[Neutrino, 4], Index[Neutrino, 2]] + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$3092]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3092, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29012], Index[Spin, j$29012]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$3086]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3086, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29010], Index[Spin, j$29010]]*Un[Index[Neutrino, 4], Index[Neutrino, 2]] + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$3093]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3093, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29012], Index[Spin, j$29012]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$3086]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3086, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29010], Index[Spin, j$29010]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]] + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$3093]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3093, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29012], Index[Spin, j$29012]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$3088]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3088, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29010], Index[Spin, j$29010]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]] + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$3095]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3095, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29012], Index[Spin, j$29012]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$3085]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3085, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29010], Index[Spin, j$29010]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]] + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$3092]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$3092, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$29012], Index[Spin, j$29012]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 4], Index[
[... block truncated ...]
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$3092]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3092, sp1]) - Mmaj*Conjugate[Ga[0, r$3085, sp1]]*n4bar[Index[Spin, r$3085]] . n5[Index[Spin, sp1]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$3093]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3093, sp1]) - Mmaj*Conjugate[Ga[0, r$3086, sp1]]*n5bar[Index[Spin, r$3086]] . n4[Index[Spin, sp1]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$3095]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3095, sp1]) + (vev*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*vmbar[Index[Spin, sp2$29474]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3441, sp1]*ProjP[Index[Spin, sp2$29474], Index[Spin, r$3441]]*yvn[Index[Generation, 2]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$3095]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3095, sp1]) + (vev*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*vmbar[Index[Spin, sp2$29476]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3441, sp1]*ProjP[Index[Spin, sp2$29476], Index[Spin, r$3441]]*yvn[Index[Generation, 2]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Ga[0, r$3085, sp1]]*n4bar[Index[Spin, r$3085]] . vm[Index[Spin, sp1]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]) + (vev*Conjugate[Ga[0, r$3085, sp1]]*n4bar[Index[Spin, r$3085]] . vm[Index[Spin, sp2$29458]]*ProjM[Index[Spin, sp1], Index[Spin, sp2$29458]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*yvn[Index[Generation, 2]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Ga[0, r$3086, sp1]]*n5bar[Index[Spin, r$3086]] . vm[Index[Spin, sp1]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]) + (vev*Conjugate[Ga[0, r$3086, sp1]]*n5bar[Index[Spin, r$3086]] . vm[Index[Spin, sp2$29460]]*ProjM[Index[Spin, sp1], Index[Spin, sp2$29460]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*yvn[Index[Generation, 2]])/Sqrt[2]
```

## FeynRules / Wolfram Engine output (tail)
```
 longer than depth of object.
From kernel 3 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.
From kernel 4 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.
From kernel 5 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.

General::stop: Further output of Part::partd will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 2 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 3 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 4 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 5 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 1 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/207 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench2/pSPSS/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/pSPSS/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
adgraph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench2/pSPSS/round0/UFO
You can also type "set auto_convert_model T" to automatically convert all python2 module to be python3 compatible in the future.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1570, in onecmd
    return self.onecmd_orig(line, **opt)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5893, in do_import
    self.import_command_file(args[1])
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1718, in import_command_file
    self.exec_cmd(line, precmd=True)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1599, in exec_cmd
    stop = Cmd.onecmd_orig(current_interface, line, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5835, in do_import
    raise err
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5819, in do_import
    self._curr_model = import_ufo.import_model(args[1], prefix=prefix,
                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        complex_mass_scheme=self.options['complex_mass_scheme'],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        options=options)
        ^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Fail to write options with error No model currently active, please import a model!
```

## UFO Python syntax error — `UFO/vertices.py` line 838: closing parenthesis ')' does not match opening parenthesis '[' on line 835
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  836 |                color = [ '1' ],
  837 |                lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1 ],
  838 |                couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_193})
  839 | 
  840 | V_139 = Vertex(name = 'V_139',
```
