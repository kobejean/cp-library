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
  bundledCode: "class FactorCounts(list[tuple[int,int]]):\n    def __init__(self,\
    \ N: int):\n        pairs = []\n        d = 2\n        while d*d<=N:\n       \
    \     while N % d == 0:\n                match pairs:\n                    case\
    \ [*_, (f,cnt)] if f == d:\n                        pairs[-1] = (f,cnt+1)\n  \
    \                  case _:\n                        pairs.append((d, 1))\n   \
    \             N //= d\n            d += 1\n        super().__init__(pairs)\n"
  code: "class FactorCounts(list[tuple[int,int]]):\n    def __init__(self, N: int):\n\
    \        pairs = []\n        d = 2\n        while d*d<=N:\n            while N\
    \ % d == 0:\n                match pairs:\n                    case [*_, (f,cnt)]\
    \ if f == d:\n                        pairs[-1] = (f,cnt+1)\n                \
    \    case _:\n                        pairs.append((d, 1))\n                N\
    \ //= d\n            d += 1\n        super().__init__(pairs)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/factor_cnts_cls.py
  requiredBy: []
  timestamp: '2024-12-29 16:20:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/factor_cnts_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/factor_cnts_cls.py
- /library/cp_library/math/table/factor_cnts_cls.py.html
title: cp_library/math/table/factor_cnts_cls.py
---
