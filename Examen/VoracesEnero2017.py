from math import floor, ceil
from typing import *


def menor_numero_intervalos(puntos: List[float], a: float) -> int:
    sol = []
    indices = sorted(range(len(puntos)), key=lambda i: puntos[i])
    aux = [0.0, 0.0]
    for i in range(len(indices)):
        if i == 0:
            aux = [puntos[indices[i]], puntos[indices[i]] + a]
            sol.append(aux)
        elif puntos[indices[i]] > aux[1]:
            aux = [puntos[indices[i]], puntos[indices[i]] + a]
            sol.append(aux)

    print("Solución: ", sol)
    return len(sol)


F = [1.0, 3.5, 9, 2.5, 7.0]
a = 3.0
print("Numero de intervalos de tamaño a =", a, ": ", menor_numero_intervalos(F, a))
