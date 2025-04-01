# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc

def main():
    N, M = rd(), rd()
    X = rdl(N)
    U, V = [0]*M, [0]*M
    for e in range(M): U[e], V[e] = rd(), rd()
    W = scc_incremental(N, M, U, V)
    dsu = DSU(N)
    cur = t = 0
    mod = 998244353
    ans = [0]*M
    for e in argsort(W):
        nt = W[e]
        if nt < 0: continue
        x, y = dsu.merge(U[e], V[e], True)
        while t < nt-1: ans[t] = cur; t += 1
        if x != y:
            cur = (cur+X[x]*X[y])%mod
            X[x] = (X[x]+X[y])%mod
    while t < M: ans[t] = cur; t += 1
    wtnl(ans)

from cp_library.alg.iter.argsort_fn import argsort
from cp_library.ds.dsu_cls import DSU
from cp_library.ds.elist_fn import elist
from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

if __name__ == '__main__':
    main()
