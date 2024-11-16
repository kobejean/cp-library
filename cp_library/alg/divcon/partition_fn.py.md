---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect_fn.py
    title: cp_library/alg/divcon/qselect_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/median_fn.py
    title: cp_library/math/median_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc122_b_insurance_median.test.py
    title: test/arc122_b_insurance_median.test.py
  - icon: ':heavy_check_mark:'
    path: test/arc182_d_increment_decrement_again_qselect.test.py
    title: test/arc182_d_increment_decrement_again_qselect.test.py
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
  timestamp: '2024-11-16 11:24:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc182_d_increment_decrement_again_qselect.test.py
  - test/arc122_b_insurance_median.test.py
documentation_of: cp_library/alg/divcon/partition_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/partition_fn.py
- /library/cp_library/alg/divcon/partition_fn.py.html
title: cp_library/alg/divcon/partition_fn.py
---
