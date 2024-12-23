# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod

def main():
    mint.set_mod(998244353)
    N, M = read()
    A = read(list[int])
    B = read(list[int])
    C = mint.ntt.conv(A, B)
    write(*C)

from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
