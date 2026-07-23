# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
.0
For more information, type ModelInformation[].

   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.

Model VLC_LN_gen loaded.
[INFO] Total Lagrangian: LSM + LTot
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
5 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 5.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Q not conserved in vertex {W}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Q not conserved in vertex {Wbar}.
4 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{A, 1}}, -I*ee*(Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[Index[Lorentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] - Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]])}
{{{W, 1}}, (I*ee*(L0bar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[Index[Lorentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] - L0bar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]]))/(Sqrt[2]*sw)}
{{{Wbar, 1}}, (I*ee*(Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[Index[Lorentz, Ext[1]]] . L0[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] - Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]]))/(Sqrt[2]*sw)}
{{{Z, 1}}, (I/2*ee*((cw^2 + sw^2)*L0bar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[Index[Lorentz, Ext[1]]] . L0[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] + (-cw^2 + sw^2)*Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[Index[Lorentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] - cw^2*L0bar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] - sw^2*L0bar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] + cw^2*Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] - sw^2*Lmbar[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . Lm[Index[Spin, SP$1], Index[HCIndex, HCIndex$1]]))/(cw*sw)}
HEPTAPOD-CHECK-ERROR
HEPTAPOD-CHECK-END: hermiticity
HEPTAPOD-CHECK-BEGIN: kinetic_terms
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
HEPTAPOD-CHECK-END: kinetic_terms
HEPTAPOD-CHECK-BEGIN: mass_spectrum
Neglecting all terms with more than 2 particles.
Non diagonal mass term found: (Acoup*eta*fpi*grho*K0bar*vev)/(2*Sqrt[3])
Non diagonal mass term found: (Acoup*fpi*grho*K0bar*pi0*vev)/2
Non diagonal mass term found: -((Acoup*fpi*grho*Kpbar*pip*vev)/Sqrt[2])
Non diagonal mass term found: (eta*fpi*grho*K0*vev*Conjugate[Acoup])/(2*Sqrt[3])
Non diagonal mass term found: (fpi*grho*K0*pi0*vev*Conjugate[Acoup])/2
Non diagonal mass term found: -((fpi*grho*Kp*pipbar*vev*Conjugate[Acoup])/Sqrt[2])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (vev*y*Lmbar[Index[Spin, sp], Index[HCIndex, aa]] . ProjM . Nvlc[Index[Spin, sp], Index[HCIndex, aa]])/Sqrt[2] + (vev*yt*Lmbar[Index[Spin, sp], Index[HCIndex, aa]] . ProjP . Nvlc[Index[Spin, sp], Index[HCIndex, aa]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (vev*Conjugate[y]*Nvlcbar[Index[Spin, r$3302], Index[HCIndex, aa]] . ProjM . Lm[Index[Spin, r$3302], Index[HCIndex, aa]])/Sqrt[2] + (vev*Conjugate[yt]*Nvlcbar[Index[Spin, r$3304], Index[HCIndex, aa]] . ProjP . Lm[Index[Spin, r$3304], Index[HCIndex, aa]])/Sqrt[2]
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench/VLC_LN/round1/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
196 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 196.
189 vertices obtained.

Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.

Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.

Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.

General::stop: Further output of Table::iterb will be suppressed during this calculation.
From kernel 1 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 1 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 1 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 1 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.

Symbol::symname: The string "ISUMObjectaI1[Index[Lorentz, Ext[1]]]Lvlcbar[Index[Spin, SP$1], 1, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 1], Index[SU2D, 1]] + Lvlcbar[Index[Spin, SP$1], 1, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 1], Index[SU2D, 2]] + Lvlcbar[Index[Spin, SP$1], 2, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 2], Index[SU2D, 1]] + Lvlcbar[Index[Spin, SP$1], 2, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 2], Index[SU2D, 2]] + Lvlcbar[Index[Spin, SP$1], 3, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 3], Index[SU2D, 1]] + Lvlcbar[Index[Spin, SP$1], 3, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 3], Index[SU2D, 2]]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.

Symbol::symname: The string "ISUMObjectaI11[Index[Lorentz, Ext[1]]]Lvlcbar[Index[Spin, SP$1], 1, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 1], 1] + Lvlcbar[Index[Spin, SP$1], 1, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 1], 2] + Lvlcbar[Index[Spin, SP$1], 1, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 1], 1] + Lvlcbar[Index[Spin, SP$1], 1, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 1], 2] + Lvlcbar[Index[Spin, SP$1], 2, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 2], 1] + Lvlcbar[Index[Spin, SP$1], 2, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 2], 2] + Lvlcbar[Index[Spin, SP$1], 2, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 2], 1] + Lvlcbar[Index[Spin, SP$1], 2, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 2], 2] + Lvlcbar[Index[Spin, SP$1], 3, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 3], 1] + Lvlcbar[Index[Spin, SP$1], 3, 1] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 3], 2] + Lvlcbar[Index[Spin, SP$1], 3, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 3], 1] + Lvlcbar[Index[Spin, SP$1], 3, 2] . Ga[Index[Lorentz, Ext[1]]] . Lvlc[Index[Spin, SP$1], Index[HCIndex, 3], 2]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.
From kernel 1 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 1 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 2 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 189
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Y not conserved in vertex {eta, G0, K0bar}.
Quantum number Y not conserved in vertex {eta, H, K0bar}.
Quantum number Q not conserved in vertex {eta, GP, Kpbar}.
Quantum number Y not conserved in vertex {eta, GP, Kpbar}.
Quantum number Y not conserved in vertex {G0, K0bar, pi0}.
Quantum number Y not conserved in vertex {H, K0bar, pi0}.
Quantum number Q not conserved in vertex {GP, Kpbar, pi0}.
Quantum number Y not conserved in vertex {GP, Kpbar, pi0}.
Quantum number Q not conserved in vertex {G0, Kpbar, pip}.
Quantum number Y not conserved in vertex {G0, Kpbar, pip}.
Quantum number Q not conserved in vertex {H, Kpbar, pip}.
Quantum number Y not conserved in vertex {H, Kpbar, pip}.
Quantum number Y not conserved in vertex {GP, K0bar, pipbar}.
Quantum number Y not conserved in vertex {eta, G0, K0}.
Quantum number Y not conserved in vertex {eta, H, K0}.
Quantum number Q not conserved in vertex {eta, GPbar, Kp}.
Quantum number Y not conserved in vertex {eta, GPbar, Kp}.
Quantum number Y not conserved in vertex {G0, K0, pi0}.
Quantum number Y not conserved in vertex {H, K0, pi0}.
Quantum number Q not conserved in vertex {GPbar, Kp, pi0}.
Quantum number Y not conserved in vertex {GPbar, Kp, pi0}.
Quantum number Y not conserved in vertex {GPbar, K0, pip}.
Quantum number Q not conserved in vertex {G0, Kp, pipbar}.
Quantum number Y not conserved in vertex {G0, Kp, pipbar}.
Quantum number Q not conserved in vertex {H, Kp, pipbar}.
Quantum number Y not conserved in vertex {H, Kp, pipbar}.
Quantum number Y not conserved in vertex {Phi}.
Quantum number Y not conserved in vertex {Phibar}.
Quantum number Q not conserved in vertex {eta, W, Wi, Wi}.
Quantum number Q not conserved in vertex {eta, Wbar, Wi, Wi}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/267 .
    - Writing files.

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phi]].

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
el = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: unterminated string literal (detected at line 513) (particles.py, line 513)
[1;31mCommand "import /private/tmp/repair_bench/VLC_LN/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/VLC_LN/round1/UFO" with error:
UFOError : unterminated string literal (detected at line 513) (particles.py, line 513)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
7, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench/VLC_LN/round1/UFO
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
models.UFOError: unterminated string literal (detected at line 513) (particles.py, line 513)
Fail to write options with error No model currently active, please import a model!
```
