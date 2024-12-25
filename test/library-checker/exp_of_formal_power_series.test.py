# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_formal_power_series

def main():
    N = read(int)
    mint.set_mod(998244353)
    A = read(list[int])
    B = fps_exp(A)
    write(*B)

from cp_library.math.fps.fps_exp_fn import fps_exp
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
