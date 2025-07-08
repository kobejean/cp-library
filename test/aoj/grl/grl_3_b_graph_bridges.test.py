# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_3_B

def main():
    N, M = read()
    G = read(Graph[N,M,0])
    E = [sort2(G.Ua[i], G.Va[i]) for i in cut_edges(G)]; E.sort()
    for s, t in E: write(s, t)

from cp_library.alg.graph.csr.graph_cls import Graph
from cp_library.alg.dp.sort2_fn import sort2
from cp_library.alg.graph.csr.snippets.cut_edges_fn import cut_edges
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()