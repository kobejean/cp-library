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
    \ndef ternary_max(lo, hi, f):\n    while hi - lo > 2:\n        m2 = (m1 := (lo+hi)//2)+1\n\
    \        if f(m1) < f(m2): lo = m1\n        else: hi = m2\n    return f(lo+1)\n"
  code: "import cp_library.alg.divcon.__header__\n\ndef ternary_max(lo, hi, f):\n\
    \    while hi - lo > 2:\n        m2 = (m1 := (lo+hi)//2)+1\n        if f(m1) <\
    \ f(m2): lo = m1\n        else: hi = m2\n    return f(lo+1)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/divcon/ternary_max_fn.py
  requiredBy: []
  timestamp: '2025-01-16 09:57:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/divcon/ternary_max_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/ternary_max_fn.py
- /library/cp_library/alg/divcon/ternary_max_fn.py.html
title: cp_library/alg/divcon/ternary_max_fn.py
---
