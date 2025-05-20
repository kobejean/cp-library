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
    path: test/atcoder/arc/arc122_b_insurance_median.test.py
    title: test/atcoder/arc/arc122_b_insurance_median.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
    title: test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
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
    \ndef median_of_three(A, l, r):\n    '''Select pivot as median of first, middle,\
    \ and last elements'''\n    if r - l < 3: return l\n    mid = (l+r) >> 1\n   \
    \ if A[mid] < A[l]:\n        A[l], A[mid] = A[mid], A[l]\n    if A[r-1] < A[mid]:\n\
    \        A[mid], A[r-1] = A[r-1], A[mid]\n        if A[mid] < A[l]:\n        \
    \    A[l], A[mid] = A[mid], A[l]\n    return mid\n"
  code: "import cp_library.alg.divcon.__header__\n\ndef median_of_three(A, l, r):\n\
    \    '''Select pivot as median of first, middle, and last elements'''\n    if\
    \ r - l < 3: return l\n    mid = (l+r) >> 1\n    if A[mid] < A[l]:\n        A[l],\
    \ A[mid] = A[mid], A[l]\n    if A[r-1] < A[mid]:\n        A[mid], A[r-1] = A[r-1],\
    \ A[mid]\n        if A[mid] < A[l]:\n            A[l], A[mid] = A[mid], A[l]\n\
    \    return mid"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/divcon/median_of_three_fn.py
  requiredBy:
  - cp_library/math/median_fn.py
  - cp_library/alg/divcon/qselect_fn.py
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
  - test/atcoder/arc/arc122_b_insurance_median.test.py
documentation_of: cp_library/alg/divcon/median_of_three_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/median_of_three_fn.py
- /library/cp_library/alg/divcon/median_of_three_fn.py.html
title: cp_library/alg/divcon/median_of_three_fn.py
---
