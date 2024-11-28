# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path

def main():
    N, M, s, t = read()
    G = read(DiGraphWeighted[N,M,0])
    path, D = G.shortest_path(s, t, True)
    if path is None:
        print("-1")
    else:
        E = G.E
        X, Y = D[t], len(path)
        print(X, Y)
        for e in path:
            u,v,_ = E[e]
            print(u,v)
    
from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted
from cp_library.io.read_specs_fn import read

if __name__ == '__main__':
    main()
