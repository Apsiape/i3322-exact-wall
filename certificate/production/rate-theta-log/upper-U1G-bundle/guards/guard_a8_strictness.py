#!/usr/bin/env python3
"""U1G guard: the band-algebra strictness chain, exact + 60-digit.

Verifies proof CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md §3's chain from
anchored inputs only:
  G1: band identity D(t) + 2b(t) = s(1-s) for s = sqrt(1-t^2)
      (symbolic, exact) and s(1-s) <= 1/4 (exact; the Lean kernel
      carries the same lemmas machine-checked: band_identity,
      s_mul_one_sub_s_le_quarter, band_quarter_ceiling).
  G2: mu_min = 2 + 2(S_LO - 1/4) exact rational, > 2 strictly.
  G3: decaying root x = 2/(mu + sqrt(mu^2 - 4)) at mu_min; round-trip
      x + 1/x = mu; TWO-SIDED brackets on x and rho = x^2 around the
      proof's displayed safe bounds (x <= 0.9590241, rho <= 0.9197272).
  G4: kappa = -log rho >= 0.0836782; kappa_eff >= kappa/2 >= 0.0418391;
      TWO-SIDED bracket on 1/kappa_eff: 23.9010648 < 1/kappa_eff <
      23.9010650 (round-3 finding F6: the one-sided assert could not
      catch a factor-of-two bookkeeping error; now it can).
  G5: display-token concordance — the proof document's displayed
      decimals must agree digit-for-digit with the values this guard
      verifies (round-3 finding 8: no more guard-enforcing-one-number-
      while-the-proof-displays-another).
All asserts fail-capable; no file output.
"""

from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from mpmath import mp, mpf, sqrt as msqrt, log as mlog, nstr

HERE = Path(__file__).resolve().parent.parent
PROOF = HERE / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"

S_LO = F(2508753845015185, 10**16)


def g1_band():
    t = sp.symbols("t", real=True)
    s = sp.sqrt(1 - t**2)
    D = t * t + (t - t) / 2 - 1          # d(t,t)
    b = s / 2
    band = sp.simplify(D + 2 * b - (s - s**2))
    assert band == 0, "band identity D + 2b = s(1-s) fails"
    u = sp.symbols("u", real=True)
    # s(1-s) <= 1/4  <=>  (2s-1)^2 >= 0
    expr = sp.expand(sp.Rational(1, 4) - u * (1 - u) - (2 * u - 1)**2 / 4)
    assert expr == 0, "quarter-ceiling algebra identity fails"
    print("PASS G1 band identity + s(1-s) <= 1/4 (symbolic exact)")


def g2_mu():
    mu_min = F(2) + 2 * (S_LO - F(1, 4))
    assert mu_min > 2, "mu_min not > 2"
    assert mu_min == F(2001750769003037, 10**15), (
        f"mu_min exact value changed: {mu_min}")
    print(f"PASS G2 mu_min = {mu_min} > 2 (exact rational)")
    return mu_min


def g3_rho(mu_min: F):
    mp.dps = 60
    mu = mpf(mu_min.numerator) / mpf(mu_min.denominator)
    x = 2 / (mu + msqrt(mu * mu - 4))
    assert abs(x + 1 / x - mu) < mpf("1e-55"), "root round-trip fails"
    assert x < mpf("0.9590241"), f"x bound fails: {nstr(x, 12)}"
    assert x > mpf("0.9590240"), f"x bracket sanity: {nstr(x, 12)}"
    rho = x * x
    assert rho < mpf("0.9197272"), f"rho bound fails: {nstr(rho, 12)}"
    assert rho > mpf("0.9197271"), f"rho bracket sanity: {nstr(rho, 12)}"
    print(f"PASS G3 x = {nstr(x, 12)} <= 0.9590241; "
          f"rho = x^2 = {nstr(rho, 12)} <= 0.9197272 < 1")
    return rho


def g4_kappa(rho):
    kappa = -mlog(rho)
    assert kappa > mpf("0.0836782"), f"kappa bound fails: {nstr(kappa, 10)}"
    assert kappa < mpf("0.0836783"), f"kappa bracket sanity: {nstr(kappa, 10)}"
    keff_lower = kappa / 2
    assert keff_lower > mpf("0.0418391"), (
        f"kappa_eff lower bound fails: {nstr(keff_lower, 10)}")
    inv_keff = 2 / kappa
    assert inv_keff < mpf("23.9010650"), (
        f"1/kappa_eff upper bound fails: {nstr(inv_keff, 12)}")
    assert inv_keff > mpf("23.9010648"), (
        f"1/kappa_eff two-sided bracket fails (factor-of-two or "
        f"bookkeeping error): {nstr(inv_keff, 12)}")
    print(f"PASS G4 kappa >= 0.0836782 per index; kappa_eff >= 0.0418391; "
          f"23.9010648 < 1/kappa_eff = {nstr(inv_keff, 12)} < 23.9010650")
    return kappa


def g5_display_concordance(kappa):
    text = PROOF.read_text(encoding="utf-8")
    required = [
        "2.001750769003037",   # mu_min exact
        "0.9590241",           # x safe upper display
        "0.9197272",           # rho safe upper display
        "0.0836782",           # kappa safe lower display
        "0.0418391",           # kappa_eff safe lower display
        "23.9010650",          # 1/kappa_eff safe upper display
    ]
    for tok in required:
        assert tok in text, f"proof display token missing: {tok!r}"
    forbidden_displays = [
        "<= 0.9197271 ",       # down-rounded (false) upper bound
        "<= 23.9010649 ",      # down-rounded (false) upper bound
    ]
    for tok in forbidden_displays:
        assert tok not in text, (
            f"proof contains a down-rounded upper-bound display: {tok!r}")
    # CHAIN CHECK (round-4 F-02; round-5 integrity finding 5): parse
    # EVERY occurrence of the proof's displayed surrogate K_0 and
    # verify the written chain for each in exact rationals — a
    # restated unsafe surrogate anywhere in the document fails.
    import re
    # Round-6 blocker 1: accept BOTH identifiers — the round-5 blocker
    # named "K :=" and the M-02 rename must not narrow the tripwire.
    ks = re.findall(r"\bK(?:_0)? := ([0-9]+\.[0-9]+)", text)
    assert ks, "G5 cannot parse any displayed K/K_0 from the proof"
    for kstr in ks:
        K = F(kstr)
        assert mpf(K.numerator) / mpf(K.denominator) <= kappa, (
            f"G5 displayed K_0 is not a valid DOWN-round of kappa: {K}")
        assert F(2) / K <= F("23.9010650"), (
            f"G5 a displayed chain 2/K_0 exceeds the displayed bound: "
            f"2/{kstr} = {float(F(2)/K)}")
        assert K / 2 >= F("0.0418391"), (
            f"G5 a displayed chain K_0/2 falls below the displayed "
            f"lower bound: {float(K/2)}")
    # STRUCTURAL DISPLAY CHECK (round-5 proof findings I-01/I-02,
    # AI-4): every decimal appearing as a <=-display in a tracked
    # constant's numeric range must be a SAFE bound (>= the true
    # value); every >=-display must be <= the true value. This closes
    # the "add a false tighter display beside the true one" family
    # without blacklisting strings.
    mu_true = mpf(2001750769003037) / mpf(10**15)
    x_true = 2 / (mu_true + msqrt(mu_true**2 - 4))
    rho_true = x_true * x_true
    inv_true = 2 / kappa
    # Round-6 blocker 2: accept ALL comparison syntaxes — ASCII
    # strict/non-strict and the Unicode symbols (V2/V3).
    LE = r"(?:<=|<|≤)"
    GE = r"(?:>=|>|≥)"
    for v_str in re.findall(LE + r"\s*([0-9]+\.[0-9]+)", text):
        v = mpf(v_str)
        if 23 < v < 24:
            assert v >= inv_true, (
                f"G5 structural: upper display {v_str} is BELOW the "
                f"true 1/kappa_eff bound (false tighter display)")
        elif mpf("2") < v < mpf("3"):
            assert v >= mu_true, (
                f"G5 structural: upper display {v_str} is BELOW true "
                f"mu_min")
        elif mpf("0.95") < v < mpf("0.96"):
            assert v >= x_true, (
                f"G5 structural: upper display {v_str} is BELOW true x")
        elif mpf("0.90") < v <= mpf("0.95"):
            assert v >= rho_true, (
                f"G5 structural: upper display {v_str} is BELOW true "
                f"rho")
    for v_str in re.findall(GE + r"\s*([0-9]+\.[0-9]+)", text):
        v = mpf(v_str)
        if mpf("2") < v < mpf("3"):
            # Round-6 blocker 3 (V4): mu_min lower displays must not
            # exceed the true value.
            assert v <= mu_true, (
                f"G5 structural: lower display {v_str} EXCEEDS true "
                f"mu_min")
        elif mpf("0.083") < v < mpf("0.084"):
            assert v <= kappa, (
                f"G5 structural: lower display {v_str} EXCEEDS true "
                f"kappa")
        elif mpf("0.0418") < v < mpf("0.0419"):
            assert v <= kappa / 2, (
                f"G5 structural: lower display {v_str} EXCEEDS true "
                f"kappa_eff lower bound")
    print(f"PASS G5 display concordance + CHAIN CHECK on "
          f"{len(ks)} K_0 occurrence(s) + structural range check of "
          f"every <=/>= display, exact rationals")


def main() -> None:
    g1_band()
    mu = g2_mu()
    rho = g3_rho(mu)
    kappa = g4_kappa(rho)
    g5_display_concordance(kappa)
    print("U1G BAND-STRICTNESS GUARD: ALL PASS")


if __name__ == "__main__":
    main()
