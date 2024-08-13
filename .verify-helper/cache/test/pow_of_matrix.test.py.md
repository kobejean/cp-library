---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_matrix
    links:
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\ndef mat_mul(A,B,mod):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = (Ri[j] + Aik*Bkj) % mod  \n    return R \n\ndef mat_id(N):\n    return\
    \ [[int(i==j) for j in range(N)] for i in range(N)]\n\ndef mat_pow(A,K,mod):\n\
    \    N = len(A)\n    ret = A if K & 1 else mat_id(N)\n    for i in range(1,K.bit_length()):\n\
    \        A = mat_mul(A,A,mod) \n        if K >> i & 1:\n            ret = mat_mul(ret,A,mod)\
    \ \n    return ret \n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n    return\
    \ [int(x, base) + shift for x in input().split()]\n\nN, K = rint()\nA = [rint()\
    \ for _ in range(N)]\nB = mat_pow(A, K, mod)\n\nfor row in B:\n    print(*row)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\ndef mat_mul(A,B,mod):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = (Ri[j] + Aik*Bkj) % mod  \n    return R \n\ndef mat_id(N):\n    return\
    \ [[int(i==j) for j in range(N)] for i in range(N)]\n\ndef mat_pow(A,K,mod):\n\
    \    N = len(A)\n    ret = A if K & 1 else mat_id(N)\n    for i in range(1,K.bit_length()):\n\
    \        A = mat_mul(A,A,mod) \n        if K >> i & 1:\n            ret = mat_mul(ret,A,mod)\
    \ \n    return ret \n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n    return\
    \ [int(x, base) + shift for x in input().split()]\n\nN, K = rint()\nA = [rint()\
    \ for _ in range(N)]\nB = mat_pow(A, K, mod)\n\nfor row in B:\n    print(*row)\n"
  dependsOn: []
  isVerificationFile: true
  path: pow_of_matrix.test.py
  requiredBy: []
  timestamp: '2024-08-14 06:01:40+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: pow_of_matrix.test.py
layout: document
redirect_from:
- /verify/pow_of_matrix.test.py
- /verify/pow_of_matrix.test.py.html
title: pow_of_matrix.test.py
---
