---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/mat/mod/mat_pow_fn.py
    title: cp_library/math/linalg/mat/mod/mat_pow_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/linear-algebra/pow_of_matrix_matpow.test.py
    title: test/library-checker/linear-algebra/pow_of_matrix_matpow.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef mat_mul(A,B,mod):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = (Ri[j] + Aik*Bkj) % mod\n    return R\n"
  code: "import cp_library.math.mod.__header__\n\ndef mat_mul(A,B,mod):\n    assert\
    \ len(A[0]) == len(B)\n    R = [[0]*len(B[0]) for _ in range(len(A))] \n    for\
    \ i,Ri in enumerate(R):\n        for k,Aik in enumerate(A[i]):\n            for\
    \ j,Bkj in enumerate(B[k]):\n                Ri[j] = (Ri[j] + Aik*Bkj) % mod\n\
    \    return R\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/linalg/mat/mod/mat_mul_fn.py
  requiredBy:
  - cp_library/math/linalg/mat/mod/mat_pow_fn.py
  timestamp: '2025-06-08 23:28:30+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/linear-algebra/pow_of_matrix_matpow.test.py
documentation_of: cp_library/math/linalg/mat/mod/mat_mul_fn.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/mat/mod/mat_mul_fn.py
- /library/cp_library/math/linalg/mat/mod/mat_mul_fn.py.html
title: cp_library/math/linalg/mat/mod/mat_mul_fn.py
---
