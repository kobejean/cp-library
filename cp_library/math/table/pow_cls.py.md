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
    \nclass Pow(list[int]):\n    def __init__(self,K,N,mod=None):\n        super().__init__([1]*(N+1))\n\
    \        if mod is None:\n            for i in range(N):\n                self[i+1]\
    \ = self[i]*K\n        else:\n            for i in range(N):\n               \
    \ self[i+1] = self[i]*K % mod\n"
  code: "import cp_library.math.table.__header__\n\nclass Pow(list[int]):\n    def\
    \ __init__(self,K,N,mod=None):\n        super().__init__([1]*(N+1))\n        if\
    \ mod is None:\n            for i in range(N):\n                self[i+1] = self[i]*K\n\
    \        else:\n            for i in range(N):\n                self[i+1] = self[i]*K\
    \ % mod"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/pow_cls.py
  requiredBy: []
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/pow_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/pow_cls.py
- /library/cp_library/math/table/pow_cls.py.html
title: cp_library/math/table/pow_cls.py
---