# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential

from cp_library.ds.potentialized_dsu_cls import PotentializedDSU
from cp_library.io.read_int_fn import read

mod = 998244353
N, Q = read()

def op(x,y):
    return (x+y)%mod

def inv(x):
    return (-x)%mod

pdsu = PotentializedDSU(op,inv,0,N)

for _ in range(Q):
    t, *q = read()
    if t:
        u, v = q
        ans = pdsu.diff(u, v) if pdsu.same(u, v) else -1
        print(ans)
    else:
        u, v, x = q
        print(int(pdsu.consistent(u,v,x)))
        pdsu.merge(u, v, x)

