# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: mg5_import_fail, mg5_python_traceback

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
Merging model-files...
This model implementation was created by
Arindam Das
P. S. Bhupal Dev
Yutaka Hosotani
Sanjoy Mandal
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.

Model GeneralU1_gen loaded.
[INFO] Total Lagrangian: LSM + LTot
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
[INFO] UFO output: /tmp/repair_bench/GeneralU1/round1/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
148 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 148.
143 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 143
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Q not conserved in vertex {GP, N1bar, ve}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, ve}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Q not conserved in vertex {GP, N1bar, vm}.
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, vm}.
Quantum number Q not conserved in vertex {GP, N1bar, vt}.
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, vt}.
Quantum number Q not conserved in vertex {GP, N2bar, ve}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, ve}.
Quantum number Q not conserved in vertex {GP, N2bar, vm}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, vm}.
Quantum number Q not conserved in vertex {GP, N2bar, vt}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, vt}.
Quantum number Q not conserved in vertex {GP, N3bar, ve}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, ve}.
Quantum number Q not conserved in vertex {GP, N3bar, vm}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, vm}.
Quantum number Q not conserved in vertex {GP, N3bar, vt}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, vt}.
Quantum number Q not conserved in vertex {G0, N1bar, e}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, e}.
Quantum number Q not conserved in vertex {G0, N1bar, mu}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, mu}.
Quantum number Q not conserved in vertex {G0, N1bar, ta}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, ta}.
Quantum number Q not conserved in vertex {G0, N2bar, e}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, e}.
Quantum number Q not conserved in vertex {G0, N2bar, mu}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, mu}.
Quantum number Q not conserved in vertex {G0, N2bar, ta}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, ta}.
Quantum number Q not conserved in vertex {G0, N3bar, e}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, e}.
Quantum number Q not conserved in vertex {G0, N3bar, mu}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, mu}.
Quantum number Q not conserved in vertex {G0, N3bar, ta}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, ta}.
Quantum number Q not conserved in vertex {H, N1bar, e}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, e}.
Quantum number Q not conserved in vertex {H, N1bar, mu}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, mu}.
Quantum number Q not conserved in vertex {H, N1bar, ta}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, ta}.
Quantum number Q not conserved in vertex {H, N2bar, e}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, e}.
Quantum number Q not conserved in vertex {H, N2bar, mu}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, mu}.
Quantum number Q not conserved in vertex {H, N2bar, ta}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, ta}.
Quantum number Q not conserved in vertex {H, N3bar, e}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, e}.
Quantum number Q not conserved in vertex {H, N3bar, mu}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, mu}.
Quantum number Q not conserved in vertex {H, N3bar, ta}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, ta}.
Quantum number Q not conserved in vertex {GPbar, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vebar, N1}.
Quantum number Q not conserved in vertex {GPbar, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vebar, N2}.
Quantum number Q not conserved in vertex {GPbar, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vebar, N3}.
Quantum number Q not conserved in vertex {GPbar, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vmbar, N1}.
Quantum number Q not conserved in vertex {GPbar, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vmbar, N2}.
Quantum number Q not conserved in vertex {GPbar, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vmbar, N3}.
Quantum number Q not conserved in vertex {GPbar, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vtbar, N1}.
Quantum number Q not conserved in vertex {GPbar, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vtbar, N2}.
Quantum number Q not conserved in vertex {GPbar, vtbar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vtbar, N3}.
Quantum number Q not conserved in vertex {G0, ebar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, ebar, N1}.
Quantum number Q not conserved in vertex {G0, ebar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, ebar, N2}.
Quantum number Q not conserved in vertex {G0, ebar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, ebar, N3}.
Quantum number Q not conserved in vertex {G0, mubar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, mubar, N1}.
Quantum number Q not conserved in vertex {G0, mubar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, mubar, N2}.
Quantum number Q not conserved in vertex {G0, mubar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, mubar, N3}.
Quantum number Q not conserved in vertex {G0, tabar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, tabar, N1}.
Quantum number Q not conserved in vertex {G0, tabar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, tabar, N2}.
Quantum number Q not conserved in vertex {G0, tabar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, tabar, N3}.
Quantum number Q not conserved in vertex {H, ebar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, ebar, N1}.
Quantum number Q not conserved in vertex {H, ebar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, ebar, N2}.
Quantum number Q not conserved in vertex {H, ebar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, ebar, N3}.
Quantum number Q not conserved in vertex {H, mubar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, mubar, N1}.
Quantum number Q not conserved in vertex {H, mubar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, mubar, N2}.
Quantum number Q not conserved in vertex {H, mubar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, mubar, N3}.
Quantum number Q not conserved in vertex {H, tabar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, tabar, N1}.
Quantum number Q not conserved in vertex {H, tabar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, tabar, N2}.
Quantum number Q not conserved in vertex {H, tabar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, tabar, N3}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/281 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench/GeneralU1/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/GeneralU1/round1/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
5_aMC/models/import_ufo.py", line 611, in load_model
    self.add_interaction(interaction_info, color_info)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 1840, in add_interaction
    raise InvalidModel('''Some couplings have \'1\' order.
    This is not allowed in MG.
    Please defines an additional coupling to your model''')
models.import_ufo.InvalidModel: Some couplings have '1' order. 
                    This is not allowed in MG. 
                    Please defines an additional coupling to your model

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
