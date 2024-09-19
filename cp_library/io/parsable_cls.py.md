---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':question:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':question:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':warning:'
    path: cp_library/io/read_edges_fn.py
    title: cp_library/io/read_edges_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':warning:'
    path: cp_library/io/read_graph_directed_fn.py
    title: cp_library/io/read_graph_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_fn.py
    title: cp_library/io/read_graph_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_weighted_directed_fn.py
    title: cp_library/io/read_graph_weighted_directed_fn.py
  - icon: ':warning:'
    path: cp_library/io/read_graph_weighted_fn.py
    title: cp_library/io/read_graph_weighted_fn.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
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
    path: test/dp_z_cht_monotone_add_min.test.py
    title: test/dp_z_cht_monotone_add_min.test.py
  - icon: ':heavy_check_mark:'
    path: test/dsl_2_c_kdtree.test.py
    title: test/dsl_2_c_kdtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_iterative.test.py
    title: test/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
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
    \nclass Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n       \
    \ return parse_spec(lambda s: cls(s))\n"
  code: "import cp_library.io.__init__\n\nclass Parsable:\n    @classmethod\n    def\
    \ parse(cls, parse_spec):\n        return parse_spec(lambda s: cls(s))"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/parsable_cls.py
  requiredBy:
  - cp_library/io/read_graph_directed_fn.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/read_graph_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/io/read_edges_fn.py
  - cp_library/io/read_graph_weighted_fn.py
  - cp_library/alg/graph/graph_cls.py
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/subset_convolution.test.py
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/grl_5_c_lca_table_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/dsl_2_c_kdtree.test.py
  - test/dp_z_cht_monotone_add_min.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_2_a_kruskal_heap.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
documentation_of: cp_library/io/parsable_cls.py
layout: document
redirect_from:
- /library/cp_library/io/parsable_cls.py
- /library/cp_library/io/parsable_cls.py.html
title: cp_library/io/parsable_cls.py
---
