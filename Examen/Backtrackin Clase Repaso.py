from typing import *
from bt_scheme import *

Solution = Tuple[int, int, Tuple[int]]

# La version con yields es más rapida para obtener la primera solución.
#Lo comentado es la versión con returns
#C: Espacio disponible, W: Peso de cada objeto; V: Valor de cada objeto

def get_all_solutions(c: int, w: List[int], v: List[int]) -> List[Solution]:
    def bt(peso_actual: int, valor_actual: int, decisiones: Tuple[int]) -> List[Solution]:
        # Caso base
        n = len(decisiones)
        if n == len(w):  # is_solution del esquema algorítmico
            yield (peso_actual, valor_actual, decisiones)
            #return [(peso_actual, valor_actual, decisiones)]  # get_solution
        else:  # Recursividad -> Metodo successors           ---------------------------------------------
            yield from bt(peso_actual, valor_actual, decisiones + (0,)) #                                |
            # sols_no_coger_objeto_n = bt(peso_actual, valor_actual, decisiones + (0,))                  |
            if peso_actual + w[n] <= c:  # Mientras quepa                                                --- SUCCESSORS
                yield from bt(peso_actual + w[n], valor_actual + v[n], decisiones + (1,)) # -------------|
                # sols_si_coger_objeto_n = bt(peso_actual + w[n], valor_actual + v[n], decisiones + (1,))|
            #else: # No cabe porque se pasa de peso
                #sols_si_coger_objeto_n = [ ]
            #return sols_no_coger_objeto_n + sols_si_coger_objeto_n


    return bt(0, 0, ( ))  # Una tupla vacía es la instancia inicial

C = 30
w = [5, 10, 20, 25]
v = [7, 11, 24, 27]
for sol in get_all_solutions(C, w, v):
    print(sol)
