# Reverse-check review package — `Monotops_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `Monotops/model/Monotops_gen.fr` |
| original model name | `Monotops_gen` (hidden from the agent) |
| paper | Monotops/text/1106.6199.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LMono` (`:=`)

```mathematica
Module[{L0,L1,L120,L121,L120p,sp,sp1,sp2,f1,f2,c1,c2,c3,mu}, L0 := SMET (uqbar[sp1,f1,c1].uq[sp1,f2,c1] A0FC[f1,f2] + uqbar[sp1,f1,c1].Ga[5,sp1,sp2].uq[sp2,f2,c1] B0FC[f1,f2]); L1 := VMET[mu] (uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].uq[sp2,f2,c1] A1FC[f1,f2] + uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].Ga[5,sp2,sp].uq[sp,f2,c1] B1FC[f1,f2]); L120 := phiC[c3] Eps[c1,c2,c3] (CC[dqbar][sp1,f1,c1].dq[sp1,f2,c2] AQS[f1,f2] + CC[dqbar][sp1,f1,c1].Ga[5,sp1,sp2].dq[sp2,f2,c2] BQS[f1,f2]) + phiC[c1] (uqbar[sp1,f1,c1].FMET[sp1] A12S[f1] + uqbar[sp1,f1,c1].Ga[5,sp1,sp2].FMET[sp2] B12S[f1]); L120p := tphiC[c3] Eps[c1,c2,c3] (CC[dqbar][sp1,f1,c1].uq[sp1,f2,c2] tAQS[f1,f2] + CC[dqbar][sp1,f1,c1].Ga[5,sp1,sp2].uq[sp2,f2,c2] tBQS[f1,f2]) + tphiC[c1] (dqbar[sp1,f1,c1].FMET[sp1] tA12S[f1] + dqbar[sp1,f1,c1].Ga[5,sp1,sp2].FMET[sp2] tB12S[f1]); L121 := VC[mu,c3] Eps[c1,c2,c3] (CC[dqbar][sp1,f1,c1].Ga[mu,sp1,sp2].dq[sp2,f2,c2] AQV[f1,f2] + CC[dqbar][sp1,f1,c1].Ga[mu,sp1,sp2].Ga[5,sp2,sp].dq[sp,f2,c2] BQV[f1,f2]) + VC[mu,c1] (uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].FMET[sp2] A12V[f1] + uqbar[sp1,f1,c1].Ga[mu,sp1,sp2].Ga[5,sp2,sp].FMET[sp] B12V[f1]); L0 + L1 + L120 + L121 + $Flag4F*L120p + HC[L0 + L1 + L120 + L121 + $Flag4F*L120p]]
```

## Blank-slate reconstruction

# Reconstructed Physics From `sanitized.fr`

## Lagrangian

Conventions: \(u_i^a\) and \(d_i^a\) are SM up- and down-type Dirac quarks, with generation indices \(i,j=1,2,3\) and colour indices \(a,b,c=1,2,3\). Repeated indices are summed. Charge conjugation is written as
\[
q^c \equiv C\bar q^{\,T},\qquad \overline{q^c}=(q^c)^\dagger\gamma^0 .
\]
The FeynRules object `CC[dqbar]` is therefore written as \(\overline{d_i^{c,a}}\). The colour tensor `Eps[c1,c2,c3]` is \(\epsilon_{abc}\). The model adds the hermitian conjugate of all displayed interaction terms through `HC[...]`.

Let
\[
S\equiv \texttt{SMET},\qquad
X_\mu\equiv \texttt{VMET},\qquad
\chi\equiv \texttt{FMET},
\]
\[
\phi^a\equiv \texttt{phiC},\qquad
\tilde\phi^a\equiv \texttt{tphiC},\qquad
V_\mu^a\equiv \texttt{VC}.
\]

### `L0`

\[
\boxed{
\mathcal L_{\texttt{L0}}
=
S\,
\bar u_i^a
\left[
A0FC_{ij}+B0FC_{ij}\gamma^5
\right]
u_j^a
+\text{h.c.}
}
\]

Equivalently, using chiral projectors,
\[
A0FC_{ij}+B0FC_{ij}\gamma^5
=
(A0FC_{ij}-B0FC_{ij})P_L
+
(A0FC_{ij}+B0FC_{ij})P_R .
\]

### `L1`

\[
\boxed{
\mathcal L_{\texttt{L1}}
=
X_\mu\,
\bar u_i^a\gamma^\mu
\left[
A1FC_{ij}+B1FC_{ij}\gamma^5
\right]
u_j^a
+\text{h.c.}
}
\]

Equivalently,
\[
A1FC_{ij}+B1FC_{ij}\gamma^5
=
(A1FC_{ij}-B1FC_{ij})P_L
+
(A1FC_{ij}+B1FC_{ij})P_R .
\]

### `L120`

\[
\boxed{
\mathcal L_{\texttt{L120}}
\supset
\phi^c\,\epsilon_{abc}\,
\overline{d_i^{c,a}}
\left[
AQS_{ij}+BQS_{ij}\gamma^5
\right]
d_j^b
+\text{h.c.}
}
\]

\[
\boxed{
\mathcal L_{\texttt{L120}}
\supset
\phi^a\,
\bar u_i^a
\left[
A12S_i+B12S_i\gamma^5
\right]
\chi
+\text{h.c.}
}
\]

### `L120p`

Since `$Flag4F = 1`, this term is active.

\[
\boxed{
\mathcal L_{\texttt{L120p}}
\supset
\tilde\phi^c\,\epsilon_{abc}\,
\overline{d_i^{c,a}}
\left[
tAQS_{ij}+tBQS_{ij}\gamma^5
\right]
u_j^b
+\text{h.c.}
}
\]

\[
\boxed{
\mathcal L_{\texttt{L120p}}
\supset
\tilde\phi^a\,
\bar d_i^a
\left[
tA12S_i+tB12S_i\gamma^5
\right]
\chi
+\text{h.c.}
}
\]

### `L121`

\[
\boxed{
\mathcal L_{\texttt{L121}}
\supset
V_\mu^c\,\epsilon_{abc}\,
\overline{d_i^{c,a}}\gamma^\mu
\left[
AQV_{ij}+BQV_{ij}\gamma^5
\right]
d_j^b
+\text{h.c.}
}
\]

\[
\boxed{
\mathcal L_{\texttt{L121}}
\supset
V_\mu^a\,
\bar u_i^a\gamma^\mu
\left[
A12V_i+B12V_i\gamma^5
\right]
\chi
+\text{h.c.}
}
\]

### Full `LMono`

\[
\boxed{
\mathcal L_{\texttt{LMono}}
=
\mathcal L_{\texttt{L0}}
+
\mathcal L_{\texttt{L1}}
+
\mathcal L_{\texttt{L120}}
+
\mathcal L_{\texttt{L121}}
+
\mathcal L_{\texttt{L120p}}
}
\]

The file contains no explicit `DC[...]` covariant derivatives or `FS[...]` field-strength terms. From the declared quantum numbers, all new states are \(SU(2)_L\) singlets. With convention
\[
D_\mu=\partial_\mu-i g_s G_\mu^A T_R^A-i g'Y B_\mu ,
\]
the colour-singlet neutral fields \(S\), \(X_\mu\), and \(\chi\) have \(D_\mu=\partial_\mu\). The colour-triplet fields \(\phi^a\), \(\tilde\phi^a\), and \(V_\mu^a\) use the fundamental \(SU(3)_c\) generators \(T^A\), with hypercharges \(Y=2/3\), \(-1/3\), and \(2/3\), respectively. There is no \(SU(2)_L\) gauge term.

## Field Table

| `.fr` symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)_Y\) / electric charge | Self-conjugate? | Mass |
|---|---:|---:|---:|---:|---|---|
| `FMET` | \(1/2\) | \(\mathbf 1\) | singlet | \(Y=0,\ Q=0\) | yes, Majorana-like | `MFM = 50` |
| `VMET` | \(1\) | \(\mathbf 1\) | singlet | \(Y=0,\ Q=0\) | yes, real vector | `MVM = 50.` |
| `VC` | \(1\) | \(\mathbf 3\) | singlet | \(Y=2/3,\ Q=2/3\) | no | `MVC = 500` |
| `SMET` | \(0\) | \(\mathbf 1\) | singlet | \(Y=0,\ Q=0\) | yes, real scalar | `MSM = 50` |
| `phiC` | \(0\) | \(\mathbf 3\) | singlet | \(Y=2/3,\ Q=2/3\) | no | `MSC = 1000` |
| `tphiC` | \(0\) | \(\mathbf 3\) | singlet | \(Y=-1/3,\ Q=-1/3\) | no | `tMSC = 1000` |

## Parameters

| Parameter | Multiplies | Physical meaning | Default nonzero entries |
|---|---|---|---|
| `A0FC[i,j]` | \(S\,\bar u_i u_j\) | scalar flavour-changing up-quark coupling to `SMET` | \(A0FC_{13}=A0FC_{31}=0.1\) |
| `B0FC[i,j]` | \(S\,\bar u_i\gamma^5 u_j\) | pseudoscalar up-quark coupling to `SMET` | all zero |
| `A1FC[i,j]` | \(X_\mu\,\bar u_i\gamma^\mu u_j\) | vector flavour-changing up-quark coupling to `VMET` | \(A1FC_{13}=A1FC_{31}=0.1\) |
| `B1FC[i,j]` | \(X_\mu\,\bar u_i\gamma^\mu\gamma^5 u_j\) | axial-vector up-quark coupling to `VMET` | all zero |
| `A12S[i]` | \(\phi^a\,\bar u_i^a\chi\) | scalar coupling between `phiC`, up quark, and `FMET` | \(A12S_3=0.1\) |
| `B12S[i]` | \(\phi^a\,\bar u_i^a\gamma^5\chi\) | pseudoscalar coupling between `phiC`, up quark, and `FMET` | all zero |
| `tA12S[i]` | \(\tilde\phi^a\,\bar d_i^a\chi\) | scalar coupling between `tphiC`, down quark, and `FMET` | \(tA12S_1=tA12S_2=0.1\) |
| `tB12S[i]` | \(\tilde\phi^a\,\bar d_i^a\gamma^5\chi\) | pseudoscalar coupling between `tphiC`, down quark, and `FMET` | all zero |
| `AQS[i,j]` | \(\phi^c\epsilon_{abc}\overline{d_i^{c,a}}d_j^b\) | scalar diquark coupling of `phiC` to two down quarks | \(AQS_{12}=0.1,\ AQS_{21}=-0.1\) |
| `BQS[i,j]` | \(\phi^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^5 d_j^b\) | pseudoscalar diquark coupling of `phiC` to two down quarks | all zero |
| `tAQS[i,j]` | \(\tilde\phi^c\epsilon_{abc}\overline{d_i^{c,a}}u_j^b\) | scalar diquark coupling of `tphiC` to down-up quark pair | \(tAQS_{13}=0.1,\ tAQS_{23}=0.1\) |
| `tBQS[i,j]` | \(\tilde\phi^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^5 u_j^b\) | pseudoscalar diquark coupling of `tphiC` to down-up quark pair | all zero |
| `A12V[i]` | \(V_\mu^a\,\bar u_i^a\gamma^\mu\chi\) | vector coupling between `VC`, up quark, and `FMET` | \(A12V_3=0.1\) |
| `B12V[i]` | \(V_\mu^a\,\bar u_i^a\gamma^\mu\gamma^5\chi\) | axial-vector coupling between `VC`, up quark, and `FMET` | all zero |
| `AQV[i,j]` | \(V_\mu^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^\mu d_j^b\) | vector diquark coupling of `VC` to two down quarks | \(AQV_{11}=0.1\) |
| `BQV[i,j]` | \(V_\mu^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^\mu\gamma^5 d_j^b\) | axial-vector diquark coupling of `VC` to two down quarks | all zero |

## Physics Summary

The file encodes a simplified extension of the SM with neutral missing-energy states: a real scalar `SMET`, real vector `VMET`, and self-conjugate fermion `FMET`, plus coloured scalar and vector mediators carrying \(SU(3)_c\) triplet quantum numbers. The neutral scalar/vector couple flavour off-diagonally to up-type quarks, while the coloured mediators couple both to quark pairs through antisymmetric colour contractions and to a quark plus the neutral fermion. It mediates flavour-changing up-quark processes, diquark resonances, and quark-initiated production of invisible `FMET` states through coloured scalar or vector exchange.

## Paper cross-check

# Comparison of `reconstruction.md` Against the Paper Model

## Located Paper Definitions

The relevant model definition is in the paper section **“EFFECTIVE THEORY FOR MONOTOPS”**. The field content is introduced immediately before Eq. (1): the paper denotes by \(\phi,\chi,V\) the scalar, fermionic, and vector missing-energy particles, and by \(\varphi,X\) colored scalar and vector fields in the fundamental representation of \(SU(3)_c\). The complete effective interaction Lagrangian is given in **Eq. (1)**, followed by explanatory text specifying charge conjugation, color indices, flavor matrices, and the symmetry consequences of the \(\epsilon_{ijk}\) tensor. Benchmark coupling choices are later stated in **“MODEL-INDEPENDENT SEARCHES”**, after the sentence beginning “To illustrate the main features...”.

## Term-by-Term Comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field definitions: \(\phi,\chi,V\) are scalar, fermionic, and vector missing-energy particles; \(\varphi,X\) are colored scalar/vector fields in fundamental \(SU(3)_c\) representations, “EFFECTIVE THEORY FOR MONOTOPS” before Eq. (1). | \(S=\texttt{SMET}\), \(\chi=\texttt{FMET}\), \(X_\mu=\texttt{VMET}\), \(\phi^a=\texttt{phiC}\), \(\tilde\phi^a=\texttt{tphiC}\), \(V_\mu^a=\texttt{VC}\). | agree | Physics mapping is consistent, but notation is potentially confusing: reconstruction’s neutral vector \(X_\mu\) corresponds to paper’s \(V_\mu\), while reconstruction’s colored vector \(V_\mu^a\) corresponds to paper’s \(X_{\mu,i}\). |
| \(L_{\rm SM}\), Eq. (1). | Included only implicitly as \(\mathcal L_{\texttt{LMono}}\) interactions; reconstruction focuses on BSM terms. | missing-in-reconstruction | Acceptable if reconstruction is only of the new model file interactions, but the paper’s Eq. (1) explicitly includes \(L_{\rm SM}\). |
| \(\phi\,\bar u\,[a^0_{FC}+b^0_{FC}\gamma^5]\,u\), Eq. (1). | \(S\,\bar u_i^a[A0FC_{ij}+B0FC_{ij}\gamma^5]u_j^a+\text{h.c.}\) | agree | Same neutral scalar flavor-changing up-quark coupling; reconstruction makes flavor/color indices explicit. |
| \(V_\mu\,\bar u\,[a^1_{FC}\gamma^\mu+b^1_{FC}\gamma^\mu\gamma^5]\,u\), Eq. (1). | \(X_\mu\,\bar u_i^a\gamma^\mu[A1FC_{ij}+B1FC_{ij}\gamma^5]u_j^a+\text{h.c.}\) | agree | Same neutral vector flavor-changing up-quark coupling; \(\gamma^\mu(A+B\gamma^5)\) is equivalent to \(A\gamma^\mu+B\gamma^\mu\gamma^5\). |
| \(\epsilon_{ijk}\varphi_i\,\bar d^c_j[a^q_{SR}+b^q_{SR}\gamma^5]d_k\), Eq. (1). | \(\phi^c\epsilon_{abc}\overline{d_i^{c,a}}[AQS_{ij}+BQS_{ij}\gamma^5]d_j^b+\text{h.c.}\) | agree | Same colored scalar diquark coupling to two down-type quarks with antisymmetric color tensor. Reconstruction uses separate color and generation indices. |
| \(\varphi_i\,\bar u_i[a^{1/2}_{SR}+b^{1/2}_{SR}\gamma^5]\chi\), Eq. (1). | \(\phi^a\bar u_i^a[A12S_i+B12S_i\gamma^5]\chi+\text{h.c.}\) | agree | Same colored scalar coupling to an up-type quark and invisible fermion. |
| \(\epsilon_{ijk}\tilde\varphi_i\,\bar d^c_j[\tilde a^q_{SR}+\tilde b^q_{SR}\gamma^5]u_k\), Eq. (1). | \(\tilde\phi^c\epsilon_{abc}\overline{d_i^{c,a}}[tAQS_{ij}+tBQS_{ij}\gamma^5]u_j^b+\text{h.c.}\) | agree | Same additional scalar coupling used for four-fermion interactions, with down-charge-conjugate/up bilinear. |
| \(\tilde\varphi_i\,\bar d_i[\tilde a^{1/2}_{SR}+\tilde b^{1/2}_{SR}\gamma^5]\chi\), Eq. (1). | \(\tilde\phi^a\bar d_i^a[tA12S_i+tB12S_i\gamma^5]\chi+\text{h.c.}\) | agree | Same additional scalar coupling to a down-type quark and invisible fermion. |
| \(\epsilon_{ijk}X_{\mu,i}\bar d^c_j[a^q_{VR}\gamma^\mu+b^q_{VR}\gamma^\mu\gamma^5]d_k\), Eq. (1). | \(V_\mu^c\epsilon_{abc}\overline{d_i^{c,a}}\gamma^\mu[AQV_{ij}+BQV_{ij}\gamma^5]d_j^b+\text{h.c.}\) | agree | Same colored vector diquark coupling. Reconstruction includes \(BQV\), but its defaults set it to zero, matching the paper’s later benchmark choice. |
| \(X_{\mu,i}\bar u_i[a^{1/2}_{VR}\gamma^\mu+b^{1/2}_{VR}\gamma^\mu\gamma^5]\chi\), Eq. (1). | \(V_\mu^a\bar u_i^a\gamma^\mu[A12V_i+B12V_i\gamma^5]\chi+\text{h.c.}\) | agree | Same colored vector coupling to an up-type quark and invisible fermion. |
| Eq. (1) ends with \(+\text{h.c.}\). | Reconstruction states all displayed interaction terms have `HC[...]`. | agree | Hermitian conjugation is consistently included. |
| Text after Eq. (1): \(c\) denotes charge conjugation; color indices are fundamental; flavor indices are understood. | Reconstruction defines \(q^c=C\bar q^T\), \(\overline{q^c}\), \(\epsilon_{abc}\), and explicit flavor/color sums. | agree | Conjugation and index structure are compatible. |
| Text after Eq. (1): identical-quark couplings to scalar \(\varphi\) vanish, and axial couplings to vector \(X\) vanish, due to \(\epsilon_{ijk}\) symmetry. | Reconstruction parameter defaults include \(AQS_{12}=0.1\), \(AQS_{21}=-0.1\), \(AQV_{11}=0.1\), all \(BQV=0\). | agree | The benchmark choices respect the stated scalar antisymmetry and vanishing vector axial benchmark coupling. |
| Benchmark after Eq. (1): all axial couplings involving new particles vanish, \(b=\tilde b=0\). | Reconstruction defaults set all \(B\)-type couplings to zero. | agree | Matches the paper’s illustrative scenarios. |
| Benchmark after Eq. (1): \((a^0_{FC})_{13}=(a^0_{FC})_{31}=(a^1_{FC})_{13}=(a^1_{FC})_{31}=(a^q_{SR})_{12}=-(a^q_{SR})_{21}=(a^{1/2}_{SR})_3=(a^q_{VR})_{11}=(a^{1/2}_{VR})_3=a=0.1\). | Reconstruction defaults list \(A0FC_{13}=A0FC_{31}=0.1\), \(A1FC_{13}=A1FC_{31}=0.1\), \(AQS_{12}=0.1\), \(AQS_{21}=-0.1\), \(A12S_3=0.1\), \(AQV_{11}=0.1\), \(A12V_3=0.1\). | agree | Coupling pattern matches the paper’s nonzero benchmark entries. |
| Four-fermion benchmark: \((a^q_{SR})_{12}=-(a^q_{SR})_{21}=(\tilde a^q_{SR})_{\{1,2\}3}=(\tilde a^{1/2}_{SR})_{\{1,2\}}=a=0.1\). | Reconstruction defaults list \(tAQS_{13}=tAQS_{23}=0.1\), \(tA12S_1=tA12S_2=0.1\). | agree | Same four-fermion-limit nonzero entries. |
| Paper does not explicitly assign \(SU(2)_L\) representations or hypercharges in Eq. (1); it works in mass eigenstates. | Reconstruction states all new states are \(SU(2)_L\) singlets and assigns \(Y=0,2/3,-1/3\) as appropriate. | extra-in-reconstruction | These assignments are consistent with electric charge conservation under a singlet assumption, but they are not explicitly specified by the paper’s effective Lagrangian. |
| Paper treats \(\chi\) as a possible invisible fermionic particle and discusses massive or massless fermionic missing energy; it does not require Majorana self-conjugacy in Eq. (1). | Reconstruction says `FMET` is “self-conjugate, Majorana-like.” | extra-in-reconstruction | This is a stronger field-property assumption than the paper states. |
| Paper treats \(\phi\) and \(V\) as neutral missing-energy bosonic states, without explicitly declaring real versus complex fields in Eq. (1). | Reconstruction says `SMET` is a real scalar and `VMET` is a real vector. | extra-in-reconstruction | Reasonable for neutral invisible particles, but not fixed by the paper text shown in Eq. (1). |
| Paper benchmark masses: resonant \(\varphi,X\) mass fixed to \(500\) GeV; four-fermion heavy masses \(M_\varphi=M_{\tilde\varphi}=3\) TeV; invisible masses vary by scenario. | Reconstruction field table lists defaults such as \(M_{\chi}=50\), \(M_{V_{\rm MET}}=50\), \(M_{VC}=500\), \(M_{\phi C}=1000\), \(M_{\tilde\phi C}=1000\). | disagree | The interaction Lagrangian agrees, but the reconstruction’s listed default masses do not reproduce all paper benchmark mass choices. |

## Disagreements and Human Checks

1. **\(L_{\rm SM}\) omission — severity: convention.** A human should check whether `reconstruction.md` intentionally reconstructs only the BSM FeynRules interactions or whether the full model file should include/import the Standard Model Lagrangian.

2. **Extra electroweak quantum numbers — severity: convention.** A human should check the implementation file’s actual class declarations to confirm whether \(SU(2)_L\) singlet and hypercharge assignments were explicit model choices or inferred by the reconstruction.

3. **Self-conjugate invisible fermion \(\chi\) — severity: substantive.** A human should check whether `FMET` is declared self-conjugate in the implementation, because the paper’s Eq. (1) does not require \(\chi\) to be Majorana-like.

4. **Real neutral scalar/vector assumptions — severity: convention.** A human should check whether `SMET` and `VMET` are explicitly self-conjugate in the implementation, since the paper only identifies them as neutral invisible bosonic states.

5. **Default mass values versus paper scenarios — severity: substantive for phenomenology, not for the interaction Lagrangian.** A human should check whether the reconstruction is reporting arbitrary implementation defaults or the benchmark masses used for the paper’s five scenarios.

6. **Notation swap \(V/X\) — severity: cosmetic.** A human should check any downstream comparison carefully because the reconstruction uses \(X_\mu\) for the paper’s neutral vector \(V_\mu\), and \(V_\mu^a\) for the paper’s colored vector \(X_{\mu,i}\).

## Overall Assessment

The reconstructed interaction Lagrangian matches the physics content of the paper’s Eq. (1) term by term: the neutral scalar/vector flavor-changing up-quark interactions, the colored scalar and vector diquark couplings, the quark-\(\chi\) mediator couplings, the tilde-scalar four-fermion-limit interactions, hermitian conjugation, charge-conjugated down-quark structure, color antisymmetry, and the benchmark nonzero coupling pattern are all represented consistently. The main caveats are outside the core interaction terms: the reconstruction adds electroweak representation, hypercharge, self-conjugacy, and default mass information that the paper either leaves unspecified or varies by scenario.

## Suggested checks for the reviewer

1. Every verbatim `.fr` term above has a reconstructed LaTeX counterpart with the same field content, chirality and conjugation.
2. Kinetic terms: covariant derivative gauge content matches the field's representations; normalization is canonical.
3. Non-self-conjugate interaction terms appear together with their Hermitian conjugates.
4. Quantum numbers in the field table match the `.fr` declarations (and the paper, where the cross-check table flags disagreements).
5. Numeric masses/couplings are placeholders unless the paper pins them — treat values as demo inputs, not measurements.
6. Sanitizer scope: 22 prose labels were scrubbed; field/parameter symbol names were kept and may hint at the model's identity.

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:

