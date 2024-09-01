import heapq
from math import inf

def dijkstra(G, N, root) -> list[int]:
    D = [inf for _ in range(N)]
    D[root] = 0
    queue = [(0, root)]
    while queue:
        d, v = heapq.heappop(queue)
        if d > D[v]: continue

        for w, u in G[v]:
            nd = d + w
            if nd < D[u]:
                D[u] = nd
                heapq.heappush(queue, (nd, u))
    return D
