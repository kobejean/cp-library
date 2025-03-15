# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components
def main():
    N, M = read()
    G = read(Graph[N,M,0])
    bccs = biconnected_components(G)
    write(len(bccs))
    for bcc in bccs:
        write(len(bcc), *bcc)
    
from cp_library.alg.graph.fast.graph_cls import Graph
from cp_library.alg.graph.fast.snippets.biconnected_components_vertices_fn import biconnected_components
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
