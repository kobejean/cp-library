---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/mat_pow_fn.py
    title: cp_library/math/mat_pow_fn.py
  - icon: ':warning:'
    path: cp_library/math/mod/mat_pow_fn.py
    title: cp_library/math/mod/mat_pow_fn.py
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
    \ndef mat_id(N):\n    return [[int(i==j) for j in range(N)] for i in range(N)]\n"
  code: "import cp_library.math.__header__\n\ndef mat_id(N):\n    return [[int(i==j)\
    \ for j in range(N)] for i in range(N)]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mat_id_fn.py
  requiredBy:
  - cp_library/math/mod/mat_pow_fn.py
  - cp_library/math/mat_pow_fn.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mat_id_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mat_id_fn.py
- /library/cp_library/math/mat_id_fn.py.html
title: cp_library/math/mat_id_fn.py
---
