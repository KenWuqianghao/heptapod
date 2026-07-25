# Reverse-check review package — `B-L-SM_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `B-L-SM/repair2/final.fr` |
| original model name | `B-L-SM_gen` (hidden from the agent) |
| paper | B-L-SM/text/1811.11452.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LZpKin` (`:=`)

```mathematica
Block[{mu,nu}, -1/4 FS[Zp,mu,nu] FS[Zp,mu,nu]]
```

### `LChi` (`:=`)

```mathematica
Block[{mu,ii}, ExpandIndices[(del[HC[Chi],mu] - I*2*g1p*Zp[mu]*HC[Chi])*(del[Chi,mu] + I*2*g1p*Zp[mu]*Chi) - muChi2*HC[Chi]*Chi - lambda2BL*(HC[Chi]*Chi)^2 - lambda3BL*(Phibar[ii]*Phi[ii])*(HC[Chi]*Chi), FlavorExpand -> SU2D]]
```

### `LBLCurrent` (`:=`)

```mathematica
Block[{mu}, ExpandIndices[-g1p*Zp[mu]*(1/3 QLbar.Ga[mu].QL + 1/3 uRbar.Ga[mu].uR + 1/3 dRbar.Ga[mu].dR - LLbar.Ga[mu].LL - lRbar.Ga[mu].lR - nuRbar.Ga[mu].nuR), FlavorExpand -> {SU2D, Generation, Colour}]]
```

### `YMRRules` (`=`)

```mathematica
{YMRMat[1,1] -> YMR1x1, YMRMat[1,2] -> YMR1x2, YMRMat[1,3] -> YMR1x3, YMRMat[2,1] -> YMR2x1, YMRMat[2,2] -> YMR2x2, YMRMat[2,3] -> YMR2x3, YMRMat[3,1] -> YMR3x1, YMRMat[3,2] -> YMR3x2, YMRMat[3,3] -> YMR3x3}
```

### `YNURules` (`=`)

```mathematica
{YNUMat[1,1] -> YNU1x1, YNUMat[1,2] -> YNU1x2, YNUMat[1,3] -> YNU1x3, YNUMat[2,1] -> YNU2x1, YNUMat[2,2] -> YNU2x2, YNUMat[2,3] -> YNU2x3, YNUMat[3,1] -> YNU3x1, YNUMat[3,2] -> YNU3x2, YNUMat[3,3] -> YNU3x3}
```

### `LNuYukNonHC` (`:=`)

```mathematica
Block[{sp,ff1,ff2}, ExpandIndices[-YNUMat[ff1,ff2] (LLbar[sp,1,ff1].nuR[sp,ff2] (Phibar[2] - vev/Sqrt[2]) - LLbar[sp,2,ff1].nuR[sp,ff2] Phibar[1]) - 1/2 YMRMat[ff1,ff2] anti[CC[nuR]][sp,ff1].nuR[sp,ff2] Chi, FlavorExpand -> Generation] /. YNURules /. YMRRules]
```

### `LNuYuk` (`:=`)

```mathematica
LNuYukNonHC + HC[LNuYukNonHC]
```

### `LScalarDiag` (`:=`)

```mathematica
Block[{mu}, ca*sa*del[H,mu]*del[H2,mu] - ca*sa*muChi2*H*H2 - ca*sa*lambda3BL*vev^2*H*H2/2 + ca*lambda3BL*vev*xBL*H*H2 - 3*ca*sa*lambda2BL*xBL^2*H*H2]
```

### `LTot` (`:=`)

```mathematica
LZpKin + LChi + LBLCurrent + LNuYuk + LScalarDiag
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
6. Sanitizer scope: 32 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

