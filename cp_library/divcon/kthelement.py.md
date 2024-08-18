---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/divcon/partition.py
    title: cp_library/divcon/partition.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/median.py
    title: cp_library/math/median.py
  - icon: ':warning:'
    path: test/arc122_b_insurance_median.text.py
    title: test/arc122_b_insurance_median.text.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\ndef partition(A, l, r):\n    pivot = A[r]\n    i = l - 1\n    \n\
    \    for j in range(l, r):\n        if A[j] <= pivot:\n            i += 1\n  \
    \          A[i], A[j] = A[j], A[i]\n    \n    A[i + 1], A[r] = A[r], A[i + 1]\n\
    \    return i + 1\n\ndef kth_element(A, k, l=0, r=None):\n    if r is None:\n\
    \        r = len(A) - 1\n    \n    while True:\n        if l == r: return A[k]\n\
    \        pi = partition(A, l, r)\n        \n        if k == pi:\n            return\
    \ A[k]\n        elif k < pi:\n            r = pi - 1\n        else:\n        \
    \    l = pi + 1\n"
  code: "from cp_library.divcon.partition import partition\n\ndef kth_element(A, k,\
    \ l=0, r=None):\n    if r is None:\n        r = len(A) - 1\n    \n    while True:\n\
    \        if l == r: return A[k]\n        pi = partition(A, l, r)\n        \n \
    \       if k == pi:\n            return A[k]\n        elif k < pi:\n         \
    \   r = pi - 1\n        else:\n            l = pi + 1\n"
  dependsOn:
  - cp_library/divcon/partition.py
  isVerificationFile: false
  path: cp_library/divcon/kthelement.py
  requiredBy:
  - test/arc122_b_insurance_median.text.py
  - cp_library/math/median.py
  timestamp: '2024-08-18 15:24:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/divcon/kthelement.py
layout: document
redirect_from:
- /library/cp_library/divcon/kthelement.py
- /library/cp_library/divcon/kthelement.py.html
title: cp_library/divcon/kthelement.py
---
