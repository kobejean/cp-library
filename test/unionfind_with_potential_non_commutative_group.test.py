# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group

mod = 998244353

from cp_library.ds.potentialized_dsu import PotentializedDSU

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, Q = rint()

def matmul2(x, y):
    return [
        (y[0] * x[0] + y[1] * x[2]) % mod,
        (y[0] * x[1] + y[1] * x[3]) % mod,
        (y[2] * x[0] + y[3] * x[2]) % mod,
        (y[2] * x[1] + y[3] * x[3]) % mod,
    ]

def matinv2(x) -> list[int]:
    return [x[3], -x[1] % mod, -x[2] % mod, x[0]]

e = [1, 0, 0, 1]
pdsu = PotentializedDSU(matmul2,matinv2,e,N)

for _ in range(Q):
    t, *q = rint()
    if t:
        u, v = q
        ans = pdsu.diff(u, v) if pdsu.same(u, v) else (-1,)
        print(*ans)
    else:
        u, v, *w = q
        print(int(pdsu.consistent(u,v, w)))
        pdsu.merge(u, v, w)
            