import cp_library.alg.graph.__header__
import heapq
from math import inf

def dijkstra(G, N, root) -> list[int]:
    D = [inf for _ in range(N)]
    D[root] = 0
    q = [(0, root)]
    while q:
        d, u = heapq.heappop(q)
        if d > D[u]: continue

        for v,w in G[u]:
            if (nd := d + w) < D[v]:
                D[v] = nd
                heapq.heappush(q, (nd, v))
    return D
