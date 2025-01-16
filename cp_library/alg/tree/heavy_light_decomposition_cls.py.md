---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - icon: ':x:'
    path: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - icon: ':x:'
    path: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import Sequence\n\nclass HLD(Sequence[int]):\n    def __init__(self,\
    \ T, r=0):\n        N = len(T)\n        T.hld_precomp(r)\n        self.N, self.T,\
    \ self.size, self.depth = N, T, T.size, T.depth\n        self.order, self.start,\
    \ self.end = T.order, T.tin, T.tout\n        self.par, self.heavy, self.head =\
    \ T.par, T.heavy, T.head\n\n    def __getitem__(self, key):\n        return self.start[key]\n\
    \    \n    def __len__(self):\n        return len(self.start)\n    \n    def __contains__(self,\
    \ value):\n        return self.start.__contains__(value)\n    \n    def subtree_range(self,\
    \ v):\n        return self.start[v], self.end[v]\n\n    def path(self, u, v, query_fn,\
    \ edge=False):\n        head, depth, par, start = self.head, self.depth, self.par,\
    \ self.start\n        while head[u] != head[v]:\n            if depth[head[u]]\
    \ < depth[head[v]]:\n                u,v = v,u\n            query_fn(start[head[u]],\
    \ start[u]+1)\n            u = par[head[u]]\n\n        if depth[u] < depth[v]:\n\
    \            u,v = v,u\n        query_fn(start[v]+edge, start[u]+1)\n"
  code: "import cp_library.alg.tree.__header__\nfrom typing import Sequence\n\nclass\
    \ HLD(Sequence[int]):\n    def __init__(self, T, r=0):\n        N = len(T)\n \
    \       T.hld_precomp(r)\n        self.N, self.T, self.size, self.depth = N, T,\
    \ T.size, T.depth\n        self.order, self.start, self.end = T.order, T.tin,\
    \ T.tout\n        self.par, self.heavy, self.head = T.par, T.heavy, T.head\n\n\
    \    def __getitem__(self, key):\n        return self.start[key]\n    \n    def\
    \ __len__(self):\n        return len(self.start)\n    \n    def __contains__(self,\
    \ value):\n        return self.start.__contains__(value)\n    \n    def subtree_range(self,\
    \ v):\n        return self.start[v], self.end[v]\n\n    def path(self, u, v, query_fn,\
    \ edge=False):\n        head, depth, par, start = self.head, self.depth, self.par,\
    \ self.start\n        while head[u] != head[v]:\n            if depth[head[u]]\
    \ < depth[head[v]]:\n                u,v = v,u\n            query_fn(start[head[u]],\
    \ start[u]+1)\n            u = par[head[u]]\n\n        if depth[u] < depth[v]:\n\
    \            u,v = v,u\n        query_fn(start[v]+edge, start[u]+1)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/tree/heavy_light_decomposition_cls.py
  requiredBy:
  - cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  timestamp: '2025-01-16 09:57:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
documentation_of: cp_library/alg/tree/heavy_light_decomposition_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/heavy_light_decomposition_cls.py
- /library/cp_library/alg/tree/heavy_light_decomposition_cls.py.html
title: cp_library/alg/tree/heavy_light_decomposition_cls.py
---
