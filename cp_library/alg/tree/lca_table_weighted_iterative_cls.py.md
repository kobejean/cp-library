---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':warning:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':warning:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable, TypeVar\n\nT = TypeVar('T')\ndef presum(iter: Iterable[T], func: Callable[[T,T],T]\
    \ = None, initial: T = None, step = 1) -> list[T]:\n    match step:\n        case\
    \ 1:\n            return list(accumulate(iter, func, initial=initial))\n     \
    \   case step:\n            assert step >= 2\n            if func is None:\n \
    \               func = operator.add\n            A = list(iter)\n            if\
    \ initial is not None:\n                A = [initial] + A\n            for i in\
    \ range(step,len(A)):\n                A[i] = func(A[i], A[i-step])\n        \
    \    return A\n\n\nfrom typing import Any, Callable, List\n\nclass SparseTable:\n\
    \    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):\n    \
    \    self.N = N = len(arr)\n        self.log = N.bit_length()\n        self.op\
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
    \nclass LCATable(SparseTable):\n    def __init__(self, T, root = 0):\n       \
    \ N = len(T)\n        T.euler_tour(root)\n        self.depth = depth = presum(T.delta)\n\
    \        self.start, self.stop = T.tin, T.tout\n\n        self.mask = (1 << (shift\
    \ := N.bit_length()))-1\n        self.shift = shift\n        order = T.order\n\
    \        M = len(order)\n        packets = [0]*M\n        for i in range(M):\n\
    \            packets[i] = depth[i] << shift | order[i] \n\n        super().__init__(min,\
    \ packets)\n\n    def _query(self, u, v):\n        l,r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        da = super().query(l, r)\n    \
    \    return l, r, da & self.mask, da >> self.shift\n\n    def query(self, u, v)\
    \ -> tuple[int,int]:\n        l, r, a, d = self._query(u, v)\n        return a,\
    \ d\n    \n    def distance(self, u, v) -> int:\n        l, r, a, d = self._query(u,\
    \ v)\n        return self.depth[l] + self.depth[r] - 2*d\n\nclass LCATableWeighted(LCATable):\n\
    \    def __init__(self, T, root = 0):\n        super().__init__(T, root)\n   \
    \     self.weights = T.Wdelta\n        self.weighted_depth = None\n\n    def distance(self,\
    \ u, v) -> int:\n        if self.weighted_depth is None:\n            self.weighted_depth\
    \ = presum(self.weights)\n        l, r, a, _ = self._query(u, v)\n        m =\
    \ self.start[a]\n        return self.weighted_depth[l] + self.weighted_depth[r]\
    \ - 2*self.weighted_depth[m]\n"
  code: "import cp_library.alg.tree.__header__\nfrom cp_library.alg.iter.presum_fn\
    \ import presum\nfrom cp_library.alg.tree.lca_table_iterative_cls import LCATable\n\
    \nclass LCATableWeighted(LCATable):\n    def __init__(self, T, root = 0):\n  \
    \      super().__init__(T, root)\n        self.weights = T.Wdelta\n        self.weighted_depth\
    \ = None\n\n    def distance(self, u, v) -> int:\n        if self.weighted_depth\
    \ is None:\n            self.weighted_depth = presum(self.weights)\n        l,\
    \ r, a, _ = self._query(u, v)\n        m = self.start[a]\n        return self.weighted_depth[l]\
    \ + self.weighted_depth[r] - 2*self.weighted_depth[m]"
  dependsOn:
  - cp_library/alg/iter/presum_fn.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/ds/sparse_table_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py.html
title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
---