---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_pivot.py
    title: cp_library/alg/divcon/partition_pivot.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/median.py
    title: cp_library/math/median.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc122_b_insurance_median.test.py
    title: test/arc122_b_insurance_median.test.py
  - icon: ':heavy_check_mark:'
    path: test/arc182_increment_decrement_again_qselect.test.py
    title: test/arc182_increment_decrement_again_qselect.test.py
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
    \            l = pi + 1\n"
  code: "import random\nfrom cp_library.alg.divcon.partition_pivot import partition\n\
    \ndef kth_element(A, k, l=0, r=None):\n    '''Find kth element in subarray [l,r)'''\n\
    \    if r is None: r = len(A)\n    while True:\n        if l == r-1: return A[k]\n\
    \        pi = partition(A, l, r, random.randint(l, r-1))\n        if k == pi:\n\
    \            return A[k]\n        elif k < pi:\n            r = pi\n        else:\n\
    \            l = pi + 1\n"
  dependsOn:
  - cp_library/alg/divcon/partition_pivot.py
  isVerificationFile: false
  path: cp_library/alg/divcon/qselect.py
  requiredBy:
  - cp_library/math/median.py
  timestamp: '2024-08-27 19:11:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc122_b_insurance_median.test.py
  - test/arc182_increment_decrement_again_qselect.test.py
documentation_of: cp_library/alg/divcon/qselect.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/qselect.py
- /library/cp_library/alg/divcon/qselect.py.html
title: cp_library/alg/divcon/qselect.py
---
