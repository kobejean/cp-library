# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
from cp_library.math.inft_cnst import inft

def main():
    N, M, r = read()
    G = read(DiGraphWeighted[N, M, 0])

    D = G.bellman_ford(r)
    neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for v,w in edges)

    if neg_cycle:
        print("NEGATIVE CYCLE")
    else:
        print(*('INF' if d == inft else d for d in D), sep='\n')

from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_specs_fn import read

if __name__ == '__main__':
    main()