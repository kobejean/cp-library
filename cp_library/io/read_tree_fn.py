import cp_library.io.__init__
from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.graph_cls import Graph


def read_tree(N, i0=1):
    T: Graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v = read(tuple[-i0,-i0])
        T[u].append(v)
        T[v].append(u)
    return T


# from cp_library.io.read_specs_fn import read
# from cp_library.alg.graph.graph_cls import Graph
