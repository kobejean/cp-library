# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
from cp_library.alg.tree.lca_table_iterative_cls import LCATable

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, = rint()
T = []
for _ in range(N):
    k, *adj = rint()
    T.append(adj)
lca = LCATable(T, 0)
Q, = rint()
for _ in range(Q):
    u, v = rint()
    print(lca.query(u,v)[0])