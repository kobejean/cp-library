---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/alg/dp/rerooting_recursive_cls.py
    title: cp_library/alg/dp/rerooting_recursive_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  - icon: ':warning:'
    path: cp_library/alg/tree/find_centroid_recursive_fn.py
    title: cp_library/alg/tree/find_centroid_recursive_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_recursive_cls.py
    title: cp_library/alg/tree/lca_table_recursive_cls.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_recursive.test.py
    title: test/grl_5_c_lca_table_recursive.test.py
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
    \nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n"
  code: 'import cp_library.misc.__header__


    import sys

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
  timestamp: '2024-12-17 03:19:43+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/grl_5_c_lca_table_recursive.test.py
documentation_of: cp_library/misc/setrecursionlimit.py
layout: document
redirect_from:
- /library/cp_library/misc/setrecursionlimit.py
- /library/cp_library/misc/setrecursionlimit.py.html
title: cp_library/misc/setrecursionlimit.py
---
