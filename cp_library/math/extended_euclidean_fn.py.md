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
    \ndef extended_euclidean(a, b):\n    match a, b:\n        case 0,0: return 0,\
    \ 1, 0\n        case _,0: return 1, 0, a\n        case 0,_: return 0, 1, b\n \
    \       case _:\n            x,y,r,s = 1,0,0,1\n            while b:\n       \
    \         q, c = divmod(a,b)\n                a, b, r, s, x, y = b, c, x - q*r,\
    \ y - q*s, r, s\n            return x, y, a\n"
  code: "import cp_library.math.__header__\n\ndef extended_euclidean(a, b):\n    match\
    \ a, b:\n        case 0,0: return 0, 1, 0\n        case _,0: return 1, 0, a\n\
    \        case 0,_: return 0, 1, b\n        case _:\n            x,y,r,s = 1,0,0,1\n\
    \            while b:\n                q, c = divmod(a,b)\n                a,\
    \ b, r, s, x, y = b, c, x - q*r, y - q*s, r, s\n            return x, y, a\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/extended_euclidean_fn.py
  requiredBy: []
  timestamp: '2024-10-02 19:58:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/extended_euclidean_fn.py
layout: document
redirect_from:
- /library/cp_library/math/extended_euclidean_fn.py
- /library/cp_library/math/extended_euclidean_fn.py.html
title: cp_library/math/extended_euclidean_fn.py
---
