# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: selfconjugate_quantum_numbers, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
No vertices found.
0 vertices obtained.
The lagrangian is hermitian.
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
```

## FeynRules / Wolfram Engine output (tail)
```
f replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
Rule::argrx: Rule called with 12 arguments; 2 arguments are expected.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 2 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 3 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 4 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 5 (Local):
Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 1 (Local):
Table::iterb: Iterator {Index[{}[[1]], Ext[3]], IndexRange[Index[{}[[1]]]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[{}[[1]], Ext[3]], IndexRange[Index[{}[[1]]]]} does not have appropriate bounds.
From kernel 3 (Local):
Table::iterb: Iterator {Index[{}[[1]], Ext[3]], IndexRange[Index[{}[[1]]]]} does not have appropriate bounds.
From kernel 4 (Local):
Table::iterb: Iterator {Index[{}[[1]], Ext[3]], IndexRange[Index[{}[[1]]]]} does not have appropriate bounds.
From kernel 5 (Local):
Table::iterb: Iterator {Index[{}[[1]], Ext[3]], IndexRange[Index[{}[[1]]]]} does not have appropriate bounds.

General::stop: Further output of Table::iterb will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 2 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 3 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 4 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 5 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 1 (Local):
Join::heads: Heads IndexRange and List at positions 1 and 2 are expected to be the same.
From kernel 2 (Local):
Join::heads: Heads IndexRange and List at positions 1 and 2 are expected to be the same.
From kernel 3 (Local):
Join::heads: Heads IndexRange and List at positions 1 and 2 are expected to be the same.
From kernel 4 (Local):
Join::heads: Heads IndexRange and List at positions 1 and 2 are expected to be the same.
From kernel 5 (Local):
Join::heads: Heads IndexRange and List at positions 1 and 2 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/97 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.

Table::itraw: Raw object 3 cannot be used as an iterator.

Table::itraw: Raw object 3 cannot be used as an iterator.

Table::itraw: Raw object 3 cannot be used as an iterator.

General::stop: Further output of Table::itraw will be suppressed during this calculation.
Done!
[INFO] Done.

```

## MadGraph import output (tail)
```
mport_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench3/ALRM_general/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench3/ALRM_general/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench3/ALRM_general/round0/UFO
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

## UFO Python syntax error — `UFO/couplings.py` line 206: unterminated string literal (detected at line 206)
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  204 | GC_49 = Coupling(name = 'GC_49',
  205 |                  value = 'ExtractFermionsFromParticleList(Table(List(List(List(G,1),List(G,2),List(G,3),List(G,4),List(h0(5),5)),(0 + 1*complex(0,1))*G**2*Ghgg*PRIVATExSortStrucConst(f(1,3,Index(Gluon,xx$16717,1)))*PRIVATExSortStrucConst(f(2,4,Index(Gluon,xx$16717,1)))*Metric(1,4)*Metric(2,3)*Classe
  206 |                  order = {'                                                                                                                                 2                                                                                                                                               
  207 | PRIVATE`GetIntOrder[ExtractFermionsFromParticleList[Table[{{{G, 1}, {G, 2}, {G, 3}, {G, 4}, {h0[Index[{}[[1]], Ext[5]]], 5}}, I G  Ghgg PRIVATE`SortStrucConst[C$f[Index[Gluon, Ext[1]], Index[Gluon, Ext[3]], Index[Gluon, xx$16717, 1]]] PRIVATE`SortStrucConst[C$f[Index[Gluon, Ext[2]], Index[Gluon, Ext
  208 | 
```

## UFO Python syntax error — `UFO/vertices.py` line 82: closing parenthesis ')' does not match opening parenthesis '[' on line 79
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   80 |               color = [ '1' ],
   81 |               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1 ],
   82 |               couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_46})
   83 | 
   84 | V_13 = Vertex(name = 'V_13',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
                                                                                                                                                                                                                                                                                       2                                                                                                                                                                                                                                                                                                                                                                                           2                                                                                                                                                                                                                                                                                                                                                                                           2                                                                                                                                                                                                                                                                                                                                                                                           2
             ^
SyntaxError: unterminated string literal (detected at line 206)

```
