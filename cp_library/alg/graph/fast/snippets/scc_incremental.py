import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
import cp_library.alg.graph.fast.snippets.__header__

def scc_incremental(N, M, U, V):
    La, Ra, Ua, Va, Ea = [0]*N, [0]*N, [0]*M, [0]*M, [0]*M
    E, F = list(range(M)), list(range(M))
    U, V = U[:], V[:]
    st, buf, sccs, tin, low = [0]*N, elist(N), list(range(N)), [-1]*N, [-1]*N
    W = [-1]*M

    def build_csr(N, E, el, er):
        u = tot = 0
        while u < N: La[u] = 0; u += 1
        i = el
        while i < er: La[U[e := E[i]]] += 1; i += 1
        u = 0
        while u < N: La[u] = Ra[u] = (tot := tot + La[u]); u += 1
        i = el
        while i < er: La[u] = a = La[u := U[e := E[i]]]-1; Ua[a], Va[a], Ea[a] = u, V[e], e; i += 1

    def scc_labels(N, E, el, em, er, La, Ra, Va):
        t = cnt = -1; i = el
        while i < em:
            u = U[E[i]]; i += 1
            if tin[u] < 0:
                d = 0
                st[0] = u
                while d >= 0:
                    if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1); buf.append(u)
                    if (a := La[u]) < Ra[u]:
                        La[u] += 1
                        if (tv := tin[v := Va[a]]) == -1: st[d:=d+1] = v
                        elif tv < low[u]: low[u] = tv
                    else:
                        if (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]
                        if low[u] == tin[u]:
                            v, cnt = -1, cnt+1
                            while u != v: tin[v := buf.pop()] = N; sccs[v] = cnt
        i = el
        while i < er:
            u, v = U[E[i]], V[E[i]]; i += 1
            if tin[u] < 0: tin[u], sccs[u] = N, (cnt:=cnt+1)
            if tin[v] < 0: tin[v], sccs[v] = N, (cnt:=cnt+1)
        i = el
        while i < er: tin[U[E[i]]] = tin[V[E[i]]] = -1; i += 1
        return cnt+1
    
    def partition(el, er, tm, end = False):
        i = em = el
        while i < er:
            if sccs[U[e := E[i]]] == sccs[V[e]]:
                W[e], F[em] = tm, e; em += 1
            i += 1
        if end: return em
        i, fm = el, em
        while i < er:
            if (u := sccs[U[e := E[i]]]) != (v := sccs[V[e]]):
                U[e], V[e], F[fm] = u, v, e; fm += 1
            i += 1
        return em
    
    def div_con(N, el, er, tl, tr):
        nonlocal E, F
        tm, em = (tl+tr) >> 1, el
        if el == er: return
        while em < er and E[em] < tm: em += 1
        build_csr(N, E, el, em)
        nN = scc_labels(N, E, el, em, er, La, Ra, Va)
        em = partition(el, er, tm, end := tr-tl==1)
        if end: return
        E, F = F, E
        div_con(nN, em, er, tm, tr)
        div_con(N, el, em, tl, tm)
        E, F = F, E
    div_con(N, 0, M, 0, M+1)
    return W

from cp_library.ds.elist_fn import elist