# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: mg5_import_fail, mg5_python_traceback

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
ctrum
[INFO] UFO output: /tmp/repair_bench2/B-L-SM/round2/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
162 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 162.
157 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 157
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, e}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, e}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, e}.
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, ta}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, vt}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N3}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/201 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench2/B-L-SM/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/B-L-SM/round2/UFO" with error:
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
