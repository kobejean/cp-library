---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc304_f_mobius_inv.test.py
    title: test/atcoder/abc/abc304_f_mobius_inv.test.py
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
  timestamp: '2025-03-12 22:12:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc304_f_mobius_inv.test.py
documentation_of: cp_library/math/table/pow_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/pow_cls.py
- /library/cp_library/math/table/pow_cls.py.html
title: cp_library/math/table/pow_cls.py
---
