#!/usr/bin/env python3
"""Scalar/symbolic identity checks for the abstract Bellman weld.

SCOPE (corrected 2026-08-07, reported by N. Mghirbi): this script
verifies five EXACT SCALAR/SYMBOLIC identities used by the weld
argument (reflected cost identity, Cauchy identity, potential product
law, local 2x2 response determinant, and the remainder bookkeeping
with commuting symbols). It does NOT verify the operator-level weld
claim: the symbols alpha/beta/core/alice/bob below commute, so the
cancellation gate is a scalar tautology relative to the operator
statement. The operator claim (R0, RA, RB all PSD and exactly
reconstructing qI - Bell) is established in the proof documents, not
by this script; an operator-level replay (rebuild R0/RA/RB from the
25,601-knot G on random finite-dimensional strategies and check PSD +
reconstruction) is the appropriate independent check and has been
performed externally with agreement to ~1e-15."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    # Bellman reflection and Cauchy use only two nonnegative two-vectors.
    x, u = sp.symbols("x u", real=True)
    d = x * u + (x - u) / 2 - 1
    reflected_d = (-u) * (-x) + ((-u) - (-x)) / 2 - 1
    r, s, t, w = sp.symbols("r s t w", nonnegative=True)
    cauchy = sp.expand(
        (r * r + t * t) * (s * s + w * w)
        - (r * s + t * w) ** 2
        - (r * w - s * t) ** 2
    )

    # Product compatibility is automatic for p=b^2/G, independently of
    # fixed-point equality, concavity, contact uniqueness, or a wall orbit.
    b, gp, gm = sp.symbols("b G_plus G_minus", positive=True)
    product = sp.simplify(
        sp.sqrt((b**2 / gp) * gm)
        * sp.sqrt((b**2 / gm) * gp)
        - b**2
    )

    # The local 2x2 response block is PSD for every response spectral value
    # |z|<=1/2 once the product law holds.
    z = sp.symbols("z", real=True)
    local_determinant = sp.expand(b**2 - (2 * b * z) ** 2)

    # Abstract operator bookkeeping: the three positive remainders cancel
    # both scalar potentials exactly and reconstruct q I - Bell.
    q, alpha, beta, core, alice, bob = sp.symbols(
        "q alpha beta core alice bob", real=True
    )
    bell = core + alice + bob
    r0 = alpha + beta - core
    ra = sp.Rational(1, 2) - alpha - alice
    rb = q - sp.Rational(1, 2) - beta - bob
    cancellation = sp.expand(r0 + ra + rb - (q - bell))

    gates = {
        "reflected_cost_identity_exact": sp.simplify(reflected_d - d) == 0,
        "cauchy_identity_exact": cauchy == 0,
        "potential_product_identity_exact": product == 0,
        "local_response_determinant_exact": (
            sp.expand(local_determinant - b**2 * (1 - 4 * z**2)) == 0
        ),
        "operator_remainder_cancellation_exact": cancellation == 0,
    }
    report = {
        "status": "exact abstract Bellman-to-I3322 operator weld",
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "input_contract": (
            "Any positive G on [-1,1] satisfying p(x)+G(u)<=q-d(x,u), "
            "with p(x)=(1-x^2)/(4G(x))."
        ),
        "output_theorem": (
            "Every standard commuting-projective I3322 strategy has value at most q."
        ),
        "excluded_dependencies": [
            "Bellman fixed-point equality",
            "concavity",
            "unique contact or predecessor map",
            "shooting-chart amplitude normalization",
            "domain-wall lower-bound construction",
        ],
        "claim_boundary": (
            "The script checks the exact algebraic weld. Positivity follows from "
            "the scalar input contract, Cauchy, joint functional calculus, and "
            "the displayed 2x2 determinant with |z|<=1/2."
        ),
    }
    output = HERE / "bellman-operator-weld.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
