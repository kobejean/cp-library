# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

from cp_library.io.read_int_fn import read

mod = 998244353


N, K = read()
if N < 10:
    from cp_library.math.mat_pow_fn import mat_pow
    from cp_library.math.mod.mint_cls import mint
    mint.mod = 998244353

    def rmint():
        return [mint(int(x)) for x in input().split()]

    A = [rmint() for _ in range(N)]
    B = mat_pow(A, K)

else:
    from cp_library.math.mod.mat_pow_fn import mat_pow

    A = [read() for _ in range(N)]
    B = mat_pow(A, K, mod)

for row in B:
    print(*row)
