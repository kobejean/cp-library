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
    path: cp_library/alg/tree/lca_table_recursive_cls.py
    title: cp_library/alg/tree/lca_table_recursive_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_iterative.test.py
    title: test/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_recursive.test.py
    title: test/grl_5_c_lca_table_recursive.test.py
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
    \nfrom typing import Any, Callable, List\n\nclass SparseTable:\n    def __init__(self,\
    \ op: Callable[[Any, Any], Any], arr: List[Any]):\n        self.n = len(arr)\n\
    \        self.log = self.n.bit_length()\n        self.op = op\n        self.st\
    \ = [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n        self.st[0]\
    \ = arr[:]\n        \n        for i in range(self.log-1):\n            row, d\
    \ = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n       \
    \         self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self, l: int,\
    \ r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n"
  code: "import cp_library.ds.__header__\n\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.n = len(arr)\n        self.log = self.n.bit_length()\n\
    \        self.op = op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in\
    \ range(self.log)]\n        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/sparse_table_cls.py
  requiredBy:
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/lca_table_recursive_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  timestamp: '2024-10-23 00:17:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_5_c_lca_table_iterative.test.py
  - test/grl_5_c_lca_table_recursive.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
documentation_of: cp_library/ds/sparse_table_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/sparse_table_cls.py
- /library/cp_library/ds/sparse_table_cls.py.html
title: cp_library/ds/sparse_table_cls.py
---
