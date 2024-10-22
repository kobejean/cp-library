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
    \nclass Mobius(list[int]):\n    def __init__(mob, N):\n        super().__init__([1]*(N+1))\n\
    \        for i in range(2, N+1):\n            if mob[i] == 1: \n             \
    \   i2 = i*i\n                for j in range(i, N+1, i): \n                  \
    \  if j % i2 == 0: \n                        mob[j] = 0\n                    else:\
    \ \n                        mob[j] *= -1\n"
  code: "import cp_library.math.table.__header__\n\nclass Mobius(list[int]):\n   \
    \ def __init__(mob, N):\n        super().__init__([1]*(N+1))\n        for i in\
    \ range(2, N+1):\n            if mob[i] == 1: \n                i2 = i*i\n   \
    \             for j in range(i, N+1, i): \n                    if j % i2 == 0:\
    \ \n                        mob[j] = 0\n                    else: \n         \
    \               mob[j] *= -1"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/mobius_cls.py
  requiredBy: []
  timestamp: '2024-10-23 00:17:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/mobius_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/mobius_cls.py
- /library/cp_library/math/table/mobius_cls.py.html
title: cp_library/math/table/mobius_cls.py
---
