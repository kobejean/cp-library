---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/divcon/qselect_fn.py
    title: cp_library/alg/divcon/qselect_fn.py
  - icon: ':warning:'
    path: cp_library/math/median_fn.py
    title: cp_library/math/median_fn.py
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
    \ndef partition(A, l, r, pi) -> int:\n    '''Partition subarray [l,r)'''\n   \
    \ r -= 1\n    A[pi], A[r] = A[r], A[pi]\n    pi = l\n    for j in range(l, r):\n\
    \        if A[j] <= A[r]:\n            A[pi], A[j] = A[j], A[pi]\n           \
    \ pi += 1\n    A[pi], A[r] = A[r], A[pi]\n    return pi\n"
  code: "import cp_library.alg.divcon.__header__\n\ndef partition(A, l, r, pi) ->\
    \ int:\n    '''Partition subarray [l,r)'''\n    r -= 1\n    A[pi], A[r] = A[r],\
    \ A[pi]\n    pi = l\n    for j in range(l, r):\n        if A[j] <= A[r]:\n   \
    \         A[pi], A[j] = A[j], A[pi]\n            pi += 1\n    A[pi], A[r] = A[r],\
    \ A[pi]\n    return pi\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/divcon/partition_fn.py
  requiredBy:
  - cp_library/math/median_fn.py
  - cp_library/alg/divcon/qselect_fn.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/divcon/partition_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/partition_fn.py
- /library/cp_library/alg/divcon/partition_fn.py.html
title: cp_library/alg/divcon/partition_fn.py
---
