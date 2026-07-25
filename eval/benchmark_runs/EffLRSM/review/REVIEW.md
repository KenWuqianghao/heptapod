# Reverse-check review package — `EffLRSM_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `EffLRSM/repair/final.fr` |
| original model name | `EffLRSM_gen` (hidden from the agent) |
| paper | EffLRSM/text/1610.08985.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LWRQuarksNonHC` (`:=`)

```mathematica
Block[{mu,ii,jj,cc}, -gWRq Sum[CKMR[ii,jj] bar[u[ii,cc]].Ga[mu].ProjP.d[jj,cc] WR[mu], {ii,1,3}, {jj,1,3}, {cc,1,3}]]
```

### `LWRQuarks` (`:=`)

```mathematica
LWRQuarksNonHC + HC[LWRQuarksNonHC]
```

### `LWRLeptonsNonHC` (`:=`)

```mathematica
Block[{mu,ll,nn}, -gWRl Sum[YR[ll,nn] bar[HN[nn]].Ga[mu].ProjP.l[ll] WR[mu], {ll,1,3}, {nn,1,3}]]
```

### `LWRLightNuNonHC` (`:=`)

```mathematica
Block[{mu,ll,nn}, -gWRl Sum[XL[ll,nn] bar[ve[nn]].Ga[mu].ProjP.l[ll] WR[mu], {ll,1,3}, {nn,1,3}]]
```

### `LWRLeptons` (`:=`)

```mathematica
LWRLeptonsNonHC + LWRLightNuNonHC + HC[LWRLeptonsNonHC + LWRLightNuNonHC]
```

### `LZRQuarks` (`:=`)

```mathematica
Block[{mu,ii,cc}, gZRq Sum[(bar[u[ii,cc]].Ga[mu].(gZRuL ProjM + gZRuR ProjP).u[ii,cc] + bar[d[ii,cc]].Ga[mu].(gZRdL ProjM + gZRdR ProjP).d[ii,cc]) ZR[mu], {ii,1,3}, {cc,1,3}]]
```

### `LZRLeptons` (`:=`)

```mathematica
Block[{mu,ii}, gZRl Sum[(bar[l[ii]].Ga[mu].(gZReL ProjM + gZReR ProjP).l[ii] + bar[ve[ii]].Ga[mu].gZRnuL ProjM.ve[ii] + bar[HN[ii]].Ga[mu].gZRNR ProjP.HN[ii]) ZR[mu], {ii,1,3}]]
```

### `LTot` (`:=`)

```mathematica
LWRQuarks + LWRLeptons + LZRQuarks + LZRLeptons
```

## Blank-slate reconstruction

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

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Located Paper Definitions

The paper defines the model in **Section II, “Effective Left-Right Symmetric Model”**. The relevant definitions are:

- Field content: Section II opening paragraph: SM states, \(W_R^\pm\), \(Z_R\), and three heavy Majorana neutrinos \(N_i\).
- Chiral fermion quantum numbers: **Table I**.
- Right-handed charged-current quark interaction: **Eq. (4)**.
- Right-handed charged-current lepton interaction: **Eq. (5)**.
- Heavy/light neutrino mixing assumptions: **Eqs. (6)-(7)**.
- \(Z_R\) neutral-current interaction: **Eq. (8)**.
- \(Z_R\) chiral coefficients: **Eqs. (9)-(10)**.
- Benchmark mass assumptions: **Eqs. (18)-(19)** and **Table II**.
- Implementation scope: **Section III.A**, which says the SM Lagrangian plus Eqs. (4)-(8) are implemented.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field content: SM states, \(W_R^\pm\), \(Z_R\), three heavy Majorana \(N_i\), with \(W_R,Z_R\) aligned to mass eigenstates; \(N_i\) aligned with RH chiral states (Sec. II) | Field table lists \(W_R^\pm\), \(Z_R\), \(N_{1,2,3}\), plus SM fermions appearing in interactions | agree | Reconstruction captures the BSM field content. It does not fully reproduce Table I for all SM chiral fermions, but the interaction terms encode the same charges. |
| Chiral fermion charges \(T_L^3,T_R^3,Q_f\) (Table I) | Uses SM fermions with \(P_L/P_R\) and \(Z_R\) chiral coefficients inferred from charges | agree | The explicit Table I charge assignments are not reproduced as a full table for all SM fermions, but the reconstructed \(Z_R\) coefficients match those charges. |
| \( \mathcal L_{W_Rqq'} = -\kappa_R^q g/\sqrt2 \sum \bar u_i V^{CKM'}_{ij} W^+_{R\mu}\gamma^\mu P_R d_j + \mathrm{H.c.}\) (Eq. 4) | `LWRQuarks`: \(-g_{WRq} V'_{CKMij}\bar u_i\gamma^\mu P_R d_j W^+_{R\mu}+\mathrm{h.c.}\), \(g_{WRq}=\kappa_R^q e/(\sqrt2 s_w)\) | agree | Since \(g=e/s_w\), the coefficient and chirality match. Color contraction is correctly included. |
| RH CKM matrix taken diagonal with unit entries for the study (text after Eq. 4) | `CKMR[i,j]` default identity matrix | agree | Reconstruction matches the study assumption. |
| \( \mathcal L_{W_R\ell\nu/N}= -\kappa_R^\ell g/\sqrt2 \sum_\ell [\sum_m \nu_m^c X_{\ell m}+\sum_{m'} N_{m'}Y_{\ell m'}] W^+_{R\mu}\gamma^\mu P_R\ell^-+\mathrm{H.c.}\) (Eq. 5) heavy-neutrino part | `LWRLeptonsNonHC`: \(-g_{WR\ell}Y_{\ell N}\bar N\gamma^\mu P_R\ell\,W^+_{R\mu}\), plus h.c. | agree | Heavy Majorana-neutrino charged current matches coefficient, chirality, and flavor structure. |
| Eq. (5) light-neutrino part with charge-conjugated light neutrino \(\nu_m^c X_{\ell m}\) | `LWRLightNuNonHC`: \(-g_{WR\ell}X_{\ell\nu}\bar\nu\gamma^\mu P_R\ell\,W^+_{R\mu}\) | disagree | Reconstruction omits the charge conjugation on the light neutrino. This matters for the field identity/chirality, even though the benchmark sets \(X_{\ell m}=0\). |
| Mixing scaling \(|Y_{\ell m'}|^2\sim O(1)\), \(|X_{\ell m}|^2\sim O(m_\nu/m_N)\) (Eq. 6) | External parameters `YR`, `XL`; `YR` identity, `XL` zero by default | agree | Reconstruction encodes the benchmark values, not the scaling statement itself. |
| Benchmark lepton mixing: \(Y\) diagonal with unit entries and all other \(Y\), all \(X\) zero (Eq. 7) | `YR` identity matrix, `XL` zero matrix | agree | Assuming generation labels \(N_1,N_2,N_3\), this matches \(eN_1,\mu N_2,\tau N_3\). |
| \( \mathcal L_{Z_Rff}= -\kappa_R^f g\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}\sum_f \bar f Z_{R\mu}\gamma^\mu(g^{ZR,f}_LP_L+g^{ZR,f}_RP_R)f\) (Eq. 8) | `LZRQuarks` and `LZRLeptons` with \(g_{ZRq,\ell}=-\kappa_R^{q,\ell}e/s_w\sqrt{1-(s_w/(c_w\kappa_R^{q,\ell}))^2}\) | agree | Coefficient structure is equivalent because \(g=e/s_w\) and \(\tan\theta_W=s_w/c_w\). |
| \(g^{ZR,f}_L=(T_L^{3,f}-Q_f)\tan^2\theta_W/(\kappa_R^f)^2\) (Eq. 9) for quarks | \(g_{ZRuL}=g_{ZRdL}=-\frac16(s_w/(c_w\kappa_R^q))^2\) | agree | Matches \(u_L: 1/2-2/3=-1/6\), \(d_L:-1/2+1/3=-1/6\). |
| Eq. (9) for charged leptons and light neutrinos | \(g_{ZReL}=+\frac12(s_w/(c_w\kappa_R^\ell))^2\), \(g_{ZR\nu L}=+\frac12(s_w/(c_w\kappa_R^\ell))^2\) | agree | Matches \(e_L:-1/2-(-1)=1/2\), \(\nu_L:1/2-0=1/2\). |
| \(g^{ZR,f}_R=T_R^{3,f}-Q_f\tan^2\theta_W/(\kappa_R^f)^2\) (Eq. 10) for quarks | \(g_{ZRuR}=1/2-\frac23(s_w/(c_w\kappa_R^q))^2\), \(g_{ZRdR}=-1/2+\frac13(s_w/(c_w\kappa_R^q))^2\) | agree | Matches Table I \(T_R^3\) and electric charges. |
| Eq. (10) for charged leptons and heavy neutrinos | \(g_{ZReR}=-1/2+(s_w/(c_w\kappa_R^\ell))^2\), \(g_{ZRN R}=1/2\) | agree | Matches \(e_R:T_R^3=-1/2,Q=-1\) and \(N_R:T_R^3=1/2,Q=0\). |
| \(Z_R\) couples to all fermions with \(B-L\) charges, including \(\nu_L\) and \(N_R\) (text before Eq. 8) | `LZRLeptons` includes charged leptons, light neutrinos with \(P_L\), and heavy neutrinos with \(P_R\) | agree | Reconstruction captures both light and heavy neutral lepton neutral currents. |
| \(M_{Z_R}\simeq1.7M_{W_R}\) relation in LRSM but \(M_{W_R}\), \(M_{Z_R}\) treated as independent phenomenological parameters (Eq. 18) | Field table gives \(M_{WR}=3000\), \(M_{ZR}=5070\) | agree | \(5070/3000\simeq1.69\), consistent with the quoted representative relation. |
| Representative masses \(M_{W_R}=3\) TeV, \(m_{N_1}=173.3\) GeV, \(m_{N_2},m_{N_3}=10^{12}\) GeV (Eq. 19) | Field table gives \(M_{WR}=3000\), \(N_1=173.3\), \(N_{2,3}=10^{12}\) | agree | Matches the benchmark values. |
| \(M_{Z_R}=5070\) GeV in Table II for representative parameters | Field table gives \(M_{ZR}=5070\) | agree | Matches Table II. |
| SM Lagrangian with Goldstone couplings in Feynman gauge is implemented along with Eqs. (4)-(8) (Sec. III.A) | Reconstruction says the file contains no covariant-derivative or field-strength kinetic terms and only the listed interaction terms | missing-in-reconstruction | If the reconstruction is intended to describe the full paper model, it omits the SM Lagrangian component explicitly mentioned in the implementation section. If it is scoped only to the sanitized BSM interaction file, this is a scope limitation rather than a physics mismatch. |
| LRSM scalar sector absent/decoupled; non-Abelian \(W_R/Z_R\) interactions not correctly modeled in the effective model (Sec. II.B) | No LRSM scalar terms or non-Abelian \(W_R/Z_R\) self-interactions reconstructed | agree | The absence is consistent with the paper’s stated effective-model limitations. |

## Disagreements and Checks

1. **Light-neutrino charged-current conjugation** — severity: **substantive**.  
   The paper’s Eq. (5) uses \(\nu_m^c X_{\ell m}\), while the reconstruction writes an unconjugated \(\nu_m\); a human should check the original implementation’s particle class and FeynRules conventions to see whether the field is actually the charge-conjugated light neutrino or whether the reconstruction normalized it away incorrectly.

2. **SM Lagrangian absent from reconstruction** — severity: **convention** if `reconstruction.md` is intentionally scoped to the sanitized BSM interaction file, otherwise **substantive**.  
   The paper’s Sec. III.A says the SM Lagrangian is implemented together with Eqs. (4)-(8), so a human should check whether the reconstruction was meant to cover the full UFO/model implementation or only the additional effective LRSM interaction file.

## Overall Assessment

The reconstruction matches the paper’s effective LRSM interaction structure very closely for the central \(W_R\) quark current, heavy-neutrino \(W_R\) lepton current, \(Z_R\) neutral currents, chiral coefficients, coupling normalizations, benchmark mixings, and benchmark masses. The main physics-level mismatch is the light-neutrino \(W_R\) term: the paper writes the light-neutrino contribution with \(\nu^c\), while the reconstruction writes an ordinary \(\nu\), which affects the field/chirality interpretation even though the benchmark sets that mixing to zero. The only other notable gap is scope-related: the reconstruction does not include the SM Lagrangian that the paper says is implemented, but this may be expected if the unavailable implementation file only contained the extra BSM terms.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 7 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

