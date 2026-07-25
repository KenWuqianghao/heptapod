# Reconstructed Physics Content of `sanitized.fr`

## Conventions

Generation indices are \(i,j,\ell,n=1,2,3\), color indices are \(\alpha=1,2,3\). FeynRules `ProjP` and `ProjM` are
\[
P_R=\frac{1+\gamma^5}{2},\qquad P_L=\frac{1-\gamma^5}{2}.
\]
`HC[...]` denotes the Hermitian conjugate. The file contains no `DC[...]` covariant derivatives and no `FS[...]` field-strength kinetic terms; only the interaction terms below are defined. The gauge content appearing explicitly is through Standard Model fermion fields \(u,d,\ell,\nu\), color-index contractions for quarks, and new vector bosons \(W_R^\pm\), \(Z_R\).

## Lagrangian

### `LWRQuarksNonHC`

\[
\mathcal L_{\texttt{LWRQuarksNonHC}}
=
-\,g_{WRq}
\sum_{i,j=1}^{3}\sum_{\alpha=1}^{3}
V'_{CKM\,ij}\,
\bar u_{i\alpha}\gamma^\mu P_R d_{j\alpha}\,
W^+_{R\mu}.
\]

with
\[
g_{WRq}
=
\kappa_R^q\,\frac{e}{\sqrt{2}\,s_w}.
\]

### `LWRQuarks`

\[
\mathcal L_{\texttt{LWRQuarks}}
=
-\,g_{WRq}
\sum_{i,j=1}^{3}\sum_{\alpha=1}^{3}
V'_{CKM\,ij}\,
\bar u_{i\alpha}\gamma^\mu P_R d_{j\alpha}\,
W^+_{R\mu}
+\text{h.c.}
\]

Equivalently, since `CKMR` is declared real in the file,

\[
\mathcal L_{\texttt{LWRQuarks}}
=
-\,g_{WRq}
\sum_{i,j,\alpha}
V'_{CKM\,ij}\,
\bar u_{i\alpha}\gamma^\mu P_R d_{j\alpha}\,
W^+_{R\mu}
-\,g_{WRq}
\sum_{i,j,\alpha}
V'_{CKM\,ij}\,
\bar d_{j\alpha}\gamma^\mu P_R u_{i\alpha}\,
W^-_{R\mu}.
\]

### `LWRLeptonsNonHC`

\[
\mathcal L_{\texttt{LWRLeptonsNonHC}}
=
-\,g_{WR\ell}
\sum_{\ell,n=1}^{3}
Y_{\ell N\,\ell n}\,
\bar N_n \gamma^\mu P_R \ell_\ell\,
W^+_{R\mu}.
\]

with
\[
g_{WR\ell}
=
\kappa_R^\ell\,\frac{e}{\sqrt{2}\,s_w}.
\]

Here \(N_n\) is the Majorana fermion class `HN[n]`.

### `LWRLightNuNonHC`

\[
\mathcal L_{\texttt{LWRLightNuNonHC}}
=
-\,g_{WR\ell}
\sum_{\ell,n=1}^{3}
X_{\ell\nu\,\ell n}\,
\bar \nu_n \gamma^\mu P_R \ell_\ell\,
W^+_{R\mu}.
\]

### `LWRLeptons`

\[
\mathcal L_{\texttt{LWRLeptons}}
=
-\,g_{WR\ell}
\sum_{\ell,n}
Y_{\ell N\,\ell n}\,
\bar N_n \gamma^\mu P_R \ell_\ell\,
W^+_{R\mu}
-\,g_{WR\ell}
\sum_{\ell,n}
X_{\ell\nu\,\ell n}\,
\bar \nu_n \gamma^\mu P_R \ell_\ell\,
W^+_{R\mu}
+\text{h.c.}
\]

With real `YR` and `XL` as declared,

\[
\mathcal L_{\texttt{LWRLeptons}}
=
-\,g_{WR\ell}
\sum_{\ell,n}
Y_{\ell N\,\ell n}\,
\bar N_n \gamma^\mu P_R \ell_\ell\,
W^+_{R\mu}
-\,g_{WR\ell}
\sum_{\ell,n}
Y_{\ell N\,\ell n}\,
\bar \ell_\ell \gamma^\mu P_R N_n\,
W^-_{R\mu}
\]
\[
\qquad
-\,g_{WR\ell}
\sum_{\ell,n}
X_{\ell\nu\,\ell n}\,
\bar \nu_n \gamma^\mu P_R \ell_\ell\,
W^+_{R\mu}
-\,g_{WR\ell}
\sum_{\ell,n}
X_{\ell\nu\,\ell n}\,
\bar \ell_\ell \gamma^\mu P_R \nu_n\,
W^-_{R\mu}.
\]

### `LZRQuarks`

\[
\mathcal L_{\texttt{LZRQuarks}}
=
g_{ZRq}
\sum_{i=1}^{3}\sum_{\alpha=1}^{3}
\left[
\bar u_{i\alpha}\gamma^\mu
\left(g_{ZRuL}P_L+g_{ZRuR}P_R\right)
u_{i\alpha}
+
\bar d_{i\alpha}\gamma^\mu
\left(g_{ZRdL}P_L+g_{ZRdR}P_R\right)
d_{i\alpha}
\right]
Z_{R\mu}.
\]

where

\[
g_{ZRq}
=
-\kappa_R^q\,\frac{e}{s_w}
\sqrt{1-\left(\frac{s_w}{c_w\kappa_R^q}\right)^2},
\]

\[
g_{ZRuL}= -\frac{1}{6}\left(\frac{s_w}{c_w\kappa_R^q}\right)^2,
\qquad
g_{ZRuR}= \frac{1}{2}-\frac{2}{3}\left(\frac{s_w}{c_w\kappa_R^q}\right)^2,
\]

\[
g_{ZRdL}= -\frac{1}{6}\left(\frac{s_w}{c_w\kappa_R^q}\right)^2,
\qquad
g_{ZRdR}= -\frac{1}{2}+\frac{1}{3}\left(\frac{s_w}{c_w\kappa_R^q}\right)^2.
\]

### `LZRLeptons`

\[
\mathcal L_{\texttt{LZRLeptons}}
=
g_{ZR\ell}
\sum_{i=1}^{3}
\left[
\bar \ell_i\gamma^\mu
\left(g_{ZReL}P_L+g_{ZReR}P_R\right)
\ell_i
+
g_{ZR\nu L}\,
\bar \nu_i\gamma^\mu P_L\nu_i
+
g_{ZRN R}\,
\bar N_i\gamma^\mu P_R N_i
\right]
Z_{R\mu}.
\]

where

\[
g_{ZR\ell}
=
-\kappa_R^\ell\,\frac{e}{s_w}
\sqrt{1-\left(\frac{s_w}{c_w\kappa_R^\ell}\right)^2},
\]

\[
g_{ZReL}= \frac{1}{2}\left(\frac{s_w}{c_w\kappa_R^\ell}\right)^2,
\qquad
g_{ZReR}= -\frac{1}{2}+\left(\frac{s_w}{c_w\kappa_R^\ell}\right)^2,
\]

\[
g_{ZR\nu L}= \frac{1}{2}\left(\frac{s_w}{c_w\kappa_R^\ell}\right)^2,
\qquad
g_{ZRN R}= \frac{1}{2}.
\]

### `LTot`

\[
\mathcal L_{\texttt{LTot}}
=
\mathcal L_{\texttt{LWRQuarks}}
+
\mathcal L_{\texttt{LWRLeptons}}
+
\mathcal L_{\texttt{LZRQuarks}}
+
\mathcal L_{\texttt{LZRLeptons}}.
\]

## Field Table

| `.fr` class | Particle symbol | Spin | SU(3) rep | SU(2) rep | U(1) charge / hypercharge | Self-conjugate | Mass |
|---|---:|---:|---|---|---|---|---|
| `WR` | \(W_R^+\), \(W_R^-\) | vector | not declared | not declared | electric charge \(Q=+1\) for `WR`, \(Q=-1\) for anti-particle | no | \(M_{WR}=3000\) |
| `ZR` | \(Z_R\) | vector | not declared | not declared | neutral, inferred from self-conjugacy and interactions; no explicit `Q` entry | yes | \(M_{ZR}=5070\) |
| `HN` / `N1` | \(N_1\) | fermion | singlet, no color index | SM \(SU(2)_L\) singlet as encoded by absence of weak index and right-chiral couplings | \(Q=0\), inferred from Majorana self-conjugacy | yes, Majorana | \(M_{N1}=173.3\) |
| `HN` / `N2` | \(N_2\) | fermion | singlet, no color index | SM \(SU(2)_L\) singlet as encoded by absence of weak index and right-chiral couplings | \(Q=0\), inferred from Majorana self-conjugacy | yes, Majorana | \(M_{N2}=1.0\times10^{12}\) |
| `HN` / `N3` | \(N_3\) | fermion | singlet, no color index | SM \(SU(2)_L\) singlet as encoded by absence of weak index and right-chiral couplings | \(Q=0\), inferred from Majorana self-conjugacy | yes, Majorana | \(M_{N3}=1.0\times10^{12}\) |

## External Parameters

| Parameter | Default value | Appears in | Meaning |
|---|---:|---|---|
| `kRquark` / \(\kappa_R^q\) | \(1\) | `gWRq`, `gZRq`, `gZRuL`, `gZRuR`, `gZRdL`, `gZRdR` | Overall right-handed quark-sector coupling rescaling relative to \(e/s_w\); controls \(W_R\) and \(Z_R\) interactions with quarks. |
| `kRlepton` / \(\kappa_R^\ell\) | \(1\) | `gWRl`, `gZRl`, `gZRnuL`, `gZReL`, `gZReR` | Overall right-handed lepton-sector coupling rescaling relative to \(e/s_w\); controls \(W_R\) and \(Z_R\) interactions with leptons and heavy neutrinos. |
| `CKMR[i,j]` / \(V'_{CKM\,ij}\) | identity matrix | `LWRQuarksNonHC` | Flavor mixing matrix multiplying the charged right-handed quark current \(\bar u_i\gamma^\mu P_R d_j W^+_{R\mu}\). |
| `YR[ll,nn]` / \(Y_{\ell N\,\ell n}\) | identity matrix | `LWRLeptonsNonHC` | Charged-current mixing/coupling matrix between charged leptons \(\ell_\ell\), heavy Majorana neutrinos \(N_n\), and \(W_R^\pm\). |
| `XL[ll,nn]` / \(X_{\ell\nu\,\ell n}\) | zero matrix | `LWRLightNuNonHC` | Charged-current mixing/coupling matrix between charged leptons \(\ell_\ell\), light neutrinos \(\nu_n\), and \(W_R^\pm\). |

## Physics Summary

The file encodes a simplified right-handed charged and neutral vector sector with a charged vector boson \(W_R^\pm\), a neutral vector boson \(Z_R\), and three heavy Majorana neutrinos \(N_i\). The \(W_R\) couples to right-chiral quark charged currents and to right-chiral charged-lepton currents involving either heavy Majorana neutrinos or light neutrinos, while the \(Z_R\) couples chirally to Standard Model quarks, charged leptons, light neutrinos, and heavy neutrinos. It mediates processes such as \(q\bar q'\to W_R^\ast\to \ell N\), \(N\to \ell jj\) through off-shell \(W_R\), and neutral-current production or decay through \(Z_R\) into fermion pairs including \(N_iN_i\).