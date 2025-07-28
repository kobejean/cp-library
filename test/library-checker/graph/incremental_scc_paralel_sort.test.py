# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc

def main():
    N, M = rd()
    X, U, V = rdl(N), [0]*M, [0]*M
    for e in range(M): U[e], V[e] = rd()
    W, dsu, ans, mod = scc_incremental(N, M, U, V), [*range(N)], [0]*M, 998244353; cur = t = 0
    isort_parallel(W, U, V)
    for e in range(M):
        u, v, w = U[e], V[e], W[e]
        while t < w: ans[t] = cur; t += 1
        while u != dsu[u]: dsu[u] = u = dsu[dsu[u]]
        while v != dsu[v]: dsu[v] = v = dsu[dsu[v]]
        if u != v: dsu[v], cur, X[u] = u, (cur+X[u]*X[v])%mod, (X[u]+X[v])%mod
    while t < M: ans[t] = cur; t += 1
    wtnl(ans)

from cp_library.alg.graph.csr.snippets.scc_incremental_fn import scc_incremental
from cp_library.alg.iter.sort.isort_parallel_fn import isort_parallel
from cp_library.io.fast_io_fn import rd, rdl, wtnl

if __name__ == '__main__':
    main()
