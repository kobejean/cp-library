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
    \n\n\ndef bisect_right(A, x, l, r):\n    while l<r:\n        if x<A[m:=(l+r)>>1]:r=m\n\
    \        else:l=m+1\n    return l\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.divcon.__header__\n\
    \ndef bisect_right(A, x, l, r):\n    while l<r:\n        if x<A[m:=(l+r)>>1]:r=m\n\
    \        else:l=m+1\n    return l"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/divcon/bisect_right_fn.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/divcon/bisect_right_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/bisect_right_fn.py
- /library/cp_library/alg/divcon/bisect_right_fn.py.html
title: cp_library/alg/divcon/bisect_right_fn.py
---
