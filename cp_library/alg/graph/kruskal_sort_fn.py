import cp_library.alg.graph.__header__
from cp_library.ds.dsu_cls import DSU

def kruskal(E, N):
    E.sort(reverse=True)
    dsu = DSU(N)
    MST = []
    need = N-1
    while E and need > 0:
        edge = E.pop()
        u,v,_ = edge
        if not dsu.same(u,v):
            dsu.merge(u,v)
            MST.append(edge)
            need -= 1
    return MST