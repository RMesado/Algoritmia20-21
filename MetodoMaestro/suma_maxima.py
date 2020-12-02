from typing import *


def busca_pico(a: List[int]) -> Tuple(int, int, int):
    def rec(b: int, e: int) -> Tuple[int, int, int]:
        num_elem = e - b
        if num_elem == 0:
            return (0, 0, 0)
        if num_elem == 1:
            return (a[b], b, b + 1)
        else:  # decrease
            h = (b + e) // 2
            mejor_izda = rec(b, h)
            mejor_der = rec(h, e)
            mejor_centro = ...  # TODO
            return max(mejor_izda, mejor_der, mejor_centro)

    return rec(0, len(a))
