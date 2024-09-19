---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
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
    \n\n\nclass Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n   \
    \     return parse_spec(lambda s: cls(s))\n\nclass DiGraphWeighted(list, Parsable):\n\
    \    def __init__(self, N, edges=[]):\n        super().__init__(([] for _ in range(N)))\n\
    \        for u,v,w in edges:\n            self[u].append((w,v))\n\n    @classmethod\n\
    \    def parse(cls, parse_spec, N, M, I=-1):\n        return cls(N, parse_spec(list[tuple[I,I,int],\
    \ M]))\n"
  code: "import cp_library.alg.__init__\n\nfrom cp_library.io.parsable_cls import\
    \ Parsable\n\nclass DiGraphWeighted(list, Parsable):\n    def __init__(self, N,\
    \ edges=[]):\n        super().__init__(([] for _ in range(N)))\n        for u,v,w\
    \ in edges:\n            self[u].append((w,v))\n\n    @classmethod\n    def parse(cls,\
    \ parse_spec, N, M, I=-1):\n        return cls(N, parse_spec(list[tuple[I,I,int],\
    \ M]))\n"
  dependsOn:
  - cp_library/io/parsable_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/digraph_weighted_cls.py
  requiredBy: []
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/alg/graph/digraph_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/digraph_weighted_cls.py
- /library/cp_library/alg/graph/digraph_weighted_cls.py.html
title: cp_library/alg/graph/digraph_weighted_cls.py
---
