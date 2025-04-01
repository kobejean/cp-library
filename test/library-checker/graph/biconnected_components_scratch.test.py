# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components

def main():
    N, M, La, Ra, Va = read_csr_graph()
    bccs, L = biconnected_components(N, M, La, Ra, Va)
    fast_write_cc(bccs, L)

from cp_library.alg.dp.chmin_fn import chmin

def read_csr_graph():
    La, Ra, U, V, Va, t = [0]*(N:=rd()), [0]*N, [0]*(M:=rd()), [0]*M, [0]*(M<<1), 0
    for e in range(M): La[u := rd()] += 1; La[v := rd()] += u!=v; U[e], V[e] = u, v
    for u, deg in enumerate(La): La[u] = Ra[u] = (t := t + deg)
    for e, u in enumerate(U): La[u] -= 1; La[v := V[e]] -= u!=v; Va[La[u]], Va[La[v]] = v, u
    return N, M, La, Ra, Va

def biconnected_components(N, M, La, Ra, Va):
    st, buf, bccs, L, par, tin, low, t, d = [0]*N, elist(N), elist(N), elist(N), [-1]*N, [-1]*N, [-1]*N, -1, -1
    for u in range(N):
        if par[u] >= 0: continue
        if La[u] == Ra[u]: L.append(len(bccs)); bccs.append(u); continue
        par[u] = N; st[d:=0] = u
        while d >= 0:
            if tin[u := st[d]] == -1: tin[u] = low[u] = (t := t+1)
            if (a := La[u]) < Ra[u]:
                La[u] += 1
                if par[v := Va[a]] == -1: par[v], st[d := d+1] = u, v; buf.append(v)
                elif par[u] != v: chmin(low, u, tin[v])
            elif (d := d-1) >= 0 and not chmin(low, p := st[d], low[u]) and low[u] >= tin[p]:
                L.append(len(bccs)); bccs.append(p); v = -1
                while u != v: bccs.append(v := buf.pop())
    return bccs, L

from cp_library.ds.elist_fn import elist
from cp_library.io.fast.fast_io_fn import rd, wt, wtn, fastio

def fast_write_cc(A, L):
    r = len(A); wtn(len(L))
    while L:
        l = L.pop(); wt(r-l)
        while l < r: r -= 1; fastio.sb.append(' '); wt(A[r])
        fastio.sb.append('\n')

if __name__ == '__main__':
    main()
