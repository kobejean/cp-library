# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B

def main():
    N, M, root = read((0, ...))
    E = read_edges(M, 0)
    MCA = edmonds_branching(E, N, root)
    ans = sum(w for w,u,v in MCA)
    print(ans)

from cp_library.io.read_specs_fn import read
from cp_library.io.read_edges_weighted_fn import read_edges
from cp_library.alg.graph.edmonds_fn import edmonds_branching

if __name__ == '__main__':
    main()