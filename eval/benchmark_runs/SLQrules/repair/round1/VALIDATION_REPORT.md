# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED
- Hermiticity check: not reached
- Kinetic-terms check: not reached
- Mass-spectrum check: not reached
- MadGraph import: not reached
- Heuristic error tags: lag_symbol_undefined, fr_syntax_error

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
From kernel 6 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^". (line 660 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/SLQrules/repair/round0/model.fr")
From kernel 1 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^". (line 660 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/SLQrules/repair/round0/model.fr")
From kernel 2 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^". (line 660 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/SLQrules/repair/round0/model.fr")
From kernel 3 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^". (line 660 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/SLQrules/repair/round0/model.fr")
From kernel 4 (Local):
Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^". (line 660 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/SLQrules/repair/round0/model.fr")

General::stop: Further output of Syntax::sntx will be suppressed during this calculation.
Merging model-files...

Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^". (line 660 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/SLQrules/repair/round0/model.fr")
This model implementation was created by
Andreas Crivellin
Luc Schnell
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.

Model SLQrules_gen loaded.
[INFO] Total Lagrangian: LSM + LBSM
Error: BSM Lagrangian symbol 'LBSM' is undefined in the model.


```
