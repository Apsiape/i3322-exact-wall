"""Exact algebra and finite-order audit for I3322 nonattainment."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent


def decreasing_bijection_count(n: int) -> int:
    """Count strictly decreasing permutations of an n-point ordered set."""
    count = 0
    for perm in itertools.permutations(range(n)):
        if all(perm[i] > perm[i + 1] for i in range(n - 1)):
            count += 1
    return count


def main() -> None:
    bx, bu, r = sp.symbols("b_x b_u rho", positive=True)
    x, u = sp.symbols("x u", real=True)
    s = bx + bu

    # The common-kernel norm ratio is rho.  Equality in the forward and
    # reflected Bellman/Cauchy steps then fixes all four F-values.
    fx = bx / r
    fmx = bx * r
    fu = bu * r
    fmu = bu / r
    px = bx**2 / fx
    pmx = bx**2 / fmx
    pu = bu**2 / fu
    pmu = bu**2 / fmu

    bellman_sums = {
        "plus_forward": sp.factor(px + fu - r * s),
        "plus_reflected": sp.factor(fmx + pmu - r * s),
        "minus_forward": sp.factor(pmx + fmu - s / r),
        "minus_reflected": sp.factor(fx + pu - s / r),
    }
    amplitude_ratios = {
        "alice_ratio_squared": sp.factor(fmx / fx - r**2),
        "bob_ratio_squared": sp.factor(fu / fmu - r**2),
        "cauchy_equality": sp.factor(px * pmu - fu * fmx),
    }

    # Audit the derivation of (14), rather than only its substitution.  If
    # t=rho^2 and Cauchy equality holds, f_minus_u is forced as below.  The
    # difference of the two Bellman sums then factors through the unique
    # positive solution f_x=b_x/rho.
    fx_generic = sp.symbols("f_x", positive=True)
    fmu_from_cauchy = bx * bu / (r**2 * fx_generic)
    forward_generic = bx**2 / fx_generic + r**2 * fmu_from_cauchy
    reflected_generic = r**2 * fx_generic + bu**2 / fmu_from_cauchy
    bellman_difference_factor = sp.factor(forward_generic - reflected_generic)
    expected_difference_factor = sp.factor(
        s * (bx**2 - r**2 * fx_generic**2) / (bx * fx_generic)
    )
    derivation_factor_residual = sp.factor(
        bellman_difference_factor - expected_difference_factor
    )

    delta = sp.symbols("delta", real=True)
    delta_rule = s * (1 / r - r)
    radical_reduction = sp.factor(
        (delta / 2 + r * s - s * (r + 1 / r) / 2).subs(delta, delta_rule)
    )
    radical_square = sp.factor(
        (s * (r + 1 / r) / 2) ** 2
        - (s**2 + delta**2 / 4).subs(delta, delta_rule)
    )

    sx, su = sp.symbols("s_x s_u", nonnegative=True)
    geom_s = (sx + su) / 2
    geom_delta = x - u
    groebner = sp.groebner(
        [sx**2 + x**2 - 1, su**2 + u**2 - 1],
        sx,
        su,
        x,
        u,
        domain=sp.QQ,
    )
    radicand_identity = sp.expand(
        geom_s**2 + geom_delta**2 / 4 - (1 - x * u + sx * su) / 2
    )
    cs_identity = sp.expand(
        (1 - x * u) ** 2 - sx**2 * su**2 - (x - u) ** 2
    )
    radicand_residual = sp.factor(groebner.reduce(radicand_identity)[1])
    cs_residual = sp.factor(groebner.reduce(cs_identity)[1])

    w = sp.symbols("w", nonnegative=True)
    final_square_residual = sp.factor(
        sp.Rational(1, 4) - (-w**2 + w) - (w - sp.Rational(1, 2)) ** 2
    )

    # Independent hostile numerical guard of the final two-variable ceiling.
    rng = np.random.default_rng(119801)
    samples = rng.uniform(-1.0, 1.0, size=(250_000, 2))
    xx, uu = samples[:, 0], samples[:, 1]
    bxx = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - xx**2))
    buu = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - uu**2))
    values = xx * uu - 1.0 + np.sqrt((bxx + buu) ** 2 + (xx - uu) ** 2 / 4)
    equality_x = np.sqrt(3.0) / 2.0
    equality_b = 0.25
    equality_value = equality_x**2 - 1.0 + 2.0 * equality_b

    # Independent operator-level sharpness fixture.  At x=u=sqrt(3)/2 the
    # collapsed finite branch is the standard qubit I3322 value 1/4.
    eye = np.eye(2)
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]])
    sigma_z = np.diag([1.0, -1.0])
    pair = [
        (eye + equality_x * sigma_z - 0.5 * sigma_x) / 2,
        (eye + equality_x * sigma_z + 0.5 * sigma_x) / 2,
        (eye + sigma_x) / 2,
    ]
    bell = -np.kron(pair[1], eye) - np.kron(eye, pair[0]) - 2 * np.kron(eye, pair[1])
    for coefficient, ai, bj in [
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
        (-1, 0, 2), (1, 1, 2), (-1, 2, 0), (1, 2, 1),
    ]:
        bell += coefficient * np.kron(pair[ai], pair[bj])
    projector_residual = max(float(np.linalg.norm(p @ p - p, ord=2)) for p in pair)
    qubit_value = float(np.linalg.eigvalsh(bell).max())

    order_audit = {
        str(n): decreasing_bijection_count(n) for n in range(1, 10)
    }
    exact_residuals = {
        **{f"bellman_{key}": str(value) for key, value in bellman_sums.items()},
        **{f"ratio_{key}": str(value) for key, value in amplitude_ratios.items()},
        "ratio_to_radical": str(radical_reduction),
        "radical_square": str(radical_square),
        "radicand_identity_mod_unit_circles": str(radicand_residual),
        "cauchy_schwarz_identity_mod_unit_circles": str(cs_residual),
        "final_quarter_square": str(final_square_residual),
        "bellman_difference_factorization": str(derivation_factor_residual),
    }
    report = {
        "status": "exact equality-kernel scalar audit plus independent numerical guard",
        "exact_residuals": exact_residuals,
        "strictly_decreasing_bijection_counts": order_audit,
        "random_guard": {
            "samples": int(len(values)),
            "maximum": float(values.max()),
            "ceiling": 0.25,
            "known_equality_fixture": float(equality_value),
        },
        "qubit_boundary_fixture": {
            "projector_residual": projector_residual,
            "maximum_bell_eigenvalue": qubit_value,
            "expected": 0.25,
        },
        "all_gates_pass": bool(
            all(value == 0 for value in bellman_sums.values())
            and all(value == 0 for value in amplitude_ratios.values())
            and radical_reduction == 0
            and radical_square == 0
            and radicand_residual == 0
            and cs_residual == 0
            and final_square_residual == 0
            and derivation_factor_residual == 0
            and all(value == 1 for value in order_audit.values())
            and values.max() <= 0.25 + 1e-12
            and abs(equality_value - 0.25) <= 1e-15
            and projector_residual < 1e-14
            and abs(qubit_value - 0.25) < 1e-14
        ),
        "claim_boundary": (
            "The engine audits the finite-order lemma and scalar contradiction. "
            "The operator-kernel reduction is proved in the theorem document."
        ),
    }
    output = HERE / "equality-kernel-audit.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
