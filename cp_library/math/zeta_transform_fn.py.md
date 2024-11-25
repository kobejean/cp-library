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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef zeta_transform(A, N, block=5):\n    for i in range(min(block,N)):\n    \
    \    for mask in range(bit := 1<<i, 1<<N):\n            if mask & bit:\n     \
    \           A[mask] += A[mask ^ bit]\n    for i in range(block,N):\n        for\
    \ base in range(bit := 1<<i, 1<<N, bit << 1):\n            for mask in range(base,\
    \ base+bit):\n                A[mask] += A[mask ^ bit]\n    return A\n"
  code: "import cp_library.math.__header__\n\ndef zeta_transform(A, N, block=5):\n\
    \    for i in range(min(block,N)):\n        for mask in range(bit := 1<<i, 1<<N):\n\
    \            if mask & bit:\n                A[mask] += A[mask ^ bit]\n    for\
    \ i in range(block,N):\n        for base in range(bit := 1<<i, 1<<N, bit << 1):\n\
    \            for mask in range(base, base+bit):\n                A[mask] += A[mask\
    \ ^ bit]\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/zeta_transform_fn.py
  requiredBy:
  - cp_library/math/subset_convolution_fn.py
  timestamp: '2024-11-25 13:28:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
documentation_of: cp_library/math/zeta_transform_fn.py
layout: document
redirect_from:
- /library/cp_library/math/zeta_transform_fn.py
- /library/cp_library/math/zeta_transform_fn.py.html
title: cp_library/math/zeta_transform_fn.py
---
