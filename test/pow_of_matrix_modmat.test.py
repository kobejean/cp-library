# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

from cp_library.math.mod.mint_cls import mint
from cp_library.math.mod.modmat_cls import ModMat
from cp_library.io.read_int_fn import read

mint.mod = 998244353

N, K = read()
A = ModMat([read() for _ in range(N)])
B = A**K
print(B)
