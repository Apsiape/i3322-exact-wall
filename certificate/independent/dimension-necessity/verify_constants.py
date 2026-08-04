"""Independent arithmetic guard for the blind I3322 reconstruction.

This file contains no repository reads and no numerical Bell experiment.  It
only checks the rational/surd constant ledger and the elementary absorptions
used in RESULT-001.md.
"""

from decimal import Decimal, getcontext

getcontext().prec = 100

D = Decimal
sqrt40 = D(40).sqrt()
mu = D(7) / D(8000)
h0 = D(1) / D(10_000_000)
K = D(4656) / D(25)
H = (D(39) / D(10)) * K + mu * mu / D(2)
theta = mu * mu / (D(16) * H)
near_width = theta * h0 / D(20)
drift_gap = near_width / D(8)
C0 = D(100) * sqrt40 / h0
Cout = D(400) * D(1_000_000) ** 2 / D(1883) ** 2
CN = (D(4) / (mu * mu)) * (D(48) + D(6) * K + H * C0)
CI = Cout + CN + D(4) * sqrt40 / drift_gap
KR = D(84) * sqrt40 / (D(19) * drift_gap)
CF = KR + D(3) * (Cout + CN)
recurrence_packet = D(1872) / D(5)
terminal_packet = D(2808) / D(5)
terminal_exit = D(18252) / D(25)
total_packet = recurrence_packet + terminal_packet
A = D(6) * total_packet
B = (D(39) / D(5)) * total_packet + terminal_exit
M = D(78) / D(5)
Gamma = (D(20) * M) ** 4
candidates = [
    D(1),
    D(1) / (D(4) * CI * CI),
    D(1) / (D(8) * A),
    D(1) / (D(64) * B * B * CF * CF),
]
c = min(candidates)

assert D(4) * H * theta == mu * mu / D(4)
assert near_width == D(8) * drift_gap
assert Gamma == D(9_475_854_336)
assert A == D(5616)
assert B == D(200772) / D(25)
assert all(x > 0 for x in candidates)

for name, value in [
    ("mu", mu),
    ("H", H),
    ("theta", theta),
    ("near_width", near_width),
    ("drift_gap", drift_gap),
    ("C0", C0),
    ("Cout", Cout),
    ("CN", CN),
    ("CI", CI),
    ("KR", KR),
    ("CF", CF),
    ("A", A),
    ("B", B),
    ("Gamma", Gamma),
    ("c", c),
]:
    print(f"{name} = {value}")
