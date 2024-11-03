import cp_library.alg.graph.__header__

from collections import deque
from math import inf

def bfs(G, s = 0) -> list[int]:
    N = len(G)
    D = [inf] * N
    D[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        nd = D[v]+1
        for c in G[v]:
            if nd < D[c]:
                D[c] = nd
                q.append(c)
    return D