---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/kthelement.py
    title: cp_library/alg/kthelement.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/partition.py
    title: cp_library/alg/partition.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc122_b_insurance_median.test.py
    title: test/arc122_b_insurance_median.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef partition(A, l, r):\n    pivot = A[r]\n    i = l - 1\n    \n\
    \    for j in range(l, r):\n        if A[j] <= pivot:\n            i += 1\n  \
    \          A[i], A[j] = A[j], A[i]\n    \n    A[i + 1], A[r] = A[r], A[i + 1]\n\
    \    return i + 1\n\ndef kth_element(A, k, l=0, r=None):\n    if r is None:\n\
    \        r = len(A) - 1\n    \n    while True:\n        if l == r: return A[k]\n\
    \        pi = partition(A, l, r)\n        \n        if k == pi:\n            return\
    \ A[k]\n        elif k < pi:\n            r = pi - 1\n        else:\n        \
    \    l = pi + 1\n\ndef median(A):\n    A = list(A)\n    n = len(A)\n    m = n\
    \ // 2\n    ret = kth_element(A, m)\n    if n % 2 == 0:\n        return (ret +\
    \ kth_element(A, m-1)) / 2\n    return ret\n"
  code: "from cp_library.alg.kthelement import kth_element\n\ndef median(A):\n   \
    \ A = list(A)\n    n = len(A)\n    m = n // 2\n    ret = kth_element(A, m)\n \
    \   if n % 2 == 0:\n        return (ret + kth_element(A, m-1)) / 2\n    return\
    \ ret"
  dependsOn:
  - cp_library/alg/kthelement.py
  - cp_library/alg/partition.py
  isVerificationFile: false
  path: cp_library/math/median.py
  requiredBy: []
  timestamp: '2024-08-18 15:35:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc122_b_insurance_median.test.py
documentation_of: cp_library/math/median.py
layout: document
redirect_from:
- /library/cp_library/math/median.py
- /library/cp_library/math/median.py.html
title: cp_library/math/median.py
---
