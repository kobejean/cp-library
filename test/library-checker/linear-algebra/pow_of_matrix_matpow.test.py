# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix


def main():
    mod = 998244353
    N, K = read()
    if N < 10:
        from cp_library.math.linalg.mat.mat_pow_fn import mat_pow
        from cp_library.math.mod.mint_cls import mint
        mint.set_mod(998244353)

        A = [read(mint) for _ in range(N)]
        B = mat_pow(A, K)
    else:
        from cp_library.math.linalg.mat.mod.mat_pow_fn import mat_pow

        A = [read() for _ in range(N)]
        B = mat_pow(A, K, mod)

    for row in B:
        write(*row)

from cp_library.io.read_func_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()