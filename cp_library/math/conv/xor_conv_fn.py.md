---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/fwht_fn.py
    title: cp_library/math/conv/fwht_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/fwht_inv_fn.py
    title: cp_library/math/conv/fwht_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/fwht_pair_fn.py
    title: cp_library/math/conv/fwht_pair_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/ixor_conv_fn.py
    title: cp_library/math/conv/ixor_conv_fn.py
  _extendedRequiredBy: []
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
    \  m = m+1|b\n    return A\n\ndef fwht_inv(A: list, N: int):\n    fwht(A, N)\n\
    \    for i, a in enumerate(A): A[i] = a >> N\n    return A\n\ndef fwht_pair(A:\
    \ list[int], B: list[int], N: int):\n    Z = len(A)\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z:\n            a0, a1, b0, b1 = A[m^b],\
    \ A[m], B[m^b], B[m]\n            A[m^b], A[m], B[m^b], B[m] = a0+a1, a0-a1, b0+b1,\
    \ b0-b1\n            m = m+1|b\n    return A, B\n\ndef ixor_conv(A: list, B: list,\
    \ N: int):\n    assert len(A) == len(B)\n    fwht_pair(A, B, N)\n    for i, b\
    \ in enumerate(B): A[i] *= b\n    fwht_inv(A, N)\n    return A\n\ndef xor_conv(A:\
    \ list, B: list, N: int, mod: int):\n    return ixor_conv(A[:], B[:], N, mod)\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    from cp_library.math.conv.ixor_conv_fn import ixor_conv\n\ndef xor_conv(A: list,\
    \ B: list, N: int, mod: int):\n    return ixor_conv(A[:], B[:], N, mod)\n"
  dependsOn:
  - cp_library/math/conv/ixor_conv_fn.py
  - cp_library/math/conv/fwht_inv_fn.py
  - cp_library/math/conv/fwht_pair_fn.py
  - cp_library/math/conv/fwht_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/xor_conv_fn.py
  requiredBy: []
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/conv/xor_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/xor_conv_fn.py
- /library/cp_library/math/conv/xor_conv_fn.py.html
title: cp_library/math/conv/xor_conv_fn.py
---
