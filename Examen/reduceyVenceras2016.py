from typing import *

from algoritmia.utils import infinity
from sys import setrecursionlimit

setrecursionlimit(10000)


def solve(vector) -> Optional[int]:
    def merge(start, end):
        tam = end - start
        if tam <= 2:
            return -1
        if tam == 3:
            if vector[0] > vector[1] < vector[2]:
                return 1
        else:
            h = (start + end) // 2
            izda = merge(start, h)
            der = merge(h, end)

            # Parte izquierda
            if izda == -1:
                for i in range(start, h):
                    if start < i:
                        if vector[i - 1] > vector[i] < vector[i + 1]:
                            return i

            # Parte derecha
            if der == -1:
                for i in range(h, end):
                    if h < i < end and i != len(vector) - 1:
                        if vector[i - 1] > vector[i] < vector[i + 1]:
                            return i

            # Parte central
            if izda == -1 and der == -1:
                for i in range(start, end):
                    if start < i < end and i != len(vector) - 1:
                        if vector[i - 1] > vector[i] < vector[i + 1]:
                            return i
                return -1
            if izda != -1:
                return izda
            if der != -1:
                return der

    return merge(0, len(vector))


if __name__ == "__main__":
    vector1 = [4, 6]
    vector2 = [6, 2, 7]
    vector3 = [9, 10, 1, 5, 11, 7, 12, 9]

    sol1 = solve(vector1)
    sol2 = solve(vector2)
    sol3 = solve(vector3)
    print(sol1)
    print(sol2)
    print(sol3)
