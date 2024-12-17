# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path

def main():
    N, M, s, t = read()
    G = read(DiGraphWeighted[N,M,0])
    path, D = G.shortest_path(s, t, True)
    if path is None:
        write("-1")
    else:
        E = G.E
        X, Y = D[t], len(path)
        write(X, Y)
        for e in path:
            u,v,_ = E[e]
            write(u,v)
    
from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
