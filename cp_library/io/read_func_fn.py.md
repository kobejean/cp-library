---
data:
  _extendedDependsOn: []
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
  bundledCode: "\ndef read(func=0, /):\n    if callable(func): return [func(s) for\
    \ s in input().split()]\n    return [int(s)+func for s in input().split()]\n"
  code: "\ndef read(func=0, /):\n    if callable(func): return [func(s) for s in input().split()]\n\
    \    return [int(s)+func for s in input().split()]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/read_func_fn.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix_matpow.test.py
documentation_of: cp_library/io/read_func_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_func_fn.py
- /library/cp_library/io/read_func_fn.py.html
title: cp_library/io/read_func_fn.py
---