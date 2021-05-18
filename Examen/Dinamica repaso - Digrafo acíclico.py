from typing import *
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.utils import infinity

Solution = Tuple[int, Tuple[int]]


def cmc_col(g: Digraph, w: WeightingFunction, vi: int, vf: int) -> Solution:
    def p(v: int) -> int:
        if v == vi:
            return 0
        preds = g.preds(v)
        if len(preds) == 0:
            return infinity
        if v not in mem:
            mem[v] = min([(p(d) + w(d, v), d) for d in preds])
        return mem[v][0]

    mem = {}
    score = p(vf)
    v = vf
    decisions = [v]
    while (v != vi):
        if v not in mem: break
        (_, v_prev) = mem[v]
        decisions.append(v_prev)
        v = v_prev
    decisions.reverse()
    return score, decisions


# Programa principal
dic_pesos = {(0, 1): 10, (0, 2): 100, (1, 2): 10, (1, 3): 1, (3, 2): 1, (4, 3): 7}
g = Digraph(E=dic_pesos.keys())
w = WeightingFunction(dic_pesos)

print(cmc_col(g, w, 0, 3))
