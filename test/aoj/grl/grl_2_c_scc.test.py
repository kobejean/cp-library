# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_C

def main():
    N, M = read()
    G = read(DiGraph[N,M,0])
    sccs = scc_labels(G)

    Q = read(int)
    for _ in range(Q):
        u, v = read()
        write(int(sccs[u]==sccs[v]))

from cp_library.alg.graph.fast.digraph_cls import DiGraph
from cp_library.alg.graph.fast.snippets.scc_labels_fn import scc_labels
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()