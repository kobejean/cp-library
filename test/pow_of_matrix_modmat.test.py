# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

from cp_library.math.mod.mint_cls import mint
from cp_library.math.mod.modmat_cls import ModMat

mint.mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]


N, K = rint()
A = ModMat([rint() for _ in range(N)])
B = A**K
print(B)
