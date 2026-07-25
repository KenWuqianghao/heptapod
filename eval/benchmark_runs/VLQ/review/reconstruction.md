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