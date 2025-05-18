---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/incremental_scc.test.py
    title: test/library-checker/graph/incremental_scc.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/incremental_scc_paralel_sort.test.py
    title: test/library-checker/graph/incremental_scc_paralel_sort.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\n\n\ndef scc_incremental(N, M, U, V):\n    U, V, W, La, Ra, Va = U[:], V[:],\
    \ [M]*M, [0]*N, [0]*N, [0]*M\n    E, F, sccs, st, buf, tin, low = [*range(M)],\
    \ [*range(M)], [0]*N, [0]*N, [0]*N, [-1]*N, [-1]*N\n\n    def build_csr(N, E,\
    \ el, er):\n        tot = 0\n        for u in range(N): La[u], tin[u] = 0, -1\n\
    \        i = el\n        while i < er: La[U[e := E[i]]] += 1; i += 1\n       \
    \ for u in range(N): La[u] = Ra[u] = (tot := tot + La[u])\n        i = el\n  \
    \      while i < er: La[u] = a = La[u := U[e := E[i]]]-1; Va[a] = V[e]; i += 1\n\
    \n    def scc_labels(N, E, el, em, er, La, Ra, Va):\n        t = cnt = -1; i =\
    \ el\n        while i < em:\n            u = U[E[i]]; i += 1\n            if tin[u]\
    \ < 0:\n                st[0] = u; d = b = 0\n                while d >= 0:\n\
    \                    if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1); buf[b]\
    \ = u; b += 1\n                    if La[u] < Ra[u]:\n                       \
    \ if (tv := tin[Va[La[u]]])== -1: st[d:=d+1] = Va[La[u]]\n                   \
    \     elif tv < low[u]: low[u] = tv\n                        La[u] += 1\n    \
    \                else:\n                        if (d:=d-1) >= 0 and low[u] <\
    \ low[st[d]]: low[st[d]] = low[u]\n                        if low[u] == tin[u]:\n\
    \                            v, cnt = -1, cnt+1\n                            while\
    \ u != v: tin[v := buf[b:=b-1]], sccs[buf[b]] = N, cnt\n        while i < er:\n\
    \            u, v = U[E[i]], V[E[i]]; i += 1\n            if tin[u] < 0: tin[u],\
    \ sccs[u] = N, (cnt:=cnt+1)\n            if tin[v] < 0: tin[v], sccs[v] = N, (cnt:=cnt+1)\n\
    \        return cnt+1\n    \n    def partition(el, er, tm):\n        i = em =\
    \ el\n        while i < er:\n            if sccs[U[e := E[i]]] == sccs[V[e]]:\
    \ W[e], F[em] = tm, e; em += 1\n            i += 1\n        i, fm = el, em\n \
    \       while i < er:\n            if (u := sccs[U[e := E[i]]]) != (v := sccs[V[e]]):\
    \ U[e], V[e], F[fm] = u, v, e; fm += 1\n            i += 1\n        return em\n\
    \    \n    def div_con(N, el, er, tl, tr):\n        nonlocal E, F\n        if\
    \ el == er: return\n        tm, em = (tl+tr) >> 1, el\n        while em < er and\
    \ E[em] <= tm: em += 1\n        build_csr(N, E, el, em)\n        nN = scc_labels(N,\
    \ E, el, em, er, La, Ra, Va)\n        em = partition(el, er, tm)\n        if tr-tl==1:\
    \ return\n        E, F = F, E\n        div_con(nN, em, er, tm, tr)\n        div_con(N,\
    \ el, em, tl, tm)\n        E, F = F, E\n    div_con(N, 0, M, -1, M)\n    return\
    \ W\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.graph.__header__\n\
    import cp_library.alg.graph.fast.__header__\nimport cp_library.alg.graph.fast.snippets.__header__\n\
    \ndef scc_incremental(N, M, U, V):\n    U, V, W, La, Ra, Va = U[:], V[:], [M]*M,\
    \ [0]*N, [0]*N, [0]*M\n    E, F, sccs, st, buf, tin, low = [*range(M)], [*range(M)],\
    \ [0]*N, [0]*N, [0]*N, [-1]*N, [-1]*N\n\n    def build_csr(N, E, el, er):\n  \
    \      tot = 0\n        for u in range(N): La[u], tin[u] = 0, -1\n        i =\
    \ el\n        while i < er: La[U[e := E[i]]] += 1; i += 1\n        for u in range(N):\
    \ La[u] = Ra[u] = (tot := tot + La[u])\n        i = el\n        while i < er:\
    \ La[u] = a = La[u := U[e := E[i]]]-1; Va[a] = V[e]; i += 1\n\n    def scc_labels(N,\
    \ E, el, em, er, La, Ra, Va):\n        t = cnt = -1; i = el\n        while i <\
    \ em:\n            u = U[E[i]]; i += 1\n            if tin[u] < 0:\n         \
    \       st[0] = u; d = b = 0\n                while d >= 0:\n                \
    \    if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1); buf[b] = u; b += 1\n\
    \                    if La[u] < Ra[u]:\n                        if (tv := tin[Va[La[u]]])==\
    \ -1: st[d:=d+1] = Va[La[u]]\n                        elif tv < low[u]: low[u]\
    \ = tv\n                        La[u] += 1\n                    else:\n      \
    \                  if (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]\n\
    \                        if low[u] == tin[u]:\n                            v,\
    \ cnt = -1, cnt+1\n                            while u != v: tin[v := buf[b:=b-1]],\
    \ sccs[buf[b]] = N, cnt\n        while i < er:\n            u, v = U[E[i]], V[E[i]];\
    \ i += 1\n            if tin[u] < 0: tin[u], sccs[u] = N, (cnt:=cnt+1)\n     \
    \       if tin[v] < 0: tin[v], sccs[v] = N, (cnt:=cnt+1)\n        return cnt+1\n\
    \    \n    def partition(el, er, tm):\n        i = em = el\n        while i <\
    \ er:\n            if sccs[U[e := E[i]]] == sccs[V[e]]: W[e], F[em] = tm, e; em\
    \ += 1\n            i += 1\n        i, fm = el, em\n        while i < er:\n  \
    \          if (u := sccs[U[e := E[i]]]) != (v := sccs[V[e]]): U[e], V[e], F[fm]\
    \ = u, v, e; fm += 1\n            i += 1\n        return em\n    \n    def div_con(N,\
    \ el, er, tl, tr):\n        nonlocal E, F\n        if el == er: return\n     \
    \   tm, em = (tl+tr) >> 1, el\n        while em < er and E[em] <= tm: em += 1\n\
    \        build_csr(N, E, el, em)\n        nN = scc_labels(N, E, el, em, er, La,\
    \ Ra, Va)\n        em = partition(el, er, tm)\n        if tr-tl==1: return\n \
    \       E, F = F, E\n        div_con(nN, em, er, tm, tr)\n        div_con(N, el,\
    \ em, tl, tm)\n        E, F = F, E\n    div_con(N, 0, M, -1, M)\n    return W\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
  requiredBy: []
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/incremental_scc_paralel_sort.test.py
  - test/library-checker/graph/incremental_scc.test.py
documentation_of: cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
- /library/cp_library/alg/graph/fast/snippets/scc_incremental_fn.py.html
title: cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
---
