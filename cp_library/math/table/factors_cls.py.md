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
  bundledCode: "class Factors(list[int]):\n    def __init__(self, N: int):\n     \
    \   factors = []\n        n = N\n        i = 2\n        while i * i <= n:\n  \
    \          while n % i == 0:\n                factors.append(i)\n            \
    \    n //= i\n            i += 1\n        if n > 1:\n            factors.append(n)\n\
    \        super().__init__(factors)\n"
  code: "class Factors(list[int]):\n    def __init__(self, N: int):\n        factors\
    \ = []\n        n = N\n        i = 2\n        while i * i <= n:\n            while\
    \ n % i == 0:\n                factors.append(i)\n                n //= i\n  \
    \          i += 1\n        if n > 1:\n            factors.append(n)\n        super().__init__(factors)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/factors_cls.py
  requiredBy: []
  timestamp: '2025-03-03 00:10:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/factors_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/factors_cls.py
- /library/cp_library/math/table/factors_cls.py.html
title: cp_library/math/table/factors_cls.py
---
