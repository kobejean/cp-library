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
    \ndef mat_add(A, B, mod):\n    return [[(Ai[j] + Bi[j]) % mod for j in range(len(Ai))]\
    \ for Ai,Bi in zip(A,B)]\n"
  code: "import cp_library.math.mod.__header__\n\ndef mat_add(A, B, mod):\n    return\
    \ [[(Ai[j] + Bi[j]) % mod for j in range(len(Ai))] for Ai,Bi in zip(A,B)]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/mat_add_fn.py
  requiredBy: []
  timestamp: '2024-12-27 22:35:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/mat_add_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mat_add_fn.py
- /library/cp_library/math/mod/mat_add_fn.py.html
title: cp_library/math/mod/mat_add_fn.py
---
