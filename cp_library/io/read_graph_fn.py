def read_graph(N, M, i0=1):
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = read(-i0)
        G[u].append(v)
        G[v].append(u)
    return G

from cp_library.io.read_int_fn import read