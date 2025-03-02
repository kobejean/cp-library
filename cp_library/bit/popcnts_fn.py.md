---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_conv_fn.py
    title: cp_library/math/conv/mod/subset_conv_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/subset_conv_fn.py
    title: cp_library/math/conv/subset_conv_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution.test.py
    title: test/library-checker/set-power-series/subset_convolution.test.py
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
    \ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n        for m\
    \ in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n"
  code: "import cp_library.bit.__header__\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n\
    \    for i in range(N):\n        for m in range(b := 1<<i):\n            P[m^b]\
    \ = P[m] + 1\n    return P\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/popcnts_fn.py
  requiredBy:
  - cp_library/math/conv/subset_conv_fn.py
  - cp_library/math/conv/mod/subset_conv_fn.py
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution.test.py
documentation_of: cp_library/bit/popcnts_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/popcnts_fn.py
- /library/cp_library/bit/popcnts_fn.py.html
title: cp_library/bit/popcnts_fn.py
---
