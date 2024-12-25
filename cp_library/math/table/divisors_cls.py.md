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
    \nclass Divisors(list[int]):\n    def __init__(D, N):\n        super().__init__()\n\
    \        C = []\n        for x in range(1,N+1):\n            if x*x>N: break\n\
    \            if N % x == 0:\n                D.append(x)\n                C.append(N//x)\n\
    \        if C[-1] == D[-1]: C.pop()\n        D.extend(reversed(C))\n"
  code: "import cp_library.math.table.__header__\n\nclass Divisors(list[int]):\n \
    \   def __init__(D, N):\n        super().__init__()\n        C = []\n        for\
    \ x in range(1,N+1):\n            if x*x>N: break\n            if N % x == 0:\n\
    \                D.append(x)\n                C.append(N//x)\n        if C[-1]\
    \ == D[-1]: C.pop()\n        D.extend(reversed(C))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/divisors_cls.py
  requiredBy: []
  timestamp: '2024-12-25 17:59:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/divisors_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/divisors_cls.py
- /library/cp_library/math/table/divisors_cls.py.html
title: cp_library/math/table/divisors_cls.py
---
