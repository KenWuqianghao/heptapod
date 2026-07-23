# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: True
- Heuristic error tags: duplicate_particle_names, selfconjugate_quantum_numbers, hermiticity_fail

## FeynRules / Wolfram Engine output (tail)
```
tumnumbers.

General::stop: Further output of LoadModel::QN will be suppressed during this calculation.

LoadModel::Part: Warning : All particles should have different names.

General::stop: Further output of LoadModel::Part will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model MDMmodel_gen loaded.
[INFO] Total Lagrangian: LSM + LMDMNP
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
21 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 21.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {tpbar, b, GP}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {tpbar, d, GP}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Y not conserved in vertex {tpbar, s, GP}.
Quantum number Y not conserved in vertex {tpbar, t, G0}.
Quantum number Y not conserved in vertex {tpbar, t, h}.
Quantum number Y not conserved in vertex {tpbar, t, sDM}.
Quantum number Y not conserved in vertex {bbar, tp, GPbar}.
Quantum number Y not conserved in vertex {dbar, tp, GPbar}.
Quantum number Y not conserved in vertex {sbar, tp, GPbar}.
Quantum number Y not conserved in vertex {tbar, tp, G0}.
Quantum number Y not conserved in vertex {tbar, tp, h}.
Quantum number Y not conserved in vertex {tbar, tp, sDM}.
21 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{tbar, 1}, {b, 2}, {GP, 3}}, -(sr*yp*CKM[Index[Generation, 3], Index[Generation, 3]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{tbar, 1}, {d, 2}, {GP, 3}}, -(sr*yp*CKM[Index[Generation, 3], Index[Generation, 1]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{tbar, 1}, {s, 2}, {GP, 3}}, -(sr*yp*CKM[Index[Generation, 3], Index[Generation, 2]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{tbar, 1}, {t, 2}, {G0, 3}}, -((sr*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*IndexDelta[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2])}
{{{tbar, 1}, {t, 2}, {h, 3}}, (-I*cs*sr*yp*Ga[5, Index[Spin, Ext[1]], Index[Spin, Ext[2]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]])/Sqrt[2]}
{{{tbar, 1}, {t, 2}, {sDM, 3}}, (I*sr*ss*yp*Ga[5, Index[Spin, Ext[1]], Index[Spin, Ext[2]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]])/Sqrt[2]}
{{{tpbar, 1}, {b, 2}, {GP, 3}}, cr*yp*CKM[Index[Generation, 3], Index[Generation, 3]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tpbar, 1}, {d, 2}, {GP, 3}}, cr*yp*CKM[Index[Generation, 3], Index[Generation, 1]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tpbar, 1}, {s, 2}, {GP, 3}}, cr*yp*CKM[Index[Generation, 3], Index[Generation, 2]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tpbar, 1}, {t, 2}, {G0, 3}}, (cr*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2]}
{{{tpbar, 1}, {t, 2}, {h, 3}}, (-I*cr*cs*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2]}
{{{tpbar, 1}, {t, 2}, {sDM, 3}}, (I*cr*ss*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2]}
{{{bbar, 1}, {t, 2}, {GPbar, 3}}, -(sr*yp*Conjugate[CKM[Index[Generation, 3], Index[Generation, 3]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{bbar, 1}, {tp, 2}, {GPbar, 3}}, cr*yp*Conjugate[CKM[Index[Generation, 3], Index[Generation, 3]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{dbar, 1}, {t, 2}, {GPbar, 3}}, -(sr*yp*Conjugate[CKM[Index[Generation, 3], Index[Generation, 1]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{dbar, 1}, {tp, 2}, {GPbar, 3}}, cr*yp*Conjugate[CKM[Index[Generation, 3], Index[Generation, 1]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{sbar, 1}, {t, 2}, {GPbar, 3}}, -(sr*yp*Conjugate[CKM[Index[Generation, 3], Index[Generation, 2]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])}
{{{sbar, 1}, {tp, 2}, {GPbar, 3}}, cr*yp*Conjugate[CKM[Index[Generation, 3], Index[Generation, 2]]]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]]}
{{{tbar, 1}, {tp, 2}, {G0, 3}}, (cr*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2]}
{{{tbar, 1}, {tp, 2}, {h, 3}}, (I*cr*cs*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2]}
{{{tbar, 1}, {tp, 2}, {sDM, 3}}, (-I*cr*ss*yp*IndexDelta[Index[Colour, Ext[1]], Index[Colour, Ext[2]]]*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/Sqrt[2]}
HEPTAPOD-CHECK-ERROR
HEPTAPOD-CHECK-END: hermiticity
HEPTAPOD-CHECK-BEGIN: kinetic_terms
Neglecting all terms with more than 2 particles.
Non diagonal kinetic term found: -3*cs*ss*del[h, Index[Lorentz, mu]]*del[sDM, Index[Lorentz, mu]]
Non diagonal kinetic term found: -I*cl*sl*tbar[Index[Spin, r$3147], Index[Colour, i1$3476]] . del[tp[Index[Spin, sp2$3511], Index[Colour, i1$3476]], Index[Lorentz, mu]]*TensDot[Ga[Index[Lorentz, mu]], ProjM][Index[Spin, r$3147], Index[Spin, sp2$3511]] - I*cr*sr*tbar[Index[Spin, r$3142], Index[Colour, i1$3486]] . del[tp[Index[Spin, sp2$3521], Index[Colour, i1$3486]], Index[Lorentz, mu]]*TensDot[Ga[Index[Lorentz, mu]], ProjP][Index[Spin, r$3142], Index[Spin, sp2$3521]]
Non diagonal kinetic term found: -I*cl*sl*tpbar[Index[Spin, r$3148], Index[Colour, i1$3476]] . del[t[Index[Spin, sp2$3511], Index[Colour, i1$3476]], Index[Lorentz, mu]]*TensDot[Ga[Index[Lorentz, mu]], ProjM][Index[Spin, r$3148], Index[Spin, sp2$3511]] - I*cr*sr*tpbar[Index[Spin, r$3143], Index[Colour, i1$3486]] . del[t[Index[Spin, sp2$3521], Index[Colour, i1$3486]], Index[Lorentz, mu]]*TensDot[Ga[Index[Lorentz, mu]], ProjP][Index[Spin, r$3143], Index[Spin, sp2$3521]]
HEPTAPOD-CHECK-END: kinetic_terms
HEPTAPOD-CHECK-BEGIN: mass_spectrum
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -(cs*h*muH^2*sDM*ss) + cs*h*muH2*sDM*ss - cs*h*muS2*sDM*ss - (cs*dkappa*h*sDM*ss*vev^2)/2 + (3*cs*dlamh*h*sDM*ss*vev^2)/4 + 3*cs*h*lam*sDM*ss*vev^2 - cs^2*dkappa*h*sDM*vev*vevf + dkappa*h*sDM*ss^2*vev*vevf + (cs*dkappa*h*sDM*ss*vevf^2)/2 - (cs*dlams*h*sDM*ss*vevf^2)/2
Non diagonal mass term found: cl*Mdltn*sr*tbar[Index[Spin, r$3142], Index[Colour, cc]] . tp[Index[Spin, sp2$3466], Index[Colour, cc]]*ProjM[Index[Spin, r$3142], Index[Spin, sp2$3466]] + cr*Mdltn*sl*tbar[Index[Spin, r$3147], Index[Colour, cc]] . tp[Index[Spin, sp2$3464], Index[Colour, cc]]*ProjP[Index[Spin, r$3147], Index[Spin, sp2$3464]]
Non diagonal mass term found: cr*Mdltn*sl*tpbar[Index[Spin, r$3143], Index[Colour, cc]] . t[Index[Spin, sp2$3466], Index[Colour, cc]]*ProjM[Index[Spin, r$3143], Index[Spin, sp2$3466]] - (cr*vev*yp*tpbar[Index[Spin, r$3143], Index[Colour, cc]] . t[Index[Spin, sp2$3547], Index[Colour, cc]]*ProjM[Index[Spin, r$3143], Index[Spin, sp2$3547]])/Sqrt[2] + cl*Mdltn*sr*tpbar[Index[Spin, r$3148], Index[Colour, cc]] . t[Index[Spin, sp2$3464], Index[Colour, cc]]*ProjP[Index[Spin, r$3148], Index[Spin, sp2$3464]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (-I*G0*sr*yp*QLb[sp, 1, 3, cc] . t[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (cs*h*sr*yp*QLb[sp, 1, 3, cc] . t[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((sDM*sr*ss*yp*QLb[sp, 1, 3, cc] . t[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]])/Sqrt[2])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (I*cr*G0*yp*QLb[sp, 1, 3, cc] . tp[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -((cr*cs*h*yp*QLb[sp, 1, 3, cc] . tp[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]])/Sqrt[2])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (cr*sDM*ss*yp*QLb[sp, 1, 3, cc] . tp[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: -I*GPbar*sr*yp*QLb[sp, 2, 3, cc] . t[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: I*cr*GPbar*yp*QLb[sp, 2, 3, cc] . tp[Index[Spin, sp2$3542], Index[Colour, cc]]*ProjP[Index[Spin, sp], Index[Spin, sp2$3542]]
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench/MDMmodel/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
154 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 154.
149 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 149
   - Saved vertices in InterfaceRun[ 1 ].
Quantum number Y not conserved in vertex {sDM, tbar, tp}.
Quantum number Y not conserved in vertex {h, tbar, tp}.
Quantum number Y not conserved in vertex {sDM, tpbar, t}.
Quantum number Y not conserved in vertex {h, tpbar, t}.
Quantum number Y not conserved in vertex {GP, tpbar, d}.
Quantum number Y not conserved in vertex {GP, tpbar, s}.
Quantum number Y not conserved in vertex {GP, tpbar, b}.
Quantum number Y not conserved in vertex {G0, tpbar, t}.
Quantum number Y not conserved in vertex {A, tbar, tp}.
Quantum number Y not conserved in vertex {G, tbar, tp}.
Quantum number Y not conserved in vertex {Z, tbar, tp}.
Quantum number Y not conserved in vertex {A, tpbar, t}.
Quantum number Y not conserved in vertex {G, tpbar, t}.
Quantum number Y not conserved in vertex {Z, tpbar, t}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/220 .
    - Writing files.
Done!
[INFO] Done.


```
