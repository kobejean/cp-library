# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inv_of_formal_power_series

def main():
    N = read(int)
    mint.set_mod(998244353)
    A = read(list[int])
    B = fps_inv(A)
    write(*B)

from cp_library.math.fps.fps_inv_fn import fps_inv
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
