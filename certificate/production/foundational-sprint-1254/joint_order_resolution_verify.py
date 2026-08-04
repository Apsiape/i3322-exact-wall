#!/usr/bin/env python3
"""Hostile matrix guard for the joint order-resolution coupling."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def hermitian_function(matrix: np.ndarray, fn) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * fn(values)) @ vectors.conj().T


def random_hermitian(rng: np.random.Generator, n: int) -> np.ndarray:
    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (raw + raw.conj().T) / 2


def main() -> None:
    rng = np.random.default_rng(1254)
    maximum_left_residual = 0.0
    maximum_right_residual = 0.0
    maximum_cost_identity_residual = 0.0
    maximum_bound_ratio = 0.0
    fixtures = 0

    for m, n in [(2, 3), (3, 2), (4, 4), (5, 3)]:
        for _ in range(600):
            d = rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))
            d /= max(np.linalg.norm(d, ord="fro"), 1.0)
            rho_a = d @ d.conj().T
            rho_b = d.conj().T @ d
            y = random_hermitian(rng, m)
            u = random_hermitian(rng, n)
            # Scale the order observables into [-1,1].
            y /= max(np.linalg.norm(y, ord=2), 1.0)
            u /= max(np.linalg.norm(u, ord=2), 1.0)
            t = float(10 ** rng.uniform(-5, 0))
            rb = np.linalg.inv(t * np.eye(n) + rho_b)
            z = np.sqrt(t) * d @ rb
            ka = hermitian_function(rho_a, lambda x: t * x / (t + x) ** 2)
            kb = hermitian_function(rho_b, lambda x: t * x / (t + x) ** 2)

            maximum_left_residual = max(
                maximum_left_residual,
                float(np.linalg.norm(z @ z.conj().T - ka, ord="fro")),
            )
            maximum_right_residual = max(
                maximum_right_residual,
                float(np.linalg.norm(z.conj().T @ z - kb, ord="fro")),
            )

            c = y @ d - d @ u
            commutator = rho_b @ u - u @ rho_b
            commutator_identity = c.conj().T @ d - d.conj().T @ c
            assert np.linalg.norm(commutator - commutator_identity, ord="fro") < 2e-11
            lhs = y @ z - z @ u
            expanded = np.sqrt(t) * (
                c @ rb + d @ (rb @ commutator @ rb)
            )
            maximum_cost_identity_residual = max(
                maximum_cost_identity_residual,
                float(np.linalg.norm(lhs - expanded, ord="fro")),
            )
            rhs = 3 * np.linalg.norm(c, ord="fro") * t ** (-1.5)
            if rhs > 1e-14:
                maximum_bound_ratio = max(
                    maximum_bound_ratio,
                    float(np.linalg.norm(lhs, ord="fro") / rhs),
                )
            fixtures += 1

    report = {
        "status": "hostile rectangular-matrix joint-coupling guard",
        "fixtures": fixtures,
        "maximum_left_marginal_residual": maximum_left_residual,
        "maximum_right_marginal_residual": maximum_right_residual,
        "maximum_contact_identity_residual": maximum_cost_identity_residual,
        "maximum_norm_bound_ratio": maximum_bound_ratio,
        "gates": {
            # The smallest sampled t is 1e-5, so the direct inverses carry a
            # visible binary64 condition tax.  The 1e-8 gate remains over an
            # order of magnitude above the worst residual and far below the
            # guarded inequality scale.
            "left_marginal": maximum_left_residual < 1e-8,
            "right_marginal": maximum_right_residual < 1e-8,
            "contact_commutator_identity": maximum_cost_identity_residual < 1e-8,
            "registered_norm_bound": maximum_bound_ratio <= 1.0 + 2e-11,
        },
        "all_gates_pass": (
            maximum_left_residual < 1e-8
            and maximum_right_residual < 1e-8
            and maximum_cost_identity_residual < 1e-8
            and maximum_bound_ratio <= 1.0 + 2e-11
        ),
        "claim_boundary": (
            "The matrix identities and conservative near-contact bound are "
            "guarded. The I3322 continuous-to-coarse descent is not proved."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "joint-order-resolution-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
