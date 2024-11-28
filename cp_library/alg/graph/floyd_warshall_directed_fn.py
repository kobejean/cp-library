import cp_library.alg.graph.__header__
from cp_library.math.inft_cnst import inft

def floyd_warshall(G, N) -> list[list[int]]:
    D = [[inft]*N for _ in range(N)]

    for u, edges in enumerate(G):
        D[u][u] = 0
        for v,w in edges:
            D[u][v] = min(D[u][v], w)
    
    for k, Dk in enumerate(D):
        for Di in D:
            for j in range(N):
                Di[j] = min(Di[j], Di[k]+Dk[j])
    return D