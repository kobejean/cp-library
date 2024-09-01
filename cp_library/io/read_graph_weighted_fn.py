from cp_library.io.rint_fn import rint

def read_graph(N, M, i0=1):
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v,w = rint(-i0)
        w += i0
        G[u].append((w,v))
        G[v].append((w,u))
    return G