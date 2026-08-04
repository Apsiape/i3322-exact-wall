#!/usr/bin/env python3
"""Hostile guards for the regularized Schmidt-flag calculus."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def soft_left(matrix: np.ndarray, t: float) -> np.ndarray:
    m = matrix.shape[0]
    gram = matrix @ matrix.T
    return np.eye(m) - t * np.linalg.inv(t * np.eye(m) + gram)


def soft_right(matrix: np.ndarray, t: float) -> np.ndarray:
    n = matrix.shape[1]
    gram = matrix.T @ matrix
    return np.eye(n) - t * np.linalg.inv(t * np.eye(n) + gram)


def random_projection(size: int, rank: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(size, size)))
    return q[:, :rank] @ q[:, :rank].T


def main() -> None:
    rng = np.random.default_rng(1242)
    intertwining_residual = 0.0
    trace_residual = 0.0
    flag_slack = float("inf")
    resolvent_slack = float("inf")
    fixtures = 0

    for _ in range(10000):
        m = int(rng.integers(2, 9))
        n = int(rng.integers(2, 9))
        d = rng.normal(size=(m, n))
        d /= max(np.linalg.norm(d, ord="fro"), 1e-12)
        t = float(10.0 ** rng.uniform(-4.0, 1.0))
        wa = soft_left(d, t)
        wb = soft_right(d, t)
        intertwining_residual = max(
            intertwining_residual, float(np.linalg.norm(wa @ d - d @ wb, ord="fro"))
        )
        trace_residual = max(trace_residual, abs(float(np.trace(wa) - np.trace(wb))))

        e = random_projection(m, int(rng.integers(0, m + 1)), rng)
        f = random_projection(n, int(rng.integers(0, n + 1)), rng)
        lhs = abs(float(np.trace(e @ wa) - np.trace(f @ wb)))
        mismatch = np.linalg.norm(e @ d - d @ f, ord="fro")
        rank = min(m, n)
        rhs = np.sqrt(rank) * mismatch / (2.0 * np.sqrt(t))
        flag_slack = min(flag_slack, float(rhs - lhs))

        perturbation = rng.normal(size=(m, n)) / 20.0
        nn = d + perturbation
        lhs_resolvent = np.linalg.norm(soft_left(d, t) - soft_left(nn, t), ord="fro")
        rhs_resolvent = (
            (np.linalg.norm(d, ord=2) + np.linalg.norm(nn, ord=2))
            * np.linalg.norm(d - nn, ord="fro")
            / t
        )
        resolvent_slack = min(resolvent_slack, float(rhs_resolvent - lhs_resolvent))
        fixtures += 1

    # The marginal-volume doppelganger is separated by its ordered flags.
    lam = np.array([1.0, 2.0, 5.0, 11.0])
    d0 = np.diag(lam)
    p = np.fliplr(np.eye(4))
    q = np.array(
        [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]]
    )
    ordered_flag_separation = 0.0
    for k in range(1, 4):
        flag = np.diag([1.0] * k + [0.0] * (4 - k))
        ordered_flag_separation += float(
            np.linalg.norm(p @ flag @ p.T - q @ flag @ q.T, ord="fro") ** 2
        )

    # Exact contact fixture E D = D F has identical soft-flag mass.
    contact_d = np.diag([0.7, 0.4, 0.1, 0.0])
    contact_e = np.diag([1.0, 1.0, 0.0, 0.0])
    contact_f = contact_e.copy()
    contact_intertwiner_residual = float(
        np.linalg.norm(contact_e @ contact_d - contact_d @ contact_f, ord="fro")
    )
    contact_mass_residual = abs(
        float(
            np.trace(contact_e @ soft_left(contact_d, 0.03))
            - np.trace(contact_f @ soft_right(contact_d, 0.03))
        )
    )

    report = {
        "status": "regularized Schmidt-flag guard",
        "random_fixtures": fixtures,
        "maximum_soft_support_intertwining_residual": intertwining_residual,
        "maximum_left_right_trace_residual": trace_residual,
        "minimum_contact_flag_bound_slack": flag_slack,
        "minimum_resolvent_stability_slack": resolvent_slack,
        "ordered_flag_doppelganger_separation": ordered_flag_separation,
        "exact_contact_fixture": {
            "intertwiner_residual": contact_intertwiner_residual,
            "soft_flag_mass_residual": contact_mass_residual,
        },
        "all_gates_pass": bool(
            fixtures == 10000
            and intertwining_residual < 1e-10
            and trace_residual < 1e-10
            and flag_slack > -1e-10
            and resolvent_slack > -1e-10
            and ordered_flag_separation > 1.0
            and contact_intertwiner_residual < 1e-12
            and contact_mass_residual < 1e-12
        ),
        "claim_boundary": (
            "This verifies the soft-support identities and hostile inequalities. "
            "It does not prove uniform I3322 flag transport or finite-rank closure."
        ),
    }
    (HERE / "regularized-schmidt-flag-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
