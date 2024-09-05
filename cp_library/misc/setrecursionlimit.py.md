---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/rerooting_recursive_cls.py
    title: cp_library/alg/dp/rerooting_recursive_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/tarjan_articulation_points_fn.py
    title: cp_library/alg/graph/tarjan_articulation_points_fn.py
  - icon: ':x:'
    path: cp_library/alg/tree/find_centroid_recursive_fn.py
    title: cp_library/alg/tree/find_centroid_recursive_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_recursive_cls.py
    title: cp_library/alg/tree/lca_table_recursive_cls.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_recursive.test.py
    title: test/grl_5_c_lca_table_recursive.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: 'import sys

    sys.setrecursionlimit(10**6)

    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

    '
  code: 'import sys

    sys.setrecursionlimit(10**6)

    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

    '
  dependsOn: []
  isVerificationFile: false
  path: cp_library/misc/setrecursionlimit.py
  requiredBy:
  - cp_library/alg/dp/rerooting_recursive_cls.py
  - cp_library/alg/tree/lca_table_recursive_cls.py
  - cp_library/alg/tree/find_centroid_recursive_fn.py
  - cp_library/alg/graph/edmonds_fn.py
  - cp_library/alg/graph/tarjan_articulation_points_fn.py
  timestamp: '2024-09-05 11:18:10+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/grl_5_c_lca_table_recursive.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/misc/setrecursionlimit.py
layout: document
redirect_from:
- /library/cp_library/misc/setrecursionlimit.py
- /library/cp_library/misc/setrecursionlimit.py.html
title: cp_library/misc/setrecursionlimit.py
---
