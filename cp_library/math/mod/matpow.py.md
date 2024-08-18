---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/matid.py
    title: cp_library/math/matid.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/matmul.py
    title: cp_library/math/mod/matmul.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_matpow.test.py
    title: test/pow_of_matrix_matpow.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef mat_mul(A,B,mod):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = (Ri[j] + Aik*Bkj) % mod  \n    return R \n\ndef mat_id(N):\n    return\
    \ [[int(i==j) for j in range(N)] for i in range(N)]\n\ndef mat_pow(A,K,mod):\n\
    \    N = len(A)\n    ret = A if K & 1 else mat_id(N)\n    for i in range(1,K.bit_length()):\n\
    \        A = mat_mul(A,A,mod) \n        if K >> i & 1:\n            ret = mat_mul(ret,A,mod)\
    \ \n    return ret \n"
  code: "from cp_library.math.mod.matmul import mat_mul\nfrom cp_library.math.matid\
    \ import mat_id\n\ndef mat_pow(A,K,mod):\n    N = len(A)\n    ret = A if K & 1\
    \ else mat_id(N)\n    for i in range(1,K.bit_length()):\n        A = mat_mul(A,A,mod)\
    \ \n        if K >> i & 1:\n            ret = mat_mul(ret,A,mod) \n    return\
    \ ret \n"
  dependsOn:
  - cp_library/math/mod/matmul.py
  - cp_library/math/matid.py
  isVerificationFile: false
  path: cp_library/math/mod/matpow.py
  requiredBy: []
  timestamp: '2024-08-18 15:24:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix_matpow.test.py
documentation_of: cp_library/math/mod/matpow.py
layout: document
redirect_from:
- /library/cp_library/math/mod/matpow.py
- /library/cp_library/math/mod/matpow.py.html
title: cp_library/math/mod/matpow.py
---
