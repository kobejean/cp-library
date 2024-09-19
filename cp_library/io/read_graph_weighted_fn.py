import cp_library.io.__init__
from cp_library.io.read_specs_fn import read

def read_graph(n: int, m: int, i0=1):
    G = [[] for _ in range(n)]
    for _ in range(m):
        u,v,w = read(tuple[-i0,-i0,int])
        G[u].append((w,v))
        G[v].append((w,u))
    return G
