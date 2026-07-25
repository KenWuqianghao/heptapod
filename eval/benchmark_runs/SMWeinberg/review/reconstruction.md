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