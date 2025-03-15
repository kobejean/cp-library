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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef mat_pow(A,K,mod):\n    N = len(A)\n    ret = A if K & 1 else mat_id(N)\n\
    \    for i in range(1,K.bit_length()):\n        A = mat_mul(A,A,mod) \n      \
    \  if K >> i & 1:\n            ret = mat_mul(ret,A,mod) \n    return ret \n\n\
    from cp_library.math.mat.mod.mat_mul_fn import mat_mul\nfrom cp_library.math.mat.mat_id_fn\
    \ import mat_id\n"
  code: "import cp_library.math.mod.__header__\n\ndef mat_pow(A,K,mod):\n    N = len(A)\n\
    \    ret = A if K & 1 else mat_id(N)\n    for i in range(1,K.bit_length()):\n\
    \        A = mat_mul(A,A,mod) \n        if K >> i & 1:\n            ret = mat_mul(ret,A,mod)\
    \ \n    return ret \n\nfrom cp_library.math.mat.mod.mat_mul_fn import mat_mul\n\
    from cp_library.math.mat.mat_id_fn import mat_id"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/linalg/mat/mod/mat_pow_fn.py
  requiredBy: []
  timestamp: '2025-03-15 12:29:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/linalg/mat/mod/mat_pow_fn.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/mat/mod/mat_pow_fn.py
- /library/cp_library/math/linalg/mat/mod/mat_pow_fn.py.html
title: cp_library/math/linalg/mat/mod/mat_pow_fn.py
---
