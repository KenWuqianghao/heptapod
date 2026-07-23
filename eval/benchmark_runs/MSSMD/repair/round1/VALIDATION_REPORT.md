# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: duplicate_particle_names, selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback

## FeynRules / Wolfram Engine output (tail)
```
[INFO] Loading via explicit file: /Users/kenwu/feynrules-current/FeynRules.m
 - FeynRules - 
Version: 2.3.49 (*29 September 2021).
Authors: A. Alloul, N. Christensen, C. Degrande, C. Duhr, B. Fuks
 
Please cite:
    - Comput.Phys.Commun.185:2250-2300,2014 (arXiv:1310.1921);
    - Comput.Phys.Commun.180:1614-1641,2009 (arXiv:0806.4194).
 
http://feynrules.phys.ucl.ac.be
 
The FeynRules palette can be opened using the command FRPalette[].
[INFO] Loading SM from: /Users/kenwu/feynrules-current/Models/SM/SM.fr
From kernel 2 (Local):
Part::partw: Part 2 of {MAD} does not exist.
From kernel 5 (Local):
Part::partw: Part 2 of {MAD} does not exist.
From kernel 6 (Local):
Part::partw: Part 2 of {MAD} does not exist.
From kernel 1 (Local):
Part::partw: Part 2 of {MAD} does not exist.
From kernel 2 (Local):
Part::partw: Part 2 of {WAD} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 2 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 5 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 6 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 8 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 1 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 2 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.

General::stop: Further output of Warning: Selfconjugated fields should not carry quantumnumbers. will be suppressed during this calculation.
From kernel 2 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 5 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 6 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 1 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 2 (Local):
LoadModel::Part: Warning : All particles should have different names.

General::stop: Further output of Warning : All particles should have different names. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Wei Shi
CMS Collaboration
Model Version: 1
For more information, type ModelInformation[].

   - Loading particle classes.

Part::partw: Part 2 of {MAD} does not exist.

Part::partw: Part 2 of {WAD} does not exist.

Part::partw: Part 2 of {WAD} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of LoadModel::QN will be suppressed during this calculation.

LoadModel::Part: Warning : All particles should have different names.

LoadModel::Part: Warning : All particles should have different names.
   - Loading gauge group classes.
   - Loading parameter classes.

Model MSSMD_gen loaded.
[INFO] Total Lagrangian: LSM + Lag
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
No vertices found.
0 vertices obtained.
The lagrangian is hermitian.
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
[INFO] UFO output: /tmp/repair_bench/MSSMD/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
99 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 99.
94 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 94
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Q not conserved in vertex {G0, G0, H, H}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Q not conserved in vertex {GP, GPbar, H, H}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Q not conserved in vertex {H, H, H, H}.
Quantum number Q not conserved in vertex {G0, G0, H}.
Quantum number Q not conserved in vertex {GP, GPbar, H}.
Quantum number Q not conserved in vertex {H, H, H}.
Quantum number Q not conserved in vertex {ghWmbar, ghWm, H}.
Quantum number Q not conserved in vertex {ghWpbar, ghWp, H}.
Quantum number Q not conserved in vertex {ghZbar, ghZ, H}.
Quantum number Q not conserved in vertex {H, dbar, d}.
Quantum number Q not conserved in vertex {H, sbar, s}.
Quantum number Q not conserved in vertex {H, bbar, b}.
Quantum number Q not conserved in vertex {H, ebar, e}.
Quantum number Q not conserved in vertex {H, mubar, mu}.
Quantum number Q not conserved in vertex {H, tabar, ta}.
Quantum number Q not conserved in vertex {H, ubar, u}.
Quantum number Q not conserved in vertex {H, cbar, c}.
Quantum number Q not conserved in vertex {H, tbar, t}.
Quantum number Q not conserved in vertex {A, GPbar, H, W}.
Quantum number Q not conserved in vertex {GPbar, H, W}.
Quantum number Q not conserved in vertex {A, GP, H, Wbar}.
Quantum number Q not conserved in vertex {GP, H, Wbar}.
Quantum number Q not conserved in vertex {H, H, W, Wbar}.
Quantum number Q not conserved in vertex {H, W, Wbar}.
Quantum number Q not conserved in vertex {G0, H, Z}.
Quantum number Q not conserved in vertex {GPbar, H, W, Z}.
Quantum number Q not conserved in vertex {GP, H, Wbar, Z}.
Quantum number Q not conserved in vertex {H, H, Z, Z}.
Quantum number Q not conserved in vertex {H, Z, Z}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/164 .
    - Writing files.
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
[1;31mCommand "import /private/tmp/repair_bench/MSSMD/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/MSSMD/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
"/Users/kenwu/MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 415, in import_full_model
    model = ufo2mg5_converter.load_model()
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 547, in load_model
    raise InvalidModel("name %s define multiple time. Please correct the UFO model!" \
                                                      % (param.name))
models.import_ufo.InvalidModel: name WH define multiple time. Please correct the UFO model!

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
