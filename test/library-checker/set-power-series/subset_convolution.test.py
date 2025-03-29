# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution

def main():
    mod = 998244353
    n = rd()
    a = rdl(1 << n)
    b = rdl(1 << n)
    wtnl(subset_conv(a, b, n, mod))

from cp_library.math.conv.mod.subset_conv_fn import subset_conv
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

main()