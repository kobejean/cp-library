---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
  _extendedRequiredBy:
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
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
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
    \nimport operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable, TypeVar\n_T = TypeVar('T')\n\ndef presum(iter: Iterable[_T], func:\
    \ Callable[[_T,_T],_T] = None, initial: _T = None, step = 1) -> list[_T]:\n  \
    \  if step == 1:\n        return list(accumulate(iter, func, initial=initial))\n\
    \    else:\n        assert step >= 2\n        if func is None:\n            func\
    \ = operator.add\n        A = list(iter)\n        if initial is not None:\n  \
    \          A = [initial] + A\n        for i in range(step,len(A)):\n         \
    \   A[i] = func(A[i], A[i-step])\n        return A\n\nfrom itertools import pairwise\n\
    from typing import Any, List\n\nclass MinSparseTable:\n    def __init__(self,\
    \ arr: List[Any]):\n        self.N = N = len(arr)\n        self.log = N.bit_length()\n\
    \        \n        self.offsets = offsets = [0]\n        for i in range(1, self.log):\n\
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
    )\n        return '\\n'.join(rows)\n\nclass LCATable(MinSparseTable):\n    def\
    \ __init__(self, T, root = 0):\n        N = len(T)\n        T.euler_tour(root)\n\
    \        self.depth = depth = presum(T.delta)\n        self.start, self.stop =\
    \ T.tin, T.tout\n        self.mask = (1 << (shift := N.bit_length()))-1\n    \
    \    self.shift = shift\n        order = T.order\n        M = len(order)\n   \
    \     packets = [0]*M\n        for i in range(M):\n            packets[i] = depth[i]\
    \ << shift | order[i] \n        super().__init__(packets)\n\n    def _query(self,\
    \ u, v):\n        start = self.start\n        l,r = min(start[u], start[v]), max(start[u],\
    \ start[v])+1\n        da = super().query(l, r)\n        return l, r, da & self.mask,\
    \ da >> self.shift\n\n    def query(self, u, v) -> tuple[int,int]:\n        l,\
    \ r, a, d = self._query(u, v)\n        return a, d\n    \n    def distance(self,\
    \ u, v) -> int:\n        l, r, a, d = self._query(u, v)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n    \n    def path(self, u, v):\n        path, par, lca,\
    \ c = [], self.T.par, self.query(u, v)[0], u\n        while c != lca:\n      \
    \      path.append(c)\n            c = par[c]\n        path.append(lca)\n    \
    \    rev_path, c = [], v\n        while c != lca:\n            rev_path.append(c)\n\
    \            c = par[c]\n        path.extend(reversed(rev_path))\n        return\
    \ path\n\nclass LCATableWeighted(LCATable):\n    def __init__(self, T, root =\
    \ 0):\n        super().__init__(T, root)\n        self.weights = T.Wdelta\n  \
    \      self.weighted_depth = None\n\n    def distance(self, u, v) -> int:\n  \
    \      if self.weighted_depth is None:\n            self.weighted_depth = presum(self.weights)\n\
    \        l, r, a, _ = self._query(u, v)\n        m = self.start[a]\n        return\
    \ self.weighted_depth[l] + self.weighted_depth[r] - 2*self.weighted_depth[m]\n"
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
  - cp_library/ds/min_sparse_table_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_a_diameter.test.py
  - test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
documentation_of: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py.html
title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
---
