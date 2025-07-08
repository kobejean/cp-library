# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
from math import inf

def main():
    N, M, r = read()
    G = read(DiGraphWeighted[N, M, 0])

    neg_cycle, D = G.bellman_ford_neg_cyc_check(r)

    if neg_cycle:
        write("NEGATIVE CYCLE")
    else:
        write(*('INF' if d == inf else d for d in D), sep='\n')

from cp_library.alg.graph.csr.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()