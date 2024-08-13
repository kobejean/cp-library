---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: cp_library/math/mod/matpow.py
    title: cp_library/math/mod/matpow.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
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
    \   K >>= 1\n    return R\n\ndef rint(shift=0, base=10):\n    return [int(x, base)\
    \ + shift for x in input().split()]\n\nmod = 998244353\n\nN, K = rint()\nA = [rint()\
    \ for _ in range(N)]\nB = matpow(A, K, mod)\nfor bi in B:\n    print(*bi) \n \
    \   \n"
  code: "from cp_library.math.mod.matpow import matpow\n\ndef rint(shift=0, base=10):\n\
    \    return [int(x, base) + shift for x in input().split()]\n\nmod = 998244353\n\
    \nN, K = rint()\nA = [rint() for _ in range(N)]\nB = matpow(A, K, mod)\nfor bi\
    \ in B:\n    print(*bi) \n    "
  dependsOn:
  - cp_library/math/mod/matpow.py
  isVerificationFile: true
  path: test/pow_of_matrix.test.py
  requiredBy: []
  timestamp: '2024-08-14 00:25:50+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/pow_of_matrix.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix.test.py
- /verify/test/pow_of_matrix.test.py.html
title: test/pow_of_matrix.test.py
---
