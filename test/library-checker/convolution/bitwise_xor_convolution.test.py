# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution

def main():
    N = rd()
    A = rdl(1 << N)
    B = rdl(1 << N)
    C = ixor_conv(A, B, N, 998244353)
    wtnl(C)

from cp_library.math.conv.mod.ixor_conv_fn import ixor_conv
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

if __name__ == '__main__':
    main()
