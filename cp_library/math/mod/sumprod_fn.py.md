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
    \n\n\ndef sumprod(A, B, mod):\n    assert len(A) == len(B)\n    ret = 0\n    for\
    \ i in range(len(A)): ret = (ret + A[i]*B[i]%mod) % mod\n    return ret\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.mod.__header__\n\
    \ndef sumprod(A, B, mod):\n    assert len(A) == len(B)\n    ret = 0\n    for i\
    \ in range(len(A)): ret = (ret + A[i]*B[i]%mod) % mod\n    return ret"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/sumprod_fn.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/sumprod_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mod/sumprod_fn.py
- /library/cp_library/math/mod/sumprod_fn.py.html
title: cp_library/math/mod/sumprod_fn.py
---
