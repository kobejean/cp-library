# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_set_power_series

def main():
    N = rd()
    B = rdl(1<<N)
    C = sps_exp(B, 998244353)
    assert sps_ln(C, 998244353) == B
    wtnl(C)

from cp_library.math.sps.mod.sps_exp_fn import sps_exp
from cp_library.math.sps.mod.sps_ln_fn import sps_ln
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

main()