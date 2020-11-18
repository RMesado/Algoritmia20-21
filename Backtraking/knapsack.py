from bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, decisions, current_weight,
                     current_value):  # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.decisions = decisions
            self.n = len(decisions)
            self.cur_weight = current_weight
            self.cur_value = current_value

        def is_solution(self) -> bool:  # IMPLEMENTAR
            return self.n == len(weights)

        def get_solution(self) -> Solution:  # IMPLEMENTAR
            return self.decisions, self.cur_weight, self.cur_value

        def successors(self) -> Iterable["KnapsackPS"]:  # IMPLEMENTAR
            if self.n < len(weights):
                new_weight = self.cur_weight + weights[self.n]  # Conocer la capacidad que queda
                if new_weight <= capacity:  # Si cabe
                    yield KnapsackPS(self.decisions + (1,), new_weight,
                                     self.cur_value + values[self.n])  # Se mete y actualiza el peso actual
                yield KnapsackPS(self.decisions + (0,), self.cur_weight,
                                 self.cur_value)  # No se mete y el peso se mantiene

        def state(self) -> State:  # IMPLEMENTAR
            return (self.n, self.cur_weight)

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -self.cur_value

    initialPS = KnapsackPS((), 0, 0)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
   #W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print(sol)
    print("\n<TERMINADO>")
