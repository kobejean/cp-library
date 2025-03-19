# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/0439
from cp_library.ds.parallel_cls import Parallel
from cp_library.alg.dp.min2_fn import min2
from cp_library.alg.tree.fast.aux_tree_weighted_cls import AuxTreeWeighted

def main():
    N = read(int)
    C = read(list[-1, N])
    U, V = read(Parallel[N-1,2,-1])
    W = [1]*(N-1)
    T = AuxTreeWeighted(N, U, V, W)

    def edge(s, i, p, u, c):
        return T.Wa[i] if C[u] == c else s+T.Wa[i]
    
    ans = T.rerooting_dp(C, N, min2, edge)
    write(*ans, sep='\n')

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()