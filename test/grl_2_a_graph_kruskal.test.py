# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A



def main():
    N, M = read()
    G = read(GraphWeighted[N,M,0])
    MST = G.kruskal()
    ans = sum(w for *_,w in MST)
    print(ans)

from cp_library.io.legacy.read_specs_fn import read
from cp_library.alg.graph.graph_weighted_cls import GraphWeighted

if __name__ == '__main__':
    main()