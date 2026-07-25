# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Conventions: repeated Lorentz and color indices are summed. The gluon field strength is
\[
G^a_{\mu\nu}
=
\partial_\mu G^a_\nu-\partial_\nu G^a_\mu
+ g_s f^{abc}G^b_\mu G^c_\nu ,
\qquad
\widetilde G^{a\mu\nu}
=
\frac12 \epsilon^{\mu\nu\rho\sigma}G^a_{\rho\sigma}.
\]
No `DC[...]` covariant derivatives appear in the file. The only derivative acting on a new field is an ordinary partial derivative. All new fields have `Q -> 0` and no declared color or weak indices, so they are SM gauge singlets; their gauge covariant derivative would therefore reduce to
\[
D_\mu = \partial_\mu
\]
on the new fields. The SM quark and gluon objects use the standard FeynRules SM gauge content.

### `L0X`

\[
\mathcal L_{\texttt{L0X},\,X_r}
=
\frac12\, M_{X_r}\, g_{S X_r}\, X_r X_r\, Y_0 .
\]

\[
\mathcal L_{\texttt{L0X},\,X_c}
=
M_{X_c}\, g_{S X_c}\, X_c^\dagger X_c\, Y_0 .
\]

\[
\mathcal L_{\texttt{L0X},\,X_d}
=
\bar X_d
\left(
g^S_{\rm DM}
+ i g^P_{\rm DM}\gamma^5
\right)
X_d\,Y_0 .
\]

### `L0SM`

\[
\mathcal L_{\texttt{L0SM}}
=
\frac{y_t}{\sqrt2}\,
\bar t_i
\left(
g^S_t
+ i g^P_t\gamma^5
\right)
t_i\,Y_0 .
\]

Here \(i\) is the color index, contracted as \(\delta_{ij}\).

### `L0SMg`

\[
\mathcal L_{\texttt{L0SMg},\,S}
=
\frac{g^S_g}{\Lambda}\,
Y_0\,G^a_{\mu\nu}G^{a\mu\nu}.
\]

\[
\mathcal L_{\texttt{L0SMg},\,P}
=
\frac{g^P_g}{\Lambda}\,
Y_0\,G^a_{\mu\nu}\widetilde G^{a\mu\nu}.
\]

### `L0DM`

\[
\mathcal L_{\texttt{L0DM}}
=
\mathcal L_{\texttt{L0X}}
+
\mathcal L_{\texttt{L0SM}}
+
\mathcal L_{\texttt{L0SMg}} .
\]

### `L1X`

\[
\mathcal L_{\texttt{L1X},\,X_c}
=
\frac{i g_{V X_c}}{2}
\left[
X_c^\dagger \partial_\mu X_c
-
(\partial_\mu X_c^\dagger)X_c
\right]
Y_1^\mu .
\]

\[
\mathcal L_{\texttt{L1X},\,X_d}
=
\bar X_d\gamma^\mu
\left(
g^V_{\rm DM}
+
g^A_{\rm DM}\gamma^5
\right)
X_d\,Y_{1\mu}.
\]

Equivalently, in chiral form,
\[
\bar X_d\gamma^\mu
\left[
(g^V_{\rm DM}-g^A_{\rm DM})P_L
+
(g^V_{\rm DM}+g^A_{\rm DM})P_R
\right]
X_d\,Y_{1\mu}.
\]

### `L1SM`

\[
\mathcal L_{\texttt{L1SM},\,t}
=
\bar t_i\gamma^\mu
\left(
g^V_t
+
g^A_t\gamma^5
\right)
t_i\,Y_{1\mu}.
\]

Equivalently,
\[
\bar t_i\gamma^\mu
\left[
(g^V_t-g^A_t)P_L
+
(g^V_t+g^A_t)P_R
\right]
t_i\,Y_{1\mu}.
\]

\[
\mathcal L_{\texttt{L1SM},\,b}
=
-\,g^A_t\,
\bar b_i\gamma^\mu\gamma^5 b_i\,Y_{1\mu}.
\]

Equivalently,
\[
\mathcal L_{\texttt{L1SM},\,b}
=
\bar b_i\gamma^\mu
\left[
g^A_t P_L
-
g^A_t P_R
\right]
b_i\,Y_{1\mu}.
\]

### `L1DM`

\[
\mathcal L_{\texttt{L1DM}}
=
\mathcal L_{\texttt{L1X}}
+
\mathcal L_{\texttt{L1SM}} .
\]

## Field Table

| Symbol | Class | Spin | SU(3) rep | SU(2) rep | U(1) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---|---|
| \(X_r\) | `S[7]` | 0 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | Yes, real scalar | \(M_{X_r}=10\) |
| \(X_c\) | `S[8]` | 0 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | No, complex scalar | \(M_{X_c}=10\) |
| \(X_d\) | `F[7]` | \(1/2\) | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | No, Dirac fermion | \(M_{X_d}=10\) |
| \(Y_0\) | `S[9]` | 0 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | Yes, real scalar | \(M_{Y_0}=1000\) |
| \(Y_1\) | `V[7]` | 1 | \(\mathbf 1\) | \(\mathbf 1\) | \(Q=0\), hence \(Y=0\) for an EW singlet | Yes, real vector | \(M_{Y_1}=1000\) |

Widths declared in the file are \(\Gamma_{X_r}=0\), \(\Gamma_{X_c}=0\), \(\Gamma_{X_d}=0\), \(\Gamma_{Y_0}=W_{Y_0}=10\), and \(\Gamma_{Y_1}=W_{Y_1}=10\).

## Parameters

| Symbol | Default value | Appears in | Physical meaning |
|---|---:|---|---|
| `gSXr` | 0 | \(\frac12 M_{X_r} g_{S X_r} X_r^2 Y_0\) | Scalar coupling of the real scalar \(X_r\) to the scalar mediator \(Y_0\). |
| `gSXc` | 0 | \(M_{X_c} g_{S X_c} X_c^\dagger X_c Y_0\) | Scalar coupling of the complex scalar \(X_c\) to \(Y_0\). |
| `gSXd` | 1 | \(\bar X_d g^S_{\rm DM} X_d Y_0\) | Scalar Yukawa-like coupling of Dirac fermion \(X_d\) to \(Y_0\). |
| `gPXd` | 0 | \(i\bar X_d g^P_{\rm DM}\gamma^5 X_d Y_0\) | Pseudoscalar coupling of \(X_d\) to \(Y_0\). |
| `gSt` | 1 | \(\frac{y_t}{\sqrt2}\bar t g^S_t tY_0\) | Scalar coupling of \(Y_0\) to top quarks, normalized by \(y_t/\sqrt2\). |
| `gPt` | 0 | \(\frac{y_t}{\sqrt2}i\bar t g^P_t\gamma^5 tY_0\) | Pseudoscalar coupling of \(Y_0\) to top quarks, normalized by \(y_t/\sqrt2\). |
| `Lambda` | 10000 | \(\Lambda^{-1}Y_0G_{\mu\nu}G^{\mu\nu}\), \(\Lambda^{-1}Y_0G_{\mu\nu}\widetilde G^{\mu\nu}\) | Heavy scale suppressing the effective scalar and pseudoscalar gluon operators. |
| `gSg` | 0 | \(\frac{g^S_g}{\Lambda}Y_0G^a_{\mu\nu}G^{a\mu\nu}\) | Effective CP-even coupling of \(Y_0\) to gluons. |
| `gPg` | 0 | \(\frac{g^P_g}{\Lambda}Y_0G^a_{\mu\nu}\widetilde G^{a\mu\nu}\) | Effective CP-odd coupling of \(Y_0\) to gluons. |
| `gVXc` | 0 | \(\frac{i g_{V X_c}}2 X_c^\dagger\overleftrightarrow{\partial_\mu}X_c\,Y_1^\mu\) | Vector-current coupling of complex scalar \(X_c\) to vector mediator \(Y_1\). |
| `gVXd` | 1 | \(\bar X_d\gamma^\mu g^V_{\rm DM}X_dY_{1\mu}\) | Vector coupling of Dirac fermion \(X_d\) to \(Y_1\). |
| `gAXd` | 0 | \(\bar X_d\gamma^\mu g^A_{\rm DM}\gamma^5X_dY_{1\mu}\) | Axial-vector coupling of \(X_d\) to \(Y_1\). |
| `gVt` | 1 | \(\bar t\gamma^\mu g^V_t tY_{1\mu}\) | Vector coupling of \(Y_1\) to top quarks. |
| `gAt` | 0 | \(\bar t\gamma^\mu g^A_t\gamma^5tY_{1\mu}\), \(-\bar b\gamma^\mu g^A_t\gamma^5bY_{1\mu}\) | Axial-vector coupling of \(Y_1\) to tops and, with opposite sign structure in the Lagrangian, to bottoms. |

## Physics Summary

The file encodes a simplified SM-singlet dark-sector mediator setup with three possible dark matter candidates: a real scalar \(X_r\), a complex scalar \(X_c\), and a Dirac fermion \(X_d\). A scalar mediator \(Y_0\) couples to these dark states, to top quarks through scalar and pseudoscalar bilinears, and to gluons through dimension-five CP-even and CP-odd operators; a vector mediator \(Y_1\) couples to scalar and fermion dark currents, to top vector/axial currents, and to a bottom axial current.

The interactions mediate production or annihilation channels such as \(gg\to Y_0\to X\bar X\), \(t\bar t\to Y_0/Y_1\to X\bar X\), mediator-associated heavy-quark processes, and mediator decays into dark matter, tops, bottoms, or gluons depending on the enabled couplings and masses.