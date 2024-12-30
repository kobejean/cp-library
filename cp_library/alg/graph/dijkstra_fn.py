import cp_library.alg.graph.__header__

from heapq import heappop, heappush
from typing import Union, overload
from cp_library.alg.dp.chmin_fn import chmin
from math import inf

@overload
def dijkstra(G, s: int = 0) -> list[int]: ...
@overload
def dijkstra(G, s: int, g: int) -> int: ...
def dijkstra(G, s = 0, g: Union[int,None] = None):
    N = len(G)
    D = [inf for _ in range(N)]
    D[s] = 0
    q = [(0, s)]
    while q:
        d, v = heappop(q)
        if d > D[v]: continue
        if v == g: return d
        for u, w, *_ in G[v]:
            if chmin(D, u, nd := d + w):
                heappush(q, (nd, u))
    return D if g is None else inf