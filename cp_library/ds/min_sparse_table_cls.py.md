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
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_a_diameter.test.py
    title: test/aoj/grl/grl_5_a_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
    title: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
    title: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
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
    from itertools import pairwise\nfrom typing import Any, List\n\nclass MinSparseTable:\n\
    \    def __init__(self, arr: List[Any]):\n        self.N = N = len(arr)\n    \
    \    self.log = N.bit_length()\n        \n        self.offsets = offsets = [0]\n\
    \        for i in range(1, self.log):\n            offsets.append(offsets[-1]\
    \ + N - (1 << (i-1)) + 1)\n            \n        self.st = st = [0] * (offsets[-1]\
    \ + N - (1 << (self.log-1)) + 1)\n        st[:N] = arr \n        \n        for\
    \ i,ni in pairwise(range(self.log)):\n            start, nxt, d = offsets[i],\
    \ offsets[ni], 1 << i\n            for j in range(N - (1 << ni) + 1):\n      \
    \          st[nxt+j] = min(st[k := start+j], st[k + d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length() - 1\n        start,\
    \ st = self.offsets[k], self.st\n        return min(st[start + l], st[start +\
    \ r - (1 << k)])\n    \n    def __repr__(self) -> str:\n        rows, offsets,\
    \ log, st = [], self.offsets, self.log, self.st\n        for i in range(log):\n\
    \            start = offsets[i]\n            end = offsets[i+1] if i+1 < log else\
    \ len(st)\n            rows.append(f\"{i:<2d} {st[start:end]}\")\n        return\
    \ '\\n'.join(rows)\n"
  code: "import cp_library.ds.__header__\nfrom itertools import pairwise\nfrom typing\
    \ import Any, List\n\nclass MinSparseTable:\n    def __init__(self, arr: List[Any]):\n\
    \        self.N = N = len(arr)\n        self.log = N.bit_length()\n        \n\
    \        self.offsets = offsets = [0]\n        for i in range(1, self.log):\n\
    \            offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)\n            \n\
    \        self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1)) + 1)\n  \
    \      st[:N] = arr \n        \n        for i,ni in pairwise(range(self.log)):\n\
    \            start, nxt, d = offsets[i], offsets[ni], 1 << i\n            for\
    \ j in range(N - (1 << ni) + 1):\n                st[nxt+j] = min(st[k := start+j],\
    \ st[k + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return min(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows, offsets, log, st = [], self.offsets, self.log, self.st\n        for\
    \ i in range(log):\n            start = offsets[i]\n            end = offsets[i+1]\
    \ if i+1 < log else len(st)\n            rows.append(f\"{i:<2d} {st[start:end]}\"\
    )\n        return '\\n'.join(rows)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/min_sparse_table_cls.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_a_diameter.test.py
  - test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/ds/min_sparse_table_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/min_sparse_table_cls.py
- /library/cp_library/ds/min_sparse_table_cls.py.html
title: cp_library/ds/min_sparse_table_cls.py
---
