# verification-helper: PROBLEM https://judge.yosupo.jp/problem/power_projection_of_set_power_series

def main():
    N, M = rd(), rd()
    A = rdl(1<<N)
    W = rdl(1<<N)
    ans = sps_pow_proj_poly(W, A, M, 998244353)
    wtnl(ans)

from cp_library.math.sps.mod.sps_pow_proj_poly_fn import sps_pow_proj_poly
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

main()