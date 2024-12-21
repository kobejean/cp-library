---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/digraph_weighted_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/digraph_weighted_meta_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_meta_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_base_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_meta_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_meta_cls.py
  - icon: ':warning:'
    path: cp_library/alg/iter/sort_parallel_fn.py
    title: cp_library/alg/iter/sort_parallel_fn.py
  - icon: ':warning:'
    path: cp_library/alg/tree/auxiliary_tree_cls.py
    title: cp_library/alg/tree/auxiliary_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_base_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_fast_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_fast_tree_lca_table_weighted_bit.test.py
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
    path: test/grl_5_a_fast_diameter.test.py
    title: test/grl_5_a_fast_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_b_fast_height.test.py
    title: test/grl_5_b_fast_height.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal.test.py
    title: test/minimum_spanning_tree_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal_heap.test.py
    title: test/minimum_spanning_tree_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_fast_graph.test.py
    title: test/shortest_path_fast_graph.test.py
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
    \ndef argsort(A: list[int]):\n    N = len(A)\n    mask = (1 << (shift := N.bit_length()))\
    \ - 1\n    indices = [0]*N\n    for i in range(N):\n        indices[i] = A[i]\
    \ << shift | i\n    indices.sort()\n    for i in range(N):\n        indices[i]\
    \ &= mask\n    return indices\n"
  code: "import cp_library.alg.iter.__header__\n\ndef argsort(A: list[int]):\n   \
    \ N = len(A)\n    mask = (1 << (shift := N.bit_length())) - 1\n    indices = [0]*N\n\
    \    for i in range(N):\n        indices[i] = A[i] << shift | i\n    indices.sort()\n\
    \    for i in range(N):\n        indices[i] &= mask\n    return indices\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/argsort_fn.py
  requiredBy:
  - cp_library/alg/iter/sort_parallel_fn.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_meta_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_meta_cls.py
  timestamp: '2024-12-21 20:47:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/grl_1_a_fast_dijkstra.test.py
  - test/minimum_spanning_tree_kruskal.test.py
  - test/grl_1_c_fast_floyd_warshall.test.py
  - test/shortest_path_fast_graph.test.py
  - test/grl_1_b_fast_bellman_ford.test.py
  - test/grl_5_b_fast_height.test.py
  - test/grl_5_a_fast_diameter.test.py
  - test/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - test/minimum_spanning_tree_kruskal_heap.test.py
documentation_of: cp_library/alg/iter/argsort_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/argsort_fn.py
- /library/cp_library/alg/iter/argsort_fn.py.html
title: cp_library/alg/iter/argsort_fn.py
---
