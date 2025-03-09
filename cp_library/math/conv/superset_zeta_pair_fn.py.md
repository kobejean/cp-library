---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/and_conv_fast_fn.py
    title: cp_library/math/conv/and_conv_fast_fn.py
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
    \n\"\"\"\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n  X[0] \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2593\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2593\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X[0]\n\
    \                \u2573          \u2572 \u2571          \u2572     \u2571    \
    \      \n  X[4] \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2593\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2573\u2500\u2593\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2572\u2500\u2500\
    \u2500\u2571\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X[1]\n                           \u2573 \u2573          \u2572 \u2572 \u2571\
    \ \u2571          \n  X[2] \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\
    \u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2573\
    \u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2572\
    \u2500\u2573\u2500\u2571\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X[2]\n                \u2573          \u2571 \u2572          \u2572\
    \ \u2573 \u2573 \u2571          \n  X[6] \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2593\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\
    \u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\
    \u2500\u2573\u2500\u2573\u2500\u2573\u2500\u2593\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X[3]\n                                        \u2573\
    \ \u2573 \u2573 \u2573         \n  X[1] \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2593\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\
    \u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\
    \u2500\u2573\u2500\u2573\u2500\u2573\u2500\u2593\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X[4]\n                \u2573          \u2572 \u2571 \
    \         \u2571 \u2573 \u2573 \u2572          \n  X[5] \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2593\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2593\u2500\u2573\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2593\u2500\u2571\u2500\u2573\u2500\u2572\u2500\u2593\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X[5]\n                           \u2573\
    \ \u2573          \u2571 \u2571 \u2572 \u2572          \n  X[3] \u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2593\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2593\u2500\u2573\u2500\u2593\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2593\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u2593\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X[6]\n                \u2573\
    \          \u2571 \u2572          \u2571     \u2572          \n  X[7] \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2593\u2500\u2593\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2593\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2593\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X[7]\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                     \
    \ Math - Convolution                     \n\"\"\"\n\ndef superset_zeta_pair(A:\
    \ list[int], B: list[int], N: int):\n    Z = len(A)\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z:\n            A[m ^ b] += A[m]\n  \
    \          B[m ^ b] += B[m]\n            m = m+1|b\n    return A\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    \ndef superset_zeta_pair(A: list[int], B: list[int], N: int):\n    Z = len(A)\n\
    \    for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n        \
    \    A[m ^ b] += A[m]\n            B[m ^ b] += B[m]\n            m = m+1|b\n \
    \   return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/conv/superset_zeta_pair_fn.py
  requiredBy:
  - cp_library/math/conv/and_conv_fast_fn.py
  timestamp: '2025-03-09 09:15:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_and_convolution_fast.test.py
documentation_of: cp_library/math/conv/superset_zeta_pair_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/superset_zeta_pair_fn.py
- /library/cp_library/math/conv/superset_zeta_pair_fn.py.html
title: cp_library/math/conv/superset_zeta_pair_fn.py
---
