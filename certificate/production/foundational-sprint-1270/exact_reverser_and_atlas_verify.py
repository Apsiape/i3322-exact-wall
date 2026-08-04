#!/usr/bin/env python3
"""Exact reverser identities plus corrected shooting-atlas scout."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.interpolate import PchipInterpolator
import sympy as sp


HERE = Path(__file__).resolve().parent
ENGINE_PATH = HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"
REFERENCE = np.array([-0.8660799622164113, -0.37693687789581193, 0.7999949210929129])


def exact_identities() -> dict:
    x, y, u, q, sx, sy = sp.symbols("x y u q sx sy", nonzero=True)
    d = x*y+(x-y)/2-1
    v = 2*(q-d-sx/(2*u))/sy
    d_reversed = (-y)*(-x)+((-y)-(-x))/2-1
    v_reversed = 2*(q-d_reversed-sy/(2*(1/v)))/sx
    v_residual = sp.factor(v_reversed-1/u)

    previous = (1-u**2*(2*y+1)+2*x*u/sx)/2
    reversed_next_coordinate = (
        ((1+2*y)-2*x*v_reversed/sx)/v_reversed**2-1
    )/2
    coordinate_residual = sp.factor(reversed_next_coordinate+previous)
    return {
        "reversed_cost_residual": str(sp.factor(d_reversed-d)),
        "reversed_ratio_residual": str(v_residual),
        "reversed_coordinate_residual": str(coordinate_residual),
        "all_exact_residuals_zero": all(
            value == 0
            for value in (sp.factor(d_reversed-d), v_residual, coordinate_residual)
        ),
    }


def load_engine():
    spec = importlib.util.spec_from_file_location("s1270_engine", ENGINE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def atlas() -> dict:
    engine = load_engine()
    ctx.prec = 250
    c = engine.arb_fraction(engine.decimal_fraction(
        "0.8782729451808124520614776394587039268823793661623032741"
    ))
    cd = engine.Dual(c, (arb(0), arb(0)))
    q = engine.q_formula(cd)
    series, mu = engine.parameterization(q, cd, 12)
    coeff = [[float(item.value.mid()) for item in row] for row in series]
    qv = float(q.value.mid())
    muv = float(mu.value.mid())

    def evaluate(t):
        return [float(np.polynomial.polynomial.polyval(t,row)) for row in coeff]

    def step(s):
        x,y,u=s; sx=np.sqrt(1-x*x); sy=np.sqrt(1-y*y)
        d=x*y+(x-y)/2-1
        v=2*(qv-d-sx/(2*u))/sy
        z=(((1-2*x)+2*y*v/sy)/(v*v)-1)/2
        return [y,z,v]

    rows=[]
    def add_chart(states):
        original=[]; reflected=[]
        for s in states:
            nxt=step(s); x,y,u=s; v=nxt[2]
            if abs(y)<=.905 and v>0:
                original.append((y,np.sqrt(1-y*y)*v/2,x))
            if abs(x)<=.905 and u>0:
                # R(s) has target -x, predecessor -y, and next ratio 1/u.
                reflected.append((-x,np.sqrt(1-x*x)/(2*u),-y))
        for chart in (original,reflected):
            chart.sort()
            if len(chart)>20:
                a=np.asarray(chart); keep=np.concatenate(([True],np.diff(a[:,0])>1e-13))
                rows.append(a[keep])

    t_hi=.0037582873342893243; t_lo=t_hi/muv
    add_chart([evaluate(t) for t in np.linspace(0,t_lo,1201)])
    central=[evaluate(t) for t in np.linspace(t_lo,t_hi,3001)]
    for _ in range(4):
        add_chart(central); central=[step(s) for s in central]
    # The fourth certified transition also certifies its target graph piece.
    add_chart(central)
    wing=[evaluate(t) for t in np.linspace(-.003719358976358651,0,2401)]
    for _ in range(2):
        add_chart(wing); wing=[step(s) for s in wing]
    # Likewise include the target of the second certified wing transition.
    add_chart(wing)

    charts=[(r[0,0],r[-1,0],PchipInterpolator(r[:,0],r[:,1]),PchipInterpolator(r[:,0],r[:,2])) for r in rows]
    # The shooting graph is the active carrier.  At the boundary contact its
    # terminal predecessor is 0.898116..., so reversibility supplies the graph
    # only down to its negative.  The remaining [-0.9,-terminal] interval is
    # Sprint 1217's separately priced inactive outer sliver and must not be
    # invented as a shooting chart.  All three registered drift roots lie in
    # the symmetric active carrier below.
    active_radius=.898
    sample=np.linspace(-active_radius,active_radius,7201); fs=[]; ps=[]; spreads=[]
    for value in sample:
        fv=[float(c[2](value)) for c in charts if c[0]<=value<=c[1]]
        pv=[float(c[3](value)) for c in charts if c[0]<=value<=c[1]]
        if not fv or not pv:
            raise ValueError(
                f"atlas gap at {value}: "
                f"{[(float(c[0]), float(c[1])) for c in charts]}"
            )
        fs.append(np.median(fv)); ps.append(np.median(pv))
        if len(fv)>1: spreads.append(max(fv)-min(fv))
    fs=np.asarray(fs); ps=np.asarray(ps)
    F=PchipInterpolator(sample,fs); P=PchipInterpolator(sample,ps)
    order=np.argsort(ps); px=ps[order]; py=sample[order]
    keep=np.concatenate(([True],np.diff(px)>1e-12)); Pinv=PchipInterpolator(px[keep],py[keep])
    chi=np.log(F(sample)/F(-sample))-np.log(F(-P(sample))/F(P(sample)))
    roots=[]
    for i in range(len(sample)-1):
        if chi[i]==0 or chi[i]*chi[i+1]<0:
            w=abs(chi[i])/(abs(chi[i])+abs(chi[i+1]))
            roots.append(float(sample[i]+(sample[i+1]-sample[i])*w))
    sep=[abs(float(Pinv(-float(P(r))))+r) for r in roots]
    error=float(np.max(np.abs(np.asarray(roots)-REFERENCE))) if len(roots)==3 else float("inf")
    return {
        "charts": len(charts),
        "symmetric_active_carrier": [-active_radius, active_radius],
        "maximum_F_overlap_spread": float(max(spreads)),
        "predecessor_min_increment": float(np.min(np.diff(ps))),
        "roots": roots,
        "maximum_root_difference": error,
        "horizontal_separations": sep,
        "corrected_atlas_pass": (
            max(spreads)<1e-4 and np.min(np.diff(ps))>-1e-6 and len(roots)==3
            and error<2e-3 and min(sep)>1/20
        ),
    }


def main():
    exact=exact_identities(); numerical=atlas()
    gates={
        "exact_reverser": exact["all_exact_residuals_zero"],
        "corrected_atlas": numerical["corrected_atlas_pass"],
    }
    report={
        "status":"exact shooting reverser and corrected numerical atlas",
        "exact":exact,
        "numerical":numerical,
        "gates":gates,
        "all_gates_pass":all(gates.values()),
        "claim_boundary":(
            "The reverser is exact. The atlas/root census is floating-point and "
            "does not replace the registered interval zero-count certificate."
        ),
    }
    assert report["all_gates_pass"],json.dumps(report,indent=2)
    (HERE/"exact-reverser-and-atlas-guard.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__": main()
