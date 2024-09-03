from heapq import heapify, heappop
from cp_library.ds.dsu_cls import DSU

def kruskal(E, N):
    heapify(E)
    dsu = DSU(N)
    MST = []
    need = N-1
    while E and need > 0:
        edge = heappop(E)
        _,u,v = edge
        if not dsu.same(u,v):
            dsu.merge(u,v)
            MST.append(edge)
            need -= 1
    return MST
