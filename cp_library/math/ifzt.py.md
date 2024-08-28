---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_convolution.py
    title: cp_library/math/subset_convolution.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef ifzt(A):\n    N = len(A).bit_length()-1\n\n    for i in range(N):\n\
    \        bit = 1 << i\n        for mask in range(1 << N):\n            if mask\
    \ & bit:\n                A[mask] -= A[mask ^ bit]\n\n    return A\n"
  code: "\ndef ifzt(A):\n    N = len(A).bit_length()-1\n\n    for i in range(N):\n\
    \        bit = 1 << i\n        for mask in range(1 << N):\n            if mask\
    \ & bit:\n                A[mask] -= A[mask ^ bit]\n\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/ifzt.py
  requiredBy:
  - cp_library/math/subset_convolution.py
  timestamp: '2024-08-29 07:36:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
documentation_of: cp_library/math/ifzt.py
layout: document
redirect_from:
- /library/cp_library/math/ifzt.py
- /library/cp_library/math/ifzt.py.html
title: cp_library/math/ifzt.py
---
