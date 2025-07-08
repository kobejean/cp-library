# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B

def main():
    N, M, root = read((0, ...))
    E = read(EdgeListWeighted[M,0])
    MCA = edmonds_branching(E, N, root)
    ans = sum(w for *_,w in MCA)
    write(ans)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.graph.edmonds_fn import edmonds_branching
from cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted

if __name__ == '__main__':
    main()