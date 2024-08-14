# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

from cp_library.math.matpow import mat_pow
from cp_library.math.mod.modint import mint

mint.mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

def rmint():
    return [mint(int(x)) for x in input().split()]

N, K = rint()
A = [rmint() for _ in range(N)]
B = mat_pow(A, K)

for row in B:
    print(*row)
