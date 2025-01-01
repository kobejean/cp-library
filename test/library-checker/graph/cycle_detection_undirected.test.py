# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected

def main():
    N, M = read()
    G = read(Graph[N,M,0])
    cyc = G.find_cycle_indices()

    if cyc is None:
        write("-1")
    else:
        write(len(cyc))
        V = [G.Ua[i] for i in cyc]
        E = [G.Ea[i] for i in cyc]
        write(*V)
        write(*E)
    
from cp_library.alg.graph.fast.graph_cls import Graph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
