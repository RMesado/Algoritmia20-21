from bt_scheme import *
from typing import *
from copy import deepcopy

Position = Tuple[int, int]
Sudoku = List[List[int]]


def vacias(s: Sudoku) -> Set[Position]:
    # return set((fila, col) for fila in range(9) for col in range(9) if s[fila][col] == 0)
    vacios = set()
    for fila in range(9):
        for col in range(9):
            if s[fila][col] == 0:
                vacios.add((fila, col))
    return vacios


def posibles_en(s: Sudoku, fila: int, col: int) -> Set[int]:
    used = set(s[fila][c] for c in range(9))
    used = used.union(s[f][col] for f in range(9))
    fc, cc = fila // 3 * 3, col // 3 * 3
    used = used.union(s[fc + f][cc + c] for f in range(3) for c in range(3))
    return set(range(1, 10)) - used


def pretty_print(s: Sudoku):
    for i, fila in enumerate(s):
        for j, columna in enumerate(fila):
            print(columna if columna != 0 else ' ', end="")
            if j in [2, 5]:
                print("|", end="")
        print()
        if i in [2, 5]:
            print("---+---+---")


class SudokuPS(PartialSolution):
    def __init__(self, sudoku: Sudoku, vacias: Set[Position]):
        self.s = sudoku
        self.v = vacias

    # Indica si la sol. parcial es ya una solución factible (completa)
    def is_solution(self) -> bool:
        return len(self.v) == 0

    # Si es sol. factible, la devuelve. Si no lanza excepción
    def get_solution(self) -> Sudoku:
        return self.s

    # Devuelve la lista de sus sol. parciales sucesoras
    def successors(self) -> Iterable["SudokuPS"]:
        if len(self.v) > 0:

            # Con copia de self.v
            # v2 = set(self.v)
            # _, f, c = min([(len(posibles_en(self.s, f, c)), f, c) for (f, c) in v2])
            # v2.remove((f, c))

            # Sin copia de self.v
            _, f, c = min([(len(posibles_en(self.s, f, c)), f, c) for (f, c) in self.v])
            self.v.remove((f, c))

            for num in posibles_en(self.s, f, c):
                # Con copia de self.s
                # s2 = deepcopy(self.s)  # Opción 2: s2 = [fila[:] for fila in self.s]
                # s2[f][c] = num

                # Sin copia de self.s
                self.s[f][c] = num  # Modificamos el sudoku padre
                yield SudokuPS(self.s, self.v)  # Crear un SudokuPS nuevo
                self.s[f][c] = 0  # Lo devolvemos a su estado anterior, como si no hubiera pasado nada
            self.v.add((f, c))


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    # m_sudoku = [[0, 0, 0, 3, 1, 6, 0, 5, 9], [0, 0, 6, 0, 0, 0, 8, 0, 7], [0, 0, 0, 0, 0, 0, 2, 0, 0],
    #           [0, 5, 0, 0, 3, 0, 0, 9, 0], [7, 9, 0, 6, 0, 2, 0, 1, 8], [0, 1, 0, 0, 8, 0, 0, 4, 0],
    #          [0, 0, 8, 0, 0, 0, 0, 0, 0], [3, 0, 9, 0, 0, 0, 6, 0, 0], [5, 6, 0, 8, 4, 7, 0, 0, 0]]

    # El sudoku más difícil del mundo
    m_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    print("Original:")
    pretty_print(m_sudoku)
    print("\nSoluciones:")
    # Mostrar todas las soluciones
    # IMPLEMENTAR utilizando SudokuPS y BacktrackingSolver
    initial_ps = SudokuPS(m_sudoku, vacias(m_sudoku))
    for solution in BacktrackingSolver.solve(initial_ps):
        pretty_print(solution)
    print("<TERMINDADO>")  # Espera a ver este mensaje para saber que el programa ha terminado
