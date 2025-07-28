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
    \nclass Lucas(list[int]):\n    def __init__(lucas,N,mod=None):\n        super().__init__([0]*(N+1))\n\
    \        dp0 = 2; dp1 = 1\n        if mod is None:\n            lucas[0] = dp0\n\
    \            for i in range(N): dp0, dp1 = dp1, dp0+dp1; lucas[i+1] = dp0\n  \
    \      else:\n            lucas[0] = dp0 % mod\n            for i in range(N):\
    \ dp0, dp1 = dp1, (dp0+dp1)%mod; lucas[i+1] = dp0\n"
  code: "import cp_library.math.table.__header__\n\nclass Lucas(list[int]):\n    def\
    \ __init__(lucas,N,mod=None):\n        super().__init__([0]*(N+1))\n        dp0\
    \ = 2; dp1 = 1\n        if mod is None:\n            lucas[0] = dp0\n        \
    \    for i in range(N): dp0, dp1 = dp1, dp0+dp1; lucas[i+1] = dp0\n        else:\n\
    \            lucas[0] = dp0 % mod\n            for i in range(N): dp0, dp1 = dp1,\
    \ (dp0+dp1)%mod; lucas[i+1] = dp0"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/lucas_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/lucas_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/lucas_cls.py
- /library/cp_library/math/table/lucas_cls.py.html
title: cp_library/math/table/lucas_cls.py
---
