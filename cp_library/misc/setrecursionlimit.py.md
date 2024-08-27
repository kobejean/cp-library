---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/alg/tree/centroid_recursive.py
    title: cp_library/alg/tree/centroid_recursive.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
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
  timestamp: '2024-08-28 02:08:48+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
documentation_of: cp_library/misc/setrecursionlimit.py
layout: document
redirect_from:
- /library/cp_library/misc/setrecursionlimit.py
- /library/cp_library/misc/setrecursionlimit.py.html
title: cp_library/misc/setrecursionlimit.py
---
