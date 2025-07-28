---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/snippets/scc_incremental_fn.py
    title: cp_library/alg/graph/csr/snippets/scc_incremental_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_bounded_fn.py
    title: cp_library/alg/iter/arg/argsort_bounded_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_fn.py
    title: cp_library/io/fast_io_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
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
    \ndef main():\n    N, M = rd()\n    X, U, V = rdl(N), [0]*M, [0]*M\n    for e\
    \ in range(M): U[e], V[e] = rd()\n    W, dsu, ans, mod = scc_incremental(N, M,\
    \ U, V), [*range(N)], [0]*M, 998244353; cur = t = 0\n    for e in argsort_bounded(W,M):\n\
    \        while t < W[e]: ans[t] = cur; t += 1\n        u, v = U[e], V[e]\n   \
    \     while u != dsu[u]: dsu[u] = u = dsu[dsu[u]]\n        while v != dsu[v]:\
    \ dsu[v] = v = dsu[dsu[v]]\n        if u != v: dsu[v], cur, X[u] = u, (cur+X[u]*X[v])%mod,\
    \ (X[u]+X[v])%mod\n    while t < M: ans[t] = cur; t += 1\n    wtnl(ans)\n\n'''\n\
    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\n\n\n\n\
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
    \ em, tl, tm)\n        E, F = F, E\n    div_con(N, 0, M, -1, M)\n    return W\n\
    \n\n\ndef argsort(A: list[int], reverse=False):\n    P = Packer(len(I := list(A))-1);\
    \ P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n    return I\n\n\n\nclass\
    \ Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length();\
    \ P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n\
    \    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def\
    \ enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A\n\
    \    def ienumerate(P, A, reverse=False):\n        if reverse:\n            for\
    \ i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n            for i,a\
    \ in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A));\
    \ return A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\
    \ndef argsort_bounded(A, mx=None, reverse=False):\n    N = len(A)\n    if mx is\
    \ None: mx = max(A)\n    if N*N.bit_length() < mx or mx < 1000: return argsort(A,\
    \ reverse)\n    I, cnt, t = [0]*N, [0]*(mx+1), 0\n    for a in A: cnt[a] += 1\n\
    \    if reverse:\n        for a in range(mx+1): cnt[~a], t = t, t+cnt[~a]\n  \
    \  else:\n        for a in range(mx+1): cnt[a], t = t, t+cnt[a]\n    for i,a in\
    \ enumerate(A): I[cnt[a]] = i; cnt[a] += 1\n    return I\n\nfrom os import read\
    \ as os_read, write as os_write, fstat as os_fstat\nimport sys\nfrom __pypy__.builders\
    \ import StringBuilder\n\n\ndef max2(a, b): return a if a > b else b\n\nclass\
    \ IOBase:\n    @property\n    def char(io) -> bool: ...\n    @property\n    def\
    \ writable(io) -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io,\
    \ s: str) -> None: ...\n    def readline(io) -> str: ...\n    def readtoken(io)\
    \ -> str: ...\n    def readtokens(io) -> list[str]: ...\n    def readints(io)\
    \ -> list[int]: ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io)\
    \ -> list[int]: ...\n    def readchar(io) -> str: ...\n    def readchars(io) ->\
    \ str: ...\n    def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass IO(IOBase):\n    BUFSIZE\
    \ = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O',\
    \ 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n\
    \    def __init__(io, file):\n        io.file = file\n        try: io.f = file.fileno();\
    \ io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode\
    \ or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE,\
    \ False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
    \ io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False,\
    \ [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def _readint(io, r):\n        while\
    \ io.p < r and io.B[io.p] <= 32: io.p += 1\n        if io.p >= r: return None\n\
    \        minus = x = 0\n        if io.B[io.p] == 45: minus = 1; io.p += 1\n  \
    \      while io.p < r and io.B[io.p] >= 48: x = x * 10 + (io.B[io.p] & 15); io.p\
    \ += 1\n        io.p += 1\n        return -x if minus else x\n    def readintsinto(io,\
    \ lst):\n        io.load(); r = io.O[io.l]\n        while io.p < r and (x := io._readint(r))\
    \ is not None: lst.append(x)\n        io.l += 1; return lst\n    def _readdigit(io):\
    \ d = io.B[io.p] & 15; io.p += 1; return d\n    def readdigitsinto(io, lst):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r and io.B[io.p] > 32:\
    \ lst.append(io._readdigit())\n        if io.B[io.p] == 10: io.l += 1\n      \
    \  io.p += 1\n        return lst\n    def readnumsinto(io, lst):\n        if io.char:\
    \ return io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n \
    \   def line(io): io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n\
    \        if io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors));\
    \ io.S = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\ndef rd(): return IO.stdin.readints()\ndef rds(): return IO.stdin.__next__()\n\
    def rdl(n): return IO.stdin.readintsinto(elist(n))\ndef wt(s): IO.stdout.write(s)\n\
    def wtn(s): IO.stdout.write(f'{s}\\n')\ndef wtnl(l): IO.stdout.write(' '.join(map(str,\
    \ l)))\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc\n\
    \ndef main():\n    N, M = rd()\n    X, U, V = rdl(N), [0]*M, [0]*M\n    for e\
    \ in range(M): U[e], V[e] = rd()\n    W, dsu, ans, mod = scc_incremental(N, M,\
    \ U, V), [*range(N)], [0]*M, 998244353; cur = t = 0\n    for e in argsort_bounded(W,M):\n\
    \        while t < W[e]: ans[t] = cur; t += 1\n        u, v = U[e], V[e]\n   \
    \     while u != dsu[u]: dsu[u] = u = dsu[dsu[u]]\n        while v != dsu[v]:\
    \ dsu[v] = v = dsu[dsu[v]]\n        if u != v: dsu[v], cur, X[u] = u, (cur+X[u]*X[v])%mod,\
    \ (X[u]+X[v])%mod\n    while t < M: ans[t] = cur; t += 1\n    wtnl(ans)\n\nfrom\
    \ cp_library.alg.graph.csr.snippets.scc_incremental_fn import scc_incremental\n\
    from cp_library.alg.iter.arg.argsort_bounded_fn import argsort_bounded\nfrom cp_library.io.fast_io_fn\
    \ import rd, rdl, wtnl\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/graph/csr/snippets/scc_incremental_fn.py
  - cp_library/alg/iter/arg/argsort_bounded_fn.py
  - cp_library/io/fast_io_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/io/io_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: true
  path: test/library-checker/graph/incremental_scc.test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/incremental_scc.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/incremental_scc.test.py
- /verify/test/library-checker/graph/incremental_scc.test.py.html
title: test/library-checker/graph/incremental_scc.test.py
---
