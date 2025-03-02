# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

def main():
    mint.set_mod(998244353)
    N, K = read()
    A = ModMat([read() for _ in range(N)])
    B = A**K
    write(B)

from cp_library.math.mod.mint_cls import mint
from cp_library.math.mat.mod.modmat_cls import ModMat
from cp_library.io.read_int_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
