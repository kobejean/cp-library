---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc184_f_subset_sum_fn.test.py
    title: test/abc184_f_subset_sum_fn.test.py
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
    \ndef subset_sum(A):\n    dp = [0]*(1 << len(A))\n    for i,a in enumerate(A):\n\
    \        for mask in range(bit := 1 << i):\n            dp[mask^bit] = dp[mask]\
    \ + a\n    return dp\n"
  code: "import cp_library.math.__header__\n\ndef subset_sum(A):\n    dp = [0]*(1\
    \ << len(A))\n    for i,a in enumerate(A):\n        for mask in range(bit := 1\
    \ << i):\n            dp[mask^bit] = dp[mask] + a\n    return dp"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/subset_sum_fn.py
  requiredBy: []
  timestamp: '2024-11-04 21:00:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc184_f_subset_sum_fn.test.py
documentation_of: cp_library/math/subset_sum_fn.py
layout: document
redirect_from:
- /library/cp_library/math/subset_sum_fn.py
- /library/cp_library/math/subset_sum_fn.py.html
title: cp_library/math/subset_sum_fn.py
---