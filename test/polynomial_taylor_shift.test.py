# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_taylor_shift

def main():
    N, c = read()
    mint.set_mod(998244353)
    modcomb.precomp(N)
    A = read(list[int])
    B = tayler_shift(A, c)
    write(*B)

from cp_library.math.table.modcomb_cls import modcomb
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.fps.tayler_shift_fn import tayler_shift
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
