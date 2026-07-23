# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED
- Hermiticity check: not reached
- Kinetic-terms check: not reached
- Mass-spectrum check: not reached
- MadGraph import: not reached
- Heuristic error tags: lag_symbol_undefined, fr_syntax_error, duplicate_particle_names, selfconjugate_quantum_numbers

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
From kernel 3 (Local):
Syntax::sntx: Invalid syntax in or before "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r].". (line 565 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/HNLs/repair/round0/model.fr")
                                                              ^
From kernel 4 (Local):
Syntax::sntx: Invalid syntax in or before "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r].". (line 565 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/HNLs/repair/round0/model.fr")
                                                              ^
From kernel 7 (Local):
Syntax::sntx: Invalid syntax in or before "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r].". (line 565 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/HNLs/repair/round0/model.fr")
                                                              ^
From kernel 8 (Local):
Syntax::sntx: Invalid syntax in or before "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r].". (line 565 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/HNLs/repair/round0/model.fr")
                                                              ^
From kernel 1 (Local):
Syntax::sntx: Invalid syntax in or before "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r].". (line 565 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/HNLs/repair/round0/model.fr")
                                                              ^

General::stop: Further output of Syntax::sntx will be suppressed during this calculation.
From kernel 3 (Local):
MergeModels::Particles: Warning: Doubly defined particle classes.
From kernel 4 (Local):
MergeModels::Particles: Warning: Doubly defined particle classes.
From kernel 7 (Local):
MergeModels::Particles: Warning: Doubly defined particle classes.
From kernel 8 (Local):
MergeModels::Particles: Warning: Doubly defined particle classes.
From kernel 1 (Local):
MergeModels::Particles: Warning: Doubly defined particle classes.

General::stop: Further output of Warning: Doubly defined particle classes. will be suppressed during this calculation.
From kernel 3 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 3 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 4 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 5 (Local):
LoadModel::Part: Warning : All particles should have different names.
From kernel 6 (Local):
LoadModel::Part: Warning : All particles should have different names.

General::stop: Further output of Warning : All particles should have different names. will be suppressed during this calculation.
From kernel 3 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 3 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 4 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 5 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 6 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of Warning: Selfconjugated fields should not carry quantumnumbers. will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 7 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
Merging model-files...

Syntax::sntx: Invalid syntax in or before "For a Majorana HNL, replace the Dirac sterile definitions by NR[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjP[sp1,sp2] vl[sp2,ff2]] and NRc[sp1_,ff_] :> Module[{sp2,ff2}, HEAV[ff,ff2] ProjM[sp1,sp2] vl[sp2,ff2]], with numass[3,3] :> 0.5*MN4*Abs[1-1/r] and numass[4,4] :> 0.5*MN4*Abs[1+1/r].". (line 565 of "/Users/kenwu/Documents/Github/heptapod/eval/benchmark_runs/HNLs/repair/round0/model.fr")
                                                              ^

MergeModels::Particles: Warning: Doubly defined particle classes.
This model implementation was created by
P. Coloma
E. Fernandez-Martinez
M. Gonzalez-Lopez
J. Hernandez-Garcia
Model Version: 1.0.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::Part: Warning : All particles should have different names.

LoadModel::Part: Warning : All particles should have different names.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model HNLs_gen loaded.
[INFO] Total Lagrangian: LSM + LHadrSemileptonic
Error: BSM Lagrangian symbol 'LHadrSemileptonic' is undefined in the model.


```
