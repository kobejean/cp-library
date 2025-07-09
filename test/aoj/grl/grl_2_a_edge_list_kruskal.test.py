# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

def main():
    N, M = read((int,int))
    E = read(EdgeListWeighted[N,M,0])
    MST = E.sub(E.kruskal())
    ans = sum(MST.W)
    write(ans)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.edge.edge_list_weighted_cls import EdgeListWeighted

if __name__ == '__main__':
    main()