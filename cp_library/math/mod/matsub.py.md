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
  bundledCode: "\ndef mat_sub(A, B, mod):\n    return [[(Ai[j] - Bi[j]) % mod for\
    \ j in range(len(Ai))] for Ai,Bi in zip(A,B)]\n"
  code: "\ndef mat_sub(A, B, mod):\n    return [[(Ai[j] - Bi[j]) % mod for j in range(len(Ai))]\
    \ for Ai,Bi in zip(A,B)]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/matsub.py
  requiredBy: []
  timestamp: '2024-08-18 16:01:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/matsub.py
layout: document
redirect_from:
- /library/cp_library/math/mod/matsub.py
- /library/cp_library/math/mod/matsub.py.html
title: cp_library/math/mod/matsub.py
---
