# Reverse-check review package — `NJLComposite_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `NJLComposite/model/NJLComposite_gen.fr` |
| original model name | `NJLComposite_gen` (hidden from the agent) |
| paper | NJLComposite/text/2311.18472.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LkinNJL` (`=`)

```mathematica
Block[{mu, aa}, ExpandIndices[DC[HC[Pi5e[aa]], mu] DC[Pi5e[aa], mu] - MPi5e^2 HC[Pi5e[aa]] Pi5e[aa] + DC[HC[Pi5mu[aa]], mu] DC[Pi5mu[aa], mu] - MPi5mu^2 HC[Pi5mu[aa]] Pi5mu[aa] + DC[HC[Pi5tau[aa]], mu] DC[Pi5tau[aa], mu] - MPi5tau^2 HC[Pi5tau[aa]] Pi5tau[aa] + DC[HC[Pi2de[aa]], mu] DC[Pi2de[aa], mu] - MPi2de^2 HC[Pi2de[aa]] Pi2de[aa] + DC[HC[Pi2dmu[aa]], mu] DC[Pi2dmu[aa], mu] - MPi2dmu^2 HC[Pi2dmu[aa]] Pi2dmu[aa] + DC[HC[Pi2dtau[aa]], mu] DC[Pi2dtau[aa], mu] - MPi2dtau^2 HC[Pi2dtau[aa]] Pi2dtau[aa] + DC[HC[Pi2ue[aa]], mu] DC[Pi2ue[aa], mu] - MPi2ue^2 HC[Pi2ue[aa]] Pi2ue[aa] + DC[HC[Pi2umu[aa]], mu] DC[Pi2umu[aa], mu] - MPi2umu^2 HC[Pi2umu[aa]] Pi2umu[aa] + DC[HC[Pi2utau[aa]], mu] DC[Pi2utau[aa], mu] - MPi2utau^2 HC[Pi2utau[aa]] Pi2utau[aa] + DC[HC[Pim1e[aa]], mu] DC[Pim1e[aa], mu] - MPim1e^2 HC[Pim1e[aa]] Pim1e[aa] + DC[HC[Pim1mu[aa]], mu] DC[Pim1mu[aa], mu] - MPim1mu^2 HC[Pim1mu[aa]] Pim1mu[aa] + DC[HC[Pim1tau[aa]], mu] DC[Pim1tau[aa], mu] - MPim1tau^2 HC[Pim1tau[aa]] Pim1tau[aa]]]
```

### `LNJLYukawaNonHC` (`:=`)

```mathematica
Block[{sp, aa}, ExpandIndices[lamEU anti[lR][sp, 1].QL[sp, 1, 1, aa] HC[Pi5e][aa] + lamMuC anti[lR][sp, 2].QL[sp, 1, 2, aa] HC[Pi5mu][aa] + lamTauT anti[lR][sp, 3].QL[sp, 1, 3, aa] HC[Pi5tau][aa] + lamED anti[lR][sp, 1].QL[sp, 2, 1, aa] HC[Pi2de][aa] + lamMuS anti[lR][sp, 2].QL[sp, 2, 2, aa] HC[Pi2dmu][aa] + lamTauB anti[lR][sp, 3].QL[sp, 2, 3, aa] HC[Pi2dtau][aa] + lamNuEU anti[LL][sp, 1, 1].QL[sp, 1, 1, aa] HC[Pi2ue][aa] + lamNuMuC anti[LL][sp, 1, 2].QL[sp, 1, 2, aa] HC[Pi2umu][aa] + lamNuTauT anti[LL][sp, 1, 3].QL[sp, 1, 3, aa] HC[Pi2utau][aa] + lamNuED anti[LL][sp, 1, 1].QL[sp, 2, 1, aa] HC[Pim1e][aa] + lamNuMuS anti[LL][sp, 1, 2].QL[sp, 2, 2, aa] HC[Pim1mu][aa] + lamNuTauB anti[LL][sp, 1, 3].QL[sp, 2, 3, aa] HC[Pim1tau][aa], FlavorExpand -> {Generation}]]
```

### `LNJLYukawa` (`:=`)

```mathematica
LNJLYukawaNonHC + HC[LNJLYukawaNonHC]
```

### `LBSM` (`=`)

```mathematica
LkinNJL + LNJLYukawa
```

## Blank-slate reconstruction

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

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Paper Model Definition Located

The paper defines the relevant composite leptoquark model in **Section II, “Nambu-Jona-Lasinio Composite Leptoquark Model.”**

Key references:

- **Table I**: composite boson field content, constituents, electric charge \(Q_i=Y+t^i_{3L}\), weak isospin \(t^i_{3L}\), hypercharge \(Y\), color representation, and LQ nomenclature.
- **Eq. (1)**: scalar leptoquark kinetic and mass term,
  \[
  (D_\mu\Phi)^\dagger(D^\mu\Phi)+M_\Pi^2\Phi^\dagger\Phi .
  \]
- **Eq. (2)**: covariant derivative,
  \[
  D_\mu=\partial_\mu+i g_1YB_\mu+\frac12 i g_2\sigma^i W^i_\mu+i g_3T^aG^a_\mu .
  \]
- Text immediately after **Eq. (2)**: the color-triplet LQ bosons form \(SU_L(2)\) doublets,
  \[
  \Pi^a_{1/6}=
  \begin{pmatrix}
  \Pi^{2/3}_{u a}\\
  \Pi^{-1/3}_a
  \end{pmatrix},
  \qquad
  \Pi^a_{7/6}=
  \begin{pmatrix}
  \Pi^{5/3}_a\\
  \Pi^{2/3}_{d a}
  \end{pmatrix}.
  \]
- **Eq. (3)**: effective contact/Yukawa interactions for the first generation, plus h.c.
- Text after **Eq. (3)**: generalization to second and third generations, baryon/lepton numbers \(B=1/3\), \(L=-1\), and conjugation relations.
- **Eq. (4)**: example flavor-mixed Yukawa couplings, with CKM-like factors.
- **Section III**: states that the MadGraph/FeynRules implementation includes the gauge terms of Eq. (1) and contact terms of Eq. (3), implemented up to the third fermion generation.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Table I and text after Eq. (2): \(SU_c(3)\) triplet scalar LQs arranged as \(SU_L(2)\) doublets \(\Pi^a_{7/6}=(\Pi^{5/3}_a,\Pi^{2/3}_{d a})^T\), \(\Pi^a_{1/6}=(\Pi^{2/3}_{u a},\Pi^{-1/3}_a)^T\). | Twelve complex color-triplet scalars, but each has “SU(2) rep declared: none / singlet as declared”; no explicit weak-isospin index. | **disagree** | Component electric charges and hypercharges match the two paper doublets, but the reconstruction says the implementation has no \(SU(2)\) doublet structure. This removes explicit charged-\(W^\pm\) transitions between doublet components required by Eq. (2). |
| Eq. (1): \((D_\mu\Phi)^\dagger(D^\mu\Phi)+M_\Pi^2\Phi^\dagger\Phi\). | For each scalar, \((D_\mu\Pi)^\dagger(D^\mu\Pi)-M_\Pi^2\Pi^\dagger\Pi\). | **disagree** | The kinetic form agrees, but the mass term sign differs from the paper as written. This may be a metric/sign convention or a paper typo, but as text-to-text comparison it is different. |
| Eq. (2): covariant derivative includes \(+\frac12 i g_2\sigma^iW^i_\mu\), acting on \(SU(2)\) doublets. | Covariant derivative includes QCD and neutral electroweak couplings fixed by \(Q,Y\), with no charged \(W^\pm\) covariant-derivative mixing. | **disagree** | This is the same core issue as the field representation disagreement: the paper has Pauli-matrix \(SU(2)\) action on doublets; the reconstruction describes component singlets with no \(W^\pm\) doublet mixing. |
| Table I: \(\Pi^{5/3}_a\propto \bar e_R u_{L a}\), \(Q=5/3\), \(t_3=+1/2\), \(Y=7/6\), color triplet; Eq. (3): \(g_{\Pi5/3}(\bar e_Ru_{L a})\Pi^{-5/3}_a+\text{h.c.}\). | \(\lambda_{EU}\bar e_Ru_L^a\Pi_{5e}^{a\dagger}\), plus \(\mu c\) and \(\tau t\) analogues. | **agree** | Chirality, electric charge, hypercharge, color, conjugation in the interaction, and generation generalization agree. Reconstruction uses separate generation labels and default numerical couplings. |
| Table I: \(\Pi^{2/3}_{d a}\propto\bar e_R d_{L a}\), \(Q=2/3\), \(t_3=-1/2\), \(Y=7/6\); Eq. (3): \(g_{\Pi-2/3}(\bar e_Rd_{L a})\Pi^{-2/3}_{d a}+\text{h.c.}\). | \(\lambda_{ED}\bar e_Rd_L^a\Pi_{2de}^{a\dagger}\), plus \(\mu s\) and \(\tau b\) analogues. | **agree** | The component assignment, chirality, color, charge, hypercharge, and use of the conjugate scalar in the interaction agree. |
| Table I: \(\Pi^{2/3}_{u a}\propto\bar\nu^R_e u_{L a}\), \(Q=2/3\), \(t_3=+1/2\), \(Y=1/6\); Eq. (3): \(g_{\Pi-2/3}(\bar\nu^R_eu_{L a})\Pi^{-2/3}_{u a}+\text{h.c.}\). | \(\lambda_{\nu EU}\bar\nu_{eL}u_L^a\Pi_{2ue}^{a\dagger}\), plus \(\nu_\mu c\) and \(\nu_\tau t\) analogues. | **disagree** | The scalar charge and hypercharge match, and conjugation is analogous, but the paper uses a barred right-handed neutrino constituent in Table I/Eq. (3), while the reconstruction uses left-handed neutrinos. |
| Table I: \(\Pi^{-1/3}_a\propto\bar\nu^R_e d_{L a}\), \(Q=-1/3\), \(t_3=-1/2\), \(Y=1/6\); Eq. (3): \(g_{\Pi1/3}(\bar\nu^R_ed_{L a})\Pi^{1/3}_a+\text{h.c.}\). | \(\lambda_{\nu ED}\bar\nu_{eL}d_L^a\Pi_{-1e}^{a\dagger}\), plus \(\nu_\mu s\) and \(\nu_\tau b\) analogues. | **disagree** | Scalar charge, hypercharge, color, and conjugation match, but neutrino chirality differs from the paper’s Table I/Eq. (3). |
| Text after Eq. (3): conjugated fields \((\Pi^{5/3})^\dagger=\Pi^{-5/3}\), \((\Pi^{-1/3})^\dagger=\Pi^{1/3}\), and conjugates for the \(Q=2/3\) states. | All new scalars are complex and non-self-conjugate; Yukawa Lagrangian includes h.c. | **agree** | The reconstruction does not introduce separate independent antiparticle fields, but the complex scalar plus h.c. treatment captures the conjugate interactions. |
| Text after Eq. (3): \(B=1/3\), \(L=-1\) for these LQ states. | All new scalar fields declare \(B=1/3\), \(L=-1\). | **agree** | Matches the paper. |
| Text after Eq. (3): spectra and interactions generalized by \(\nu_e,e,u,d\to\nu_\mu,\mu,c,s\) and \(\nu_\tau,\tau,t,b\). | Reconstruction includes diagonal first-, second-, and third-generation couplings. | **agree** | The diagonal generation generalization is represented. |
| Eq. (3): \(g_{\Pi i}=(F_{\Pi i}/\Lambda)^2\sim O(1)\); paper later uses \(\lambda\) for \(g_{\Pi i}\). | Independent real parameters \(\lambda_{EU}\), \(\lambda_{\mu C}\), etc., defaulting to 1.0. | **agree** | The coefficient structure is compatible with the paper’s \(\lambda\sim O(1)\) convention. Equal default values are benchmark choices, not a structural disagreement. |
| Text after Eq. (3): masses \(M_{\Pi i}\) and couplings \(g_{\Pi i}\) can differ across generations. | Separate mass symbols for each scalar, but all default to 1000; separate coupling symbols, all default to 1.0. | **agree** | The reconstruction has independent parameters even though the displayed defaults are common benchmark values. |
| Eq. (4): example flavor-mixed couplings such as \(g_{\Pi5/3}(U_R^\dagger U_L)_{1,2}(\bar\mu_Rc_L)\Pi^{-5/3}_a\) and \((U_R^\dagger U_L)_{1,3}(\bar\tau_Rt_L)\Pi^{-5/3}_a\), with analogous terms possible for other LQs. | Only generation-aligned couplings are listed: \(eu\), \(\mu c\), \(\tau t\), \(ed\), \(\mu s\), \(\tau b\), and neutrino analogues. | **missing-in-reconstruction** | Eq. (4) describes flavor-mixed couplings of a given LQ state to other generations via mixing matrices. The reconstruction instead has separate generation-labeled LQ fields with diagonal couplings and no explicit CKM-like mixing factors. |
| Section III: implementation includes gauge Eq. (1) and contact Eq. (3) terms up to third generation. | `LBSM = LkinNJL + LNJLYukawa`, with twelve scalar fields and Yukawa terms plus h.c. | **agree** | At the broad implementation-scope level, the reconstruction matches the stated UFO contents, except for the specific disagreements above. |

## Disagreements and Human Checks

1. **Missing \(SU(2)_L\) doublet structure and charged-\(W\) interactions** — **substantive**.  
   A human should check whether the actual implementation intentionally broke the paper’s Eq. (2) doublet structure into electroweak-component singlets, because this changes gauge interactions involving \(W^\pm\).

2. **Neutrino chirality in the \(Y=1/6\) leptoquark interactions** — **substantive**.  
   A human should check the implementation file’s chiral projectors for the neutrino vertices against Table I and Eq. (3), since the paper uses \(\bar\nu_R q_L\) for the positive-charge \(Y=1/6\) constituents while the reconstruction reports \(\bar\nu_L q_L\).

3. **Mass-term sign relative to Eq. (1)** — **convention**.  
   A human should check the paper’s metric/sign convention and the FeynRules scalar mass convention before treating this as a physical mismatch.

4. **Flavor-mixed Yukawa terms of Eq. (4) absent from the reconstruction** — **substantive**.  
   A human should check whether Eq. (4) was intended as part of the implemented model or only as a phenomenological possibility, because the reconstruction contains only generation-aligned couplings without explicit mixing-matrix factors.

## Overall Assessment

The reconstruction captures the paper’s broad leptoquark content: complex color-triplet scalar states with charges \(5/3\), \(2/3\), and \(-1/3\), baryon number \(1/3\), lepton number \(-1\), generation-aligned Yukawa-like couplings, and hermitian conjugates. The main mismatches are notationally small but physically important: the paper defines the charged states as components of \(SU(2)_L\) doublets with the full \(W^i_\mu\) covariant derivative, while the reconstruction describes separate weak singlets with no charged-\(W\) mixing; and the neutrino-coupled \(Y=1/6\) terms use left-handed neutrinos in the reconstruction where the paper’s Table I and Eq. (3) use right-handed neutrino constituents. The absence of Eq. (4)-type flavor-mixed couplings is also important if the review target is the full paper model rather than only a simplified diagonal UFO benchmark.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 24 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

