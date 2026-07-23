# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

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
112 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 112.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {A, A, R2bar}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {A, R2bar}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Y not conserved in vertex {A, A, R2tbar}.
Quantum number Y not conserved in vertex {A, R2tbar}.
Quantum number Y not conserved in vertex {A, A, S3bar}.
Quantum number Y not conserved in vertex {A, S3bar}.
Quantum number Y not conserved in vertex {A, G, R2bar}.
Quantum number Y not conserved in vertex {G, R2bar}.
Quantum number Y not conserved in vertex {A, G, R2tbar}.
Quantum number Y not conserved in vertex {G, R2tbar}.
Quantum number Q not conserved in vertex {G, S1bar}.
Quantum number Q not conserved in vertex {G, S1tbar}.
Quantum number Y not conserved in vertex {A, G, S3bar}.
Quantum number Y not conserved in vertex {G, S3bar}.
Quantum number Y not conserved in vertex {R2p23hat}.
Quantum number Y not conserved in vertex {R2p53hat}.
Quantum number Y not conserved in vertex {R2tm13hat}.
Quantum number Y not conserved in vertex {R2tp23hat}.
Quantum number Y not conserved in vertex {R2p23hatbar, R2tm13hat, S1, S1tbar}.
Quantum number Y not conserved in vertex {R2p53hatbar, R2tp23hat, S1, S1tbar}.

                                               5     2      5  2    1      2   1  4
Thread::tdlen: Objects of unequal length in {-(-), -(-)} + {-, -} - - + {-(-), -, -} cannot be combined.
                                               3     3      3  3    3      3   3  3
Quantum number Y not conserved in vertex {R2p23hatbar, R2p53hat, S1, S3m13hatbar}.

                                             5  2       5     2     1      2   1  4
Thread::tdlen: Objects of unequal length in {-, -} + {-(-), -(-)} - - + {-(-), -, -} cannot be combined.
                                             3  3       3     3     3      3   3  3
Quantum number Y not conserved in vertex {R2p23hat, R2p53hatbar, S1, S3m13hatbar}.

                                               2   1     2    1     1      2   1  4
Thread::tdlen: Objects of unequal length in {-(-), -} + {-, -(-)} - - + {-(-), -, -} cannot be combined.
                                               3   3     3    3     3      3   3  3

General::stop: Further output of Thread::tdlen will be suppressed during this calculation.
Quantum number Y not conserved in vertex {R2tm13hatbar, R2tp23h
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
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[1, 2, aa$3550]]*Ga[0, r$3556, 1]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[2, 2, aa$3550]]*Ga[0, r$3556, 1]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[3, 2, aa$3550]]*Ga[0, r$3556, 1]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[1, 2, aa$3550]]*Ga[0, r$3556, 2]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[2, 2, aa$3550]]*Ga[0, r$3556, 2]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[3, 2, aa$3550]]*Ga[0, r$3556, 2]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[1, 2, aa$3550]]*Ga[0, r$3556, 3]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[2, 2, aa$3550]]*Ga[0, r$3556, 3]*R2p23hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[3, 2, aa$3550]]*Ga[0, r$3556, 3]*R2p23hatbar[Index[Colour, aa$3550]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[1, 1, aa$3550]]*Ga[0, r$3556, 1]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[2, 1, aa$3550]]*Ga[0, r$3556, 1]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[3, 1, aa$3550]]*Ga[0, r$3556, 1]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[1, 1, aa$3550]]*Ga[0, r$3556, 2]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[2, 1, aa$3550]]*Ga[0, r$3556, 2]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[3, 1, aa$3550]]*Ga[0, r$3556, 2]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[1, 1, aa$3550]]*Ga[0, r$3556, 3]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[2, 1, aa$3550]]*Ga[0, r$3556, 3]*R2p53hatbar[Index[Colour, aa$3550]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3556]] . HC[ProjR] . HC[Qbar[3, 1, aa$3550]]*Ga[0, r$3556, 3]*R2p53hatbar[Index[Colour, aa$35
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
Pbar, R2p53hatbar, S1tbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {S1bar, S3m13hat, S3m43hat, S3p23hatbar}.
Quantum number Y not conserved in vertex {S1, S1, S3p23hatbar, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar, R2p53hat, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hat, R2p53hatbar, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar, R2tp23hat, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2tm13hat, R2tp23hatbar, S1, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hat, R2tm13hatbar, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {R2p23hat, R2tp23hatbar, S1t, S3p23hatbar}.
Quantum number Y not conserved in vertex {A, S3p23hatbar, W}.
Quantum number Y not conserved in vertex {A, S3m13hatbar, W}.
Quantum number Y not conserved in vertex {A, S3m43hatbar, W}.
Quantum number Y not conserved in vertex {S3p23hatbar, W}.
Quantum number Y not conserved in vertex {S3m13hatbar, W}.
Quantum number Y not conserved in vertex {S3m43hatbar, W}.
Quantum number Y not conserved in vertex {A, R2p53hatbar, W}.
Quantum number Y not conserved in vertex {A, R2p23hatbar, W}.
Quantum number Y not conserved in vertex {R2p53hatbar, W}.
Quantum number Y not conserved in vertex {R2p23hatbar, W}.
Quantum number Y not conserved in vertex {A, R2tp23hatbar, W}.
Quantum number Y not conserved in vertex {A, R2tm13hatbar, W}.
Quantum number Y not conserved in vertex {R2tp23hatbar, W}.
Quantum number Y not conserved in vertex {R2tm13hatbar, W}.
Quantum number Q not conserved in vertex {G, W}.
Quantum number Q not conserved in vertex {W, W}.
Quantum number Y not conserved in vertex {A, S3p23hatbar, Wbar}.
Quantum number Y not conserved in vertex {A, S3m13hatbar, Wbar}.
Quantum number Y not conserved in vertex {A, S3m43hatbar, Wbar}.
Quantum number Y not conserved in vertex {S3p23hatbar, Wbar}.
Quantum number Y not conserved in vertex {S3m13hatbar, Wbar}.
Quantum number Y not conserved in vertex {S3m43hatbar, Wbar}.
Quantum number Y not conserved in vertex {A, R2p53hatbar, Wbar}.
Quantum number Y not conserved in vertex {A, R2p23hatbar, Wbar}.
Quantum number Y not conserved in vertex {R2p53hatbar, Wbar}.
Quantum number Y not conserved in vertex {R2p23hatbar, Wbar}.
Quantum number Y not conserved in vertex {A, R2tp23hatbar, Wbar}.
Quantum number Y not conserved in vertex {A, R2tm13hatbar, Wbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar, Wbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar, Wbar}.
Quantum number Q not conserved in vertex {G, Wbar}.
Quantum number Q not conserved in vertex {Wbar, Wbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar}.
Quantum number Y not conserved in vertex {G, R2p53hat, Z}.
Quantum number Y not conserved in vertex {G, R2p23hat, Z}.
Quantum number Y not conserved in vertex {G, R2tp23hat, Z}.
Quantum number Y not conserved in vertex {G, R2tm13hat, Z}.
Quantum number Y not conserved in vertex {G, S3p23hat, Z}.
Quantum number Y not conserved in vertex {G, S3m13hat, Z}.
Quantum number Y not conserved in vertex {G, S3m43hat, Z}.
Quantum number Y not conserved in vertex {S3p23hatbar, W, Z}.
Quantum number Y not conserved in vertex {S3m13hatbar, W, Z}.
Quantum number Y not conserved in vertex {S3m43hatbar, W, Z}.
Quantum number Y not conserved in vertex {R2p53hatbar, W, Z}.
Quantum number Y not conserved in vertex {R2p23hatbar, W, Z}.
Quantum number Y not conserved in vertex {R2tp23hatbar, W, Z}.
Quantum number Y not conserved in vertex {R2tm13hatbar, W, Z}.
Quantum number Y not conserved in vertex {S3p23hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {S3m13hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {S3m43hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2p53hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2p23hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2tp23hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2tm13hatbar, Wbar, Z}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/575 .
    - Writing files.

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phi]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
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
[1;31mCommand "import /private/tmp/repair_bench2/SLQrules/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/SLQrules/round1/UFO" with error:
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
convert model /tmp/repair_bench2/SLQrules/round1/UFO
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

## UFO Python syntax error — `UFO/lorentz.py` line 15: cannot assign to literal here. Maybe you meant '==' instead of '='?
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   13 | 
   14 | 
   15 | 1 = Lorentz(name = '1',
   16 |             spins = [],
   17 |             structure = '1')
```

## UFO Python syntax error — `UFO/vertices.py` line 421: invalid syntax
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  419 | 
  420 | V_69 = Vertex(name = 'V_69',
  421 |               particles = [ P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]], P.R2p53hat__tilde__, P.R2p53hat ],
  422 |               color = [ '1' ],
  423 |               lorentz = [ L.SSSS1 ],
```
