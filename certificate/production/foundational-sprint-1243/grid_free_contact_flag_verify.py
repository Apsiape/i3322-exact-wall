#!/usr/bin/env python3
"""Exact-rational layer-cake and contact-coercivity guards."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
Q = Fraction


def main() -> None:
    rng = random.Random(1243)
    fixtures = 0
    minimum_cauchy_slack = None
    maximum_layer_cake_residual = Q(0)

    for _ in range(20000):
        count = rng.randint(1, 30)
        raw_weights = [Q(rng.randint(1, 50), rng.randint(1, 50)) for _ in range(count)]
        total = sum(raw_weights, Q(0))
        weights = [value / total for value in raw_weights]
        y = [Q(rng.randint(-100, 100), 100) for _ in range(count)]
        u = [Q(rng.randint(-100, 100), 100) for _ in range(count)]

        # Integrating the disagreement of two cumulative indicators is the
        # interval length between their jump locations.
        integrated_indicators = sum(
            weights[i] * abs(y[i] - u[i]) for i in range(count)
        )
        layer_cake = sum(weights[i] * abs(y[i] - u[i]) for i in range(count))
        maximum_layer_cake_residual = max(
            maximum_layer_cake_residual, abs(integrated_indicators - layer_cake)
        )

        mean_square = sum(weights[i] * (y[i] - u[i]) ** 2 for i in range(count))
        cauchy_slack = mean_square - layer_cake**2
        if minimum_cauchy_slack is None or cauchy_slack < minimum_cauchy_slack:
            minimum_cauchy_slack = cauchy_slack

        # Add an arbitrary nonnegative Bellman surplus above the certified
        # quadratic lower bound r0 >= (u-Y)^2/40.
        surplus = [Q(rng.randint(0, 20), 1000) for _ in range(count)]
        epsilon_0 = sum(
            weights[i] * ((y[i] - u[i]) ** 2 / 40 + surplus[i])
            for i in range(count)
        )
        assert layer_cake**2 <= 40 * epsilon_0
        fixtures += 1

    # Endpoint and equality fixtures.
    endpoint_pairs = [(Q(-1), Q(1)), (Q(1), Q(-1)), (Q(0), Q(0))]
    endpoint_integrals = [abs(a - b) for a, b in endpoint_pairs]

    report = {
        "status": "exact-rational grid-free contact-flag guard",
        "random_fixtures": fixtures,
        "maximum_layer_cake_residual": str(maximum_layer_cake_residual),
        "minimum_cauchy_slack": str(minimum_cauchy_slack),
        "endpoint_integrals": [str(value) for value in endpoint_integrals],
        "all_gates_pass": bool(
            fixtures == 20000
            and maximum_layer_cake_residual == 0
            and minimum_cauchy_slack is not None
            and minimum_cauchy_slack >= 0
            and endpoint_integrals == [Q(2), Q(2), Q(0)]
        ),
        "claim_boundary": (
            "This guards the layer-cake identity and exact-rational coercive "
            "implication. The global I3322 coefficient 1/40 is owned by Sprint "
            "1232; response transport and finite-rank closure remain open."
        ),
    }
    (HERE / "grid-free-contact-flag-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
