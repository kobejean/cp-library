# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

def main():
    N, M = read((int,int))
    E = read(EdgeListWeighted[M,0])
    MST = kruskal(E, N)
    ans = sum(w for w,u,v in MST)
    print(ans)

from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted
from cp_library.alg.graph.kruskal_sort_fn import kruskal

if __name__ == '__main__':
    main()