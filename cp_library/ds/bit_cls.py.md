---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/auxiliary_tree_cls.py
    title: cp_library/alg/tree/auxiliary_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_fast_cls.py
    title: cp_library/alg/tree/tree_fast_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_set_cls.py
    title: cp_library/alg/tree/tree_set_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  - icon: ':warning:'
    path: cp_library/ds/bir_cls.py
    title: cp_library/ds/bir_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc202_e_dfs_enter_leave.test.py
    title: test/abc202_e_dfs_enter_leave.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_iterative.test.py
    title: test/grl_5_c_lca_table_iterative.test.py
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
    \nclass BinaryIndexTree:\n    def __init__(self, v: int|list):\n        if isinstance(v,\
    \ int):\n            self.data, self.size = [0]*v, v\n        else:\n        \
    \    self.build(v)\n\n    def build(self, data):\n        self.data, self.size\
    \ = data, len(data)\n        for i in range(self.size):\n            if (r :=\
    \ i|(i+1)) < self.size: \n                self.data[r] += self.data[i]\n\n   \
    \ def get(self, i: int):\n        assert 0 <= i < self.size\n        s = self.data[i]\n\
    \        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n           \
    \ s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def set(self,\
    \ i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n    def add(self,\
    \ i: int, x: int) -> None:\n        assert 0 <= i <= self.size\n        i += 1\n\
    \        data, size = self.data, self.size\n        while i <= size:\n       \
    \     data[i-1], i = data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n\
    \        assert 0 <= i <= self.size\n        s = 0\n        data = self.data\n\
    \        for _ in range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n\
    \        return s\n    \n    def range_sum(self, l: int, r: int):\n        return\
    \ self.pref_sum(r) - self.pref_sum(l)\n"
  code: "import cp_library.ds.__header__\n\nclass BinaryIndexTree:\n    def __init__(self,\
    \ v: int|list):\n        if isinstance(v, int):\n            self.data, self.size\
    \ = [0]*v, v\n        else:\n            self.build(v)\n\n    def build(self,\
    \ data):\n        self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            if (r := i|(i+1)) < self.size: \n                self.data[r] +=\
    \ self.data[i]\n\n    def get(self, i: int):\n        assert 0 <= i < self.size\n\
    \        s = self.data[i]\n        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n\
    \            s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def\
    \ set(self, i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n \
    \   def add(self, i: int, x: int) -> None:\n        assert 0 <= i <= self.size\n\
    \        i += 1\n        data, size = self.data, self.size\n        while i <=\
    \ size:\n            data[i-1], i = data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self,\
    \ i: int):\n        assert 0 <= i <= self.size\n        s = 0\n        data =\
    \ self.data\n        for _ in range(i.bit_count()):\n            s, i = s+data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def range_sum(self, l: int, r: int):\n\
    \        return self.pref_sum(r) - self.pref_sum(l)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bit_cls.py
  requiredBy:
  - cp_library/ds/bir_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/tree_set_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/tree_fast_cls.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-22 04:31:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_5_c_lca_table_iterative.test.py
  - test/abc202_e_dfs_enter_leave.test.py
  - test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/dp_v_subtree_rerooting_iterative.test.py
documentation_of: cp_library/ds/bit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bit_cls.py
- /library/cp_library/ds/bit_cls.py.html
title: cp_library/ds/bit_cls.py
---
