---
data:
  _extendedDependsOn: []
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
    \nclass Mobius(list[int]):\n    def __init__(mu, N):\n        super().__init__([0]*(N+1))\n\
    \        mu[1] = 1\n        for i in range(1, N+1):\n            for j in range(i<<1,\
    \ N+1, i):\n                mu[j] -= mu[i]\n"
  code: "import cp_library.math.table.__header__\n\nclass Mobius(list[int]):\n   \
    \ def __init__(mu, N):\n        super().__init__([0]*(N+1))\n        mu[1] = 1\n\
    \        for i in range(1, N+1):\n            for j in range(i<<1, N+1, i):\n\
    \                mu[j] -= mu[i]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/mobius_cls.py
  requiredBy: []
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/mobius_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/mobius_cls.py
- /library/cp_library/math/table/mobius_cls.py.html
title: cp_library/math/table/mobius_cls.py
---
