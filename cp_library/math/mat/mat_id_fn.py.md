---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat/mat_pow_fn.py
    title: cp_library/math/mat/mat_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat/mod/mat_pow_fn.py
    title: cp_library/math/mat/mod/mat_pow_fn.py
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
    \ndef mat_id(N):\n    return [[int(i==j) for j in range(N)] for i in range(N)]\n"
  code: "import cp_library.math.__header__\n\ndef mat_id(N):\n    return [[int(i==j)\
    \ for j in range(N)] for i in range(N)]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mat/mat_id_fn.py
  requiredBy:
  - cp_library/math/mat/mat_pow_fn.py
  - cp_library/math/mat/mod/mat_pow_fn.py
  timestamp: '2025-03-03 00:10:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/linear-algebra/pow_of_matrix_matpow.test.py
documentation_of: cp_library/math/mat/mat_id_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mat/mat_id_fn.py
- /library/cp_library/math/mat/mat_id_fn.py.html
title: cp_library/math/mat/mat_id_fn.py
---
