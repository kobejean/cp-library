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
    \ndef subset_zeta(A: list[int], N: int):\n    Z = len(A)\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z:\n            A[m] += A[m^b]\n    \
    \        m = m+1|b\n    return A\n\ndef subset_mobius(A: list[int], N: int):\n\
    \    Z = len(A)\n    for i in range(N):\n        m = b = 1<<i\n        while m\
    \ < Z:\n            A[m] -= A[m^b]\n            m = m+1|b\n    return A\n\ndef\
    \ or_conv(A: list[int], B: list[int], N: int) -> list[int]:\n    assert len(A)\
    \ == len(B)\n    subset_zeta(A, N), subset_zeta(B, N)\n    for i, b in enumerate(B):\
    \ A[i] *= b\n    return subset_mobius(A, N)\n"
  code: "import cp_library.math.conv.__header__\nfrom cp_library.math.conv.subset_zeta_fn\
    \ import subset_zeta\nfrom cp_library.math.conv.subset_mobius_fn import subset_mobius\n\
    \ndef or_conv(A: list[int], B: list[int], N: int) -> list[int]:\n    assert len(A)\
    \ == len(B)\n    subset_zeta(A, N), subset_zeta(B, N)\n    for i, b in enumerate(B):\
    \ A[i] *= b\n    return subset_mobius(A, N)\n"
  dependsOn:
  - cp_library/math/conv/subset_zeta_fn.py
  - cp_library/math/conv/subset_mobius_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/or_conv_fast_fn.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/conv/or_conv_fast_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/or_conv_fast_fn.py
- /library/cp_library/math/conv/or_conv_fast_fn.py.html
title: cp_library/math/conv/or_conv_fast_fn.py
---
