---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/digraph_weighted_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_proto.py
    title: cp_library/alg/graph/fast/graph_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_fast_dijkstra.test.py
    title: test/grl_1_a_fast_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_fast_bellman_ford.test.py
    title: test/grl_1_b_fast_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_fast_floyd_warshall.test.py
    title: test/grl_1_c_fast_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal.test.py
    title: test/minimum_spanning_tree_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal_heap.test.py
    title: test/minimum_spanning_tree_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_static_graph_weighted.test.py
    title: test/shortest_path_static_graph_weighted.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from array import array\n\ndef fill_i32(N: int, elm: int = 0):\n \
    \   return array('i', (elm,)) * N\n\ndef fill_u32(N: int, elm: int = 0):\n   \
    \ return array('I', (elm,)) * N\n\ndef fill_i64(N: int, elm: int = 0):\n    return\
    \ array('q', (elm,)) * N\n\ndef fill_u64(N: int, elm: int = 0):\n    return array('Q',\
    \ (elm,)) * N\n"
  code: "from array import array\n\ndef fill_i32(N: int, elm: int = 0):\n    return\
    \ array('i', (elm,)) * N\n\ndef fill_u32(N: int, elm: int = 0):\n    return array('I',\
    \ (elm,)) * N\n\ndef fill_i64(N: int, elm: int = 0):\n    return array('q', (elm,))\
    \ * N\n\ndef fill_u64(N: int, elm: int = 0):\n    return array('Q', (elm,)) *\
    \ N"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/fill_fn.py
  requiredBy:
  - cp_library/alg/graph/fast/graph_weighted_proto.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  timestamp: '2024-11-29 11:58:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_c_fast_floyd_warshall.test.py
  - test/grl_1_b_fast_bellman_ford.test.py
  - test/shortest_path_static_graph_weighted.test.py
  - test/grl_1_a_fast_dijkstra.test.py
  - test/minimum_spanning_tree_kruskal_heap.test.py
  - test/minimum_spanning_tree_kruskal.test.py
documentation_of: cp_library/ds/fill_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/fill_fn.py
- /library/cp_library/ds/fill_fn.py.html
title: cp_library/ds/fill_fn.py
---
