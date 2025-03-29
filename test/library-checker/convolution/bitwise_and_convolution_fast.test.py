# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

def main():
    N = rd()
    A = rdl(1 << N)
    B = rdl(1 << N)
    wtnl(and_conv(A, B, N, 998244353))

from cp_library.math.conv.and_conv_fast_fn import and_conv
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

if __name__ == '__main__':
    main()
