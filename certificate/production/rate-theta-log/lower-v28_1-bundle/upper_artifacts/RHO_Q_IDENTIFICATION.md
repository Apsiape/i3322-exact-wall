# Endpoint Multiplier and Return-Distortion Identification — v28

To avoid collision with the normalized response gain \(\alpha\) in the live lower proof, denote the forward endpoint scalar label by
\[
\alpha_{\rm end}
\]
and retain \(x_{+,\rm end}\) for the reflected source endpoint. Put
\[
a_{+,\rm end}=r_{B,{\rm mult}}(\alpha_{\rm end}),
\qquad
b_{+,\rm end}=r_{A,{\rm mult}}(x_{+,\rm end}),
\]
\[
\rho_+=\frac{a_{+,\rm end}}{b_{+,\rm end}}.
\]
The tail theorem gives \(\lambda_j\to0\), hence \(0<\rho_+\le1\).

The distorted-return theorem orients its **normalized gain** ratio into \((0,1]\):
\[
q_{\rm ret,+}:=\min\left\{\frac{a_{+,\rm end}}{b_{+,\rm end}},\frac{b_{+,\rm end}}{a_{+,\rm end}}\right\}.
\]
Because \(\rho_+\le1\),
\[
\boxed{q_{\rm ret,+}=\rho_+.}
\]
Therefore
\[
\boxed{\rho_+=1\iff q_{\rm ret,+}=1.}
\]
The negative endpoint uses distinct endpoint-label symbols and the reversed outward orientation.

This file is upper-only. It does not supply the lower-route quarter ceiling and cannot promote `D_upper` or `Theta(log)`.
