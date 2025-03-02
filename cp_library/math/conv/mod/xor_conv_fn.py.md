---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/fwht_fn.py
    title: cp_library/math/conv/fwht_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/fwht_pair_fn.py
    title: cp_library/math/conv/fwht_pair_fn.py
  _extendedRequiredBy: []
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
    \ = a0+a1, a0-a1, b0+b1, b0-b1\n            m = m+1|b\n    return A, B\n\ndef\
    \ fwht(A: list, N: int):\n    Z = len(A)\n    for i in range(N):\n        m =\
    \ b = 1<<i\n        while m < Z:\n            a0, a1 = A[m^b], A[m]\n        \
    \    A[m^b], A[m] = a0+a1, a0-a1\n            m = m+1|b\n    return A\n\ndef xor_conv(A:\
    \ list, B: list, N: int, mod: int):\n    assert len(A) == len(B)\n    fwht_pair(A,\
    \ B, N)\n    for i, b in enumerate(B): A[i] = A[i]%mod * (b%mod) % mod\n    fwht(A,\
    \ N)\n    inv = pow(len(A), -1, mod)\n    for i, a in enumerate(A): A[i] = a%mod\
    \ * inv%mod\n    return A\n"
  code: "import cp_library.math.conv.mod.__header__\nfrom cp_library.math.conv.fwht_pair_fn\
    \ import fwht_pair\nfrom cp_library.math.conv.fwht_fn import fwht\n\ndef xor_conv(A:\
    \ list, B: list, N: int, mod: int):\n    assert len(A) == len(B)\n    fwht_pair(A,\
    \ B, N)\n    for i, b in enumerate(B): A[i] = A[i]%mod * (b%mod) % mod\n    fwht(A,\
    \ N)\n    inv = pow(len(A), -1, mod)\n    for i, a in enumerate(A): A[i] = a%mod\
    \ * inv%mod\n    return A\n"
  dependsOn:
  - cp_library/math/conv/fwht_pair_fn.py
  - cp_library/math/conv/fwht_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/mod/xor_conv_fn.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_xor_convolution.test.py
documentation_of: cp_library/math/conv/mod/xor_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/mod/xor_conv_fn.py
- /library/cp_library/math/conv/mod/xor_conv_fn.py.html
title: cp_library/math/conv/mod/xor_conv_fn.py
---
