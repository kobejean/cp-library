# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_composite_set_power_series

def main():
    M, N = rd(), rd()
    A = rdl(M)
    B = rdl(1<<N)
    C = sps_composite(A, B, 998244353)
    wtnl(C)

from cp_library.math.sps.mod.sps_composite_fn import sps_composite
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

main()