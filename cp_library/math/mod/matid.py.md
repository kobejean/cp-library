---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/matpow.py
    title: cp_library/math/mod/matpow.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix.test.py
    title: test/pow_of_matrix.test.py
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
  path: cp_library/math/mod/matid.py
  requiredBy:
  - cp_library/math/mod/matpow.py
  timestamp: '2024-08-14 14:27:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix.test.py
documentation_of: cp_library/math/mod/matid.py
layout: document
redirect_from:
- /library/cp_library/math/mod/matid.py
- /library/cp_library/math/mod/matid.py.html
title: cp_library/math/mod/matid.py
---
