---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
    title: cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/incremental_scc
    links:
    - https://judge.yosupo.jp/problem/incremental_scc
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc\n\
    \ndef main():\n    N, M = rd(), rd()\n    X, U, V = rdl(N), [0]*M, [0]*M\n   \
    \ for e in range(M): U[e], V[e] = rd(), rd()\n    W, dsu, ans, mod = scc_incremental(N,\
    \ M, U, V), [*range(N)], [0]*M, 998244353; cur = t = 0\n    isort_parallel(W,\
    \ U, V)\n    for e in range(M):\n        u, v, w = U[e], V[e], W[e]\n        while\
    \ t < w: ans[t] = cur; t += 1\n        while u != dsu[u]: dsu[u] = u = dsu[dsu[u]]\n\
    \        while v != dsu[v]: dsu[v] = v = dsu[dsu[v]]\n        if u != v: dsu[v],\
    \ cur, X[u] = u, (cur+X[u]*X[v])%mod, (X[u]+X[v])%mod\n    while t < M: ans[t]\
    \ = cur; t += 1\n    wtnl(ans)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\n\n\ndef scc_incremental(N, M, U, V):\n    U, V, W,\
    \ La, Ra, Va = U[:], V[:], [M]*M, [0]*N, [0]*N, [0]*M\n    E, F, sccs, st, buf,\
    \ tin, low = [*range(M)], [*range(M)], [0]*N, [0]*N, [0]*N, [-1]*N, [-1]*N\n\n\
    \    def build_csr(N, E, el, er):\n        tot = 0\n        for u in range(N):\
    \ La[u], tin[u] = 0, -1\n        i = el\n        while i < er: La[U[e := E[i]]]\
    \ += 1; i += 1\n        for u in range(N): La[u] = Ra[u] = (tot := tot + La[u])\n\
    \        i = el\n        while i < er: La[u] = a = La[u := U[e := E[i]]]-1; Va[a]\
    \ = V[e]; i += 1\n\n    def scc_labels(N, E, el, em, er, La, Ra, Va):\n      \
    \  t = cnt = -1; i = el\n        while i < em:\n            u = U[E[i]]; i +=\
    \ 1\n            if tin[u] < 0:\n                st[0] = u; d = b = 0\n      \
    \          while d >= 0:\n                    if tin[u := st[d]] == -1: tin[u]\
    \ = low[u] = (t:=t+1); buf[b] = u; b += 1\n                    if La[u] < Ra[u]:\n\
    \                        if (tv := tin[Va[La[u]]])== -1: st[d:=d+1] = Va[La[u]]\n\
    \                        elif tv < low[u]: low[u] = tv\n                     \
    \   La[u] += 1\n                    else:\n                        if (d:=d-1)\
    \ >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]\n                        if\
    \ low[u] == tin[u]:\n                            v, cnt = -1, cnt+1\n        \
    \                    while u != v: tin[v := buf[b:=b-1]], sccs[buf[b]] = N, cnt\n\
    \        while i < er:\n            u, v = U[E[i]], V[E[i]]; i += 1\n        \
    \    if tin[u] < 0: tin[u], sccs[u] = N, (cnt:=cnt+1)\n            if tin[v] <\
    \ 0: tin[v], sccs[v] = N, (cnt:=cnt+1)\n        return cnt+1\n    \n    def partition(el,\
    \ er, tm):\n        i = em = el\n        while i < er:\n            if sccs[U[e\
    \ := E[i]]] == sccs[V[e]]: W[e], F[em] = tm, e; em += 1\n            i += 1\n\
    \        i, fm = el, em\n        while i < er:\n            if (u := sccs[U[e\
    \ := E[i]]]) != (v := sccs[V[e]]): U[e], V[e], F[fm] = u, v, e; fm += 1\n    \
    \        i += 1\n        return em\n    \n    def div_con(N, el, er, tl, tr):\n\
    \        nonlocal E, F\n        if el == er: return\n        tm, em = (tl+tr)\
    \ >> 1, el\n        while em < er and E[em] <= tm: em += 1\n        build_csr(N,\
    \ E, el, em)\n        nN = scc_labels(N, E, el, em, er, La, Ra, Va)\n        em\
    \ = partition(el, er, tm)\n        if tr-tl==1: return\n        E, F = F, E\n\
    \        div_con(nN, em, er, tm, tr)\n        div_con(N, el, em, tl, tm)\n   \
    \     E, F = F, E\n    div_con(N, 0, M, -1, M)\n    return W\n\n\n\ndef argsort(A:\
    \ list[int], reverse=False):\n    s, m = pack_sm(len(A))\n    if reverse:\n  \
    \      I = [a<<s|m^i for i,a in enumerate(A)]\n        I.sort(reverse=True)\n\
    \        for i,ai in enumerate(I): I[i] = m^ai&m\n    else:\n        I = [a<<s|i\
    \ for i,a in enumerate(A)]\n        I.sort()\n        for i,ai in enumerate(I):\
    \ I[i] = ai&m\n    return I\n\n\ndef pack_sm(N: int): s=N.bit_length(); return\
    \ s,(1<<s)-1\n\n\ndef isort_parallel(*L: list, reverse=False):\n    inv, order\
    \ = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n    for i, j in enumerate(order):\
    \ inv[j] = i\n    for i, j in enumerate(order):\n        for A in L: A[i], A[j]\
    \ = A[j], A[i]\n        order[inv[i]], inv[j] = j, inv[i]\n    return L\n\n\n\
    from __pypy__.builders import StringBuilder\nimport sys\nfrom os import read as\
    \ os_read, write as os_write\nfrom atexit import register as atexist_register\n\
    \nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n    sb = StringBuilder()\n\
    \    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n        self.ibuf\
    \ += os_read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n   \
    \ def flush_atexit(self): os_write(1, self.sb.build().encode())\n    def flush(self):\n\
    \        os_write(1, self.sb.build().encode())\n        self.sb = StringBuilder()\n\
    \    def fastin(self):\n        if self.pir - self.pil < 64: self.load()\n   \
    \     minus = x = 0\n        while self.ibuf[self.pil] < 45: self.pil += 1\n \
    \       if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1\n        while\
    \ self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil] &\
    \ 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n):\n    lst = [0]*n\n    for i in\
    \ range(n): lst[i] = rd()\n    return lst\ndef wtnl(l): wtn(' '.join(map(str,\
    \ l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc\n\
    \ndef main():\n    N, M = rd(), rd()\n    X, U, V = rdl(N), [0]*M, [0]*M\n   \
    \ for e in range(M): U[e], V[e] = rd(), rd()\n    W, dsu, ans, mod = scc_incremental(N,\
    \ M, U, V), [*range(N)], [0]*M, 998244353; cur = t = 0\n    isort_parallel(W,\
    \ U, V)\n    for e in range(M):\n        u, v, w = U[e], V[e], W[e]\n        while\
    \ t < w: ans[t] = cur; t += 1\n        while u != dsu[u]: dsu[u] = u = dsu[dsu[u]]\n\
    \        while v != dsu[v]: dsu[v] = v = dsu[dsu[v]]\n        if u != v: dsu[v],\
    \ cur, X[u] = u, (cur+X[u]*X[v])%mod, (X[u]+X[v])%mod\n    while t < M: ans[t]\
    \ = cur; t += 1\n    wtnl(ans)\n\nfrom cp_library.alg.graph.fast.snippets.scc_incremental_fn\
    \ import scc_incremental\nfrom cp_library.alg.iter.sort.isort_parallel_fn import\
    \ isort_parallel\nfrom cp_library.io.fast.fast_io_fn import rd, rdl, wtnl\n\n\
    if __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/graph/fast/snippets/scc_incremental_fn.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/io/fast/fast_io_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: true
  path: test/library-checker/graph/incremental_scc_paralel_sort.test.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/incremental_scc_paralel_sort.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/incremental_scc_paralel_sort.test.py
- /verify/test/library-checker/graph/incremental_scc_paralel_sort.test.py.html
title: test/library-checker/graph/incremental_scc_paralel_sort.test.py
---
