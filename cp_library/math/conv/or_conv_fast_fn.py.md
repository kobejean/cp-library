---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_mobius_fn.py
    title: cp_library/math/conv/subset_mobius_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/subset_zeta_fn.py
    title: cp_library/math/conv/subset_zeta_fn.py
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
    \ Math - Convolution                     \n\"\"\"\n\ndef subset_zeta(A: list[int],\
    \ N: int):\n    Z = len(A)\n    for i in range(N):\n        m = b = 1<<i\n   \
    \     while m < Z:\n            A[m] += A[m^b]\n            m = m+1|b\n    return\
    \ A\n\ndef subset_mobius(A: list[int], N: int):\n    Z = len(A)\n    for i in\
    \ range(N):\n        m = b = 1<<i\n        while m < Z:\n            A[m] -= A[m^b]\n\
    \            m = m+1|b\n    return A\n\ndef or_conv(A: list[int], B: list[int],\
    \ N: int) -> list[int]:\n    assert len(A) == len(B)\n    subset_zeta(A, N), subset_zeta(B,\
    \ N)\n    for i, b in enumerate(B): A[i] *= b\n    return subset_mobius(A, N)\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    from cp_library.math.conv.subset_zeta_fn import subset_zeta\nfrom cp_library.math.conv.subset_mobius_fn\
    \ import subset_mobius\n\ndef or_conv(A: list[int], B: list[int], N: int) -> list[int]:\n\
    \    assert len(A) == len(B)\n    subset_zeta(A, N), subset_zeta(B, N)\n    for\
    \ i, b in enumerate(B): A[i] *= b\n    return subset_mobius(A, N)\n"
  dependsOn:
  - cp_library/math/conv/subset_zeta_fn.py
  - cp_library/math/conv/subset_mobius_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/or_conv_fast_fn.py
  requiredBy: []
  timestamp: '2025-03-09 09:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/conv/or_conv_fast_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/or_conv_fast_fn.py
- /library/cp_library/math/conv/or_conv_fast_fn.py.html
title: cp_library/math/conv/or_conv_fast_fn.py
---
