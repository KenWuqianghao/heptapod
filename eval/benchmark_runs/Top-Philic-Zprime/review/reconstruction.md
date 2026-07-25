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