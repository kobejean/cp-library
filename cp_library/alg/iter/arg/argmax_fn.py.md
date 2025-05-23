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
    \n\n\n\ndef argmax(A, l = 0, r=None):\n    if r is None: r = len(A)\n    if l\
    \ == r: return -1\n    m = l\n    while (l:=l+1)<r:\n        if A[m] < A[l]: m\
    \ = l\n    return m\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.arg.__header__\n\ndef argmax(A, l = 0, r=None):\n \
    \   if r is None: r = len(A)\n    if l == r: return -1\n    m = l\n    while (l:=l+1)<r:\n\
    \        if A[m] < A[l]: m = l\n    return m"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/arg/argmax_fn.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/arg/argmax_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/arg/argmax_fn.py
- /library/cp_library/alg/iter/arg/argmax_fn.py.html
title: cp_library/alg/iter/arg/argmax_fn.py
---
