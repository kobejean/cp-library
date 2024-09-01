from cp_library.ds.dsu_cls import DSU

def kruskal(N, M, E):
    E.sort(reverse=True)
    dsu = DSU(N)
    MST = []
    need = N-1
    while E and need > 0:
        edge = E.pop()
        _,u,v = edge
        if not dsu.same(u,v):
            dsu.merge(u,v)
            MST.append(edge)
            need -= 1
    return MST