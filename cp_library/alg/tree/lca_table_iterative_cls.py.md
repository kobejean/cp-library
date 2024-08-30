---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_iterative.test.py
    title: test/grl_5_c_lca_table_iterative.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from typing import List\n\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.n = len(arr)\n        self.log = self.n.bit_length()\n\
    \        self.op = op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in\
    \ range(self.log)]\n        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass LCATable(SparseTable):\n\
    \    def __init__(self, T: List[List[int]], root: int = 0):\n        self.start\
    \ = [-1] * len(T)\n        euler_tour = []\n        depths = []\n        \n  \
    \      # Iterative DFS\n        stack = [(root, -1, 0)]\n        while stack:\n\
    \            u, p, depth = stack.pop()\n            \n            if self.start[u]\
    \ == -1:  # start visit to this node\n                self.start[u] = len(euler_tour)\n\
    \                euler_tour.append(u)\n                depths.append(depth)\n\
    \                \n                # Add children to stack in reverse order\n\
    \                for child in reversed(T[u]):\n                    if child !=\
    \ p:\n                        stack.append((u, p, depth))  # Re-add parent for\
    \ backtracking\n                        stack.append((child, u, depth + 1))\n\
    \            else:  # Revisiting node (backtracking)\n                euler_tour.append(u)\n\
    \                depths.append(depth)\n        super().__init__(min, list(zip(depths,\
    \ euler_tour)))\n\n    def query(self, u: int, v: int) -> int:\n        l, r =\
    \ min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n   \
    \     _, a = super().query(l, r)\n        return a\n"
  code: "from typing import List\n\nfrom cp_library.ds.sparse_table_cls import SparseTable\n\
    \nclass LCATable(SparseTable):\n    def __init__(self, T: List[List[int]], root:\
    \ int = 0):\n        self.start = [-1] * len(T)\n        euler_tour = []\n   \
    \     depths = []\n        \n        # Iterative DFS\n        stack = [(root,\
    \ -1, 0)]\n        while stack:\n            u, p, depth = stack.pop()\n     \
    \       \n            if self.start[u] == -1:  # start visit to this node\n  \
    \              self.start[u] = len(euler_tour)\n                euler_tour.append(u)\n\
    \                depths.append(depth)\n                \n                # Add\
    \ children to stack in reverse order\n                for child in reversed(T[u]):\n\
    \                    if child != p:\n                        stack.append((u,\
    \ p, depth))  # Re-add parent for backtracking\n                        stack.append((child,\
    \ u, depth + 1))\n            else:  # Revisiting node (backtracking)\n      \
    \          euler_tour.append(u)\n                depths.append(depth)\n      \
    \  super().__init__(min, list(zip(depths, euler_tour)))\n\n    def query(self,\
    \ u: int, v: int) -> int:\n        l, r = min(self.start[u], self.start[v]), max(self.start[u],\
    \ self.start[v])+1\n        _, a = super().query(l, r)\n        return a\n"
  dependsOn:
  - cp_library/ds/sparse_table_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/lca_table_iterative_cls.py
  requiredBy: []
  timestamp: '2024-08-31 03:51:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_5_c_lca_table_iterative.test.py
documentation_of: cp_library/alg/tree/lca_table_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/lca_table_iterative_cls.py
- /library/cp_library/alg/tree/lca_table_iterative_cls.py.html
title: cp_library/alg/tree/lca_table_iterative_cls.py
---
