from math import inf

def bellman_ford(G, N, root) -> list[int]:
    D = [inf]*N
    D[root] = 0
    for _ in range(N-1):
        for u, edges in enumerate(G):
            for w, v in edges:
                D[v] = min(D[v], D[u] + w)
    return D
