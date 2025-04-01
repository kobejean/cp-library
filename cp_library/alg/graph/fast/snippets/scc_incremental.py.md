---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\n\n\ndef scc_incremental(N, M, U, V):\n    La, Ra, Ua, Va, Ea = [0]*N, [0]*N,\
    \ [0]*M, [0]*M, [0]*M\n    E, F = list(range(M)), list(range(M))\n    U, V = U[:],\
    \ V[:]\n    st, buf, sccs, tin, low = [0]*N, elist(N), list(range(N)), [-1]*N,\
    \ [-1]*N\n    W = [-1]*M\n\n    def build_csr(N, E, el, er):\n        u = tot\
    \ = 0\n        while u < N: La[u] = 0; u += 1\n        i = el\n        while i\
    \ < er: La[U[e := E[i]]] += 1; i += 1\n        u = 0\n        while u < N: La[u]\
    \ = Ra[u] = (tot := tot + La[u]); u += 1\n        i = el\n        while i < er:\
    \ La[u] = a = La[u := U[e := E[i]]]-1; Ua[a], Va[a], Ea[a] = u, V[e], e; i +=\
    \ 1\n\n    def scc_labels(N, E, el, em, er, La, Ra, Va):\n        t = cnt = -1;\
    \ i = el\n        while i < em:\n            u = U[E[i]]; i += 1\n           \
    \ if tin[u] < 0:\n                d = 0\n                st[0] = u\n         \
    \       while d >= 0:\n                    if tin[u := st[d]] == -1: tin[u] =\
    \ low[u] = (t:=t+1); buf.append(u)\n                    if (a := La[u]) < Ra[u]:\n\
    \                        La[u] += 1\n                        if (tv := tin[v :=\
    \ Va[a]]) == -1: st[d:=d+1] = v\n                        elif tv < low[u]: low[u]\
    \ = tv\n                    else:\n                        if (d:=d-1) >= 0 and\
    \ low[u] < low[st[d]]: low[st[d]] = low[u]\n                        if low[u]\
    \ == tin[u]:\n                            v, cnt = -1, cnt+1\n               \
    \             while u != v: tin[v := buf.pop()] = N; sccs[v] = cnt\n        i\
    \ = el\n        while i < er:\n            u, v = U[E[i]], V[E[i]]; i += 1\n \
    \           if tin[u] < 0: tin[u], sccs[u] = N, (cnt:=cnt+1)\n            if tin[v]\
    \ < 0: tin[v], sccs[v] = N, (cnt:=cnt+1)\n        i = el\n        while i < er:\
    \ tin[U[E[i]]] = tin[V[E[i]]] = -1; i += 1\n        return cnt+1\n    \n    def\
    \ partition(el, er, tm, end = False):\n        i = em = el\n        while i <\
    \ er:\n            if sccs[U[e := E[i]]] == sccs[V[e]]:\n                W[e],\
    \ F[em] = tm, e; em += 1\n            i += 1\n        if end: return em\n    \
    \    i, fm = el, em\n        while i < er:\n            if (u := sccs[U[e := E[i]]])\
    \ != (v := sccs[V[e]]):\n                U[e], V[e], F[fm] = u, v, e; fm += 1\n\
    \            i += 1\n        return em\n    \n    def div_con(N, el, er, tl, tr):\n\
    \        nonlocal E, F\n        tm, em = (tl+tr) >> 1, el\n        if el == er:\
    \ return\n        while em < er and E[em] < tm: em += 1\n        build_csr(N,\
    \ E, el, em)\n        nN = scc_labels(N, E, el, em, er, La, Ra, Va)\n        em\
    \ = partition(el, er, tm, end := tr-tl==1)\n        if end: return\n        E,\
    \ F = F, E\n        div_con(nN, em, er, tm, tr)\n        div_con(N, el, em, tl,\
    \ tm)\n        E, F = F, E\n    div_con(N, 0, M, 0, M+1)\n    return W\n\n\n\n\
    def elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.graph.__header__\n\
    import cp_library.alg.graph.fast.__header__\nimport cp_library.alg.graph.fast.snippets.__header__\n\
    \ndef scc_incremental(N, M, U, V):\n    La, Ra, Ua, Va, Ea = [0]*N, [0]*N, [0]*M,\
    \ [0]*M, [0]*M\n    E, F = list(range(M)), list(range(M))\n    U, V = U[:], V[:]\n\
    \    st, buf, sccs, tin, low = [0]*N, elist(N), list(range(N)), [-1]*N, [-1]*N\n\
    \    W = [-1]*M\n\n    def build_csr(N, E, el, er):\n        u = tot = 0\n   \
    \     while u < N: La[u] = 0; u += 1\n        i = el\n        while i < er: La[U[e\
    \ := E[i]]] += 1; i += 1\n        u = 0\n        while u < N: La[u] = Ra[u] =\
    \ (tot := tot + La[u]); u += 1\n        i = el\n        while i < er: La[u] =\
    \ a = La[u := U[e := E[i]]]-1; Ua[a], Va[a], Ea[a] = u, V[e], e; i += 1\n\n  \
    \  def scc_labels(N, E, el, em, er, La, Ra, Va):\n        t = cnt = -1; i = el\n\
    \        while i < em:\n            u = U[E[i]]; i += 1\n            if tin[u]\
    \ < 0:\n                d = 0\n                st[0] = u\n                while\
    \ d >= 0:\n                    if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1);\
    \ buf.append(u)\n                    if (a := La[u]) < Ra[u]:\n              \
    \          La[u] += 1\n                        if (tv := tin[v := Va[a]]) == -1:\
    \ st[d:=d+1] = v\n                        elif tv < low[u]: low[u] = tv\n    \
    \                else:\n                        if (d:=d-1) >= 0 and low[u] <\
    \ low[st[d]]: low[st[d]] = low[u]\n                        if low[u] == tin[u]:\n\
    \                            v, cnt = -1, cnt+1\n                            while\
    \ u != v: tin[v := buf.pop()] = N; sccs[v] = cnt\n        i = el\n        while\
    \ i < er:\n            u, v = U[E[i]], V[E[i]]; i += 1\n            if tin[u]\
    \ < 0: tin[u], sccs[u] = N, (cnt:=cnt+1)\n            if tin[v] < 0: tin[v], sccs[v]\
    \ = N, (cnt:=cnt+1)\n        i = el\n        while i < er: tin[U[E[i]]] = tin[V[E[i]]]\
    \ = -1; i += 1\n        return cnt+1\n    \n    def partition(el, er, tm, end\
    \ = False):\n        i = em = el\n        while i < er:\n            if sccs[U[e\
    \ := E[i]]] == sccs[V[e]]:\n                W[e], F[em] = tm, e; em += 1\n   \
    \         i += 1\n        if end: return em\n        i, fm = el, em\n        while\
    \ i < er:\n            if (u := sccs[U[e := E[i]]]) != (v := sccs[V[e]]):\n  \
    \              U[e], V[e], F[fm] = u, v, e; fm += 1\n            i += 1\n    \
    \    return em\n    \n    def div_con(N, el, er, tl, tr):\n        nonlocal E,\
    \ F\n        tm, em = (tl+tr) >> 1, el\n        if el == er: return\n        while\
    \ em < er and E[em] < tm: em += 1\n        build_csr(N, E, el, em)\n        nN\
    \ = scc_labels(N, E, el, em, er, La, Ra, Va)\n        em = partition(el, er, tm,\
    \ end := tr-tl==1)\n        if end: return\n        E, F = F, E\n        div_con(nN,\
    \ em, er, tm, tr)\n        div_con(N, el, em, tl, tm)\n        E, F = F, E\n \
    \   div_con(N, 0, M, 0, M+1)\n    return W\n\nfrom cp_library.ds.elist_fn import\
    \ elist"
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/fast/snippets/scc_incremental.py
  requiredBy: []
  timestamp: '2025-04-02 01:29:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/fast/snippets/scc_incremental.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/fast/snippets/scc_incremental.py
- /library/cp_library/alg/graph/fast/snippets/scc_incremental.py.html
title: cp_library/alg/graph/fast/snippets/scc_incremental.py
---
