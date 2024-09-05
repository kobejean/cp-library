---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_heap_fn.py
    title: cp_library/alg/graph/kruskal_heap_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_sort_fn.py
    title: cp_library/alg/graph/kruskal_sort_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/unionfind.test.py
    title: test/unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nclass DSU:\n    def __init__(self, n) -> None:\n        self.n =\
    \ n\n        self.par = [-1] * n\n\n    def merge(self, u, v) -> int:\n      \
    \  assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\n        x, y = self.leader(u),\
    \ self.leader(v)\n        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return x\n\n    def same(self, u: int, v: int) -> bool:\n   \
    \     assert 0 <= u < self.n\n        assert 0 <= v < self.n\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.n\n\n        p = self.par[i]\n        while p >= 0:\n            if self.par[p]\
    \ < 0:\n                return p\n            self.par[i], i, p = self.par[p],\
    \ self.par[p], self.par[self.par[p]]\n\n        return i\n\n    def size(self,\
    \ i) -> int:\n        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n"
  code: "\nclass DSU:\n    def __init__(self, n) -> None:\n        self.n = n\n  \
    \      self.par = [-1] * n\n\n    def merge(self, u, v) -> int:\n        assert\
    \ 0 <= u < self.n\n        assert 0 <= v < self.n\n\n        x, y = self.leader(u),\
    \ self.leader(v)\n        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return x\n\n    def same(self, u: int, v: int) -> bool:\n   \
    \     assert 0 <= u < self.n\n        assert 0 <= v < self.n\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.n\n\n        p = self.par[i]\n        while p >= 0:\n            if self.par[p]\
    \ < 0:\n                return p\n            self.par[i], i, p = self.par[p],\
    \ self.par[p], self.par[self.par[p]]\n\n        return i\n\n    def size(self,\
    \ i) -> int:\n        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/dsu_cls.py
  requiredBy:
  - cp_library/alg/graph/edmonds_fn.py
  - cp_library/alg/graph/kruskal_sort_fn.py
  - cp_library/alg/graph/kruskal_heap_fn.py
  timestamp: '2024-09-05 11:18:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/unionfind.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/ds/dsu_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/dsu_cls.py
- /library/cp_library/ds/dsu_cls.py.html
title: cp_library/ds/dsu_cls.py
---
