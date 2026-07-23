# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

General::stop: Further output of Inner::incom will be suppressed during this calculation.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
45 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 45.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {R2p23hat}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {R2p53hat}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Y not conserved in vertex {R2tm13hat}.
Quantum number Y not conserved in vertex {R2tp23hat}.

                                               5     2      5  2    1    2    1     4
Thread::tdlen: Objects of unequal length in {-(-), -(-)} + {-, -} + - + {-, -(-), -(-)} cannot be combined.
                                               3     3      3  3    3    3    3     3
Quantum number Y not conserved in vertex {R2p23hatbar, R2p53hat, S1bar, S3m13hat}.

                                               2   1     2    1     1    2    1     4
Thread::tdlen: Objects of unequal length in {-(-), -} + {-, -(-)} + - + {-, -(-), -(-)} cannot be combined.
                                               3   3     3    3     3    3    3     3
Quantum number Y not conserved in vertex {R2tm13hatbar, R2tp23hat, S1bar, S3m13hat}.

                                               5     2      2    1     4    2    1     4
Thread::tdlen: Objects of unequal length in {-(-), -(-)} + {-, -(-)} + - + {-, -(-), -(-)} cannot be combined.
                                               3     3      3    3     3    3    3     3

General::stop: Further output of Thread::tdlen will be suppressed during this calculation.
Quantum number Y not conserved in vertex {R2p53hatbar, R2tm13hat, S1tbar, S3m13hat}.
Quantum number Y not conserved in vertex {R2p23hatbar, R2tp23hat, S1tbar, S3m13hat}.
Quantum number Y not conserved in vertex {R2p23hat, R2p53hatbar, S1bar, S3m13hat}.
Quantum number Y not conserved in vertex {R2tm13hat, R2tp23hatbar, S1bar, S3m13hat}.
Quantum number Y not conserved in vertex {R2p23hat, R2p53hatbar, S1, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2tm13hat, R2tp23hatbar, S1, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2p53hat, R2tm13hatbar, S1t, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2p23hat, R2tp23hatbar, S1t, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar, R2p53hat, S1, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar, R2tp23hat, S1, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.

[... block truncated ...]
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[1, 2, aa$3510]]*Ga[0, r$3516, 1]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[2, 2, aa$3510]]*Ga[0, r$3516, 1]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[3, 2, aa$3510]]*Ga[0, r$3516, 1]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[1, 2, aa$3510]]*Ga[0, r$3516, 2]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[2, 2, aa$3510]]*Ga[0, r$3516, 2]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[3, 2, aa$3510]]*Ga[0, r$3516, 2]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[1, 2, aa$3510]]*Ga[0, r$3516, 3]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[2, 2, aa$3510]]*Ga[0, r$3516, 3]*R2p23hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[3, 2, aa$3510]]*Ga[0, r$3516, 3]*R2p23hatbar[Index[Colour, aa$3510]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[1, 1, aa$3510]]*Ga[0, r$3516, 1]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[2, 1, aa$3510]]*Ga[0, r$3516, 1]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[3, 1, aa$3510]]*Ga[0, r$3516, 1]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[1, 1, aa$3510]]*Ga[0, r$3516, 2]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[2, 1, aa$3510]]*Ga[0, r$3516, 2]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[3, 1, aa$3510]]*Ga[0, r$3516, 2]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[1, 1, aa$3510]]*Ga[0, r$3516, 3]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[2, 1, aa$3510]]*Ga[0, r$3516, 3]*R2p53hatbar[Index[Colour, aa$3510]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3516]] . HC[ProjR] . HC[Qbar[3, 1, aa$3510]]*Ga[0, r$3516, 3]*R2p53hatbar[Index[Colour, aa$35
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
2p53hat, S1t, S3p23hat}.
Quantum number Y not conserved in vertex {S1, S3m13hatbar, S3m43hatbar, S3p23hat}.
Quantum number Y not conserved in vertex {S1bar, S1bar, S3p23hat, S3p23hat}.
Quantum number Y not conserved in vertex {GPbar, R2tm13hat, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2tp23hat, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2tp23hat, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, GP, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, GPbar, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {GP, H, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, H, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {GP, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, G0, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {GP, GP, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, H, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, H, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar, R2p53hat, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hat, R2p53hatbar, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar, R2tp23hat, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tm13hat, R2tp23hatbar, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hat, R2tm13hatbar, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hat, R2tp23hatbar, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2p23hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2p23hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GP, R2p53hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, R2tm13hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2tp23hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2tp23hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar, S3m13hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GP, R2p23hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2p53hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2p53hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2tm13hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2tm13hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, R2tp23hatbar, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {S1, S3m13hatbar, S3m43hat, S3p23hatbar}.
Quantum number Y not conserved in vertex {S1, S3m13hat, S3m43hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GP, R2p23hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2p53hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2p53hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2tm13hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2tm13hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, R2tp23hatbar, S1bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {G0, R2p23hatbar, S1tbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {H, R2p23hatbar, S1tbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar, S1tbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, R2p53hatbar, S1tbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {S1bar, S3m13hat, S3m43hat, S3p23hatbar}.
Quantum number Y not conserved in vertex {S1, S1, S3p23hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/715 .
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
[1;31mCommand "import /private/tmp/repair_bench2/SLQrules/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/SLQrules/round2/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
raph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench2/SLQrules/round2/UFO
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
