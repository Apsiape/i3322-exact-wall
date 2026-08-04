#!/usr/bin/env python3
"""Two-resolution max-plus Lyapunov scout for the Bellman derivative."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/"foundational-sprint-1272"/"normalization_defect_geometry_scout.py"
KAPPA=0.9


def load_source():
    spec=importlib.util.spec_from_file_location("s1276_source",SOURCE)
    module=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def cycles_of(successor: np.ndarray) -> list[list[int]]:
    globally_seen=np.zeros(len(successor),dtype=bool)
    cycles=[]
    for start in range(len(successor)):
        if globally_seen[start]:
            continue
        local={}; path=[]; current=start
        while not globally_seen[current] and current not in local:
            local[current]=len(path); path.append(current)
            current=int(successor[current])
        if current in local:
            cycles.append(path[local[current]:])
        for item in path:
            globally_seen[item]=True
    return cycles


def construct_weight(successor: np.ndarray, coefficient: np.ndarray, cycles: list[list[int]]) -> np.ndarray:
    logk=np.log(KAPPA)
    h=np.full(len(successor),np.nan)
    for cycle in cycles:
        h[cycle[0]]=0.0
        for node in cycle[:-1]:
            following=int(successor[node])
            h[following]=h[node]-np.log(coefficient[node])+logk
        # The final edge has the nonnegative cycle slack; do not overwrite h[0].
    for _ in range(len(successor)):
        changed=0
        for node in range(len(successor)):
            following=int(successor[node])
            if np.isnan(h[node]) and not np.isnan(h[following]):
                h[node]=np.log(coefficient[node])+h[following]-logk
                changed+=1
        if changed==0:
            break
    if np.any(np.isnan(h)):
        raise AssertionError("weight construction left an unpriced component")
    return np.exp(h-np.min(h))


def inspect(source, nodes: int) -> dict:
    reconstruction=source.reconstruct(nodes)
    F=reconstruction["F_callable"]
    P=reconstruction["P_callable"]
    grid=np.linspace(-.9,.9,3601)
    predecessor=np.asarray([P(float(x)) for x in grid])
    successor=np.clip(
        np.rint((predecessor+.9)/1.8*(len(grid)-1)).astype(int),
        0,len(grid)-1,
    )
    f_predecessor=np.asarray([F(float(x)) for x in predecessor])
    coefficient=(1-predecessor*predecessor)/(4*f_predecessor*f_predecessor)
    cycles=cycles_of(successor)
    cycle_rows=[]
    for cycle in cycles:
        cycle_rows.append({
            "length":len(cycle),
            "geometric_mean":float(np.exp(np.mean(np.log(coefficient[cycle])))),
            "coordinates":[float(grid[index]) for index in cycle],
        })
    weight=construct_weight(successor,coefficient,cycles)
    weighted=coefficient*weight[successor]/weight
    return {
        "bellman_nodes":nodes,
        "sample_points":len(grid),
        "unweighted_maximum":float(np.max(coefficient)),
        "unweighted_maximum_coordinate":float(grid[int(np.argmax(coefficient))]),
        "cycles":cycle_rows,
        "cycle_count":len(cycles),
        "maximum_cycle_geometric_mean":max(row["geometric_mean"] for row in cycle_rows),
        "weight_dynamic_range":float(np.max(weight)/np.min(weight)),
        "weighted_maximum":float(np.max(weighted)),
        "weighted_minimum":float(np.min(weighted)),
    }


def main() -> None:
    source=load_source()
    coarse=inspect(source,1601)
    fine=inspect(source,3201)
    gates={
        "local_amplification_present":min(coarse["unweighted_maximum"],fine["unweighted_maximum"])>1,
        "one_cycle_each":coarse["cycle_count"]==fine["cycle_count"]==1,
        "cycle_radius_below_point_nine":max(
            coarse["maximum_cycle_geometric_mean"],fine["maximum_cycle_geometric_mean"]
        )<KAPPA,
        "weighted_contraction":max(coarse["weighted_maximum"],fine["weighted_maximum"])<=KAPPA+1e-12,
        "weight_range_below_ten":max(
            coarse["weight_dynamic_range"],fine["weight_dynamic_range"]
        )<10,
    }
    report={
        "status":"two-resolution max-plus Bellman contraction scout; cycle-count prediction failed",
        "registered_kappa":KAPPA,
        "coarse":coarse,
        "fine":fine,
        "gates":gates,
        "all_gates_pass":all(gates.values()),
        "claim_boundary":(
            "This proves the displayed inequalities only on two finite sampled "
            "functional graphs. A continuous interval Lyapunov certificate is open."
        ),
    }
    (HERE/"weighted-bellman-contraction-scout.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8"
    )
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
