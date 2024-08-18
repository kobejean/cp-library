---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/kthelement.py
    title: cp_library/alg/kthelement.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/median.py
    title: cp_library/math/median.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc122_b_insurance_median.test.py
    title: test/arc122_b_insurance_median.test.py
  - icon: ':heavy_check_mark:'
    path: test/arc182_increment_decrement_again_kthelement.test.py
    title: test/arc182_increment_decrement_again_kthelement.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "import random\n\ndef partition(A, l, r):\n    pi = random.randint(l,\
    \ r)\n    A[pi], A[r] = A[r], A[pi]\n    pivot = A[r]\n    i = l - 1\n    \n \
    \   for j in range(l, r):\n        if A[j] <= pivot:\n            i += 1\n   \
    \         A[i], A[j] = A[j], A[i]\n    \n    A[i + 1], A[r] = A[r], A[i + 1]\n\
    \    return i + 1\n"
  code: "import random\n\ndef partition(A, l, r):\n    pi = random.randint(l, r)\n\
    \    A[pi], A[r] = A[r], A[pi]\n    pivot = A[r]\n    i = l - 1\n    \n    for\
    \ j in range(l, r):\n        if A[j] <= pivot:\n            i += 1\n         \
    \   A[i], A[j] = A[j], A[i]\n    \n    A[i + 1], A[r] = A[r], A[i + 1]\n    return\
    \ i + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/partition.py
  requiredBy:
  - cp_library/alg/kthelement.py
  - cp_library/math/median.py
  timestamp: '2024-08-18 16:01:16+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc182_increment_decrement_again_kthelement.test.py
  - test/arc122_b_insurance_median.test.py
documentation_of: cp_library/alg/partition.py
layout: document
redirect_from:
- /library/cp_library/alg/partition.py
- /library/cp_library/alg/partition.py.html
title: cp_library/alg/partition.py
---
