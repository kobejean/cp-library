import cp_library.alg.graph.__header__

from collections import deque
from typing import overload
from math import inf

@overload
def bfs(G, s: int = 0) -> list[int]: ...
@overload
def bfs(G, s: int, g: int) -> int: ...

def bfs(G, s: int = 0, g: int = None):
    D = [inf for _ in range(G.N)]
    D[s] = 0
    q = deque([s])
    while q:
        nd = D[u := q.popleft()]+1
        if u == g: return D[u]
        for v in G[u]:
            if nd < D[v]:
                D[v] = nd
                q.append(v)
    return D if g is None else inf