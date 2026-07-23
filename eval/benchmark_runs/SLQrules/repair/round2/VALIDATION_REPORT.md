# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
ntum number Y not conserved in vertex {R2tm13hatbar, W, Z}.
Quantum number Q not conserved in vertex {S3p23hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {S3p23hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m13hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {S3m13hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m43hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {S3m43hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {R2p53hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2p53hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {R2p23hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2p23hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {R2tp23hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2tp23hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {R2tm13hatbar, Wbar, Z}.
Quantum number Y not conserved in vertex {R2tm13hatbar, Wbar, Z}.
Preparing Python output.

Part::pkspec1: The expression LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]] cannot be used as a part specification.

Inner::normal: Nonatomic expression expected at position 3 in Inner[PRIVATE`TurnFermionicIndexDeltas, LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], List].

Join::heads: Heads Inner and List at positions 1 and 2 are expected to be the same.

Join::heads: Heads Inner and List at positions 1 and 2 are expected to be the same.

Join::heads: Heads Inner and List at positions 1 and 2 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.

Function::slotn: Slot number 2 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[1].

Function::slotn: Slot number 3 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[1].

Function::slotn: Slot number 3 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[{R2p23hat, 1}, 2].

General::stop: Further output of Function::slotn will be suppressed during this calculation.

Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

Part::pkspec1: The expression LLbar[Index[Spin, g], 2] . HC[ProjL] . u[Index[Spin, h]] cannot be used as a part specification.

Inner::normal: Nonatomic expression expected at position 3 in Inner[PRIVATE`TurnFermionicIndexDeltas, LLbar[Index[Spin, g], 2] . HC[ProjL] . u[Index[Spin, h]], List].

Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 2] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

Part::pkspec1: The expression LLbar[Index[Spin, g], 1] . HC[ProjL] . d[Index[Spin, h]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

Inner::normal: Nonatomic expression expected at position 3 in Inner[PRIVATE`TurnFermionicIndexDeltas, LLbar[Index[Spin, g], 1] . HC[ProjL] . d[Index[Spin, h]], List].

General::stop: Further output of Inner::normal will be suppressed during this calculation.

Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.

ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . d[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.

MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.

MapAt::partw: Part {1} of List does not exist.

MapAt::partw: Part {1} of 1 does not exist.

General::stop: Further output of MapAt::partw will be suppressed during this calculation.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
From kernel 1 (Local):
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
From kernel 2 (Local):
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
From kernel 3 (Local):
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
From kernel 4 (Local):
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
From kernel 8 (Local):
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.

General::stop: Further output of MapAt::partw will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of MapAt::partw will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of MapAt::partw will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of MapAt::partw will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of MapAt::partw will be suppressed during this calculation.
From kernel 8 (Local):
General::stop: Further output of MapAt::partw will be suppressed during this calculation.
From kernel 1 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 2 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 3 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 4 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 8 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 1 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 8 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 3 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 4 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 6 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 1 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 6 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[LLbar[Index[Spin, g], 1] . HC[ProjL] . u[Index[Spin, h]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/575 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
C/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_bench/SLQrules/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/SLQrules/round1/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
graph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench/SLQrules/round1/UFO
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
