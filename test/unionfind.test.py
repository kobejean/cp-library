# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from operator import add, neg
from cp_library.ds.potentialized_dsu import PotentializedDSU

mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, Q = rint()

pdsu = PotentializedDSU(add,neg,0,N)

for _ in range(Q):
    t, u, v = rint()
    if t:
        print(int(pdsu.same(u, v)))
    else:
        pdsu.merge(u, v, 0)

