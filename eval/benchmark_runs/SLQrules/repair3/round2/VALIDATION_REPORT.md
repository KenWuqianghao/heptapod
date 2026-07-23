# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: True
- Heuristic error tags: hermiticity_fail

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
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p53hatbar, R2tm13hat, S1tbar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2tp23hat, S1tbar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, S1, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, S1, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2p53hat, R2tm13hatbar, S1t, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2p23hat, R2tp23hatbar, S1t, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, S1, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, S1, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar}.
20 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{R2p23hat, 1}}, -I*(Conjugate[Y2RL[Index[Generation, 1], Index[Generation, 2]]]*LLbar[Index[Spin, q], Index[SU2D, 1]] . ProjL . u[Index[Spin, r]]*Ga[0, 1, r$3457]*Ga[0, r$3456, 2]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, 1]] + Conjugate[Y2RL[Index[Generation, 3], Index[Generation, 2]]]*LLbar[Index[Spin, s], Index[SU2D, 1]] . ProjL . u[Index[Spin, t]]*Ga[0, 3, r$3457]*Ga[0, r$3456, 2]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, 1]] + Conjugate[Y2RL[Index[Generation, 1], Index[Generation, 3]]]*LLbar[Index[Spin, u], Index[SU2D, 1]] . ProjL . u[Index[Spin, v]]*Ga[0, 1, r$3457]*Ga[0, r$3456, 3]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, 1]] + Conjugate[Y2RL[Index[Generati
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
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[1, 2, aa$3449]]*Ga[0, r$3455, 1]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[2, 2, aa$3449]]*Ga[0, r$3455, 1]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[3, 2, aa$3449]]*Ga[0, r$3455, 1]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[1, 2, aa$3449]]*Ga[0, r$3455, 2]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[2, 2, aa$3449]]*Ga[0, r$3455, 2]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[3, 2, aa$3449]]*Ga[0, r$3455, 2]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[1, 2, aa$3449]]*Ga[0, r$3455, 3]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[2, 2, aa$3449]]*Ga[0, r$3455, 3]*R2p23hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[3, 2, aa$3449]]*Ga[0, r$3455, 3]*R2p23hatbar[Index[Colour, aa$3449]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[1, 1, aa$3449]]*Ga[0, r$3455, 1]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[2, 1, aa$3449]]*Ga[0, r$3455, 1]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[3, 1, aa$3449]]*Ga[0, r$3455, 1]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[1, 1, aa$3449]]*Ga[0, r$3455, 2]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[2, 1, aa$3449]]*Ga[0, r$3455, 2]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[3, 1, aa$3449]]*Ga[0, r$3455, 2]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[1, 1, aa$3449]]*Ga[0, r$3455, 3]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[2, 1, aa$3449]]*Ga[0, r$3455, 3]*R2p53hatbar[Index[Colour, aa$3449]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3455]] . ProjR . HC[Qbar[3, 1, aa$3449]]*Ga[0, r$3455, 3]*R2p53hatbar[Index[Colour, aa$3449]]
Non diagonal mass term found: (vev^2*Y2t2*R2p23hatbar[Index[Colour,
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, R2p53hatbar, S1tbar, S3p23hatbar}.
Quantum number Q not conserved in vertex {S1bar, S3m13hat, S3m43hat, S3p23hatbar}.
Quantum number Q not conserved in vertex {S1, S1, S3p23hatbar, S3p23hatbar}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, W}.
Quantum number Q not conserved in vertex {A, R2p23hat, R2p53hatbar, W}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, W}.
Quantum number Q not conserved in vertex {A, R2tm13hat, R2tp23hatbar, W}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, W}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, W}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, W}.
Quantum number Q not conserved in vertex {A, S3m13hatbar, S3m43hat, W}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, W}.
Quantum number Q not conserved in vertex {A, S3m13hat, S3m43hatbar, W}.
Quantum number Q not conserved in vertex {A, S3m43hatbar, S3p23hat, W}.
Quantum number Q not conserved in vertex {A, S3m43hat, S3p23hatbar, W}.
Quantum number Q not conserved in vertex {G, R2p23hat, R2p53hatbar, W}.
Quantum number Q not conserved in vertex {G, R2tm13hat, R2tp23hatbar, W}.
Quantum number Q not conserved in vertex {G, S3m13hatbar, S3m43hat, W}.
Quantum number Q not conserved in vertex {G, S3m13hat, S3m43hatbar, W}.
Quantum number Q not conserved in vertex {G, S3m43hatbar, S3p23hat, W}.
Quantum number Q not conserved in vertex {G, S3m43hat, S3p23hatbar, W}.
Quantum number Q not conserved in vertex {S3m13hat, S3m13hatbar, W, W}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3p23hat, W, W}.
Quantum number Q not conserved in vertex {S3m13hat, S3p23hatbar, W, W}.
Quantum number Q not conserved in vertex {S3p23hat, S3p23hatbar, W, W}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, Wbar}.
Quantum number Q not conserved in vertex {A, R2p23hatbar, R2p53hat, Wbar}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, Wbar}.
Quantum number Q not conserved in vertex {A, R2tm13hatbar, R2tp23hat, Wbar}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, Wbar}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, Wbar}.
Quantum number Q not conserved in vertex {A, S3m13hatbar, S3m43hat, Wbar}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, Wbar}.
Quantum number Q not conserved in vertex {A, S3m13hat, S3m43hatbar, Wbar}.
Quantum number Q not conserved in vertex {A, S3m43hatbar, S3p23hat, Wbar}.
Quantum number Q not conserved in vertex {A, S3m43hat, S3p23hatbar, Wbar}.
Quantum number Q not conserved in vertex {G, R2p23hatbar, R2p53hat, Wbar}.
Quantum number Q not conserved in vertex {G, R2tm13hatbar, R2tp23hat, Wbar}.
Quantum number Q not conserved in vertex {G, S3m13hatbar, S3m43hat, Wbar}.
Quantum number Q not conserved in vertex {G, S3m13hat, S3m43hatbar, Wbar}.
Quantum number Q not conserved in vertex {G, S3m43hatbar, S3p23hat, Wbar}.
Quantum number Q not conserved in vertex {G, S3m43hat, S3p23hatbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hat, S3m13hatbar, Wbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3p23hat, Wbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hat, S3p23hatbar, Wbar, Wbar}.
Quantum number Q not conserved in vertex {S3p23hat, S3p23hatbar, Wbar, Wbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, W, Z}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, W, Z}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, W, Z}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, W, Z}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, W, Z}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, W, Z}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, Wbar, Z}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, Wbar, Z}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/729 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] Done.

```
