---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/auxiliary_tree_cls.py
    title: cp_library/alg/tree/auxiliary_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_cls.py
    title: cp_library/alg/tree/fast/aux_tree_cls.py
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
  _extendedVerifiedWith:
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
    path: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
    title: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
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
    \ndef sort2(a, b):\n    return (a,b) if a < b else (b,a)\n"
  code: "import cp_library.alg.dp.__header__\n\ndef sort2(a, b):\n    return (a,b)\
    \ if a < b else (b,a)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/dp/sort2_fn.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/fast/aux_tree_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  timestamp: '2025-03-19 01:19:38+07:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/vol/0439_aux_dijkstra.test.py
  - test/aoj/vol/0439_aux_rerooting_dp.test.py
  - test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - test/aoj/grl/grl_5_a_diameter.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/alg/dp/sort2_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/sort2_fn.py
- /library/cp_library/alg/dp/sort2_fn.py.html
title: cp_library/alg/dp/sort2_fn.py
---
