from typing import *
from algoritmia.utils import infinity
from math import ceil


def jarras_solver(c: List[int], p: List[int], m: List[int], L: int) -> float:
    def C(n, l):
        if n == 0 and l == 0:  # Caso 1
            return 0
        if n == 0 and l > 0:  # Caso 2
            return infinity

        if (n, l) not in mem:  # Caso con el min/max
            mem[n, l] = (infinity, ())  # Se añade una tupla vacia porque no sabemos que decision es
            for d in range(0, l // c[n - 1] + 1):  # Para cada decision (Parte de arriba de la flecha)
                # EL parentesis del min/max de la formila - Se añade al final lo de dentro de la C y d
                mem[n, l] = min(mem[n, l],
                                (C(n - 1, l - d * c[n - 1]) + ceil(d / m[n - 1]) * p[n - 1],
                                (n - 1, l - d * c[n - 1], d)))
        return mem[n, l][0]

    mem = {}
    score = C(len(c), L)
    decisions = []
    n, l = len(c), L
    while n > 0:
        (_, (n_prev, l_prev, d)) = mem[n, l]
        decisions.append(d)
        n, l = n_prev, l_prev
    decisions.reverse()
    return score, decisions


# Programa principal

C = [1, 2, 5, 10]
P = [1, 1.5, 4, 8]
M = [1, 1, 1, 1]
L = 333

print(jarras_solver(C, P, M, L))
