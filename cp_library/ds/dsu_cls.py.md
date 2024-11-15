---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_heap_fn.py
    title: cp_library/alg/graph/kruskal_heap_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_sort_fn.py
    title: cp_library/alg/graph/kruskal_sort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc375_g_find_bridges.test.py
    title: test/abc375_g_find_bridges.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nclass DSU:\n    def __init__(self, n):\n        self.n = n\n        self.par\
    \ = [-1] * n\n\n    def merge(self, u, v, src = False):\n        assert 0 <= u\
    \ < self.n\n        assert 0 <= v < self.n\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return (x,y) if src else x\n\n        if -self.par[x] < -self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n\
    \        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n        return\
    \ self.leader(u) == self.leader(v)\n\n    def leader(self, i) -> int:\n      \
    \  assert 0 <= i < self.n\n\n        p = self.par[i]\n        while p >= 0:\n\
    \            if self.par[p] < 0:\n                return p\n            self.par[i],\
    \ i, p = self.par[p], self.par[p], self.par[self.par[p]]\n\n        return i\n\
    \n    def size(self, i) -> int:\n        assert 0 <= i < self.n\n        \n  \
    \      return -self.par[self.leader(i)]\n\n    def groups(self) -> list[list[int]]:\n\
    \        leader_buf = [self.leader(i) for i in range(self.n)]\n\n        result\
    \ = [[] for _ in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return list(filter(lambda r: r, result))\n"
  code: "import cp_library.ds.__header__\n\nclass DSU:\n    def __init__(self, n):\n\
    \        self.n = n\n        self.par = [-1] * n\n\n    def merge(self, u, v,\
    \ src = False):\n        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\
    \n        x, y = self.leader(u), self.leader(v)\n        if x == y: return (x,y)\
    \ if src else x\n\n        if -self.par[x] < -self.par[y]:\n            x, y =\
    \ y, x\n\n        self.par[x] += self.par[y]\n        self.par[y] = x\n\n    \
    \    return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n     \
    \   assert 0 <= u < self.n\n        assert 0 <= v < self.n\n        return self.leader(u)\
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
  - cp_library/alg/graph/kruskal_heap_fn.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/graph/kruskal_sort_fn.py
  - cp_library/alg/graph/edmonds_fn.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-16 03:24:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc375_g_find_bridges.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_2_a_kruskal_heap.test.py
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/unionfind.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/ds/dsu_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/dsu_cls.py
- /library/cp_library/ds/dsu_cls.py.html
title: cp_library/ds/dsu_cls.py
---
