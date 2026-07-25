# Reconstructed Physics From `sanitized.fr`

## Lagrangian

The scalar doublet is declared as
\[
\Phi_i =
\begin{pmatrix}
-i\,G^+\\[2pt]
\dfrac{v_h+c_\theta h+s_\theta h_2+iG^0}{\sqrt2}
\end{pmatrix}_i,
\qquad
c_\theta=\cos\theta,\quad s_\theta=\sin\theta ,
\]
with hypercharge \(Y_\Phi=1/2\). The complex singlet is
\[
S=\frac{v_s-s_\theta h+c_\theta h_2+iX}{\sqrt2}.
\]

The covariant derivative acting on \(\Phi\) is
\[
D_\mu \Phi_i
=
\partial_\mu \Phi_i
+i g\, W^a_\mu (T^a)_{ij}\Phi_j
+i g' Y_\Phi B_\mu \Phi_i,
\qquad Y_\Phi=\frac12,
\]
with no \(SU(3)_c\) coupling. The singlet \(S\) uses an ordinary derivative,
\[
\partial_\mu S,
\]
because it is neutral under \(SU(3)_c\times SU(2)_L\times U(1)_Y\).

The file sets `FeynmanGauge = False`, so Goldstone fields are removed by
\[
G^0=G^+=G^-=0
\]
inside `LHiggsPng` and `Lint`.

### `LHiggsPng`

\[
\mathcal L_{\texttt{LHiggsPng, kin}}
=
(D_\mu\Phi)^\dagger_i(D^\mu\Phi)_i .
\]

\[
\mathcal L_{\texttt{LHiggsPng, mass}}
=
\frac{\mu_\Phi^2}{2}\,\Phi_i^\dagger\Phi_i .
\]

\[
\mathcal L_{\texttt{LHiggsPng, quartic}}
=
-\frac{\lambda_\Phi}{2}
(\Phi_i^\dagger\Phi_i)
(\Phi_j^\dagger\Phi_j).
\]

### `LS`

\[
\mathcal L_{\texttt{LS, kin}}
=
(\partial_\mu S^\dagger)(\partial^\mu S).
\]

\[
\mathcal L_{\texttt{LS, mass}}
=
\frac{\mu_S^2}{2}\,S^\dagger S .
\]

\[
\mathcal L_{\texttt{LS, quartic}}
=
-\frac{\lambda_S}{2}(S^\dagger S)^2 .
\]

### `Lint`

\[
\mathcal L_{\texttt{Lint}}
=
-\lambda_{\Phi S}
(\Phi_i^\dagger\Phi_i)(S^\dagger S).
\]

### `Lsoft`

\[
\mathcal L_{\texttt{Lsoft}}
=
\frac{\mu_S^{\prime 2}}{4}
\left(S^2+S^{\dagger 2}\right).
\]

### Composite Symbols

\[
\mathcal L_{\texttt{LpNG}}
=
\mathcal L_{\texttt{LS}}
+
\mathcal L_{\texttt{Lint}}
+
\mathcal L_{\texttt{Lsoft}} .
\]

\[
\mathcal L_{\texttt{LScalarPng}}
=
\mathcal L_{\texttt{LHiggsPng}}
+
\mathcal L_{\texttt{LpNG}} .
\]

The internal parameter definitions are
\[
\lambda_\Phi
=
\frac{M_h^2 c_\theta^2+M_{h_2}^2 s_\theta^2}{v_h^2},
\]
\[
\lambda_S
=
\frac{M_h^2 s_\theta^2+M_{h_2}^2 c_\theta^2}{v_s^2},
\]
\[
\lambda_{\Phi S}
=
\frac{(M_{h_2}^2-M_h^2)s_\theta c_\theta}{v_h v_s},
\]
\[
\mu_S^{\prime 2}=m_X^2,
\]
\[
\mu_\Phi^2
=
\lambda_\Phi v_h^2+\lambda_{\Phi S}v_s^2,
\]
\[
\mu_S^2
=
\lambda_S v_s^2+\lambda_{\Phi S}v_h^2-\mu_S^{\prime 2}.
\]

## Field Table

| `.fr` class | Symbol | Spin | \(SU(3)_c\) rep | \(SU(2)_L\) rep | \(U(1)_Y\) / charge | Self-conjugate | Mass |
|---|---:|---:|---:|---:|---|---|---|
| `S[2]` | `h2` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | \(M_{h_2}=\texttt{Mh2}=300\) |
| `S[3]` | `X` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | yes | \(m_X=\texttt{mX}=100\) |
| `S[11]` | `Phi[i]` | 0 | singlet | doublet | \(Y=1/2\) | no | unphysical field, no mass declared |
| `S[12]` | `S` | 0 | singlet | singlet | \(Y=0,\ Q=0\) | no | unphysical complex field, no mass declared |

## External Parameters

| Parameter | Value | Appears in / multiplies | Physical meaning |
|---|---:|---|---|
| `vs` | 300 | Singlet field shift \(S=(v_s-s_\theta h+c_\theta h_2+iX)/\sqrt2\); also enters \(\lambda_S\), \(\lambda_{\Phi S}\), and \(\mu_S^2\) | Vacuum expectation value of the complex gauge-singlet scalar |
| `theta` | 0.7854 | Defines \(c_\theta=\cos\theta\), \(s_\theta=\sin\theta\), which enter the scalar-field rotations and the derived quartic couplings | Mixing angle between the neutral doublet scalar excitation and the real singlet scalar excitation |

## Physics Summary

The file encodes a scalar extension of the electroweak Higgs sector by one complex gauge-singlet scalar \(S\), whose real component mixes with the neutral Higgs excitation to form \(h\) and \(h_2\), while its imaginary component is the real scalar \(X\). The soft term \(\mu_S^{\prime 2}(S^2+S^{\dagger2})/4\) gives \(X\) a mass and explicitly breaks the phase symmetry of the complex singlet down to a residual symmetry that keeps \(X\) self-conjugate. The interactions mediate Higgs-portal processes through \((\Phi^\dagger\Phi)(S^\dagger S)\), including scalar mixing, couplings of \(h\) and \(h_2\) to Standard Model electroweak states through the doublet component, and portal production or annihilation involving pairs of \(X\).