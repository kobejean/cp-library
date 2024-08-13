---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/math/mod/matpow.py
    title: cp_library/math/mod/matpow.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "def matmul(A, B, mod):\n    N1, N2, N3 = len(A),len(B),len(B[0])\n\
    \    R = [[0]*N3 for _ in range(N1)]\n    for i in range(N1):\n        for j in\
    \ range(N3):\n            for k in range(N2):\n                R[i][j] += A[i][k]*B[k][j]\
    \ % mod\n                R[i][j] %= mod\n    return R\n"
  code: "def matmul(A, B, mod):\n    N1, N2, N3 = len(A),len(B),len(B[0])\n    R =\
    \ [[0]*N3 for _ in range(N1)]\n    for i in range(N1):\n        for j in range(N3):\n\
    \            for k in range(N2):\n                R[i][j] += A[i][k]*B[k][j] %\
    \ mod\n                R[i][j] %= mod\n    return R"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/matmul.py
  requiredBy:
  - cp_library/math/mod/matpow.py
  timestamp: '2024-08-14 00:25:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/matmul.py
layout: document
redirect_from:
- /library/cp_library/math/mod/matmul.py
- /library/cp_library/math/mod/matmul.py.html
title: cp_library/math/mod/matmul.py
---
