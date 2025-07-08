# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components

def main():
    N, M = read()
    G = read(Graph[N,M,0])
    e2ccs = two_edge_connected_components(G)
    write(len(e2ccs))
    for e2cc in e2ccs:
        write(len(e2cc), *e2cc)
    
from cp_library.alg.graph.csr.graph_cls import Graph
from cp_library.alg.graph.csr.snippets.two_edge_connected_components_fn import two_edge_connected_components
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
