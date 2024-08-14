---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/matpow.py
    title: cp_library/math/matpow.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/matpow.py
    title: cp_library/math/mod/matpow.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_matpow.test.py
    title: test/pow_of_matrix_matpow.test.py
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_mint.test.py
    title: test/pow_of_matrix_mint.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef mat_id(N):\n    return [[int(i==j) for j in range(N)] for i\
    \ in range(N)]\n"
  code: "\ndef mat_id(N):\n    return [[int(i==j) for j in range(N)] for i in range(N)]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/matid.py
  requiredBy:
  - cp_library/math/matpow.py
  - cp_library/math/mod/matpow.py
  timestamp: '2024-08-15 03:04:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix_matpow.test.py
  - test/pow_of_matrix_mint.test.py
documentation_of: cp_library/math/matid.py
layout: document
redirect_from:
- /library/cp_library/math/matid.py
- /library/cp_library/math/matid.py.html
title: cp_library/math/matid.py
---
