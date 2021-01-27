from sys import setrecursionlimit
from typing import *

setrecursionlimit(10000)


def examen2019(F, D, M):
    def examen(f, d: int):
        if f == 0:
            return 0
        if (f, d) not in mem:
            if f > 0 and d < M:
                mem[f, d] = (examen(f - 1, d), (f - 1, d, 0))
        else:
            mem[f, d] = max((examen(f - 1, d - k) + g(f, k), (f - 1, d - k, 1)))
        return mem[f, d][0]

    mem = {}
    score = examen(F, D)
    sol = []

    f, d = F, D
    while f != 0:
        _, (fPrev, dPrev, dec) = mem[f, D]
        sol.append(dec)
        f, d = fPrev, dPrev
    sol.reverse()

    return score, sol
