import cp_library.alg.graph.__header__

from collections import deque
from math import inf

def bfs(G, s = 0) -> list[int]:
    N = len(G)
    D = [inf for _ in range(N)]
    D[s] = 0
    q = deque([s])
    while q:
        nd = D[u := q.popleft()]+1
        for v in G[u]:
            if nd < D[v]:
                D[v] = nd
                q.append(v)
    return D