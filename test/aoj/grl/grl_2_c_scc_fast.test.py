# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_C

def strongly_connected_components(N, M, La, Ra, Va):
    st, buf, sccs, tin, low, t, d, id = [0]*N, elist(N), [-1]*N, [-1]*N, [N]*N, -1, -1, -1
    for u in range(N):
        if tin[u] >= 0: continue
        st[d:=0] = u
        while d >= 0:
            if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1); buf.append(u)
            if (a := La[u]) < Ra[u]:
                La[u] += 1
                if (tv := tin[v := Va[a]]) == -1: st[d:=d+1] = v
                elif tv < low[u]: low[u] = tv
            else:
                if (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]
                if low[u] == tin[u]:
                    v, id = -1, id+1
                    while u != v: tin[v := buf.pop()] = N; sccs[v] = id
    return sccs

def main():
    N, M, La, Ra, Va = read_csr_graph()
    sccs = strongly_connected_components(N, M, La, Ra, Va)
    Q = rd()
    for _ in range(Q):
        u, v = rd(), rd()
        wtn(int(sccs[u]==sccs[v]))

from cp_library.ds.elist_fn import elist

def read_csr_graph():
    La, Ra, U, V, Va, t = [0]*(N:=rd()), [0]*N, [0]*(M:=rd()), [0]*M, [0]*M, 0
    for e in range(M): La[u := rd()] += 1; U[e], V[e] = u, rd()
    for u, deg in enumerate(La): La[u] = Ra[u] = (t := t + deg)
    for e, u in enumerate(U): La[u] -= 1; Va[La[u]] = V[e]
    return N, M, La, Ra, Va

from cp_library.io.fast.fast_io_fn import rd, wt, wtn, fastio

if __name__ == '__main__':
    main()