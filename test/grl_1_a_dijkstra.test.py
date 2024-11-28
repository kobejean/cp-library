# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A

from cp_library.math.inft_cnst import inft

def main():
    N, M, r = read()
    G = read(DiGraphWeighted[N, M, 0])
    D = dijkstra(G, r)
    print(*('INF' if d == inft else d for d in D), sep='\n')

from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.dijkstra_fn import dijkstra
from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted

if __name__ == '__main__':
    main()