---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/xor_conv_fn.py
    title: cp_library/math/conv/mod/xor_conv_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/bitwise_xor_convolution.test.py
    title: test/library-checker/convolution/bitwise_xor_convolution.test.py
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
    \ndef fwht_pair(A: list[int], B: list[int], N: int):\n    Z = len(A)\n    for\
    \ i in range(N):\n        m = b = 1<<i\n        while m < Z:\n            a0,\
    \ a1, b0, b1 = A[m^b], A[m], B[m^b], B[m]\n            A[m^b], A[m], B[m^b], B[m]\
    \ = a0+a1, a0-a1, b0+b1, b0-b1\n            m = m+1|b\n    return A, B\n"
  code: "import cp_library.math.conv.__header__\n\ndef fwht_pair(A: list[int], B:\
    \ list[int], N: int):\n    Z = len(A)\n    for i in range(N):\n        m = b =\
    \ 1<<i\n        while m < Z:\n            a0, a1, b0, b1 = A[m^b], A[m], B[m^b],\
    \ B[m]\n            A[m^b], A[m], B[m^b], B[m] = a0+a1, a0-a1, b0+b1, b0-b1\n\
    \            m = m+1|b\n    return A, B\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/conv/fwht_pair_fn.py
  requiredBy:
  - cp_library/math/conv/mod/xor_conv_fn.py
  timestamp: '2025-03-03 00:10:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_xor_convolution.test.py
documentation_of: cp_library/math/conv/fwht_pair_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/fwht_pair_fn.py
- /library/cp_library/math/conv/fwht_pair_fn.py.html
title: cp_library/math/conv/fwht_pair_fn.py
---
