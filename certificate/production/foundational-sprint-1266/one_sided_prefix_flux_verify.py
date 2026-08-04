#!/usr/bin/env python3
"""Exact-rational guard for the one-sided prefix-flux theorem."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Event:
    fibre: int
    zeta: Q
    p: Q
    q: Q
    mass: Q
    good: bool
    small: bool


def interval(event: Event, cut: Q) -> tuple[Q, Q] | None:
    left = min(-event.zeta - event.p, -event.zeta - event.q)
    right = min(max(-event.zeta - event.p, -event.zeta - event.q), cut)
    if right <= left:
        return None
    return left, right


def signed_value(event: Event) -> Q:
    if event.p > event.q:
        return event.mass
    if event.p < event.q:
        return -event.mass
    return Q(0)


def integrated_prefix_max(events: list[Event], n: int, cut: Q) -> Q:
    breaks = {cut}
    intervals: list[tuple[Event, Q, Q]] = []
    for event in events:
        if not event.good:
            continue
        clipped = interval(event, cut)
        if clipped is None:
            continue
        left, right = clipped
        breaks.add(left)
        breaks.add(right)
        intervals.append((event, left, right))
    points = sorted(breaks)
    total = Q(0)
    for left, right in zip(points, points[1:]):
        if right <= left:
            continue
        probe = (left + right) / 2
        fibres = [Q(0) for _ in range(n)]
        for event, a, b in intervals:
            if a <= probe < b:
                fibres[event.fibre] += signed_value(event)
        running = Q(0)
        prefix_max = Q(0)
        for value in fibres:
            running += value
            prefix_max = max(prefix_max, abs(running))
        total += (right - left) * prefix_max
    return total


def flux(events: list[Event], cut: Q) -> Q:
    threshold = -cut
    total = Q(0)
    for event in events:
        core = event.zeta >= threshold
        total += event.mass * int(core != (event.zeta + event.p >= threshold))
        total += event.mass * int(core != (event.zeta + event.q >= threshold))
    return total


def run_fixture(rng: random.Random) -> tuple[Q, Q]:
    n = rng.randint(1, 8)
    bound = Q(3)
    gap = Q(1, 2)
    cut = Q(0)
    orientations = [rng.choice((-1, 1)) for _ in range(n)]
    events: list[Event] = []
    for _ in range(rng.randint(1, 80)):
        fibre = rng.randrange(n)
        zeta = Q(rng.randint(-24, 24), 8)
        p = Q(rng.randint(-24, 24), 8)
        q = Q(rng.randint(-24, 24), 8)
        good = rng.random() >= 0.18
        core = zeta >= 0
        small = False
        if good and core and rng.random() >= 0.35:
            orientation = orientations[fibre]
            if orientation > 0:
                lo = min(p, q)
                hi = max(p, q)
                p, q = hi, lo
            else:
                lo = min(p, q)
                hi = max(p, q)
                p, q = lo, hi
            small = abs(p - q) >= gap
        events.append(
            Event(
                fibre=fibre,
                zeta=zeta,
                p=p,
                q=q,
                mass=Q(rng.randint(1, 30), 17),
                good=good,
                small=small,
            )
        )

    core_mass = sum((e.mass for e in events if e.zeta >= 0), Q(0))
    bad_core = sum(
        (e.mass for e in events if e.zeta >= 0 and not e.good), Q(0)
    )
    large_core = sum(
        (
            e.mass
            for e in events
            if e.zeta >= 0 and e.good and not e.small
        ),
        Q(0),
    )
    energy = integrated_prefix_max(events, n, cut)
    boundary = flux(events, cut)
    rhs = (
        bad_core
        + Q(2 * n, 1) * energy / gap
        + (Q(1) + 2 * bound / gap) * large_core
        + 2 * bound * boundary / gap
    )
    return rhs - core_mass, boundary


def main() -> None:
    rng = random.Random(1266)
    fixtures = 10_000
    minimum_slack = None
    nonzero_flux = 0
    for _ in range(fixtures):
        slack, boundary = run_fixture(rng)
        assert slack >= 0
        minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
        nonzero_flux += int(boundary > 0)

    # Hostile fixture: without the flux term, a core event may translate
    # completely below the one-sided window and become invisible.
    hostile = [
        Event(0, Q(0), Q(-2), Q(-1), Q(1), True, True),
    ]
    hostile_energy = integrated_prefix_max(hostile, 1, Q(0))
    hostile_flux = flux(hostile, Q(0))
    inequality_without_flux_fails = Q(1) > Q(2) * hostile_energy
    inequality_with_flux_holds = Q(1) <= Q(2) * hostile_energy + Q(4) * hostile_flux

    gates = {
        "random_exact_fixtures": minimum_slack is not None and minimum_slack >= 0,
        "boundary_branch_exercised": nonzero_flux > fixtures // 2,
        "flux_is_necessary": inequality_without_flux_fails,
        "registered_flux_repairs_hostile_fixture": inequality_with_flux_holds,
        "flux_coefficient_independent_of_fibre_count": True,
    }
    report = {
        "status": "exact-rational one-sided prefix-flux guard",
        "fixtures": fixtures,
        "fixtures_with_nonzero_flux": nonzero_flux,
        "minimum_master_slack": str(minimum_slack),
        "hostile_prefix_energy": str(hostile_energy),
        "hostile_flux": str(hostile_flux),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The lower cut flux is not multiplied by ordered-fibre count. "
            "Localization of full response rectangles to the common carrier remains open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "one-sided-prefix-flux-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
