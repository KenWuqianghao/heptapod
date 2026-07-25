# Reverse-check review package — `VLC_LN_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `VLC_LN/repair2/final.fr` |
| original model name | `VLC_LN_gen` (hidden from the agent) |
| paper | VLC_LN/text/1508.01112.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `PiMat` (`=`)

```mathematica
{{pi0/Sqrt[2] + eta/Sqrt[6] + etaP/Sqrt[3], pip, Kp}, {pipbar, -pi0/Sqrt[2] + eta/Sqrt[6] + etaP/Sqrt[3], K0}, {Kpbar, K0bar, -2 eta/Sqrt[6] + etaP/Sqrt[3]}}
```

### `Umat` (`:=`)

```mathematica
MatrixExp[I Sqrt[2] PiMat/fpi]
```

### `Mmat` (`=`)

```mathematica
{{mL, 0, y PhiSM[1]}, {0, mL, y PhiSM[2]}, {Conjugate[ytil] PhiSMBar[1], Conjugate[ytil] PhiSMBar[2], mN}}
```

### `LUVVLC` (`:=`)

```mathematica
Block[{mu,sp,aa,kin,yuk},
  kin = I L0bar[sp,aa].Ga[mu].DC[L0[sp,aa],mu] +
        I Lmbar[sp,aa].Ga[mu].DC[Lm[sp,aa],mu] +
        I Nvlcbar[sp,aa].Ga[mu].DC[Nvlc[sp,aa],mu];
  yuk = y PhiSM[1] L0bar[sp,aa].ProjM.Nvlc[sp,aa] +
        y PhiSM[2] Lmbar[sp,aa].ProjM.Nvlc[sp,aa] +
        ytil PhiSMBar[1] L0bar[sp,aa].ProjP.Nvlc[sp,aa] +
        ytil PhiSMBar[2] Lmbar[sp,aa].ProjP.Nvlc[sp,aa];
  1/2 (kin + HC[kin]) -
  mL (L0bar[sp,aa].L0[sp,aa] + Lmbar[sp,aa].Lm[sp,aa]) -
  mN Nvlcbar[sp,aa].Nvlc[sp,aa] +
  yuk + HC[yuk]
]
```

### `LChiralFull` (`:=`)

```mathematica
Block[{mu,i}, fpi^2/4 Tr[DC[Umat,mu].DC[HC[Umat],mu]] + (grho fpi^3 Tr[Mmat.Umat] + HC[grho fpi^3 Tr[Mmat.Umat]]) + fpi^2/16 (mEtaP^2/3) (Log[Det[Umat]] - Log[Det[HC[Umat]]])^2 + 3 gw^2 grho^2 fpi^4/(2 (4 Pi)^2) Sum[Tr[Umat.Ta[i].HC[Umat].Ta[i]], {i,1,3}]]
```

### `LKinCompositeScalars` (`:=`)

```mathematica
Block[{mu}, 1/2 del[pi0,mu] del[pi0,mu] + del[pipbar,mu] del[pip,mu] + 1/2 del[eta,mu] del[eta,mu] + 1/2 del[etaP,mu] del[etaP,mu] - mEtaP^2/2 etaP^2]
```

### `LMExpanded` (`:=`)

```mathematica
-mK2^2 (Kpbar Kp + K0bar K0) - mPi3^2/2 (pi0^2 + 2 pip pipbar) - mEta^2/2 eta^2 + (-I Sqrt[2] grho fpi^2 Bcoup (Kpbar PhiSM[1] + K0bar PhiSM[2]) - grho/Sqrt[2] Acoup fpi (Sum[(Kpbar PauliSigma[a,1,jj] + K0bar PauliSigma[a,2,jj]) PhiSM[jj] PiTriplet[a], {a,1,3}, {jj,1,2}] - eta (Kpbar PhiSM[1] + K0bar PhiSM[2])/Sqrt[3]) + HC[-I Sqrt[2] grho fpi^2 Bcoup (Kpbar PhiSM[1] + K0bar PhiSM[2]) - grho/Sqrt[2] Acoup fpi (Sum[(Kpbar PauliSigma[a,1,jj] + K0bar PauliSigma[a,2,jj]) PhiSM[jj] PiTriplet[a], {a,1,3}, {jj,1,2}] - eta (Kpbar PhiSM[1] + K0bar PhiSM[2])/Sqrt[3])])
```

### `LKinTriplet` (`:=`)

```mathematica
(I del[pipbar, mu] gw pi0 WiPhys[mu, 1])/(2 Sqrt[2]) - (I del[pip, mu] gw pi0 WiPhys[mu, 1])/(2 Sqrt[2]) - (I del[pi0, mu] gw pipbar WiPhys[mu, 1])/(2 Sqrt[2]) + (I del[pi0, mu] gw pip WiPhys[mu, 1])/(2 Sqrt[2]) + (del[pipbar, mu] gw pi0 WiPhys[mu, 2])/(2 Sqrt[2]) + (del[pip, mu] gw pi0 WiPhys[mu, 2])/(2 Sqrt[2]) - (del[pi0, mu] gw pipbar WiPhys[mu, 2])/(2 Sqrt[2]) - (del[pi0, mu] gw pip WiPhys[mu, 2])/(2 Sqrt[2]) + 1/2 I del[pip, mu] gw pipbar WiPhys[mu, 3] - 1/2 I del[pipbar, mu] gw pip WiPhys[mu, 3]
```

### `LKinK2` (`:=`)

```mathematica
Block[{mu}, DK2Bar[1, mu] DK2[1, mu] + DK2Bar[2, mu] DK2[2, mu]]
```

### `LAnomalyTriplet` (`:=`)

```mathematica
Block[{mu,nu,rho,sig}, NHC g1 gw/(32 Pi^2 fpi) Eps[mu,nu,rho,sig] BFS[rho,sig] (PiTriplet[1] SU2FS[mu,nu,1] + PiTriplet[2] SU2FS[mu,nu,2] + PiTriplet[3] SU2FS[mu,nu,3])]
```

### `LAnomalyEta` (`:=`)

```mathematica
Block[{mu,nu,rho,sig}, -NHC eta/(32 Sqrt[3] Pi^2 fpi) Eps[mu,nu,rho,sig] (gw^2 (SU2FS[mu,nu,1] SU2FS[rho,sig,1] + SU2FS[mu,nu,2] SU2FS[rho,sig,2] + SU2FS[mu,nu,3] SU2FS[rho,sig,3]) + g1^2 BFS[mu,nu] BFS[rho,sig])]
```

### `LEDM` (`:=`)

```mathematica
Block[{mu,nu,rho,sig,a}, -mPi3^2/2 Sum[PiTriplet[a]^2,{a,1,3}] - mEta^2/2 eta^2 + 4 Im[y ytil] grho^2 fpi^3/mK2^2 (Sum[PhiSMBar[i] PauliSigma[a,i,j] PhiSM[j] PiTriplet[a],{a,1,3},{i,1,2},{j,1,2}] - eta Sum[PhiSMBar[i] PhiSM[i],{i,1,2}]/Sqrt[3]) + NHC g1 gw/(32 Pi^2 fpi) Eps[mu,nu,rho,sig] BFS[rho,sig] (PiTriplet[1] SU2FS[mu,nu,1] + PiTriplet[2] SU2FS[mu,nu,2] + PiTriplet[3] SU2FS[mu,nu,3]) - NHC eta/(32 Sqrt[3] Pi^2 fpi) Eps[mu,nu,rho,sig] (gw^2 (SU2FS[mu,nu,1] SU2FS[rho,sig,1] + SU2FS[mu,nu,2] SU2FS[rho,sig,2] + SU2FS[mu,nu,3] SU2FS[rho,sig,3]) + g1^2 BFS[mu,nu] BFS[rho,sig])]
```

### `LRhoff` (`:=`)

```mathematica
1/Sqrt[2] gV (rhop[mu] (vlbar.Ga[mu].ProjM.l + ubar.Ga[mu].ProjM.d + cbar.Ga[mu].ProjM.s + tbar.Ga[mu].ProjM.b) + rhopbar[mu] (lbar.Ga[mu].ProjM.vl + dbar.Ga[mu].ProjM.u + sbar.Ga[mu].ProjM.c + bbar.Ga[mu].ProjM.t)) + 1/2 gV rho0[mu] (vlbar.Ga[mu].ProjM.vl + ubar.Ga[mu].ProjM.u + cbar.Ga[mu].ProjM.c + tbar.Ga[mu].ProjM.t - lbar.Ga[mu].ProjM.l - dbar.Ga[mu].ProjM.d - sbar.Ga[mu].ProjM.s - bbar.Ga[mu].ProjM.b)
```

### `LRhoTriplet` (`:=`)

```mathematica
grho 1/2 I del[pip, mu] pipbar rho0[mu] - grho 1/2 I del[pipbar, mu] pip rho0[mu] - grho 1/2 I del[pip, mu] pi0 rhopbar[mu] + grho 1/2 I del[pi0, mu] pip rhopbar[mu] + grho 1/2 I del[pipbar, mu] pi0 rhop[mu] - grho 1/2 I del[pi0, mu] pipbar rhop[mu]
```

### `LTot` (`:=`)

```mathematica
LUVVLC + LKinCompositeScalars + LMExpanded + LKinTriplet + LKinK2 + LAnomalyTriplet + LAnomalyEta + LRhoff + LRhoTriplet
```

## Blank-slate reconstruction

*(reconstruction phase failed — see agent_runs in the tool result)*

## Paper cross-check

*(not run — provide `paper_tex_path` to enable the term-by-term comparison)*

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 24 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

