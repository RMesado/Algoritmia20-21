from typing import *
from bt_scheme import *
from sys import setrecursionlimit

setrecursionlimit(10000)


def resuelveDomino(F: List[Tuple], N: int):
    class CadenaDominoPS(PartialSolution):
        def __init__(self, decisiones: List[Tuple]):
            self.decisiones = decisiones
            self.n = len(decisiones)

        def is_solution(self) -> bool:
            if self.n==N:
                for i in range(N-1):
                    if decisiones[i][1]!=decisiones[i+1][0]:
                        return False
                return True
            return False

        def get_solution(self) -> Solution:
            return self.decisiones

        def successors(self) -> Iterable[Solution]:
            if self.n < N:
                for i in range(N):
                    if self.n == 0:
                        self.decisiones.append(F[i])
                        yield CadenaDominoPS(decisiones)
                        self.decisiones.remove(F[i])
                        self.decisiones.append(F[i][::-1])
                        yield CadenaDominoPS(decisiones)
                        self.decisiones.remove(F[i][::-1])
                    elif F[i] not in self.decisiones and F[i][::-1] not in self.decisiones:
                        if F[i][0] == self.decisiones[self.n - 1][1]:
                            self.decisiones.append(F[i])
                            yield CadenaDominoPS(decisiones)
                            self.decisiones.remove(F[i])

                        elif F[i][1] == self.decisiones[self.n - 1][1]:
                            self.decisiones.append(F[i][::-1])
                            yield CadenaDominoPS(decisiones)
                            self.decisiones.remove(F[i][::-1])
    decisiones = []
    return BacktrackingSolver.solve(CadenaDominoPS(decisiones))


if __name__ == "__main__":
    F = [(2, 3), (1, 6), (3, 3), (3, 6), (2, 6)]
    num_sol = 0
    for i in resuelveDomino(F, len(F)):
        num_sol+=1
    print(num_sol)
