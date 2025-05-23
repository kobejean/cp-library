---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':heavy_check_mark:'
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
    max_unroll_recursion=-1\")\nfrom typing import Generic, Callable\nfrom typing\
    \ import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\n\nclass SparseTable(Generic[_T]):\n\
    \    def __init__(st, op: Callable[[_T,_T],_T], arr: list[_T]):\n        st.N\
    \ = N = len(arr)\n        st.log, st.op = N.bit_length(), op\n        st.data\
    \ = [0] * (st.log*N)\n        st.data[:N] = arr\n        for i in range(1,st.log):\n\
    \            a,b,c=i*N,(i-1)*N,(i-1)*N+(1<<(i-1))\n            for j in range(N-(1<<i)+1):\n\
    \                st.data[a+j] = op(st.data[b+j], st.data[c+j])\n\n    def query(st,\
    \ l: int, r: int) -> _T:\n        k = (r-l).bit_length()-1\n        return st.op(st.data[k*st.N+l],st.data[k*st.N+r-(1<<k)])\n\
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
  timestamp: '2025-05-23 09:29:26+09:00'
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
