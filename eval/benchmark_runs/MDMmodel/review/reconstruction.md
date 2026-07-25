# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Field definitions used by the Lagrangian:

\[
S = v_f + s_s\, h + c_s\, s_{\rm DM}
\]

\[
\Phi =
\begin{pmatrix}
-i G^+ \\
\dfrac{v + c_s h - s_s s_{\rm DM} + iG^0}{\sqrt{2}}
\end{pmatrix}
\]

\[
T_L = P_L(-s_l\, t + c_l\, t'), \qquad
T_R = P_R(-s_r\, t + c_r\, t')
\]

with

\[
P_L=\frac{1-\gamma^5}{2}, \qquad P_R=\frac{1+\gamma^5}{2}.
\]

The covariant derivatives are

\[
D_\mu \Phi =
\left(
\partial_\mu
- i g\, W_\mu^a \frac{\sigma^a}{2}
- i g' \frac{1}{2} B_\mu
\right)\Phi ,
\]

\[
D_\mu T =
\left(
\partial_\mu
- i g_s\, G_\mu^A T^A
- i g' \frac{2}{3} B_\mu
\right)T ,
\]

where \(T\) is an \(SU(3)_c\) triplet, \(SU(2)_L\) singlet fermion with \(Y=Q=2/3\). The singlet scalar \(S\) has ordinary derivative \(\partial_\mu S\).

### `LFermionsDM`

\[
\mathcal L_{\mathrm{kin},T}^{\texttt{LFermionsDM}}
=
i\,\overline{T_L}\gamma^\mu D_\mu T_L
+i\,\overline{T_L}\gamma^\mu D_\mu T_R
+i\,\overline{T_R}\gamma^\mu D_\mu T_L
+i\,\overline{T_R}\gamma^\mu D_\mu T_R .
\]

Equivalently, with \(T=T_L+T_R\),

\[
\mathcal L_{\mathrm{kin},T}^{\texttt{LFermionsDM}}
=
i\,\overline T \gamma^\mu D_\mu T .
\]

\[
\mathcal L_{S\overline TT}^{\texttt{LFermionsDM}}
=
-\frac{M_{\Delta}}{v_f}\,
S\,
\left(
\overline{T_L}T_L
+\overline{T_L}T_R
+\overline{T_R}T_L
+\overline{T_R}T_R
\right),
\]

with

\[
M_{\Delta}\equiv \texttt{Mdltn}=M_{T'}c_l .
\]

Equivalently,

\[
\mathcal L_{S\overline TT}^{\texttt{LFermionsDM}}
=
-\frac{M_{\Delta}}{v_f}\,S\,\overline T T .
\]

### `LHiggsMDM`

\[
\mathcal L_{\Phi,\mathrm{kin}}^{\texttt{LHiggsMDM}}
=
(D_\mu\Phi)^\dagger(D^\mu\Phi).
\]

\[
\mathcal L_{S,\mathrm{kin}}^{\texttt{LHiggsMDM}}
=
-\frac12\,\partial_\mu S\,\partial^\mu S .
\]

\[
\mathcal L_{S^2}^{\texttt{LHiggsMDM}}
=
-\frac{\mu_S^2}{2}\,S^2 .
\]

\[
\mathcal L_{S^4}^{\texttt{LHiggsMDM}}
=
-\frac{\lambda_S}{24}\,S^4 .
\]

\[
\mathcal L_{S^2\Phi^\dagger\Phi}^{\texttt{LHiggsMDM}}
=
-\frac{\kappa}{2}\,S^2\,\Phi^\dagger\Phi .
\]

\[
\mathcal L_{\Phi^\dagger\Phi}^{\texttt{LHiggsMDM}}
=
-\mu_H^2\,\Phi^\dagger\Phi .
\]

\[
\mathcal L_{(\Phi^\dagger\Phi)^2}^{\texttt{LHiggsMDM}}
=
-\frac{\lambda_H}{4}\,
(\Phi^\dagger\Phi)^2 .
\]

The parameters appearing here are the internal FeynRules symbols

\[
\kappa=\texttt{dkappa},\qquad
\lambda_H=\texttt{dlamh},\qquad
\lambda_S=\texttt{dlams},
\]

\[
\mu_S^2=\texttt{muS2},\qquad
\mu_H^2=\texttt{muH2}.
\]

### `LYukawaDM`

The FeynRules expression

\[
-\texttt{yp}\;
\overline{Q}_{L,3}^{\,i}\,
T_R\,
\Phi^{\dagger j}\,
\epsilon_{ij}
+\mathrm{h.c.}
\]

is

\[
\mathcal L_{\mathrm{Yuk}}^{\texttt{LYukawaDM}}
=
-y'\,\overline Q_{L,3}^{\,i}\,
\widetilde\Phi_i\,
T_R
+\mathrm{h.c.},
\]

where

\[
\widetilde\Phi_i \equiv \epsilon_{ij}\Phi^{\dagger j},
\qquad
Q_{L,3}=
\begin{pmatrix}
t_L\\
b_L
\end{pmatrix},
\]

and

\[
y'=\texttt{yp}=\frac{\sqrt2}{v}M_{T'}s_l .
\]

The hermitian conjugate is

\[
-y'^{\,*}\,
\overline{T_R}\,
\widetilde\Phi_i^\dagger
Q_{L,3}^{\,i}.
\]

## Field Table

| `.fr` class | Symbol | Spin | SU(3) rep | SU(2) rep | \(U(1)_Y\) / charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---|---|---|
| `S[21]` | `sDM` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | \(M_{s{\rm DM}}=\texttt{MsDM}=173.2\) |
| `F[7]` | `tp` | 1/2 | triplet | singlet | \(Y=2/3,\ Q=2/3\) | no | \(M_{T'}=\texttt{MTP}=1670.3\) |
| `S[31]` | `S` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | unphysical gauge/electroweak-basis field |
| `S[11]` | `Phi` | 0 | singlet | doublet | \(Y=1/2\) | no | unphysical Higgs doublet |
| `F[26]` | `TR` | 1/2 | triplet | singlet | \(Y=2/3,\ Q=2/3\) | no | unphysical right-chiral component |
| `F[27]` | `TL` | 1/2 | triplet | singlet | \(Y=2/3,\ Q=2/3\) | no | unphysical left-chiral component |

## External Parameters

| Symbol | Value | Appears in | Physical meaning |
|---|---:|---|---|
| `eta` | 0.33 | \(v_f=v/\eta\) | Ratio setting the singlet vev \(v_f\) relative to the SM Higgs vev \(v\). |
| `ts` | -0.23 | \(s_s=t_s/\sqrt{1+t_s^2}\), \(c_s=1/\sqrt{1+t_s^2}\), scalar potential parameters | Tangent of the scalar mixing angle, \(t_s=\tan\theta_S\). |
| `sl` | 0.12 | \(c_l=\sqrt{1-s_l^2}\), \(s_r=M_t s_l/(M_{T'}c_l)\), \(y'=\sqrt2 M_{T'}s_l/v\), \(M_\Delta=M_{T'}c_l\) | Sine of the left-handed top-partner mixing angle, \(s_l=\sin\theta_L\). |

## Physics Summary

The file encodes a singlet-scalar extension of the Higgs sector together with a vector-like color-triplet, electroweak-singlet fermion of charge \(2/3\) that mixes chirally with the SM top quark. The physical scalar `sDM` is a real scalar mixed with the SM Higgs through the singlet vev and portal interaction, while `tp` is a heavy top partner coupled to the third-generation quark doublet through a \(\widetilde\Phi\) Yukawa interaction. The model mediates Higgs-portal scalar interactions, scalar production and decay through mixing, and top-partner processes such as \(t'\) production and decays involving \(t\), \(h\), electroweak bosons, and the singlet-like scalar.