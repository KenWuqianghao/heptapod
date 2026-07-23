# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: duplicate_particle_names, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
ex[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 3], Index[Neutrinos, 4]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v1bar, 1}, {e, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 1]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v1bar, 1}, {mu, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 1]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v1bar, 1}, {ta, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 3], Index[Neutrinos, 1]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v2bar, 1}, {e, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 2]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v2bar, 1}, {mu, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 2]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v2bar, 1}, {ta, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 3], Index[Neutrinos, 2]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v3bar, 1}, {e, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 1], Index[Neutrinos, 3]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v3bar, 1}, {mu, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 2], Index[Neutrinos, 3]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{v3bar, 1}, {ta, 2}, {rho, 3}}, I*Sqrt[2]*frho*Gf*Conjugate[CKM[Index[Generation, 1], Index[Generation, 1]]]*Conjugate[PMNS[Index[Generation, 3], Index[Neutrinos, 3]]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{ebar, 1}, {v1, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 1], Index[Neutrinos, 1]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{ebar, 1}, {v2, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 1], Index[Neutrinos, 2]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{ebar, 1}, {v3, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 1], Index[Neutrinos, 3]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{ebar, 1}, {N4, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 1], Index[Neutrinos, 4]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{mubar, 1}, {v1, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 2], Index[Neutrinos, 1]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{mubar, 1}, {v2, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 2], Index[Neutrinos, 2]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{mubar, 1}, {v3, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 2], Index[Neutrinos, 3]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{mubar, 1}, {N4, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 2], Index[Neutrinos, 4]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tabar, 1}, {v1, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 3], Index[Neutrinos, 1]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tabar, 1}, {v2, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 3], Index[Neutrinos, 2]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tabar, 1}, {v3, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 3], Index[Neutrinos, 3]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tabar, 1}, {N4, 2}, {rhobar, 3}}, -I*Sqrt[2]*frho*Gf*CKM[Index[Generation, 1], Index[Generation, 1]]*PMNS[Index[Generation, 3], Index[Neutrinos, 4]]*TensDot[Ga[Index[Lorentz, Ext[3]]], ProjM][Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
HEPTAPOD-CHECK-END: hermiticity
HEPTAPOD-CHECK-BEGIN: kinetic_terms
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
HEPTAPOD-CHECK-END: kinetic_terms
HEPTAPOD-CHECK-BEGIN: mass_spectrum
Neglecting all terms with more than 2 particles.
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31838]] . v1[Index[Spin, sp2$31839]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31839]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 1], Index[Heavynus, 1]]]*N4bar[Index[Spin, sp2$31840]] . v1[Index[Spin, sp2$31909]]*ProjM[Index[Spin, sp2$31840], Index[Spin, sp2$31909]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31836]] . v1[Index[Spin, sp2$31837]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]*ProjP[Index[Spin, sp2$31836], Index[Spin, sp2$31837]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31838]] . v2[Index[Spin, sp2$31839]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31839]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 2], Index[Heavynus, 1]]]*N4bar[Index[Spin, sp2$31841]] . v2[Index[Spin, sp2$31925]]*ProjM[Index[Spin, sp2$31841], Index[Spin, sp2$31925]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31836]] . v2[Index[Spin, sp2$31837]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]*ProjP[Index[Spin, sp2$31836], Index[Spin, sp2$31837]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31838]] . v3[Index[Spin, sp2$31839]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31839]]) - (vev*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*Conjugate[yN[Index[Generation, 3], Index[Heavynus, 1]]]*N4bar[Index[Spin, sp2$31842]] . v3[Index[Spin, sp2$31941]]*ProjM[Index[Spin, sp2$31842], Index[Spin, sp2$31941]])/Sqrt[2] - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]]*N4bar[Index[Spin, sp2$31836]] . v3[Index[Spin, sp2$31837]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]*ProjP[Index[Spin, sp2$31836], Index[Spin, sp2$31837]]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]]*v1bar[Index[Spin, sp2$31838]] . N4[Index[Spin, sp2$31839]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31839]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 1]]]*v1bar[Index[Spin, sp2$31836]] . N4[Index[Spin, sp2$31837]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31836], Index[Spin, sp2$31837]] - (vev*v1bar[Index[Spin, sp2$31861]] . N4[Index[Spin, sp2$31843]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31861], Index[Spin, sp2$31843]]*yN[Index[Generation, 1], Index[Heavynus, 1]])/Sqrt[2]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]]*v2bar[Index[Spin, sp2$31838]] . N4[Index[Spin, sp2$31839]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31839]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 2]]]*v2bar[Index[Spin, sp2$31836]] . N4[Index[Spin, sp2$31837]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31836], Index[Spin, sp2$31837]] - (vev*v2bar[Index[Spin, sp2$31877]] . N4[Index[Spin, sp2$31844]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31877], Index[Spin, sp2$31844]]*yN[Index[Generation, 2], Index[Heavynus, 1]])/Sqrt[2]
Non diagonal mass term found: -(MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]]*v3bar[Index[Spin, sp2$31838]] . N4[Index[Spin, sp2$31839]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjM[Index[Spin, sp2$31838], Index[Spin, sp2$31839]]) - MN4*Conjugate[HEAV[Index[Heavynus, 1], Index[Neutrinos, 3]]]*v3bar[Index[Spin, sp2$31836]] . N4[Index[Spin, sp2$31837]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31836], Index[Spin, sp2$31837]] - (vev*v3bar[Index[Spin, sp2$31893]] . N4[Index[Spin, sp2$31845]]*HEAV[Index[Heavynus, 1], Index[Neutrinos, 4]]*ProjP[Index[Spin, sp2$31893], Index[Spin, sp2$31845]]*yN[Index[Generation, 3], Index[Heavynus, 1]])/Sqrt[2]
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench/HNLs/round2/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
270 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 270.
267 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 267
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {Phi, v1bar, LL}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {Phi, v2bar, LL}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number LeptonNumber not conserved in vertex {Phi, v3bar, LL}.
Quantum number LeptonNumber not conserved in vertex {Phi, N4bar, LL}.
Quantum number LeptonNumber not conserved in vertex {Phibar, LLbar, v1}.
Quantum number LeptonNumber not conserved in vertex {Phibar, LLbar, v2}.
Quantum number LeptonNumber not conserved in vertex {Phibar, LLbar, v3}.
Quantum number LeptonNumber not conserved in vertex {Phibar, LLbar, N4}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/306 .
    - Writing files.

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[LLbar]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[LLbar]].

General::stop: Further output of StringJoin::string will be suppressed during this calculation.

Part::partw: Part 3 of {{NP, 1}, {NP, 0}} does not exist.
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
[1;31mCommand "import /private/tmp/repair_bench/HNLs/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/HNLs/round2/UFO" with error:
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
convert model /tmp/repair_bench/HNLs/round2/UFO
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
