---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/math/mod/matmul.py
    title: cp_library/math/mod/matmul.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/pow_of_matrix.test.py
    title: test/pow_of_matrix.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "def matmul(A, B, mod):\n    N1, N2, N3 = len(A),len(B),len(B[0])\n\
    \    R = [[0]*N3 for _ in range(N1)]\n    for i in range(N1):\n        for j in\
    \ range(N3):\n            for k in range(N2):\n                R[i][j] += A[i][k]*B[k][j]\
    \ % mod\n                R[i][j] %= mod\n    return R\n\ndef matpow(A, K, mod):\n\
    \    N = len(A)\n    R = [[int(i == j) for j in range(N)] for i in range(N)]\n\
    \    An = [[aij for aij in ai] for ai in A]\n    while K > 0:\n        if K &\
    \ 1:\n            R = matmul(R,An,mod)\n        An = matmul(An,An,mod)\n     \
    \   K >>= 1\n    return R\n"
  code: "from cp_library.math.mod.matmul import matmul\n\ndef matpow(A, K, mod):\n\
    \    N = len(A)\n    R = [[int(i == j) for j in range(N)] for i in range(N)]\n\
    \    An = [[aij for aij in ai] for ai in A]\n    while K > 0:\n        if K &\
    \ 1:\n            R = matmul(R,An,mod)\n        An = matmul(An,An,mod)\n     \
    \   K >>= 1\n    return R"
  dependsOn:
  - cp_library/math/mod/matmul.py
  isVerificationFile: false
  path: cp_library/math/mod/matpow.py
  requiredBy: []
  timestamp: '2024-08-14 00:25:50+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/pow_of_matrix.test.py
documentation_of: cp_library/math/mod/matpow.py
layout: document
redirect_from:
- /library/cp_library/math/mod/matpow.py
- /library/cp_library/math/mod/matpow.py.html
title: cp_library/math/mod/matpow.py
---
