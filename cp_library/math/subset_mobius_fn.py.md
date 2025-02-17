---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/math/subset_conv_fn.py
    title: cp_library/math/subset_conv_fn.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library-checker/set-power-series/subset_convolution.test.py
    title: test/library-checker/set-power-series/subset_convolution.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef subset_mobius(A, N, block=5):\n    for i in range(min(block,N)):\n     \
    \   for mask in range(bit := 1<<i, 1<<N):\n            if mask & bit:\n      \
    \          A[mask] -= A[mask ^ bit]\n    for i in range(block,N):\n        for\
    \ base in range(bit := 1<<i, 1<<N, bit << 1):\n            for mask in range(base,\
    \ base+bit):\n                A[mask] -= A[mask ^ bit]\n    return A\n"
  code: "import cp_library.math.__header__\n\ndef subset_mobius(A, N, block=5):\n\
    \    for i in range(min(block,N)):\n        for mask in range(bit := 1<<i, 1<<N):\n\
    \            if mask & bit:\n                A[mask] -= A[mask ^ bit]\n    for\
    \ i in range(block,N):\n        for base in range(bit := 1<<i, 1<<N, bit << 1):\n\
    \            for mask in range(base, base+bit):\n                A[mask] -= A[mask\
    \ ^ bit]\n    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/subset_mobius_fn.py
  requiredBy:
  - cp_library/math/subset_conv_fn.py
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution.test.py
documentation_of: cp_library/math/subset_mobius_fn.py
layout: document
redirect_from:
- /library/cp_library/math/subset_mobius_fn.py
- /library/cp_library/math/subset_mobius_fn.py.html
title: cp_library/math/subset_mobius_fn.py
---
