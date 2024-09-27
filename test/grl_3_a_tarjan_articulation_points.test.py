# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A

def main():
    N, M = read()
    G = read(Graph[N,M,0])
    ans = sorted(tarjan_articulation_points(G, N))
    if ans:
        print(*ans, sep='\n')

from cp_library.alg.graph.tarjan_articulation_points_fn import tarjan_articulation_points
from cp_library.alg.graph.graph_cls import Graph
from cp_library.io.read_specs_fn import read

if __name__ == '__main__':
    main()