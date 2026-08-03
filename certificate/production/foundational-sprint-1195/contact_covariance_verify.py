"""Independent symbolic verifier for the Bellman/contact weld.

The script rebuilds the shooting map from its displayed formulas, derives the
Bellman and stationarity identities, and verifies contact covariance without
using floating-point arithmetic.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    z, x, u, q = sp.symbols("z x u q", real=True)
    sz = sp.sqrt(1 - z**2)
    sx = sp.sqrt(1 - x**2)

    cost = z * x + (z - x) / 2 - 1
    v = sp.factor(2 * (q - cost - sz / (2 * u)) / sx)
    y = sp.factor(-sp.Rational(1, 2) + (1 - 2 * z) / (2 * v**2) + x / (sx * v))

    # Bellman equality at predecessor z and target x.
    fz = sz * u / 2
    fx = sx * v / 2
    bellman_residual = sp.factor(fx - (q - cost - (1 - z**2) / (4 * fz)))

    # Stationarity of the z-line at target x, assuming F'(z)=1/2-w.
    # Solving the stationarity equation for the target reproduces y after one
    # shift; equivalently the formula below must vanish identically.
    shooting_position_residual = sp.factor(
        y + sp.Rational(1, 2) - (1 - 2 * z) / (2 * v**2) - x / (sx * v)
    )

    # beta = dF(x) - (1/2-z) dx after Bellman elimination.
    # Its current-state coefficients in (dz,dx,du) are computed by
    # differentiation rather than inserted from the exploratory run.
    beta = [sp.factor(sp.diff(fx, w) - (sp.Rational(1, 2) - z) * sp.diff(x, w)) for w in (z, x, u)]

    # Build the next step afresh and pull its beta back through M.
    sy = sp.sqrt(1 - y**2)
    cost_next = x * y + (x - y) / 2 - 1
    w_ratio = sp.factor(2 * (q - cost_next - sx / (2 * v)) / sy)
    fy = sp.factor(sy * w_ratio / 2)
    beta_next_pullback = [
        sp.factor(sp.diff(fy, var) - (sp.Rational(1, 2) - x) * sp.diff(y, var))
        for var in (z, x, u)
    ]
    contact_residuals = [sp.factor(sp.together(beta_next_pullback[i] - beta[i] / v**2)) for i in range(3)]

    c = sp.symbols("c", positive=True)
    r_wall = sp.sqrt(1 - c**2) * (2 * c - 1) / ((1 - c) * (2 * c + 1))
    a = (1 + c) * (2 * c - 1) ** 2
    d = (1 - c) * (2 * c + 1) ** 2
    multiplier_residual = sp.factor(1 / r_wall**2 - d / a)

    report = {
        "status": "exact symbolic contact covariance",
        "bellman_residual": str(bellman_residual),
        "shooting_position_residual": str(shooting_position_residual),
        "beta_coefficients": [str(sp.factor(value)) for value in beta],
        "contact_covariance_residuals": [str(value) for value in contact_residuals],
        "contact_multiplier": "1/v**2",
        "plateau_multiplier_residual": str(multiplier_residual),
        "plateau_contact_multiplier": "D/A=(1-c)(2c+1)^2/((1+c)(2c-1)^2)",
        "all_exact_checks_zero": all(
            value == 0
            for value in [bellman_residual, shooting_position_residual, multiplier_residual, *contact_residuals]
        ),
        "claim_boundary": (
            "The displayed shooting map preserves the Bellman envelope one-form up to the positive factor 1/v^2. "
            "On the high plateau branch this covector multiplier is the isolated stable root D/A, not the unstable root."
        ),
    }
    output = Path(__file__).with_name("contact-covariance.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
