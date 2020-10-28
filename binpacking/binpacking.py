from typing import *
from random import random, seed


def mientras_quepa(W: List[int], C: int) -> List[int]:
    sol = []
    espacio_libre = C
    ultimo_contenedor = 0
    for w in W:
        if w > espacio_libre:
            espacio_libre = C
            ultimo_contenedor += 1
        espacio_libre -= w
        sol.append(ultimo_contenedor)
    return sol


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    sol = []
    contenedores = [C] * len(W)
    for w in W:
        for pos in range(len(contenedores)):
            if w <= contenedores[pos]:
                contenedores[pos] -= w
                sol.append(pos)
                break
    return sol


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    sol = [0] * len(W);
    contenedores = [C] * len(W)
    objetos = sorted(range(len(W)), key=lambda i: -W[i])
    for w in objetos:
        for pos in range(len(contenedores)):
            if W[w] <= contenedores[pos]:
                contenedores[pos] -= W[w]
                sol[w] = pos
                break
    return sol


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
