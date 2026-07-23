# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED (TIMED OUT — the compile exceeded the time limit; the model may need simplification of redundant/expanded terms, without changing the physics)
- Hermiticity check: not reached
- Kinetic-terms check: not reached
- Mass-spectrum check: not reached
- MadGraph import: not reached
- Heuristic error tags: compile_timeout

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
From kernel 1 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 2 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 4 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 6 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 3 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

General::stop: Further output of ToExpression::argb will be suppressed during this calculation.
From kernel 1 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 2 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 3 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 6 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 7 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.

General::stop: Further output of Length `1` of dimension `2` in `3` is incommensurate with length `4` of dimension 1 in `5`. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Mariana Frank
Benjamin Fuks
Ozer Ozdal
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.

ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
   - Loading gauge group classes.
   - Loading parameter classes.

Model ALRM_general_gen loaded.

Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.

Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
[INFO] Total Lagrangian: LSM + LTot
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.

```
