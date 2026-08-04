#!/usr/bin/env python3
"""Test lower-envelope selection across folded shooting characteristics."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.interpolate import PchipInterpolator


HERE = Path(__file__).resolve().parent
ENGINE_PATH = HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"
BELLMAN_PATH = HERE.parent / "foundational-sprint-1272" / "normalization_defect_geometry_scout.py"
REFERENCE = np.array([-0.8660799622164113, -0.37693687789581193, 0.7999949210929129])


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run(selector: str = "least") -> dict:
    engine = load(ENGINE_PATH, "s1274_engine")
    bellman = load(BELLMAN_PATH, "s1274_bellman")
    ctx.prec = 250
    c = engine.arb_fraction(engine.decimal_fraction(
        "0.8782729451808124520614776394587039268823793661623032741"
    ))
    cd = engine.Dual(c, (arb(0), arb(0)))
    q = engine.q_formula(cd)
    series, _mu = engine.parameterization(q, cd, 12)
    coefficients = [
        [float(entry.value.mid()) for entry in row] for row in series
    ]
    q_value = float(q.value.mid())

    def evaluate(t: float) -> list[float]:
        return [
            float(np.polynomial.polynomial.polyval(t, row))
            for row in coefficients
        ]

    def step(state: list[float]) -> list[float] | None:
        x, y, u = state
        if abs(x) >= 1 or abs(y) >= 1 or u == 0:
            return None
        sx = np.sqrt(1-x*x)
        sy = np.sqrt(1-y*y)
        diagonal = x*y+(x-y)/2-1
        v = 2*(q_value-diagonal-sx/(2*u))/sy
        z = (((1-2*x)+2*y*v/sy)/(v*v)-1)/2
        if not np.isfinite(v) or not np.isfinite(z):
            return None
        return [y,z,v]

    rows = []

    def family(parameters: np.ndarray, iterates: int) -> None:
        states = [evaluate(float(t)) for t in parameters]
        for _ in range(iterates):
            chart = []
            next_states = []
            for state in states:
                nxt = step(state)
                next_states.append(nxt)
                if nxt is None:
                    continue
                x,y,_u = state
                v = nxt[2]
                if -.905 <= y <= .905 and v > 0:
                    chart.append((y,np.sqrt(1-y*y)*v/2,x))
            if len(chart)>50:
                chart.sort()
                data=np.asarray(chart)
                keep=np.concatenate(([True],np.diff(data[:,0])>1e-13))
                data=data[keep]
                if len(data)>50:
                    rows.append(data)
            states=[state for state in next_states if state is not None]
            if len(states)!=len(parameters):
                break

    family(np.linspace(0,.0037582873342893243,3001),11)
    family(np.linspace(-.003719358976358651,0,2401),3)
    charts=[]
    for row in rows:
        if not np.all(np.diff(row[:,0])>0):
            continue
        f_chart=PchipInterpolator(row[:,0],row[:,1])
        p_chart=PchipInterpolator(row[:,0],row[:,2])
        charts.append((row[0,0],row[-1,0],f_chart,p_chart,p_chart.derivative()))

    sample=np.linspace(-.9,.9,7201)
    selected_f=[]; selected_p=[]; multiplicities=[]; gaps=[]
    coverage=True; first_uncovered=None
    for x in sample:
        candidates=[
            (float(chart[2](x)),float(chart[3](x)),index,float(chart[4](x)))
            for index,chart in enumerate(charts) if chart[0]<=x<=chart[1]
        ]
        candidates=[row for row in candidates if row[0]>0 and np.isfinite(row[0])]
        if selector == "stable_least":
            candidates=[row for row in candidates if row[3]>0]
        elif selector != "least":
            raise ValueError(selector)
        if not candidates:
            coverage=False
            first_uncovered=float(x)
            break
        candidates.sort(key=lambda row: row[0])
        selected_f.append(candidates[0][0]); selected_p.append(candidates[0][1])
        multiplicities.append(len(candidates))
        gaps.append(candidates[1][0]-candidates[0][0] if len(candidates)>1 else float("inf"))

    if not coverage:
        gates={
            "complete_coverage":False,
            "selected_predecessor_near_monotone":False,
            "exactly_three_roots":False,
            "registered_root_agreement":False,
            "global_F_agreement":False,
            "global_P_agreement":False,
        }
        return {
            "status":"characteristic-atlas selector test",
            "selector":selector,
            "shooting_charts":len(charts),
            "first_uncovered_coordinate":first_uncovered,
            "maximum_sheet_multiplicity_before_failure":(
                max(multiplicities) if multiplicities else 0
            ),
            "gates":gates,
            "all_gates_pass":False,
            "claim_boundary":(
                "The registered selector fails coverage before any global "
                "profile or root census can be formed."
            ),
        }
    selected_f=np.asarray(selected_f); selected_p=np.asarray(selected_p)
    F=PchipInterpolator(sample,selected_f)
    P=PchipInterpolator(sample,selected_p)
    D=F(sample)*F(P(sample))-F(-sample)*F(-P(sample))
    roots=[]
    for index in range(len(sample)-1):
        if D[index]==0 or D[index]*D[index+1]<0:
            weight=abs(D[index])/(abs(D[index])+abs(D[index+1]))
            roots.append(float(sample[index]*(1-weight)+sample[index+1]*weight))

    reference=bellman.reconstruct(1601)
    reference_F=reference["F_callable"]
    reference_P=reference["P_callable"]
    reference_f=np.asarray([float(reference_F(x)) for x in sample])
    reference_p=np.asarray([float(reference_P(float(x))) for x in sample])
    root_error=(
        float(np.max(np.abs(np.asarray(roots)-REFERENCE)))
        if len(roots)==3 else float("inf")
    )
    finite_gaps=[gap for gap in gaps if np.isfinite(gap)]
    gates={
        "complete_coverage": coverage,
        "selected_predecessor_near_monotone": float(np.min(np.diff(selected_p)))>-1e-4,
        "exactly_three_roots": len(roots)==3,
        "registered_root_agreement": root_error<2e-3,
        "global_F_agreement": float(np.max(np.abs(selected_f-reference_f)))<2e-3,
        "global_P_agreement": float(np.max(np.abs(selected_p-reference_p)))<2e-2,
    }
    report={
        "status":"characteristic-atlas selector test",
        "selector":selector,
        "shooting_charts":len(charts),
        "maximum_sheet_multiplicity":max(multiplicities),
        "minimum_selected_sheet_gap":float(min(finite_gaps)),
        "selected_predecessor_minimum_increment":float(np.min(np.diff(selected_p))),
        "roots":roots,
        "maximum_root_difference":root_error,
        "maximum_F_disagreement":float(np.max(np.abs(selected_f-reference_f))),
        "maximum_P_disagreement":float(np.max(np.abs(selected_p-reference_p))),
        "gates":gates,
        "all_gates_pass":all(gates.values()),
        "claim_boundary":(
            "This is a floating-point selector test. Passing would identify an "
            "interval-atlas strategy but would not prove Bellman envelope selection."
        ),
    }
    return report


def main() -> None:
    report=run("least")
    (HERE/"lower-envelope-characteristic-atlas.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8"
    )
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
