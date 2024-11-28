# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path

def main():
    N, M, s, t = read(tuple[int, ...])
    G = read(DiGraphWeighted[N,M,0])
    path = G.shortest_path(s, t)
    if path is None:
        write("-1")
    else:
        X, Y = G.D[t], len(path)-1
        write(X, Y)
        for i in range(Y):
            write(path[i],path[i+1])
    
from cp_library.alg.graph.fast.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
