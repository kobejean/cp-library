# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A

def main():
    N, M = read()
    G = read(Graph[N,M,0])
    ap = cut_vertices(G)
    ans = [v for v,b in enumerate(ap) if b]
    if ans:
        write(*ans, sep='\n')

from cp_library.alg.graph.csr.snippets.cut_vertices_fn import cut_vertices
from cp_library.alg.graph.csr.graph_cls import Graph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()