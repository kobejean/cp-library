# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst

def main():
    N, M, S = read()
    E = read(EdgeListWeighted[N, M, 0])
    I = E.edmond(S)
    if I is None:
        write(-1)
    else:
        X = 0; P = [0]*N; P[S] = S
        for e in I: X += E.W[e]; P[E.V[e]] = E.U[e]
        write(X, *P)

from cp_library.alg.graph.edge.edge_list_weighted_cls import EdgeListWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
if __name__ == '__main__':
    main()