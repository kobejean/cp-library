# verification-helper: PROBLEM https://judge.yosupo.jp/problem/minimum_spanning_tree

def main():
    N, M = read(tuple[int, ...])
    G = read(GraphWeighted[N,M,0])
    W = G.W
    E = G.kruskal_heap()
    X = sum([W[e] for e in E])
    write(X)
    write(*E)
    
from cp_library.alg.graph.fast.graph_weighted_cls import GraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
