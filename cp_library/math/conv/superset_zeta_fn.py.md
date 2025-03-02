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
    \ndef superset_zeta(A, N: int):\n    Z = len(A)\n    for i in range(N):\n    \
    \    m = b = 1<<i\n        while m < Z:\n            A[m^b] += A[m]\n        \
    \    m = m+1|b\n    return A\n"
  code: "import cp_library.math.conv.__header__\n\ndef superset_zeta(A, N: int):\n\
    \    Z = len(A)\n    for i in range(N):\n        m = b = 1<<i\n        while m\
    \ < Z:\n            A[m^b] += A[m]\n            m = m+1|b\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/conv/superset_zeta_fn.py
  requiredBy: []
  timestamp: '2025-03-03 00:10:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/conv/superset_zeta_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/superset_zeta_fn.py
- /library/cp_library/math/conv/superset_zeta_fn.py.html
title: cp_library/math/conv/superset_zeta_fn.py
---
