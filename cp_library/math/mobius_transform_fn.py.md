---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_convolution_fn.py
    title: cp_library/math/subset_convolution_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef mobius_transform(A, N):\n    for i in range(N):\n        bit\
    \ = 1 << i\n        for mask in range(1 << N):\n            if mask & bit:\n \
    \               A[mask] -= A[mask ^ bit]\n    return A\n"
  code: "\ndef mobius_transform(A, N):\n    for i in range(N):\n        bit = 1 <<\
    \ i\n        for mask in range(1 << N):\n            if mask & bit:\n        \
    \        A[mask] -= A[mask ^ bit]\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mobius_transform_fn.py
  requiredBy:
  - cp_library/math/subset_convolution_fn.py
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
documentation_of: cp_library/math/mobius_transform_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mobius_transform_fn.py
- /library/cp_library/math/mobius_transform_fn.py.html
title: cp_library/math/mobius_transform_fn.py
---
