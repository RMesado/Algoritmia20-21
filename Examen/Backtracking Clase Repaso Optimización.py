from bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State
from typing import *

Solution = Tuple[int, int, Tuple[int]]  # (Beneficio, peso, decisiones)


def tienda_solver(c: int, b: List[int], p: List[int], m: List[int]) -> Iterable[Solution]:
    class TiendaPS(PartialSolutionWithOptimization):
        def __init__(self, beneficio, cap_disponible, decisions):
            self.beneficio = beneficio
            self.cap_disponible = cap_disponible
            self.decisions = decisions
            self.n = len(decisions)

        def is_solution(self) -> bool:  # No chequear la capacidad, se mira en el successors
            return self.n == len(b)

        def get_solution(self) -> Solution:
            return (self.beneficio, self.cap_disponible, self.decisions)

        def successors(self) -> Iterable["TiendaPS"]:
            if self.n < len(b):
                max_numElec = min(self.cap_disponible // p[self.n], m[self.n])
                for numElec in range(max_numElec + 1):
                    yield TiendaPS(self.beneficio + numElec * b[self.n],
                                   self.cap_disponible - numElec * p[self.n],
                                   self.decisions + (numElec,))

        def state(self) -> State:
            return (self.n, self.cap_disponible)

        def f(self) -> Union[int, float]:
            # Cambio de signo porque por defecto siempre minimiza
            return -self.beneficio

    initial_ps = TiendaPS(0, C, ())
    return BacktrackingOptSolver.solve(initial_ps)


# Programa principal
C = 1000  # capacidad en Kg
b = (100, 911)  # beneficio de cada tipo de electrodomésticos
p = (100, 910)  # peso de cada tipo de electrodoméstico
m = (10000, 10000)  # máximo nº de unidades de cada tipo de electrodomestico que podemos vender

print("Mejor solución: ", tienda_solver(C, b, p, m))
for sol in tienda_solver(C, b, p, m):
    print(sol)
