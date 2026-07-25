# Reverse-check review package — `LeptoQuark_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `LeptoQuark/model/LeptoQuark_gen.fr` |
| original model name | `LeptoQuark_gen` (hidden from the agent) |
| paper | LeptoQuark/text/1901.10480.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LVLQKin` (`:=`)

```mathematica
Block[{mu,nu,cc1}, -1/2*(DC[Ubar[mu,cc1],nu] - DC[Ubar[nu,cc1],mu])*(DC[U[mu,cc1],nu] - DC[U[nu,cc1],mu])]
```

### `LVLQF` (`:=`)

```mathematica
Block[{ff1,ff2,ff3,s1,s2,s3,cc1,mu}, gU/Sqrt[2]*VLQ[mu,cc1]*(betaL[ff1,ff2]*newCKM[ff3,ff1]*uqbar[s1,ff3,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*vl[s3,ff2] + betaL[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*l[s3,ff2] + betaRd[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjP[s2,s3]*l[s3,ff2])]
```

### `LVLQG` (`:=`)

```mathematica
Block[{cc1,cc2,aa1,mu,nu}, -I*gs*(1 - kappaU)*Ubar[mu,cc1]*T[aa1,cc1,cc2]*U[nu,cc2]*FS[G,mu,nu,aa1] - I*2/3*g1*(1 - kappaUtilde)*Ubar[mu,cc1]*U[nu,cc1]*FS[B,mu,nu]]
```

### `LZpF` (`:=`)

```mathematica
Block[{ff1,ff2,ff3,ff4,s1,s2,s3,mu,cc1}, gZp/(2*Sqrt[6])*Zp[mu]*(zetaq[ff1,ff2]*newCKM[ff3,ff1]*uqbar[s1,ff3,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*Conjugate[newCKM[ff4,ff2]]*uq[s3,ff4,cc1] + zetaq[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjM[s2,s3]*dq[s3,ff2,cc1] - 3*zetal[ff1,ff2]*lbar[s1,ff1]*Ga[mu,s1,s2]*ProjM[s2,s3]*l[s3,ff2] - 3*zetal[ff1,ff2]*vlbar[s1,ff1]*Ga[mu,s1,s2]*ProjM[s2,s3]*vl[s3,ff2] + zetaRu[ff1,ff2]*uqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjP[s2,s3]*uq[s3,ff2,cc1] + zetaRd[ff1,ff2]*dqbar[s1,ff1,cc1]*Ga[mu,s1,s2]*ProjP[s2,s3]*dq[s3,ff2,cc1] - 3*zetaRe[ff1,ff2]*lbar[s1,ff1]*Ga[mu,s1,s2]*ProjP[s2,s3]*l[s3,ff2])]
```

### `LGpKin` (`:=`)

```mathematica
Block[{mu,nu,aa1}, -1/4*(DC[Gp[mu,aa1],nu] - DC[Gp[nu,aa1],mu])*(DC[Gp[mu,aa1],nu] - DC[Gp[nu,aa1],mu])]
```

### `LGpF` (`:=`)

```mathematica
Block[{ff1,ff2,ff3,ff4,s1,s2,s3,aa1,cc1,cc2,mu}, gGp*Gp[mu,aa1]*(kappaL[ff1,ff2]*newCKM[ff3,ff1]*uqbar[s1,ff3,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjM[s2,s3]*Conjugate[newCKM[ff4,ff2]]*uq[s3,ff4,cc2] + kappaL[ff1,ff2]*dqbar[s1,ff1,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjM[s2,s3]*dq[s3,ff2,cc2] + kappaRu[ff1,ff2]*uqbar[s1,ff1,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjP[s2,s3]*uq[s3,ff2,cc2] + kappaRd[ff1,ff2]*dqbar[s1,ff1,cc1]*T[aa1,cc1,cc2]*Ga[mu,s1,s2]*ProjP[s2,s3]*dq[s3,ff2,cc2])]
```

### `LGpG` (`:=`)

```mathematica
Block[{aa1,aa2,aa3,mu,nu}, 1/2*kappaG1*(DC[Gp[nu,aa1],mu] - DC[Gp[mu,aa1],nu])*FS[G,mu,nu,aa1] + gs*kappaG2*f[aa1,aa2,aa3]*Gp[mu,aa1]*Gp[nu,aa2]*FS[G,mu,nu,aa3]]
```

### `LLeptoQuark` (`:=`)

```mathematica
LVLQKin + LVLQF + HC[LVLQF] + LVLQG + LZpF + LGpKin + LGpF + LGpG
```

## Blank-slate reconstruction

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

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Locations

The model is defined mainly in **Section 3, “Phenomenological Lagrangian”**.

Key references:

- **Eq. (1)**: initial effective \(U_1\) fermion-current interaction and field representation \(U_1 \sim (3,1,2/3)\).
- **Section 2 / Introduction**: companion vectors \(Z' \sim (1,1,0)\), \(G' \sim (8,1,0)\).
- **Eqs. (9), (10), (11)**: full phenomenological Lagrangian for \(U_1\), \(Z'\), and \(G'\).
- **Eq. (12)**: flavor basis choice,
  \[
  q_L^i=\begin{pmatrix}V^*_{ji}u_L^j\\ d_L^i\end{pmatrix},\qquad
  \ell_L^i=\begin{pmatrix}\nu_L^i\\ e_L^i\end{pmatrix}.
  \]
- **Eq. (13)**: benchmark flavor textures for \(\beta\), \(\zeta\), and \(\kappa\), including
  \[
  \beta_L^{13}=\frac{V_{td}^*}{V_{ts}^*}\beta_L^{23}.
  \]

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field content: \(U_1\sim(3,1,2/3)\), \(Z'\sim(1,1,0)\), \(G'\sim(8,1,0)\) (Intro, Sec. 2, Sec. 3) | Field table lists `VLQ` as color triplet, weak singlet, \(Y=2/3\); `Zp` as singlet; `Gp` as color octet | agree | Physics representations and charges match. |
| \(U_1\) kinetic term: \(-\frac12 U^\dagger_{1\mu\nu}U_1^{\mu\nu}\) (Eq. 9) | `LVLQKin`: \(-\frac12\bar U_{\mu\nu}^aU^{a\mu\nu}\) | agree | Same kinetic structure for a complex vector triplet. |
| \(U_1\) mass term: \(+M_U^2 U^\dagger_{1\mu}U_1^\mu\) (Eq. 9) | No explicit mass term in `LLeptoQuark`; mass only listed in particle declarations | missing-in-reconstruction | The paper includes the mass term in the Lagrangian. The reconstruction explicitly says no mass terms are written in `LLeptoQuark`. |
| \(U_1\)-gluon non-minimal term: \(-ig_s(1-\kappa_U)U^\dagger_{1\mu}T^aU_{1\nu}G^{a\mu\nu}\) (Eq. 9) | `LVLQG`: \(-ig_s(1-\kappa_U)\bar U_\mu T^AU_\nu G^{A\mu\nu}\) | agree | Coefficient, color generator, and Lorentz structure match. |
| \(U_1\)-hypercharge non-minimal term: \(-ig_Y\frac23(1-\tilde\kappa_U)U^\dagger_{1\mu}U_{1\nu}B^{\mu\nu}\) (Eq. 9) | `LVLQG`: \(-i\frac23g_1(1-\tilde\kappa_U)\bar U_\mu U_\nu B^{\mu\nu}\) | agree | Same structure; \(g_1\) vs \(g_Y\) is notation. |
| \(U_1\) LH fermion coupling: \(\frac{g_U}{\sqrt2}U_1^\mu\beta_L^{ij}\bar q_L^i\gamma_\mu\ell_L^j+\mathrm{h.c.}\) (Eq. 9) | `LVLQF` plus `HC[LVLQF]`, expanded into \(V_{ki}\bar u_k\gamma^\mu P_L\nu_j+\bar d_i\gamma^\mu P_L\ell_j\) | agree | Expansion agrees with Eq. (12): the barred up-quark component carries \(V_{ki}\). |
| \(U_1\) RH fermion coupling: \(\frac{g_U}{\sqrt2}U_1^\mu\beta_R^{ij}\bar d_R^i\gamma_\mu e_R^j+\mathrm{h.c.}\) (Eq. 9) | `LVLQF`: \(\frac{g_U}{\sqrt2}U_\mu\beta^{Rd}_{ij}\bar d_i\gamma^\mu P_R\ell_j\) plus H.c. | agree | Same physics; reconstruction labels the matrix \(\beta^{Rd}\) instead of \(\beta_R\). |
| \(U_1\) flavor texture: \(\beta_L=\begin{pmatrix}0&0&\beta_L^{13}\\0&0&\beta_L^{23}\\0&\beta_L^{32}&\beta_L^{33}\end{pmatrix}\), \(\beta_R=\mathrm{diag}(0,0,\beta_R^{33})\) (Eq. 13) | Nonzero \(\beta^L_{13},\beta^L_{23},\beta^L_{32},\beta^L_{33}\); \(\beta^{Rd}_{33}\) only | agree | Matches the texture. |
| Spurion relation: \(\beta_L^{13}=V_{td}^*/V_{ts}^*\,\beta_L^{23}\) (below Eq. 13) | \(\beta^L_{13}=(V_{31}/V_{32})^*\beta^L_{23}\) | agree | Same relation if \(V_{31}=V_{td}\), \(V_{32}=V_{ts}\). |
| \(Z'\) kinetic term: \(-\frac14Z'_{\mu\nu}Z'^{\mu\nu}\) (Eq. 10) | No `LZpKin` term included in reconstructed `LLeptoQuark` | missing-in-reconstruction | This is a real omission relative to the paper Lagrangian. |
| \(Z'\) mass term: \(+\frac12M_{Z'}^2Z'_\mu Z'^\mu\) (Eq. 10) | No explicit mass term in `LLeptoQuark`; mass only listed in particle declarations | missing-in-reconstruction | The paper includes the mass term in the Lagrangian. |
| \(Z'\) LH quark coupling: \(\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_q^{ij}\bar q_L^i\gamma^\mu q_L^j\) (Eq. 10) | `LZpF`: up-sector \(V_{ki}V^*_{nj}\bar u_k\gamma^\mu P_Lu_n\) and down-sector \(\bar d_i\gamma^\mu P_Ld_j\) | agree | Correct expansion using Eq. (12). |
| \(Z'\) RH up coupling: \(\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_u^{ij}\bar u_R^i\gamma^\mu u_R^j\) (Eq. 10) | `LZpF`: \(\zeta^u_{ij}\bar u_i\gamma^\mu P_Ru_j\) | agree | Same chirality and coefficient. |
| \(Z'\) RH down coupling: \(\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_d^{ij}\bar d_R^i\gamma^\mu d_R^j\) (Eq. 10) | `LZpF`: \(\zeta^d_{ij}\bar d_i\gamma^\mu P_Rd_j\) | agree | Same chirality and coefficient. |
| \(Z'\) LH lepton coupling: \(-3\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_\ell^{ij}\bar\ell_L^i\gamma^\mu\ell_L^j\) (Eq. 10) | `LZpF`: separate \(-3\zeta^\ell_{ij}\bar\ell_iP_L\ell_j\) and \(-3\zeta^\ell_{ij}\bar\nu_iP_L\nu_j\) | agree | Correct doublet expansion. |
| \(Z'\) RH charged-lepton coupling: \(-3\frac{g_{Z'}}{2\sqrt6}Z'_\mu\zeta_e^{ij}\bar e_R^i\gamma^\mu e_R^j\) (Eq. 10) | `LZpF`: \(-3\zeta^e_{ij}\bar\ell_i\gamma^\mu P_R\ell_j\) | agree | Same physics; reconstruction uses \(\ell\) for charged leptons. |
| \(Z'\) flavor textures: \(\zeta_\ell\), \(\zeta_e\), \(\zeta_Q=\mathrm{diag}(\zeta_Q^{ll},\zeta_Q^{ll},\zeta_Q^{33})\) (Eq. 13) | Nonzero \(\zeta^\ell_{22},\zeta^\ell_{23},\zeta^\ell_{32},\zeta^\ell_{33}\), \(\zeta^e_{22},\zeta^e_{33}\), diagonal light/third quark entries | agree | Matches Eq. (13), including Hermitian \(\zeta^\ell_{32}=(\zeta^\ell_{23})^*\). |
| \(G'\) kinetic term: \(-\frac14G'^a_{\mu\nu}G'^{a\mu\nu}\) (Eq. 11) | `LGpKin`: \(-\frac14G'^A_{\mu\nu}G'^{A\mu\nu}\) | agree | Same kinetic structure. |
| \(G'\) mass term: \(+\frac12M_{G'}^2G'^a_\mu G'^{a\mu}\) (Eq. 11) | No explicit mass term in `LLeptoQuark`; mass only listed in particle declarations | missing-in-reconstruction | The paper includes the mass term in the Lagrangian. |
| \(G'\)-gluon field-strength mixing: \(+\frac12\kappa_{G'}G'^a_{\mu\nu}G^{a\mu\nu}\) (Eq. 11) | `LGpG`: \(\frac12\kappa_{G'}G'^A_{\mu\nu}G^{A\mu\nu}\) | agree | Same coefficient and structure. |
| \(G'G'G\) non-minimal term: \(+g_s\tilde\kappa_{G'}f^{abc}G'^a_\mu G'^b_\nu G^{c\mu\nu}\) (Eq. 11) | `LGpG`: \(g_s\tilde\kappa_{G'}f^{ABC}G'^A_\mu G'^B_\nu G^{C\mu\nu}\) | agree | Same structure. |
| \(G'\) LH quark coupling: \(g_{G'}G'^a_\mu\kappa_q^{ij}\bar q_L^iT^a\gamma^\mu q_L^j\) (Eq. 11) | `LGpF`: up-sector \(V_{ki}V^*_{nj}\bar u_kT^A\gamma^\mu P_Lu_n\) and down-sector \(\bar d_iT^A\gamma^\mu P_Ld_j\) | agree | Correct expansion using Eq. (12). |
| \(G'\) RH up coupling: \(g_{G'}G'^a_\mu\kappa_u^{ij}\bar u_R^iT^a\gamma^\mu u_R^j\) (Eq. 11) | `LGpF`: \(\kappa^u_{ij}\bar u_iT^A\gamma^\mu P_Ru_j\) | agree | Same chirality, color generator, and coefficient. |
| \(G'\) RH down coupling: \(g_{G'}G'^a_\mu\kappa_d^{ij}\bar d_R^iT^a\gamma^\mu d_R^j\) (Eq. 11) | `LGpF`: \(\kappa^d_{ij}\bar d_iT^A\gamma^\mu P_Rd_j\) | agree | Same chirality, color generator, and coefficient. |
| \(G'\) flavor textures: \(\kappa_Q=\mathrm{diag}(\kappa_Q^{ll},\kappa_Q^{ll},\kappa_Q^{33})\), \(Q=q,u,d\) (Eq. 13) | Nonzero diagonal light-pair and third-generation entries for \(\kappa^q,\kappa^u,\kappa^d\) | agree | Matches Eq. (13). |
| Paper neglects Higgs couplings to \(Z'\) and other UV-completion-dependent interactions (Sec. 3) | Reconstruction contains no Higgs couplings or extra UV-sector interactions | agree | Consistent with the stated phenomenological setup. |
| Gauge-model limit: \(\kappa_U=\tilde\kappa_U=\kappa_{G'}=\tilde\kappa_{G'}=0\); later analyses take \(\kappa_{G'}=0\) (below Eq. 11) | External parameters default these anomalous couplings to zero | agree | The reconstruction captures the implementation benchmark, not just the symbolic Lagrangian. |
| `VLQ` carries `LeptonNumber -> -1` | No explicit lepton-number assignment for \(U_1\) in the paper Lagrangian | extra-in-reconstruction | This is an implementation bookkeeping convention; it is not an additional interaction. |
| `U` listed as an unphysical alias of `VLQ` | No separate alias field in the paper | extra-in-reconstruction | Cosmetic implementation detail, not a distinct physical state. |

## Disagreements and Human Checks

1. **Missing \(U_1\) mass term** — severity: **substantive**.  
   A human should check whether the implementation supplies the vector mass solely through particle declarations in a way that FeynRules/UFO treats equivalently, or whether the Lagrangian object itself is incomplete.

2. **Missing \(Z'\) kinetic term** — severity: **substantive**.  
   A human should check whether a separate `LZpKin` exists outside the reconstructed `LLeptoQuark` sum or whether the reconstruction/implementation accidentally omits the propagating \(Z'\) kinetic term.

3. **Missing \(Z'\) mass term** — severity: **substantive**.  
   A human should check whether the \(Z'\) mass is generated from particle metadata only, or whether the Lagrangian used for model export lacks the paper’s \(\frac12M_{Z'}^2Z'_\mu Z'^\mu\) term.

4. **Missing \(G'\) mass term** — severity: **substantive**.  
   A human should check whether the coloron mass is included elsewhere in the implementation or only assigned as a particle property.

5. **Implementation-only lepton-number assignment for `VLQ`** — severity: **cosmetic**.  
   A human should check that this bookkeeping charge does not enforce unintended selection rules or conflict with the intended \(U_1\) interactions.

6. **Implementation-only unphysical alias `U` for `VLQ`** — severity: **cosmetic**.  
   A human should check that the alias is not exported as an additional physical vector state.

## Overall Assessment

The reconstruction captures the paper’s main physics content very closely for the interaction terms: field representations, chiral structures, CKM rotations, color factors, anomalous gauge-field couplings, and the benchmark flavor textures all match Eqs. (9)–(13) up to notation. The important gaps are in the explicit propagator-sector terms: the paper writes mass terms for all three new vectors and a kinetic term for \(Z'\), while the reconstructed summed Lagrangian omits them, even though masses are listed separately in the field table. The main review question is therefore not the fermionic or gauge-interaction structure, which appears consistent, but whether the implementation supplies the omitted kinetic/mass pieces elsewhere in a form equivalent to the paper’s Lagrangian.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 42 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

