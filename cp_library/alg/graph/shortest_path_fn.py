import cp_library.alg.graph.__header__
from cp_library.math.inft_cnst import inft
from cp_library.ds.heap.min_heap_cls import MinHeap

def shortest_path(G, s: int, g: int) -> tuple[list[int]|None,list[int]]:
    D = [inft] * G.N
    D[s] = 0
    if s == g:
        return [], D
    par = [-1] * G.N
    par_edge = [-1] * G.N
    Eid = G.edge_ids()
    heap = MinHeap()
    heap.push((0, s))

    while heap:
        d, v = heap.pop()
        if d > D[v]: continue
        if v == g: break
    
        for i,(u, w, *_) in enumerate(G[v]):
            if (nd := d + w) < D[u]:
                D[u] = nd
                par[u] = v
                par_edge[u] = Eid[v][i]
                heap.push((nd, u))
    
    if D[g] == inft:
        return None, D
        
    path = []
    current = g
    while current != s:
        path.append(par_edge[current])
        current = par[current]
        
    return path[::-1], D


