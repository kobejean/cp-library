# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path


def main():
    N, M, s, t = read()
    G = read(DiGraphWeighted[N,M,0])
    path, D = shortest_path(G, s, t)
    if path is None:
        write("-1")
    else:
        X, Y = D[t], len(path)
        write(X, Y)
        for e in path:
            u,v = G.U[e], G.V[e]
            write(u,v)
    
from math import inf
    
def shortest_path(G, s: int, g: int) -> list[int]:
    D = [inf] * G.N
    D[s] = 0
    if s == g:
        return [], D
    par = [-1] * G.N
    par_edge = [-1] * G.N
    heap = MinHeap()
    heap.push((0, s))

    while heap:
        d, u = heap.pop()
        if d > D[u]: continue
        if u == g: break
        i, r = G.La[u]-1, G.Ra[u]
        while (i:=i+1) < r:
            if (nd := d + G.Wa[i]) < D[v := G.Va[i]]:
                D[v] = nd
                par[v] = u
                par_edge[v] = G.Ea[i]
                heap.push((nd, v))
    
    if D[g] == inf:
        return None, D
        
    path = []
    current = g
    while current != s:
        path.append(par_edge[current])
        current = par[current]
        
    return path[::-1], D

from cp_library.alg.graph.fast.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.ds.heap.min_heap_cls import MinHeap

if __name__ == '__main__':
    main()
