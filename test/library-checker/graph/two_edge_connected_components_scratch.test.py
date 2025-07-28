# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components

def main():
    N, M = rd()
    La, Ra, Va, Ea = read_csr_graph(N, M)
    e2ccs, L = two_edge_connected_components(N, M, La, Ra, Va, Ea)
    fast_write_cc(e2ccs, L)

from cp_library.alg.dp.chmin_fn import chmin

def read_csr_graph(N, M):
    U, V, La, Ra, Va, Ea, t = [0]*M, [0]*M, [0]*N, [0]*N, [0]*(M << 1), [-1]*(M << 1), 0
    for e in range(M): U[e], V[e] = rd(); La[U[e]] += 1; La[V[e]] += U[e]!=V[e]
    for u in range(N): La[u] = Ra[u] = (t := t + La[u])
    for e in range(M): La[u := U[e]] -= 1; La[v := V[e]] -= u!=v; Va[La[u]], Va[La[v]] = v, u; Ea[La[u]] = Ea[La[v]] = e
    return La, Ra, Va, Ea

def two_edge_connected_components(N, M, La, Ra, Va, Ea):
    st, buf, e2ccs, L, Ein, tin, low, t, d = [0]*N, elist(N), elist(N), elist(N), [-1]*N, [-1]*N, [-1]*N, -1, -1
    for u in range(N):
        if Ein[u] >= 0: continue
        Ein[u] = M; st[d:=0] = u
        while d >= 0:
            if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1); buf.append(u)
            if (a := La[u]) < Ra[u]:
                La[u] += 1
                if Ein[v := Va[a]] == -1: Ein[v] = Ea[a]; st[d:=d+1] = v
                elif Ea[a] != Ein[u]: chmin(low, u, tin[v])
            elif (d:=d-1) >= 0 and not chmin(low, p := st[d], low[u]) and low[u] > tin[p]:
                L.append(len(e2ccs)); v = -1
                while u != v: e2ccs.append(v := buf.pop())
        L.append(len(e2ccs)); e2ccs.extend(buf); buf.clear()
    return e2ccs, L

from cp_library.ds.list.elist_fn import elist
from cp_library.io.fast_io_fn import rd, wt, wtn

def fast_write_cc(A, L):
    r = len(A); wtn(len(L))
    while L:
        l = L.pop(); wt(str(r-l))
        while l < r: r -= 1; wt(' '); wt(str(A[r]))
        wt('\n')

if __name__ == '__main__':
    main()
