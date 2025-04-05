import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
import cp_library.alg.graph.fast.snippets.__header__

def scc_incremental(N, M, U, V):
    U, V, W, La, Ra, Va = U[:], V[:], [M]*M, [0]*N, [0]*N, [0]*M
    E, F, sccs, st, buf, tin, low = [*range(M)], [*range(M)], [0]*N, [0]*N, [0]*N, [-1]*N, [-1]*N

    def build_csr(N, E, el, er):
        tot = 0
        for u in range(N): La[u], tin[u] = 0, -1
        i = el
        while i < er: La[U[e := E[i]]] += 1; i += 1
        for u in range(N): La[u] = Ra[u] = (tot := tot + La[u])
        i = el
        while i < er: La[u] = a = La[u := U[e := E[i]]]-1; Va[a] = V[e]; i += 1

    def scc_labels(N, E, el, em, er, La, Ra, Va):
        t = cnt = -1; i = el
        while i < em:
            u = U[E[i]]; i += 1
            if tin[u] < 0:
                st[0] = u; d = b = 0
                while d >= 0:
                    if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1); buf[b] = u; b += 1
                    if La[u] < Ra[u]:
                        if (tv := tin[Va[La[u]]])== -1: st[d:=d+1] = Va[La[u]]
                        elif tv < low[u]: low[u] = tv
                        La[u] += 1
                    else:
                        if (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]
                        if low[u] == tin[u]:
                            v, cnt = -1, cnt+1
                            while u != v: tin[v := buf[b:=b-1]], sccs[buf[b]] = N, cnt
        while i < er:
            u, v = U[E[i]], V[E[i]]; i += 1
            if tin[u] < 0: tin[u], sccs[u] = N, (cnt:=cnt+1)
            if tin[v] < 0: tin[v], sccs[v] = N, (cnt:=cnt+1)
        return cnt+1
    
    def partition(el, er, tm):
        i = em = el
        while i < er:
            if sccs[U[e := E[i]]] == sccs[V[e]]: W[e], F[em] = tm, e; em += 1
            i += 1
        i, fm = el, em
        while i < er:
            if (u := sccs[U[e := E[i]]]) != (v := sccs[V[e]]): U[e], V[e], F[fm] = u, v, e; fm += 1
            i += 1
        return em
    
    def div_con(N, el, er, tl, tr):
        nonlocal E, F
        if el == er: return
        tm, em = (tl+tr) >> 1, el
        while em < er and E[em] <= tm: em += 1
        build_csr(N, E, el, em)
        nN = scc_labels(N, E, el, em, er, La, Ra, Va)
        em = partition(el, er, tm)
        if tr-tl==1: return
        E, F = F, E
        div_con(nN, em, er, tm, tr)
        div_con(N, el, em, tl, tm)
        E, F = F, E
    div_con(N, 0, M, -1, M)
    return W
