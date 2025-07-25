# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_set_power_series

def main():
    N = rd()
    B = rdl(1<<N)
    C = sps_exp_half(B, 998244353)
    wtnl(C)
    # assert sps_ln(C, 998244353) == B

# from cp_library.math.sps.mod.sps_exp_fn import sps_exp
from cp_library.math.sps.mod.sps_ln_fn import sps_ln
from cp_library.math.sps.mod.sps_exp_half_fn import sps_exp_half
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl
# from cp_library.io.write_fn import write
# from cp_library.io.read_fn import read

main()