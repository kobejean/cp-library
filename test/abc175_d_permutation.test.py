# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d


from cp_library.math.inft_cnst import inft


def main():
    N, K = read(tuple[int, ...])
    P = read(Permutation[N])
    C = read(list[int, N])

    ans = -inft
    for cyc in P.cycles():
        L = len(cyc)
        A = [C[u] for u in cyc]
        loop = sum(A)
        A = presum(A*3)
        m, k = divmod(K, L)
        if m:
            k += L
            m -= 1
        rem = max(A[i+j+1] - A[i] for i in range(L) for j in range(k))
        cost = max(m*loop + rem, rem)
        ans = max(ans, cost)

    write(ans)
    
from cp_library.alg.iter.presum_fn import presum
from cp_library.alg.graph.permutation_cls import Permutation
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()