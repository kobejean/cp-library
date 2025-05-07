---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/median_of_three_fn.py
    title: cp_library/alg/divcon/median_of_three_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_fn.py
    title: cp_library/alg/divcon/partition_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect_fn.py
    title: cp_library/alg/divcon/qselect_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc122_b_insurance_median.test.py
    title: test/atcoder/arc/arc122_b_insurance_median.test.py
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
    \n\ndef median_of_three(A, l, r):\n    '''Select pivot as median of first, middle,\
    \ and last elements'''\n    if r - l < 3: return l\n    mid = (l+r) >> 1\n   \
    \ if A[mid] < A[l]:\n        A[l], A[mid] = A[mid], A[l]\n    if A[r-1] < A[mid]:\n\
    \        A[mid], A[r-1] = A[r-1], A[mid]\n        if A[mid] < A[l]:\n        \
    \    A[l], A[mid] = A[mid], A[l]\n    return mid\n\ndef partition(A, l, r, p)\
    \ -> int:\n    '''Partition subarray [l,r)'''\n    A[p], A[r], p = A[r := r-1],\
    \ A[p], l\n    for j in range(l, r):\n        if A[j] <= A[r]: A[p], A[j], p =\
    \ A[j], A[p], p+1\n    A[p], A[r] = A[r], A[p]\n    return p\n\ndef qselect(A,\
    \ k, l=0, r=None):\n    '''Find kth element in subarray [l,r)'''\n    if r is\
    \ None: r = len(A)\n    while l != r-1:\n        if k < (p := partition(A, l,\
    \ r, median_of_three(A,l,r))): r = p\n        elif k > p: l = p+1\n        else:\
    \ return A[k]\n    return A[k]\n\n\ndef median(A):\n    med = qselect(A, M :=\
    \ (N := len(A)) >> 1)\n    return med if N&1 else (med + qselect(A, M-1)) >> 1\n"
  code: "import cp_library.__header__\nfrom cp_library.alg.divcon.qselect_fn import\
    \ qselect\nimport cp_library.math.__header__\n\ndef median(A):\n    med = qselect(A,\
    \ M := (N := len(A)) >> 1)\n    return med if N&1 else (med + qselect(A, M-1))\
    \ >> 1\n"
  dependsOn:
  - cp_library/alg/divcon/qselect_fn.py
  - cp_library/alg/divcon/median_of_three_fn.py
  - cp_library/alg/divcon/partition_fn.py
  isVerificationFile: false
  path: cp_library/math/median_fn.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/arc/arc122_b_insurance_median.test.py
documentation_of: cp_library/math/median_fn.py
layout: document
redirect_from:
- /library/cp_library/math/median_fn.py
- /library/cp_library/math/median_fn.py.html
title: cp_library/math/median_fn.py
---
