---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from itertools import groupby\nfrom operator import itemgetter\n\ndef sort_buckets(A,\
    \ N, key=0):\n    if isinstance(key,int):\n        key = itemgetter(key)\n   \
    \ A.sort(key=key)\n    B = [[] for _ in range(N)]\n    for k,g in groupby(A, key=key):\n\
    \        B[k] = list(g)\n    return B\n    \n"
  code: "import cp_library.alg.iter.__header__\nfrom itertools import groupby\nfrom\
    \ operator import itemgetter\n\ndef sort_buckets(A, N, key=0):\n    if isinstance(key,int):\n\
    \        key = itemgetter(key)\n    A.sort(key=key)\n    B = [[] for _ in range(N)]\n\
    \    for k,g in groupby(A, key=key):\n        B[k] = list(g)\n    return B\n \
    \   "
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/sort_buckets_fn.py
  requiredBy: []
  timestamp: '2024-12-21 20:47:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sort_buckets_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort_buckets_fn.py
- /library/cp_library/alg/iter/sort_buckets_fn.py.html
title: cp_library/alg/iter/sort_buckets_fn.py
---
