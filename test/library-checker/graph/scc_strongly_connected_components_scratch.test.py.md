---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\n\
    \ndef strongly_connected_components(N, M, La, Ra, Va):\n    st, buf, sccs, L,\
    \ tin, low, t, d = [0]*N, elist(N), elist(N), elist(N), [-1]*N, [N]*N, -1, -1\n\
    \    for u in range(N):\n        if tin[u] >= 0: continue\n        st[d:=0] =\
    \ u\n        while d >= 0:\n            if tin[u := st[d]] == -1: tin[u] = low[u]\
    \ = (t:=t+1); buf.append(u)\n            if (a := La[u]) < Ra[u]:\n          \
    \      La[u] += 1\n                if (tv := tin[v := Va[a]]) == -1: st[d:=d+1]\
    \ = v\n                elif tv < low[u]: low[u] = tv\n            else:\n    \
    \            if (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]\n \
    \               if low[u] == tin[u]:\n                    L.append(len(sccs));\
    \ v = -1\n                    while u != v: tin[v := buf.pop()] = N; sccs.append(v)\n\
    \    return sccs, L\n\ndef main():\n    N, M, La, Ra, Va = read_csr_graph()\n\
    \    sccs, L = strongly_connected_components(N, M, La, Ra, Va)\n    fast_write_cc(sccs,\
    \ L)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \n\n\nfrom __pypy__.builders import StringBuilder\nimport sys\nfrom os import\
    \ read as os_read, write as os_write\nfrom atexit import register as atexist_register\n\
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
    \ l)))\n\ndef read_csr_graph():\n    La, Ra, U, V, Va, t = [0]*(N:=rd()), [0]*N,\
    \ [0]*(M:=rd()), [0]*M, [0]*M, 0\n    for e in range(M): La[u := rd()] += 1; U[e],\
    \ V[e] = u, rd()\n    for u, deg in enumerate(La): La[u] = Ra[u] = (t := t + deg)\n\
    \    for e, u in enumerate(U): La[u] -= 1; Va[La[u]] = V[e]\n    return N, M,\
    \ La, Ra, Va\n\ndef fast_write_cc(A, L):\n    r = len(A); wtn(len(L))\n    while\
    \ L:\n        l = L.pop(); wt(r-l)\n        while l < r: r -= 1; fastio.sb.append('\
    \ '); wt(A[r])\n        fastio.sb.append('\\n')\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\n\ndef\
    \ strongly_connected_components(N, M, La, Ra, Va):\n    st, buf, sccs, L, tin,\
    \ low, t, d = [0]*N, elist(N), elist(N), elist(N), [-1]*N, [N]*N, -1, -1\n   \
    \ for u in range(N):\n        if tin[u] >= 0: continue\n        st[d:=0] = u\n\
    \        while d >= 0:\n            if tin[u := st[d]] == -1: tin[u] = low[u]\
    \ = (t:=t+1); buf.append(u)\n            if (a := La[u]) < Ra[u]:\n          \
    \      La[u] += 1\n                if (tv := tin[v := Va[a]]) == -1: st[d:=d+1]\
    \ = v\n                elif tv < low[u]: low[u] = tv\n            else:\n    \
    \            if (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]\n \
    \               if low[u] == tin[u]:\n                    L.append(len(sccs));\
    \ v = -1\n                    while u != v: tin[v := buf.pop()] = N; sccs.append(v)\n\
    \    return sccs, L\n\ndef main():\n    N, M, La, Ra, Va = read_csr_graph()\n\
    \    sccs, L = strongly_connected_components(N, M, La, Ra, Va)\n    fast_write_cc(sccs,\
    \ L)\n\nfrom cp_library.ds.elist_fn import elist\nfrom cp_library.io.fast.fast_io_fn\
    \ import rd, wt, wtn, fastio\n\ndef read_csr_graph():\n    La, Ra, U, V, Va, t\
    \ = [0]*(N:=rd()), [0]*N, [0]*(M:=rd()), [0]*M, [0]*M, 0\n    for e in range(M):\
    \ La[u := rd()] += 1; U[e], V[e] = u, rd()\n    for u, deg in enumerate(La): La[u]\
    \ = Ra[u] = (t := t + deg)\n    for e, u in enumerate(U): La[u] -= 1; Va[La[u]]\
    \ = V[e]\n    return N, M, La, Ra, Va\n\ndef fast_write_cc(A, L):\n    r = len(A);\
    \ wtn(len(L))\n    while L:\n        l = L.pop(); wt(r-l)\n        while l < r:\
    \ r -= 1; fastio.sb.append(' '); wt(A[r])\n        fastio.sb.append('\\n')\n\n\
    if __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/ds/elist_fn.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
  requiredBy: []
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
- /verify/test/library-checker/graph/scc_strongly_connected_components_scratch.test.py.html
title: test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
---
