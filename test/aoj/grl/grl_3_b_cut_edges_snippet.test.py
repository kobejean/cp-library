# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_3_B

from cp_library.ds.elist_fn import elist
from cp_library.alg.dp.max2_fn import max2
from cp_library.alg.dp.min2_fn import min2


def main():
    N, M = read()
    G = read(Graph[N,M,0])
    E = elist(M)
    for i in cut_edges(G):
        u, v = min2(G.Ua[i], G.Va[i]), max2(G.Ua[i], G.Va[i])
        E.append((u, v))
    E.sort()
    for u, v in E:
        write(u, v)

from cp_library.alg.graph.csr.graph_cls import Graph
from cp_library.alg.graph.csr.snippets.cut_edges_fn import cut_edges
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()