# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
from math import inf

def main():
    N, M = read((int,int))
    G = read(DiGraphWeighted[N,M,0])
    neg_cycle, D = floyd_warshall(G, N)

    if neg_cycle:
        write("NEGATIVE CYCLE")
    else:
        for row in D:
            write(*('INF' if d == inf else d for d in row))

from cp_library.io.legacy.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.alg.graph.floyd_warshall_check_neg_cycle_fn import floyd_warshall

if __name__ == '__main__':
    main()