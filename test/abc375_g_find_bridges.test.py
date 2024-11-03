# verification-helper: PROBLEM https://atcoder.jp/contests/abc375/tasks/abc375_g

def main():
    N, M = read(tuple[int, int])
    G = read(GraphWeighted[N,M])
    S = G.dijkstra(0)
    T = G.dijkstra(N-1)
    D = [w+min(S[u]+T[v], S[v]+T[u]) for u,v,w in G.E]
    Dmin = S[-1]

    H = GraphWeighted(N, [(*G.E[i], i) for i,d in enumerate(D) if Dmin == d])

    ans = [False]*M
    for e in H.bridges():
        *_,i = H.E[e]
        ans[i] = True

    for i in range(M):
        print("Yes" if ans[i] else "No")

from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.graph_weighted_cls import GraphWeighted

if __name__ == "__main__":
    main()