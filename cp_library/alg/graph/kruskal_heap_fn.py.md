---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_a_kruskal_heap.test.py
    title: test/aoj/grl/grl_2_a_kruskal_heap.test.py
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
    \nfrom heapq import heapify, heappop\n\n\nclass DSU:\n    def __init__(self, N):\n\
    \        self.N = N\n        self.par = [-1] * N\n\n    def merge(self, u, v,\
    \ src = False):\n        assert 0 <= u < self.N\n        assert 0 <= v < self.N\n\
    \n        x, y = self.leader(u), self.leader(v)\n        if x == y: return (x,y)\
    \ if src else x\n\n        if self.par[x] > self.par[y]:\n            x, y = y,\
    \ x\n\n        self.par[x] += self.par[y]\n        self.par[y] = x\n\n       \
    \ return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n        assert\
    \ 0 <= u < self.N\n        assert 0 <= v < self.N\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.N\n        par = self.par\n        p = par[i]\n        while p >= 0:\n\
    \            if par[p] < 0:\n                return p\n            par[i], i,\
    \ p = par[p], par[p], par[par[p]]\n\n        return i\n\n    def size(self, i)\
    \ -> int:\n        assert 0 <= i < self.N\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.N)]\n\n        result = [[] for _ in range(self.N)]\n  \
    \      for i in range(self.N):\n            result[leader_buf[i]].append(i)\n\n\
    \        return [r for r in result if r]\n\ndef kruskal(E, N):\n    heapify(E)\n\
    \    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and need:\n     \
    \   edge = heappop(E)\n        u,v,_ = edge\n        if not dsu.same(u,v):\n \
    \           dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom heapq import heapify, heappop\n\
    from cp_library.ds.dsu_cls import DSU\n\ndef kruskal(E, N):\n    heapify(E)\n\
    \    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and need:\n     \
    \   edge = heappop(E)\n        u,v,_ = edge\n        if not dsu.same(u,v):\n \
    \           dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n"
  dependsOn:
  - cp_library/ds/dsu_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/kruskal_heap_fn.py
  requiredBy: []
  timestamp: '2025-03-15 12:29:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/alg/graph/kruskal_heap_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/kruskal_heap_fn.py
- /library/cp_library/alg/graph/kruskal_heap_fn.py.html
title: cp_library/alg/graph/kruskal_heap_fn.py
---
