import cp_library.alg.graph.__header__
from cp_library.math.inft_cnst import inft

def bellman_ford(G, N, root) -> list[int]:
    D = [inft]*N
    D[root] = 0
    for _ in range(N-1):
        for u, edges in enumerate(G):
            if D[u] == inft: continue
            for v,w in edges:
                D[v] = min(D[v], D[u] + w)
    return D
