#!/usr/bin/env python3
"""Exact-rational adversary for the finite monotone skew-flow theorem."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def tail(mass: Q, center: Q, cut: Q) -> Q:
    return mass if center >= -cut else Q(0)


def tv_at_cut(A, Bvals, p, q, masses, centers, cut: Q) -> Q:
    coefficients: dict[int, Q] = {}
    for i in range(len(A)):
        coefficients[A[i]] = coefficients.get(A[i], Q(0)) + tail(
            masses[i], centers[i], cut + p[i]
        )
        coefficients[Bvals[i]] = coefficients.get(Bvals[i], Q(0)) - tail(
            masses[i], centers[i], cut + q[i]
        )
    return sum(abs(value) for value in coefficients.values())


def main() -> None:
    rng = random.Random(1255)
    fixtures = 0
    minimum_slack = None
    nontrivial_cycle_detections = 0

    for _ in range(25000):
        n = rng.randint(1, 8)
        d = n
        universe = list(range(-20, 21))
        A = sorted(rng.sample(universe, n), reverse=True)
        Bvals = sorted(rng.sample(universe, n), reverse=True)
        p = [Q(rng.randint(-4, 4), 2) for _ in range(n)]
        q = [Q(rng.randint(-4, 4), 2) for _ in range(n)]
        fixed = [i for i in range(n) if A[i] == Bvals[i]]
        # Enforce the registered fixed gap g=1/2.
        for i in fixed:
            if abs(p[i] - q[i]) < Q(1, 2):
                q[i] = p[i] + Q(1, 2)
        Bbound = max([abs(x) for x in p + q] + [Q(1, 2)])
        g = Q(1, 2)
        H = Q(6)
        masses = [Q(rng.randint(1, 7), 7) for _ in range(n)]
        centers = [Q(rng.randint(-12, 4), 2) for _ in range(n)]

        edges = {}
        for i, value in enumerate(A):
            if value in Bvals:
                edges[i] = Bvals.index(value)
        # Any detected cycle in the partial increasing map must be fixed.
        for start in range(n):
            seen = []
            node = start
            while node in edges and node not in seen:
                seen.append(node)
                node = edges[node]
            if node in seen and len(seen[seen.index(node):]) > 1:
                nontrivial_cycle_detections += 1

        core = sum(
            mass for mass, center in zip(masses, centers) if -H <= center <= 0
        )
        R = 2 * Bbound * d + Bbound
        # Step tails change only at these exact rational breakpoints.
        cuts = {-R, H + R}
        for i in range(n):
            cuts.add(-centers[i] - p[i])
            cuts.add(-centers[i] - q[i])
        ordered = sorted(x for x in cuts if -R <= x <= H + R)
        probes = set(ordered)
        for left, right in zip(ordered, ordered[1:]):
            probes.add((left + right) / 2)
        V = max(
            tv_at_cut(A, Bvals, p, q, masses, centers, cut)
            for cut in probes
        )
        rhs = (3 * d**3 + (H + 2 * Bbound) / g) * V
        slack = rhs - core
        assert slack >= 0
        if minimum_slack is None or slack < minimum_slack:
            minimum_slack = slack
        fixtures += 1

    report = {
        "status": "exact-rational finite skew-flow adversary",
        "fixtures": fixtures,
        "minimum_theorem_slack": str(minimum_slack),
        "nontrivial_cycle_detections": nontrivial_cycle_detections,
        "gates": {
            "all_random_fixtures": minimum_slack is not None and minimum_slack >= 0,
            "increasing_graph_has_only_fixed_cycles": nontrivial_cycle_detections == 0,
        },
        "all_gates_pass": (
            minimum_slack is not None
            and minimum_slack >= 0
            and nontrivial_cycle_detections == 0
        ),
        "claim_boundary": (
            "The abstract finite-flow inequality is guarded on exact-rational "
            "step-tail adversaries. I3322 coarse descent is not asserted."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "finite-monotone-skew-flow-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
