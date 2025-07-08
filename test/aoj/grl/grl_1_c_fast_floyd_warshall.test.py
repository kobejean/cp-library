# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
from math import inf

def main():
    N, M = read((int,int))
    G = read(DiGraphWeighted[N,M,0])
    neg_cycle, D = G.floyd_warshall_neg_cyc_check()

    if neg_cycle:
        write("NEGATIVE CYCLE")
    else:
        for row in D:
            write(*('INF' if d >= inf else d for d in row))

from cp_library.io.legacy.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.csr.digraph_weighted_cls import DiGraphWeighted

if __name__ == '__main__':
    main()