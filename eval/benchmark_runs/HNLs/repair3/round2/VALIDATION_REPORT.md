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
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]]*v1bar[Index[Spin, r$3030]] . N4[Index[Spin, sp2$25747]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, r$3030], Index[Spin, sp2$25747]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]]*v1bar[Index[Spin, r$3037]] . N4[Index[Spin, sp2$25745]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, r$3037], Index[Spin, sp2$25745]] - (vev*v1bar[Index[Spin, sp2$25769]] . N4[Index[Spin, sp2$25751]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$25769], Index[Spin, sp2$25751]]*yN[Index[Generation, 1], Index[Heavynus, 1]])/Sqrt[2]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]]*v2bar[Index[Spin, r$3031]] . N4[Index[Spin, sp2$25747]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, r$3031], Index[Spin, sp2$25747]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]]*v2bar[Index[Spin, r$3038]] . N4[Index[Spin, sp2$25745]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, r$3038], Index[Spin, sp2$25745]] - (vev*v2bar[Index[Spin, sp2$25785]] . N4[Index[Spin, sp2$25752]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$25785], Index[Spin, sp2$25752]]*yN[Index[Generation, 2], Index[Heavynus, 1]])/Sqrt[2]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]]*v3bar[Index[Spin, r$3032]] . N4[Index[Spin, sp2$25747]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, r$3032], Index[Spin, sp2$25747]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]]*v3bar[Index[Spin, r$3039]] . N4[Index[Spin, sp2$25745]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, r$3039], Index[Spin, sp2$25745]] - (vev*v3bar[Index[Spin, sp2$25801]] . N4[Index[Spin, sp2$25753]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$25801], Index[Spin, sp2$25753]]*yN[Index[Generation, 3], Index[Heavynus, 1]])/Sqrt[2]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, r$3033]] . v1[Index[Spin, sp2$25747]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, r$3033], Index[Spin, sp2$25747]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 1], Index[Heavynus, 1]]]*N4bar[Index[Spin, r$3033]] . v1[Index[Spin, sp2$25817]]*ProjM[Index[Spin, r$3033], Index[Spin, sp2$25817]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, r$3040]] . v1[Index[Spin, sp2$25745]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]*ProjP[Index[Spin, r$3040], Index[Spin, sp2$25745]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, r$3033]] . v2[Index[Spin, sp2$25747]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]*ProjM[Index[Spin, r$3033], Index[Spin, sp2$25747]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 2], Index[Heavynus, 1]]]*N4bar[Index[Spin, r$3033]] . v2[Index[Spin, sp2$25833]]*ProjM[Index[Spin, r$3033], Index[Spin, sp2$25833]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, r$3040]] . v2[Index[Spin, sp2$25745]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]*ProjP[Index[Spin, r$3040], Index[Spin, sp2$25745]]
Non 
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
le[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
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

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + NoUnfold[{1, 2, 3, 4}], 0].

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[2]], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 2 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 3 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 4 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 8 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/408 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.
    - Writing files.

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[LLbar]].

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
[1;31mCommand "import /private/tmp/repair_bench3/HNLs/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench3/HNLs/round1/UFO" with error:
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
convert model /tmp/repair_bench3/HNLs/round1/UFO
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

## UFO Python syntax error — `UFO/vertices.py` line 2386: closing parenthesis ')' does not match opening parenthesis '[' on line 2383
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
 2384 |                color = [ '1' ],
 2385 |                lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1 ],
 2386 |                couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_617})
 2387 | 
 2388 | V_397 = Vertex(name = 'V_397',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_bench3/HNLs/round1/UFO/__init__.py", line 2, in <module>
    import particles
  File "/tmp/repair_bench3/HNLs/round1/UFO/particles.py", line 8, in <module>
    import parameters as Param
  File "/tmp/repair_bench3/HNLs/round1/UFO/parameters.py", line 295, in <module>
    value = MassN4,
            ^^^^^^
NameError: name 'MassN4' is not defined

```
