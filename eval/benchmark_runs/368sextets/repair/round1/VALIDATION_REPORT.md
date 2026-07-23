# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
les-current/Models/SM/SM.fr
Merging model-files...
This model implementation was created by
Linda M. Carpenter
Taylor Murphy
Tim M. P. Tait
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.

Model 368sextets_gen loaded.
[INFO] Total Lagrangian: LSM + LSextet
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
2 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 2.
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
[INFO] UFO output: /tmp/repair_bench/368sextets/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
154 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 154.
149 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 149
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {A, G, CC[sFubar], u}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {A, G, CC[sFubar], c}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Y not conserved in vertex {A, G, CC[sFubar], t}.
Quantum number Y not conserved in vertex {G, Z, CC[sFubar], u}.
Quantum number Y not conserved in vertex {G, Z, CC[sFubar], c}.
Quantum number Y not conserved in vertex {G, Z, CC[sFubar], t}.
Quantum number Y not conserved in vertex {A, G, G, CC[sFubar], u}.
Quantum number Y not conserved in vertex {A, G, G, CC[sFubar], c}.
Quantum number Y not conserved in vertex {A, G, G, CC[sFubar], t}.
Quantum number Y not conserved in vertex {G, G, Z, CC[sFubar], u}.
Quantum number Y not conserved in vertex {G, G, Z, CC[sFubar], c}.
Quantum number Y not conserved in vertex {G, G, Z, CC[sFubar], t}.
Quantum number Y not conserved in vertex {A, G, CC[dbar], sFd}.
Quantum number Y not conserved in vertex {A, G, CC[sbar], sFd}.
Quantum number Y not conserved in vertex {A, G, CC[bbar], sFd}.
Quantum number Y not conserved in vertex {G, Z, CC[dbar], sFd}.
Quantum number Y not conserved in vertex {G, Z, CC[sbar], sFd}.
Quantum number Y not conserved in vertex {G, Z, CC[bbar], sFd}.
Quantum number Y not conserved in vertex {A, G, G, CC[dbar], sFd}.
Quantum number Y not conserved in vertex {A, G, G, CC[sbar], sFd}.
Quantum number Y not conserved in vertex {A, G, G, CC[bbar], sFd}.
Quantum number Y not conserved in vertex {G, G, Z, CC[dbar], sFd}.
Quantum number Y not conserved in vertex {G, G, Z, CC[sbar], sFd}.
Quantum number Y not conserved in vertex {G, G, Z, CC[bbar], sFd}.
Quantum number Y not conserved in vertex {A, G, dbar, CC[sFd]}.
Quantum number Y not conserved in vertex {A, G, sbar, CC[sFd]}.
Quantum number Y not conserved in vertex {A, G, bbar, CC[sFd]}.
Quantum number Y not conserved in vertex {G, Z, dbar, CC[sFd]}.
Quantum number Y not conserved in vertex {G, Z, sbar, CC[sFd]}.
Quantum number Y not conserved in vertex {G, Z, bbar, CC[sFd]}.
Quantum number Y not conserved in vertex {A, G, G, dbar, CC[sFd]}.
Quantum number Y not conserved in vertex {A, G, G, sbar, CC[sFd]}.
Quantum number Y not conserved in vertex {A, G, G, bbar, CC[sFd]}.
Quantum number Y not conserved in vertex {G, G, Z, dbar, CC[sFd]}.
Quantum number Y not conserved in vertex {G, G, Z, sbar, CC[sFd]}.
Quantum number Y not conserved in vertex {G, G, Z, bbar, CC[sFd]}.
Quantum number Y not conserved in vertex {A, G, sFubar, CC[u]}.
Quantum number Y not conserved in vertex {A, G, sFubar, CC[c]}.
Quantum number Y not conserved in vertex {A, G, sFubar, CC[t]}.
Quantum number Y not conserved in vertex {G, Z, sFubar, CC[u]}.
Quantum number Y not conserved in vertex {G, Z, sFubar, CC[c]}.
Quantum number Y not conserved in vertex {G, Z, sFubar, CC[t]}.
Quantum number Y not conserved in vertex {A, G, G, sFubar, CC[u]}.
Quantum number Y not conserved in vertex {A, G, G, sFubar, CC[c]}.
Quantum number Y not conserved in vertex {A, G, G, sFubar, CC[t]}.
Quantum number Y not conserved in vertex {G, G, Z, sFubar, CC[u]}.
Quantum number Y not conserved in vertex {G, G, Z, sFubar, CC[c]}.
Quantum number Y not conserved in vertex {G, G, Z, sFubar, CC[t]}.
Quantum number Y not conserved in vertex {G, sSdbar, ebar, CC[d]}.
Quantum number Y not conserved in vertex {G, sSdbar, ebar, CC[s]}.
Quantum number Y not conserved in vertex {G, sSdbar, ebar, CC[b]}.
Quantum number Y not conserved in vertex {G, sSdbar, mubar, CC[d]}.
Quantum number Y not conserved in vertex {G, sSdbar, mubar, CC[s]}.
Quantum number Y not conserved in vertex {G, sSdbar, mubar, CC[b]}.
Quantum number Y not conserved in vertex {G, sSdbar, tabar, CC[d]}.
Quantum number Y not conserved in vertex {G, sSdbar, tabar, CC[s]}.
Quantum number Y not conserved in vertex {G, sSdbar, tabar, CC[b]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, ebar, CC[d]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, ebar, CC[s]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, ebar, CC[b]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, mubar, CC[d]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, mubar, CC[s]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, mubar, CC[b]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, tabar, CC[d]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, tabar, CC[s]}.
Quantum number Y not conserved in vertex {G, G, sSdbar, tabar, CC[b]}.
Quantum number Y not conserved in vertex {G, sSubar, ebar, CC[u]}.
Quantum number Y not conserved in vertex {G, sSubar, ebar, CC[c]}.
Quantum number Y not conserved in vertex {G, sSubar, ebar, CC[t]}.
Quantum number Y not conserved in vertex {G, sSubar, mubar, CC[u]}.
Quantum number Y not conserved in vertex {G, sSubar, mubar, CC[c]}.
Quantum number Y not conserved in vertex {G, sSubar, mubar, CC[t]}.
Quantum number Y not conserved in vertex {G, sSubar, tabar, CC[u]}.
Quantum number Y not conserved in vertex {G, sSubar, tabar, CC[c]}.
Quantum number Y not conserved in vertex {G, sSubar, tabar, CC[t]}.
Quantum number Y not conserved in vertex {G, G, sSubar, ebar, CC[u]}.
Quantum number Y not conserved in vertex {G, G, sSubar, ebar, CC[c]}.
Quantum number Y not conserved in vertex {G, G, sSubar, ebar, CC[t]}.
Quantum number Y not conserved in vertex {G, G, sSubar, mubar, CC[u]}.
Quantum number Y not conserved in vertex {G, G, sSubar, mubar, CC[c]}.
Quantum number Y not conserved in vertex {G, G, sSubar, mubar, CC[t]}.
Quantum number Y not conserved in vertex {G, G, sSubar, tabar, CC[u]}.
Quantum number Y not conserved in vertex {G, G, sSubar, tabar, CC[c]}.
Quantum number Y not conserved in vertex {G, G, sSubar, tabar, CC[t]}.
Quantum number Y not conserved in vertex {G, sFdbar, CC[d]}.
Quantum number Y not conserved in vertex {G, sFdbar, CC[s]}.
Quantum number Y not conserved in vertex {G, sFdbar, CC[b]}.
Quantum number Y not conserved in vertex {G, G, sFdbar, CC[d]}.
Quantum number Y not conserved in vertex {G, G, sFdbar, CC[s]}.
Quantum number Y not conserved in vertex {G, G, sFdbar, CC[b]}.
Quantum number Y not conserved in vertex {G, sFubar, CC[u]}.
Quantum number Y not conserved in vertex {G, sFubar, CC[c]}.
Quantum number Y not conserved in vertex {G, sFubar, CC[t]}.
Quantum number Y not conserved in vertex {G, G, sFubar, CC[u]}.
Quantum number Y not conserved in vertex {G, G, sFubar, CC[c]}.
Quantum number Y not conserved in vertex {G, G, sFubar, CC[t]}.
Quantum number Y not conserved in vertex {G, CC[dbar], sFd}.
Quantum number Y not conserved in vertex {G, CC[sbar], sFd}.
Quantum number Y not conserved in vertex {G, CC[bbar], sFd}.
Quantum number Y not conserved in vertex {G, G, CC[dbar], sFd}.
Quantum number Y not conserved in vertex {G, G, CC[sbar], sFd}.
Quantum number Y not conserved in vertex {G, G, CC[bbar], sFd}.
Quantum number Y not conserved in vertex {G, CC[ubar], sFu}.
Quantum number Y not conserved in vertex {G, CC[cbar], sFu}.
Quantum number Y not conserved in vertex {G, CC[tbar], sFu}.
Quantum number Y not conserved in vertex {G, G, CC[ubar], sFu}.
Quantum number Y not conserved in vertex {G, G, CC[cbar], sFu}.
Quantum number Y not conserved in vertex {G, G, CC[tbar], sFu}.
Quantum number Y not conserved in vertex {G, sSd, CC[dbar], e}.
Quantum number Y not conserved in vertex {G, sSd, CC[dbar], mu}.
Quantum number Y not conserved in vertex {G, sSd, CC[dbar], ta}.
Quantum number Y not conserved in vertex {G, sSd, CC[sbar], e}.
Quantum number Y not conserved in vertex {G, sSd, CC[sbar], mu}.
Quantum number Y not conserved in vertex {G, sSd, CC[sbar], ta}.
Quantum number Y not conserved in vertex {G, sSd, CC[bbar], e}.
Quantum number Y not conserved in vertex {G, sSd, CC[bbar], mu}.
Quantum number Y not conserved in vertex {G, sSd, CC[bbar], ta}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[dbar], e}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[dbar], mu}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[dbar], ta}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[sbar], e}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[sbar], mu}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[sbar], ta}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[bbar], e}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[bbar], mu}.
Quantum number Y not conserved in vertex {G, G, sSd, CC[bbar], ta}.
Quantum number Y not conserved in vertex {G, sSu, CC[ubar], e}.
Quantum number Y not conserved in vertex {G, sSu, CC[ubar], mu}.
Quantum number Y not conserved in vertex {G, sSu, CC[ubar], ta}.
Quantum number Y not conserved in vertex {G, sSu, CC[cbar], e}.
Quantum number Y not conserved in vertex {G, sSu, CC[cbar], mu}.
Quantum number Y not conserved in vertex {G, sSu, CC[cbar], ta}.
Quantum number Y not conserved in vertex {G, sSu, CC[tbar], e}.
Quantum number Y not conserved in vertex {G, sSu, CC[tbar], mu}.
Quantum number Y not conserved in vertex {G, sSu, CC[tbar], ta}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[ubar], e}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[ubar], mu}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[ubar], ta}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[cbar], e}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[cbar], mu}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[cbar], ta}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[tbar], e}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[tbar], mu}.
Quantum number Y not conserved in vertex {G, G, sSu, CC[tbar], ta}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/331 .
    - Writing files.

Part::partw: Part 3 of {{NP, 2}, {NP, 0}} does not exist.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
dels/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench/368sextets/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/368sextets/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
aph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench/368sextets/round0/UFO
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
