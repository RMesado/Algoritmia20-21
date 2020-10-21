from Grafos.Problema1 import create_labyrinth

from algoritmia.datastructures.digraphs import UndirectedGraph
from labyrinthviewer import LabyrinthViewer
from sys import setrecursionlimit
from algoritmia.datastructures.queues import Fifo

from typing import *
import random

setrecursionlimit(10000)

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def recorredor_aristas_profundidad(g: UndirectedGraph, v_inicial: Vertex) -> List[Edge]:
    def recorrido_desde(u, v):
        seen.add(v)
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                recorrido_desde(v, suc)
        # aristas.append((u,v))

    aristas = []
    seen = set()
    recorrido_desde(v_inicial, v_inicial)
    return aristas


def recorredor_aristas_anchura(g: UndirectedGraph, v_inicial: Vertex) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))
    seen.add(v_inicial)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas


def recuperador_camino(lista_aristas: List[Edge], v: Vertex) -> List[Vertex]:
    # Crea diccionario punteros hacia atras
    bp = {}
    for orig, dest in lista_aristas:
        bp[dest] = orig
    # Reconstruye camino hacia atras
    camino = []
    camino.append(v)
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    # Invierte camino que estaba al reves
    camino.reverse()
    return camino


def shortest_path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    lista_aristas = recorredor_aristas_anchura(g, source)
    return recuperador_camino(lista_aristas, target)


def path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    lista_aristas = recorredor_aristas_profundidad(g, source)
    return recuperador_camino(lista_aristas, target)


if __name__ == "__main__":
    random.seed(1)
    num_rows = 60
    num_cols = 80
    g = create_labyrinth(num_rows, num_cols, 2000)

    camino_largo = path(g, (0, 0), (num_rows - 1, num_cols - 1))
    camino = shortest_path(g, (0, 0), (num_rows - 1, num_cols - 1))
    print(f"Camino largo: {len(camino_largo)}")
    print(f"Camino corto: {len(camino)}")

    lv = LabyrinthViewer(g, canvas_width=1200, canvas_height=800, margin=10)
    lv.add_path(camino_largo, 'blue')
    lv.add_path(camino, 'red')
    lv.run()
