# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path


def main():
    N, M, s, t = read()
    G = read(DiGraphWeighted[N,M,0])
    path, D = shortest_path(G, s, t)
    if path is None:
        write("-1")
    else:
        E = G.E
        X, Y = D[t], len(path)
        write(X, Y)
        for e in path:
            u,v,_ = E[e]
            write(u,v)
    
from cp_library.math.inft_cnst import inft
    
def shortest_path(G, s: int, g: int) -> list[int]:
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

from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.ds.heap.min_heap_cls import MinHeap

if __name__ == '__main__':
    main()
