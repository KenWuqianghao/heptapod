# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED
- Hermiticity check: not reached
- Kinetic-terms check: not reached
- Mass-spectrum check: not reached
- MadGraph import: not reached
- Heuristic error tags: lag_symbol_undefined, fr_syntax_error, builtin_symbol_collision, selfconjugate_quantum_numbers

## FeynRules / Wolfram Engine output (tail)
```
[INFO] Loading via explicit file: /Users/kenwu/feynrules-current/FeynRules.m
 - FeynRules - 
Version: 2.3.49 (*29 September 2021).
Authors: A. Alloul, N. Christensen, C. Degrande, C. Duhr, B. Fuks
 
Please cite:
    - Comput.Phys.Commun.185:2250-2300,2014 (arXiv:1310.1921);
    - Comput.Phys.Commun.180:1614-1641,2009 (arXiv:0806.4194).
 
http://feynrules.phys.ucl.ac.be
 
The FeynRules palette can be opened using the command FRPalette[].
[INFO] Loading SM from: /Users/kenwu/feynrules-current/Models/SM/SM.fr
From kernel 2 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/GeneralU1/repair/round0/model.fr")
From kernel 4 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/GeneralU1/repair/round0/model.fr")
From kernel 7 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/GeneralU1/repair/round0/model.fr")
From kernel 1 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/GeneralU1/repair/round0/model.fr")
From kernel 3 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/GeneralU1/repair/round0/model.fr")

General::stop: Further output of Syntax::sntx will be suppressed during this calculation.
From kernel 7 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 3 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 1 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 4 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 2 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 3 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

General::stop: Further output of Warning: Selfconjugated fields should not carry quantumnumbers. will be suppressed during this calculation.
From kernel 1 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.
From kernel 3 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.
From kernel 7 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.
From kernel 1 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

General::stop: Further output of Format::nosym will be suppressed during this calculation.
From kernel 3 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 7 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 3 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 5 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 6 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 7 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
Merging model-files...

Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/GeneralU1/repair/round0/model.fr")
This model implementation was created by
Arindam Das
P. S. Bhupal Dev
Yutaka Hosotani
Sanjoy Mandal
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

General::stop: Further output of N::argt will be suppressed during this calculation.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model GeneralU1_gen loaded.
[INFO] Total Lagrangian: LSM + LGeneralU1
Error: BSM Lagrangian symbol 'LGeneralU1' is undefined in the model.


```
