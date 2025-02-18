---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/or_conv_fn.py
    title: cp_library/math/or_conv_fn.py
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
    \ndef subset_zeta(A: list[int], N: int, Z: int = None):\n    Z = 1 << N if Z is\
    \ None else Z\n    for i in range(N):\n        m = b = 1<<i\n        while m <\
    \ Z:\n            A[m] += A[m^b]\n            m = m+1|b\n    return A\n"
  code: "import cp_library.math.__header__\n\ndef subset_zeta(A: list[int], N: int,\
    \ Z: int = None):\n    Z = 1 << N if Z is None else Z\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z:\n            A[m] += A[m^b]\n    \
    \        m = m+1|b\n    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/subset_zeta_fn.py
  requiredBy:
  - cp_library/math/or_conv_fn.py
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/subset_zeta_fn.py
layout: document
redirect_from:
- /library/cp_library/math/subset_zeta_fn.py
- /library/cp_library/math/subset_zeta_fn.py.html
title: cp_library/math/subset_zeta_fn.py
---
