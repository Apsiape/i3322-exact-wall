"""Exact rational checks of the new finite weighted-flow separation lemma.

Exhaustive directed graphs through three vertices and selected larger graphs.
Analytic convex-envelope and critical-weld inputs are NOT verified here.
"""

from fractions import Fraction as F
from itertools import product
import random


def decomposition(n, edges):
    reach = [[i == j for j in range(n)] for i in range(n)]
    for i, j in edges:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    comps, owner = [], [-1] * n
    for i in range(n):
        if owner[i] >= 0:
            continue
        comp = [j for j in range(n) if reach[i][j] and reach[j][i]]
        for j in comp:
            owner[j] = len(comps)
        comps.append(comp)
    dag = {(owner[i], owner[j]) for i, j in edges if owner[i] != owner[j]}
    order, left = [], set(range(len(comps)))
    while left:
        available = [c for c in left if not any(b == c and a in left
                                                for a, b in dag)]
        assert available
        order.extend(sorted(available))
        left.difference_update(available)
    cyclic = [len(comp) > 1 or (comp[0], comp[0]) in edges for comp in comps]
    return reach, comps, owner, dag, order, cyclic


def certificate(n, edges, rates, data=None, c=F(1, 4)):
    reach, comps, owner, dag, order, cyclic = data or decomposition(n, edges)
    lows, highs = [], []
    for k, comp in enumerate(comps):
        if not cyclic[k]:
            continue
        if all(rates[v] <= 1 - c for v in comp):
            lows.append(k)
        elif all(rates[v] >= 1 + c for v in comp):
            highs.append(k)
        else:
            return None
    if any(reach[comps[a][0]][comps[b][0]] for a in lows for b in highs):
        return None
    U = {j for a in lows for j in range(n) if reach[comps[a][0]][j]}
    rmin, rmax = min(rates), max(rates)
    f = [F(0)] * n
    for k in order:
        if comps[k][0] not in U:
            continue
        previous = [a for a, b in dag if b == k]
        # Only U predecessors matter in the U condensation DAG.
        previous = [a for a in previous if comps[a][0] in U]
        g = max([F(1), 1 / c] +
                [rmax * (-f[comps[a][0]]) + 1 for a in previous])
        for v in comps[k]:
            f[v] = -g
    for k in reversed(order):
        if comps[k][0] in U:
            continue
        following = [b for a, b in dag if a == k and comps[b][0] not in U]
        value = max([1 / rmin, 1 / c] +
                    [(f[comps[b][0]] + 1) / rmin for b in following])
        for v in comps[k]:
            f[v] = value
    assert all(rates[i] * f[i] - f[j] >= 1 for i, j in edges)
    B = 4 + 2 * rmax + 2 / rmin + 2 / c
    assert max(map(abs, f)) <= B ** (n + 1)
    outgoing, incoming = [F(0)] * n, [F(0)] * n
    total = F(0)
    for i, j in edges:
        weight = F(1 + i + 2 * j, 1 + n)
        outgoing[i] += weight
        incoming[j] += weight
        total += weight
    residual = [rates[i] * outgoing[i] - incoming[i] for i in range(n)]
    assert total <= sum(a * b for a, b in zip(f, residual))
    assert total <= max(map(abs, f)) * sum(map(abs, residual))
    return f


def negative_controls():
    # Source orientation from the actual weld: r_A^2=g(-t)/g(t).
    # g(t)=4,g(-t)=1; an unnormalized state (2,1) is swapped to (1,2).
    r = (F(1, 2), F(2))
    psi = (F(2), F(1))
    assert (psi[1], psi[0]) == tuple(r[i] * psi[i] for i in range(2))
    p, q = (F(4, 5), F(1, 5)), (F(1, 5), F(4, 5))
    assert q == tuple(r[i] ** 2 * p[i] for i in range(2))
    assert q != tuple(p[i] / r[i] ** 2 for i in range(2))
    # Two homogeneous but opposite cycles connected by a directed path:
    # this is an EXACT positive balanced flow. The path condition is needed.
    n, rates = 2, (F(1, 2), F(2))
    edges = {(0, 0), (0, 1), (1, 1)}
    assert certificate(n, edges, rates) is None
    outgoing, incoming = (F(2), F(1)), (F(1), F(2))
    assert all(rates[i] * outgoing[i] == incoming[i] for i in range(n))
    # A single component with mixed gain signs also has an exact kernel.
    edges = {(0, 1), (1, 0)}
    assert certificate(n, edges, rates) is None
    assert all(rates[i] * outgoing[i] == incoming[i] for i in range(n))


def main():
    negative_controls()
    tried = passed = rejected = 0
    choices = (F(1, 2), F(1), F(2))
    for n in (1, 2, 3):
        pairs = list(product(range(n), repeat=2))
        for mask in range(1 << len(pairs)):
            edges = {pair for k, pair in enumerate(pairs) if mask & (1 << k)}
            data = decomposition(n, edges)
            for rates in product(choices, repeat=n):
                tried += 1
                result = certificate(n, edges, rates, data)
                if result is None:
                    rejected += 1
                else:
                    passed += 1
    rng = random.Random(20260910)
    larger = 0
    for n in (4, 6, 9):
        for _ in range(100):
            edges = {(i, j) for i in range(n) for j in range(n)
                     if rng.random() < F(1, 5)}
            rates = tuple(rng.choice(choices) for _ in range(n))
            result = certificate(n, edges, rates)
            larger += result is not None
    print(f"PASS: {tried} exhaustive graph/rate cases considered;")
    print(f"  {passed} admissible certificates, {rejected} rejected hypotheses.")
    print(f"PASS: {larger} admissible cases among 300 larger random cases.")
    print("PASS: both exact positive-kernel negative controls rejected.")
    print("PASS: physical two-fibre gain orientation; reciprocal error rejected.")
    print("Scope: finite graph lemma controls; NOT an analytic I3322 proof gate.")


if __name__ == "__main__":
    main()
