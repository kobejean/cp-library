# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
from cp_library.math.inft_cnst import inft

def main():
    N, M, r = read()
    G = read(DiGraphWeighted[N, M, 0])

    D = G.bellman_ford(r)
    neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for v,w in edges if D[u] != inft)

    if neg_cycle:
        write("NEGATIVE CYCLE")
    else:
        write(*('INF' if d == inft else d for d in D), sep='\n')

from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()