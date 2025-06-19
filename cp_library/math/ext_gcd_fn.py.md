---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc186_e_gcd_ex.test.py
    title: test/atcoder/abc/abc186_e_gcd_ex.test.py
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
    \ndef ext_gcd(a, b):\n    ''' Returns (x, y, d) where: ax + by = d = gcd(a,b)\
    \ '''\n    if a and b:\n        x,y,r,s = 1,0,0,1\n        while b:\n        \
    \    q, c = divmod(a,b)\n            a, b, r, s, x, y = b, c, x - q*r, y - q*s,\
    \ r, s\n        return x, y, a\n    elif a: return 1, 0, a\n    elif b: return\
    \ 0, 1, b\n    else: return 0, 1, 0\n"
  code: "import cp_library.math.__header__\n\ndef ext_gcd(a, b):\n    ''' Returns\
    \ (x, y, d) where: ax + by = d = gcd(a,b) '''\n    if a and b:\n        x,y,r,s\
    \ = 1,0,0,1\n        while b:\n            q, c = divmod(a,b)\n            a,\
    \ b, r, s, x, y = b, c, x - q*r, y - q*s, r, s\n        return x, y, a\n    elif\
    \ a: return 1, 0, a\n    elif b: return 0, 1, b\n    else: return 0, 1, 0\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/ext_gcd_fn.py
  requiredBy: []
  timestamp: '2025-06-20 03:24:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc186_e_gcd_ex.test.py
documentation_of: cp_library/math/ext_gcd_fn.py
layout: document
redirect_from:
- /library/cp_library/math/ext_gcd_fn.py
- /library/cp_library/math/ext_gcd_fn.py.html
title: cp_library/math/ext_gcd_fn.py
---
