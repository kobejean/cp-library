---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dijkstra_fn.py
    title: cp_library/alg/graph/dijkstra_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/digraph_cls.py
    title: cp_library/alg/graph/fast/digraph_cls.py
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
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/snippets/strongly_connected_components_fn.py
    title: cp_library/alg/graph/snippets/strongly_connected_components_fn.py
  - icon: ':warning:'
    path: cp_library/alg/graph/strongly_connected_components_fn.py
    title: cp_library/alg/graph/strongly_connected_components_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_base_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_a_dijkstra.test.py
    title: test/aoj/grl/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_a_fast_dijkstra.test.py
    title: test/aoj/grl/grl_1_a_fast_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_b_fast_bellman_ford.test.py
    title: test/aoj/grl/grl_1_b_fast_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_c_fast_floyd_warshall.test.py
    title: test/aoj/grl/grl_1_c_fast_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_a_fast_diameter.test.py
    title: test/aoj/grl/grl_5_a_fast_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_b_fast_height.test.py
    title: test/aoj/grl/grl_5_b_fast_height.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
    title: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc301_e_fast_grid_graph.test.py
    title: test/atcoder/abc/abc301_e_fast_grid_graph.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/cycle_detection.test.py
    title: test/library-checker/graph/cycle_detection.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/minimum_spanning_tree_kruskal.test.py
    title: test/library-checker/graph/minimum_spanning_tree_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/minimum_spanning_tree_kruskal_heap.test.py
    title: test/library-checker/graph/minimum_spanning_tree_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/scc.test.py
    title: test/library-checker/graph/scc.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/scc_strongly_connected_components.test.py
    title: test/library-checker/graph/scc_strongly_connected_components.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/shortest_path_fast_graph.test.py
    title: test/library-checker/graph/shortest_path_fast_graph.test.py
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
    \ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return ch\n"
  code: "import cp_library.alg.dp.__header__\n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n\
    \    return ch"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/dp/chmin_fn.py
  requiredBy:
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/graph/snippets/strongly_connected_components_fn.py
  - cp_library/alg/graph/dijkstra_fn.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_meta_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_meta_cls.py
  - cp_library/alg/graph/fast/digraph_cls.py
  - cp_library/alg/graph/strongly_connected_components_fn.py
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc218_f_fast_shortest_path.test.py
  - test/atcoder/abc/abc301_e_fast_grid_graph.test.py
  - test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - test/library-checker/graph/minimum_spanning_tree_kruskal.test.py
  - test/library-checker/graph/scc.test.py
  - test/library-checker/graph/cycle_detection.test.py
  - test/library-checker/graph/shortest_path_fast_graph.test.py
  - test/library-checker/graph/scc_strongly_connected_components.test.py
  - test/library-checker/graph/minimum_spanning_tree_kruskal_heap.test.py
  - test/aoj/grl/grl_1_a_fast_dijkstra.test.py
  - test/aoj/grl/grl_1_c_fast_floyd_warshall.test.py
  - test/aoj/grl/grl_1_a_dijkstra.test.py
  - test/aoj/grl/grl_1_b_fast_bellman_ford.test.py
  - test/aoj/grl/grl_5_b_fast_height.test.py
  - test/aoj/grl/grl_5_a_fast_diameter.test.py
documentation_of: cp_library/alg/dp/chmin_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/chmin_fn.py
- /library/cp_library/alg/dp/chmin_fn.py.html
title: cp_library/alg/dp/chmin_fn.py
---