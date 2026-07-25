# Reverse-check review package — `331_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `331/repair2/final.fr` |
| original model name | `331_gen` (hidden from the agent) |
| paper | 331/text/1611.09337.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `VHiggs331` (`=`)

```mathematica
mu1sq HC[rho].rho + mu2sq HC[eta].eta + mu3sq HC[chi].chi + lam1 (HC[rho].rho)^2 + lam2 (HC[eta].eta)^2 + lam3 (HC[chi].chi)^2 + lam12 (HC[rho].rho) (HC[eta].eta) + lam13 (HC[rho].rho) (HC[chi].chi) + lam23 (HC[eta].eta) (HC[chi].chi) + lamp12 (HC[rho].eta) (HC[eta].rho) + lamp13 (HC[rho].chi) (HC[chi].rho) + lamp23 (HC[eta].chi) (HC[chi].eta) + Sqrt[2] f331 (Eps[i,j,k] rho[i] eta[j] chi[k] + HC[Eps[i,j,k] rho[i] eta[j] chi[k]])
```

### `LHiggs331` (`=`)

```mathematica
HC[DC[rho, mu]].DC[rho, mu] + HC[DC[eta, mu]].DC[eta, mu] + HC[DC[chi, mu]].DC[chi, mu] - VHiggs331
```

### `LGauge331Mass` (`=`)

```mathematica
1/4 gw^2 vev^2 W[mu] HC[W[mu]] + 1/4 gw^2 (v3^2 + v2^2) Yp[mu] HC[Yp[mu]] + 1/4 gw^2 (v3^2 + v1^2) Vp[mu] HC[Vp[mu]] + 1/2 MZp^2 Zp[mu] Zp[mu]
```

### `LGaugeSelf331` (`=`)

```mathematica
(-I ee) A[mu] W[nu] HC[W[sig]] VVV[mu,nu,sig] + (I am ee/2) A[mu] Vp[nu] HC[Vp[sig]] VVV[mu,nu,sig] + (I ap ee/2) A[mu] Yp[nu] HC[Yp[sig]] VVV[mu,nu,sig] - I Sqrt[3] ee a0/(2 cw sw) Zp[mu] (Vp[nu] HC[Vp[sig]] + Yp[nu] HC[Yp[sig]]) VVV[mu,nu,sig]
```

### `LScalarFermion331` (`=`)

```mathematica
H0 (O331[3,1] ME[ll]/v3 HC[EL[ll]].EL[ll] + O331[2,1] Ml[ll]/v2 HC[LL[ll]].LL[ll]) - I H2 (U331[3,2] ME[ll]/v3 HC[EL[ll]].EL[ll]) - I H3 (U331[3,3] ME[ll]/v3 HC[EL[ll]].EL[ll]) - I H2 (U331[1,2] Md[q]/v1 HC[d[q]].d[q] + U331[2,2] Mu[q]/v2 HC[u[q]].u[q]) - I H3 (U331[1,3] Md[q]/v1 HC[d[q]].d[q] + U331[2,3] Mu[q]/v2 HC[u[q]].u[q])
```

### `LTot` (`:=`)

```mathematica
LGaugeSelf331
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
6. Sanitizer scope: 54 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

