# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
from math import inf

def main():
    N, M, r = read()
    G = read(DiGraphWeighted[N, M, 0])

    neg_cycle, D = bellman_ford(G, N, r)

    if neg_cycle:
        print("NEGATIVE CYCLE")
    else:
        print(*('INF' if d == inf else d for d in D), sep='\n')

from cp_library.alg.graph.bellman_ford_neg_cyc_check_fn import bellman_ford
from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_specs_fn import read

if __name__ == '__main__':
    main()