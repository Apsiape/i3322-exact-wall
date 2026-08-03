"""Independent symbolic reconstruction of the finite-closure contradiction."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    bx, bu, rho = sp.symbols("b_x b_u rho", positive=True)
    fx = sp.symbols("f_x", positive=True)
    total = bx + bu

    # Start from the common norm ratio and Cauchy equality. This independently
    # eliminates f(-u), then factors equality of the two Bellman sums.
    fmx = rho**2 * fx
    fmu = bx * bu / (rho**2 * fx)
    fu = rho**2 * fmu
    px = bx**2 / fx
    pmu = bu**2 / fmu
    forward = sp.factor(px + fu)
    reflected = sp.factor(fmx + pmu)
    bellman_gap = sp.factor(forward - reflected)
    expected_gap = sp.factor(total * (bx**2 - rho**2 * fx**2) / (bx * fx))
    gap_residual = sp.factor(bellman_gap - expected_gap)

    # Positivity selects rho*f_x=b_x from the factored square relation.
    substitution = {fx: bx / rho}
    plus_value = sp.factor(forward.subs(substitution))
    minus_value = sp.factor(
        (bx**2 / fmx + fmu).subs(substitution)
    )

    delta = sp.factor(minus_value - plus_value)
    radical_identity = sp.factor(
        (delta / 2 + plus_value) ** 2
        - (total**2 + delta**2 / 4)
    )

    x, u, sx, su = sp.symbols("x u s_x s_u", real=True)
    circle_ideal = sp.groebner(
        [sx**2 + x**2 - 1, su**2 + u**2 - 1],
        sx, su, x, u, domain=sp.QQ,
    )
    geometric_identity = sp.expand(
        ((sx + su) / 2) ** 2 + ((x - u) / 2) ** 2
        - (1 - x * u + sx * su) / 2
    )
    geometric_residual = sp.factor(circle_ideal.reduce(geometric_identity)[1])
    order_identity = sp.expand(
        (1 - x * u) ** 2 - sx**2 * su**2 - (x - u) ** 2
    )
    order_residual = sp.factor(circle_ideal.reduce(order_identity)[1])

    w = sp.symbols("w", nonnegative=True)
    quarter_residual = sp.factor(
        sp.Rational(1, 4) - (w - w**2) - (w - sp.Rational(1, 2)) ** 2
    )

    # Direct proof of the finite-order lemma: a decreasing bijection sends
    # rank k to rank n-1-k. This table audits the formula without permutation
    # enumeration and is implementation-independent of Sprint 1198.
    order_tables = {
        str(n): [n - 1 - k for k in range(n)] for n in range(1, 33)
    }
    order_involutions = all(
        all(row[row[k]] == k for k in range(len(row)))
        for row in order_tables.values()
    )

    exact = {
        "bellman_gap_factorization": str(gap_residual),
        "plus_value_minus_rho_total": str(sp.factor(plus_value - rho * total)),
        "minus_value_minus_total_over_rho": str(sp.factor(minus_value - total / rho)),
        "ratio_to_radical_identity": str(radical_identity),
        "geometric_radicand_identity": str(geometric_residual),
        "one_minus_xu_order_identity": str(order_residual),
        "quarter_square_identity": str(quarter_residual),
    }
    report = {
        "status": "independent symbolic nonattainment reconstruction",
        "exact_residuals": exact,
        "finite_order_tables": order_tables,
        "all_order_tables_involutive": order_involutions,
        "all_gates_pass": all(value == "0" for value in exact.values()) and order_involutions,
        "claim_boundary": (
            "This engine independently reconstructs the scalar elimination and "
            "finite-order lemma; strict contact uniqueness is owned by the Arb audit."
        ),
    }
    output = HERE / "independent-nonattainment.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "finite_order_tables"}, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
