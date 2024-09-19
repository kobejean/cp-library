# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
from cp_library.alg.tree.lca_table_iterative_cls import LCATable
from cp_library.io.read_specs_fn import read

N, = read()
T = []
for _ in range(N):
    k, *adj = read()
    T.append(adj)
lca = LCATable(T, 0)
Q, = read()
for _ in range(Q):
    u, v = read()
    print(lca.query(u,v)[0])