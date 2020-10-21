from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle, seed
from labyrinthviewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def create_labyrinth(num_rows: int, num_cols: int, n: int = 0) -> UndirectedGraph:
    vertices: List[Tuple] = []
    for r in range(num_rows):
        for c in range(num_cols):
            vertices.append((r, c))

    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges: List[Edge] = []
    for r, c in vertices:
        if r > 0:
            edges.append(((r, c), (r - 1, c)))
        if c > 0:
            edges.append(((r, c), (r, c - 1)))
    shuffle(edges)

    corridors: List[Edge] = []

    for e in edges:
        (v, u) = e
        if mfs.find(v) != mfs.find(u):
            mfs.merge(v, u)
            corridors.append(e)
        else:
            if n > 0:
                corridors.append((u, v))
                n -= 1
    return UndirectedGraph(E=corridors)


# Programa Principal
if __name__ == "__main__":
    seed(42)
    graph = create_labyrinth(60, 80)
    lv = LabyrinthViewer(graph, canvas_width=1200, canvas_height=800, margin=10)
    lv.run()
