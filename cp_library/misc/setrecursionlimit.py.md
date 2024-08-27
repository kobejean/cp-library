---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/centroid.py
    title: cp_library/alg/tree/centroid.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
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
  - cp_library/alg/tree/centroid.py
  timestamp: '2024-08-27 19:11:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/misc/setrecursionlimit.py
layout: document
redirect_from:
- /library/cp_library/misc/setrecursionlimit.py
- /library/cp_library/misc/setrecursionlimit.py.html
title: cp_library/misc/setrecursionlimit.py
---
