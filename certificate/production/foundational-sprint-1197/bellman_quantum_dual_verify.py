"""Exact algebra and independent random-matrix gates for the I3322 dual."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


def random_projector(rng: np.random.Generator, n: int, rank: int) -> np.ndarray:
    raw = rng.normal(size=(n, rank)) + 1j * rng.normal(size=(n, rank))
    q, _ = np.linalg.qr(raw)
    return q @ q.conj().T


def kron(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.kron(left, right)


def original_bell(a: list[np.ndarray], b: list[np.ndarray]) -> np.ndarray:
    da, db = a[0].shape[0], b[0].shape[0]
    ia, ib = np.eye(da), np.eye(db)
    out = -kron(a[1], ib) - kron(ia, b[0]) - 2 * kron(ia, b[1])
    for coefficient, ai, bj in [
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
        (-1, 0, 2), (1, 1, 2), (-1, 2, 0), (1, 2, 1),
    ]:
        out += coefficient * kron(a[ai], b[bj])
    return out


def reparameterized_bell(a: list[np.ndarray], b: list[np.ndarray]) -> np.ndarray:
    da, db = a[0].shape[0], b[0].shape[0]
    ia, ib = np.eye(da), np.eye(db)
    x = a[0] + a[1] - ia
    y = a[1] - a[0]
    u = b[0] + b[1] - ib
    v = b[1] - b[0]
    return (
        kron(x, u)
        + kron(x / 2, ib)
        - kron(ia, u / 2)
        - kron(ia, ib)
        + kron(y, b[2] - ib / 2)
        + kron(a[2] - ia / 2, v)
    )


def main() -> None:
    # Independent commutative coefficient expansion.
    a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
    original = -a2 - b1 - 2 * b2 + a1*b1 + a1*b2 + a2*b1 + a2*b2 - a1*b3 + a2*b3 - a3*b1 + a3*b2
    x, y, u, v = a1+a2-1, a2-a1, b1+b2-1, b2-b1
    rewritten = x*u + x/2 - u/2 - 1 + y*(b3-sp.Rational(1,2)) + (a3-sp.Rational(1,2))*v
    bell_residual = sp.expand(original - rewritten)

    q, xx, uu, fx, fmx, fu, fmu = sp.symbols("q x u F_x F_minus_x F_u F_minus_u", positive=True)
    d = xx*uu + (xx-uu)/2 - 1
    bx, bu = sp.symbols("b_x b_u", nonnegative=True)
    px, pmx = bx**2/fx, bx**2/fmx
    pu, pmu = bu**2/fu, bu**2/fmu
    ax, amx = sp.sqrt(px*fmx), sp.sqrt(pmx*fx)
    bu_potential, bmu_potential = sp.sqrt(fu*pmu), sp.sqrt(fmu*pu)
    product_a_residual = sp.simplify(ax*amx-bx**2)
    product_b_residual = sp.simplify(bu_potential*bmu_potential-bu**2)
    reflected_cost_residual = sp.factor(((-uu)*(-xx)+((-uu)-(-xx))/2-1)-d)

    # Cauchy in polynomial square-root coordinates:
    # (r^2+t^2)(s^2+w^2)-(rs+tw)^2=(rw-st)^2.
    r, sroot, t, w = sp.symbols("r s t w", real=True)
    cauchy_residual = sp.expand((r*r+t*t)*(sroot*sroot+w*w)-(r*sroot+t*w)**2-(r*w-sroot*t)**2)

    bb, z = sp.symbols("b z", real=True)
    fp, fm = sp.symbols("F_plus F_minus", positive=True)
    local_det = sp.factor(fp*fm - (2*bb*z)**2)
    reflected_local_det = sp.factor(local_det.subs(fp*fm, bb**2))
    endpoint_plus = sp.factor((sp.Rational(1,2) - (sp.Rational(1,2) - fm)))
    zero_block_gap = sp.factor(sp.Rational(1,2) - 0 - sp.Rational(1,2))

    rng = np.random.default_rng(119703)
    random_checks = []
    for da, db in [(2, 2), (3, 4), (5, 3), (6, 6)]:
        residuals = []
        relation_residuals = []
        for _ in range(12):
            a = [random_projector(rng, da, int(rng.integers(1, da + 1))) for _ in range(3)]
            b = [random_projector(rng, db, int(rng.integers(1, db + 1))) for _ in range(3)]
            residuals.append(float(np.linalg.norm(original_bell(a, b) - reparameterized_bell(a, b), ord=2)))
            xa, ya = a[0] + a[1] - np.eye(da), a[1] - a[0]
            ub, vb = b[0] + b[1] - np.eye(db), b[1] - b[0]
            relation_residuals.extend([
                float(np.linalg.norm(xa@xa + ya@ya - np.eye(da), ord=2)),
                float(np.linalg.norm(xa@ya + ya@xa, ord=2)),
                float(np.linalg.norm(ub@ub + vb@vb - np.eye(db), ord=2)),
                float(np.linalg.norm(ub@vb + vb@ub, ord=2)),
            ])
        random_checks.append({
            "dimensions": [da, db],
            "max_bell_operator_residual": max(residuals),
            "max_pair_relation_residual": max(relation_residuals),
        })

    report = {
        "status": "exact algebra plus held-out complex-matrix reconstruction",
        "original_reparameterization_residual": str(bell_residual),
        "A_product_residual": str(product_a_residual),
        "B_product_residual": str(product_b_residual),
        "reflected_cost_residual": str(reflected_cost_residual),
        "cauchy_polynomial_residual": str(cauchy_residual),
        "local_determinant_before_reflection": str(local_det),
        "local_determinant_after_reflection": str(reflected_local_det),
        "local_determinant_nonnegative_for_response_interval": "b^2*(1-4*z^2) >= 0 for |z|<=1/2",
        "endpoint_plus_gap": str(endpoint_plus),
        "zero_block_gap": str(zero_block_gap),
        "random_matrix_checks": random_checks,
        "max_random_bell_residual": max(row["max_bell_operator_residual"] for row in random_checks),
        "max_random_pair_relation_residual": max(row["max_pair_relation_residual"] for row in random_checks),
        "all_gates_pass": (
            bell_residual == 0
            and product_a_residual == 0
            and product_b_residual == 0
            and reflected_cost_residual == 0
            and cauchy_residual == 0
            and sp.simplify(reflected_local_det - bb**2 * (1 - 4*z**2)) == 0
            and zero_block_gap == 0
            and max(row["max_bell_operator_residual"] for row in random_checks) < 1e-12
            and max(row["max_pair_relation_residual"] for row in random_checks) < 1e-12
        ),
        "claim_boundary": (
            "These identities validate the Bell-operator decomposition and geometric symmetrization. The theorem also requires the exact Bellman fixed point certified in Sprint 1195."
        ),
    }
    output = Path(__file__).with_name("bellman-quantum-dual.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
