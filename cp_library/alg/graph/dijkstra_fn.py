import cp_library.alg.graph.__init__
import heapq
from math import inf

def dijkstra(G, N, root) -> list[int]:
    D = [inf for _ in range(N)]
    D[root] = 0
    q = [(0, root)]
    while q:
        d, v = heapq.heappop(q)
        if d > D[v]: continue

        for w, u in G[v]:
            if (nd := d + w) < D[u]:
                D[u] = nd
                heapq.heappush(q, (nd, u))
    return D
