from typing import *


def ej1(M: int, L: List[int], B: List[int], P: List[int]):
    sol = [0] * len(L)
    m_restante = M
    indices_ord_L = sorted(range(len(L)), key=lambda i: -B[i] / L[i])
    for i in indices_ord_L:
        for pos in range(len(L)):
            l_act = L[i]
            p_act = P[i]
            while p_act > 0:
                espacio_gastado = l_act * p_act
                if espacio_gastado <= m_restante:
                    m_restante -= espacio_gastado
                    sol[i] = p_act
                    break
                p_act -= 1
            break

    return sol


def beneficio(v: List[int], sol: List[int]) -> int:
    return sum([f * v[i] for i, f in enumerate(sol)])


if __name__ == "__main__":
    M = 94
    L = [2, 9, 5, 7, 6, 1, 4]
    P = [2, 3, 1, 6, 1, 2, 5]
    B = [3, 5, 10, 9, 4, 8, 1]
    sol = ej1(M, L, B, P)
    print(L)
    print(P)
    print(sol, beneficio(B, sol))
    peso = 0
    ratio = []
    for i in range(len(L)):
        ratio.append(B[i] / L[i])
    print(ratio)
    for i in range(len(sol)):
        peso += sol[i] * L[i]
    print(peso)
