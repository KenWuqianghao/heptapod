# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
t[#3, opt]]}}.

Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x3 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2994, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vtbar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vtbar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vtbar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.

General::stop: Further output of Take::take will be suppressed during this calculation.
From kernel 1 (Local):
Part::pkspec1: The expression PRIVATE`hold[Ext[2], b] cannot be used as a part specification.
From kernel 2 (Local):
Part::pkspec1: The expression PRIVATE`hold[Ext[2], b] cannot be used as a part specification.
From kernel 3 (Local):
Part::pkspec1: The expression PRIVATE`hold[Ext[2], b] cannot be used as a part specification.
From kernel 4 (Local):
Part::pkspec1: The expression PRIVATE`hold[Ext[2], b] cannot be used as a part specification.
From kernel 5 (Local):
Part::pkspec1: The expression PRIVATE`hold[Ext[2], b] cannot be used as a part specification.
From kernel 1 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.
From kernel 2 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.
From kernel 3 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.
From kernel 4 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.
From kernel 5 (Local):
Part::partd: Part specification PRIVATE`TurnFermionicIndexDeltas[[2]] is longer than depth of object.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

General::stop: Further output of Part::partd will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 1 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 2 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 3 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 4 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 5 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 1 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2992, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 2 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2992, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 3 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2992, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 4 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2992, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 5 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$2992, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.

General::stop: Further output of Take::take will be suppressed during this calculation.
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

General::stop: Further output of Select::normal will be suppressed during this calculation.

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/169 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.
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
[1;31mCommand "import /private/tmp/repair_bench/pSPSS/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/pSPSS/round1/UFO" with error:
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
convert model /tmp/repair_bench/pSPSS/round1/UFO
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
