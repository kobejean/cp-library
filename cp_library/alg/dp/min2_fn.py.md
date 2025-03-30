---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_base_cls.py
    title: cp_library/alg/tree/fast/aux_tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_cls.py
    title: cp_library/alg/tree/fast/aux_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
    title: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_b_cut_edges_snippet.test.py
    title: test/aoj/grl/grl_3_b_cut_edges_snippet.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_a_diameter.test.py
    title: test/aoj/grl/grl_5_a_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
    title: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_dijkstra.test.py
    title: test/aoj/vol/0439_aux_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
    title: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/staticrmq.test.py
    title: test/library-checker/data-structure/staticrmq.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/staticrmq_general.test.py
    title: test/library-checker/data-structure/staticrmq_general.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/jump_on_tree.test.py
    title: test/library-checker/tree/jump_on_tree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/lca.test.py
    title: test/library-checker/tree/lca.test.py
  - icon: ':heavy_check_mark:'
    path: test/yukicoder/3407.test.py
    title: test/yukicoder/3407.test.py
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
    \ndef min2(a, b):\n    return a if a < b else b\n"
  code: "import cp_library.alg.dp.__header__\n\ndef min2(a, b):\n    return a if a\
    \ < b else b"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/dp/min2_fn.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/fast/aux_tree_base_cls.py
  - cp_library/alg/tree/fast/aux_tree_cls.py
  - cp_library/alg/tree/fast/aux_tree_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/ds/min_sparse_table_cls.py
  timestamp: '2025-03-30 20:17:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/vol/0439_aux_dijkstra.test.py
  - test/aoj/vol/0439_aux_rerooting_dp.test.py
  - test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - test/aoj/grl/grl_3_b_cut_edges_snippet.test.py
  - test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - test/aoj/grl/grl_5_a_diameter.test.py
  - test/library-checker/tree/lca.test.py
  - test/library-checker/tree/jump_on_tree.test.py
  - test/library-checker/data-structure/staticrmq_general.test.py
  - test/library-checker/data-structure/staticrmq.test.py
  - test/yukicoder/3407.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/alg/dp/min2_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/min2_fn.py
- /library/cp_library/alg/dp/min2_fn.py.html
title: cp_library/alg/dp/min2_fn.py
---
