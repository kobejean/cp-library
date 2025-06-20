# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

def main():
    N, M = read([int])
    E = read(EdgeListWeighted[M,0])
    MST = kruskal(E, N)
    ans = sum(w for *_,w in MST)
    write(ans)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.kruskal_heap_fn import kruskal
from cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted

if __name__ == '__main__':
    main()