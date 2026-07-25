# Reverse-check review package — `VLQ_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `VLQ/model/VLQ_gen.fr` |
| original model name | `VLQ_gen` (hidden from the agent) |
| paper | VLQ/text/hep-ph_0607115.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LyTP` (`=`)

```mathematica
-lamT (bar[Q3L].Phi.tR) - lamTp (bar[Q3L].Phi.tpR) + HC[-lamT (bar[Q3L].Phi.tR) - lamTp (bar[Q3L].Phi.tpR)]
```

### `LDTP` (`=`)

```mathematica
-MT0 bar[tpL].tpR - MTmix bar[tpL].tR + HC[-MT0 bar[tpL].tpR - MTmix bar[tpL].tR]
```

### `LWTP` (`=`)

```mathematica
-(gw/Sqrt[2]) (cT CKM[3, ff] bar[t].Ga[mu].ProjM.dq[ff] + sT CKM[3, ff] bar[tp].Ga[mu].ProjM.dq[ff]) W[mu] + HC[-(gw/Sqrt[2]) (cT CKM[3, ff] bar[t].Ga[mu].ProjM.dq[ff] + sT CKM[3, ff] bar[tp].Ga[mu].ProjM.dq[ff]) W[mu]]
```

### `LZTP` (`=`)

```mathematica
-(gw/(2 cw)) (cT^2 bar[t].Ga[mu].ProjM.t + sT cT bar[t].Ga[mu].ProjM.tp + sT cT bar[tp].Ga[mu].ProjM.t + sT^2 bar[tp].Ga[mu].ProjM.tp) Z[mu]
```

### `LHTP` (`=`)

```mathematica
(gw/(2 MW)) ((cT^2 MT bar[t].ProjP.t + sT cT MTP bar[t].ProjP.tp + sT cT MT bar[tp].ProjP.t + sT^2 MTP bar[tp].ProjP.tp) H + HC[(cT^2 MT bar[t].ProjP.t + sT cT MTP bar[t].ProjP.tp + sT cT MT bar[tp].ProjP.t + sT^2 MTP bar[tp].ProjP.tp) H])
```

### `LyBP` (`=`)

```mathematica
-lamB (bar[Q3L].Phibar.bR) - lamBp (bar[Q3L].Phibar.bpR) + HC[-lamB (bar[Q3L].Phibar.bR) - lamBp (bar[Q3L].Phibar.bpR)]
```

### `LDBP` (`=`)

```mathematica
-MB0 bar[bpL].bpR - MBmix bar[bpL].bR + HC[-MB0 bar[bpL].bpR - MBmix bar[bpL].bR]
```

### `LWBP` (`=`)

```mathematica
-(gw/Sqrt[2]) (cB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.b + sB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.bp) W[mu] + HC[-(gw/Sqrt[2]) (cB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.b + sB CKM[ff,3] bar[uq[ff]].Ga[mu].ProjM.bp) W[mu]]
```

### `LZBP` (`=`)

```mathematica
-(gw/(2 cw)) (cB^2 bar[b].Ga[mu].ProjM.b + sB cB bar[b].Ga[mu].ProjM.bp + sB cB bar[bp].Ga[mu].ProjM.b + sB^2 bar[bp].Ga[mu].ProjM.bp) Z[mu]
```

### `L4CKM` (`=`)

```mathematica
-(gw/Sqrt[2]) ((cU4 CKM[3, ff] - sU4 sV4 CKM[2, ff] - sU4 cV4 sW4 CKM[1, ff]) bar[t].Ga[mu].ProjM.dq[ff] + (sU4 CKM[3, ff] + cU4 sV4 CKM[2, ff] + cU4 cV4 sW4 CKM[1, ff]) bar[t4].Ga[mu].ProjM.dq[ff] + (cV4 CKM[2, ff] - sV4 sW4 CKM[1, ff]) bar[c].Ga[mu].ProjM.dq[ff] + cW4 CKM[1, ff] bar[u].Ga[mu].ProjM.dq[ff]) W[mu] + HC[-(gw/Sqrt[2]) ((cU4 CKM[3, ff] - sU4 sV4 CKM[2, ff] - sU4 cV4 sW4 CKM[1, ff]) bar[t].Ga[mu].ProjM.dq[ff] + (sU4 CKM[3, ff] + cU4 sV4 CKM[2, ff] + cU4 cV4 sW4 CKM[1, ff]) bar[t4].Ga[mu].ProjM.dq[ff] + (cV4 CKM[2, ff] - sV4 sW4 CKM[1, ff]) bar[c].Ga[mu].ProjM.dq[ff] + cW4 CKM[1, ff] bar[u].Ga[mu].ProjM.dq[ff]) W[mu]]
```

### `L4Mass` (`=`)

```mathematica
-MT4 bar[t4].t4 - MB4 bar[b4].b4 - MN4 bar[n4].n4 - ME4 bar[e4].e4
```

## Blank-slate reconstruction

# Reconstruction from `sanitized.fr`

## Conventions

The file uses
\[
P_L \equiv \texttt{ProjM}=\frac{1-\gamma^5}{2},\qquad
P_R \equiv \texttt{ProjP}=\frac{1+\gamma^5}{2}.
\]

Hermitian conjugates are written as `HC[...]`. Charge conjugation `CC`, covariant derivatives `DC`, and field strengths `FS` do not appear in this file.

Repeated flavor index \(f\) is summed over the three SM generations. I write
\[
V_{ij}\equiv \texttt{CKM[i,j]},\qquad d_f\equiv \texttt{dq[ff]}.
\]

The file uses `W[mu]` in charged-current terms of the form \(\bar u\,\gamma^\mu P_L d\,W_\mu\); by electric charge conservation this is \(W_\mu^+\), with the hermitian conjugate giving the \(W_\mu^-\) interaction.

For the electroweak-doublet Yukawa contractions,
\[
Q_{3L}=\begin{pmatrix}t_L\\ b_L\end{pmatrix}.
\]
Gauge invariance of the written terms implies that `Phi` is the up-type Higgs doublet contraction, i.e. \(\tilde H=i\sigma^2 H^\ast\), while `Phibar` is the down-type Higgs doublet \(H\). The dot `.` denotes contraction of the \(SU(2)_L\) doublet index and color indices where present.

No explicit `DC[...]` kinetic terms are present. If canonical kinetic terms are assumed for a declared fermion \(\psi\), the gauge content follows from the declared color and charges:
\[
D_\mu\psi
=
\left[
\partial_\mu
+i g_s G_\mu^A T^A_{\mathbf 3}
+i e Q_\psi A_\mu
+i\frac{g_w}{c_w}\left(T^3_\psi-Q_\psi s_w^2\right)Z_\mu
+\text{charged }W^\pm\text{ terms if an }SU(2)_L\text{ multiplet is specified}
\right]\psi .
\]
In the actual class declarations here, no explicit \(SU(2)_L\) index is assigned to any new field.

## Lagrangian

### `LyTP`

\[
\boxed{
\mathcal L_{\texttt{LyTP}}
=
-\lambda_T\,\bar Q_{3L\,i}\,\tilde H^i\,t_R
-\lambda'_T\,\bar Q_{3L\,i}\,\tilde H^i\,t'_R
+\text{h.c.}
}
\]

Here \(t'\equiv\texttt{tp}\). Color indices are contracted between \(\bar Q_{3L}\) and \(t_R,t'_R\).

### `LDTP`

\[
\boxed{
\mathcal L_{\texttt{LDTP}}
=
-M_{T0}\,\bar t'_L t'_R
-M_{T\mathrm{mix}}\,\bar t'_L t_R
+\text{h.c.}
}
\]

### `LWTP`

\[
\boxed{
\mathcal L_{\texttt{LWTP}}
=
-\frac{g_w}{\sqrt2}
\left[
c_T\,V_{3f}\,\bar t\,\gamma^\mu P_L d_f
+s_T\,V_{3f}\,\bar t'\,\gamma^\mu P_L d_f
\right]W^+_\mu
+\text{h.c.}
}
\]

with
\[
s_T=\sin\theta_T,\qquad c_T=\cos\theta_T .
\]

### `LZTP`

\[
\boxed{
\mathcal L_{\texttt{LZTP}}
=
-\frac{g_w}{2c_w}
\left[
c_T^2\,\bar t\gamma^\mu P_L t
+s_Tc_T\,\bar t\gamma^\mu P_L t'
+s_Tc_T\,\bar t'\gamma^\mu P_L t
+s_T^2\,\bar t'\gamma^\mu P_L t'
\right]Z_\mu
}
\]

### `LHTP`

\[
\boxed{
\mathcal L_{\texttt{LHTP}}
=
\frac{g_w}{2M_W}
\left[
c_T^2 M_T\,\bar t P_R t
+s_Tc_T M_{T'}\,\bar t P_R t'
+s_Tc_T M_T\,\bar t' P_R t
+s_T^2 M_{T'}\,\bar t' P_R t'
\right]h
+\text{h.c.}
}
\]

Here \(h\equiv\texttt{H}\), \(M_T\equiv\texttt{MT}\), and \(M_{T'}\equiv\texttt{MTP}\).

### `LyBP`

\[
\boxed{
\mathcal L_{\texttt{LyBP}}
=
-\lambda_B\,\bar Q_{3L\,i}\,H^i\,b_R
-\lambda'_B\,\bar Q_{3L\,i}\,H^i\,b'_R
+\text{h.c.}
}
\]

Here \(b'\equiv\texttt{bp}\).

### `LDBP`

\[
\boxed{
\mathcal L_{\texttt{LDBP}}
=
-M_{B0}\,\bar b'_L b'_R
-M_{B\mathrm{mix}}\,\bar b'_L b_R
+\text{h.c.}
}
\]

### `LWBP`

\[
\boxed{
\mathcal L_{\texttt{LWBP}}
=
-\frac{g_w}{\sqrt2}
\left[
c_B\,V_{f3}\,\bar u_f\gamma^\mu P_L b
+s_B\,V_{f3}\,\bar u_f\gamma^\mu P_L b'
\right]W^+_\mu
+\text{h.c.}
}
\]

with
\[
s_B=\sin\theta_B,\qquad c_B=\cos\theta_B .
\]

### `LZBP`

\[
\boxed{
\mathcal L_{\texttt{LZBP}}
=
-\frac{g_w}{2c_w}
\left[
c_B^2\,\bar b\gamma^\mu P_L b
+s_Bc_B\,\bar b\gamma^\mu P_L b'
+s_Bc_B\,\bar b'\gamma^\mu P_L b
+s_B^2\,\bar b'\gamma^\mu P_L b'
\right]Z_\mu
}
\]

### `L4CKM`

\[
\boxed{
\begin{aligned}
\mathcal L_{\texttt{L4CKM}}
=
-\frac{g_w}{\sqrt2}
\Big[
&
\left(c_{U4}V_{3f}-s_{U4}s_{V4}V_{2f}-s_{U4}c_{V4}s_{W4}V_{1f}\right)
\bar t\gamma^\mu P_L d_f
\\
&+
\left(s_{U4}V_{3f}+c_{U4}s_{V4}V_{2f}+c_{U4}c_{V4}s_{W4}V_{1f}\right)
\bar t_4\gamma^\mu P_L d_f
\\
&+
\left(c_{V4}V_{2f}-s_{V4}s_{W4}V_{1f}\right)
\bar c\gamma^\mu P_L d_f
\\
&+
c_{W4}V_{1f}\,\bar u\gamma^\mu P_L d_f
\Big]W^+_\mu
+\text{h.c.}
\end{aligned}
}
\]

where
\[
s_{U4}=\sin\theta_{U4},\quad c_{U4}=\cos\theta_{U4},\quad
s_{V4}=\sin\theta_{V4},\quad c_{V4}=\cos\theta_{V4},\quad
s_{W4}=\sin\theta_{W4},\quad c_{W4}=\cos\theta_{W4}.
\]

### `L4Mass`

\[
\boxed{
\mathcal L_{\texttt{L4Mass}}
=
-M_{T4}\,\bar t_4 t_4
-M_{B4}\,\bar b_4 b_4
-M_{N4}\,\bar n_4 n_4
-M_{E4}\,\bar e_4 e_4
}
\]

## Field table

| Class | Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(Q\) | \(Y\) | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `F[100]` | `tp` | \(1/2\) Dirac fermion | \(\mathbf 3\) | not declared | \(+2/3\) | \(+2/3\) | no | `MTP = 600.` |
| `F[101]` | `bp` | \(1/2\) Dirac fermion | \(\mathbf 3\) | not declared | \(-1/3\) | \(-1/3\) | no | `MBP = 600.` |
| `F[102]` | `t4` | \(1/2\) Dirac fermion | \(\mathbf 3\) | not declared | \(+2/3\) | \(+1/6\) | no | `MT4 = 600.` |
| `F[103]` | `b4` | \(1/2\) Dirac fermion | \(\mathbf 3\) | not declared | \(-1/3\) | \(+1/6\) | no | `MB4 = 600.` |
| `F[104]` | `n4` | \(1/2\) Dirac fermion | \(\mathbf 1\) | not declared | \(0\) | \(-1/2\) | no | `MN4 = 100.` |
| `F[105]` | `e4` | \(1/2\) Dirac fermion | \(\mathbf 1\) | not declared | \(-1\) | \(-1/2\) | no | `ME4 = 100.` |

## External parameters

| Parameter | Value | Appears in | Meaning |
|---|---:|---|---|
| `thT` | `0.1` | `LWTP`, `LZTP`, `LHTP` through \(s_T,c_T\) | Left-chiral mixing angle between the SM top and `tp` in charged, neutral, and Higgs interactions. |
| `lamT` | `1.` | `LyTP` | Yukawa coupling multiplying \(\bar Q_{3L}\tilde H t_R\). |
| `lamTp` | `1.` | `LyTP` | Yukawa coupling multiplying \(\bar Q_{3L}\tilde H t'_R\). |
| `MT0` | `600.` | `LDTP` | Vectorlike Dirac mass parameter for `tp`. |
| `MTmix` | `0.` | `LDTP` | Mass-mixing parameter multiplying \(\bar t'_L t_R\). |
| `thB` | `0.01` | `LWBP`, `LZBP` through \(s_B,c_B\) | Left-chiral mixing angle between the SM bottom and `bp` in charged and neutral interactions. |
| `lamB` | `1.` | `LyBP` | Yukawa coupling multiplying \(\bar Q_{3L}H b_R\). |
| `lamBp` | `1.` | `LyBP` | Yukawa coupling multiplying \(\bar Q_{3L}H b'_R\). |
| `MB0` | `600.` | `LDBP` | Vectorlike Dirac mass parameter for `bp`. |
| `MBmix` | `0.` | `LDBP` | Mass-mixing parameter multiplying \(\bar b'_L b_R\). |
| `thU4` | `0.1` | `L4CKM` through \(s_{U4},c_{U4}\) | Mixing angle controlling the redistribution of charged-current couplings between \(t\) and \(t_4\). |
| `thV4` | `0.1` | `L4CKM` through \(s_{V4},c_{V4}\) | Mixing angle modifying charged-current couplings involving \(t,t_4,c\). |
| `thW4` | `0.` | `L4CKM` through \(s_{W4},c_{W4}\) | Mixing angle modifying charged-current couplings involving \(u,c,t,t_4\). |

## Physics summary

The file encodes an extension of the SM fermion sector with heavy Dirac quarks `tp` and `bp` that mix chirally with the top and bottom sectors, plus additional Dirac fermions `t4`, `b4`, `n4`, and `e4` with explicit Dirac masses. The interactions modify \(W^\pm\), \(Z\), and Higgs couplings of the third-generation quarks and introduce charged-current mixing between \(t_4\) and SM down-type quarks.

It mediates processes such as heavy-quark production and decay through \(t'\to Wd_f,Zt,ht\), \(b'\to Wu_f,Zb\), and charged-current production or decay involving \(t_4\) through the extended CKM-like structure.

## Paper cross-check

**Paper Locations**

The paper defines the vector-like top model in Sec. 2.1, “The case for a vector-like \(t'\) quark”: charged current Eq. (7), mixing rotation Eq. (8), rescaled CKM entries Eqs. (9)-(10), Yukawa terms Eq. (11), Dirac mass terms Eq. (12), neutral-current and Higgs FCNC structures Eqs. (14)-(16). It briefly comments on the analogous down-type vector-like \(b'\) model immediately after Eq. (16). The fourth-generation model is defined in Sec. 2.2, “The case for a fourth generation”: a unitary \(V_{4\times4}\) matrix with rotations Eq. (31), and entries Eqs. (32)-(35). The paper also notes anomaly cancellation requiring fourth-generation leptons near Sec. 2.2.1, after Eq. (42), but does not write their Lagrangian.

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---:|---|
| Vector-like \(t'\) field content: one \(Q=+2/3\) vector-like electroweak iso-singlet quark, Sec. 2.1 | `tp`: Dirac color triplet, \(Q=+2/3\), no explicit \(SU(2)_L\) index | agree | The absence of an \(SU(2)_L\) index is consistent with the paper’s iso-singlet \(t'\). |
| Charged current \(L_{W^\pm}=-g/\sqrt2[\bar u_L V\gamma^\mu d_L W_\mu^+ + h.c.]\), Eq. (7), with \(V_{ti}=V^{(0)}_{ti}\cos\theta\), \(V_{t'i}=V^{(0)}_{ti}\sin\theta\), Eqs. (9)-(10) | `LWTP`: \(-g_w/\sqrt2[c_T V_{3f}\bar t\gamma^\mu P_L d_f+s_TV_{3f}\bar t'\gamma^\mu P_Ld_f]W^+_\mu+h.c.\) | agree | Matches the \(t,t'\) rows of Eq. (7) after the rotation. The reconstruction omits unchanged \(u,c\) charged currents, which is acceptable if it is only listing non-SM or modified terms. |
| Left-handed \(t-t'\) rotation \(R_{34}(\theta)\), Eq. (8) | \(s_T=\sin\theta_T,\ c_T=\cos\theta_T\) in `LWTP`, `LZTP`, `LHTP` | agree | Same physical mixing structure. |
| Yukawa terms \(L_y(t')=\lambda (t^0,b^0)_L\Phi t_R^0+\lambda'(t^0,b^0)_L\Phi t_R^{\prime0}+h.c.\), Eq. (11) | `LyTP`: \(-\lambda_T\bar Q_{3L}\tilde H t_R-\lambda'_T\bar Q_{3L}\tilde H t'_R+h.c.\) | agree | Same gauge-invariant content for an up-type Yukawa, modulo sign and notation. The reconstruction’s \(\tilde H\) is the expected up-type contraction. |
| Dirac mass terms \(L_D(t')=M\bar t_L^{\prime0}t_R^{\prime0}+M'\bar t_L^{\prime0}t_R^0+h.c.\), Eq. (12) | `LDTP`: \(-M_{T0}\bar t'_Lt'_R-M_{Tmix}\bar t'_Lt_R+h.c.\) | agree | Same vector-like mass and mixing mass content; overall sign is a convention. |
| Neutral current \(L_{Z^0}= -g/(2c_w)\bar u_LVV^\dagger\gamma^\mu u_LZ^0_\mu\), Eq. (14), with \(VV^\dagger\) block in Eq. (16) | `LZTP`: \(-g_w/(2c_w)[c_T^2\bar tP_Lt+s_Tc_T\bar tP_Lt'+s_Tc_T\bar t'P_Lt+s_T^2\bar t'P_Lt']Z_\mu\) | agree | Matches the \(t,t'\) block of \(VV^\dagger\) in Eq. (16). |
| Higgs FCNC \(L_{H^0}=g/(2M_W)[\bar u_LVV^\dagger M_u u_R+h.c.]H^0\), Eq. (15), with \(M_u=\mathrm{diag}(m_u,m_c,m_t,m_{t'})\), Eq. (16) | `LHTP`: \(g_w/(2M_W)[c_T^2M_T\bar tP_Rt+s_Tc_TM_{T'}\bar tP_Rt'+s_Tc_TM_T\bar t'P_Rt+s_T^2M_{T'}\bar t'P_Rt']h+h.c.\) | agree | Correct mass appears by right-handed flavor column, as in \(VV^\dagger M_u\). |
| Down-type vector-like \(b'\) model: paper says only that the \(3\times4\) matrix is the transpose analogue of Eq. (6), with \(V_{tb}=V^{(0)}_{tb}\cos\theta_d\), immediately after Eq. (16) | `LyBP`, `LDBP`, `LWBP`, `LZBP` | extra-in-reconstruction | The paper mentions the analogous \(b'\) model but does not define its full Yukawa, mass, \(Z\), or Higgs Lagrangian. The reconstruction includes a full explicit down-type vector-like model. |
| Down-type vector-like Yukawa analogue, not explicitly written in paper | `LyBP`: \(-\lambda_B\bar Q_{3L}Hb_R-\lambda'_B\bar Q_{3L}Hb'_R+h.c.\) | extra-in-reconstruction | Plausible analogue of Eq. (11), but not a paper equation. |
| Down-type vector-like Dirac mass analogue, not explicitly written in paper | `LDBP`: \(-M_{B0}\bar b'_Lb'_R-M_{Bmix}\bar b'_Lb_R+h.c.\) | extra-in-reconstruction | Plausible analogue of Eq. (12), but not defined in the paper. |
| Down-type vector-like charged current transpose analogue after Eq. (16) | `LWBP`: \(-g_w/\sqrt2[c_BV_{f3}\bar u_f\gamma^\mu P_Lb+s_BV_{f3}\bar u_f\gamma^\mu P_Lb']W^+_\mu+h.c.\) | agree | This agrees with the stated transpose analogue if one treats the paper’s comment as defining the \(b'\) case. It is still extra relative to the paper’s main models. |
| Down-type vector-like neutral current analogue, not explicitly written in paper | `LZBP`: \(-g_w/(2c_w)[c_B^2\bar bP_Lb+s_Bc_B\bar bP_Lb'+s_Bc_B\bar b'P_Lb+s_B^2\bar b'P_Lb']Z_\mu\) | extra-in-reconstruction | Expected by analogy, but the paper does not write this term. |
| Fourth-generation model: unitary \(V_{4\times4}\), no tree-level hadronic \(Z^0\) FCNCs, Sec. 2.2 | `t4`, `b4`, `n4`, `e4` Dirac fields plus `L4CKM` | agree | The reconstruction captures the presence of extra up/down quarks and leptons, but its field-representation table is incomplete/problematic. |
| Fourth-generation CKM parametrization \(V_{4\times4}=R_{34}(\theta_u)R_{24}(\theta_v)R_{14}(\theta_w)\begin{pmatrix}V^{(0)}_{3\times3}&0\\0&1\end{pmatrix}\), Eq. (31) | `L4CKM` with \(s_{U4},s_{V4},s_{W4}\) and \(c_{U4},c_{V4},c_{W4}\) | agree | Same three-angle parametrization. |
| \(V_{ui}=c_wV^{(0)}_{ui}\), Eq. (32) | `L4CKM`: \(c_{W4}V_{1f}\bar u\gamma^\mu P_Ld_f\) | agree | Matches Eq. (32), identifying \(W4\leftrightarrow w\). |
| \(V_{ci}=c_vV^{(0)}_{ci}-s_vs_wV^{(0)}_{ui}\), Eq. (33) | `L4CKM`: \((c_{V4}V_{2f}-s_{V4}s_{W4}V_{1f})\bar c\gamma^\mu P_Ld_f\) | agree | Matches Eq. (33). |
| \(V_{ti}=c_uV^{(0)}_{ti}-s_us_vV^{(0)}_{ci}-s_uc_vs_wV^{(0)}_{ui}\), Eq. (34) | `L4CKM`: \((c_{U4}V_{3f}-s_{U4}s_{V4}V_{2f}-s_{U4}c_{V4}s_{W4}V_{1f})\bar t\gamma^\mu P_Ld_f\) | agree | Matches Eq. (34). |
| \(V_{t'i}=s_uV^{(0)}_{ti}+c_us_vV^{(0)}_{ci}+c_uc_vs_wV^{(0)}_{ui}\), Eq. (35) | `L4CKM`: \((s_{U4}V_{3f}+c_{U4}s_{V4}V_{2f}+c_{U4}c_{V4}s_{W4}V_{1f})\bar t_4\gamma^\mu P_Ld_f\) | agree | Matches Eq. (35), with reconstruction’s `t4` corresponding to the fourth-generation \(t'\). |
| Fourth-generation quark electroweak structure: a sequential fourth generation with \(t'_L,b'_L\) in an \(SU(2)_L\) doublet is implied by Sec. 2.2 and the unitary CKM construction | Reconstruction field table lists `t4` and `b4` as Dirac fields with no declared \(SU(2)_L\) rep; both have \(Y=+1/6\) | disagree | A sequential fourth generation requires chiral electroweak assignments: left-handed doublet \(Y=1/6\), right-handed singlets \(Y=2/3,-1/3\). A Dirac field with no \(SU(2)_L\) rep and a single listed \(Y=1/6\) is not a complete or gauge-covariant representation statement. |
| Fourth-generation lepton content required by anomaly cancellation, discussed after Eq. (42) | `n4`, `e4` Dirac fields with no declared \(SU(2)_L\) rep; both have \(Y=-1/2\) | disagree | The paper only states the need for leptons; a sequential generation would have a left-handed lepton doublet \(Y=-1/2\) plus right-handed singlets. The reconstruction’s single Dirac-field hypercharge assignment is incomplete. |
| Fourth-generation masses: paper uses \(m_{t'}\), discusses \(m_{b'}=m_{t'}\) near Eq. (40), but does not write gauge-invariant mass/Yukawa terms | `L4Mass`: \(-M_{T4}\bar t_4t_4-M_{B4}\bar b_4b_4-M_{N4}\bar n_4n_4-M_{E4}\bar e_4e_4\) | disagree | These look like explicit vector-like Dirac masses. For a chiral sequential fourth generation, bare Dirac masses are not \(SU(2)_L\times U(1)_Y\) invariant before EWSB; masses should arise from Higgs Yukawa terms, even if the phenomenology later treats physical masses as inputs. |
| Fourth-generation neutral-current structure: paper says tree-level hadronic \(Z^0\) FCNCs are forbidden in Sec. 2.2 | No `LZ4` FCNC term in reconstruction | agree | Absence of fourth-generation \(Z\)-FCNC terms is consistent with the paper. |
| Fourth-generation Yukawa sector for \(t',b'\) and leptons | No fourth-generation Higgs/Yukawa terms in reconstruction | missing-in-reconstruction | The paper does not explicitly write these terms, but a sequential fourth generation under the SM gauge group requires them for gauge-invariant masses. This is missing if the reconstruction is meant to be a Lagrangian-level model, rather than a phenomenological mass/CKM implementation. |

**Disagreements To Check**

| issue | severity | what a human should check |
|---|---:|---|
| The reconstruction includes a full vector-like \(b'\) model (`LyBP`, `LDBP`, `LWBP`, `LZBP`) while the paper only briefly comments on an analogous down-type case after Eq. (16). | substantive | Check whether the implementation intentionally bundled the paper’s aside as an additional optional model, or whether the target paper model should only include the vector-like up-type \(t'\) and fourth-generation cases. |
| The fourth-generation fields are listed as Dirac fields with no \(SU(2)_L\) representation, while the paper’s Sec. 2.2 implies a sequential chiral fourth generation. | substantive | Check the original implementation’s class declarations and gauge quantum numbers, especially whether left- and right-handed components are represented separately elsewhere. |
| `t4` and `b4` both have listed \(Y=+1/6\), and `n4`/`e4` both have listed \(Y=-1/2\), without separating left doublets from right singlets. | substantive | Verify whether the reconstruction confused doublet hypercharge with full Dirac-field hypercharge, since right-handed fourth-generation singlets need different hypercharges. |
| `L4Mass` uses explicit Dirac mass terms for fourth-generation fermions. | substantive | Check whether these are merely post-EWSB physical mass terms in a phenomenological implementation, or intended as gauge-invariant pre-EWSB Lagrangian terms; the latter would not match a chiral sequential fourth generation. |
| The reconstruction omits explicit fourth-generation Yukawa interactions. | substantive | Check whether the implementation only works in the mass basis for phenomenology, or whether a gauge-invariant Lagrangian reconstruction was expected. |
| Overall signs in the reconstructed Yukawa and Dirac mass terms differ from the signs printed in Eqs. (11)-(12). | convention | Check the implementation’s Lagrangian sign convention; this likely has no physical effect if used consistently. |
| The reconstruction’s vector-like top charged current omits unchanged \(u,c\) SM charged currents from Eq. (7). | cosmetic | Check whether the reconstruction is intentionally listing only modified/new interactions rather than the full SM charged-current Lagrangian. |

**Overall Assessment**

The reconstruction matches the paper’s vector-like up-type \(t'\) model well at the level of charged-current mixing, Yukawa structure, vector-like mass mixing, and the \(Z/H\) FCNC coefficient structure in Eqs. (7)-(16). Its fourth-generation charged-current block also correctly reproduces the three-angle CKM parametrization of Eqs. (31)-(35). The main caveats are that the reconstruction contains an explicit vector-like \(b'\) sector that the paper only mentions as an aside, and its fourth-generation field and mass descriptions look more like phenomenological Dirac fields than a gauge-invariant sequential fourth-generation Lagrangian. A human reviewer should therefore distinguish between “implementation-level mass-basis phenomenology” and “full electroweak-gauge-invariant model definition” before interpreting the mismatches.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 29 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

