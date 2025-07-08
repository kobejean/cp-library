# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection

def main():
    N, M = read()
    G = read(DiGraph[N,M,0])
    cyc = G.find_cycle_edge_ids()
    if cyc is None:
        write("-1")
    else:
        write(len(cyc))
        write(*cyc, sep='\n')
    
from cp_library.alg.graph.csr.digraph_cls import DiGraph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
