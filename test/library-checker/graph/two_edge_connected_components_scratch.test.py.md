---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
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
    PROBLEM: https://judge.yosupo.jp/problem/two_edge_connected_components
    links:
    - https://judge.yosupo.jp/problem/two_edge_connected_components
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\n\
    \ndef main():\n    N, M = rd(), rd()\n    La, Ra, Va, Ea = read_csr_graph(N, M)\n\
    \    e2ccs, L = two_edge_connected_components(N, M, La, Ra, Va, Ea)\n    fast_write_cc(e2ccs,\
    \ L)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return ch\n\ndef read_csr_graph(N,\
    \ M):\n    U, V, La, Ra, Va, Ea, t = [0]*M, [0]*M, [0]*N, [0]*N, [0]*(M << 1),\
    \ [-1]*(M << 1), 0\n    for e in range(M): La[u := rd()] += 1; La[v := rd()] +=\
    \ u!=v; U[e], V[e] = u, v\n    for u in range(N): La[u] = Ra[u] = (t := t + La[u])\n\
    \    for e in range(M): La[u := U[e]] -= 1; La[v := V[e]] -= u!=v; Va[La[u]],\
    \ Va[La[v]] = v, u; Ea[La[u]] = Ea[La[v]] = e\n    return La, Ra, Va, Ea\n\ndef\
    \ two_edge_connected_components(N, M, La, Ra, Va, Ea):\n    st, buf, e2ccs, L,\
    \ Ein, tin, low, t, d = [0]*N, elist(N), elist(N), elist(N), [-1]*N, [-1]*N, [-1]*N,\
    \ -1, -1\n    for u in range(N):\n        if Ein[u] >= 0: continue\n        Ein[u]\
    \ = M; st[d:=0] = u\n        while d >= 0:\n            if tin[u := st[d]] ==\
    \ -1: tin[u] = low[u] = (t:=t+1); buf.append(u)\n            if (a := La[u]) <\
    \ Ra[u]:\n                La[u] += 1\n                if Ein[v := Va[a]] == -1:\
    \ Ein[v] = Ea[a]; st[d:=d+1] = v\n                elif Ea[a] != Ein[u]: chmin(low,\
    \ u, tin[v])\n            elif (d:=d-1) >= 0 and not chmin(low, p := st[d], low[u])\
    \ and low[u] > tin[p]:\n                L.append(len(e2ccs)); v = -1\n       \
    \         while u != v: e2ccs.append(v := buf.pop())\n        L.append(len(e2ccs));\
    \ e2ccs.extend(buf); buf.clear()\n    return e2ccs, L\n\n\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \n\n\n\
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
    \ l)))\n\ndef fast_write_cc(A, L):\n    r = len(A); wtn(len(L))\n    while L:\n\
    \        l = L.pop(); wt(r-l)\n        while l < r: r -= 1; fastio.sb.append('\
    \ '); wt(A[r])\n        fastio.sb.append('\\n')\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\n\
    \ndef main():\n    N, M = rd(), rd()\n    La, Ra, Va, Ea = read_csr_graph(N, M)\n\
    \    e2ccs, L = two_edge_connected_components(N, M, La, Ra, Va, Ea)\n    fast_write_cc(e2ccs,\
    \ L)\n\nfrom cp_library.alg.dp.chmin_fn import chmin\n\ndef read_csr_graph(N,\
    \ M):\n    U, V, La, Ra, Va, Ea, t = [0]*M, [0]*M, [0]*N, [0]*N, [0]*(M << 1),\
    \ [-1]*(M << 1), 0\n    for e in range(M): La[u := rd()] += 1; La[v := rd()] +=\
    \ u!=v; U[e], V[e] = u, v\n    for u in range(N): La[u] = Ra[u] = (t := t + La[u])\n\
    \    for e in range(M): La[u := U[e]] -= 1; La[v := V[e]] -= u!=v; Va[La[u]],\
    \ Va[La[v]] = v, u; Ea[La[u]] = Ea[La[v]] = e\n    return La, Ra, Va, Ea\n\ndef\
    \ two_edge_connected_components(N, M, La, Ra, Va, Ea):\n    st, buf, e2ccs, L,\
    \ Ein, tin, low, t, d = [0]*N, elist(N), elist(N), elist(N), [-1]*N, [-1]*N, [-1]*N,\
    \ -1, -1\n    for u in range(N):\n        if Ein[u] >= 0: continue\n        Ein[u]\
    \ = M; st[d:=0] = u\n        while d >= 0:\n            if tin[u := st[d]] ==\
    \ -1: tin[u] = low[u] = (t:=t+1); buf.append(u)\n            if (a := La[u]) <\
    \ Ra[u]:\n                La[u] += 1\n                if Ein[v := Va[a]] == -1:\
    \ Ein[v] = Ea[a]; st[d:=d+1] = v\n                elif Ea[a] != Ein[u]: chmin(low,\
    \ u, tin[v])\n            elif (d:=d-1) >= 0 and not chmin(low, p := st[d], low[u])\
    \ and low[u] > tin[p]:\n                L.append(len(e2ccs)); v = -1\n       \
    \         while u != v: e2ccs.append(v := buf.pop())\n        L.append(len(e2ccs));\
    \ e2ccs.extend(buf); buf.clear()\n    return e2ccs, L\n\nfrom cp_library.ds.elist_fn\
    \ import elist\nfrom cp_library.io.fast.fast_io_fn import rd, wt, wtn, fastio\n\
    \ndef fast_write_cc(A, L):\n    r = len(A); wtn(len(L))\n    while L:\n      \
    \  l = L.pop(); wt(r-l)\n        while l < r: r -= 1; fastio.sb.append(' '); wt(A[r])\n\
    \        fastio.sb.append('\\n')\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/graph/two_edge_connected_components_scratch.test.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/two_edge_connected_components_scratch.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/two_edge_connected_components_scratch.test.py
- /verify/test/library-checker/graph/two_edge_connected_components_scratch.test.py.html
title: test/library-checker/graph/two_edge_connected_components_scratch.test.py
---
