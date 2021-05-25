from typing import *
from algoritmia.utils import infinity


def busca(lista: list(int)) -> (h, i, v, j):
    def rec(b: int, e: int) -> (int, int, int, int):
        if e - b <= 2:  # IsSimple()
            return (-infinity, 0, 0, 0)  # trivial_solution
        h = (b + e) // 2
        izda = rec(b, h)  # divide
        der = rec(h, e)
        cent = rec()???

        return max(izda, der, cent)
