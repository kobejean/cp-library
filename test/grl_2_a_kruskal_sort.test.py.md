---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_sort_fn.py
    title: cp_library/alg/graph/kruskal_sort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef read(shift=0, base=10):\n    return [int(s, base) + shift for s in  input().split()]\n\
    \ndef read_edges(M, i0=1):\n    E = []\n    for _ in range(M):\n        u,v,w\
    \ = read(-i0)\n        w += i0\n        E.append((w,u,v))\n    return E\n\n\n\
    class DSU:\n    def __init__(self, n):\n        self.n = n\n        self.par =\
    \ [-1] * n\n\n    def merge(self, u, v):\n        assert 0 <= u < self.n\n   \
    \     assert 0 <= v < self.n\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n    \
    \        x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return x\n\n    def same(self, u: int, v: int):\n        assert\
    \ 0 <= u < self.n\n        assert 0 <= v < self.n\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.n\n\n        p = self.par[i]\n        while p >= 0:\n            if self.par[p]\
    \ < 0:\n                return p\n            self.par[i], i, p = self.par[p],\
    \ self.par[p], self.par[self.par[p]]\n\n        return i\n\n    def size(self,\
    \ i) -> int:\n        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n\ndef kruskal(E, N):\n    E.sort(reverse=True)\n\
    \    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and need > 0:\n \
    \       edge = E.pop()\n        _,u,v = edge\n        if not dsu.same(u,v):\n\
    \            dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n\nN, M = read()\nE = read_edges(M, 0)\nMST = kruskal(E, N)\n\
    ans = sum(w for w,u,v in MST)\nprint(ans)\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

    from cp_library.io.read_int_fn import read

    from cp_library.io.read_edges_weighted_fn import read_edges

    from cp_library.alg.graph.kruskal_sort_fn import kruskal


    N, M = read()

    E = read_edges(M, 0)

    MST = kruskal(E, N)

    ans = sum(w for w,u,v in MST)

    print(ans)'
  dependsOn:
  - cp_library/io/read_int_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/kruskal_sort_fn.py
  - cp_library/ds/dsu_cls.py
  isVerificationFile: true
  path: test/grl_2_a_kruskal_sort.test.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_a_kruskal_sort.test.py
layout: document
redirect_from:
- /verify/test/grl_2_a_kruskal_sort.test.py
- /verify/test/grl_2_a_kruskal_sort.test.py.html
title: test/grl_2_a_kruskal_sort.test.py
---