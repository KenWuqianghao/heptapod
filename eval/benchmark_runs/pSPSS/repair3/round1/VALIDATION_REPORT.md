# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: mg5_import_fail, ufo_semantic_error, mg5_python_traceback, mg5_invalid_cmd

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
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: (n4bar[Index[Spin, r$2933]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2933, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15063], Index[Spin, j$15063]])/2 + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2937]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2937, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15065], Index[Spin, j$15065]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: -1/2*(n5bar[Index[Spin, r$2934]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2934, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15063], Index[Spin, j$15063]]) + I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2938]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2938, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15065], Index[Spin, j$15065]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2937]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2937, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15065], Index[Spin, j$15065]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2938]] . del[vm[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2938, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15065], Index[Spin, j$15065]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2940]] . del[n4[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2940, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15065], Index[Spin, j$15065]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]]
Warning: not numerical value encountered. Unable to decide whether kinetic term is diagonal
Non diagonal kinetic term found: I*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2940]] . del[n5[Index[Spin1]], Index[Lorentz, mu]]*Ga[0, r$2940, Index[Spin2]]*Ga[Index[Lorentz, mu], Index[Spin, i$15065], Index[Spin, j$15065]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]]
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]]*n4bar[Index[Spin, r$2937]] . n5[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2937, sp1])/Sqrt[2]) - (I*Mmaj*Conjugate[Ga[0, r$2933, sp1]]*n4bar[Index[Spin, r$2933]] . n5[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 5]])/Sqrt[2] - I/2*vev*Conjugate[UnCL[Index[Generation, 1], Index[Neutrino, 4]]]*n4bar[Index[Spin, i$15536]] . n5[Index[Spin, j$15536]]*ProjP[Index[Spin, i$15536], Index[Spin, j$15536]]*yvn[Index[Generation, 1]] - (vev*Conjugate[UnCL[Index[Generation, 1], Index[Neutrino, 5]]]*n4bar[Index[Spin, j$15544]] . n5[Index[Spin, i$15544]]*ProjP[Index[Spin, j$15544], Index[Spin, i$15544]]*yvn[Index[Generation, 1]])/2 + I/2*vev*n4bar[Index[Spin, j$15634]] . n5[Index[Spin, i$15634]]*ProjM[Index[Spin, j$15634], Index[Spin, i$15634]]*UnCL[Index[Generation, 1], Index[Neutrino, 4]]*yvn[Index[Generation, 1]] - (vev*n4bar[Index[Spin, i$15640]] . n5[Index[Spin, j$15640]]*ProjM[Index[Spin, i$15640], Index[Spin, j$15640]]*UnCL[Index[Generation, 1], Index[Neutrino, 5]]*yvn[Index[Generation, 1]])/2 - I/2*vev*Conjugate[UnCL[Index[Generation, 2], Index[Neutrino, 4]]]*n4bar[Index[Spin, i$15664]] . n5[Index[Spin, j$15664]]*ProjP[Index[Spin, i$15664], Index[Spin, j$15664]]*yvn[Index[Generation, 2]] - (vev*Conjugate[UnCL[Index[Generation, 2], Index[Neutrino, 5]]]*n4bar[Index[Spin, j$15672]] . n5[Index[Spin, i$15672]]*ProjP[Index[Spin, j$15672], Index[Spin, i$15672]]*yvn[Index[Generation, 2]])/2 + I/2*vev*n4bar[Index[Spin, j$15762]] . n5[Index[Spin, i$15762]]*ProjM[Index[Spin, j$15762], Index[Spin, i$15762]]*UnCL[Index[Generation, 2], Index[Neutrino, 4]]*yvn[Index[Generation, 2]] - (vev*n4bar[Index[Spin, i$15768]] . n5[Index[Spin, j$15768]]*ProjM[Index[Spin, i$15768], Index[Spin, j$15768]]*UnCL[Index[Generation, 2], Index[Neutrino, 5]]*yvn[Index[Generation, 2]])/2 - I/2*vev*Conjugate[UnCL[Index[Generation, 3], Index[Neutrino, 4]]]*n4bar[Index[Spin, i$15788]] . n5[Index[Spin, j$15788]]*ProjP[Index[Spin, i$15788], Index[Spin, j$15788]]*yvn[Index[Generation, 3]] - (vev*Conjugate[UnCL[Index[Generation, 3], Index[Neutrino, 5]]]*n4bar[Index[Spin, j$15796]] . n5[Index[Spin, i$15796]]*ProjP[Index[Spin, j$15796], Index[Spin, i$15796]]*yvn[Index[Generation, 3]])/2 + I/2*vev*n4bar[Index[Spin, j$15890]] . n5[Index[Spin, i$15890]]*ProjM[Index[Spin, j$15890], Index[Spin, i$15890]]*UnCL[Index[Generation, 3], Index[Neutrino, 4]]*yvn[Index[Generation, 3]] - (vev*n4bar[Index[Spin, i$15896]] . n5[Index[Spin, j$15896]]*ProjM[Index[Spin, i$15896], Index[Spin, j$15896]]*UnCL[Index[Generation, 3], Index[Neutrino, 5]]*yvn[Index[Generation, 3]])/2
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (I*Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 5]]]*n5bar[Index[Spin, r$2938]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2938, sp1])/Sqrt[2] - (Mmaj*Conjugate[Ga[0, r$2934, sp1]]*n5bar[Index[Spin, r$2934]] . n4[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 4]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (I*Mmaj*Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 2]]]*vmbar[Index[Spin, r$2940]] . n4[Index[Spin, sp1]] . Ga[0]*Ga[0, r$2940, sp1])/Sqrt[2] - (vev*Conjugate[UnCL[Index[Generation, 1], I
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
qrt[2] - (vev*n4bar[Index[Spin, i$15604]] . vm[Index[Spin, j$15604]]*ProjM[Index[Spin, i$15604], Index[Spin, j$15604]]*UnCL[Index[Generation, 1], Index[Neutrino, 2]]*yvn[Index[Generation, 1]])/2 - (vev*n4bar[Index[Spin, i$15732]] . vm[Index[Spin, j$15732]]*ProjM[Index[Spin, i$15732], Index[Spin, j$15732]]*UnCL[Index[Generation, 2], Index[Neutrino, 2]]*yvn[Index[Generation, 2]])/2 - (vev*n4bar[Index[Spin, i$15860]] . vm[Index[Spin, j$15860]]*ProjM[Index[Spin, i$15860], Index[Spin, j$15860]]*UnCL[Index[Generation, 3], Index[Neutrino, 2]]*yvn[Index[Generation, 3]])/2
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((Mmaj*Conjugate[Ga[0, r$2934, sp1]]*n5bar[Index[Spin, r$2934]] . vm[Index[Spin, sp1]]*Un[Index[Neutrino, 5], Index[Neutrino, 2]])/Sqrt[2]) + I/2*vev*n5bar[Index[Spin, i$15610]] . vm[Index[Spin, j$15610]]*ProjM[Index[Spin, i$15610], Index[Spin, j$15610]]*UnCL[Index[Generation, 1], Index[Neutrino, 2]]*yvn[Index[Generation, 1]] + I/2*vev*n5bar[Index[Spin, i$15738]] . vm[Index[Spin, j$15738]]*ProjM[Index[Spin, i$15738], Index[Spin, j$15738]]*UnCL[Index[Generation, 2], Index[Neutrino, 2]]*yvn[Index[Generation, 2]] + I/2*vev*n5bar[Index[Spin, i$15866]] . vm[Index[Spin, j$15866]]*ProjM[Index[Spin, i$15866], Index[Spin, j$15866]]*UnCL[Index[Generation, 3], Index[Neutrino, 2]]*yvn[Index[Generation, 3]]
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench3/pSPSS/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
140 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 140.
135 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 135
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, n4bar, e}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, n5bar, e}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, n4}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, n5}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, n4}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, n4}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, n5}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, n5}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, n4}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, n4}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, n5}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, n5}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, n4}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, n4}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, n5}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, n5}.
Quantum number LeptonNumber not conserved in vertex {G0, n4bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, n4bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, n5bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, n5bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, n4bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, n4bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, n5bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, n5bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, n4bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, n4bar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, n5bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, n5bar, vt}.
Quantum number LeptonNumber not conserved in vertex {GP, n4bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, n5bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, n4}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, n5}.
Quantum number LeptonNumber not conserved in vertex {GP, n4bar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, n5bar, ta}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, n4}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, n5}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/205 .
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
[1;31mCommand "import /private/tmp/repair_bench3/pSPSS/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench3/pSPSS/round0/UFO" with error:
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
convert model /tmp/repair_bench3/pSPSS/round0/UFO
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

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_bench3/pSPSS/round0/UFO/__init__.py", line 2, in <module>
    import particles
  File "/tmp/repair_bench3/pSPSS/round0/UFO/particles.py", line 8, in <module>
    import parameters as Param
  File "/tmp/repair_bench3/pSPSS/round0/UFO/parameters.py", line 31, in <module>
    value = 2 + 1.*e,
                   ^
NameError: name 'e' is not defined. Did you mean: 're'?

```
