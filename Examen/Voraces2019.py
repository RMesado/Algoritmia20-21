from typing import *

# M: Espacio disponible; L: Cantidad de cada tipo de objeto; B: beneficio de cada objeto; P: Peso de cada objeto
def ej1(M: int, L: List[int], B: List[int], P: List[int]):
    sol = [0] * len(L)  # Paso 1: lista de solución vacía
    beneficio = 0
    peso_usado = 0 # Variable para hacer comprobaciones
    indices_ord_L = sorted(range(len(L)),
                           key=lambda i: -B[i] / P[i])  # Paso 2: ordenar una lista de indices de mayor a menor ratio Beneficio/Peso
    for i in indices_ord_L:
        # while p_act > 0:  # --------NO USAR BUCLE WHILE PEDAZO DE SUBNORMAL
        #   espacio_gastado = l_act * p_act
        #  if espacio_gastado <= M:
        #     M -= espacio_gastado
        #    sol[i] = p_act
        #   break
        # p_act -= 1
        cogemos = min(M // P[i], L[i])
        sol[i] = cogemos
        M -= cogemos * P[i]
        peso_usado += cogemos * P[i]
        beneficio += cogemos * B[i]

    return beneficio, sol, peso_usado


def beneficio(v: List[int], sol: List[int]) -> int:
    return sum([f * v[i] for i, f in enumerate(sol)])


if __name__ == "__main__":
    M = 50
    L = [2, 9, 5, 7, 6, 1, 4]
    P = [2, 3, 1, 6, 1, 2, 5]
    B = [3, 5, 10, 9, 4, 8, 1]
    sol = ej1(M, L, B, P)
    print('Cantidad Obj.: ', L)
    print('Pesos: ', P)
    print('Beneficio: ', B)
    print('Solucion(Beneficio, lista_sol, peso usado) y Beneficio calculado a parte:\n', sol, beneficio(B, sol[1]))
    peso = 0
    ratio = []
    for i in range(len(L)):
        ratio.append(B[i] / P[i])
    print('Ratio: ', ratio)
    for i in range(len(sol[1])):
        peso += sol[1][i] * P[i]
    print('Peso usado: ', peso)
