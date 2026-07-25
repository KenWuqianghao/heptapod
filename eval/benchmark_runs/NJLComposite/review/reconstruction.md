# Reconstruction of `sanitized.fr`

## Lagrangian

Notation: color indices are \(a,b=1,2,3\). The SM fermions are written as
\[
Q_{Li}^a=(u_{Li}^a,d_{Li}^a)^T,\qquad L_{Li}=(\nu_{Li},\ell_{Li})^T,
\]
with \(i=1,2,3\) for \(e/\mu/\tau\)-aligned generations. Thus \(u_L,c_L,t_L\), \(d_L,s_L,b_L\), \(e_R,\mu_R,\tau_R\), and \(\nu_{eL},\nu_{\mu L},\nu_{\tau L}\) appear.

For each new scalar \(\phi^a\), the kinetic operator uses the FeynRules `DC` covariant derivative. From the declarations, all new scalars carry a color index and no explicit weak-isospin index. The gauge content encoded in the file is therefore
\[
D_\mu \phi^a
=
\partial_\mu \phi^a
-i g_s\,G_\mu^A (T^A)^a{}_b \phi^b
+\text{neutral electroweak couplings fixed by the declared } Q \text{ and } Y .
\]
Equivalently, in a broken-electroweak notation,
\[
D_\mu \phi^a
=
\left[
\partial_\mu
-i g_s G_\mu^A T^A
-i e Q_\phi A_\mu
-i\frac{e}{s_W c_W}\bigl(T_{3,\phi}-Q_\phi s_W^2\bigr)Z_\mu
\right]^a{}_b\phi^b,
\qquad T_{3,\phi}=Q_\phi-Y_\phi .
\]
No charged \(W^\pm\) covariant-derivative mixing between the component fields is explicitly declared because the fields have no `SU2W` index.

### `LkinNJL`

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{5e}^{a})^\dagger(D^\mu \Pi_{5e}^{a})
-M_{\Pi5e}^2\,\Pi_{5e}^{a\dagger}\Pi_{5e}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{5\mu}^{a})^\dagger(D^\mu \Pi_{5\mu}^{a})
-M_{\Pi5mu}^2\,\Pi_{5\mu}^{a\dagger}\Pi_{5\mu}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{5\tau}^{a})^\dagger(D^\mu \Pi_{5\tau}^{a})
-M_{\Pi5tau}^2\,\Pi_{5\tau}^{a\dagger}\Pi_{5\tau}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{2de}^{a})^\dagger(D^\mu \Pi_{2de}^{a})
-M_{\Pi2de}^2\,\Pi_{2de}^{a\dagger}\Pi_{2de}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{2d\mu}^{a})^\dagger(D^\mu \Pi_{2d\mu}^{a})
-M_{\Pi2dmu}^2\,\Pi_{2d\mu}^{a\dagger}\Pi_{2d\mu}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{2d\tau}^{a})^\dagger(D^\mu \Pi_{2d\tau}^{a})
-M_{\Pi2dtau}^2\,\Pi_{2d\tau}^{a\dagger}\Pi_{2d\tau}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{2ue}^{a})^\dagger(D^\mu \Pi_{2ue}^{a})
-M_{\Pi2ue}^2\,\Pi_{2ue}^{a\dagger}\Pi_{2ue}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{2u\mu}^{a})^\dagger(D^\mu \Pi_{2u\mu}^{a})
-M_{\Pi2umu}^2\,\Pi_{2u\mu}^{a\dagger}\Pi_{2u\mu}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{2u\tau}^{a})^\dagger(D^\mu \Pi_{2u\tau}^{a})
-M_{\Pi2utau}^2\,\Pi_{2u\tau}^{a\dagger}\Pi_{2u\tau}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{-1e}^{a})^\dagger(D^\mu \Pi_{-1e}^{a})
-M_{\Pi m1e}^2\,\Pi_{-1e}^{a\dagger}\Pi_{-1e}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{-1\mu}^{a})^\dagger(D^\mu \Pi_{-1\mu}^{a})
-M_{\Pi m1mu}^2\,\Pi_{-1\mu}^{a\dagger}\Pi_{-1\mu}^{a}
\]

\[
\mathcal L_{\texttt{LkinNJL}}
\supset
(D_\mu \Pi_{-1\tau}^{a})^\dagger(D^\mu \Pi_{-1\tau}^{a})
-M_{\Pi m1tau}^2\,\Pi_{-1\tau}^{a\dagger}\Pi_{-1\tau}^{a}
\]

### `LNJLYukawaNonHC`

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{EU}\,\bar e_R\,u_L^a\,\Pi_{5e}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\mu C}\,\bar\mu_R\,c_L^a\,\Pi_{5\mu}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\tau T}\,\bar\tau_R\,t_L^a\,\Pi_{5\tau}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{ED}\,\bar e_R\,d_L^a\,\Pi_{2de}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\mu S}\,\bar\mu_R\,s_L^a\,\Pi_{2d\mu}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\tau B}\,\bar\tau_R\,b_L^a\,\Pi_{2d\tau}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\nu EU}\,\bar\nu_{eL}\,u_L^a\,\Pi_{2ue}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\nu\mu C}\,\bar\nu_{\mu L}\,c_L^a\,\Pi_{2u\mu}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\nu\tau T}\,\bar\nu_{\tau L}\,t_L^a\,\Pi_{2u\tau}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\nu ED}\,\bar\nu_{eL}\,d_L^a\,\Pi_{-1e}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\nu\mu S}\,\bar\nu_{\mu L}\,s_L^a\,\Pi_{-1\mu}^{a\dagger}
\]

\[
\mathcal L_{\texttt{LNJLYukawaNonHC}}
\supset
\lambda_{\nu\tau B}\,\bar\nu_{\tau L}\,b_L^a\,\Pi_{-1\tau}^{a\dagger}
\]

### `LNJLYukawa`

\[
\mathcal L_{\texttt{LNJLYukawa}}
=
\mathcal L_{\texttt{LNJLYukawaNonHC}}
+
\mathcal L_{\texttt{LNJLYukawaNonHC}}^\dagger
\]

### `LBSM`

\[
\mathcal L_{\texttt{LBSM}}
=
\mathcal L_{\texttt{LkinNJL}}
+
\mathcal L_{\texttt{LNJLYukawa}}
\]

## Field Table

| `.fr` symbol | Spin | SU(3) rep | SU(2) rep declared | \(Q\) | \(Y\) | Self-conjugate | Mass |
|---|---:|---|---|---:|---:|---|---|
| `Pi5e` | 0 | \(\mathbf 3\) | none / singlet as declared | \(5/3\) | \(7/6\) | no | `MPi5e = 1000.` |
| `Pi5mu` | 0 | \(\mathbf 3\) | none / singlet as declared | \(5/3\) | \(7/6\) | no | `MPi5mu = 1000.` |
| `Pi5tau` | 0 | \(\mathbf 3\) | none / singlet as declared | \(5/3\) | \(7/6\) | no | `MPi5tau = 1000.` |
| `Pi2de` | 0 | \(\mathbf 3\) | none / singlet as declared | \(2/3\) | \(7/6\) | no | `MPi2de = 1000.` |
| `Pi2dmu` | 0 | \(\mathbf 3\) | none / singlet as declared | \(2/3\) | \(7/6\) | no | `MPi2dmu = 1000.` |
| `Pi2dtau` | 0 | \(\mathbf 3\) | none / singlet as declared | \(2/3\) | \(7/6\) | no | `MPi2dtau = 1000.` |
| `Pi2ue` | 0 | \(\mathbf 3\) | none / singlet as declared | \(2/3\) | \(1/6\) | no | `MPi2ue = 1000.` |
| `Pi2umu` | 0 | \(\mathbf 3\) | none / singlet as declared | \(2/3\) | \(1/6\) | no | `MPi2umu = 1000.` |
| `Pi2utau` | 0 | \(\mathbf 3\) | none / singlet as declared | \(2/3\) | \(1/6\) | no | `MPi2utau = 1000.` |
| `Pim1e` | 0 | \(\mathbf 3\) | none / singlet as declared | \(-1/3\) | \(1/6\) | no | `MPim1e = 1000.` |
| `Pim1mu` | 0 | \(\mathbf 3\) | none / singlet as declared | \(-1/3\) | \(1/6\) | no | `MPim1mu = 1000.` |
| `Pim1tau` | 0 | \(\mathbf 3\) | none / singlet as declared | \(-1/3\) | \(1/6\) | no | `MPim1tau = 1000.` |

All new scalar fields also declare
\[
B=1/3,\qquad L=-1,
\]
and widths `W... = 1.`.

## Parameters

| Parameter | Value | Multiplies | Physical meaning |
|---|---:|---|---|
| `lamEU` | 1.0 | \(\bar e_R u_L^a \Pi_{5e}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamMuC` | 1.0 | \(\bar\mu_R c_L^a \Pi_{5\mu}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamTauT` | 1.0 | \(\bar\tau_R t_L^a \Pi_{5\tau}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamED` | 1.0 | \(\bar e_R d_L^a \Pi_{2de}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamMuS` | 1.0 | \(\bar\mu_R s_L^a \Pi_{2d\mu}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamTauB` | 1.0 | \(\bar\tau_R b_L^a \Pi_{2d\tau}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamNuEU` | 1.0 | \(\bar\nu_{eL} u_L^a \Pi_{2ue}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamNuMuC` | 1.0 | \(\bar\nu_{\mu L} c_L^a \Pi_{2u\mu}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamNuTauT` | 1.0 | \(\bar\nu_{\tau L} t_L^a \Pi_{2u\tau}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamNuED` | 1.0 | \(\bar\nu_{eL} d_L^a \Pi_{-1e}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamNuMuS` | 1.0 | \(\bar\nu_{\mu L} s_L^a \Pi_{-1\mu}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |
| `lamNuTauB` | 1.0 | \(\bar\nu_{\tau L} b_L^a \Pi_{-1\tau}^{a\dagger}\) | real Yukawa-like scalar leptoquark coupling |

## Physics Summary

The file encodes twelve complex color-triplet scalar states with baryon number \(1/3\) and lepton number \(-1\), each coupled diagonally to one lepton generation and one quark generation. The interactions are scalar leptoquark-like Yukawa couplings involving \(\bar\ell_R q_L\) or \(\bar\nu_L q_L\), plus Hermitian conjugates.

These states mediate quark-lepton transitions such as \(q\ell \leftrightarrow \Pi\), scalar pair production through QCD gauge interactions, and \(t\)- or \(s\)-channel quark-lepton scattering with generation-aligned final states.