---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/mod/matpow.py
    title: cp_library/math/mod/matpow.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\ndef mat_mul(A,B,mod):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = (Ri[j] + Aik*Bkj) % mod  \n    return R \n"
  code: "\ndef mat_mul(A,B,mod):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = (Ri[j] + Aik*Bkj) % mod  \n    return R \n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/matmul.py
  requiredBy:
  - cp_library/math/mod/matpow.py
  timestamp: '2024-08-14 06:21:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/matmul.py
layout: document
redirect_from:
- /library/cp_library/math/mod/matmul.py
- /library/cp_library/math/mod/matmul.py.html
title: cp_library/math/mod/matmul.py
---
