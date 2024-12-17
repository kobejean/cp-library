---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/mod/subset_convolution_fn.py
    title: cp_library/math/mod/subset_convolution_fn.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef zeta_transform(A, N, mod, block=5):\n    for i in range(min(block,N)):\n\
    \        for mask in range(bit := 1<<i, 1<<N):\n            if mask & bit:\n \
    \               A[mask] = (A[mask] + A[mask ^ bit]) % mod\n    for i in range(block,N):\n\
    \        for base in range(bit := 1<<i, 1<<N, bit << 1):\n            for mask\
    \ in range(base, base+bit):\n                A[mask] = (A[mask] + A[mask ^ bit])\
    \ % mod\n    return A\n"
  code: "import cp_library.math.mod.__header__\n\ndef zeta_transform(A, N, mod, block=5):\n\
    \    for i in range(min(block,N)):\n        for mask in range(bit := 1<<i, 1<<N):\n\
    \            if mask & bit:\n                A[mask] = (A[mask] + A[mask ^ bit])\
    \ % mod\n    for i in range(block,N):\n        for base in range(bit := 1<<i,\
    \ 1<<N, bit << 1):\n            for mask in range(base, base+bit):\n         \
    \       A[mask] = (A[mask] + A[mask ^ bit]) % mod\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/zeta_transform_fn.py
  requiredBy:
  - cp_library/math/mod/subset_convolution_fn.py
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/zeta_transform_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mod/zeta_transform_fn.py
- /library/cp_library/math/mod/zeta_transform_fn.py.html
title: cp_library/math/mod/zeta_transform_fn.py
---
