# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

from cp_library.math.mod.matpow import mat_pow

mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, K = rint()
A = [rint() for _ in range(N)]
B = mat_pow(A, K, mod)

for row in B:
    print(*row)
