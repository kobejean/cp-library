import cp_library.io.__init__
from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.graph_cls import Graph


def read_graph(n: int, m: int, i0=1):
    G: Graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = read(tuple[-i0,-i0])
        G[u].append(v)
    return G
