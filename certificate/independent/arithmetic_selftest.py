#!/usr/bin/env python3
"""Exact-rational enclosure tests for the independent interval layer."""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path

from iv_core import I, iv


HERE = Path(__file__).resolve().parent


def encloses(interval, exact: Fraction) -> bool:
    target = I(exact)
    return bool(interval.a <= target.a and interval.b >= target.b)


def main() -> None:
    rng = random.Random(20260803)
    failures = []
    checks = 0
    for _ in range(4000):
        a = Fraction(rng.randint(-10_000, 10_000), rng.randint(1, 10_000))
        b = Fraction(rng.randint(-10_000, 10_000), rng.randint(1, 10_000))
        ia, ib = I(a), I(b)
        fixtures = [
            ("add", ia+ib, a+b),
            ("sub", ia-ib, a-b),
            ("mul", ia*ib, a*b),
        ]
        if b:
            fixtures.append(("div", ia/ib, a/b))
        for name, observed, exact in fixtures:
            checks += 1
            if not encloses(observed, exact) and len(failures) < 20:
                failures.append({"operation": name, "a": str(a), "b": str(b), "observed": str(observed), "exact": str(exact)})

    sqrt_checks = 0
    for _ in range(2000):
        value = Fraction(rng.randint(0, 10_000), rng.randint(1, 10_000))
        root = iv.sqrt(I(value))
        # Interval squaring is monotone here because the root is nonnegative.
        squared = root*root
        checks += 1
        sqrt_checks += 1
        if not encloses(squared, value) and len(failures) < 20:
            failures.append({"operation": "sqrt-square", "value": str(value), "root": str(root), "squared": str(squared)})

    result = {
        "status": "independent mpmath interval arithmetic self-test",
        "seed": 20260803,
        "rational_operation_checks": checks-sqrt_checks,
        "sqrt_checks": sqrt_checks,
        "total_checks": checks,
        "failure_count": len(failures),
        "first_failures": failures,
        "all_gates_pass": not failures and checks >= 10_000,
        "arithmetic_backend": "mpmath.iv real intervals; local rectangular complex layer",
        "forbidden_import_flint": True,
    }
    (HERE/"arithmetic-selftest.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    assert result["all_gates_pass"]


if __name__ == "__main__":
    main()
