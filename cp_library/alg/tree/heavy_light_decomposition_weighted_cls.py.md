---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/alg/tree/heavy_light_decomposition_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_cls.py
  _extendedRequiredBy: []
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
    \            u,v = v,u\n        query_fn(start[v]+edge, start[u]+1)\n\nclass HLDWeighted(HLD):\n\
    \    def __init__(self, T, r=0):\n        super().__init__(T, r)\n        self.weights\
    \ = T.Wpar\n"
  code: "import cp_library.alg.tree.__header__\nfrom cp_library.alg.tree.heavy_light_decomposition_cls\
    \ import HLD\n\nclass HLDWeighted(HLD):\n    def __init__(self, T, r=0):\n   \
    \     super().__init__(T, r)\n        self.weights = T.Wpar\n"
  dependsOn:
  - cp_library/alg/tree/heavy_light_decomposition_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  requiredBy: []
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
- /library/cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py.html
title: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
---