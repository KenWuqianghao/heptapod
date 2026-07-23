# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
r[u[Index[Spin, 3], Index[Colour, 2]]] . Ga[Index[Lorentz, mu]] . ProjM . u[Index[Spin, 3], Index[Colour, 2]]*ZR[Index[Lorentz, mu]] + gZRq*gZRuR*bar[u[Index[Spin, 3], Index[Colour, 2]]] . Ga[Index[Lorentz, mu]] . ProjP . u[Index[Spin, 3], Index[Colour, 2]]*ZR[Index[Lorentz, mu]] + gZRq*gZRuL*bar[u[Index[Spin, 3], Index[Colour, 3]]] . Ga[Index[Lorentz, mu]] . ProjM . u[Index[Spin, 3], Index[Colour, 3]]*ZR[Index[Lorentz, mu]] + gZRq*gZRuR*bar[u[Index[Spin, 3], Index[Colour, 3]]] . Ga[Index[Lorentz, mu]] . ProjP . u[Index[Spin, 3], Index[Colour, 3]]*ZR[Index[Lorentz, mu]]
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench/EffLRSM/round1/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
36 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 36.
31 vertices obtained.
Flavor expansion of the vertices: Dynamic[FR$Count1] / 31

Part::partw: Part 1 of {} does not exist.

Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.

Part::partw: Part 1 of {} does not exist.

Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.

Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.

Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.

Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.

Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.

ReplaceRepeated::reps: {Join[{dq[1] -> d, dq[2] -> s, dq[3] -> b}, {dqbar[1] -> dbar, dqbar[2] -> sbar, dqbar[3] -> bbar}, IndexRange[HN[Index[{}[[1]]]] -> {N1, N2, N3}[[Index[{}[[1]]]]]], IndexRange[HNbar[Index[{}[[1]]]] -> {N1bar, N2bar, N3bar}[[Index[{}[[1]]]]]], {l[1] -> e, l[2] -> mu, l[3] -> ta}, {lbar[1] -> ebar, lbar[2] -> mubar, lbar[3] -> tabar}, {uq[1] -> u, uq[2] -> c, uq[3] -> t}, {uqbar[1] -> ubar, uqbar[2] -> cbar, uqbar[3] -> tbar}, {vl[1] -> ve, vl[2] -> vm, vl[3] -> vt}, {vlbar[1] -> vebar, vlbar[2] -> vmbar, vlbar[3] -> vtbar}, {CC[dq][1] -> CC[d], CC[dq][2] -> CC[s], CC[dq][3] -> CC[b]}, {CC[dqbar][1] -> CC[dbar], CC[dqbar][2] -> CC[sbar], CC[dqbar][3] -> CC[bbar]}, {CC[l][1] -> CC[e], CC[l][2] -> CC[mu], CC[l][3] -> CC[ta]}, {CC[lbar][1] -> CC[ebar], CC[lbar][2] -> CC[mubar], CC[lbar][3] -> CC[tabar]}, {CC[uq][1] -> CC[u], CC[uq][2] -> CC[c], CC[uq][3] -> CC[t]}, {CC[uqbar][1] -> CC[ubar], CC[uqbar][2] -> CC[cbar], CC[uqbar][3] -> CC[tbar]}, {CC[vl][1] -> CC[ve], CC[vl][2] -> CC[vm], CC[vl][3] -> CC[vt]}, {CC[vlbar][1] -> CC[vebar], CC[vlbar][2] -> CC[vmbar], CC[vlbar][3] -> CC[vtbar]}]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

ReplaceRepeated::reps: {Join[{dq[1] -> d, dq[2] -> s, dq[3] -> b}, {dqbar[1] -> dbar, dqbar[2] -> sbar, dqbar[3] -> bbar}, IndexRange[HN[Index[{}[[1]]]] -> {N1, N2, N3}[[Index[{}[[1]]]]]], IndexRange[HNbar[Index[{}[[1]]]] -> {N1bar, N2bar, N3bar}[[Index[{}[[1]]]]]], {l[1] -> e, l[2] -> mu, l[3] -> ta}, {lbar[1] -> ebar, lbar[2] -> mubar, lbar[3] -> tabar}, {uq[1] -> u, uq[2] -> c, uq[3] -> t}, {uqbar[1] -> ubar, uqbar[2] -> cbar, uqbar[3] -> tbar}, {vl[1] -> ve, vl[2] -> vm, vl[3] -> vt}, {vlbar[1] -> vebar, vlbar[2] -> vmbar, vlbar[3] -> vtbar}, {CC[dq][1] -> CC[d], CC[dq][2] -> CC[s], CC[dq][3] -> CC[b]}, {CC[dqbar][1] -> CC[dbar], CC[dqbar][2] -> CC[sbar], CC[dqbar][3] -> CC[bbar]}, {CC[l][1] -> CC[e], CC[l][2] -> CC[mu], CC[l][3] -> CC[ta]}, {CC[lbar][1] -> CC[ebar], CC[lbar][2] -> CC[mubar], CC[lbar][3] -> CC[tabar]}, {CC[uq][1] -> CC[u], CC[uq][2] -> CC[c], CC[uq][3] -> CC[t]}, {CC[uqbar][1] -> CC[ubar], CC[uqbar][2] -> CC[cbar], CC[uqbar][3] -> CC[tbar]}, {CC[vl][1] -> CC[ve], CC[vl][2] -> CC[vm], CC[vl][3] -> CC[vt]}, {CC[vlbar][1] -> CC[vebar], CC[vlbar][2] -> CC[vmbar], CC[vlbar][3] -> CC[vtbar]}]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

ReplaceRepeated::reps: {Join[{dq[1] -> d, dq[2] -> s, dq[3] -> b}, {dqbar[1] -> dbar, dqbar[2] -> sbar, dqbar[3] -> bbar}, IndexRange[HN[Index[{}[[1]]]] -> {N1, N2, N3}[[Index[{}[[1]]]]]], IndexRange[HNbar[Index[{}[[1]]]] -> {N1bar, N2bar, N3bar}[[Index[{}[[1]]]]]], {l[1] -> e, l[2] -> mu, l[3] -> ta}, {lbar[1] -> ebar, lbar[2] -> mubar, lbar[3] -> tabar}, {uq[1] -> u, uq[2] -> c, uq[3] -> t}, {uqbar[1] -> ubar, uqbar[2] -> cbar, uqbar[3] -> tbar}, {vl[1] -> ve, vl[2] -> vm, vl[3] -> vt}, {vlbar[1] -> vebar, vlbar[2] -> vmbar, vlbar[3] -> vtbar}, {CC[dq][1] -> CC[d], CC[dq][2] -> CC[s], CC[dq][3] -> CC[b]}, {CC[dqbar][1] -> CC[dbar], CC[dqbar][2] -> CC[sbar], CC[dqbar][3] -> CC[bbar]}, {CC[l][1] -> CC[e], CC[l][2] -> CC[mu], CC[l][3] -> CC[ta]}, {CC[lbar][1] -> CC[ebar], CC[lbar][2] -> CC[mubar], CC[lbar][3] -> CC[tabar]}, {CC[uq][1] -> CC[u], CC[uq][2] -> CC[c], CC[uq][3] -> CC[t]}, {CC[uqbar][1] -> CC[ubar], CC[uqbar][2] -> CC[cbar], CC[uqbar][3] -> CC[tbar]}, {CC[vl][1] -> CC[ve], CC[vl][2] -> CC[vm], CC[vl][3] -> CC[vt]}, {CC[vlbar][1] -> CC[vebar], CC[vlbar][2] -> CC[vmbar], CC[vlbar][3] -> CC[vtbar]}]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of ReplaceRepeated::reps will be suppressed during this calculation.
   - Saved vertices in InterfaceRun[ 1 ].
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
From kernel 1 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 2 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 3 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 4 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 5 (Local):
Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 1 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 2 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 3 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 4 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 5 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 2 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 3 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 4 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 5 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.
From kernel 1 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 2 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 3 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 4 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 5 (Local):
Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 1 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 2 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 3 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 4 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.
From kernel 5 (Local):
Part::pkspec1: The expression Index[{}[[1]]] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::partw will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 2 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 3 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 4 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.
From kernel 5 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 3 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/31 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
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
[1;31mCommand "import /private/tmp/repair_bench/EffLRSM/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench/EffLRSM/round1/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
dgraph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench/EffLRSM/round1/UFO
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
