---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/rerooting.py
    title: cp_library/alg/dp/rerooting.py
  - icon: ':x:'
    path: cp_library/alg/tree/centroid_recursive.py
    title: cp_library/alg/tree/centroid_recursive.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting.test.py
    title: test/dp_v_subtree_rerooting.test.py
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
  - cp_library/alg/tree/centroid_recursive.py
  - cp_library/alg/dp/rerooting.py
  timestamp: '2024-08-29 07:36:44+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - test/dp_v_subtree_rerooting.test.py
documentation_of: cp_library/misc/setrecursionlimit.py
layout: document
redirect_from:
- /library/cp_library/misc/setrecursionlimit.py
- /library/cp_library/misc/setrecursionlimit.py.html
title: cp_library/misc/setrecursionlimit.py
---
