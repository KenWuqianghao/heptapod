# Reconstructed Physics From `sanitized.fr`

## Lagrangian

### Conventions

Flavor indices \(i,j,m,n=1,2,3\). Color fundamental indices \(a,b\), adjoint indices \(A,B,C\). The SM quark and lepton fields are Dirac fields, with
\[
P_L=\frac{1-\gamma_5}{2},\qquad P_R=\frac{1+\gamma_5}{2}.
\]
`ProjM` is \(P_L\), `ProjP` is \(P_R\). `Ga[mu]` is \(\gamma^\mu\). `HC[...]` is the Hermitian conjugate.

The new complex vector field `VLQ` is denoted \(U_\mu^a\). The neutral singlet vector `Zp` is \(Z'_\mu\). The color-octet vector `Gp` is \(G'^A_\mu\).

The covariant derivatives appearing in `DC` are
\[
D_\rho U_\mu^a
=
\partial_\rho U_\mu^a
-i g_s\,G_\rho^A (T^A)^a{}_{b} U_\mu^b
-i g_1\,\frac{2}{3} B_\rho U_\mu^a ,
\]
\[
D_\rho \bar U_\mu^a
=
\partial_\rho \bar U_\mu^a
+i g_s\,\bar U_\mu^b (T^A)^b{}_{a}G_\rho^A
+i g_1\,\frac{2}{3} B_\rho \bar U_\mu^a ,
\]
and
\[
D_\rho G'^A_\mu
=
\partial_\rho G'^A_\mu
+g_s f^{ABC}G_\rho^B G'^C_\mu .
\]
The corresponding antisymmetric tensors used below are
\[
U_{\mu\nu}^a=D_\mu U_\nu^a-D_\nu U_\mu^a,
\qquad
G'^{A}_{\mu\nu}=D_\mu G'^A_\nu-D_\nu G'^A_\mu .
\]

### `LVLQKin`

\[
\mathcal L_{\texttt{LVLQKin}}
=
-\frac12\,\bar U_{\mu\nu}^{\,a} U^{a\,\mu\nu}.
\]

### `LVLQF`

\[
\mathcal L_{\texttt{LVLQF}}
=
\frac{g_U}{\sqrt2}\,
U_\mu^a
\left[
\beta^L_{ij} V_{ki}\,
\bar u_k^a \gamma^\mu P_L \nu_j
+
\beta^L_{ij}\,
\bar d_i^a \gamma^\mu P_L \ell_j
+
\beta^{R d}_{ij}\,
\bar d_i^a \gamma^\mu P_R \ell_j
\right].
\]

The internal flavor matrices are
\[
\beta^L_{13}=\left(\frac{V_{31}}{V_{32}}\right)^* \beta^L_{23},
\qquad
\beta^L_{23}=\betaL23,
\qquad
\beta^L_{32}=\betaL32,
\qquad
\beta^L_{33}=\betaL33,
\]
with all entries involving lepton generation \(1\) set to zero, and \(\beta^L_{12}=\beta^L_{22}=0\). Also
\[
\beta^{R d}_{33}=\betaRd33,
\]
with all other declared entries zero.

### `HC[LVLQF]`

\[
\mathcal L_{\texttt{HC[LVLQF]}}
=
\frac{g_U}{\sqrt2}\,
\bar U_\mu^a
\left[
(\beta^L_{ij})^* V^*_{ki}\,
\bar\nu_j \gamma^\mu P_L u_k^a
+
(\beta^L_{ij})^*\,
\bar\ell_j \gamma^\mu P_L d_i^a
+
(\beta^{R d}_{ij})^*\,
\bar\ell_j \gamma^\mu P_R d_i^a
\right].
\]

### `LVLQG`

\[
\mathcal L_{\texttt{LVLQG}}
=
-i g_s(1-\kappa_U)\,
\bar U_\mu^a (T^A)^a{}_{b} U_\nu^b\,G^{A\,\mu\nu}
-i\,\frac{2}{3}g_1(1-\tilde\kappa_U)\,
\bar U_\mu^a U_\nu^a\,B^{\mu\nu}.
\]

### `LZpF`

\[
\mathcal L_{\texttt{LZpF}}
=
\frac{g_{Z'}}{2\sqrt6}\,
Z'_\mu
\left[
\zeta^q_{ij} V_{ki}V^*_{nj}\,
\bar u_k^a\gamma^\mu P_L u_n^a
+
\zeta^q_{ij}\,
\bar d_i^a\gamma^\mu P_L d_j^a
\right.
\]
\[
\left.
-3\zeta^\ell_{ij}\,
\bar\ell_i\gamma^\mu P_L\ell_j
-3\zeta^\ell_{ij}\,
\bar\nu_i\gamma^\mu P_L\nu_j
+
\zeta^u_{ij}\,
\bar u_i^a\gamma^\mu P_R u_j^a
+
\zeta^d_{ij}\,
\bar d_i^a\gamma^\mu P_R d_j^a
-3\zeta^e_{ij}\,
\bar\ell_i\gamma^\mu P_R\ell_j
\right].
\]

The nonzero internal entries are
\[
\zeta^q_{11}=\zeta^q_{22}=\zetaqll,\qquad
\zeta^q_{33}=\zetaq33,
\]
\[
\zeta^\ell_{22}=\zetal22,\qquad
\zeta^\ell_{23}=\zetal23,\qquad
\zeta^\ell_{32}=\zetal23^*,\qquad
\zeta^\ell_{33}=\zetal33,
\]
\[
\zeta^u_{11}=\zeta^u_{22}=\zetaRull,\qquad
\zeta^u_{33}=\zetaRu33,
\]
\[
\zeta^d_{11}=\zeta^d_{22}=\zetaRdll,\qquad
\zeta^d_{33}=\zetaRd33,
\]
\[
\zeta^e_{22}=\zetaRe22,\qquad
\zeta^e_{33}=\zetaRe33.
\]
The \(\zeta\) matrices are Hermitian, with all undeclared off-diagonal entries zero.

### `LGpKin`

\[
\mathcal L_{\texttt{LGpKin}}
=
-\frac14\,G'^{A}_{\mu\nu}G'^{A\,\mu\nu}.
\]

### `LGpF`

\[
\mathcal L_{\texttt{LGpF}}
=
g_{G'}\,G'^A_\mu
\left[
\kappa^q_{ij} V_{ki}V^*_{nj}\,
\bar u_k^a (T^A)^a{}_{b}\gamma^\mu P_L u_n^b
+
\kappa^q_{ij}\,
\bar d_i^a (T^A)^a{}_{b}\gamma^\mu P_L d_j^b
\right.
\]
\[
\left.
+
\kappa^u_{ij}\,
\bar u_i^a (T^A)^a{}_{b}\gamma^\mu P_R u_j^b
+
\kappa^d_{ij}\,
\bar d_i^a (T^A)^a{}_{b}\gamma^\mu P_R d_j^b
\right].
\]

The nonzero internal entries are
\[
\kappa^q_{11}=\kappa^q_{22}=\kappaqll,\qquad
\kappa^q_{33}=\kappaq33,
\]
\[
\kappa^u_{11}=\kappa^u_{22}=\kappaRull,\qquad
\kappa^u_{33}=\kappaRu33,
\]
\[
\kappa^d_{11}=\kappa^d_{22}=\kappaRdll,\qquad
\kappa^d_{33}=\kappaRd33.
\]
The \(\kappa\) matrices are Hermitian and flavor diagonal as declared.

### `LGpG`

\[
\mathcal L_{\texttt{LGpG}}
=
\frac12\,\kappa_{G'}\,
G'^{A}_{\mu\nu}G^{A\,\mu\nu}
+
g_s\tilde\kappa_{G'}\,
f^{ABC}G'^A_\mu G'^B_\nu G^{C\,\mu\nu}.
\]

### `LLeptoQuark`

\[
\mathcal L_{\texttt{LLeptoQuark}}
=
\mathcal L_{\texttt{LVLQKin}}
+\mathcal L_{\texttt{LVLQF}}
+\mathcal L_{\texttt{HC[LVLQF]}}
+\mathcal L_{\texttt{LVLQG}}
+\mathcal L_{\texttt{LZpF}}
+\mathcal L_{\texttt{LGpKin}}
+\mathcal L_{\texttt{LGpF}}
+\mathcal L_{\texttt{LGpG}}.
\]

No explicit mass terms for the new vectors are written in `LLeptoQuark`, although masses are assigned in the particle-class declarations.

## Field Table

| `.fr` class | Symbol | Spin | SU(3) | SU(2) | \(U(1)_Y\) / charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| `VLQ` | \(U_\mu^a\) | 1 | fundamental \(\mathbf 3\) | singlet \(\mathbf 1\) | \(Y=2/3,\ Q=2/3\) | no | `MVLQ = 3000.` |
| `U` | \(U_\mu^a\) | 1 | fundamental \(\mathbf 3\) | singlet \(\mathbf 1\) | \(Y=2/3,\ Q=2/3\) | no | unphysical alias of `VLQ` |
| `Zp` | \(Z'_\mu\) | 1 | singlet \(\mathbf 1\) | singlet \(\mathbf 1\) | \(Y=0,\ Q=0\) | yes | `MZp = 3000.` |
| `Gp` | \(G'^A_\mu\) | 1 | adjoint \(\mathbf 8\) | singlet \(\mathbf 1\) | \(Y=0,\ Q=0\) | yes | `MGp = 4000.` |

`VLQ` also carries `LeptonNumber -> -1` in the file.

## External Parameters

| Parameter | Value | Multiplies | Physical meaning |
|---|---:|---|---|
| `gU` | `3.0` | `LVLQF` | Overall vector leptoquark coupling strength. |
| `betaL33` | `1.0` | \(\beta^L_{33}\) in `LVLQF` | Left-handed third-generation quark-lepton coupling. |
| `betaRd33` | `1.0` | \(\beta^{Rd}_{33}\) in `LVLQF` | Right-handed \(b_R\)-\(\tau_R\) coupling. |
| `betaL23` | `0.0` | \(\beta^L_{23}\) and \(\beta^L_{13}\) via CKM ratio | Left-handed second-quark-generation to third-lepton-generation coupling. |
| `betaL32` | `0.0` | \(\beta^L_{32}\) | Left-handed third-quark-generation to second-lepton-generation coupling. |
| `kappaU` | `0.0` | \(U^\dagger U G_{\mu\nu}\) term in `LVLQG` | Anomalous chromomagnetic-type vector leptoquark coupling parameter. |
| `kappaUtilde` | `0.0` | \(U^\dagger U B_{\mu\nu}\) term in `LVLQG` | Anomalous hypercharge field-strength coupling parameter. |
| `gZp` | `3.0` | `LZpF` | Overall neutral vector \(Z'\) coupling strength. |
| `zetaq33` | `1.0` | \(\zeta^q_{33}\) | \(Z'\) coupling to third-generation left-handed quark doublet current. |
| `zetal33` | `1.0` | \(\zeta^\ell_{33}\) | \(Z'\) coupling to third-generation left-handed lepton doublet current. |
| `zetaRu33` | `1.0` | \(\zeta^u_{33}\) | \(Z'\) coupling to \(t_R\) current. |
| `zetaRd33` | `1.0` | \(\zeta^d_{33}\) | \(Z'\) coupling to \(b_R\) current. |
| `zetaRe33` | `1.0` | \(\zeta^e_{33}\) | \(Z'\) coupling to \(\tau_R\) current. |
| `zetaqll` | `0.0` | \(\zeta^q_{11},\zeta^q_{22}\) | \(Z'\) coupling to first- and second-generation left-handed quark doublet currents. |
| `zetal22` | `0.0` | \(\zeta^\ell_{22}\) | \(Z'\) coupling to second-generation left-handed lepton doublet current. |
| `zetal23` | `0.0` | \(\zeta^\ell_{23},\zeta^\ell_{32}\) | Flavor-changing \(Z'\) coupling between second- and third-generation left-handed lepton doublets. |
| `zetaRull` | `0.0` | \(\zeta^u_{11},\zeta^u_{22}\) | \(Z'\) coupling to \(u_R,c_R\) currents. |
| `zetaRdll` | `0.0` | \(\zeta^d_{11},\zeta^d_{22}\) | \(Z'\) coupling to \(d_R,s_R\) currents. |
| `zetaRe22` | `0.0` | \(\zeta^e_{22}\) | \(Z'\) coupling to \(\mu_R\) current. |
| `gGp` | `3.0` | `LGpF` | Overall color-octet vector \(G'\) coupling strength. |
| `kappaq33` | `1.0` | \(\kappa^q_{33}\) | \(G'\) coupling to third-generation left-handed quark doublet current. |
| `kappaRu33` | `1.0` | \(\kappa^u_{33}\) | \(G'\) coupling to \(t_R\) current. |
| `kappaRd33` | `1.0` | \(\kappa^d_{33}\) | \(G'\) coupling to \(b_R\) current. |
| `kappaqll` | `0.0` | \(\kappa^q_{11},\kappa^q_{22}\) | \(G'\) coupling to first- and second-generation left-handed quark doublet currents. |
| `kappaRull` | `0.0` | \(\kappa^u_{11},\kappa^u_{22}\) | \(G'\) coupling to \(u_R,c_R\) currents. |
| `kappaRdll` | `0.0` | \(\kappa^d_{11},\kappa^d_{22}\) | \(G'\) coupling to \(d_R,s_R\) currents. |
| `kappaG1` | `0.0` | \(G'_{\mu\nu}G^{\mu\nu}\) in `LGpG` | Kinetic or field-strength mixing between the color-octet vector and the gluon. |
| `kappaG2` | `0.0` | \(f^{ABC}G'^A_\mu G'^B_\nu G^{C\mu\nu}\) in `LGpG` | Anomalous two-\(G'\)-one-gluon field-strength coupling. |

## Physics Summary

The file encodes a model with three new spin-1 states: a complex color-triplet, electroweak-singlet vector leptoquark \(U_\mu\) with charge \(2/3\), a neutral color-singlet vector \(Z'_\mu\), and a neutral color-octet vector \(G'^A_\mu\). The leptoquark couples quark-lepton currents with specified left- and right-handed flavor structures, while the \(Z'\) couples to quark and lepton neutral currents and the \(G'\) couples to color-octet quark currents plus possible gluonic field-strength interactions.

It mediates semileptonic quark-lepton transitions through \(U_\mu\), neutral-current dilepton and dijet processes through \(Z'\), and colored dijet or heavy-quark production processes through \(G'\), with CKM rotations explicitly present in the up-type left-handed quark currents.