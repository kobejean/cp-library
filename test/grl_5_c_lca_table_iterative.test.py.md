---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C\n\
    from typing import Any, Callable, List\n\nclass SparseTable:\n    def __init__(self,\
    \ op: Callable[[Any, Any], Any], arr: List[Any]):\n        self.n = len(arr)\n\
    \        self.log = self.n.bit_length()\n        self.op = op\n        self.st\
    \ = [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n        self.st[0]\
    \ = arr[:]\n        \n        for i in range(self.log-1):\n            row, d\
    \ = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n       \
    \         self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self, l: int,\
    \ r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass LCATable(SparseTable):\n\
    \    def __init__(self, T, root = 0):\n        self.start = [-1] * len(T)\n  \
    \      self.euler = []\n        self.depth = []\n        \n        # Iterative\
    \ DFS\n        stack = [(root, -1, 0)]\n        while stack:\n            u, p,\
    \ d = stack.pop()\n            \n            if self.start[u] == -1:  # start\
    \ visit to this node\n                self.start[u] = len(self.euler)\n      \
    \          self.euler.append(u)\n                self.depth.append(d)\n      \
    \          \n                # Add children to stack in reverse order\n      \
    \          for child in reversed(T[u]):\n                    if child != p:\n\
    \                        stack.append((u, p, d))  # Re-add parent for backtracking\n\
    \                        stack.append((child, u, d + 1))\n            else:  #\
    \ Revisiting node (backtracking)\n                self.euler.append(u)\n     \
    \           self.depth.append(d)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n\ndef read(shift=0, base=10):\n\
    \    return [int(s, base) + shift for s in  input().split()]\n\nN, = read()\n\
    T = []\nfor _ in range(N):\n    k, *adj = read()\n    T.append(adj)\nlca = LCATable(T,\
    \ 0)\nQ, = read()\nfor _ in range(Q):\n    u, v = read()\n    print(lca.query(u,v)[0])\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C\n\
    from cp_library.alg.tree.lca_table_iterative_cls import LCATable\nfrom cp_library.io.read_int_fn\
    \ import read\n\nN, = read()\nT = []\nfor _ in range(N):\n    k, *adj = read()\n\
    \    T.append(adj)\nlca = LCATable(T, 0)\nQ, = read()\nfor _ in range(Q):\n  \
    \  u, v = read()\n    print(lca.query(u,v)[0])"
  dependsOn:
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/ds/sparse_table_cls.py
  isVerificationFile: true
  path: test/grl_5_c_lca_table_iterative.test.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_5_c_lca_table_iterative.test.py
layout: document
redirect_from:
- /verify/test/grl_5_c_lca_table_iterative.test.py
- /verify/test/grl_5_c_lca_table_iterative.test.py.html
title: test/grl_5_c_lca_table_iterative.test.py
---
