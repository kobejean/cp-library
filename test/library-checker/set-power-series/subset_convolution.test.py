# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution

def main():
    mod, n = 998244353, rd()
    wtnl(subset_conv(rdl(1<<n), rdl(1<<n), n, mod))

from cp_library.math.conv.mod.subset_conv_fn import subset_conv
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

main()