---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
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
    \ndef argsort(A: list[int], reverse=False):\n    N = len(A)\n    mask = (1 <<\
    \ (shift := N.bit_length())) - 1\n    indices = [0]*N\n    for i in range(N):\n\
    \        indices[i] = A[i] << shift | i\n    indices.sort(reverse=reverse)\n \
    \   for i in range(N):\n        indices[i] &= mask\n    return indices\n\ndef\
    \ sort_parallel(*L: list, reverse=False):\n    inv, order = [-1]*(N := len(L[0])),\
    \ argsort(L[0], reverse=reverse)\n    for i, idx in enumerate(order): inv[idx]\
    \ = i\n    for j in range(N):\n        i, k = inv[j], order[j]\n        for A\
    \ in L: A[j], A[k] = A[k], A[j] \n        order[i], inv[k] = k, i\n    return\
    \ L\n"
  code: "import cp_library.alg.iter.__header__\nfrom cp_library.alg.iter.argsort_fn\
    \ import argsort\n\ndef sort_parallel(*L: list, reverse=False):\n    inv, order\
    \ = [-1]*(N := len(L[0])), argsort(L[0], reverse=reverse)\n    for i, idx in enumerate(order):\
    \ inv[idx] = i\n    for j in range(N):\n        i, k = inv[j], order[j]\n    \
    \    for A in L: A[j], A[k] = A[k], A[j] \n        order[i], inv[k] = k, i\n \
    \   return L\n"
  dependsOn:
  - cp_library/alg/iter/argsort_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/sort_parallel_fn.py
  requiredBy: []
  timestamp: '2025-01-24 05:21:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sort_parallel_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort_parallel_fn.py
- /library/cp_library/alg/iter/sort_parallel_fn.py.html
title: cp_library/alg/iter/sort_parallel_fn.py
---
