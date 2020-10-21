from algoritmia.datastructures.digraphs import UndirectedGraph
from labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo
from Utils.graph2dviewer import Graph2dViewer
from typing import *
import random

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def knight_graph(num_rows: int, num_cols: int) -> UndirectedGraph:
    vertices: List[Tuple] = []
    for r in range(num_rows):
        for c in range(num_cols):
            vertices.append((r, c))

    edges: List[Edge] = []
    for r, c in vertices:
        for (ir, ic) in [(-2, -1), (-1, -2), (-2, 1), (-1, 2)]:
            if 0 <= r + ir < num_rows and 0 <= c + ic < num_cols:
                edges.append(((r, c), (r + ir, c + ic)))

    return UndirectedGraph(V=vertices, E=edges)

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


if __name__ == "__main__":
    g = knight_graph(num_rows=8, num_cols=8)
    print(len(g.V), len(g.E))
    #lv = recorredor_aristas_anchura(g, (0,))
    lv = Graph2dViewer(g, (1200, 800))
    lv.run()
