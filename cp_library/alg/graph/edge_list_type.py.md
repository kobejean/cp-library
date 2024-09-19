---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':question:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
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
    from typing import TypeAlias, TypeVar\n\nM = TypeVar('M', int, None)\nI = TypeVar('I',\
    \ int, None)\nEdgeList: TypeAlias = list[tuple[I,I], M]\n"
  code: 'import cp_library.alg.graph.__init__

    from typing import TypeAlias, TypeVar


    M = TypeVar(''M'', int, None)

    I = TypeVar(''I'', int, None)

    EdgeList: TypeAlias = list[tuple[I,I], M]'
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/edge_list_type.py
  requiredBy:
  - cp_library/io/read_graph_directed_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_graph_fn.py
  - cp_library/alg/graph/graph_cls.py
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
documentation_of: cp_library/alg/graph/edge_list_type.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge_list_type.py
- /library/cp_library/alg/graph/edge_list_type.py.html
title: cp_library/alg/graph/edge_list_type.py
---
