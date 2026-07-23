# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
36 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 36.

Part::pkspec1: The expression Index[Spin, Ext[1]] cannot be used as a part specification.

Part::pkspec1: The expression Index[Spin, a] cannot be used as a part specification.

Part::pkspec1: The expression Index[Spin, Ext[1]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {n4, e, GP}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {n4, ve, G0}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number LeptonNumber not conserved in vertex {n4, ve, H}.
Quantum number LeptonNumber not conserved in vertex {n5, e, GP}.
Quantum number LeptonNumber not conserved in vertex {n5, ve, G0}.
Quantum number LeptonNumber not conserved in vertex {n5, ve, H}.
Quantum number LeptonNumber not conserved in vertex {ebar, n4, GPbar}.
Quantum number LeptonNumber not conserved in vertex {ebar, n5, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vebar, n4, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, n4, H}.
Quantum number LeptonNumber not conserved in vertex {vebar, n5, G0}.
Quantum number LeptonNumber not conserved in vertex {vebar, n5, H}.
Quantum number LeptonNumber not conserved in vertex {n4, mu, GP}.
Quantum number LeptonNumber not conserved in vertex {n4, vm, G0}.
Quantum number LeptonNumber not conserved in vertex {n4, vm, H}.
Quantum number LeptonNumber not conserved in vertex {n5, mu, GP}.
Quantum number LeptonNumber not conserved in vertex {n5, vm, G0}.
Quantum number LeptonNumber not conserved in vertex {n5, vm, H}.
Quantum number LeptonNumber not conserved in vertex {mubar, n4, GPbar}.
Quantum number LeptonNumber not conserved in vertex {mubar, n5, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vmbar, n4, G0}.
Quantum number LeptonNumber not conserved in vertex {vmbar, n4, H}.
Quantum number LeptonNumber not conserved in vertex {vmbar, n5, G0}.
Quantum number LeptonNumber not conserved in vertex {vmbar, n5, H}.
Quantum number LeptonNumber not conserved in vertex {n4, ta, GP}.
Quantum number LeptonNumber not conserved in vertex {n4, vt, G0}.
Quantum number LeptonNumber not conserved in vertex {n4, vt, H}.
Quantum number LeptonNumber not conserved in vertex {n5, ta, GP}.
Quantum number LeptonNumber not conserved in vertex {n5, vt, G0}.
Quantum number LeptonNumber not conserved in vertex {n5, vt, H}.
Quantum number LeptonNumber not conserved in vertex {tabar, n4, GPbar}.
Quantum number LeptonNumber not conserved in vertex {tabar, n5, GPbar}.
Quantum number LeptonNumber not conserved in vertex {vtbar, n4, G0}.
Quantum number LeptonNumber not conserved in vertex {vtbar, n4, H}.
Quantum number LeptonNumber not conserved in vertex {vtbar, n5, G0}.
Quantum number LeptonNumber not cons
[... block truncated ...]
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: (n4bar[Index[Spin, r$2977]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2977, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13865], Index[Spin, j$13865]])/2 + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2981]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2981, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13867], Index[Spin, j$13867]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: -1/2*(n5bar[Index[Spin, r$2978]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2978, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13865], Index[Spin, j$13865]]) + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2982]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2982, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13867], Index[Spin, j$13867]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2981]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2981, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13867], Index[Spin, j$13867]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2982]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2982, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13867], Index[Spin, j$13867]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2984]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2984, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13867], Index[Spin, j$13867]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2984]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2984, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$13867], Index[Spin, j$13867]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2981]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2981, sp1])/Sqrt[2]) - (I*Mmaj*Conjugate[Ga[0, r$2977, sp1]]*n4bar[Index[Spin, r$2977]] . n5[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (I*Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2982]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2982, sp1])/Sqrt[2] - (Mmaj*Conjugate[Ga[0, r$2978, sp1]]*n5bar[Index[Spin, r$2978]] . n4[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (I*Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2984]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2984, sp1])/Sqrt[2] - I/2*vev*vmbar[Index[Spin, sp2$13951]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3315, sp1]*ProjP[Index[Spin, sp2$13951], Index[Spin, r$3315]]*yvn[Index[Generation, 2]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2984]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2984, sp1])/Sqrt[2]) + (vev*vmbar[Index[Spin, sp2$13953]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$3315, sp1]*ProjP[Index[Spin, sp2$13953], Index[Spin, r$3315]]*yvn[Index[Generation, 2]])/2
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (-I*Mmaj*Conjugate[Ga[0, r$2977, sp1]]*n4bar[Index[Spin, r$2977]] . vm[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]])/Sqrt[2] + I/2*vev*Conjugate[Ga[0, r$2977, sp1]]*n4bar[Index[Spin, r$2977]] . vm[Index[Spin, sp2$13955]]*ProjM[Index[Spin, sp1], Index[Spin, sp2$13955]]*yvn[Index[Generation, 2]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((Mmaj*Conjugate[Ga[0, r$2978, sp1]]*n5bar[Index[Spin, r$2978]] . vm[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]])/Sqrt[2]) + (vev*Conjugate[Ga[0, r$2978, sp1]]*n5bar[Index[Spin, r$2978]] . vm[Index[Spin, sp2$13957]]*ProjM[Index[Spin, sp1], Index[Spin, sp2$13957]]*yvn[Index[Generation, 2]])/2
```

## FeynRules / Wolfram Engine output (tail)
```
                                                                                                                      1
Take::take: Cannot take positions 2 through 2 in {{1, Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2977, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{n4bar, 1}, {LL, 2}, {Phi, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] PRIVATE`PYSVPower[2, -(-)] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{n4bar, 1}, {LL, 2}, {Phi, 3}}[[PRIVATE`hold[Ext[1], a]]], {{n4bar, 1}, {LL, 2}, {Phi, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
                                                                                                                                                                                                                                                                                                                                                                                     2
From kernel 5 (Local):
                                                                                                                                                                                                                                                                                                                                                                                     1
Take::take: Cannot take positions 2 through 2 in {{1, Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2977, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{n4bar, 1}, {LL, 2}, {Phi, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] PRIVATE`PYSVPower[2, -(-)] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{n4bar, 1}, {LL, 2}, {Phi, 3}}[[PRIVATE`hold[Ext[1], a]]], {{n4bar, 1}, {LL, 2}, {Phi, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
                                                                                                                                                                                                                                                                                                                                                                                     2

General::stop: Further output of Take::take will be suppressed during this calculation.
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

General::stop: Further output of Select::normal will be suppressed during this calculation.

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/166 .

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
[1;31mCommand "import /private/tmp/repair_bench2/pSPSS/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/pSPSS/round1/UFO" with error:
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
convert model /tmp/repair_bench2/pSPSS/round1/UFO
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

## UFO Python syntax error — `UFO/vertices.py` line 598: closing parenthesis ')' does not match opening parenthesis '[' on line 595
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  596 |               color = [ 'Select(1,Function(MatchColor(Slot(1))))' ],
  597 |               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1 ],
  598 |               couplings = {(0,0):C.GC_131})
  599 | 
  600 | V_99 = Vertex(name = 'V_99',
```
