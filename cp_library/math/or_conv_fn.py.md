---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_mobius_fn.py
    title: cp_library/math/subset_mobius_fn.py
  - icon: ':warning:'
    path: cp_library/math/subset_zeta_fn.py
    title: cp_library/math/subset_zeta_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "import operator\nfrom typing import Callable\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef subset_zeta(A: list[int], N: int, Z: int = None):\n\
    \    Z = 1 << N if Z is None else Z\n    for i in range(N):\n        m = b = 1<<i\n\
    \        while m < Z:\n            A[m] += A[m^b]\n            m = m+1|b\n   \
    \ return A\n\ndef subset_mobius(A: list[int], N: int, Z: int = None):\n    Z =\
    \ 1 << N if Z is None else Z\n    for i in range(N):\n        m = b = 1<<i\n \
    \       while m < Z:\n            A[m] -= A[m^b]\n            m = m+1|b\n    return\
    \ A\n\ndef or_conv(A: list[int], B: list[int], N: int,\n            add: Callable[[int,int],int]\
    \ = operator.add,\n            sub: Callable[[int,int],int] = operator.sub,\n\
    \            mul: Callable[[int,int],int] = operator.mul) -> list[int]:\n    subset_zeta(A,\
    \ N), subset_zeta(B, N)\n    for i, b in enumerate(B): A[i] *= b\n    return subset_mobius(A,\
    \ N)\n"
  code: "import operator\nfrom typing import Callable\nimport cp_library.math.__header__\n\
    from cp_library.math.subset_zeta_fn import subset_zeta\nfrom cp_library.math.subset_mobius_fn\
    \ import subset_mobius\n\ndef or_conv(A: list[int], B: list[int], N: int,\n  \
    \          add: Callable[[int,int],int] = operator.add,\n            sub: Callable[[int,int],int]\
    \ = operator.sub,\n            mul: Callable[[int,int],int] = operator.mul) ->\
    \ list[int]:\n    subset_zeta(A, N), subset_zeta(B, N)\n    for i, b in enumerate(B):\
    \ A[i] *= b\n    return subset_mobius(A, N)\n"
  dependsOn:
  - cp_library/math/subset_zeta_fn.py
  - cp_library/math/subset_mobius_fn.py
  isVerificationFile: false
  path: cp_library/math/or_conv_fn.py
  requiredBy: []
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/or_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/or_conv_fn.py
- /library/cp_library/math/or_conv_fn.py.html
title: cp_library/math/or_conv_fn.py
---
