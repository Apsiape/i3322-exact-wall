"""Exact symbolic matrix audit for the cyclic Bellman sum of squares."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def verify_size(n: int) -> dict:
    f = sp.symbols(f"f0:{n}", positive=True)
    b = sp.symbols(f"b0:{n}", nonnegative=True)
    slack = sp.symbols(f"r0:{n}", nonnegative=True)

    # q-d_i = F_(i+1) + b_i^2/F_i + r_i.
    carrier = sp.zeros(n)
    for i in range(n):
        carrier[i, i] = f[(i + 1) % n] + b[i] ** 2 / f[i] + slack[i]
        carrier[(i - 1) % n, i] -= b[i]
        carrier[i, (i - 1) % n] -= b[i]

    # Row i is sqrt(F_i)e_(i-1) - b_i/sqrt(F_i)e_i.
    gram = sp.zeros(n)
    for i in range(n):
        gram[(i - 1) % n, (i - 1) % n] += f[i]
        gram[i, i] += b[i] ** 2 / f[i]
        gram[(i - 1) % n, i] -= b[i]
        gram[i, (i - 1) % n] -= b[i]
    gram += sp.diag(*slack)

    residual = carrier - gram
    nonzero = [(i, j, sp.factor(residual[i, j])) for i in range(n) for j in range(n) if residual[i, j] != 0]
    return {"n": n, "nonzero_residuals": [(i, j, str(value)) for i, j, value in nonzero], "passed": not nonzero}


def main() -> None:
    checks = [verify_size(n) for n in range(3, 10)]
    s = sp.symbols("s", real=True)
    q_selfloop = sp.factor(s * (1 - s))
    quarter_gap = sp.factor(sp.Rational(1, 4) - q_selfloop)
    report = {
        "status": "exact cyclic Bellman SOS matrix identity",
        "size_checks": checks,
        "all_matrix_residuals_zero": all(row["passed"] for row in checks),
        "equality_selfloop_q": str(q_selfloop),
        "quarter_minus_selfloop_q": str(quarter_gap),
        "quarter_gap_is_square": quarter_gap == (2 * s - 1) ** 2 / 4,
        "zero_couplings_allowed": True,
        "claim_boundary": (
            "Conditional only on the positive Bellman fixed point from Sprint 1195, every finite aligned periodic carrier is strictly below q_*. "
            "This does not align arbitrary I3322 strategies."
        ),
    }
    output = Path(__file__).with_name("cyclic-sos.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_matrix_residuals_zero"] or not report["quarter_gap_is_square"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
