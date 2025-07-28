# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence
def main():
    N, = rd()
    A = rdl(N)
    ans = lis(A)
    wtn(len(ans))
    wtnl(ans)

from cp_library.alg.dp.lis_fn import lis
from cp_library.io.fast_io_fn import rd, rdl, wtn, wtnl

main()