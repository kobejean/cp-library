# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

def main():
    N, = rd()
    A = rdl(1 << N)
    B = rdl(1 << N)
    wtnl(iand_conv(A, B, N, 998244353))

from cp_library.math.conv.mod.iand_conv_fn import iand_conv
from cp_library.io.fast_io_fn import rd, rdl, wtnl

if __name__ == '__main__':
    main()
