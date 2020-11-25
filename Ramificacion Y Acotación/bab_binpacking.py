from itertools import groupby
from random import seed, randint
from typing import *
from math import ceil
from bab_scheme import BabPartialSolution, BabSolver, Solution


def binpacking_solve(objects: List[int], capacity: int):
    class BinPackingBabPS(BabPartialSolution):
        def __init__(self, decisions: Tuple[int, ...], container_weights: Tuple[int, ...]):
            self.decisions = decisions
            self.container_weights = container_weights
            self.n = len(decisions)
            self._opt = self._calc_opt_bound()
            self._pes = self._calc_pes_bound()

        # TODO: IMPLEMENTAR - Relaja el problema. Trata los objetos que quedan como si fueran un líquido
        def _calc_opt_bound(self) -> Union[int, float]:
            if len(self.container_weights) == 0:
                return ceil(sum(objects) / capacity)

            mayor_hueco = capacity - min(self.container_weights)
            l_g = l_p = 0
            for num_obj in range(self.n, len(objects)):
                if objects[num_obj] > mayor_hueco:
                    l_g += objects[num_obj]
                else:
                    l_p += objects[num_obj]
            primer_menor_objeto = objects[-1]
            for num_camion in range(len(self.container_weights)):
                hueco = capacity - self.container_weights[num_camion]
                if capacity - objects[num_camion] >= primer_menor_objeto:
                    l_p -= hueco
            if l_p < 0: l_p = 0
            l_g += l_p
            return len(self.container_weights) + ceil(l_g/capacity)  # AHORA ES DEMASIADO OPTIMISTA

        # TODO: IMPLEMENTAR - Algoritmo voraz. Completa la solución parcial actual con "En el primero en el que quepa"
        def _calc_pes_bound(self) -> Union[int, float]:
            cw2 = list(self.container_weights)
            for num_obj in range(self.n, len(objects)):
                metido = False
                for num_camion in range(len(cw2)):
                    if cw2[num_camion] + objects[num_obj] <= capacity:
                        cw2[num_camion] += objects[num_obj]
                        metido = True
                        break
                if not metido:
                    cw2.append(objects[num_obj])
            return len(cw2)  # AHORA ES DEMASIADO PESIMISTA

        def is_solution(self) -> bool:
            return self.n == len(objects)

        def get_solution(self) -> Solution:
            return self.decisions

        def successors(self) -> Iterable["BinPackingBabPS"]:
            if self.n < len(objects):
                object_weight = objects[self.n]
                for num_container, container_weight in enumerate(self.container_weights):
                    if container_weight + object_weight <= capacity:
                        list_cw = list(self.container_weights)  # copia tupla a lista
                        list_cw[num_container] += object_weight
                        yield BinPackingBabPS(self.decisions + (num_container,), tuple(list_cw))
                num_container = len(self.container_weights)
                yield BinPackingBabPS(self.decisions + (num_container,), self.container_weights + (object_weight,))

    initial_ps = BinPackingBabPS((), ())
    return BabSolver.solve_minimization(initial_ps)


def show_solution_grouped_by_containers(sol: Solution):
    print("\nSOLUTION GROUPED BY CONTAINERS (shows the weights of objects in each container):")
    for pos, g in groupby(sorted([o, i] for i, o in enumerate(sol)), lambda e: e[0]):
        print("\t{}: {}".format(pos, [objs[e[1]] for e in g]))


def create_exact_binpacking_problem(num_containers: int, objects_per_container: int) -> Tuple[int, List[int]]:
    seed(5)
    objects = []
    num_c = num_containers
    num_e_c = objects_per_container
    min_v = 25
    max_v = 35
    capacity = max_v * num_e_c + 0
    for ic in range(num_c):
        s = 0
        for ie in range(num_e_c - 1):
            o = randint(min_v, max_v)
            objects.append(o)
            s += o
        objects.append(capacity - s)
    return capacity, list(sorted(objects, reverse=True))


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    # Descomenta la instancia del problema que quieras resolver:
    #C, objs = 10, [6, 6, 3, 3, 2, 2, 2, 2, 2, 2]  # SOLUCIÓN ÓPTIMA: 3 contenedores
    #C, objs = create_exact_binpacking_problem(6, 3)  # SOLUCIÓN ÓPTIMA: 6 contenedores
    C, objs = create_exact_binpacking_problem(12, 3) # SOLUCIÓN ÓPTIMA: 12 contenedores

    print("PROBLEM TO SOLVE:")
    print("\tContainer capacity:", C)
    print("\tObjects (weights):", objs)

    solution = binpacking_solve(objs, C)

    print("\nBEST SOLUTION:")
    print("\tB&B solution: {0} containers. Details: {1}".format(max(solution) + 1, solution))

    show_solution_grouped_by_containers(solution)
