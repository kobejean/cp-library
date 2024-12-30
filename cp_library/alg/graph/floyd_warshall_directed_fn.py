import cp_library.alg.graph.__header__
from math import inf

def floyd_warshall(G, N) -> list[list[int]]:
    D = [[inf]*N for _ in range(N)]

    for u, edges in enumerate(G):
        D[u][u] = 0
        for v,w in edges:
            D[u][v] = min(D[u][v], w)
    
    for k, Dk in enumerate(D):
        for Di in D:
            if Di[k] == inf: continue
            for j in range(N):
                if Dk[j] == inf: continue
                Di[j] = min(Di[j], Di[k]+Dk[j])
    return D