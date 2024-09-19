---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/io/read_graph_directed_fn.py
    title: cp_library/io/read_graph_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_fn.py
    title: cp_library/io/read_graph_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
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
    \     return parse_spec(lambda s: cls(s))\n\nclass Graph(list, Parsable):\n  \
    \  def __init__(self, N, edges=[]):\n        super().__init__(([] for _ in range(N)))\n\
    \        for u,v in edges:\n            self[u].append(v)\n            self[v].append(u)\n\
    \n    @classmethod\n    def parse(cls, parse_spec, N, M, I=-1):\n        return\
    \ cls(N, parse_spec(list[tuple[I,I], M]))\n"
  code: "import cp_library.alg.__init__\n\nfrom cp_library.io.parsable_cls import\
    \ Parsable\n\nclass Graph(list, Parsable):\n    def __init__(self, N, edges=[]):\n\
    \        super().__init__(([] for _ in range(N)))\n        for u,v in edges:\n\
    \            self[u].append(v)\n            self[v].append(u)\n\n    @classmethod\n\
    \    def parse(cls, parse_spec, N, M, I=-1):\n        return cls(N, parse_spec(list[tuple[I,I],\
    \ M]))\n"
  dependsOn:
  - cp_library/io/parsable_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_cls.py
  requiredBy:
  - cp_library/io/read_graph_directed_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_graph_fn.py
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
documentation_of: cp_library/alg/graph/graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_cls.py
- /library/cp_library/alg/graph/graph_cls.py.html
title: cp_library/alg/graph/graph_cls.py
---
