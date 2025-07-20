---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/bisect_left_fn.py
    title: cp_library/alg/divcon/bisect_left_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/other/longest_increasing_sequence.test.py
    title: test/library-checker/other/longest_increasing_sequence.test.py
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
    \n\n\ndef bisect_left(A, x, l, r):\n    while l<r:\n        if A[m:=(l+r)>>1]<x:l=m+1\n\
    \        else:r=m\n    return l\n\n\ndef max2(a, b):\n    return a if a > b else\
    \ b\n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return ch\n\ndef\
    \ lis(A: list):\n    '''Returns indices of a longest increasing sequence'''\n\
    \    N = len(A)\n    mn, mx = min(A), max(A)\n    dp, idx, prev = [mx+1]*(N+1),\
    \ [-1]*(N+1), [-1]*N\n    dp[0], r = mn-1, 0\n    for i,a in enumerate(A):\n \
    \       if chmin(dp, p := bisect_left(dp,a,0,r+1), a):\n            idx[p], prev[i],\
    \ r = i, idx[p-1], max2(r,p)\n    ans, i = [0]*r, idx[r]\n    for j in range(r-1,-1,-1):\
    \ ans[j], i = i, prev[i]\n    return ans\n\n    \n\n"
  code: "import cp_library.__header__\nfrom cp_library.alg.divcon.bisect_left_fn import\
    \ bisect_left\nimport cp_library.alg.__header__\nimport cp_library.alg.dp.__header__\n\
    from cp_library.alg.dp.max2_fn import max2\nfrom cp_library.alg.dp.chmin_fn import\
    \ chmin\n\ndef lis(A: list):\n    '''Returns indices of a longest increasing sequence'''\n\
    \    N = len(A)\n    mn, mx = min(A), max(A)\n    dp, idx, prev = [mx+1]*(N+1),\
    \ [-1]*(N+1), [-1]*N\n    dp[0], r = mn-1, 0\n    for i,a in enumerate(A):\n \
    \       if chmin(dp, p := bisect_left(dp,a,0,r+1), a):\n            idx[p], prev[i],\
    \ r = i, idx[p-1], max2(r,p)\n    ans, i = [0]*r, idx[r]\n    for j in range(r-1,-1,-1):\
    \ ans[j], i = i, prev[i]\n    return ans\n\n    \n\n"
  dependsOn:
  - cp_library/alg/divcon/bisect_left_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/alg/dp/chmin_fn.py
  isVerificationFile: false
  path: cp_library/alg/dp/lis_fn.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/other/longest_increasing_sequence.test.py
documentation_of: cp_library/alg/dp/lis_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/lis_fn.py
- /library/cp_library/alg/dp/lis_fn.py.html
title: cp_library/alg/dp/lis_fn.py
---
