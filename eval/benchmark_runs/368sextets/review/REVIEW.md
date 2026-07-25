# Reverse-check review package — `368sextets_gen`

An independent, **blank-slate** agent instance reconstructed the physics below from the sanitized `.fr` alone (no paper, no metadata, no conversation history). A second fresh instance then compared the reconstruction against the source paper. The final verdict belongs to the human reviewer — sign off at the bottom.

| item | value |
|---|---|
| model file | `368sextets/repair/final.fr` |
| original model name | `368sextets_gen` (hidden from the agent) |
| paper | 368sextets/text/2110.11359.txt |
| blindness scope | blank slate w.r.t. paper, authors, model name, comments and prose labels — NOT w.r.t. field/parameter symbol names, which are kept so the reviewer can map the reconstruction back |

## Verbatim Lagrangian terms (from the `.fr`)

These are the terms the reconstruction must account for, quoted unmodified. Check each against its reconstructed LaTeX form below.

### `LSextetKin` (`:=`)

```mathematica
sFubar[ss,kk].(I Ga[mu,ss,rr].DC[sFu[rr,kk],mu] - MFu sFu[ss,kk]) + sFdbar[ss,kk].(I Ga[mu,ss,rr].DC[sFd[rr,kk],mu] - MFd sFd[ss,kk]) + DC[sSubar[kk], mu] DC[sSu[kk],mu] - MSu^2 sSubar[kk] sSu[kk] + DC[sSdbar[kk], mu] DC[sSd[kk],mu] - MSd^2 sSdbar[kk] sSd[kk]
```

### `LFu` (`:=`)

```mathematica
CFu[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFubar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CFu[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFubar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii]] FS[G,mu,nu,aa] + CFBu[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFubar[ss,kk].CC[uR][ss,mm,ii] FS[G,mu,nu,aa] FS[B,mu,nu] + HC[CFBu[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFubar[ss,kk].CC[uR][ss,mm,ii]] FS[G,mu,nu,aa] FS[B,mu,nu]
```

### `LFd` (`:=`)

```mathematica
CFd[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFdbar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CFd[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFdbar[ss,kk].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii]] FS[G,mu,nu,aa] + CFBd[mm] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sFdbar[ss,kk].CC[dR][ss,mm,ii] FS[G,mu,nu,aa] FS[B,mu,nu] + HC[CFBd[mm]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sFdbar[ss,kk].CC[dR][ss,mm,ii]] FS[G,mu,nu,aa] FS[B,mu,nu]
```

### `LSu` (`:=`)

```mathematica
CSu[mm,ll] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sSubar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CSu[mm,ll]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sSubar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[uR][tt,mm,ii] FS[G,mu,nu,aa]]
```

### `LSd` (`:=`)

```mathematica
CSd[mm,ll] I Sqrt[2] K6[kk,yy,zz] T[aa,zz,xx] K3bar[ii,xx,yy] sSdbar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii] FS[G,mu,nu,aa] + HC[CSd[mm,ll]] (-I Sqrt[2]) K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy] HC[sSdbar[kk] lRbar[ss,ll].(I/2)(Ga[mu,ss,rr].Ga[nu,rr,tt]-Ga[nu,ss,rr].Ga[mu,rr,tt]).CC[dR][tt,mm,ii] FS[G,mu,nu,aa]]
```

### `LTot` (`:=`)

```mathematica
LSextetKin + LFu + LFd + LSu + LSd
```

## Blank-slate reconstruction

# Reconstructed Model From `sanitized.fr`

## Notation

Generation indices are \(m,\ell\). Color triplet indices are \(i,x,y,z\), adjoint color index is \(a\), and sextet index is \(k=1,\dots,6\). Repeated indices are summed.

The file defines the color tensor
\[
\mathcal C^{a}_{ki}
\equiv
\sqrt{2}\,
K_6{}_{k y z}\,
(T^a)_{z x}\,
\bar K_3{}_{i x y},
\]
with hermitian-conjugate tensor
\[
\mathcal C^{a\,*}_{ki}
=
\sqrt{2}\,
K_3{}_{i x y}\,
(T^a)_{x z}\,
\bar K_6{}_{k z y}.
\]

The FeynRules expression
\[
\frac{i}{2}\left(\gamma^\mu\gamma^\nu-\gamma^\nu\gamma^\mu\right)
\]
is written as
\[
\sigma^{\mu\nu}.
\]

Charge conjugation is
\[
q_R^c \equiv C \bar q_R^{\,T}.
\]

The fields are all \(SU(2)_L\) singlets. For a field \(\Phi_k\) in the sextet representation with hypercharge \(Y_\Phi\),
\[
D_\mu \Phi_k
=
\partial_\mu \Phi_k
+ i g_s G_\mu^a (T_6^a)_{k k'} \Phi_{k'}
+ i g' Y_\Phi B_\mu \Phi_k .
\]
For the conjugate field,
\[
D_\mu \Phi^\dagger_k
=
\partial_\mu \Phi^\dagger_k
- i g_s G_\mu^a \Phi^\dagger_{k'}(T_6^a)_{k'k}
- i g' Y_\Phi B_\mu \Phi^\dagger_k .
\]

The field strengths are
\[
G^a_{\mu\nu}=FS[G,\mu,\nu,a],
\qquad
B_{\mu\nu}=FS[B,\mu,\nu].
\]

## Lagrangian

### `LSextetKin`

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
\bar sFu_k
\left(
i\gamma^\mu D_\mu - M_{Fu}
\right)
sFu_k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
\bar sFd_k
\left(
i\gamma^\mu D_\mu - M_{Fd}
\right)
sFd_k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu sSu^\dagger_k)(D^\mu sSu_k)
-
M_{Su}^2 sSu^\dagger_k sSu_k .
\]

\[
\mathcal L_{\texttt{LSextetKin}}
\supset
(D_\mu sSd^\dagger_k)(D^\mu sSd_k)
-
M_{Sd}^2 sSd^\dagger_k sSd_k .
\]

The covariant derivatives use the following hypercharges:
\[
Y_{sFu}=-\frac23,\qquad
Y_{sFd}=+\frac13,\qquad
Y_{sSu}=+\frac13,\qquad
Y_{sSd}=+\frac43.
\]

### `LFu`

\[
\mathcal L_{\texttt{LFu}}
\supset
i\, C_{Fu}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFu_k\,
\sigma^{\mu\nu}
(u_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

\[
\mathcal L_{\texttt{LFu}}
\supset
i\, C_{FBu}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFu_k\,
(u_R^c)_{m i}\,
G^a_{\mu\nu}B^{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Fu}^{m}=CFuR_m+i\,CFuI_m,
\qquad
C_{FBu}^{m}=CFBuR_m+i\,CFBuI_m .
\]

### `LFd`

\[
\mathcal L_{\texttt{LFd}}
\supset
i\, C_{Fd}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFd_k\,
\sigma^{\mu\nu}
(d_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

\[
\mathcal L_{\texttt{LFd}}
\supset
i\, C_{FBd}^{m}\,
\mathcal C^{a}_{ki}\,
\bar sFd_k\,
(d_R^c)_{m i}\,
G^a_{\mu\nu}B^{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Fd}^{m}=CFdR_m+i\,CFdI_m,
\qquad
C_{FBd}^{m}=CFBdR_m+i\,CFBdI_m .
\]

### `LSu`

\[
\mathcal L_{\texttt{LSu}}
\supset
i\, C_{Su}^{m\ell}\,
\mathcal C^{a}_{ki}\,
sSu^\dagger_k\,
\bar \ell_{R\ell}\,
\sigma^{\mu\nu}
(u_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Su}^{m\ell}=CSuR_{m\ell}+i\,CSuI_{m\ell}.
\]

### `LSd`

\[
\mathcal L_{\texttt{LSd}}
\supset
i\, C_{Sd}^{m\ell}\,
\mathcal C^{a}_{ki}\,
sSd^\dagger_k\,
\bar \ell_{R\ell}\,
\sigma^{\mu\nu}
(d_R^c)_{m i}\,
G^a_{\mu\nu}
+
\text{h.c.}
\]

where
\[
C_{Sd}^{m\ell}=CSdR_{m\ell}+i\,CSdI_{m\ell}.
\]

### `LTot`

\[
\mathcal L_{\texttt{LTot}}
=
\mathcal L_{\texttt{LSextetKin}}
+
\mathcal L_{\texttt{LFu}}
+
\mathcal L_{\texttt{LFd}}
+
\mathcal L_{\texttt{LSu}}
+
\mathcal L_{\texttt{LSd}} .
\]

## Field Table

| Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)_Y\) | Electric charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---:|---|---|
| `sFu` | \(1/2\) Dirac fermion | \(\mathbf 6\) | \(\mathbf 1\) | \(-2/3\) | \(-2/3\) | No | \(M_{Fu}=500\) |
| `sFd` | \(1/2\) Dirac fermion | \(\mathbf 6\) | \(\mathbf 1\) | \(+1/3\) | \(+1/3\) | No | \(M_{Fd}=500\) |
| `sSu` | scalar | \(\mathbf 6\) | \(\mathbf 1\) | \(+1/3\) | \(+1/3\) | No | \(M_{Su}=500\) |
| `sSd` | scalar | \(\mathbf 6\) | \(\mathbf 1\) | \(+4/3\) | \(+4/3\) | No | \(M_{Sd}=500\) |

The antiparticles transform in the conjugate color representation \(\bar{\mathbf 6}\) with opposite gauge charges.

## External Parameters

| External parameter | Default | Multiplies | Physical meaning |
|---|---:|---|---|
| `CFBuR[m]` | \(0.1\) | Real part of \(C_{FBu}^m\) in `LFu` | Coupling of \(\bar sFu\,u_R^c\,G_{\mu\nu}B^{\mu\nu}\) |
| `CFBuI[m]` | \(0\) | Imaginary part of \(C_{FBu}^m\) in `LFu` | CP-odd/complex phase component of the same coupling |
| `CFBdR[m]` | \(0.1\) | Real part of \(C_{FBd}^m\) in `LFd` | Coupling of \(\bar sFd\,d_R^c\,G_{\mu\nu}B^{\mu\nu}\) |
| `CFBdI[m]` | \(0\) | Imaginary part of \(C_{FBd}^m\) in `LFd` | CP-odd/complex phase component of the same coupling |
| `CFuR[m]` | \(0.1\) | Real part of \(C_{Fu}^m\) in `LFu` | Chromomagnetic-type coupling \(\bar sFu\,\sigma^{\mu\nu}u_R^c\,G^a_{\mu\nu}\) |
| `CFuI[m]` | \(0\) | Imaginary part of \(C_{Fu}^m\) in `LFu` | CP-odd/complex phase component of the same coupling |
| `CFdR[m]` | \(0.1\) | Real part of \(C_{Fd}^m\) in `LFd` | Chromomagnetic-type coupling \(\bar sFd\,\sigma^{\mu\nu}d_R^c\,G^a_{\mu\nu}\) |
| `CFdI[m]` | \(0\) | Imaginary part of \(C_{Fd}^m\) in `LFd` | CP-odd/complex phase component of the same coupling |
| `CSuR[m,l]` | \(0.1\) | Real part of \(C_{Su}^{m\ell}\) in `LSu` | Coupling of \(sSu^\dagger\,\bar\ell_R\,\sigma^{\mu\nu}u_R^c\,G^a_{\mu\nu}\) |
| `CSuI[m,l]` | \(0\) | Imaginary part of \(C_{Su}^{m\ell}\) in `LSu` | CP-odd/complex phase component of the same coupling |
| `CSdR[m,l]` | \(0.1\) | Real part of \(C_{Sd}^{m\ell}\) in `LSd` | Coupling of \(sSd^\dagger\,\bar\ell_R\,\sigma^{\mu\nu}d_R^c\,G^a_{\mu\nu}\) |
| `CSdI[m,l]` | \(0\) | Imaginary part of \(C_{Sd}^{m\ell}\) in `LSd` | CP-odd/complex phase component of the same coupling |

## Physics Summary

The file encodes four new color-sextet, electroweak-singlet states: two Dirac fermions with charges \(-2/3\) and \(+1/3\), and two complex scalars with charges \(+1/3\) and \(+4/3\). Their interactions are higher-dimensional operators coupling them to right-handed charge-conjugated up- or down-type quarks, gluon field strengths, and in two fermion operators also the hypercharge field strength.

The model mediates processes involving color-sextet resonances connected to quarks plus gluons, and scalar sextet interactions involving a charged right-handed lepton, a charge-conjugated right-handed quark, and a gluon. These operators can generate exotic colored-particle production and decays into quark-gluon or lepton-quark-gluon final states, with generation-dependent complex couplings.

## Paper cross-check

**Paper Model References**

The model targeted by the reconstruction is defined in **Section III, “Sextets at the LHC”**. The explicit fermion Lagrangian is **Eq. (12)**, the scalar Lagrangian is **Eq. (13)**, and the exotic field quantum numbers are summarized in **Table X**. The relevant operator catalog entry is **Table IX**, based on the color invariant \(3\otimes 6\otimes 8\). The color Clebsch-Gordan conventions for \(J_{sia}\) and \(\bar J_{sai}\) are given in **Appendix A**, especially **Eqs. (A15)–(A18)**.

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| \(\Psi_u\sim(6,1,-2/3)\), \(L=0\) (**Table X**) | `sFu`: Dirac fermion, \((6,1,-2/3)\), charge \(-2/3\) | agree | Gauge quantum numbers and spin agree. Reconstruction omits the paper’s explicit lepton-number assignment \(L=0\). |
| \(\Psi_d\sim(6,1,+1/3)\), \(L=0\) (**Table X**) | `sFd`: Dirac fermion, \((6,1,+1/3)\), charge \(+1/3\) | agree | Gauge quantum numbers and spin agree. Reconstruction omits \(L=0\). |
| \(\Phi_u\sim(6,1,+1/3)\), \(L=-1\) (**Table X**) | `sSu`: scalar, \((6,1,+1/3)\), charge \(+1/3\) | agree | Gauge quantum numbers and spin agree. Reconstruction omits the scalar lepton number \(L=-1\). |
| \(\Phi_d\sim(6,1,+4/3)\), \(L=-1\) (**Table X**) | `sSd`: scalar, \((6,1,+4/3)\), charge \(+4/3\) | agree | Gauge quantum numbers and spin agree. Reconstruction omits \(L=-1\). |
| \(\bar\Psi_q(i\!\not\!D-m_{\Psi_q})\Psi_q\) for \(q\in\{u,d\}\) (**Eq. 12**) | \(\bar{sFu}(i\gamma^\mu D_\mu-M_{Fu})sFu\), \(\bar{sFd}(i\gamma^\mu D_\mu-M_{Fd})sFd\) | agree | Same Dirac kinetic and mass structure. Reconstruction names separate masses and gives implementation defaults later. |
| \((D_\mu\Phi_q)^\dagger D^\mu\Phi_q-m_{\Phi_q}^2\Phi_q^\dagger\Phi_q\) for \(q\in\{u,d\}\) (**Eq. 13**) | \((D_\mu sSu^\dagger)(D^\mu sSu)-M_{Su}^2sSu^\dagger sSu\), similarly for `sSd` | agree | Same complex scalar kinetic and mass structure. |
| \(J_{sia}\), \(\bar J_{sai}\) color contraction for \(3\otimes6\otimes8\) (**Table IX**, **App. A**, **Eqs. A15–A18**) | \(\mathcal C^a_{ki}=\sqrt2\,K_6{}_{kyz}(T^a)_{zx}\bar K_3{}_{ixy}\), plus conjugate | agree | This appears to be the implementation form of the paper’s \(J\) tensor using the relation to \(K\), \(L\), and \(t_3^a\) in Eq. (A18). Overall phase/index placement should be checked against the implementation convention. |
| \(\frac{1}{\Lambda_{\Psi_u}}\left[\kappa_u^I J_{sia}(u^c_{RIi}\sigma_{\mu\nu}\Psi_{us})G^{\mu\nu a}+\text{H.c.}\right]\) (**Eq. 12**) | \(i\,C_{Fu}^m\mathcal C^a_{ki}\bar{sFu}_k\sigma^{\mu\nu}(u_R^c)_{mi}G^a_{\mu\nu}+\text{h.c.}\) | disagree | Field content, chirality, gluon field strength, and sextet/up-quark assignment match up to Hermitian conjugation and Dirac-bilinear ordering. Reconstruction does not show the paper’s \(1/\Lambda_{\Psi_u}\) coefficient structure. |
| \(\frac{1}{\Lambda_{\Psi_d}}\left[\kappa_d^I J_{sia}(d^c_{RIi}\sigma_{\mu\nu}\Psi_{ds})G^{\mu\nu a}+\text{H.c.}\right]\) (**Eq. 12**) | \(i\,C_{Fd}^m\mathcal C^a_{ki}\bar{sFd}_k\sigma^{\mu\nu}(d_R^c)_{mi}G^a_{\mu\nu}+\text{h.c.}\) | disagree | Same physics content as the paper operator, but the explicit EFT suppression \(1/\Lambda_{\Psi_d}\) is absent or absorbed without being stated. |
| \(\frac{1}{\Lambda_{\Psi_uB}^3}\left[\kappa_{uB}^I J_{sia}(u^c_{RIi}\Psi_{us})B_{\mu\nu}G^{\mu\nu a}+\text{H.c.}\right]\) (**Eq. 12**) | \(i\,C_{FBu}^m\mathcal C^a_{ki}\bar{sFu}_k(u_R^c)_{mi}G^a_{\mu\nu}B^{\mu\nu}+\text{h.c.}\) | disagree | Correct fields and no \(\sigma_{\mu\nu}\), matching the scalar Lorentz bilinear structure in Eq. (12), but reconstruction omits or absorbs the required \(1/\Lambda^3\). |
| \(\frac{1}{\Lambda_{\Psi_dB}^3}\left[\kappa_{dB}^I J_{sia}(d^c_{RIi}\Psi_{ds})B_{\mu\nu}G^{\mu\nu a}+\text{H.c.}\right]\) (**Eq. 12**) | \(i\,C_{FBd}^m\mathcal C^a_{ki}\bar{sFd}_k(d_R^c)_{mi}G^a_{\mu\nu}B^{\mu\nu}+\text{h.c.}\) | disagree | Same operator content, but the EFT coefficient/cutoff structure differs from the paper unless \(C_{FBd}\) implicitly includes \(1/\Lambda^3\). |
| \(\frac{1}{\Lambda_{\Phi_u}^2}\left[\lambda_u^{XI}J_{sia}\Phi_{us}(u^c_{RIi}\sigma_{\mu\nu}\ell_{RX})G^{\mu\nu a}+\text{H.c.}\right]\) (**Eq. 13**) | \(i\,C_{Su}^{m\ell}\mathcal C^a_{ki}sSu^\dagger_k\bar\ell_{R\ell}\sigma^{\mu\nu}(u_R^c)_{mi}G^a_{\mu\nu}+\text{h.c.}\) | disagree | Reconstruction uses the Hermitian-conjugate-looking form with \(sSu^\dagger\), which is acceptable because the paper includes H.c.; however, the explicit \(1/\Lambda_{\Phi_u}^2\) suppression is missing or absorbed. |
| \(\frac{1}{\Lambda_{\Phi_d}^2}\left[\lambda_d^{XI}J_{sia}\Phi_{ds}(d^c_{RIi}\sigma_{\mu\nu}\ell_{RX})G^{\mu\nu a}+\text{H.c.}\right]\) (**Eq. 13**) | \(i\,C_{Sd}^{m\ell}\mathcal C^a_{ki}sSd^\dagger_k\bar\ell_{R\ell}\sigma^{\mu\nu}(d_R^c)_{mi}G^a_{\mu\nu}+\text{h.c.}\) | disagree | Same comments as the up-type scalar term: field content and charges are consistent through the H.c., but the EFT cutoff factor is not represented explicitly. |
| Paper assigns lepton numbers \(L(\Phi_u)=L(\Phi_d)=-1\), \(L(\Psi_u)=L(\Psi_d)=0\) (**Table X**) | Reconstruction field table has no lepton-number column | missing-in-reconstruction | This is part of the paper’s field definition, not just phenomenological commentary. |
| Paper uses free masses \(m_{\Psi_q}\), \(m_{\Phi_q}\) (**Eqs. 12–13**) | Reconstruction parameter table lists defaults \(M_{Fu}=M_{Fd}=M_{Su}=M_{Sd}=500\) | extra-in-reconstruction | A benchmark/default mass may be implementation-specific, but it is not specified as part of the analytic model definition in Eqs. (12)–(13). |
| Paper coefficients are \(\kappa_q^I/\Lambda_{\Psi_q}\), \(\kappa_{qB}^I/\Lambda_{\Psi_qB}^3\), \(\lambda_q^{XI}/\Lambda_{\Phi_q}^2\) (**Eqs. 12–13**) | Reconstruction coefficients are complex \(C\)-parameters with real/imaginary parts and no displayed \(\Lambda\) | disagree | Complex couplings are compatible in spirit, but the reconstruction changes the coefficient bookkeeping and mass dimension unless the \(C\)’s are explicitly dimensionful Wilson coefficients. |

**Disagreements To Check**

- **Missing scalar and fermion lepton numbers** — severity: **substantive**. A human should check whether the implementation tracks the accidental lepton-number assignments in Table X or intentionally omits them because they do not affect generated vertices.

- **All higher-dimensional operator coefficients lack explicit EFT cutoff powers** — severity: **substantive**. A human should check whether \(C_{Fu},C_{Fd},C_{FBu},C_{FBd},C_{Su},C_{Sd}\) are intended to be dimensionful Wilson coefficients already including \(1/\Lambda\), \(1/\Lambda^2\), or \(1/\Lambda^3\).

- **Scalar operators are written with \(\Phi^\dagger\) and reordered barred spinors rather than the paper’s \(\Phi(q_R^c\sigma\ell_R)\)** — severity: **convention**. A human should verify that the reconstruction corresponds exactly to the Hermitian-conjugate term included in Eq. (13), including coupling conjugation and color tensor conjugation.

- **Fermion operators are written as \(\bar\Psi\,\Gamma\,q_R^c\) rather than the paper’s \((q_R^c\Gamma\Psi)\)** — severity: **convention**. A human should check the Dirac-charge-conjugation convention used by the implementation, especially signs for tensor bilinears.

- **Color tensor \(\mathcal C\) is not named \(J\) and is expressed through \(K\)-type tensors** — severity: **convention**. A human should compare \(\mathcal C\) against Eq. (A18), including the overall phase and index ordering, because a phase can be absorbed into couplings but an index swap cannot always be ignored.

- **Implementation default masses \(500\) appear in the reconstruction** — severity: **cosmetic**. A human should check whether these are merely UFO/FeynRules benchmark defaults rather than claims about the paper’s physical model.

**Overall Assessment**

The reconstruction captures the main field content and operator inventory of the paper’s Section III sextet model: two color-sextet Dirac fermions \(\Psi_u,\Psi_d\), two color-sextet complex scalars \(\Phi_u,\Phi_d\), the correct Standard Model gauge representations, and the intended \(3\otimes6\otimes8\) quark-gluon-sextet interactions. Most apparent differences in chirality ordering, barred fields, conjugated scalars, and the color tensor notation look like implementation or Hermitian-conjugation conventions. The main physics-level gap is coefficient normalization: the paper’s EFT structure is organized by explicit cutoff powers \(1/\Lambda_{\Psi}\), \(1/\Lambda_{\Psi B}^3\), and \(1/\Lambda_\Phi^2\), while the reconstruction replaces these with complex \(C\)-parameters without stating their mass dimension or relation to \(\kappa,\lambda,\Lambda\).

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

