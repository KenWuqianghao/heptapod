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
Non diagonal mass term found: (Acoup*eta*fpi*grho*K0bar*vev)/(2*Sqrt[3])
Non diagonal mass term found: (Acoup*fpi*grho*K0bar*pi0*vev)/2
Non diagonal mass term found: -((Acoup*fpi*grho*Kpbar*pip*vev)/Sqrt[2])
Non diagonal mass term found: (eta*fpi*grho*K0*vev*Conjugate[Acoup])/(2*Sqrt[3])
Non diagonal mass term found: (fpi*grho*K0*pi0*vev*Conjugate[Acoup])/2
Non diagonal mass term found: -((fpi*grho*Kp*pipbar*vev*Conjugate[Acoup])/Sqrt[2])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (vev*y*Lmbar[Index[Spin, sp], Index[HCIndex, aa]] . ProjM . Nvlc[Index[Spin, sp], Index[HCIndex, aa]])/Sqrt[2] + (vev*yt*Lmbar[Index[Spin, sp], Index[HCIndex, aa]] . ProjP . Nvlc[Index[Spin, sp], Index[HCIndex, aa]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (vev*Conjugate[y]*Nvlcbar[Index[Spin, r$3285], Index[HCIndex, aa]] . ProjM . Lm[Index[Spin, r$3285], Index[HCIndex, aa]])/Sqrt[2] + (vev*Conjugate[yt]*Nvlcbar[Index[Spin, r$3287], Index[HCIndex, aa]] . ProjP . Lm[Index[Spin, r$3287], Index[HCIndex, aa]])/Sqrt[2]
```

## FeynRules / Wolfram Engine output (tail)
```
rentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, 2]] + Lmbar[Index[Spin, SP$1], 3] . Ga[Index[Lorentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, 3]]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.

Symbol::symname: The string "ISUMObjectaI7[Index[Lorentz, Ext[1]]]L0bar[Index[Spin, SP$1], 1] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, 1]] + L0bar[Index[Spin, SP$1], 2] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, 2]] + L0bar[Index[Spin, SP$1], 3] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, 3]]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.

General::stop: Further output of Symbol::symname will be suppressed during this calculation.
From kernel 5 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 6 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 7 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 8 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 5 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.

General::stop: Further output of Table::iterb will be suppressed during this calculation.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 176
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {eta, G0, K0bar}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {eta, H, K0bar}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
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
Quantum number Q not conserved in vertex {GP}.
Quantum number Q not conserved in vertex {GPbar}.
Quantum number Q not conserved in vertex {A, pip, W}.
Quantum number Q not conserved in vertex {A, pipbar, Wbar}.
Quantum number Q not conserved in vertex {pip, W, Z}.
Quantum number Q not conserved in vertex {pipbar, Wbar, Z}.
Quantum number Q not conserved in vertex {A, K0bar, Kp, W}.
Quantum number Q not conserved in vertex {K0bar, Kp, W}.
Quantum number Q not conserved in vertex {pi0, pip, W}.
Quantum number Q not conserved in vertex {A, A, pip, W}.
Quantum number Q not conserved in vertex {A, pip, W, Z}.
Quantum number Q not conserved in vertex {A, K0, Kpbar, Wbar}.
Quantum number Q not conserved in vertex {K0, Kpbar, Wbar}.
Quantum number Q not conserved in vertex {pi0, pipbar, Wbar}.
Quantum number Q not conserved in vertex {A, A, pipbar, Wbar}.
Quantum number Q not conserved in vertex {A, pipbar, Wbar, Z}.
Quantum number Q not conserved in vertex {K0bar, Kp, W, Z}.
Quantum number Q not conserved in vertex {pip, W, Z, Z}.
Quantum number Q not conserved in vertex {K0, Kpbar, Wbar, Z}.
Quantum number Q not conserved in vertex {pipbar, Wbar, Z, Z}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/254 .
    - Writing files.
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
[1;31mCommand "import /private/tmp/repair_bench2/VLC_LN/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/VLC_LN/round1/UFO" with error:
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
models.import_ufo.InvalidModel: name WL define multiple time. Please correct the UFO model!

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
