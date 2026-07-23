# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
6] - I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*del[n4bar[Index[Spin, r$2987]], Index[Lorentz, mu]] . vm[Index[Spin1]]*Ga[0, r$2987, Index[Spin2]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14438, j$14438]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2981]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2981, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14432], Index[Spin, j$14432]]*Un[Index[Neutrino, 4], Index[Neutrino, 2]] + I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2988]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2988, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14434], Index[Spin, j$14434]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]] - I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*del[n5bar[Index[Spin, r$2981]], Index[Lorentz, mu]] . vm[Index[Spin1]]*Ga[0, r$2981, Index[Spin2]]*Un[Index[Neutrino, 4], Index[Neutrino, 2]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14436, j$14436] - I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*del[n5bar[Index[Spin, r$2988]], Index[Lorentz, mu]] . vm[Index[Spin1]]*Ga[0, r$2988, Index[Spin2]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14438, j$14438]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2981]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2981, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14432], Index[Spin, j$14432]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]] + I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2988]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2988, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14434], Index[Spin, j$14434]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]] - I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*del[n5bar[Index[Spin, r$2981]], Index[Lorentz, mu]] . n4[Index[Spin1]]*Ga[0, r$2981, Index[Spin2]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14436, j$14436] - I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*del[n5bar[Index[Spin, r$2988]], Index[Lorentz, mu]] . n4[Index[Spin1]]*Ga[0, r$2988, Index[Spin2]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14438, j$14438]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2983]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2983, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14432], Index[Spin, j$14432]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]] + I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2990]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2990, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14434], Index[Spin, j$14434]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]] - I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*del[vmbar[Index[Spin, r$2983]], Index[Lorentz, mu]] . n4[Index[Spin1]]*Ga[0, r$2983, Index[Spin2]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14436, j$14436] - I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*del[vmbar[Index[Spin, r$2990]], Index[Lorentz, mu]] . n4[Index[Spin1]]*Ga[0, r$2990, Index[Spin2]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14438, j$14438]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2980]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2980, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14432], Index[Spin, j$14432]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]] + I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2987]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2987, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14434], Index[Spin, j$14434]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]] - I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*del[n4bar[Index[Spin, r$2980]], Index[Lorentz, mu]] . n5[Index[Spin1]]*Ga[0, r$2980, Index[Spin2]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14436, j$14436] - I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*del[n4bar[Index[Spin, r$2987]], Index[Lorentz, mu]] . n5[Index[Spin1]]*Ga[0, r$2987, Index[Spin2]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14438, j$14438]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2983]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2983, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14432], Index[Spin, j$14432]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]] + I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2990]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2990, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$14434], Index[Spin, j$14434]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]] - I/2*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*del[vmbar[Index[Spin, r$2983]], Index[Lorentz, mu]] . n5[Index[Spin1]]*Ga[0, r$2983, Index[Spin2]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14436, j$14436] - I/2*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*del[vmbar[Index[Spin, r$2990]], Index[Lorentz, mu]] . n5[Index[Spin1]]*Ga[0, r$2990, Index[Spin2]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]*TensDot[Ga[0], Ga[Index[Lorentz, mu]], Ga[0]][i$14438, j$14438]
HEPTAPOD-CHECK-END: kinetic_terms
HEPTAPOD-CHECK-BEGIN: mass_spectrum
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2987]] . n4bar[Index[Spin, r$2980]]*Ga[0, r$2980, Index[Spin2, i1$14507]]*Ga[0, r$2987, Index[Spin2, i1$14507]])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2987]] . n5bar[Index[Spin, r$2981]]*Ga[0, r$2981, Index[Spin2, i1$14507]]*Ga[0, r$2987, Index[Spin2, i1$14507]]) - Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2988]] . n4bar[Index[Spin, r$2980]]*Ga[0, r$2980, Index[Spin2, i1$14507]]*Ga[0, r$2988, Index[Spin2, i1$14507]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2987]] . vmbar[Index[Spin, r$2983]]*Ga[0, r$2983, Index[Spin2, i1$14507]]*Ga[0, r$2987, Index[Spin2, i1$14507]]) - Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2990]] . n4bar[Index[Spin, r$2980]]*Ga[0, r$2980, Index[Spin2, i1$14507]]*Ga[0, r$2990, Index[Spin2, i1$14507]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2988]] . n5bar[Index[Spin, r$2981]]*Ga[0, r$2981, Index[Spin2, i1$14507]]*Ga[0, r$2988, Index[Spin2, i1$14507]])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 2]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2988]] . vmbar[Index[Spin, r$2983]]*Ga[0, r$2983, Index[Spin2, i1$14507]]*Ga[0, r$2988, Index[Spin2, i1$14507]]) - Mmaj*Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]]*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2990]] . n5bar[Index[Spin, r$2981]]*Ga[0, r$2981, Index[Spin2, i1$14507]]*Ga[0, r$2990, Index[Spin2, i1$14507]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*n4[Index[Spin1, i1$14506]] . vm[Index[Spin1, i1$14506]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]) - Mmaj*vm[Index[Spin1, i1$14506]] . n4[Index[Spin1, i1$14506]]*Un[Index[Neutrino, 4], Index[Neutrino, 2]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*n5[Index[Spin1, i1$14506]] . vm[Index[Spin1, i1$14506]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]) - Mmaj*vm[Index[Spin1, i1$14506]] . n5[Index[Spin1, i1$14506]]*Un[Index[Neutrino, 4], Index[Neutrino, 2]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*n4[Index[Spin1, i1$14506]] . n4[Index[Spin1, i1$14506]]*Un[Index[Neutrino, 4], Index[Neutrino, 4]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(Mmaj*n5[Index[Spin1, i1$14506]] . n5[Index[Spin1, i1$14506]]*Un[Index[Neutrino, 4], Index[Neutrino, 5]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (3*vev*N1L . LL[Index[Spin, 1], Index[SU2D, 1]]*yvn[Index[Generation, 1]])/Sqrt[2] + (3*vev*N1L . LL[Index[Spin, 1], Index[SU2D, 2]]*yvn[Index[Generation, 2]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (3*vev*LLbar[Index[Spin, r$3326], Index[SU2D, 1]] . N1Lbar*Ga[0, r$3326, 1]*yvn[Index[Generation, 1]])/Sqrt[2] + (3*vev*LLbar[Index[Spin, r$3326], Index[SU2D, 2]] . N1Lbar*Ga[0, r$3326, 1]*yvn[Index[Generation, 2]])/Sqrt[2]
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench/pSPSS/round2/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
100 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 100.

Part::partw: Part 1 of {} does not exist.
94 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 94
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {Phi}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/164 .
    - Writing files.

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].
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
[1;31mCommand "import /private/tmp/repair_bench/pSPSS/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/pSPSS/round2/UFO" with error:
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
convert model /tmp/repair_bench/pSPSS/round2/UFO
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
