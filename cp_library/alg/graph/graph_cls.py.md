---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/graph/edge_list_type.py
    title: cp_library/alg/graph/edge_list_type.py
  - icon: ':question:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/io/read_graph_directed_fn.py
    title: cp_library/io/read_graph_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_fn.py
    title: cp_library/io/read_graph_fn.py
  - icon: ':question:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\nfrom typing import TypeAlias, TypeVar\n\nM = TypeVar('M', int, None)\nI =\
    \ TypeVar('I', int, None)\nEdgeList: TypeAlias = list[tuple[I,I], M]\n\n\nclass\
    \ Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n        return\
    \ parse_spec(lambda s: cls(s))\n\nclass Graph(list, Parsable):\n    def __init__(self,\
    \ N, edges: EdgeList=[]):\n        super().__init__(([] for _ in range(N)))\n\
    \        for u,v in edges:\n            self[u].append(v)\n            self[v].append(u)\n\
    \n    @classmethod\n    def parse(cls, parse_spec, N, M, I=-1):\n        return\
    \ cls(N, parse_spec(EdgeList[I,M]))\n"
  code: "import cp_library.alg.__init__\n\nfrom cp_library.alg.graph.edge_list_type\
    \ import EdgeList\nfrom cp_library.io.parsable_cls import Parsable\n\nclass Graph(list,\
    \ Parsable):\n    def __init__(self, N, edges: EdgeList=[]):\n        super().__init__(([]\
    \ for _ in range(N)))\n        for u,v in edges:\n            self[u].append(v)\n\
    \            self[v].append(u)\n\n    @classmethod\n    def parse(cls, parse_spec,\
    \ N, M, I=-1):\n        return cls(N, parse_spec(EdgeList[I,M]))\n"
  dependsOn:
  - cp_library/alg/graph/edge_list_type.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_cls.py
  requiredBy:
  - cp_library/io/read_graph_directed_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_graph_fn.py
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
documentation_of: cp_library/alg/graph/graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_cls.py
- /library/cp_library/alg/graph/graph_cls.py.html
title: cp_library/alg/graph/graph_cls.py
---
