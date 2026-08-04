#!/usr/bin/env python3
"""Guards for the Schmidt-correspondence and soft-volume theorem."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent


def involution(size: int, rng: np.random.Generator) -> np.ndarray:
    """A random real orthogonal self-adjoint involution."""
    q, _ = np.linalg.qr(rng.normal(size=(size, size)))
    signs = np.ones(size)
    signs[: size // 2] = -1.0
    rng.shuffle(signs)
    return q @ np.diag(signs) @ q.T


def phi(matrix: np.ndarray, t: float) -> float:
    singular = np.linalg.svd(matrix, compute_uv=False)
    return float(np.log(t + singular * singular).sum())


def main() -> None:
    rng = np.random.default_rng(1240)
    identity_residual = 0.0
    mirsky_slack = float("inf")
    soft_volume_slack = float("inf")
    fixtures = 0

    for _ in range(5000):
        n = int(rng.integers(2, 10))
        ja = involution(n, rng)
        sa = involution(n, rng)
        jb = involution(n, rng)
        sb = involution(n, rng)
        d = rng.normal(size=(n, n))

        # Build positive weights and their sign-reflections directly.  This
        # is the finite matrix form of L(-X)=J L(X) J.
        qa, _ = np.linalg.qr(rng.normal(size=(n, n)))
        la = qa @ np.diag(rng.uniform(0.2, 2.0, size=n)) @ qa.T
        la_minus = ja @ la @ ja
        ca = np.linalg.solve(la_minus, la)

        qb, _ = np.linalg.qr(rng.normal(size=(n, n)))
        lb = qb @ np.diag(rng.uniform(0.2, 2.0, size=n)) @ qb.T
        lb_minus = jb @ lb @ jb
        cb = np.linalg.solve(lb_minus, lb)

        alice_direct = la @ d - ja @ la @ d @ sb.T
        alice_factored = la_minus @ (ca @ d - ja @ d @ sb.T)
        bob_direct = d @ lb.T - sa @ d @ lb.T @ jb.T
        bob_factored = (d @ cb.T - sa @ d @ jb.T) @ lb_minus.T
        identity_residual = max(
            identity_residual,
            float(np.linalg.norm(alice_direct - alice_factored, ord="fro")),
            float(np.linalg.norm(bob_direct - bob_factored, ord="fro")),
        )

        target = ca @ d
        unitary_image = ja @ d @ sb.T
        spectral_distance = float(
            np.linalg.norm(
                np.linalg.svd(target, compute_uv=False)
                - np.linalg.svd(d, compute_uv=False)
            )
        )
        matrix_distance = float(np.linalg.norm(target - unitary_image, ord="fro"))
        mirsky_slack = min(mirsky_slack, matrix_distance - spectral_distance)

        # Independent hostile check of the soft-volume Lipschitz inequality.
        m = rng.normal(size=(n, n))
        perturbation = rng.normal(size=(n, n)) / 10.0
        nn = m + perturbation
        t = float(10.0 ** rng.uniform(-4.0, 2.0))
        lhs = abs(phi(m, t) - phi(nn, t))
        rhs = np.sqrt(n / t) * np.linalg.norm(m - nn, ord="fro")
        soft_volume_slack = min(soft_volume_slack, float(rhs - lhs))
        fixtures += 1

    # Exact nontrivial finite cocycle: reversal transports a diagonal Schmidt
    # operator.  Its multiplier is nonconstant but its total volume is one.
    lam = np.array([1.0, 2.0, 5.0, 11.0])
    reversal = np.fliplr(np.eye(4))
    d_exact = np.diag(lam)
    c_exact = np.diag(lam[::-1] / lam)
    exact_correspondence_residual = float(
        np.linalg.norm(reversal @ d_exact @ reversal.T - c_exact @ d_exact)
    )
    exact_log_volume = float(np.log(np.diag(c_exact)).sum())

    # Equal total Hilbert--Schmidt mass need not mean equal singular spectra.
    scalar_a = np.eye(2)
    scalar_b = np.diag([np.sqrt(1.5), np.sqrt(0.5)])
    scalar_mass_residual = float(
        abs(np.linalg.norm(scalar_a, ord="fro") - np.linalg.norm(scalar_b, ord="fro"))
    )
    singular_separation = float(
        np.linalg.norm(
            np.linalg.svd(scalar_a, compute_uv=False)
            - np.linalg.svd(scalar_b, compute_uv=False)
        )
    )

    # Exact regularized-volume telescope for an open one-step shift.
    shift_lam = np.array([0.91, 0.53, 0.27, 0.08, 0.01])
    shift_d = np.diag(shift_lam)
    shifted = np.diag(np.r_[shift_lam[1:], 0.0])
    telescope_residual = 0.0
    for t in [1e-6, 1e-3, 0.1, 1.0, 7.0]:
        expected = np.log(t) - np.log(t + shift_lam[0] ** 2)
        telescope_residual = max(
            telescope_residual, abs((phi(shifted, t) - phi(shift_d, t)) - expected)
        )
    t_symbol = sp.symbols("t", positive=True)
    l_symbols = sp.symbols("l0:5", positive=True)
    symbolic_telescope = sp.simplify(
        sum(sp.log(t_symbol + l_symbols[i] ** 2) for i in range(1, 5))
        + sp.log(t_symbol)
        - sum(sp.log(t_symbol + l_symbols[i] ** 2) for i in range(5))
        - (sp.log(t_symbol) - sp.log(t_symbol + l_symbols[0] ** 2))
    )

    report = {
        "status": "Schmidt-correspondence and regularized-volume guard",
        "random_fixtures": fixtures,
        "maximum_matrix_factorization_residual": identity_residual,
        "minimum_mirsky_slack": mirsky_slack,
        "minimum_soft_volume_lipschitz_slack": soft_volume_slack,
        "exact_cocycle_fixture": {
            "correspondence_residual": exact_correspondence_residual,
            "log_volume": exact_log_volume,
        },
        "scalar_null": {
            "frobenius_mass_residual": scalar_mass_residual,
            "singular_spectrum_separation": singular_separation,
        },
        "maximum_boundary_telescope_residual": telescope_residual,
        "symbolic_boundary_telescope_residual": str(symbolic_telescope),
        "all_gates_pass": bool(
            fixtures == 5000
            and identity_residual < 1e-10
            and mirsky_slack > -1e-10
            and soft_volume_slack > -1e-10
            and exact_correspondence_residual < 1e-12
            and abs(exact_log_volume) < 1e-12
            and scalar_mass_residual < 1e-12
            and singular_separation > 0.1
            and telescope_residual < 1e-12
            and symbolic_telescope == 0
        ),
        "claim_boundary": (
            "This certifies the matrix ordering, singular-spectrum control, "
            "soft-volume Lipschitz bound on hostile fixtures, and exact open-shift "
            "telescope. It does not prove the Bellman-contact-to-rank boundary law."
        ),
    }
    (HERE / "schmidt-correspondence-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
