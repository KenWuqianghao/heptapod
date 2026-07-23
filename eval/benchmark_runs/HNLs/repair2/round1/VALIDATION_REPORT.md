# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
192 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 192.
192 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{v1bar, 1}, {e, 2}, {Pip, 3}}, fpi*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 1], Index[Generation, 1]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {e, 2}, {Kp, 3}}, fK*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 2]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 1], Index[Generation, 1]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {e, 2}, {Dd, 3}}, fD*Gf*Conjugate[CKM[Index[Generation, 2], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 1], Index[Generation, 1]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {e, 2}, {Ds, 3}}, fDs*Gf*Conjugate[CKM[Index[Generation, 2], Index[Generation, 2]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 1], Index[Generation, 1]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {mu, 2}, {Pip, 3}}, fpi*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 2], Index[Generation, 2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {mu, 2}, {Kp, 3}}, fK*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 2]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 2], Index[Generation, 2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {mu, 2}, {Dd, 3}}, fD*Gf*Conjugate[CKM[Index[Generation, 2], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 2], Index[Generation, 2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{v1bar, 1}, {mu, 2}, {Ds, 3}}, fDs*Gf*Conjugate[CKM[Index[Generation, 2], Index[Generation, 2]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 1]]]*(Sqrt[2]*numass[Index[Neutrinos, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]] - vev*Conjugate[yl[Index[Generation, 
[... block truncated ...]
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31835]] . v1[Index[Spin, sp2$31836]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, sp2$31835], Index[Spin, sp2$31836]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 1], Index[Heavynus, 1]]]*N4bar[Index[Spin, sp2$31837]] . v1[Index[Spin, sp2$31906]]*ProjM[Index[Spin, sp2$31837], Index[Spin, sp2$31906]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31833]] . v1[Index[Spin, sp2$31834]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]*ProjP[Index[Spin, sp2$31833], Index[Spin, sp2$31834]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31835]] . v2[Index[Spin, sp2$31836]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]*ProjM[Index[Spin, sp2$31835], Index[Spin, sp2$31836]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 2], Index[Heavynus, 1]]]*N4bar[Index[Spin, sp2$31838]] . v2[Index[Spin, sp2$31922]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31922]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31833]] . v2[Index[Spin, sp2$31834]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]*ProjP[Index[Spin, sp2$31833], Index[Spin, sp2$31834]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31835]] . v3[Index[Spin, sp2$31836]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]*ProjM[Index[Spin, sp2$31835], Index[Spin, sp2$31836]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 3], Index[Heavynus, 1]]]*N4bar[Index[Spin, sp2$31839]] . v3[Index[Spin, sp2$31938]]*ProjM[Index[Spin, sp2$31839], Index[Spin, sp2$31938]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31833]] . v3[Index[Spin, sp2$31834]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]*ProjP[Index[Spin, sp2$31833], Index[Spin, sp2$31834]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]]*v1bar[Index[Spin, sp2$31835]] . N4[Index[Spin, sp2$31836]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, sp2$31835], Index[Spin, sp2$31836]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]]*v1bar[Index[Spin, sp2$31833]] . N4[Index[Spin, sp2$31834]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31833], Index[Spin, sp2$31834]] - (vev*v1bar[Index[Spin, sp2$31858]] . N4[Index[Spin, sp2$31840]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31858], Index[Spin, sp2$31840]]*yN[Index[Generation, 1], Index[Heavynus, 1]])/Sqrt[2]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]]*v2bar[Index[Spin, sp2$31835]] . N4[Index[Spin, sp2$31836]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, sp2$31835], Index[Spin, sp2$31836]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]]*v2bar[Index[Spin, sp2$31833]] . N4[Index[Spin, sp2$31834]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31833], Index[Spin, sp2$31834]] - (vev*v2bar[Index[Spin, sp2$31874]] . N4[Index[Spin, sp2$31841]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, 
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
l::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 8 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad Index[Neutrinos, Ext[1]], 0].
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad NoUnfold[{1, 2, 3, 4}], 0].
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad Index[Neutrinos, Ext[2]], 0].
From kernel 8 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 2 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad Index[Neutrinos, Ext[1]], 0].
From kernel 2 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad NoUnfold[{1, 2, 3, 4}], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + NoUnfold[{1, 2, 3, 4}], 0].

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[2]], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 2 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 4 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 1 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 2 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + NoUnfold[{1, 2, 3, 4}], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 8 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/306 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.
    - Writing files.

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.

Part::partw: Part 3 of {{NP, 1}, {NP, 0}} does not exist.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench2/HNLs/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/HNLs/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
madgraph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench2/HNLs/round0/UFO
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

## UFO Python syntax error — `UFO/lorentz.py` line 15: cannot assign to literal here. Maybe you meant '==' instead of '='?
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   13 | 
   14 | 
   15 | 1 = Lorentz(name = '1',
   16 |             spins = [],
   17 |             structure = '0')
```

## UFO Python syntax error — `UFO/vertices.py` line 1786: closing parenthesis ')' does not match opening parenthesis '[' on line 1783
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
 1784 |                color = [ '1' ],
 1785 |                lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1 ],
 1786 |                couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_421})
 1787 | 
 1788 | V_297 = Vertex(name = 'V_297',
```
