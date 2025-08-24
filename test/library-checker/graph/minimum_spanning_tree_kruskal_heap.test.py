# verification-helper: PROBLEM https://judge.yosupo.jp/problem/minimum_spanning_tree

def main():
    N, M = read(tuple[int, ...])
    G = read(GraphWeighted[N,M,0])
    W = G.W
    E = kruskal_heap(G)
    X = sum([W[e] for e in E])
    write(X)
    write(*E)
    
from cp_library.ds.dsu_cls import DSU
from cp_library.ds.heap.priority_queue_cls import PriorityQueue
from cp_library.alg.graph.csr.graph_weighted_cls import GraphWeighted

def kruskal_heap(G):
    N, M, U, V, W = G.N, G.M, G.U, G.V, G.W 
    que, dsu, MST = PriorityQueue(M, list(range(M)), W), DSU(N), [0]*(need := N-1)
    while que and need:
        _, e = que.pop()
        u, v = dsu.merge(U[e],V[e])
        if u != v:
            MST[need := need-1] = e
    return None if need else MST
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
