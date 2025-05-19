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
    \nclass DivisorCounts(list[tuple[int,int]]):\n    def __init__(D, N):\n      \
    \  super().__init__()\n        k = 1\n        while k <= N:\n            D.append((d\
    \ := N//k, -k + (k := N//d+1)))\n        D.reverse()\n"
  code: "import cp_library.math.table.__header__\n\nclass DivisorCounts(list[tuple[int,int]]):\n\
    \    def __init__(D, N):\n        super().__init__()\n        k = 1\n        while\
    \ k <= N:\n            D.append((d := N//k, -k + (k := N//d+1)))\n        D.reverse()\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/divisors_cnts_cls.py
  requiredBy: []
  timestamp: '2025-05-20 05:03:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/divisors_cnts_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/divisors_cnts_cls.py
- /library/cp_library/math/table/divisors_cnts_cls.py.html
title: cp_library/math/table/divisors_cnts_cls.py
---
