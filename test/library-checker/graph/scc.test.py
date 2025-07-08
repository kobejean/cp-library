# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc

def main():
    N, M = read()
    G = read(DiGraph[N,M,0])
    sccs = G.scc()
    write(len(sccs))
    for scc in sccs:
        write(len(scc), *scc)
    
from cp_library.alg.graph.csr.digraph_cls import DiGraph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
