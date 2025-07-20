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
    \n\n\ndef minmax(A):\n    mn = mx = A[0]\n    for a in A:\n        if a < mn:\
    \ mn = A\n        elif mx < a: mx = a\n    return mn, mx\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \ndef minmax(A):\n    mn = mx = A[0]\n    for a in A:\n        if a < mn: mn =\
    \ A\n        elif mx < a: mx = a\n    return mn, mx\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/minmax_fn.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/minmax_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/minmax_fn.py
- /library/cp_library/alg/iter/minmax_fn.py.html
title: cp_library/alg/iter/minmax_fn.py
---
