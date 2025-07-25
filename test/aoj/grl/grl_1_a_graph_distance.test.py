# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A

from math import inf

def main():
    N, M, r = read(int, int, int)
    G = read(DiGraphWeighted[N, M, 0])
    D = G.distance(r)
    write(*('INF' if d == inf else d for d in D), sep='\n')

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.csr.digraph_weighted_cls import DiGraphWeighted

if __name__ == '__main__':
    main()