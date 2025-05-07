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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_C\n\
    \ndef strongly_connected_components(N, M, La, Ra, Va):\n    st, buf, sccs, tin,\
    \ low, t, d, id = [0]*N, elist(N), [-1]*N, [-1]*N, [N]*N, -1, -1, -1\n    for\
    \ u in range(N):\n        if tin[u] >= 0: continue\n        st[d:=0] = u\n   \
    \     while d >= 0:\n            if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1);\
    \ buf.append(u)\n            if (a := La[u]) < Ra[u]:\n                La[u] +=\
    \ 1\n                if (tv := tin[v := Va[a]]) == -1: st[d:=d+1] = v\n      \
    \          elif tv < low[u]: low[u] = tv\n            else:\n                if\
    \ (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]\n               \
    \ if low[u] == tin[u]:\n                    v, id = -1, id+1\n               \
    \     while u != v: tin[v := buf.pop()] = N; sccs[v] = id\n    return sccs\n\n\
    def main():\n    N, M, La, Ra, Va = read_csr_graph()\n    sccs = strongly_connected_components(N,\
    \ M, La, Ra, Va)\n    Q = rd()\n    for _ in range(Q):\n        u, v = rd(), rd()\n\
    \        wtn(int(sccs[u]==sccs[v]))\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from\
    \ __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n       \
    \ return []\nelist = newlist_hint\n    \n\ndef read_csr_graph():\n    La, Ra,\
    \ U, V, Va, t = [0]*(N:=rd()), [0]*N, [0]*(M:=rd()), [0]*M, [0]*M, 0\n    for\
    \ e in range(M): La[u := rd()] += 1; U[e], V[e] = u, rd()\n    for u, deg in enumerate(La):\
    \ La[u] = Ra[u] = (t := t + deg)\n    for e, u in enumerate(U): La[u] -= 1; Va[La[u]]\
    \ = V[e]\n    return N, M, La, Ra, Va\n\n\n\nfrom __pypy__.builders import StringBuilder\n\
    import sys\nfrom os import read as os_read, write as os_write\nfrom atexit import\
    \ register as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n    pil =\
    \ pir = 0\n    sb = StringBuilder()\n    def load(self):\n        self.ibuf =\
    \ self.ibuf[self.pil:]\n        self.ibuf += os_read(0, 131072)\n        self.pil\
    \ = 0; self.pir = len(self.ibuf)\n    def flush_atexit(self): os_write(1, self.sb.build().encode())\n\
    \    def flush(self):\n        os_write(1, self.sb.build().encode())\n       \
    \ self.sb = StringBuilder()\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
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
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_C\n\
    \ndef strongly_connected_components(N, M, La, Ra, Va):\n    st, buf, sccs, tin,\
    \ low, t, d, id = [0]*N, elist(N), [-1]*N, [-1]*N, [N]*N, -1, -1, -1\n    for\
    \ u in range(N):\n        if tin[u] >= 0: continue\n        st[d:=0] = u\n   \
    \     while d >= 0:\n            if tin[u := st[d]] == -1: tin[u] = low[u] = (t:=t+1);\
    \ buf.append(u)\n            if (a := La[u]) < Ra[u]:\n                La[u] +=\
    \ 1\n                if (tv := tin[v := Va[a]]) == -1: st[d:=d+1] = v\n      \
    \          elif tv < low[u]: low[u] = tv\n            else:\n                if\
    \ (d:=d-1) >= 0 and low[u] < low[st[d]]: low[st[d]] = low[u]\n               \
    \ if low[u] == tin[u]:\n                    v, id = -1, id+1\n               \
    \     while u != v: tin[v := buf.pop()] = N; sccs[v] = id\n    return sccs\n\n\
    def main():\n    N, M, La, Ra, Va = read_csr_graph()\n    sccs = strongly_connected_components(N,\
    \ M, La, Ra, Va)\n    Q = rd()\n    for _ in range(Q):\n        u, v = rd(), rd()\n\
    \        wtn(int(sccs[u]==sccs[v]))\n\nfrom cp_library.ds.elist_fn import elist\n\
    \ndef read_csr_graph():\n    La, Ra, U, V, Va, t = [0]*(N:=rd()), [0]*N, [0]*(M:=rd()),\
    \ [0]*M, [0]*M, 0\n    for e in range(M): La[u := rd()] += 1; U[e], V[e] = u,\
    \ rd()\n    for u, deg in enumerate(La): La[u] = Ra[u] = (t := t + deg)\n    for\
    \ e, u in enumerate(U): La[u] -= 1; Va[La[u]] = V[e]\n    return N, M, La, Ra,\
    \ Va\n\nfrom cp_library.io.fast.fast_io_fn import rd, wt, wtn, fastio\n\nif __name__\
    \ == '__main__':\n    main()"
  dependsOn:
  - cp_library/ds/elist_fn.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/aoj/grl/grl_2_c_scc_fast.test.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_2_c_scc_fast.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_2_c_scc_fast.test.py
- /verify/test/aoj/grl/grl_2_c_scc_fast.test.py.html
title: test/aoj/grl/grl_2_c_scc_fast.test.py
---
