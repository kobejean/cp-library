---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc186_e_gcd_ex.test.py
    title: test/abc186_e_gcd_ex.test.py
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
    \ndef ext_gcd(a, b):\n    match a, b:\n        case 0,0: return 0, 1, 0\n    \
    \    case _,0: return 1, 0, a\n        case 0,_: return 0, 1, b\n        case\
    \ _,_:\n            x,y,r,s = 1,0,0,1\n            while b:\n                q,\
    \ c = divmod(a,b)\n                a, b, r, s, x, y = b, c, x - q*r, y - q*s,\
    \ r, s\n            return x, y, a\n"
  code: "import cp_library.math.__header__\n\ndef ext_gcd(a, b):\n    match a, b:\n\
    \        case 0,0: return 0, 1, 0\n        case _,0: return 1, 0, a\n        case\
    \ 0,_: return 0, 1, b\n        case _,_:\n            x,y,r,s = 1,0,0,1\n    \
    \        while b:\n                q, c = divmod(a,b)\n                a, b, r,\
    \ s, x, y = b, c, x - q*r, y - q*s, r, s\n            return x, y, a\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/ext_gcd_fn.py
  requiredBy: []
  timestamp: '2024-11-05 04:28:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc186_e_gcd_ex.test.py
documentation_of: cp_library/math/ext_gcd_fn.py
layout: document
redirect_from:
- /library/cp_library/math/ext_gcd_fn.py
- /library/cp_library/math/ext_gcd_fn.py.html
title: cp_library/math/ext_gcd_fn.py
---
