---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/linalg/mat/mat_pow_fn.py
    title: cp_library/math/linalg/mat/mat_pow_fn.py
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
    \n\n\n\ndef mat_mul(A,B):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = Bkj*Aik + Ri[j]  \n    return R \n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.linalg.__header__\n\
    import cp_library.math.linalg.mat.__header__\n\ndef mat_mul(A,B):\n    assert\
    \ len(A[0]) == len(B)\n    R = [[0]*len(B[0]) for _ in range(len(A))] \n    for\
    \ i,Ri in enumerate(R):\n        for k,Aik in enumerate(A[i]):\n            for\
    \ j,Bkj in enumerate(B[k]):\n                Ri[j] = Bkj*Aik + Ri[j]  \n    return\
    \ R \n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/linalg/mat/mat_mul_fn.py
  requiredBy:
  - cp_library/math/linalg/mat/mat_pow_fn.py
  timestamp: '2025-03-15 19:36:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/linalg/mat/mat_mul_fn.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/mat/mat_mul_fn.py
- /library/cp_library/math/linalg/mat/mat_mul_fn.py.html
title: cp_library/math/linalg/mat/mat_mul_fn.py
---
