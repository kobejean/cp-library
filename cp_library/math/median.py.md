---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_pivot.py
    title: cp_library/alg/divcon/partition_pivot.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect.py
    title: cp_library/alg/divcon/qselect.py
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
  bundledCode: "import random\n\ndef partition(A, l, r, pi):\n    '''Partition subarray\
    \ [l,r)'''\n    r -= 1\n    A[pi], A[r] = A[r], A[pi]\n    pi = l\n    for j in\
    \ range(l, r):\n        if A[j] <= A[r]:\n            A[pi], A[j] = A[j], A[pi]\n\
    \            pi += 1\n    A[pi], A[r] = A[r], A[pi]\n    return pi\n\ndef kth_element(A,\
    \ k, l=0, r=None):\n    '''Find kth element in subarray [l,r)'''\n    if r is\
    \ None: r = len(A)\n    while True:\n        if l == r-1: return A[k]\n      \
    \  pi = partition(A, l, r, random.randint(l, r-1))\n        if k == pi:\n    \
    \        return A[k]\n        elif k < pi:\n            r = pi\n        else:\n\
    \            l = pi + 1\n\ndef median(A):\n    n = len(A)\n    m = n // 2\n  \
    \  ret = kth_element(A, m)\n    if n % 2 == 0:\n        return (ret + kth_element(A,\
    \ m-1)) / 2\n    return ret\n"
  code: "from cp_library.alg.divcon.qselect import kth_element\n\ndef median(A):\n\
    \    n = len(A)\n    m = n // 2\n    ret = kth_element(A, m)\n    if n % 2 ==\
    \ 0:\n        return (ret + kth_element(A, m-1)) / 2\n    return ret"
  dependsOn:
  - cp_library/alg/divcon/qselect.py
  - cp_library/alg/divcon/partition_pivot.py
  isVerificationFile: false
  path: cp_library/math/median.py
  requiredBy: []
  timestamp: '2024-08-29 01:33:12+09:00'
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
