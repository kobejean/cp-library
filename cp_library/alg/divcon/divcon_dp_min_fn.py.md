---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
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
    \n\n\n\ndef min2(a, b):\n    return a if a < b else b\n    \ndef divcon_dp_min(N,\
    \ M, cost_fn, default = 1<<62):\n    dp, ndp = [default]*N, [default]*N\n    for\
    \ i in range(N): dp[i] = cost_fn(0,i)\n    def rec(l, r, optl, optr):\n      \
    \  first, last = optl, optr\n        i, j = optl, min2(m := (l+r)>>1, optr+1)\n\
    \        ndp[m] = default\n        while i < j:\n            if (cost:=dp[i]+cost_fn(i,m))\
    \ < ndp[m]:\n                ndp[m] = cost\n                first = last = i\n\
    \            elif ndp[m] == cost:\n                last = i\n            i +=\
    \ 1\n        if r <= l: return\n        rec(l, m-1, optl, first)\n        rec(m+1,\
    \ r, last, optr)\n    for _ in range(1,M):\n        rec(0, N-1, 0, N-1)\n    \
    \    dp, ndp = ndp, dp\n    return dp\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.divcon.__header__\n\
    from cp_library.alg.dp.min2_fn import min2\n    \ndef divcon_dp_min(N, M, cost_fn,\
    \ default = 1<<62):\n    dp, ndp = [default]*N, [default]*N\n    for i in range(N):\
    \ dp[i] = cost_fn(0,i)\n    def rec(l, r, optl, optr):\n        first, last =\
    \ optl, optr\n        i, j = optl, min2(m := (l+r)>>1, optr+1)\n        ndp[m]\
    \ = default\n        while i < j:\n            if (cost:=dp[i]+cost_fn(i,m)) <\
    \ ndp[m]:\n                ndp[m] = cost\n                first = last = i\n \
    \           elif ndp[m] == cost:\n                last = i\n            i += 1\n\
    \        if r <= l: return\n        rec(l, m-1, optl, first)\n        rec(m+1,\
    \ r, last, optr)\n    for _ in range(1,M):\n        rec(0, N-1, 0, N-1)\n    \
    \    dp, ndp = ndp, dp\n    return dp"
  dependsOn:
  - cp_library/alg/dp/min2_fn.py
  isVerificationFile: false
  path: cp_library/alg/divcon/divcon_dp_min_fn.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/divcon/divcon_dp_min_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/divcon_dp_min_fn.py
- /library/cp_library/alg/divcon/divcon_dp_min_fn.py.html
title: cp_library/alg/divcon/divcon_dp_min_fn.py
---
