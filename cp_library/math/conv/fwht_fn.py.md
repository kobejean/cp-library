---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/conv/fwht_inv_fn.py
    title: cp_library/math/conv/fwht_inv_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/ixor_conv_fn.py
    title: cp_library/math/conv/ixor_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/fwht_inv_fn.py
    title: cp_library/math/conv/mod/fwht_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/ixor_conv_fn.py
    title: cp_library/math/conv/mod/ixor_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/xor_conv_fn.py
    title: cp_library/math/conv/mod/xor_conv_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/xor_conv_fn.py
    title: cp_library/math/conv/xor_conv_fn.py
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
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2080\n                \u2573          \u2572 \u2571          \u2572     \u2571\
    \          \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\
    \u2500\u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2081\n                           \u2573 \u2573          \u2572\
    \ \u2572 \u2571 \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2082\n                \u2573          \u2571\
    \ \u2572          \u2572 \u2573 \u2573 \u2571          \n    x\u2086 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n             \
    \                           \u2573 \u2573 \u2573 \u2573         \n    x\u2081\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2084\n \
    \               \u2573          \u2572 \u2571          \u2571 \u2573 \u2573 \u2572\
    \          \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\
    \u2500\u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2085\n                           \u2573 \u2573          \u2571\
    \ \u2571 \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2086\n                \u2573          \u2571\
    \ \u2572          \u2571     \u2572          \n    x\u2087 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                      Math - Convolution\
    \                     \n'''\n\ndef fwht(A: list, N: int):\n    Z = len(A)\n  \
    \  for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n          \
    \  a0, a1 = A[m^b], A[m]\n            A[m^b], A[m] = a0+a1, a0-a1\n          \
    \  m = m+1|b\n    return A\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    \ndef fwht(A: list, N: int):\n    Z = len(A)\n    for i in range(N):\n       \
    \ m = b = 1<<i\n        while m < Z:\n            a0, a1 = A[m^b], A[m]\n    \
    \        A[m^b], A[m] = a0+a1, a0-a1\n            m = m+1|b\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/conv/fwht_fn.py
  requiredBy:
  - cp_library/math/conv/mod/fwht_inv_fn.py
  - cp_library/math/conv/mod/xor_conv_fn.py
  - cp_library/math/conv/mod/ixor_conv_fn.py
  - cp_library/math/conv/fwht_inv_fn.py
  - cp_library/math/conv/xor_conv_fn.py
  - cp_library/math/conv/ixor_conv_fn.py
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_xor_convolution.test.py
documentation_of: cp_library/math/conv/fwht_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/fwht_fn.py
- /library/cp_library/math/conv/fwht_fn.py.html
title: cp_library/math/conv/fwht_fn.py
---
