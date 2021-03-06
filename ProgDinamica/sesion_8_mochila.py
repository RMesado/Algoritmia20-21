from typing import *

# Versión recursiva directa
from algoritmia.utils import infinity


def mochila_rec(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        # --------------------
        if n == 0:
            return 0  # quitar
        if c < w[n - 1]:
            return B(n - 1, c)
        else:
            return max(B(n - 1, c),
                       B(n - 1, c - w[n - 1]) + v[n - 1])
        # --------------------

    N = len(v)
    return B(N, C)


# Versión recursiva con memoización
def mochila_rec_mem(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        # --------------------
        if n == 0:
            return 0  # quitar
        if (n, c) not in mem:
            mem[n, c] = -infinity
            if c < w[n - 1]:
                mem[n, c] = B(n - 1, c)
            else:
                mem[n, c] = max(B(n - 1, c),
                                B(n - 1, c - w[n - 1]) + v[n - 1])
        return mem[n, c]
        # --------------------

    N = len(v)
    mem = {}
    return B(N, C)


# Versión recursiva con memoización y recuperación de camino
def mochila_rec_mem_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    def B(n: int, c: int) -> int:
        # --------------------
        # TODO: IMPLEMENTAR
        if n == 0:
            return 0  # quitar
        if (n, c) not in mem:
            if c < w[n - 1]:
                mem[n, c] = (B(n - 1, c), (n - 1, c, 0))
            else:
                mem[n, c] = max((B(n - 1, c), (n - 1, c, 0)),
                (B(n - 1, c - w[n - 1]) + v[n - 1], (n - 1, c - w[n - 1], 1)))

        return mem[n, c][0]
    # --------------------


    N = len(v)
    mem = {}
    score = B(N, C)
    sol = []
# --------------------
    n, c = N, C
    while n != 0:
        _, (nPrev, cPrev, d) = mem[n, C]
        sol.append(d)
        n, c = nPrev, cPrev
    sol.reverse()

    # --------------------
    return score, sol


# Versión iterativa con recuperación de camino
def mochila_iter_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(v)  # número de objetos
    # --------------------
    # TODO: IMPLEMENTAR rellenar tabla mem
    for c in range(0, C + 1):
        mem[0, c] = (0, ())
    for n in range(1, N + 1):
        for c in range(0, C + 1):
            if w[n - 1] > c:
                mem[n, c] = mem[n - 1, c][0], (n - 1, c, 0)
            else:
                mem[n, c] = max((mem[n - 1, c][0],(n - 1, c, 0))
                                ,(mem[n - 1, c - w[n - 1]][0] + v[n - 1], (n - 1, c - w[n - 1], 1)))
    # --------------------
    score = mem[N, C][0]
    sol = []
    # --------------------
    # TODO: IMPLEMENTAR recuperación de camino en sol
    n, c = N, C
    while n > 0:
        _, (n_previo, c_previo, d) = mem[n, c]
        sol.append(d)
        n, c = n_previo, c_previo
    sol.reverse()
    # --------------------
    return score, sol


# Versión iterativa con reduccion del coste espacial

def mochila_iter_reduccion_coste(v: List[int], w: List[int], C: int) -> int:
    N = len(v)  # número de objetos
    current = [0] * (C + 1)
    previous = [None] * (C + 1)
    # --------------------
    # TODO: IMPLEMENTAR usar dos columnas para rellenar la última de la tabla
    # --------------------
    return current[C]


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    values = [90, 75, 60, 20, 10]
    weights = [4, 3, 3, 2, 2]
    capacity = 6

    print("Versión recursiva:")
    print(mochila_rec(values, weights, capacity))
    print()
    print("Versión recursiva con memoización:")
    print(mochila_rec_mem(values, weights, capacity))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(mochila_rec_mem_camino(values, weights, capacity))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(mochila_iter_camino(values, weights, capacity))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(mochila_iter_reduccion_coste(values, weights, capacity))
