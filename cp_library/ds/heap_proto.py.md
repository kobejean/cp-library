---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/fast_graph_cls.py
    title: cp_library/alg/graph/fast/fast_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/static_graph_cls.py
    title: cp_library/alg/graph/fast/static_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':warning:'
    path: cp_library/alg/graph/shortest_path_fn.py
    title: cp_library/alg/graph/shortest_path_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  - icon: ':x:'
    path: cp_library/ds/k_heap_mixin.py
    title: cp_library/ds/k_heap_mixin.py
  - icon: ':x:'
    path: cp_library/ds/max_heap_cls.py
    title: cp_library/ds/max_heap_cls.py
  - icon: ':x:'
    path: cp_library/ds/max_k_heap_cls.py
    title: cp_library/ds/max_k_heap_cls.py
  - icon: ':question:'
    path: cp_library/ds/min_heap_cls.py
    title: cp_library/ds/min_heap_cls.py
  - icon: ':x:'
    path: cp_library/ds/min_k_heap_cls.py
    title: cp_library/ds/min_k_heap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/priority_queue_cls.py
    title: cp_library/ds/priority_queue_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc218_f_shortest_path_weighted.test.py
    title: test/abc218_f_shortest_path_weighted.test.py
  - icon: ':x:'
    path: test/abc249_f_max_k_heap.test.py
    title: test/abc249_f_max_k_heap.test.py
  - icon: ':x:'
    path: test/abc249_f_min_k_heap.test.py
    title: test/abc249_f_min_k_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc375_g_find_bridges.test.py
    title: test/abc375_g_find_bridges.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_graph_distance.test.py
    title: test/grl_1_a_graph_distance.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_graph_bellman_ford.test.py
    title: test/grl_1_b_graph_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_graph_kruskal.test.py
    title: test/grl_2_a_graph_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_graph_weighted.test.py
    title: test/shortest_path_graph_weighted.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_min_heap.test.py
    title: test/shortest_path_min_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_static_graph_weighted.test.py
    title: test/shortest_path_static_graph_weighted.test.py
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
    from typing import Generic, TypeVar\n\nT = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n\
    \    def pop(self) -> T: ...\n    def push(self, item: T): ...\n    def pushpop(self,\
    \ item: T) -> T: ...\n    def replace(self, item: T) -> T: ...\n"
  code: "import cp_library.ds.__header__\nfrom typing import Generic, TypeVar\n\n\
    T = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n    def pop(self) -> T: ...\n\
    \    def push(self, item: T): ...\n    def pushpop(self, item: T) -> T: ...\n\
    \    def replace(self, item: T) -> T: ..."
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap_proto.py
  requiredBy:
  - cp_library/ds/max_heap_cls.py
  - cp_library/ds/min_k_heap_cls.py
  - cp_library/ds/k_heap_mixin.py
  - cp_library/ds/max_k_heap_cls.py
  - cp_library/ds/priority_queue_cls.py
  - cp_library/ds/min_heap_cls.py
  - cp_library/alg/graph/shortest_path_fn.py
  - cp_library/alg/graph/fast/fast_graph_cls.py
  - cp_library/alg/graph/fast/static_graph_cls.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-28 19:02:10+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/abc375_g_find_bridges.test.py
  - test/shortest_path_min_heap.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_1_a_graph_distance.test.py
  - test/grl_1_b_graph_bellman_ford.test.py
  - test/abc249_f_min_k_heap.test.py
  - test/shortest_path_graph_weighted.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/abc249_f_max_k_heap.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc218_f_shortest_path_weighted.test.py
  - test/shortest_path_static_graph_weighted.test.py
  - test/grl_2_a_graph_kruskal.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/ds/heap_proto.py
layout: document
redirect_from:
- /library/cp_library/ds/heap_proto.py
- /library/cp_library/ds/heap_proto.py.html
title: cp_library/ds/heap_proto.py
---
