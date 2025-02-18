---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/and_conv_fast_fn.py
    title: cp_library/math/and_conv_fast_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
    title: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
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
    \ndef superset_mobius(A, N: int, Z: int = None):\n    Z = 1 << N if Z is None\
    \ else Z\n    for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n\
    \            A[m ^ b] -= A[m]\n            m = m+1|b\n    return A\n"
  code: "import cp_library.math.__header__\n\ndef superset_mobius(A, N: int, Z: int\
    \ = None):\n    Z = 1 << N if Z is None else Z\n    for i in range(N):\n     \
    \   m = b = 1<<i\n        while m < Z:\n            A[m ^ b] -= A[m]\n       \
    \     m = m+1|b\n    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/superset_mobius_fn.py
  requiredBy:
  - cp_library/math/and_conv_fast_fn.py
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_and_convolution_fast.test.py
documentation_of: cp_library/math/superset_mobius_fn.py
layout: document
redirect_from:
- /library/cp_library/math/superset_mobius_fn.py
- /library/cp_library/math/superset_mobius_fn.py.html
title: cp_library/math/superset_mobius_fn.py
---
