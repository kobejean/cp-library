---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_pow_fn.py
    title: cp_library/math/mat_pow_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_matpow.test.py
    title: test/pow_of_matrix_matpow.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef mat_mul(A,B):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = Bkj*Aik + Ri[j]  \n    return R \n"
  code: "\ndef mat_mul(A,B):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = Bkj*Aik + Ri[j]  \n    return R \n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mat_mul_fn.py
  requiredBy:
  - cp_library/math/mat_pow_fn.py
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix_matpow.test.py
documentation_of: cp_library/math/mat_mul_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mat_mul_fn.py
- /library/cp_library/math/mat_mul_fn.py.html
title: cp_library/math/mat_mul_fn.py
---