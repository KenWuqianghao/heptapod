# Reverse-check review package — `SMWeinberg_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `SMWeinberg/model/SMWeinberg_gen.fr` |
| original model name | `SMWeinberg_gen` (hidden from the agent) |
| paper | SMWeinberg/text/2012.09882.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LNKin` (`:=`)

```mathematica
I/2 N1bar[s1].Ga[v,s1,s2].del[N1[s2],v] - 1/2 mN1 N1bar[s1].N1[s1]
```

### `LNCCbare` (`:=`)

```mathematica
gw/Sqrt[2] * N1bar.W[m].ProjM[m].e + gw/Sqrt[2] * N1bar.W[m].ProjM[m].mu + gw/Sqrt[2] * N1bar.W[m].ProjM[m].ta
```

### `LNCC` (`:=`)

```mathematica
LNCCbare + HC[LNCCbare]
```

### `LNNCbare` (`:=`)

```mathematica
1/2 * gw/cw * N1bar.Z[m].ProjM[m].ve + 1/2 * gw/cw * N1bar.Z[m].ProjM[m].vm + 1/2 * gw/cw * N1bar.Z[m].ProjM[m].vt
```

### `LNNC` (`:=`)

```mathematica
LNNCbare + HC[LNNCbare]
```

### `LNHbare` (`:=`)

```mathematica
- gw*mN1/(2*MW) * (1 + H*gw/(4*MW)) * N1bar.ProjM.ve H - gw*mN1/(2*MW) * (1 + H*gw/(4*MW)) * N1bar.ProjM.vm H - gw*mN1/(2*MW) * (1 + H*gw/(4*MW)) * N1bar.ProjM.vt H
```

### `LNHX` (`:=`)

```mathematica
LNHbare + HC[LNHbare]
```

### `LNGbare` (`:=`)

```mathematica
I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * ebar.ProjP.N1 GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * mubar.ProjP.N1 GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * tabar.ProjP.N1 GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * N1bar.ProjP.CC[e] GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * N1bar.ProjP.CC[mu] GPbar + I *gw*mN1/(2*Sqrt[2]*MW) * (1 + H*gw/(2*MW)) * N1bar.ProjP.CC[ta] GPbar + I *gw*mN1/(2*MW) * (1 + H*gw/(2*MW)) * vebar.ProjP.N1 G0 + I *gw*mN1/(2*MW) * (1 + H*gw/(2*MW)) * vmbar.ProjP.N1 G0 + I *gw*mN1/(2*MW) * (1 + H*gw/(2*MW)) * vtbar.ProjP.N1 G0
```

### `LNGX` (`:=`)

```mathematica
LNGbare + HC[LNGbare]
```

### `LNGGbare` (`:=`)

```mathematica
gw*gw*mN1/(4*MW*MW) * ebar.ProjP.CC[e] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * mubar.ProjP.CC[e] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * tabar.ProjP.CC[e] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * ebar.ProjP.CC[mu] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * mubar.ProjP.CC[mu] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * tabar.ProjP.CC[mu] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * ebar.ProjP.CC[ta] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * mubar.ProjP.CC[ta] GPbar GPbar + gw*gw*mN1/(4*MW*MW) * tabar.ProjP.CC[ta] GPbar GPbar + gw*gw*mN1/(8*MW*MW) * vebar.ProjP.N1 G0 G0 + gw*gw*mN1/(8*MW*MW) * vmbar.ProjP.N1 G0 G0 + gw*gw*mN1/(8*MW*MW) * vtbar.ProjP.N1 G0 G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * ebar.ProjP.N1 GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * mubar.ProjP.N1 GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * tabar.ProjP.N1 GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * N1bar.ProjP.CC[e] GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * N1bar.ProjP.CC[mu] GPbar G0 + gw*gw*mN1/(4*Sqrt[2]*MW*MW) * N1bar.ProjP.CC[ta] GPbar G0
```

### `LNGGX` (`:=`)

```mathematica
LNGGbare + HC[LNGGbare]
```

### `LD5` (`:=`)

```mathematica
LNKin + LNCC + LNNC + LNHX + LNGX + LNGGX
```

### `LFull` (`:=`)

```mathematica
LSM + LD5
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Conventions

Let
\[
\ell_i=(e,\mu,\tau), \qquad \nu_i=(\nu_e,\nu_\mu,\nu_\tau), \qquad i,j\in\{e,\mu,\tau\}.
\]

The new fermion is denoted \(N\equiv N1\). It is self-conjugate:
\[
N^c=N .
\]

FeynRules projectors are translated as
\[
\texttt{ProjM}=P_L=\frac{1-\gamma^5}{2}, \qquad
\texttt{ProjP}=P_R=\frac{1+\gamma^5}{2}.
\]

The charged fields are interpreted by charge conservation as
\[
\texttt{W}=W^+, \qquad \texttt{GPbar}=G^-,
\]
with the hermitian conjugate terms containing \(W^-\) and \(G^+\). The neutral Goldstone is
\[
\texttt{G0}=G^0 .
\]

No `DC` covariant derivative appears in the new-sector kinetic term. The file uses `del`, so the kinetic derivative is the ordinary derivative:
\[
D_\mu N=\partial_\mu N .
\]
This is consistent with the declared new field carrying no color, weak-isospin, or hypercharge indices and electric charge \(Q=0\). Thus the new kinetic term contains no gluon, \(W\), \(B\), photon, or \(Z\) gauge connection.

The internal mass parameter is
\[
m_N \equiv \texttt{mN1}
= \frac{v^2}{\Lambda}
\left|C_{ee}+C_{e\mu}+C_{e\tau}+C_{\mu\mu}+C_{\mu\tau}+C_{\tau\tau}\right| .
\]

## Lagrangian

### `LNKin`

\[
\boxed{
\mathcal L_{\texttt{LNKin}}
=
\frac{i}{2}\,\overline N\,\gamma^\mu \partial_\mu N
-\frac{1}{2}\,m_N\,\overline N N
}
\]

### `LNCCbare`

\[
\boxed{
\mathcal L_{\texttt{LNCCbare}}
=
\frac{g_w}{\sqrt 2}
\sum_i
\overline N\,\gamma^\mu P_L\,\ell_i\,W^+_\mu
}
\]

### `LNCC`

\[
\boxed{
\mathcal L_{\texttt{LNCC}}
=
\frac{g_w}{\sqrt 2}
\sum_i
\left(
\overline N\,\gamma^\mu P_L\,\ell_i\,W^+_\mu
+
\overline{\ell_i}\,\gamma^\mu P_L\,N\,W^-_\mu
\right)
}
\]

### `LNNCbare`

\[
\boxed{
\mathcal L_{\texttt{LNNCbare}}
=
\frac{g_w}{2c_w}
\sum_i
\overline N\,\gamma^\mu P_L\,\nu_i\,Z_\mu
}
\]

### `LNNC`

\[
\boxed{
\mathcal L_{\texttt{LNNC}}
=
\frac{g_w}{2c_w}
\sum_i
\left(
\overline N\,\gamma^\mu P_L\,\nu_i
+
\overline{\nu_i}\,\gamma^\mu P_L\,N
\right)Z_\mu
}
\]

### `LNHbare`

\[
\boxed{
\mathcal L_{\texttt{LNHbare}}
=
-\frac{g_w m_N}{2M_W}
\left(1+\frac{g_w H}{4M_W}\right)
H
\sum_i
\overline N\,P_L\,\nu_i
}
\]

Equivalently, expanded in powers of \(H\),
\[
\mathcal L_{\texttt{LNHbare}}
=
-\frac{g_w m_N}{2M_W}
H\sum_i\overline N P_L\nu_i
-\frac{g_w^2 m_N}{8M_W^2}
H^2\sum_i\overline N P_L\nu_i .
\]

### `LNHX`

\[
\boxed{
\mathcal L_{\texttt{LNHX}}
=
-\frac{g_w m_N}{2M_W}
\left(1+\frac{g_w H}{4M_W}\right)
H
\sum_i
\left(
\overline N\,P_L\,\nu_i
+
\overline{\nu_i}\,P_R\,N
\right)
}
\]

### `LNGbare`

\[
\boxed{
\begin{aligned}
\mathcal L_{\texttt{LNGbare}}
={}&
\frac{i g_w m_N}{2\sqrt 2 M_W}
\left(1+\frac{g_w H}{2M_W}\right)
G^-
\sum_i
\left(
\overline{\ell_i}\,P_R\,N
+
\overline N\,P_R\,\ell_i^c
\right)
\\
&+
\frac{i g_w m_N}{2M_W}
\left(1+\frac{g_w H}{2M_W}\right)
G^0
\sum_i
\overline{\nu_i}\,P_R\,N .
\end{aligned}
}
\]

### `LNGX`

\[
\boxed{
\mathcal L_{\texttt{LNGX}}
=
\mathcal L_{\texttt{LNGbare}}
+
\mathcal L_{\texttt{LNGbare}}^\dagger
}
\]

Explicitly, this adds the \(G^+\) conjugates and the conjugate neutral-Goldstone bilinears.

### `LNGGbare`

\[
\boxed{
\begin{aligned}
\mathcal L_{\texttt{LNGGbare}}
={}&
\frac{g_w^2 m_N}{4M_W^2}
(G^-)^2
\sum_{i,j}
\overline{\ell_i}\,P_R\,\ell_j^c
\\
&+
\frac{g_w^2 m_N}{8M_W^2}
(G^0)^2
\sum_i
\overline{\nu_i}\,P_R\,N
\\
&+
\frac{g_w^2 m_N}{4\sqrt 2 M_W^2}
G^-G^0
\sum_i
\left(
\overline{\ell_i}\,P_R\,N
+
\overline N\,P_R\,\ell_i^c
\right).
\end{aligned}
}
\]

The first sum is over all nine ordered charged-lepton flavor combinations:
\[
(i,j)=(e,e),(\mu,e),(\tau,e),(e,\mu),(\mu,\mu),(\tau,\mu),(e,\tau),(\mu,\tau),(\tau,\tau).
\]

### `LNGGX`

\[
\boxed{
\mathcal L_{\texttt{LNGGX}}
=
\mathcal L_{\texttt{LNGGbare}}
+
\mathcal L_{\texttt{LNGGbare}}^\dagger
}
\]

### `LD5`

\[
\boxed{
\mathcal L_{\texttt{LD5}}
=
\mathcal L_{\texttt{LNKin}}
+
\mathcal L_{\texttt{LNCC}}
+
\mathcal L_{\texttt{LNNC}}
+
\mathcal L_{\texttt{LNHX}}
+
\mathcal L_{\texttt{LNGX}}
+
\mathcal L_{\texttt{LNGGX}}
}
\]

### `LFull`

\[
\boxed{
\mathcal L_{\texttt{LFull}}
=
\mathcal L_{\texttt{SM}}
+
\mathcal L_{\texttt{LD5}}
}
\]

The file does not define `LSM`; it only adds the new-sector terms above to the Standard Model Lagrangian object.

## Field Table

| `.fr` symbol | Particle | Spin | SU(3) rep | SU(2) rep | U(1) / charge | Self-conjugate | Mass |
|---|---:|---:|---|---|---|---|---|
| `N1` | \(N\) | \(1/2\) Majorana fermion | singlet, no color index declared | singlet, no weak index declared | \(Q=0\); hypercharge not declared | yes | `mN1`, internal: \(\dfrac{v^2}{\Lambda}\left|C_{ee}+C_{e\mu}+C_{e\tau}+C_{\mu\mu}+C_{\mu\tau}+C_{\tau\tau}\right|\) |

Width:
\[
\Gamma_N=\texttt{WN1}=0 .
\]

PDG code:
\[
9900012 .
\]

## External Parameters

| Symbol | Value | Multiplies / enters | Physical meaning |
|---|---:|---|---|
| `Lambda` | \(200000.\) | Appears in the denominator of `mN1`: \(m_N\propto v^2/\Lambda\) | Heavy mass scale suppressing the effective Majorana mass operator |
| `Cee` | \(1.1\) | Contribution to the sum defining `mN1` | Dimensionless coefficient associated with the \(ee\) flavor entry |
| `Cem` | \(1.0\) | Contribution to the sum defining `mN1` | Dimensionless coefficient associated with the \(e\mu\) flavor entry |
| `Cet` | \(1.3\) | Contribution to the sum defining `mN1` | Dimensionless coefficient associated with the \(e\tau\) flavor entry |
| `Cmm` | \(1.4\) | Contribution to the sum defining `mN1` | Dimensionless coefficient associated with the \(\mu\mu\) flavor entry |
| `Cmt` | \(1.5\) | Contribution to the sum defining `mN1` | Dimensionless coefficient associated with the \(\mu\tau\) flavor entry |
| `Ctt` | \(1.6\) | Contribution to the sum defining `mN1` | Dimensionless coefficient associated with the \(\tau\tau\) flavor entry |

The external coefficients do not appear as independent flavor-dependent vertices in the displayed interaction terms. In this file they enter the Lagrangian only through the internal mass parameter `mN1`.

## Physics Summary

The file adds one electrically neutral, self-conjugate Majorana fermion \(N\), with mass generated by an effective scale \(\Lambda\) and dimensionless flavor coefficients \(C_{ij}\). The new fermion couples left-chirally to SM charged leptons and neutrinos through \(W^\pm\), \(Z\), the Higgs boson, and the electroweak Goldstones in Feynman gauge. It mediates heavy neutral lepton production and decay channels such as \(W^\pm\to N\ell^\pm\), \(Z\to N\nu\), Higgs/Goldstone-associated interactions, and lepton-number-violating Goldstone-sector contact interactions tied to the Majorana mass.

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Located Model Definitions

The paper defines the underlying dimension-five SMEFT model in **“The Standard Model at Dimension Five”**, with the Weinberg operator in **Eq. (2)**,
\[
\mathcal L_5=\frac{C^{\ell\ell'}_5}{\Lambda}[\Phi\cdot L^c_\ell][L_{\ell'}\cdot\Phi]+\text{H.c.},
\]
the effective Majorana mass in **Eq. (3)**,
\[
m_{\ell\ell'}=C^{\ell\ell'}_5v^2/\Lambda,
\]
and the EFT Lagrangian in **Eq. (4)**. In unitary gauge, the post-EWSB Weinberg terms are written in **Eq. (5)**. The collider prescription replaces the \((\nu_\ell\nu^c_{\ell'})\) current by an unphysical Majorana fermion \(N\), with the charged-current interaction in **Eq. (8)** and the implementation mass prescription in **Eq. (9)**.

The implementation-level field and interaction definitions are in the **Appendix: Technical details on methodology**. The generic-gauge Higgs/Goldstone definitions are in **Eqs. (16)-(17)**, the expanded Weinberg operator is in **Eqs. (18)-(22)**, the SMWeinberg UFO interaction Lagrangian is in **Eqs. (23)-(29)**, and the UFO parameter table is **Table II**.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---:|---|
| SMEFT Lagrangian \( \mathcal L_{\rm SMEFT}=\mathcal L_{\rm SM}+\mathcal L_5+\mathcal O(\Lambda^{-2})\), Eq. (4) | `LFull = LSM + LD5` | agree | The reconstruction mirrors the paper’s structure: SM plus the dimension-five/new-sector implementation. |
| Weinberg operator \(C^{\ell\ell'}_5[\Phi\cdot L^c_\ell][L_{\ell'}\cdot\Phi]/\Lambda+\text{H.c.}\), Eq. (2) | Replaced by \(N\)-mediated `LD5` terms | agree | The reconstruction does not keep the gauge-invariant operator literally; this matches the paper’s stated UFO prescription that models the current with an unphysical Majorana \(N\). |
| Effective mass \(m_{\ell\ell'}=C^{\ell\ell'}_5v^2/\Lambda\), Eq. (3) | \(m_N=(v^2/\Lambda)|C_{ee}+C_{e\mu}+C_{e\tau}+C_{\mu\mu}+C_{\mu\tau}+C_{\tau\tau}|\) | agree | This matches the paper’s implementation prescription in Eq. (9), not a single flavor-entry mass. |
| Unphysical Majorana neutrino \(N\) with mass \(m_N\), text before Eq. (9), Table II | Field table: \(N1\), Majorana, self-conjugate, neutral, mass `mN1` | agree | The paper calls \(N\) an unphysical Majorana neutrino and lists \(m_N\) as the internal mass parameter. Neutral singlet status is inferred consistently from the implementation. |
| \(m_N=|C^5_{ee}+C^5_{e\mu}+C^5_{e\tau}+C^5_{\mu\mu}+C^5_{\mu\tau}+C^5_{\tau\tau}|v^2/\Lambda\), Eq. (9) | Same expression with `Cee`, `Cem`, `Cet`, `Cmm`, `Cmt`, `Ctt` | agree | Same six independent symmetric flavor coefficients enter only through \(m_N\). |
| \(\Gamma_N\), Table II | \(\Gamma_N=\texttt{WN1}=0\) | agree | Table II identifies the width parameter; the reconstruction’s zero-width value is compatible with an internal unphysical mediator used for the prescription. |
| Generic-gauge Higgs doublet \(\sqrt2\Phi=(-i\sqrt2G^+,v+h+iG^0)^T\), Eqs. (16)-(17) | Uses \(H\), \(G^0\), \(G^-\)/\(G^+\) Goldstones in `LNHX`, `LNGX`, `LNGGX` | agree | The reconstruction uses the charge-conjugate Goldstone orientation for several “bare” terms, then adds H.c.; physics content matches. |
| Weinberg post-EWSB neutrino mass term \(-C^{\ell\ell'}_5v^2\nu^c_\ell\nu_{\ell'}/(2\Lambda)+\text{H.c.}\), Eq. (5), Eq. (18) | \(-\frac12m_N\bar NN\) in `LNKin` | agree | This is the \(N\)-mediated implementation of the mass insertion/current, with the implementation mass of Eq. (9). |
| Single-Higgs Weinberg term \(-C^{\ell\ell'}_5v\,h\,\nu^c_\ell\nu_{\ell'}/\Lambda+\text{H.c.}\), Eq. (5), Eq. (18) | \(-g_Wm_NH/(2M_W)\sum_i(\bar NP_L\nu_i+\bar\nu_iP_RN)\) in `LNHX` | agree | Using \(M_W=g_Wv/2\), the coefficient is \(-m_N/v\), matching the implementation form in Eq. (25). |
| Double-Higgs Weinberg term \(-C^{\ell\ell'}_5h h\,\nu^c_\ell\nu_{\ell'}/(2\Lambda)+\text{H.c.}\), Eq. (5), Eq. (18) | \(-g_W^2m_NH^2/(8M_W^2)\sum_i(\bar NP_L\nu_i+\bar\nu_iP_RN)\) in `LNHX` | agree | Coefficient equals \(-m_N/(2v^2)\), matching Eq. (25). |
| Charged current \(-g_W W^+_\mu\sum_\ell \bar N\gamma^\mu P_L\ell^-/\sqrt2+\text{H.c.}\), Eq. (8), Eq. (23) | \(+g_W W^+_\mu\sum_i\bar N\gamma^\mu P_L\ell_i/\sqrt2+\text{H.c.}\) in `LNCC` | disagree | Field content, chirality, flavor sum, and H.c. structure match, but the overall sign is opposite to Eqs. (8) and (23). |
| Neutral current \(-g_W Z_\mu\sum_\ell\bar N\gamma^\mu P_L\nu_\ell/(2\cos\theta_W)+\text{H.c.}\), Eq. (24) | \(+g_W Z_\mu\sum_i(\bar N\gamma^\mu P_L\nu_i+\bar\nu_i\gamma^\mu P_LN)/(2c_W)\) in `LNNC` | disagree | Same field content and chirality, but the coefficient sign is opposite to Eq. (24). |
| Higgs interaction \(-g_Wm_N h(1+g_Wh/(4m_W))\sum_\ell\bar NP_L\nu_\ell/(2m_W)+\text{H.c.}\), Eq. (25) | Same coefficient and H.c. in `LNHX` | agree | Matches coefficient, Higgs expansion, chirality, and flavor-universal implementation. |
| Charged-Goldstone term \(-i g_Wm_NG^+(1+g_Wh/(2m_W))\sum_\ell(\bar NP_L\ell+\bar\ell^cP_LN)/(2\sqrt2m_W)+\text{H.c.}\), Eq. (26) | \(+i g_Wm_NG^-(1+g_WH/(2M_W))\sum_i(\bar\ell_iP_RN+\bar NP_R\ell_i^c)/(2\sqrt2M_W)+\text{H.c.}\) in `LNGX` | agree | Reconstruction writes the charge-conjugate \(G^-\) piece as the bare term; with H.c., it matches Eq. (26). The \(P_R\) form is the conjugate bilinear of the paper’s \(P_L\) form. |
| Neutral-Goldstone term \(-i g_Wm_NG^0(1+g_Wh/(2m_W))\sum_\ell\bar NP_L\nu_\ell/(2m_W)+\text{H.c.}\), Eq. (27) | \(+i g_Wm_NG^0(1+g_WH/(2M_W))\sum_i\bar\nu_iP_RN/(2M_W)+\text{H.c.}\) in `LNGX` | agree | Reconstruction displays the Hermitian-conjugate bilinear as the bare term; with H.c., coefficient and chirality match Eq. (27). |
| \(G^+G^+\) contact term \(+g_W^2m_N\,2G^+G^+\sum_{\ell,\ell'}\bar\ell^cP_L\ell'/(8m_W^2)+\text{H.c.}\), Eq. (28) | \(+g_W^2m_N(G^-)^2\sum_{i,j}\bar\ell_iP_R\ell_j^c/(4M_W^2)+\text{H.c.}\) in `LNGGX` | agree | Reconstruction writes the H.c. \(G^-G^-\) orientation; coefficient and all ordered flavor combinations match. |
| \(G^0G^0\) contact term \(+g_W^2m_NG^0G^0\sum_\ell\bar NP_L\nu_\ell/(8m_W^2)+\text{H.c.}\), Eq. (28) | \(+g_W^2m_N(G^0)^2\sum_i\bar\nu_iP_RN/(8M_W^2)+\text{H.c.}\) in `LNGGX` | agree | Reconstruction writes the conjugate bilinear; H.c. completes the paper term. |
| Mixed \(G^0G^+\) contact term \(+g_W^2m_NG^0G^+\sum_\ell(\bar NP_L\ell+\bar\ell^cP_LN)/(4\sqrt2m_W^2)+\text{H.c.}\), Eq. (29) | \(+g_W^2m_NG^-G^0\sum_i(\bar\ell_iP_RN+\bar NP_R\ell_i^c)/(4\sqrt2M_W^2)+\text{H.c.}\) in `LNGGX` | agree | Reconstruction gives the charge-conjugate \(G^-G^0\) bare orientation; full H.c. agrees with Eq. (29). |
| Direct flavor-dependent vertices proportional to individual \(C^{\ell\ell'}_5\), Eqs. (18)-(22) | No independent \(C_{ij}\)-dependent vertices; coefficients enter only through \(m_N\) | agree | This matches the SMWeinberg UFO prescription described around Eq. (9), although it is not the literal flavor-basis Weinberg operator. |
| \(Z\), Higgs, and Goldstone interactions in the appendix, Eqs. (24)-(29) | Included in `LNNC`, `LNHX`, `LNGX`, `LNGGX` | agree | These terms would look extra if compared only to the main-text Eq. (8), but they are explicitly part of the appendix UFO Lagrangian. |
| \(N\) kinetic term | \(\frac{i}{2}\bar N\gamma^\mu\partial_\mu N\) in `LNKin` | agree | The paper does not print this term explicitly, but a single free Majorana field with mass \(m_N\) is required by the implementation. Ordinary derivative is consistent with \(N\) being neutral/singlet. |
| Gauge-covariant kinetic coupling of \(N\) | None | agree | The paper’s \(N\) is an unphysical Majorana neutrino with prescribed EW interactions, not a field carrying SM gauge indices. |

## Disagreements to Check

1. **Charged-current overall sign, Eqs. (8) and (23)** — severity: **convention**.  
   Human check: compare the original FeynRules/UFO vertex convention for \(W^+N\ell^-\) against the paper’s printed \(\Delta\mathcal L\), because the reconstruction has the same fields and chirality but the opposite Lagrangian sign.

2. **Neutral-current overall sign, Eq. (24)** — severity: **convention**.  
   Human check: verify whether the \(ZN\nu\) sign in the implementation is tied to the same convention as the charged-current sign or whether it is a transcription/sign error relative to the appendix.

No substantive mismatch was found in the mass prescription, flavor sums, Majorana nature of \(N\), Higgs terms, Goldstone terms, Hermitian-conjugate structure, or chirality assignments after accounting for charge-conjugate bilinears.

## Overall Assessment

The reconstruction closely matches the SMWeinberg implementation described in the paper’s appendix: it identifies the same unphysical neutral Majorana mediator \(N\), the same internally calculated mass \(m_N\), the same flavor-universal \(W/Z/H\) and Goldstone interactions, and the same replacement of explicit \(C^{\ell\ell'}_5\)-dependent Weinberg vertices by coefficients entering through \(m_N\). The main caveat is an apparent overall sign difference in the reconstructed \(W\) and \(Z\) interaction terms relative to the printed Eqs. (8), (23), and (24); this is likely convention-level but should be checked against the actual FeynRules/UFO vertex output before relying on relative signs in amplitudes involving interference.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 9 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

