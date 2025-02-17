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
    \ndef argsort(A: list[int], reverse=False):\n    mask, I = (1 << (shift := (N\
    \ := len(A)).bit_length())) - 1, [0]*N\n    if reverse:\n        for i in range(N):\
    \ I[i] = A[i] << shift | (i ^ mask)\n        I.sort(reverse=True)\n        for\
    \ i in range(N): I[i] = (I[i] & mask) & mask\n    else:\n        for i in range(N):\
    \ I[i] = A[i] << shift | i\n        I.sort()\n        for i in range(N): I[i]\
    \ &= mask\n    return I\n\ndef sort_parallel_copies(*L: list, reverse=False):\n\
    \    N, K, order = len(L[0]), len(L), argsort(L[0], reverse)\n    R = tuple([0]*N\
    \ for _ in range(K))\n    for k, Llst in enumerate(L):\n        Rlst = R[k]\n\
    \        for ri, li in enumerate(order):\n            Rlst[ri] = Llst[li]\n  \
    \  return R\n"
  code: "import cp_library.alg.iter.__header__\nfrom cp_library.alg.iter.argsort_fn\
    \ import argsort\n\ndef sort_parallel_copies(*L: list, reverse=False):\n    N,\
    \ K, order = len(L[0]), len(L), argsort(L[0], reverse)\n    R = tuple([0]*N for\
    \ _ in range(K))\n    for k, Llst in enumerate(L):\n        Rlst = R[k]\n    \
    \    for ri, li in enumerate(order):\n            Rlst[ri] = Llst[li]\n    return\
    \ R\n"
  dependsOn:
  - cp_library/alg/iter/argsort_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/sort_parallel_copies_fn.py
  requiredBy: []
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sort_parallel_copies_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort_parallel_copies_fn.py
- /library/cp_library/alg/iter/sort_parallel_copies_fn.py.html
title: cp_library/alg/iter/sort_parallel_copies_fn.py
---
