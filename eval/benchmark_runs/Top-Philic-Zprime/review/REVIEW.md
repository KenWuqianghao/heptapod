# Reverse-check review package — `Top-Philic-Zprime_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `Top-Philic-Zprime/model/Top-Philic-Zprime_gen.fr` |
| original model name | `Top-Philic-Zprime_gen` (hidden from the agent) |
| paper | Top-Philic-Zprime/text/1604.07421.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LV1kin` (`=`)

```mathematica
-1/4 (del[V1[nu], mu] - del[V1[mu], nu]) (del[V1[nu], mu] - del[V1[mu], nu]) + 1/2 MV1^2 V1[mu] V1[mu]
```

### `LV1intL` (`=`)

```mathematica
Block[{sp1, sp2, cc}, cL V1[mu] QLbar[sp1, 1, 3, cc] Ga[mu, sp1, sp2] QL[sp2, 1, 3, cc]]
```

### `LV1intR` (`=`)

```mathematica
Block[{sp1, sp2, cc}, cR V1[mu] uRbar[sp1, 3, cc] Ga[mu, sp1, sp2] uR[sp2, 3, cc]]
```

### `LV1int` (`=`)

```mathematica
LV1intL + LV1intR
```

### `LBSM` (`=`)

```mathematica
LV1kin + LV1int
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

The model contains one new real neutral massive vector field \(V_{1\mu}\). It has no declared nontrivial gauge indices and has
\[
Q(V_1)=0,\qquad Y(V_1)=0.
\]
Since \(V_1\) is a gauge singlet, its covariant derivative is just
\[
D_\mu V_{1\nu}=\partial_\mu V_{1\nu}.
\]
The corresponding Abelian field strength appearing in the file is
\[
V_{1\mu\nu} \equiv \partial_\mu V_{1\nu}-\partial_\nu V_{1\mu}.
\]

### `LV1kin`

```mathematica
LV1kin = -1/4 (del[V1[nu], mu] - del[V1[mu], nu])
              (del[V1[nu], mu] - del[V1[mu], nu])
         + 1/2 MV1^2 V1[mu] V1[mu];
```

\[
\mathcal L_{\texttt{LV1kin}}
=
-\frac14 V_{1\mu\nu}V_1^{\mu\nu}
+\frac12 M_{V_1}^2 V_{1\mu}V_1^\mu .
\]

### `LV1intL`

```mathematica
LV1intL =
Block[{sp1, sp2, cc},
  cL V1[mu] QLbar[sp1, 1, 3, cc]
     Ga[mu, sp1, sp2]
     QL[sp2, 1, 3, cc]
];
```

Here `QL[sp, 1, 3, cc]` is the upper component of the third-generation left-handed quark doublet, i.e. the left-handed top quark \(t_L\), with color index \(c\). The color index is contracted diagonally.

\[
\mathcal L_{\texttt{LV1intL}}
=
c_L\, V_{1\mu}\,
\bar t_{L,c}\gamma^\mu t_L^{c}.
\]

Equivalently, using chiral projectors,
\[
\mathcal L_{\texttt{LV1intL}}
=
c_L\, V_{1\mu}\,
\bar t_c \gamma^\mu P_L t^c,
\qquad
P_L=\frac{1-\gamma^5}{2}.
\]

### `LV1intR`

```mathematica
LV1intR =
Block[{sp1, sp2, cc},
  cR V1[mu] uRbar[sp1, 3, cc]
     Ga[mu, sp1, sp2]
     uR[sp2, 3, cc]
];
```

Here `uR[sp, 3, cc]` is the right-handed top quark \(t_R\), again with a diagonally contracted color index.

\[
\mathcal L_{\texttt{LV1intR}}
=
c_R\, V_{1\mu}\,
\bar t_{R,c}\gamma^\mu t_R^{c}.
\]

Equivalently,
\[
\mathcal L_{\texttt{LV1intR}}
=
c_R\, V_{1\mu}\,
\bar t_c \gamma^\mu P_R t^c,
\qquad
P_R=\frac{1+\gamma^5}{2}.
\]

### `LV1int`

```mathematica
LV1int = LV1intL + LV1intR;
```

\[
\mathcal L_{\texttt{LV1int}}
=
V_{1\mu}\,
\bar t_c \gamma^\mu
\left(
c_L P_L+c_R P_R
\right)
t^c .
\]

### `LBSM`

```mathematica
LBSM = LV1kin + LV1int;
```

\[
\mathcal L_{\texttt{LBSM}}
=
-\frac14 V_{1\mu\nu}V_1^{\mu\nu}
+\frac12 M_{V_1}^2 V_{1\mu}V_1^\mu
+
V_{1\mu}\,
\bar t_c \gamma^\mu
\left(
c_L P_L+c_R P_R
\right)
t^c .
\]

The internal coupling definitions are
\[
c_L = c_t \cos\theta,
\qquad
c_R = c_t \sin\theta,
\]
where the `.fr` symbols are `cL`, `cR`, `ct`, and `thetaV1`.

Thus the interaction can also be written as
\[
\mathcal L_{\texttt{LV1int}}
=
c_t\,V_{1\mu}\,
\bar t_c \gamma^\mu
\left(
\cos\theta\,P_L+\sin\theta\,P_R
\right)
t^c .
\]

## Field Table

| `.fr` symbol | Particle | Spin | SU(3) rep | SU(2) rep | \(U(1)_Y\) | Electric charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `V1` | \(V_{1\mu}\) | 1 | singlet, no color index declared | singlet, no weak index declared | \(0\) | \(0\) | yes | `MV1 = 1500.` |

The vector width is internal:

\[
\Gamma_{V_1} = \texttt{WV1}.
\]

For \(M_{V_1}>2m_t\), the file defines

\[
\Gamma_{V_1}
=
\frac{c_t^2 M_{V_1}}{8\pi}
\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}
\left[
1-\frac{m_t^2}{M_{V_1}^2}
\left(
1-3\sin 2\theta
\right)
\right],
\]
and otherwise
\[
\Gamma_{V_1}=0.
\]

## Parameters

| `.fr` symbol | Type | Value | Appears in | Physical meaning |
|---|---:|---:|---|---|
| `ct` | external | `2.` | `cL`, `cR`, `WV1` | Overall strength of the \(V_1 \bar t t\) coupling |
| `thetaV1` | external | `1.5707963267948966` | `cL`, `cR`, `WV1` | Chiral mixing angle controlling the relative left- and right-handed top couplings |
| `cL` | internal | \(c_t\cos\theta\) | `LV1intL` | Left-handed top coupling |
| `cR` | internal | \(c_t\sin\theta\) | `LV1intR` | Right-handed top coupling |
| `WV1` | internal | width formula above | particle width of `V1` | Total width for \(V_1\to t\bar t\), when kinematically open |

Only `ct` and `thetaV1` are new external parameters in the file.

## Physics Summary

This model adds a single real, electrically neutral, color-singlet massive vector boson \(V_1\) with direct vector-current interactions only to top quarks. Its couplings are chiral, with independent left- and right-handed pieces fixed by \(c_L=c_t\cos\theta\) and \(c_R=c_t\sin\theta\).

It mediates processes involving top-quark pairs, especially resonant or off-shell production and decay \(V_1 \leftrightarrow t\bar t\), with chirality-dependent amplitudes.

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Location

The model is defined in **Section 2, “A Top-Philic Resonance: Simplified Model”**, especially **Section 2.1, “Setup”**. The paper introduces a **color-singlet vector particle \(V_1\)** that dominantly couples to \(t\bar t\), and gives the relevant interaction Lagrangian in **Eq. (2.1)**:
\[
\mathcal L_{\rm int}
=
\bar t\gamma_\mu(c_L P_L+c_R P_R)t\,V_1^\mu
=
c_t\bar t\gamma_\mu(\cos\theta P_L+\sin\theta P_R)t\,V_1^\mu .
\]
The chiral projectors and coupling definitions are stated immediately below Eq. (2.1):
\[
P_{R/L}=(1\pm\gamma^5)/2,\qquad
c_t=\sqrt{c_L^2+c_R^2},\qquad
\tan\theta=c_R/c_L .
\]
The decay width is given in **Eq. (2.2)**:
\[
\Gamma(V_1\to t\bar t)
=
\frac{c_t^2 M_{V_1}}{8\pi}
\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}
\left[
1-\frac{m_t^2}{M_{V_1}^2}
\left(1-3\sin(2\theta)\right)
\right].
\]
Section 2.2 states that the paper treats \((M_{V_1},c_t,\theta)\) as the three free parameters and then sets \(\theta=\pi/2\) for the rest of the collider study. Section 3 says the MadGraph implementation is based on Eq. (2.1) with parameters \(M_{V_1},c_t,\theta\).

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Color-singlet vector particle \(V_1\), Section 2.1 | One new real neutral massive vector field \(V_{1\mu}\), color singlet, weak singlet, \(Q=Y=0\), self-conjugate | agree | The paper explicitly says “color singlet vector particle.” It does not explicitly list \(SU(2)_L\), \(U(1)_Y\), electric charge, or self-conjugacy, but the neutral \(V_1^\mu \bar t\gamma_\mu t\) interaction implies no electric or color charge. Weak-singlet status is an implementation-level completion of the simplified post-EWSB interaction. |
| \(\bar t\gamma_\mu c_LP_Lt\,V_1^\mu\), Eq. (2.1) | \(c_L V_{1\mu}\bar t_c\gamma^\mu P_Lt^c\), reconstructed from `QLbar[...,1,3,cc] QL[...,1,3,cc]` | agree | Physics content matches: left-handed top current only, diagonal color contraction, no bottom or light-quark current. |
| \(\bar t\gamma_\mu c_RP_Rt\,V_1^\mu\), Eq. (2.1) | \(c_R V_{1\mu}\bar t_c\gamma^\mu P_Rt^c\), reconstructed from `uRbar[...,3,cc] uR[...,3,cc]` | agree | Physics content matches: right-handed top current only, diagonal color contraction. |
| Full interaction \(\bar t\gamma_\mu(c_LP_L+c_RP_R)tV_1^\mu\), Eq. (2.1) | \(V_{1\mu}\bar t_c\gamma^\mu(c_LP_L+c_RP_R)t^c\) | agree | Same chiral current structure. Differences are only index placement and metric/notational conventions. |
| Reparametrized interaction \(c_t\bar t\gamma_\mu(\cos\theta P_L+\sin\theta P_R)tV_1^\mu\), Eq. (2.1) | \(c_tV_{1\mu}\bar t_c\gamma^\mu(\cos\theta P_L+\sin\theta P_R)t^c\) | agree | Matches the paper’s second form of Eq. (2.1). |
| \(P_{R/L}=(1\pm\gamma^5)/2\), text below Eq. (2.1) | \(P_L=(1-\gamma^5)/2\), \(P_R=(1+\gamma^5)/2\) | agree | Exact match. |
| \(c_t=\sqrt{c_L^2+c_R^2}\), \(\tan\theta=c_R/c_L\), text below Eq. (2.1) | \(c_L=c_t\cos\theta\), \(c_R=c_t\sin\theta\) | agree | Equivalent when \(c_t\) is taken positive and \(\theta\) carries the quadrant/sign convention. A human should note that the reconstruction uses the implementation’s explicit parametrization rather than the paper’s inverse definitions. |
| \(\Gamma(V_1\to t\bar t)\), Eq. (2.2) | Same expression for \(\Gamma_{V_1}\), with \(\Gamma_{V_1}=0\) below threshold | agree | The formula matches Eq. (2.2). The below-threshold zero is an implementation detail; the paper focuses on TeV-range \(M_{V_1}\) and only remarks that other modes below \(2m_t\) are possible. |
| Three free parameters \((M_{V_1},c_t,\theta)\), Section 2.2 and Section 3 | Parameters `MV1`, `ct`, `thetaV1`; defaults `MV1=1500`, `ct=2`, `thetaV1=pi/2` | agree | The parameter set matches. The numerical values correspond to the paper’s benchmark and later choice \(\theta=\pi/2\), but the paper scans \(M_{V_1}\) and \(c_t\); the defaults should not be read as the full paper model. |
| Paper later sets \(\theta=\pi/2\), Section 2.2 | `thetaV1 = 1.5707963267948966` | agree | This matches the right-handed-top benchmark used for the rest of the paper. |
| Contact interaction after integrating out \(V_1\) at \(\theta=\pi/2\): \(\frac12\frac{c_t^2}{M_{V_1}^2}(\bar t_R\gamma_\mu t_R)(\bar t_R\gamma^\mu t_R)\), Eq. (2.3) | No contact operator listed | missing-in-reconstruction | This is not part of the fundamental implemented Lagrangian; it is an effective comparison used for ATLAS bounds. Missing it is not a mismatch for the UV/simplified model implementation. |
| No explicit kinetic or Proca mass term written in the paper’s model equations | \(-\frac14V_{1\mu\nu}V_1^{\mu\nu}+\frac12M_{V_1}^2V_{1\mu}V_1^\mu\) | extra-in-reconstruction | The paper gives only the “relevant interaction” Lagrangian in Eq. (2.1), not the full free-field Lagrangian. The kinetic and mass terms are standard for a massive real vector and consistent with the stated massive resonance. |
| Paper assumes other interactions are weak/negligible, Section 2.1 | Reconstruction includes only \(V_1\bar tt\) interactions | agree | The reconstruction correctly omits light-quark, bottom, lepton, gauge-boson, and Higgs interactions. |
| Possible below-threshold modes for \(M_{V_1}<2m_t\), mentioned in Section 2.2 via Ref. [37] | Reconstruction sets \(\Gamma_{V_1}=0\) below \(2m_t\) | disagree | For the paper’s TeV-range study this is irrelevant, but strictly the paper acknowledges other possible decay modes below threshold rather than defining a zero total width there. |

## Disagreements and Checks

- **Extra Proca kinetic/mass term** — severity: **cosmetic**. A human should check whether the review target is the paper’s displayed interaction-only Lagrangian or the full FeynRules implementation, because the extra term is standard and physically expected for event generation.

- **Below-threshold width set to zero** — severity: **convention**. A human should check whether the implementation is intended only for \(M_{V_1}>2m_t\), since the paper explicitly points to possible sub-threshold decays but does not use them in the TeV analysis.

- **Contact operator Eq. (2.3) absent** — severity: **cosmetic**. A human should check whether the reconstruction is meant to include derived EFT limits; it is not necessary for reproducing the simplified model Lagrangian Eq. (2.1).

- **Default numerical values \(M_{V_1}=1.5\) TeV, \(c_t=2\), \(\theta=\pi/2\)** — severity: **convention**. A human should check that these are treated as benchmark/default parameter-card values, not as fixed model definitions, because the paper scans \(M_{V_1}\) and \(c_t\).

## Overall Assessment

The reconstruction captures the core model defined by the paper: a color-singlet neutral vector resonance \(V_1\) with chiral couplings only to the top quark, parametrized by \(c_t\) and \(\theta\), with the same \(V_1\to t\bar t\) width as Eq. (2.2). The main differences are about scope rather than the central interaction: the reconstruction includes the standard free massive-vector terms that the paper does not explicitly write, omits the derived contact operator used only for bounds, and encodes a zero below-threshold width despite the paper noting possible non-\(t\bar t\) decays in that region. For the TeV-scale four-top simplified model studied in the paper, the physics content is closely aligned.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 6 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

