#!/usr/bin/env python3
"""Arb interval-Newton proof for the degree-12 shooting system.

This certifies a zero of the *truncated* parameterization/reflection equations.
It deliberately does not claim that the truncated series is an exact unstable
manifold; that requires the separate analytic-tail estimate.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from flint import acb, arb, ctx


HERE = Path(__file__).resolve().parent
ctx.prec = 400


def decimal_fraction(text: str) -> Fraction:
    return Fraction(text)


def arb_fraction(value: Fraction, radius: Fraction | None = None) -> arb:
    midpoint = f"{value.numerator}/{value.denominator}"
    if radius is None:
        return arb(midpoint)
    return arb(midpoint, f"{radius.numerator}/{radius.denominator}")


@dataclass
class Dual:
    value: arb
    derivative: tuple[arb, arb]

    @staticmethod
    def lift(value: "Dual | arb | int | str") -> "Dual":
        if isinstance(value, Dual):
            return value
        if isinstance(value, Fraction):
            lifted = arb_fraction(value)
        else:
            lifted = value if isinstance(value, (arb, acb)) else arb(value)
        return Dual(lifted, (arb(0), arb(0)))

    def __add__(self, other):
        other = Dual.lift(other)
        return Dual(self.value + other.value, tuple(a + b for a, b in zip(self.derivative, other.derivative)))

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, tuple(-x for x in self.derivative))

    def __sub__(self, other):
        return self + (-Dual.lift(other))

    def __rsub__(self, other):
        return Dual.lift(other) - self

    def __mul__(self, other):
        other = Dual.lift(other)
        return Dual(
            self.value * other.value,
            tuple(a * other.value + self.value * b for a, b in zip(self.derivative, other.derivative)),
        )

    __rmul__ = __mul__

    def reciprocal(self):
        value = 1 / self.value
        return Dual(value, tuple(-x / self.value**2 for x in self.derivative))

    def __truediv__(self, other):
        return self * Dual.lift(other).reciprocal()

    def __rtruediv__(self, other):
        return Dual.lift(other) / self

    def __pow__(self, power: int):
        if power < 0:
            return (self.reciprocal()) ** (-power)
        result = Dual.lift(1)
        base = self
        exponent = power
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def sqrt(self):
        value = self.value.sqrt()
        return Dual(value, tuple(x / (2 * value) for x in self.derivative))


def series_constant(value, order: int):
    return [Dual.lift(value)] + [Dual.lift(0) for _ in range(order)]


def series_add(a, b):
    return [x + y for x, y in zip(a, b)]


def series_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def series_scale(a, scalar):
    return [x * scalar for x in a]


def series_mul(a, b):
    return [sum((a[k] * b[n - k] for k in range(n + 1)), Dual.lift(0)) for n in range(len(a))]


def series_inv(a):
    out = [Dual.lift(0) for _ in a]
    out[0] = 1 / a[0]
    for n in range(1, len(a)):
        out[n] = -sum((a[k] * out[n - k] for k in range(1, n + 1)), Dual.lift(0)) / a[0]
    return out


def series_div(a, b):
    return series_mul(a, series_inv(b))


def series_sqrt(a):
    out = [Dual.lift(0) for _ in a]
    out[0] = a[0].sqrt()
    for n in range(1, len(a)):
        middle = sum((out[k] * out[n - k] for k in range(1, n)), Dual.lift(0))
        out[n] = (a[n] - middle) / (2 * out[0])
    return out


def map_series(series, q: Dual):
    order = len(series[0]) - 1
    one = series_constant(1, order)
    x, y, u = series
    sx = series_sqrt(series_sub(one, series_mul(x, x)))
    sy = series_sqrt(series_sub(one, series_mul(y, y)))
    diagonal = series_sub(series_add(series_mul(x, y), series_scale(series_sub(x, y), Fraction(1, 2))), one)
    v = series_div(
        series_scale(series_sub(series_sub(series_constant(q, order), diagonal), series_div(sx, series_scale(u, 2))), 2),
        sy,
    )
    numerator = series_add(series_sub(one, series_scale(x, 2)), series_div(series_scale(series_mul(y, v), 2), sy))
    z = series_scale(series_sub(series_div(numerator, series_mul(v, v)), one), Fraction(1, 2))
    return [list(y), z, v]


def solve_matrix(matrix, vector):
    n = len(vector)
    augmented = [list(matrix[i]) + [vector[i]] for i in range(n)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(float(augmented[row][column].value.mid())))
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        assert not divisor.value.contains(0)
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [a - factor * b for a, b in zip(augmented[row], augmented[column])]
    return [augmented[i][-1] for i in range(n)]


def q_formula(c: Dual):
    return (4 * c**4 - 5 * c**2 + 2) / (4 * c**2 - 1)


def q_derivative(c: arb):
    return 2 * c * (4 * c**2 - 3) * (4 * c**2 + 1) / ((2 * c - 1) ** 2 * (2 * c + 1) ** 2)


def root_bracket(q_center: Fraction, q_radius: Fraction, c_center: Fraction, c_radius: Fraction):
    q_lo, q_hi = q_center - q_radius, q_center + q_radius
    c_lo, c_hi = c_center - c_radius, c_center + c_radius

    def polynomial(c, q):
        return 4 * c**4 - 5 * c**2 + 2 - q * (4 * c**2 - 1)

    assert polynomial(c_lo, q_lo) < 0
    assert polynomial(c_hi, q_hi) > 0
    return arb_fraction(c_center, c_radius)


def parameterization(q: Dual, c: Dual, order: int):
    r = (1 - c**2).sqrt() * (2 * c - 1) / ((1 - c) * (2 * c + 1))
    point = [c, c, r]

    columns = []
    for axis in range(3):
        local = [[point[row], Dual.lift(int(axis == row))] for row in range(3)]
        columns.append([entry[1] for entry in map_series(local, q)])
    jacobian = [[columns[j][i] for j in range(3)] for i in range(3)]

    aa = 4 * c**3 - 3 * c + 1
    bb = 4 * c**2 * (1 - 4 * c**2)
    dd = -4 * c**3 + 3 * c + 1
    mu = (-bb + (bb**2 - 4 * aa * dd).sqrt()) / (2 * aa)
    u_component = (jacobian[2][0] + jacobian[2][1] * mu) / (mu - jacobian[2][2])
    norm = (1 + mu**2 + u_component**2).sqrt()
    direction = [-1 / norm, -mu / norm, -u_component / norm]

    series = [[Dual.lift(0) for _ in range(order + 1)] for _ in range(3)]
    for row in range(3):
        series[row][0] = point[row]
        series[row][1] = direction[row]
    for degree in range(2, order + 1):
        image = map_series(series, q)
        matrix = [
            [Dual.lift(int(i == j)) * mu**degree - jacobian[i][j] for j in range(3)]
            for i in range(3)
        ]
        coefficient = solve_matrix(matrix, [image[row][degree] for row in range(3)])
        for row in range(3):
            series[row][degree] = coefficient[row]
    return series, mu


def evaluate(series, t: Dual):
    values = []
    for row in series:
        value = Dual.lift(0)
        for coefficient in reversed(row):
            value = value * t + coefficient
        values.append(value)
    return values


def step(state, q):
    x, y, u = state
    sx = (1 - x**2).sqrt()
    sy = (1 - y**2).sqrt()
    diagonal = x * y + (x - y) / 2 - 1
    v = 2 * (q - diagonal - sx / (2 * u)) / sy
    z = (((1 - 2 * x) + 2 * y * v / sy) / v**2 - 1) / 2
    return [y, z, v]


def shooting(q: Dual, t: Dual, c: Dual, order: int = 12, steps: int = 3):
    series, _ = parameterization(q, c, order)
    state = evaluate(series, t)
    for _ in range(steps):
        state = step(state, q)
    crossing = step(state, q)
    after = step(crossing, q)
    return [crossing[0] + crossing[1], after[2] - 1 / crossing[2]]


def interval_inverse_2x2(j):
    determinant = j[0][0] * j[1][1] - j[0][1] * j[1][0]
    assert not determinant.contains(0)
    return [
        [j[1][1] / determinant, -j[0][1] / determinant],
        [-j[1][0] / determinant, j[0][0] / determinant],
    ]


def matvec(matrix, vector):
    return [sum((matrix[i][j] * vector[j] for j in range(len(vector))), arb(0)) for i in range(len(matrix))]


def main() -> None:
    order = 12
    steps = 3
    q_center = decimal_fraction("0.250875384513976535617336610945947773366494880828229841631130356952704664237")
    t_center = decimal_fraction("0.00375828733428932426644591899620669106766298401865537960944481386320752563003")
    c_center = decimal_fraction("0.8782729451808124520614776394587039268823793661623032741245323669525128359013555849466448306991773688")

    q_radius = Fraction(1, 10**48)
    t_radius = Fraction(1, 10**48)
    c_radius = Fraction(1, 10**45)
    c_box = root_bracket(q_center, q_radius, c_center, c_radius)
    q_box = arb_fraction(q_center, q_radius)
    t_box = arb_fraction(t_center, t_radius)
    c_dual_box = Dual(c_box, (1 / q_derivative(c_box), arb(0)))
    residual_box = shooting(
        Dual(q_box, (arb(1), arb(0))),
        Dual(t_box, (arb(0), arb(1))),
        c_dual_box,
        order,
        steps,
    )
    jacobian_box = [[residual_box[i].derivative[j] for j in range(2)] for i in range(2)]

    # Point evaluation uses an independently certified much tighter C bracket.
    q_point_radius = Fraction(0)
    c_point_radius = Fraction(1, 10**88)
    c_point = root_bracket(q_center, q_point_radius, c_center, c_point_radius)
    residual_point = shooting(
        Dual(arb_fraction(q_center), (arb(1), arb(0))),
        Dual(arb_fraction(t_center), (arb(0), arb(1))),
        Dual(c_point, (1 / q_derivative(c_point), arb(0))),
        order,
        steps,
    )
    f_point = [entry.value for entry in residual_point]

    inverse_box = interval_inverse_2x2(jacobian_box)
    correction = matvec(inverse_box, f_point)
    newton = [arb_fraction(q_center) - correction[0], arb_fraction(t_center) - correction[1]]
    inclusion = [q_box.contains_interior(newton[0]), t_box.contains_interior(newton[1])]
    assert all(inclusion)

    result = {
        "status": "Arb interval-Newton certificate for the degree-12 truncated shooting zero",
        "precision_bits": ctx.prec,
        "order": order,
        "steps": steps,
        "starting_box": {
            "q": str(q_box),
            "t": str(t_box),
            "c_enclosure": str(c_box),
        },
        "point_residual": [str(value) for value in f_point],
        "jacobian_box": [[str(value) for value in row] for row in jacobian_box],
        "newton_image": {"q": str(newton[0]), "t": str(newton[1])},
        "strict_inclusion": inclusion,
        "claim_boundary": (
            "This proves existence and uniqueness of a zero inside the displayed "
            "box for the degree-12 truncated coefficient/reflection system. It "
            "does not validate the infinite power-series tail."
        ),
    }
    (HERE / "validated-truncated-shooting.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
