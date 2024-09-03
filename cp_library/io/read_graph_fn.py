from cp_library.io.rint_fn import rint

def read_graph(N, M, i0=1):
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = rint(-i0)
        G[u].append(v)
        G[v].append(u)
    return G