from typing import Union, Iterable

from bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution


def energia_solver(V, W, CC, CE):
    class energiaPS(PartialSolutionWithOptimization):
        def __init__(self, decisions, V_atual, W_actual, CC_actual):
            self.decisions = decisions
            self.n = len(decisions)
            self.V_actual = V_atual
            self.W_actual = W_actual
            self.CC_actual = CC_actual

        def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
            if self.n < len(CC):
                yield energiaPS(self.decisions + (0,), self.V_actual, self.W_actual, self.CC_actual)
                if self.V_actual - CE[self.n] >= 0:
                    yield (energiaPS(self.decisions + (1,), self.V_actual - CE[self.n], self.W_actual,
                                     self.CC_actual + CC[self.n]))
                if self.W_actual - CE[self.n] >= 0:
                    yield (energiaPS(self.decisions + (2,), self.V_actual, self.W_actual - CE[self.n],
                                     self.CC_actual + CC[self.n]))

        def f(self) -> Union[int, float]:
            return -self.CC_actual

        def state(self) -> State:
            return self.n, self.V_actual, self.W_actual

        def is_solution(self) -> bool:
            return self.n == len(CC)

        def get_solution(self) -> Solution:
            return self.decisions, self.CC_actual, self.V_actual, self.W_actual

    initial_PS = energiaPS((), V, W, 0)
    return BacktrackingOptSolver.solve(initial_PS)
