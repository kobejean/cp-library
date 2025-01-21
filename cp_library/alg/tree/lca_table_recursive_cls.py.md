---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
    title: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
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
    \n\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\nfrom typing import Any, Callable, List\n\nclass\
    \ SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):\n\
    \        self.N = N = len(arr)\n        self.log = N.bit_length()\n        self.op\
    \ = op\n        \n        self.offsets = offsets = [0]\n        for i in range(1,\
    \ self.log):\n            offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)\n\
    \            \n        self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1))\
    \ + 1)\n        st[:N] = arr \n        \n        for i in range(self.log - 1):\n\
    \            d = 1 << i\n            start = offsets[i]\n            next_start\
    \ = offsets[i + 1]\n            for j in range(N - (1 << (i+1)) + 1):\n      \
    \          st[next_start + j] = op(st[k := start+j], st[k + d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length() - 1\n        start,\
    \ st = self.offsets[k], self.st\n        return self.op(st[start + l], st[start\
    \ + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n        rows = []\n\
    \        for i in range(self.log):\n            start = self.offsets[i]\n    \
    \        end = self.offsets[i+1] if i+1 < self.log else len(self.st)\n       \
    \     rows.append(f\"{i:<2d} {self.st[start:end]}\")\n        return '\\n'.join(rows)\n\
    \nclass LCATable(SparseTable):\n    def __init__(self, T, root):\n        self.start\
    \ = [-1] * len(T)\n        euler_tour = []\n        depths = []\n        \n  \
    \      def dfs(u: int, p: int, depth: int):\n            self.start[u] = len(euler_tour)\n\
    \            euler_tour.append(u)\n            depths.append(depth)\n        \
    \    \n            for child in T[u]:\n                if child != p:\n      \
    \              dfs(child, u, depth + 1)\n                    euler_tour.append(u)\n\
    \                    depths.append(depth)\n        \n        dfs(root, -1, 0)\n\
    \        super().__init__(min, list(zip(depths, euler_tour)))\n\n    def query(self,\
    \ u, v) -> tuple[int,int]:\n        l, r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        d, a = super().query(l, r)\n  \
    \      return a, d\n\n    def distance(self, u, v) -> int:\n        l, r = min(self.start[u],\
    \ self.start[v]), max(self.start[u], self.start[v])+1\n        d, _ = super().query(l,\
    \ r)\n        return self.depth[l] + self.depth[r] - 2*d\n"
  code: "import cp_library.alg.tree.__header__\nimport cp_library.misc.setrecursionlimit\n\
    from cp_library.ds.sparse_table_cls import SparseTable\n\nclass LCATable(SparseTable):\n\
    \    def __init__(self, T, root):\n        self.start = [-1] * len(T)\n      \
    \  euler_tour = []\n        depths = []\n        \n        def dfs(u: int, p:\
    \ int, depth: int):\n            self.start[u] = len(euler_tour)\n           \
    \ euler_tour.append(u)\n            depths.append(depth)\n            \n     \
    \       for child in T[u]:\n                if child != p:\n                 \
    \   dfs(child, u, depth + 1)\n                    euler_tour.append(u)\n     \
    \               depths.append(depth)\n        \n        dfs(root, -1, 0)\n   \
    \     super().__init__(min, list(zip(depths, euler_tour)))\n\n    def query(self,\
    \ u, v) -> tuple[int,int]:\n        l, r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        d, a = super().query(l, r)\n  \
    \      return a, d\n\n    def distance(self, u, v) -> int:\n        l, r = min(self.start[u],\
    \ self.start[v]), max(self.start[u], self.start[v])+1\n        d, _ = super().query(l,\
    \ r)\n        return self.depth[l] + self.depth[r] - 2*d"
  dependsOn:
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/sparse_table_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/lca_table_recursive_cls.py
  requiredBy: []
  timestamp: '2025-01-21 19:55:16+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_c_lca_table_recursive.test.py
documentation_of: cp_library/alg/tree/lca_table_recursive_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/lca_table_recursive_cls.py
- /library/cp_library/alg/tree/lca_table_recursive_cls.py.html
title: cp_library/alg/tree/lca_table_recursive_cls.py
---
