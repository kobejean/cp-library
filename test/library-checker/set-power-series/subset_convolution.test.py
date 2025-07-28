# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution

def main():
    mod, n = 998244353, rd()[0]
    A, B = rdl(1<<n), rdl(1<<n)
    C = subset_conv(A, B, n, mod)
    wtnl(C)
    assert subset_deconv(C, B, n, mod) == A

from cp_library.math.conv.mod.subset_conv_fn import subset_conv
from cp_library.math.conv.mod.subset_deconv_fn import subset_deconv
from cp_library.io.fast_io_fn import rd, rdl, wtnl

main()