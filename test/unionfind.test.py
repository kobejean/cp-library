# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from cp_library.io.read_int_fn import read
from cp_library.io.write_fn import write
from cp_library.ds.dsu_cls import DSU

N, Q = read()

dsu = DSU(N)

for _ in range(Q):
    t, u, v = read()
    if t:
        write(int(dsu.same(u, v)))
    else:
        dsu.merge(u, v)

