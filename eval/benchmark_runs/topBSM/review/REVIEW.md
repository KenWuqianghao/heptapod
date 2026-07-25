# Reverse-check review package — `topBSM_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `topBSM/model/topBSM_gen.fr` |
| original model name | `topBSM_gen` (hidden from the agent) |
| paper | topBSM/text/1305.7386.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `bjzeros` (`=`)

```mathematica
Table[N[BesselJZero[1, x]], {x, 1, 10}]

M$Parameters = {
  s0scalar == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S0PARAMS,
    InteractionOrder -> {QS0, 1},
    ParameterName -> s0scalar,
    TeX -> "Subscript[s0, scalar]",
    Description -> "S0 scalar coupling"
  },
  s0axial == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S0PARAMS,
    InteractionOrder -> {QS0, 1},
    ParameterName -> s0axial,
    TeX -> "Subscript[s0, axial]",
    Description -> "S0 axial coupling"
  },
  s0fusionScalar == {
    ParameterType -> Internal,
    InteractionOrder -> {QS0, 1},
    Definitions -> {s0fusionScalar :> If[NumericalValue[MS0] > 2 NumericalValue[MT], -s0scalar gs^2/(12 Pi^2 vev) sertHeavy[(2 MT/MS0)^2], -s0scalar gs^2/(12 Pi^2 vev) sertLight[(2 MT/MS0)^2]]},
    TeX -> "Subscript[s0, fusionScalar]",
    Description -> "S0 effective coupling due to gluon fusion, scalar"
  },
  s0fusionAxial == {
    ParameterType -> Internal,
    InteractionOrder -> {QS0, 1},
    Definitions -> {s0fusionAxial :> If[NumericalValue[MS0] > 2 NumericalValue[MT], -s0axial gs^2/(8 Pi^2 vev) serpHeavy[(2 MT/MS0)^2], -s0axial gs^2/(8 Pi^2 vev) serpLight[(2 MT/MS0)^2]]},
    TeX -> "Subscript[s0, fusionAxial]",
    Description -> "S0 effective coupling due to gluon fusion, axial"
  },
  WS0 == {
    ParameterType -> Internal,
    Definitions -> {WS0 :> If[NumericalValue[MS0] > 2 NumericalValue[MT], (3 MT^2 Sqrt[MS0^4 - 4 MS0^2 MT^2] (-4 MT^2 s0scalar^2 + MS0^2 (s0axial^2 + s0scalar^2)))/(8 Pi vev^2 MS0^3) + (MS0^3 Abs[s0fusionScalar]^2)/(8 Pi), (MS0^3 Abs[s0fusionScalar]^2)/(8 Pi)]},
    Description -> "S0 width"
  },
  o0scalar == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> O0PARAMS,
    InteractionOrder -> {QO0, 1},
    ParameterName -> o0scalar,
    TeX -> "Subscript[o0, scalar]",
    Description -> "O0 scalar coupling"
  },
  o0axial == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> O0PARAMS,
    InteractionOrder -> {QO0, 1},
    ParameterName -> o0axial,
    TeX -> "Subscript[o0, axial]",
    Description -> "O0 axial coupling"
  },
  o0fusionScalar == {
    ParameterType -> Internal,
    InteractionOrder -> {QO0, 1},
    Definitions -> {o0fusionScalar :> If[NumericalValue[MO0] > 2 NumericalValue[MT], -o0scalar gs^2/(12 Pi^2 vev) sertHeavy[(2 MT/MO0)^2], -o0scalar gs^2/(12 Pi^2 vev) sertLight[(2 MT/MO0)^2]]},
    TeX -> "Subscript[o0, fusionScalar]",
    Description -> "O0 effective coupling due to gluon fusion, scalar"
  },
  o0fusionAxial == {
    ParameterType -> Internal,
    InteractionOrder -> {QO0, 1},
    Definitions -> {o0fusionAxial :> If[NumericalValue[MO0] > 2 NumericalValue[MT], -o0axial gs^2/(8 Pi^2 vev) serpHeavy[(2 MT/MO0)^2], -o0axial gs^2/(8 Pi^2 vev) serpLight[(2 MT/MO0)^2]]},
    TeX -> "Subscript[o0, fusionAxial]",
    Description -> "O0 effective coupling due to gluon fusion, axial"
  },
  WO0 == {
    ParameterType -> Internal,
    Definitions -> {WO0 :> If[NumericalValue[MO0] > 2 NumericalValue[MT], 1/6 (3 MT^2 Sqrt[MO0^4 - 4 MO0^2 MT^2] (-4 MT^2 o0scalar^2 + MO0^2 (o0axial^2 + o0scalar^2)))/(8 Pi vev^2 MO0^3) + 1/64 (MO0^3 Abs[o0fusionScalar]^2)/(8 Pi), 1/64 (MO0^3 Abs[o0fusionScalar]^2)/(8 Pi)]},
    Description -> "O0 width"
  },
  s1uright == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1uright,
    TeX -> "Subscript[s1, ur]",
    Description -> "S1 right up quark coupling"
  },
  s1uleft == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1uleft,
    TeX -> "Subscript[s1, ul]",
    Description -> "S1 left up quark coupling"
  },
  s1dright == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1dright,
    TeX -> "Subscript[s1, dr]",
    Description -> "S1 right down quark coupling"
  },
  s1dleft == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1dleft,
    TeX -> "Subscript[s1, dl]",
    Description -> "S1 left down quark coupling"
  },
  s1eright == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1eright,
    TeX -> "Subscript[s1, er]",
    Description -> "S1 right electron coupling"
  },
  s1eleft == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1eleft,
    TeX -> "Subscript[s1, el]",
    Description -> "S1 left electron coupling"
  },
  s1nu == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> S1PARAMS,
    InteractionOrder -> {QS1, 1},
    ParameterName -> s1nu,
    TeX -> "Subscript[s1, v]",
    Description -> "S1 neutrino coupling"
  },
  WS1 == {
    ParameterType -> Internal,
    Definitions -> {WS1 -> 1/(288*cw^2*Pi*sw^2*MS1^3)*ee^2*(+9*MS1^4*s1nu^2 +2*MS1^4*(16*s1uright^2*sw^4 + s1uleft^2*(3 - 4*sw^2)^2) +6*MS1^4*(4*s1eright^2*sw^4 + s1eleft^2*(1 - 2*sw^2)^2) +2*MS1^4*(4*s1dright^2*sw^4 + s1dleft^2*(3 - 2*sw^2)^2) +Sqrt[MS1^4 - 4*MS1^2*MT^2]*(+MT^2*(-9*s1uleft^2 +24*s1uleft*(s1uleft - 3*s1uright)*sw^2 -16*(s1uleft^2 - 6*s1uleft*s1uright + s1uright^2)*sw^4) +MS1^2*(16*s1uright^2*sw^4 + s1uleft^2*(3 - 4*sw^2)^2)) +3*Sqrt[MS1^4 - 4*MS1^2*MTA^2]*(-MTA^2*(+s1eleft^2 -4*s1eleft*(s1eleft - 3*s1eright)*sw^2 +4*(s1eleft^2 - 6*s1eleft*s1eright + s1eright^2)*sw^4) +MS1^2*(4*s1eright^2*sw^4 + s1eleft^2*(1 - 2*sw^2)^2)) +Sqrt[-4*MB^2*MS1^2 + MS1^4]*(+MB^2*(-9*s1dleft^2 +12*s1dleft*(s1dleft - 3*s1dright)*sw^2 -4*(s1dleft^2 - 6*s1dleft*s1dright + s1dright^2)*sw^4) +MS1^2*(4*s1dright^2*sw^4 + s1dleft^2*(3 - 2*sw^2)^2)))},
    Description -> "S1 width"
  },
  o1uright == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> O1PARAMS,
    InteractionOrder -> {QO1, 1},
    ParameterName -> o1uright,
    TeX -> "Subscript[o1, ur]",
    Description -> "O1 right up quark coupling"
  },
  o1uleft == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> O1PARAMS,
    InteractionOrder -> {QO1, 1},
    ParameterName -> o1uleft,
    TeX -> "Subscript[o1, ul]",
    Description -> "O1 left up quark coupling"
  },
  o1dright == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> O1PARAMS,
    InteractionOrder -> {QO1, 1},
    ParameterName -> o1dright,
    TeX -> "Subscript[o1, dr]",
    Description -> "O1 right down quark coupling"
  },
  o1dleft == {
    ParameterType -> External,
    Value -> 1,
    BlockName -> O1PARAMS,
    InteractionOrder -> {QO1, 1},
    ParameterName -> o1dleft,
    TeX -> "Subscript[o1, dl]",
    Description -> "O1 left down quark coupling"
  },
  WO1 == {
    ParameterType -> Internal,
    Definitions -> {WO1 -> (gs^2/(48*Pi*MO1^3))*(+2*MO1^4*(o1dleft^2 + o1dright^2) +Sqrt[-4*MB^2*MO1^2 + MO1^4]*(MO1^2*(o1dleft^2 + o1dright^2) -MB^2*(o1dleft^2 - 6*o1dleft*o1dright + o1dright^2)) +2*MO1^4*(o1uleft^2 + o1uright^2) +Sqrt[MO1^4 - 4*MO1^2*MT^2]*(MO1^2*(o1uleft^2 + o1uright^2) -MT^2*(o1uleft^2 - 6*o1uleft*o1uright + o1uright^2)))},
    Description -> "O1 width"
  }
}
```

### `LS0top` (`=`)

```mathematica
s0scalar MT/vev S0 tbar.t + I s0axial MT/vev S0 tbar.Ga[5].t
```

### `LS0ggfusionScalar` (`=`)

```mathematica
-1/4 s0fusionScalar S0 FS[G,mu,nu,aa] FS[G,mu,nu,aa]
```

### `LS0ggfusionAxial` (`=`)

```mathematica
-1/4 s0fusionAxial S0 FS[G,mu,nu,aa] Dual[FS][G,mu,nu,aa]
```

### `LS0ggfusion` (`=`)

```mathematica
LS0ggfusionScalar + LS0ggfusionAxial
```

### `LS0` (`=`)

```mathematica
LS0top + LS0ggfusion
```

### `LO0top` (`=`)

```mathematica
o0scalar MT/vev tbar.T[a].t O0[a] + I o0axial MT/vev tbar.Ga[5].T[a].t O0[a]
```

### `LO0ggfusionScalar` (`=`)

```mathematica
-1/4 o0fusionScalar dSUN[aa,bb,cc] O0[aa] FS[G,mu,nu,bb] FS[G,mu,nu,cc]
```

### `LO0ggfusionAxial` (`=`)

```mathematica
-1/4 o0fusionAxial dSUN[aa,bb,cc] O0[aa] FS[G,mu,nu,bb] Dual[FS][G,mu,nu,cc]
```

### `LO0ggfusion` (`=`)

```mathematica
LO0ggfusionScalar + LO0ggfusionAxial
```

### `LO0` (`=`)

```mathematica
LO0top + LO0ggfusion
```

### `ez` (`=`)

```mathematica
ee/(sw cw)
```

### `ey` (`=`)

```mathematica
ee sw/cw
```

### `LS1ul` (`=`)

```mathematica
- s1uleft S1[mu] QLbar[sp1,1,ff,cc] Ga[mu,sp1,sp2] QL[sp2,1,ff,cc] * ez (-1/2 + sw^2 2/3)
```

### `LS1dl` (`=`)

```mathematica
- s1dleft S1[mu] QLbar[sp1,2,ff,cc] Ga[mu,sp1,sp2] QL[sp2,2,ff,cc] * ez (1/2 - sw^2/3)
```

### `LS1ur` (`=`)

```mathematica
- s1uright S1[mu] uRbar.Ga[mu].uR * ey*2/3
```

### `LS1dr` (`=`)

```mathematica
- s1dright S1[mu] dRbar.Ga[mu].dR * (-ey)/3
```

### `LS1el` (`=`)

```mathematica
- s1eleft S1[mu] LLbar[sp1,2,ff] Ga[mu,sp1,sp2] LL[sp2,2,ff] * ez (1/2 - sw^2)
```

### `LS1nu` (`=`)

```mathematica
- s1nu S1[mu] LLbar[sp1,1,ff] Ga[mu,sp1,sp2] LL[sp2,1,ff] * (-ez)/2
```

### `LS1er` (`=`)

```mathematica
- s1eright S1[mu] lRbar.Ga[mu].lR * (-ey)
```

### `LS1` (`=`)

```mathematica
LS1ul + LS1dl + LS1ur + LS1dr + LS1el + LS1er + LS1nu
```

### `LO1ul` (`=`)

```mathematica
o1uleft gs O1[mu, a] QLbar[sp1,1,ff,cc1] Ga[mu,sp1,sp2] T[a,cc1,cc2] QL[sp2,1,ff,cc2]
```

### `LO1dl` (`=`)

```mathematica
o1dleft gs O1[mu, a] QLbar[sp1,2,ff,cc1] Ga[mu,sp1,sp2] T[a,cc1,cc2] QL[sp2,2,ff,cc2]
```

### `LO1ur` (`=`)

```mathematica
o1uright gs O1[mu, a] uRbar.Ga[mu].T[a].uR
```

### `LO1dr` (`=`)

```mathematica
o1dright gs O1[mu, a] dRbar.Ga[mu].T[a].dR
```

### `LO1` (`=`)

```mathematica
LO1ul + LO1dl + LO1ur + LO1dr
```

## Blank-slate reconstruction

# Reconstructed Physics from `sanitized.fr`

## Lagrangian

Conventions: \(G^a_{\mu\nu}\equiv\mathrm{FS}[G,\mu,\nu,a]\), \(\widetilde G^{a\mu\nu}=\frac12\epsilon^{\mu\nu\rho\sigma}G^a_{\rho\sigma}\), \(T^a\) are fundamental \(SU(3)_c\) generators, and \(d^{abc}\equiv\mathrm{dSUN}[a,b,c]\). Flavor indices are summed where present. The file defines
\[
g_Z \equiv \frac{e}{s_W c_W},\qquad e\,t_W \equiv \frac{e s_W}{c_W}.
\]

No `DC[...]` covariant derivatives appear explicitly in the interaction Lagrangian. From the declared gauge quantum numbers, \(S0,S1,S2\) are color and electroweak singlets with \(D_\mu=\partial_\mu\). \(O0^a,O1_\mu^a\) are color adjoints with \(Y=Q=0\), so if their kinetic terms are supplied elsewhere the QCD covariant derivative is
\[
(D_\mu X)^a=\partial_\mu X^a+g_s f^{abc}G^b_\mu X^c,
\]
with no \(SU(2)_L\) or \(U(1)_Y\) gauge piece.

### `LS0top`

\[
\mathcal L_{\mathrm{S0top}}
=
s0scalar\,\frac{m_t}{v}\,S0\,\bar t t
+
i\,s0axial\,\frac{m_t}{v}\,S0\,\bar t\gamma^5 t .
\]

### `LS0ggfusionScalar`

\[
\mathcal L_{\mathrm{S0ggfusionScalar}}
=
-\frac14\,s0fusionScalar\,S0\,G^a_{\mu\nu}G^{a\mu\nu}.
\]

### `LS0ggfusionAxial`

\[
\mathcal L_{\mathrm{S0ggfusionAxial}}
=
-\frac14\,s0fusionAxial\,S0\,G^a_{\mu\nu}\widetilde G^{a\mu\nu}.
\]

### `LS0ggfusion`

\[
\mathcal L_{\mathrm{S0ggfusion}}
=
\mathcal L_{\mathrm{S0ggfusionScalar}}
+
\mathcal L_{\mathrm{S0ggfusionAxial}} .
\]

### `LS0`

\[
\mathcal L_{\mathrm{S0}}
=
\mathcal L_{\mathrm{S0top}}
+
\mathcal L_{\mathrm{S0ggfusion}} .
\]

### `LO0top`

\[
\mathcal L_{\mathrm{O0top}}
=
o0scalar\,\frac{m_t}{v}\,O0^a\,\bar t\,T^a t
+
i\,o0axial\,\frac{m_t}{v}\,O0^a\,\bar t\,\gamma^5 T^a t .
\]

### `LO0ggfusionScalar`

\[
\mathcal L_{\mathrm{O0ggfusionScalar}}
=
-\frac14\,o0fusionScalar\,d^{abc}\,O0^a\,G^b_{\mu\nu}G^{c\mu\nu}.
\]

### `LO0ggfusionAxial`

\[
\mathcal L_{\mathrm{O0ggfusionAxial}}
=
-\frac14\,o0fusionAxial\,d^{abc}\,O0^a\,G^b_{\mu\nu}\widetilde G^{c\mu\nu}.
\]

### `LO0ggfusion`

\[
\mathcal L_{\mathrm{O0ggfusion}}
=
\mathcal L_{\mathrm{O0ggfusionScalar}}
+
\mathcal L_{\mathrm{O0ggfusionAxial}} .
\]

### `LO0`

\[
\mathcal L_{\mathrm{O0}}
=
\mathcal L_{\mathrm{O0top}}
+
\mathcal L_{\mathrm{O0ggfusion}} .
\]

### `LS1ul`

\[
\mathcal L_{\mathrm{S1ul}}
=
-\,s1uleft\,g_Z
\left(-\frac12+\frac23 s_W^2\right)
S1_\mu\,
\bar u_{L\,f c}\gamma^\mu u_L^{f c}.
\]

### `LS1dl`

\[
\mathcal L_{\mathrm{S1dl}}
=
-\,s1dleft\,g_Z
\left(\frac12-\frac13 s_W^2\right)
S1_\mu\,
\bar d_{L\,f c}\gamma^\mu d_L^{f c}.
\]

### `LS1ur`

\[
\mathcal L_{\mathrm{S1ur}}
=
-\,s1uright\,
\frac23\,e t_W\,
S1_\mu\,
\bar u_{R\,f c}\gamma^\mu u_R^{f c}.
\]

### `LS1dr`

\[
\mathcal L_{\mathrm{S1dr}}
=
+\,s1dright\,
\frac13\,e t_W\,
S1_\mu\,
\bar d_{R\,f c}\gamma^\mu d_R^{f c}.
\]

### `LS1el`

\[
\mathcal L_{\mathrm{S1el}}
=
-\,s1eleft\,g_Z
\left(\frac12-s_W^2\right)
S1_\mu\,
\bar e_{L\,f}\gamma^\mu e_L^f.
\]

### `LS1nu`

\[
\mathcal L_{\mathrm{S1nu}}
=
+\,s1nu\,\frac{g_Z}{2}\,
S1_\mu\,
\bar\nu_{L\,f}\gamma^\mu \nu_L^f.
\]

### `LS1er`

\[
\mathcal L_{\mathrm{S1er}}
=
+\,s1eright\,e t_W\,
S1_\mu\,
\bar e_{R\,f}\gamma^\mu e_R^f.
\]

### `LS1`

\[
\mathcal L_{\mathrm{S1}}
=
\mathcal L_{\mathrm{S1ul}}
+\mathcal L_{\mathrm{S1dl}}
+\mathcal L_{\mathrm{S1ur}}
+\mathcal L_{\mathrm{S1dr}}
+\mathcal L_{\mathrm{S1el}}
+\mathcal L_{\mathrm{S1er}}
+\mathcal L_{\mathrm{S1nu}} .
\]

### `LO1ul`

\[
\mathcal L_{\mathrm{O1ul}}
=
o1uleft\,g_s\,
O1^a_\mu\,
\bar u_{L\,f c_1}\gamma^\mu
T^a_{c_1c_2}
u_L^{f c_2}.
\]

### `LO1dl`

\[
\mathcal L_{\mathrm{O1dl}}
=
o1dleft\,g_s\,
O1^a_\mu\,
\bar d_{L\,f c_1}\gamma^\mu
T^a_{c_1c_2}
d_L^{f c_2}.
\]

### `LO1ur`

\[
\mathcal L_{\mathrm{O1ur}}
=
o1uright\,g_s\,
O1^a_\mu\,
\bar u_{R\,f c_1}\gamma^\mu
T^a_{c_1c_2}
u_R^{f c_2}.
\]

### `LO1dr`

\[
\mathcal L_{\mathrm{O1dr}}
=
o1dright\,g_s\,
O1^a_\mu\,
\bar d_{R\,f c_1}\gamma^\mu
T^a_{c_1c_2}
d_R^{f c_2}.
\]

### `LO1`

\[
\mathcal L_{\mathrm{O1}}
=
\mathcal L_{\mathrm{O1ul}}
+\mathcal L_{\mathrm{O1dl}}
+\mathcal L_{\mathrm{O1ur}}
+\mathcal L_{\mathrm{O1dr}} .
\]

## Field table

| `.fr` class | Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)\) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `S[21]` | `S0` | 0 | singlet | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MS0 = 400` |
| `S[22]` | `O0[a]` | 0 | adjoint, index `Gluon` | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MO0 = 400` |
| `V[7]` | `S1[mu]` | 1 | singlet | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MS1 = 2000` |
| `V[8]` | `O1[mu,a]` | 1 | adjoint, index `Gluon` | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MO1 = 2000` |
| `T[1]` | `S2` | 2 | singlet | not declared, singlet by indices | \(Q=0,\ Y=0\) | yes | `MS2 = 500` |

## Parameters

| External parameter | Value | Multiplies | Physical meaning |
|---|---:|---|---|
| `s0scalar` | 1 | \(S0\,\bar t t\), and internally `s0fusionScalar` | CP-even scalar coupling of color-singlet spin-0 state `S0` to top quarks; also controls loop-induced scalar gluon-fusion operator |
| `s0axial` | 1 | \(iS0\,\bar t\gamma^5 t\), and internally `s0fusionAxial` | CP-odd pseudoscalar coupling of `S0` to top quarks; also controls loop-induced dual-gluon operator |
| `o0scalar` | 1 | \(O0^a\bar tT^a t\), and internally `o0fusionScalar` | CP-even scalar coupling of color-octet spin-0 state `O0` to top quarks; also controls loop-induced \(d^{abc}O0^aG^bG^c\) operator |
| `o0axial` | 1 | \(iO0^a\bar t\gamma^5T^a t\), and internally `o0fusionAxial` | CP-odd pseudoscalar coupling of `O0` to top quarks; also controls loop-induced \(d^{abc}O0^aG^b\widetilde G^c\) operator |
| `s1uright` | 1 | `LS1ur` | Right-handed up-type quark coupling of neutral color-singlet vector `S1` |
| `s1uleft` | 1 | `LS1ul` | Left-handed up-type quark coupling of `S1` |
| `s1dright` | 1 | `LS1dr` | Right-handed down-type quark coupling of `S1` |
| `s1dleft` | 1 | `LS1dl` | Left-handed down-type quark coupling of `S1` |
| `s1eright` | 1 | `LS1er` | Right-handed charged-lepton coupling of `S1` |
| `s1eleft` | 1 | `LS1el` | Left-handed charged-lepton coupling of `S1` |
| `s1nu` | 1 | `LS1nu` | Left-handed neutrino coupling of `S1` |
| `o1uright` | 1 | `LO1ur` | Right-handed up-type quark coupling of color-octet vector `O1` |
| `o1uleft` | 1 | `LO1ul` | Left-handed up-type quark coupling of `O1` |
| `o1dright` | 1 | `LO1dr` | Right-handed down-type quark coupling of `O1` |
| `o1dleft` | 1 | `LO1dl` | Left-handed down-type quark coupling of `O1` |

Internal parameters `s0fusionScalar`, `s0fusionAxial`, `o0fusionScalar`, and `o0fusionAxial` are loop-form-factor coefficients built from the corresponding top couplings, \(g_s\), \(v\), and the spin-0 mass. Internal widths are `WS0`, `WO0`, `WS1`, and `WO1`. The tensor field `S2` has a fixed width declaration `WS2 = 2`, but no interactions are defined for it in the file.

## Physics summary

The file encodes neutral color-singlet and color-octet spin-0 and spin-1 resonances, plus a neutral singlet spin-2 state with no listed interactions. The spin-0 states couple to top quarks through scalar and pseudoscalar Yukawa-like terms and to gluons through effective \(GG\) and \(G\widetilde G\) operators, while the spin-1 states couple chirally to Standard Model fermion currents: the singlet vector to quarks and leptons with electroweak-charge-weighted coefficients, and the octet vector to quark color currents. These interactions mediate resonance production in gluon fusion or quark annihilation and decays to \(t\bar t\), dijets, charged leptons, and neutrinos depending on the state and coupling choices.

## Paper cross-check

**Lagrangian And Field Definitions**

The paper defines an EFT in the **INTRODUCTION** and **SETUP** sections. The master EFT Lagrangian is Eq. (1):
\[
\mathcal L_{\rm EFT}=\mathcal L_{\rm SM}+\sum_i \frac{C_i O_i}{\Lambda^2}+{\rm H.c.}
\]
The field notation is given in **SETUP**: \(Q\) is the third-generation left-handed quark doublet, \(q\) is a first- or second-generation left-handed quark doublet, \(t\) is the right-handed top quark, \(u,c\) are right-handed up/charm quarks, \(\phi\) is the Higgs doublet, and \(\tilde\phi=i\sigma_2\phi\).

The paper’s defining dimension-six operators are Eqs. (2)-(5):
\[
O^{(1,3)}_{uG}=y_t g_s(\bar q\sigma^{\mu\nu}T^A t)\tilde\phi G^A_{\mu\nu},
\]
\[
O^{(1,3)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar q t)\tilde\phi,
\]
\[
O^{(3,1)}_{uG}=y_t g_s(\bar Q\sigma^{\mu\nu}T^A u)\tilde\phi G^A_{\mu\nu},
\]
\[
O^{(3,1)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar Q u)\tilde\phi.
\]
The tree-level \(tuh\) interaction is Eq. (8), modified after removing \(u_L-t_R\) mixing to Eq. (11):
\[
\mathcal L'_{tuh}=
-C_{u\phi}\frac{m_t^2}{\Lambda^2}\frac{2y_t}{\sqrt2}(\bar u P_R t)h+{\rm H.c.}
\]
The paper also gives the effective \(utg\) interaction from \(O_{uG}\) in Eq. (30):
\[
\mathcal L_{\rm Eff}=
-\frac{C_{uG}}{\Lambda^2}2m_tg_s(\bar u_L\sigma^{\mu\nu}T^A t_R)\partial_\nu G^A_\mu.
\]

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| SM field content \(Q,q,t,u,c,\phi,\tilde\phi\) in **SETUP** | New fields \(S0,O0,S1,O1,S2\) plus SM fermions | disagree | The paper defines only SM fields in an EFT basis; the reconstruction defines new neutral spin-0, spin-1, and spin-2 resonances absent from the paper. |
| \(\mathcal L_{\rm EFT}=\mathcal L_{\rm SM}+\sum_i C_iO_i/\Lambda^2+{\rm H.c.}\), Eq. (1) | Sum of explicit resonance interactions \(\mathcal L_{S0},\mathcal L_{O0},\mathcal L_{S1},\mathcal L_{O1}\) | disagree | Paper is a dimension-six SM EFT; reconstruction is a simplified resonance model with independent new fields. |
| \(O^{(1,3)}_{uG}=y_tg_s(\bar q\sigma^{\mu\nu}T^At)\tilde\phi G^A_{\mu\nu}\), Eq. (2) | None | missing-in-reconstruction | No flavor-changing chromomagnetic \(q_L-t_R\) operator appears. |
| \(O^{(1,3)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar qt)\tilde\phi\), Eq. (3) | None | missing-in-reconstruction | No dimension-six flavor-changing Higgs-Yukawa operator appears. |
| \(O^{(3,1)}_{uG}=y_tg_s(\bar Q\sigma^{\mu\nu}T^Au)\tilde\phi G^A_{\mu\nu}\), Eq. (4) | None | missing-in-reconstruction | No opposite-flavor chromomagnetic operator involving \(Q_L\) and \(u_R/c_R\) appears. |
| \(O^{(3,1)}_{u\phi}=-y_t^3(\phi^\dagger\phi)(\bar Qu)\tilde\phi\), Eq. (5) | None | missing-in-reconstruction | No opposite-flavor Higgs-Yukawa operator involving \(Q_L\) and \(u_R/c_R\) appears. |
| Hermitian conjugates of Eqs. (2)-(5), discussed after Eq. (5) | Self-conjugate resonance fields and ordinary bilinears | disagree | The paper requires H.c. flavor-changing operators with chirality-flipped contributions; reconstruction has real self-conjugate bosons and flavor-diagonal currents. |
| \(y_t=\sqrt2m_t/v\), Eq. (7) | Uses \(m_t/v\) in scalar-top terms | convention | Related normalization appears, but the reconstruction applies it to new scalar resonance couplings rather than the paper’s EFT operators. |
| Tree-level \(tuh\) interaction \(-C_{u\phi}m_t^2\Lambda^{-2}(3y_t/\sqrt2)(\bar uP_Rt)h+{\rm H.c.}\), Eq. (8) | None | missing-in-reconstruction | Reconstruction contains no Higgs field \(h\), no \(t-u/c\) flavor change, and no \(P_R\) chiral structure of this kind. |
| Field rotations removing \(u_L-t_R\) mixing, Eqs. (9)-(10) | None | missing-in-reconstruction | Reconstruction has no flavor-changing mass mixing induced by \(O_{u\phi}\). |
| Rotated \(tuh\) interaction \(-C_{u\phi}m_t^2\Lambda^{-2}(2y_t/\sqrt2)(\bar uP_Rt)h+{\rm H.c.}\), Eq. (11) | None | missing-in-reconstruction | This is the paper’s physical tree-level \(tuh\) vertex after diagonalization; reconstruction has no counterpart. |
| Counterterm form \(O_{u\phi}\to -y_t^3(\phi^\dagger\phi-v^2/2)(\bar qt)\tilde\phi\), Eq. (12) | None | missing-in-reconstruction | Reconstruction has no Higgs-doublet EFT operator or subtraction of the vev-induced mixing term. |
| Effective decomposition \(\mathcal L_{\rm Eff}=\mathcal L_{tu}+\mathcal L_{tuh}\), Eqs. (25)-(27) | None | missing-in-reconstruction | Reconstruction lacks the \(u_L-t_R\) mixing and \(tuh\) counterterm structure. |
| \(utg\) dipole interaction from \(O_{uG}\), Eq. (30) | None | missing-in-reconstruction | Reconstruction has gluon field-strength operators, but they couple gluons to new scalars, not to a flavor-changing quark dipole. |
| EOM-vanishing counterterm operators \(O^{(1)},O^{(2)}\), Eqs. (33)-(34) | None | missing-in-reconstruction | These are part of the paper’s renormalization treatment of \(O_{uG}\); reconstruction has no analogous EFT renormalization structure. |
| Renormalized effective Lagrangian with \(C_{u\phi}\), \(C_{uG}\), and mixing counterterms, Eq. (37) | None | missing-in-reconstruction | Reconstruction does not contain Wilson coefficients \(C_{u\phi},C_{uG}\), operator mixing, or dimension-six counterterms. |
| None | \(S0\,\bar tt\) scalar coupling | extra-in-reconstruction | No color-singlet scalar resonance \(S0\) or flavor-diagonal \(S0\bar tt\) interaction is defined in the paper. |
| None | \(iS0\,\bar t\gamma^5t\) pseudoscalar coupling | extra-in-reconstruction | No pseudoscalar top resonance coupling appears in the paper. |
| None | \(S0\,G^a_{\mu\nu}G^{a\mu\nu}\) | extra-in-reconstruction | Paper has a chromomagnetic quark-Higgs-gluon operator, not a scalar-gluon-gluon effective resonance operator. |
| None | \(S0\,G^a_{\mu\nu}\tilde G^{a\mu\nu}\) | extra-in-reconstruction | No CP-odd scalar-gluon-gluon operator is part of the paper’s model. |
| None | \(O0^a\bar tT^at\) scalar color-octet coupling | extra-in-reconstruction | Paper has no color-octet scalar resonance. |
| None | \(iO0^a\bar t\gamma^5T^at\) color-octet pseudoscalar coupling | extra-in-reconstruction | Paper has no color-octet pseudoscalar top coupling. |
| None | \(d^{abc}O0^aG^b_{\mu\nu}G^{c\mu\nu}\) | extra-in-reconstruction | Paper has no \(d^{abc}\) scalar-octet gluon-fusion operator. |
| None | \(d^{abc}O0^aG^b_{\mu\nu}\tilde G^{c\mu\nu}\) | extra-in-reconstruction | Paper has no CP-odd color-octet scalar-gluon operator. |
| None | \(S1_\mu\bar u_L\gamma^\mu u_L\), \(S1_\mu\bar d_L\gamma^\mu d_L\), \(S1_\mu\bar u_R\gamma^\mu u_R\), \(S1_\mu\bar d_R\gamma^\mu d_R\) | extra-in-reconstruction | Paper has no neutral color-singlet vector resonance or flavor-diagonal quark-current interactions. |
| None | \(S1_\mu\bar e_L\gamma^\mu e_L\), \(S1_\mu\bar e_R\gamma^\mu e_R\), \(S1_\mu\bar\nu_L\gamma^\mu\nu_L\) | extra-in-reconstruction | Paper does not introduce lepton-current couplings. |
| None | \(O1^a_\mu\bar u_{L,R}\gamma^\mu T^au_{L,R}\), \(O1^a_\mu\bar d_{L,R}\gamma^\mu T^ad_{L,R}\) | extra-in-reconstruction | Paper has no color-octet vector resonance or flavor-diagonal color-current couplings. |
| None | Tensor field \(S2\), neutral singlet, no interactions | extra-in-reconstruction | No spin-2 field is present in the paper. |

**Disagreements**

| item | severity | what a human should check |
|---|---|---|
| Reconstruction introduces \(S0,O0,S1,O1,S2\) resonance fields absent from the paper. | substantive | Check whether `reconstruction.md` came from a different model file than the paper, possibly a generic resonance implementation. |
| Paper’s EFT master Lagrangian Eq. (1) is not reproduced. | substantive | Verify whether the implementation was supposed to encode the paper’s dimension-six EFT or a separate phenomenological model. |
| Missing \(O^{(1,3)}_{uG}\), Eq. (2). | substantive | Check for any hidden flavor-changing top-light-quark chromomagnetic operator in the original implementation. |
| Missing \(O^{(1,3)}_{u\phi}\), Eq. (3). | substantive | Check whether the implementation contains a \(tuh\) FCNC Yukawa vertex under another name. |
| Missing \(O^{(3,1)}_{uG}\), Eq. (4). | substantive | Check whether chirality-flipped or conjugate flavor structures were intentionally omitted. |
| Missing \(O^{(3,1)}_{u\phi}\), Eq. (5). | substantive | Check whether the implementation supports both \(t\to uh/ch\) chiralities. |
| Reconstruction lacks the paper’s Hermitian-conjugate FCNC structure. | substantive | Check whether both decay and conjugate amplitudes are generated in the implementation. |
| Reconstruction uses \(m_t/v\) normalization for unrelated scalar-top resonance couplings. | convention | Check whether this normalization was copied from another simplified model and not from the EFT paper. |
| Missing paper’s tree-level \(tuh\) interaction Eq. (8). | substantive | Check generated Feynman rules for a \(t-u/c-h\) vertex. |
| Missing field rotations Eqs. (9)-(10). | substantive | Check whether mass diagonalization or equivalent counterterms are implemented. |
| Missing physical rotated \(tuh\) coupling Eq. (11). | substantive | Check whether the implementation uses the correct factor \(2y_t/\sqrt2\), not the pre-rotation factor \(3y_t/\sqrt2\). |
| Missing counterterm-subtracted \(O_{u\phi}\) form Eq. (12). | substantive | Check whether vev-induced \(u_L-t_R\) mixing is removed consistently. |
| Missing \(\mathcal L_{tu}+\mathcal L_{tuh}\) counterterm structure Eqs. (25)-(27). | substantive | Check whether NLO renormalization was implemented at all. |
| Missing \(utg\) dipole interaction Eq. (30). | substantive | Check whether the implementation contains a flavor-changing \(t-u/c-g\) dipole vertex rather than only gluon-fusion resonance operators. |
| Missing EOM-vanishing counterterms Eqs. (33)-(34). | substantive | Check whether the implementation is intended only for tree level or includes the NLO operator-renormalization setup. |
| Missing renormalized Lagrangian Eq. (37). | substantive | Check whether Wilson-coefficient mixing \(C_{uG}\to C_{u\phi}\) is encoded elsewhere. |
| Extra \(S0\bar tt\), \(S0GG\), and \(S0G\tilde G\) terms. | substantive | Check whether the source implementation is for a scalar resonance model, not this FCNC Higgs EFT paper. |
| Extra \(O0\bar tT^at\), \(O0GG\), and \(O0G\tilde G\) terms. | substantive | Check whether color-octet scalar resonance interactions belong to another paper or benchmark. |
| Extra \(S1\) flavor-diagonal quark and lepton currents. | substantive | Check whether a \(Z'\)-like model was accidentally reconstructed instead of the paper’s EFT. |
| Extra \(O1\) color-octet vector quark currents. | substantive | Check whether an axigluon/coloron model was mixed into the reconstruction. |
| Extra inert spin-2 field \(S2\). | substantive | Check whether the implementation file contains unused benchmark particles unrelated to the paper. |

**Overall Assessment**

The reconstruction does not match the model defined in the paper. The paper is a Standard Model EFT treatment of flavor-changing top-Higgs interactions, centered on the dimension-six operators \(O_{uG}\) and \(O_{u\phi}\), their flavor assignments, chirality structure, Higgs-doublet dependence, and NLO QCD renormalization. The reconstruction instead describes a simplified resonance model with new scalar, vector, color-octet, and tensor fields coupled mostly to flavor-diagonal SM currents or gluon-fusion operators. Apart from incidental use of familiar SM quantities such as \(m_t/v\), \(g_s\), and color generators, the field content, operator basis, charges, chirality structure, and coefficient organization are substantively different.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 28 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

