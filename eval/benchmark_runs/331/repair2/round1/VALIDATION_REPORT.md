# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
10 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 10.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
5 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{A, 1}, {Vp, 2}, {Vpbar, 3}}, -1/2*(am*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]])}
{{{A, 1}, {W, 2}, {Wbar, 3}}, ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]}
{{{A, 1}, {Yp, 2}, {Ypbar, 3}}, -1/2*(ap*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]])}
{{{Vp, 1}, {Vpbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]])/(2*cw*sw)}
{{{Yp, 1}, {Ypbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]])/(2*cw*sw)}
HEPTAPOD-CHECK-ERROR
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
 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 4 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 1 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

General::stop: Further output of In FeynRules mode, all class members should be given a mass name. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Codex extraction from Cao and Zhang, arXiv:1611.09337
Model Version: 1.0.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model 331_gen loaded.
[INFO] Total Lagrangian: LSM + LTot
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
10 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 10.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
5 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{A, 1}, {Vp, 2}, {Vpbar, 3}}, -1/2*(am*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]])}
{{{A, 1}, {W, 2}, {Wbar, 3}}, ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]}
{{{A, 1}, {Yp, 2}, {Ypbar, 3}}, -1/2*(ap*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]])}
{{{Vp, 1}, {Vpbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]])/(2*cw*sw)}
{{{Yp, 1}, {Ypbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*HC[VVV[mu, nu, sig]]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]])/(2*cw*sw)}
HEPTAPOD-CHECK-ERROR
HEPTAPOD-CHECK-END: hermiticity
HEPTAPOD-CHECK-BEGIN: kinetic_terms
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
HEPTAPOD-CHECK-END: kinetic_terms
HEPTAPOD-CHECK-BEGIN: mass_spectrum
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench2/331/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
41 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 41.
31 vertices obtained.
Flavor expansion of the vertices: Dynamic[FR$Count1] / 31
   - Saved vertices in InterfaceRun[ 1 ].
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/75 .
    - Writing files.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
u/MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench2/331/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/331/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
/madgraph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench2/331/round0/UFO
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
