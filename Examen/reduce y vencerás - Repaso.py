from typing import *


def buscar_recursivo(elem: int, lista: list(int)) -> int:
    def rec(b: int, e: int) -> int:  # b inicial indice 0 y e inicial len(lista)
        if e - b <= 1:  # ---IsSimple()
            if lista[b] == elem:  # --|
                return b  # ----------|
            else:  # -----------------|--trivial_solution()
                return -1  # ---------|
            h = (e + b) // 2  # Decrease
            if lista[h] < elem:
                return rec(h, e)
            elif lista[h] > elem:
                return rec(b, h)
            else:
                return h  # Esto no es decrease, para ser decrease es return rec(h, h+1) para el esquema


def buscar_iterativo(elem: int, lista: list(int)) -> int:
    b = 0
    e = len(lista)
    while e - b > 1:  # Is_Simple()
        h = (e + b) // 2  # Decrease
        if lista[h] < elem:
            b = h
        elif lista[h] > elem:
            e = h
        else:
            return h  # Atajo

    if lista[b] == elem:  # trivial_Solution
        return b
    else:
        return -1
