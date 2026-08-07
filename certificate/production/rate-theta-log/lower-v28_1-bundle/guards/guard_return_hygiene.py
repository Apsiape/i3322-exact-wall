#!/usr/bin/env python3
"""Non-tautological v28.1 two-fibre normalization/multiplier guards."""
from fractions import Fraction as F


def matvec(M,v):
    return [sum((M[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(M))]

def scale(c,M): return [[c*x for x in row] for row in M]
def ident(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def reverse(n): return [[F(int(j==n-1-i)) for j in range(n)] for i in range(n)]
def swap(R):
    n=len(R); Z=[[F(0) for _ in range(n)] for _ in range(n)]
    return [Z[i]+R[i] for i in range(n)] + [R[i]+Z[i] for i in range(n)]
def block_plus(v,n): return v[:n]
def block_minus(v,n): return v[n:]
def eq(a,b): return all(x==y for x,y in zip(a,b))
def mul(c,v): return [c*x for x in v]

def compose(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum((A[i][t]*B[t][j] for t in range(k)),F(0)) for j in range(m)] for i in range(n)]

def extract_gain(out,dest):
    pairs=[(o,d) for o,d in zip(out,dest) if d!=0]
    assert pairs
    gain=pairs[0][0]/pairs[0][1]
    assert all(o==gain*d for o,d in zip(out,dest))
    return gain

bA=F(3,7); bB=F(2,5)
a=F(2); c=F(3)
alpha=a/c
checks=0
for m in (1,2,4,8):
    IA=ident(m); RB=reverse(m)
    KA=swap(IA); KB=swap(RB)
    # involutive normalized transports
    I2=ident(2*m)
    assert compose(KA,KA)==I2 and compose(KB,KB)==I2
    WA=scale(bA,KA); WB=scale(bB,KB)
    u=[F(1) for _ in range(m)]  # fixed by both I and reversal
    psi=mul(a,u)+mul(c,u)
    # full multiplier law: K psi = r(X/U) psi with reciprocal fibre multipliers
    KAp=matvec(KA,psi); KBp=matvec(KB,psi)
    rplus=c/a; rminus=a/c
    target=mul(rplus,block_plus(psi,m))+mul(rminus,block_minus(psi,m))
    assert KAp==target and KBp==target

    # Source + fibre to one common destination - fibre.
    src=mul(a,u)+[F(0)]*m
    dest=block_minus(psi,m)
    outA=block_minus(matvec(KA,src),m)
    outB=block_minus(matvec(KB,src),m)
    assert eq(outA,mul(alpha,dest))
    beta=extract_gain(outB,dest)
    assert eq(outB,mul(beta,dest))
    assert alpha==beta

    # Raw W gains are NOT the F(q) gains when bA != bB.
    rawA=bA*alpha; rawB=bB*beta
    assert rawA/rawB == bA/bB and rawA/rawB != 1
    assert alpha/beta == 1

    # Isometry-only negative control for multiplicity >1: a different swap can
    # send the source to a nonparallel vector unless the multiplier law is imposed.
    if m>1:
        e0=[F(1)]+[F(0)]*(m-1)
        src_bad=mul(a,e0)+[F(0)]*m
        out_bad=block_minus(matvec(KB,src_bad),m)
        assert not eq(out_bad,mul(alpha,mul(c,e0)))
    checks+=1

# Exact F(q) neutral member and the v27 service-gap receipt.
def Fq(q): return (1+q)**2/(16*q)
assert Fq(F(1))==F(1,4)
q0=F(889,1000)
Slo=F(2508753845015185,10**16)
gap=Slo-Fq(q0)
assert gap == F(16308643699893,1778000000000000000) and gap>0

# Exact rho<->q orientation receipt on 1000 rationals.
for k in range(1,1001):
    rho=F(k,1000)
    q=min(rho,1/rho)
    assert q==rho
    assert (rho==1)==(q==1)

print('PASS v28.1 normalized two-fibre return guard')
print('  multiplicities tested = 1,2,4,8')
print('  multiplier-law alpha=beta verified; raw-gain negative control verified')
print('  S_- - F(889/1000)=', gap)
print('  rho<=1 => q_oriented=rho checked on 1000 rationals')
