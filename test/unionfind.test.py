# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from cp_library.io.rint_fn import rint
from cp_library.ds.dsu_cls import DSU

N, Q = rint()

dsu = DSU(N)

for _ in range(Q):
    t, u, v = rint()
    if t:
        print(int(dsu.same(u, v)))
    else:
        dsu.merge(u, v)

