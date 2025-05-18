---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: cp_library/alg/iter/arg/argsort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
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
    \n\n\n\ndef argsort(A: list[int], reverse=False):\n    s, m = pack_sm(len(A))\n\
    \    if reverse:\n        I = [a<<s|m^i for i,a in enumerate(A)]\n        I.sort(reverse=True)\n\
    \        for i,ai in enumerate(I): I[i] = m^ai&m\n    else:\n        I = [a<<s|i\
    \ for i,a in enumerate(A)]\n        I.sort()\n        for i,ai in enumerate(I):\
    \ I[i] = ai&m\n    return I\n\n\ndef pack_sm(N: int): s=N.bit_length(); return\
    \ s,(1<<s)-1\n\n\ndef sort_parallel(*L: list, reverse=False):\n    N, K, order\
    \ = len(L[0]), len(L), argsort(L[0], reverse)\n    R = tuple([0]*N for _ in range(K))\n\
    \    for k, Lk in enumerate(L):\n        Rk = R[k]\n        for i, j in enumerate(order):\
    \ Rk[i] = Lk[j]\n    return R\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    from cp_library.alg.iter.arg.argsort_fn import argsort\nimport cp_library.alg.iter.sort.__header__\n\
    \ndef sort_parallel(*L: list, reverse=False):\n    N, K, order = len(L[0]), len(L),\
    \ argsort(L[0], reverse)\n    R = tuple([0]*N for _ in range(K))\n    for k, Lk\
    \ in enumerate(L):\n        Rk = R[k]\n        for i, j in enumerate(order): Rk[i]\
    \ = Lk[j]\n    return R\n"
  dependsOn:
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/sort/sort_parallel_fn.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sort/sort_parallel_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort/sort_parallel_fn.py
- /library/cp_library/alg/iter/sort/sort_parallel_fn.py.html
title: cp_library/alg/iter/sort/sort_parallel_fn.py
---
