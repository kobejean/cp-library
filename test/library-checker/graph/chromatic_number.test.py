# verification-helper: PROBLEM https://judge.yosupo.jp/problem/chromatic_number

def main():
    N, M = read()
    G = read(BitGraph[N,M,0])
    write(G.chromatic_number())

from cp_library.alg.graph.bit.bit_graph_cls import BitGraph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
