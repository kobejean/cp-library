import cp_library.alg.graph.__header__

from cp_library.ds.heap.fast_heapq  import heapify, heappop
from cp_library.ds.dsu_cls import DSU

def kruskal(E, N):
    heapify(E)
    dsu = DSU(N)
    MST = []
    need = N-1
    while E and need:
        edge = heappop(E)
        u,v,_ = edge
        if not dsu.same(u,v):
            dsu.merge(u,v)
            MST.append(edge)
            need -= 1
    return MST
