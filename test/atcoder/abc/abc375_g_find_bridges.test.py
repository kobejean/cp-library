# verification-helper: PROBLEM https://atcoder.jp/contests/abc375/tasks/abc375_g

from cp_library.alg.dp.min2_fn import min2
from cp_library.alg.graph.fast.snippets.cut_edges_fn import cut_edges


def main():
    N, M = read(tuple[int, int])
    G = read(GraphWeighted[N,M])
    S = G.dijkstra(0)
    T = G.dijkstra(N-1)
    D = [G.W[e]+min2(S[G.U[e]]+T[G.V[e]], S[G.V[e]]+T[G.U[e]]) for e in range(M)]
    Dmin = S[-1]
    U, V, I = [], [], []
    for i,d in enumerate(D):
        if Dmin == d:
            U.append(G.U[i]); V.append(G.V[i]); I.append(i)

    H = GraphWeighted(N, U, V, I)
    ans = [False]*M
    for i in cut_edges(H): ans[H.Wa[i]] = True
    for i in range(M):
        write("Yes" if ans[i] else "No")

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.fast.graph_weighted_cls import GraphWeighted

if __name__ == "__main__":
    main()