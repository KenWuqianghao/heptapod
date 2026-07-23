# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: selfconjugate_quantum_numbers, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

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
From kernel 1 (Local):
Get::noopen: Cannot open Heidi`.
From kernel 2 (Local):
Get::noopen: Cannot open Heidi`.
From kernel 3 (Local):
Get::noopen: Cannot open Heidi`.
From kernel 5 (Local):
Get::noopen: Cannot open Heidi`.
From kernel 6 (Local):
Get::noopen: Cannot open Heidi`.

General::stop: Further output of Get::noopen will be suppressed during this calculation.
From kernel 3 (Local):
Needs::nocont: Context Heidi` was not created when Needs was evaluated.
From kernel 6 (Local):
Needs::nocont: Context Heidi` was not created when Needs was evaluated.
From kernel 1 (Local):
Needs::nocont: Context Heidi` was not created when Needs was evaluated.
From kernel 2 (Local):
Needs::nocont: Context Heidi` was not created when Needs was evaluated.
From kernel 4 (Local):
Needs::nocont: Context Heidi` was not created when Needs was evaluated.

General::stop: Further output of Context `1` was not created when Needs was evaluated. will be suppressed during this calculation.
From kernel 2 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 5 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 6 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 1 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 3 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of Warning: Selfconjugated fields should not carry quantumnumbers. will be suppressed during this calculation.
Merging model-files...

Get::noopen: Cannot open Heidi`.

Needs::nocont: Context Heidi` was not created when Needs was evaluated.
This model implementation was created by
C. Speckner
Model Version: 0.1
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
   - Loading gauge group classes.
   - Loading parameter classes.

Model CHEIDI_gen loaded.

Range::range: Range specification in Range[Heidi$nmodes] does not have appropriate bounds.

                                             2                                                                  2
                                           gs  HhHeidi$nmodes Sqrt[kggh] (del[G[mu, a], nu] - del[G[nu, a], mu])  xi[Heidi$nmodes]
Range::range: Range specification in Range[---------------------------------------------------------------------------------------] does not have appropriate bounds.
                                                                                       2
                                                                                  48 Pi  v
[INFO] Total Lagrangian: LSM + LHEIDIggHeavyTop

                                             2                                                                  2
                                           gs  HhHeidi$nmodes Sqrt[kggh] (del[G[mu, a], nu] - del[G[nu, a], mu])  xi[Heidi$nmodes]
Range::range: Range specification in Range[---------------------------------------------------------------------------------------] does not have appropriate bounds.
                                                                                       2
                                                                                  48 Pi  v

General::stop: Further output of Range::range will be suppressed during this calculation.
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
[INFO] UFO output: /tmp/repair_bench/CHEIDI/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
36 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 36.
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
5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench/CHEIDI/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/CHEIDI/round0/UFO" with error:
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
convert model /tmp/repair_bench/CHEIDI/round0/UFO
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
