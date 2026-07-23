# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED
- Hermiticity check: not reached
- Kinetic-terms check: not reached
- Mass-spectrum check: not reached
- MadGraph import: not reached
- Heuristic error tags: mixing_declaration_error, wolfram_aborted

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
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 4 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 6 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 1 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 2 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

General::stop: Further output of In FeynRules mode, all class members should be given a mass name. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 3 (Local):
MassDiag::OneMassOneGaugeBases: One mixing declaration wrongly containing one single mass and one single gauge basis.
From kernel 6 (Local):
MassDiag::OneMassOneGaugeBases: One mixing declaration wrongly containing one single mass and one single gauge basis.
From kernel 7 (Local):
MassDiag::OneMassOneGaugeBases: One mixing declaration wrongly containing one single mass and one single gauge basis.
From kernel 8 (Local):
MassDiag::OneMassOneGaugeBases: One mixing declaration wrongly containing one single mass and one single gauge basis.
From kernel 1 (Local):
MassDiag::OneMassOneGaugeBases: One mixing declaration wrongly containing one single mass and one single gauge basis.

General::stop: Further output of One mixing declaration wrongly containing one single mass and one single gauge basis. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Codex extraction from Cao and Zhang, arXiv:1611.09337
Model Version: 1.0.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.
$Aborted
Model 331_gen loaded.

MassDiag::OneMassOneGaugeBases: One mixing declaration wrongly containing one single mass and one single gauge basis.


```
