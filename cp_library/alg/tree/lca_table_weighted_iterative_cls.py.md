---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  _extendedRequiredBy:
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
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\nfrom typing import Any, Callable, List\n\nclass SparseTable:\n   \
    \ def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):\n       \
    \ self.n = len(arr)\n        self.log = self.n.bit_length()\n        self.op =\
    \ op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n\
    \        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\nfrom itertools\
    \ import accumulate\n\nclass LCATableWeighted(SparseTable):\n    def __init__(self,\
    \ T, root = 0):\n        self.start = [-1] * len(T)\n        self.end = [-1] *\
    \ len(T)\n        self.euler = []\n        self.depth = []\n        self.weights\
    \ = []\n        self.weighted_depth = None\n        \n        # Iterative DFS\n\
    \        stack = [(root, -1, 0, 0)]\n        while stack:\n            u, p, d,\
    \ w = stack.pop()\n            \n            if self.start[u] == -1:\n       \
    \         self.start[u] = len(self.euler)\n                for v, nw in reversed(T[u]):\n\
    \                    if v != p:\n                        stack.append((u, p, d,\
    \ -nw))\n                        stack.append((v, u, d+1, nw))\n\n           \
    \ self.euler.append(u)\n            self.depth.append(d)\n            self.weights.append(w)\n\
    \            self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n\n    def distance(self,\
    \ u, v) -> int:\n        if self.weighted_depth is None:\n            self.weighted_depth\
    \ = list(accumulate(self.weights))\n        l, r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        _, a = super().query(l, r)\n  \
    \      m = self.start[a]\n        return self.weighted_depth[l] + self.weighted_depth[r]\
    \ - 2*self.weighted_depth[m]\n"
  code: "import cp_library.alg.tree.__header__\nfrom cp_library.ds.sparse_table_cls\
    \ import SparseTable\nfrom itertools import accumulate\n\nclass LCATableWeighted(SparseTable):\n\
    \    def __init__(self, T, root = 0):\n        self.start = [-1] * len(T)\n  \
    \      self.end = [-1] * len(T)\n        self.euler = []\n        self.depth =\
    \ []\n        self.weights = []\n        self.weighted_depth = None\n        \n\
    \        # Iterative DFS\n        stack = [(root, -1, 0, 0)]\n        while stack:\n\
    \            u, p, d, w = stack.pop()\n            \n            if self.start[u]\
    \ == -1:\n                self.start[u] = len(self.euler)\n                for\
    \ v, nw in reversed(T[u]):\n                    if v != p:\n                 \
    \       stack.append((u, p, d, -nw))\n                        stack.append((v,\
    \ u, d+1, nw))\n\n            self.euler.append(u)\n            self.depth.append(d)\n\
    \            self.weights.append(w)\n            self.end[u] = len(self.euler)\n\
    \        super().__init__(min, list(zip(self.depth, self.euler)))\n\n    def query(self,\
    \ u, v) -> tuple[int,int]:\n        l, r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        d, a = super().query(l, r)\n  \
    \      return a, d\n\n    def distance(self, u, v) -> int:\n        if self.weighted_depth\
    \ is None:\n            self.weighted_depth = list(accumulate(self.weights))\n\
    \        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n\
    \        _, a = super().query(l, r)\n        m = self.start[a]\n        return\
    \ self.weighted_depth[l] + self.weighted_depth[r] - 2*self.weighted_depth[m]"
  dependsOn:
  - cp_library/ds/sparse_table_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-16 11:24:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc361_e_tree_diameter.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
documentation_of: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py.html
title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
---
