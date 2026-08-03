#!/usr/bin/env python3
"""Independent mpmath interval core for the I3322 reconstruction.

This module deliberately contains no flint imports and loads no production
engine.  Complex arithmetic is built from rectangular real intervals.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable

from mpmath import iv
from mpmath.libmp import to_str


iv.dps = 90


def I(lo=0, hi=None):
    if isinstance(lo, iv.mpf):
        return lo
    if isinstance(lo, Fraction) and hi is None:
        return iv.mpf(lo.numerator) / iv.mpf(lo.denominator)
    if hi is None:
        hi = lo
    if isinstance(lo, Fraction) or isinstance(hi, Fraction):
        low_interval = I(lo) if isinstance(lo, Fraction) else iv.mpf(str(lo))
        high_interval = I(hi) if isinstance(hi, Fraction) else iv.mpf(str(hi))
        return iv.mpf([low_interval.a, high_interval.b])
    return iv.mpf([str(lo), str(hi)])


ZERO = I(0)
ONE = I(1)


def lo(x) -> float:
    return float(x.a)


def hi(x) -> float:
    return float(x.b)


def endpoint_text(x, digits: int = 100):
    return [to_str(x._mpi_[0], digits), to_str(x._mpi_[1], digits)]


def contains_zero(x) -> bool:
    return bool(x.a <= 0 and x.b >= 0)


def expand(x, radius):
    radius = I(radius)
    return iv.mpf([x.a - radius.b, x.b + radius.b])


def hull(a, b):
    return iv.mpf([min(a.a, b.a), max(a.b, b.b)])


def midpoint(x):
    return (x.a + x.b) / 2


def midpoint_float(x) -> float:
    return (lo(x) + hi(x)) / 2


def radius(x):
    return (x.b - x.a) / 2


def upper_abs(x):
    return max(abs(lo(x)), abs(hi(x)))


def square_iv(x):
    if contains_zero(x):
        return I(0, max(lo(x)**2, hi(x)**2))
    return x*x


@dataclass
class Dual:
    value: object
    derivative: tuple

    @staticmethod
    def lift(value, width: int = 2):
        if isinstance(value, Dual):
            return value
        return Dual(I(value), tuple(I(0) for _ in range(width)))

    def __add__(self, other):
        other = Dual.lift(other, len(self.derivative))
        return Dual(self.value + other.value, tuple(a + b for a, b in zip(self.derivative, other.derivative)))

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, tuple(-x for x in self.derivative))

    def __sub__(self, other):
        return self + (-Dual.lift(other, len(self.derivative)))

    def __rsub__(self, other):
        return Dual.lift(other, len(self.derivative)) - self

    def __mul__(self, other):
        other = Dual.lift(other, len(self.derivative))
        return Dual(self.value * other.value, tuple(a * other.value + self.value * b for a, b in zip(self.derivative, other.derivative)))

    __rmul__ = __mul__

    def reciprocal(self):
        value = 1 / self.value
        return Dual(value, tuple(-x / self.value**2 for x in self.derivative))

    def __truediv__(self, other):
        return self * Dual.lift(other, len(self.derivative)).reciprocal()

    def __rtruediv__(self, other):
        return Dual.lift(other, len(self.derivative)) / self

    def __pow__(self, power: int):
        if power < 0:
            return self.reciprocal() ** (-power)
        result = Dual.lift(1, len(self.derivative))
        base, exponent = self, power
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def sqrt(self):
        value = iv.sqrt(self.value)
        return Dual(value, tuple(x / (2 * value) for x in self.derivative))


def series_constant(value, order: int, width: int = 2):
    return [Dual.lift(value, width)] + [Dual.lift(0, width) for _ in range(order)]


def series_add(a, b):
    return [x + y for x, y in zip(a, b)]


def series_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def series_scale(a, scalar):
    return [x * scalar for x in a]


def series_mul(a, b):
    width = len(a[0].derivative)
    return [sum((a[k] * b[n-k] for k in range(n+1)), Dual.lift(0, width)) for n in range(len(a))]


def series_inv(a):
    width = len(a[0].derivative)
    out = [Dual.lift(0, width) for _ in a]
    out[0] = 1 / a[0]
    for n in range(1, len(a)):
        out[n] = -sum((a[k] * out[n-k] for k in range(1, n+1)), Dual.lift(0, width)) / a[0]
    return out


def series_div(a, b):
    return series_mul(a, series_inv(b))


def series_sqrt(a):
    width = len(a[0].derivative)
    out = [Dual.lift(0, width) for _ in a]
    out[0] = a[0].sqrt()
    for n in range(1, len(a)):
        middle = sum((out[k] * out[n-k] for k in range(1, n)), Dual.lift(0, width))
        out[n] = (a[n] - middle) / (2 * out[0])
    return out


def map_series(series, q: Dual):
    order = len(series[0])-1
    width = len(q.derivative)
    one = series_constant(1, order, width)
    x, y, u = series
    sx = series_sqrt(series_sub(one, series_mul(x, x)))
    sy = series_sqrt(series_sub(one, series_mul(y, y)))
    diagonal = series_sub(series_add(series_mul(x, y), series_scale(series_sub(x, y), Fraction(1, 2))), one)
    v = series_div(series_scale(series_sub(series_sub(series_constant(q, order, width), diagonal), series_div(sx, series_scale(u, 2))), 2), sy)
    numerator = series_add(series_sub(one, series_scale(x, 2)), series_div(series_scale(series_mul(y, v), 2), sy))
    z = series_scale(series_sub(series_div(numerator, series_mul(v, v)), one), Fraction(1, 2))
    return [list(y), z, v]


def solve_matrix(matrix, vector):
    n = len(vector)
    augmented = [list(matrix[i]) + [vector[i]] for i in range(n)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(midpoint_float(augmented[row][column].value)))
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        assert not contains_zero(divisor.value)
        augmented[column] = [entry/divisor for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [a-factor*b for a, b in zip(augmented[row], augmented[column])]
    return [augmented[i][-1] for i in range(n)]


def q_formula(c: Dual):
    return (4*c**4-5*c**2+2)/(4*c**2-1)


def parameterization(q: Dual, c: Dual, order: int):
    width = len(c.derivative)
    r = (1-c**2).sqrt()*(2*c-1)/((1-c)*(2*c+1))
    point = [c, c, r]
    columns = []
    for axis in range(3):
        local = [[point[row], Dual.lift(int(axis == row), width)] for row in range(3)]
        columns.append([entry[1] for entry in map_series(local, q)])
    jacobian = [[columns[j][i] for j in range(3)] for i in range(3)]
    aa = 4*c**3-3*c+1
    bb = 4*c**2*(1-4*c**2)
    dd = -4*c**3+3*c+1
    mu = (-bb+(bb**2-4*aa*dd).sqrt())/(2*aa)
    u_component = (jacobian[2][0]+jacobian[2][1]*mu)/(mu-jacobian[2][2])
    norm = (1+mu**2+u_component**2).sqrt()
    direction = [-1/norm, -mu/norm, -u_component/norm]
    series = [[Dual.lift(0, width) for _ in range(order+1)] for _ in range(3)]
    for row in range(3):
        series[row][0], series[row][1] = point[row], direction[row]
    for degree in range(2, order+1):
        image = map_series(series, q)
        matrix = [[Dual.lift(int(i == j), width)*mu**degree-jacobian[i][j] for j in range(3)] for i in range(3)]
        coefficient = solve_matrix(matrix, [image[row][degree] for row in range(3)])
        for row in range(3):
            series[row][degree] = coefficient[row]
    return series, mu


def evaluate(series, t: Dual):
    values = []
    for row in series:
        value = Dual.lift(0, len(t.derivative))
        for coefficient in reversed(row):
            value = value*t+coefficient
        values.append(value)
    return values


def step(state, q):
    x, y, u = state
    sx, sy = (1-x**2).sqrt(), (1-y**2).sqrt()
    diagonal = x*y+(x-y)/2-1
    v = 2*(q-diagonal-sx/(2*u))/sy
    z = (((1-2*x)+2*y*v/sy)/v**2-1)/2
    return [y, z, v]


def shooting(q: Dual, t: Dual, c: Dual, order: int = 12, steps: int = 3):
    series, _ = parameterization(q, c, order)
    state = evaluate(series, t)
    for _ in range(steps):
        state = step(state, q)
    crossing = step(state, q)
    after = step(crossing, q)
    return [crossing[0]+crossing[1], after[2]-1/crossing[2]]


@dataclass
class CRect:
    re: object
    im: object = ZERO

    @staticmethod
    def lift(value):
        if isinstance(value, CRect):
            return value
        return CRect(I(value), I(0))

    def __add__(self, other):
        other = CRect.lift(other)
        return CRect(self.re+other.re, self.im+other.im)

    __radd__ = __add__

    def __neg__(self):
        return CRect(-self.re, -self.im)

    def __sub__(self, other):
        return self+(-CRect.lift(other))

    def __rsub__(self, other):
        return CRect.lift(other)-self

    def __mul__(self, other):
        other = CRect.lift(other)
        return CRect(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def reciprocal(self):
        denominator = square_iv(self.re)+square_iv(self.im)
        assert not contains_zero(denominator)
        return CRect(self.re/denominator, -self.im/denominator)

    def __truediv__(self, other):
        return self*CRect.lift(other).reciprocal()

    def __rtruediv__(self, other):
        return CRect.lift(other)/self

    def __pow__(self, power: int):
        if power < 0:
            return self.reciprocal()**(-power)
        result, base, exponent = CRect.lift(1), self, power
        while exponent:
            if exponent & 1:
                result = result*base
            base = base*base
            exponent //= 2
        return result

    def abs(self):
        return iv.sqrt(square_iv(self.re)+square_iv(self.im))

    def sqrt(self):
        assert self.re.a > 0
        modulus = self.abs()
        real = iv.sqrt((modulus+self.re)/2)
        imag = self.im/(2*real)
        return CRect(real, imag)


def complex_step(state, q):
    x, y, u = state
    sx, sy = (1-x**2).sqrt(), (1-y**2).sqrt()
    diagonal = x*y+(x-y)/2-1
    v = 2*(q-diagonal-sx/(2*u))/sy
    z = (((1-2*x)+2*y*v/sy)/v**2-1)/2
    return [y, z, v]


def polynomial_value(coefficients: Iterable, t):
    value = t*0
    for coefficient in reversed(list(coefficients)):
        value = value*t+coefficient
    return value
