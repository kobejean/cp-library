---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
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
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc122_b_insurance_median.test.py
    title: test/arc122_b_insurance_median.test.py
  - icon: ':heavy_check_mark:'
    path: test/arc168_c_swap_characters_mint_comb.test.py
    title: test/arc168_c_swap_characters_mint_comb.test.py
  - icon: ':heavy_check_mark:'
    path: test/arc182_d_increment_decrement_again_qselect.test.py
    title: test/arc182_d_increment_decrement_again_qselect.test.py
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
    path: test/dp_z_cht_monotone_add_max.test.py
    title: test/dp_z_cht_monotone_add_max.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_z_cht_monotone_add_min.test.py
    title: test/dp_z_cht_monotone_add_min.test.py
  - icon: ':heavy_check_mark:'
    path: test/dsl_2_a_segtree.test.py
    title: test/dsl_2_a_segtree.test.py
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
    path: test/grl_5_c_lca_table_recursive.test.py
    title: test/grl_5_c_lca_table_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_modmat.test.py
    title: test/pow_of_matrix_modmat.test.py
  - icon: ':heavy_check_mark:'
    path: test/unionfind.test.py
    title: test/unionfind.test.py
  - icon: ':heavy_check_mark:'
    path: test/unionfind_with_potential.test.py
    title: test/unionfind_with_potential.test.py
  - icon: ':heavy_check_mark:'
    path: test/unionfind_with_potential_non_commutative_group.test.py
    title: test/unionfind_with_potential_non_commutative_group.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "\ndef read(shift=0, base=10):\n    return [int(s, base) + shift for\
    \ s in  input().split()]\n"
  code: "\ndef read(shift=0, base=10):\n    return [int(s, base) + shift for s in\
    \  input().split()]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/read_int_fn.py
  requiredBy:
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/io/read_graph_weighted_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/io/read_graph_fn.py
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/grl_2_a_kruskal_sort.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/dp_z_cht_monotone_add_max.test.py
  - test/unionfind.test.py
  - test/grl_5_c_lca_table_iterative.test.py
  - test/unionfind_with_potential.test.py
  - test/grl_5_c_lca_table_recursive.test.py
  - test/dp_z_cht_monotone_add_min.test.py
  - test/dsl_2_c_kdtree.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - test/arc122_b_insurance_median.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/arc168_c_swap_characters_mint_comb.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/arc182_d_increment_decrement_again_qselect.test.py
  - test/dsl_2_a_segtree.test.py
  - test/pow_of_matrix_modmat.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/unionfind_with_potential_non_commutative_group.test.py
  - test/grl_2_a_kruskal_heap.test.py
  - test/grl_1_c_floyd_warshall.test.py
documentation_of: cp_library/io/read_int_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_int_fn.py
- /library/cp_library/io/read_int_fn.py.html
title: cp_library/io/read_int_fn.py
---
