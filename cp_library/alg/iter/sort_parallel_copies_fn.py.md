---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
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
    \n\ndef pack_sm(N: int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\ndef\
    \ pack_enc(a: int, b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab:\
    \ int, s: int, m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n\
    \    return [a << s | i for i,a in enumerate(A)]\n\ndef argsort(A: list[int],\
    \ reverse=False):\n    s, m = pack_sm(len(A))\n    if reverse:\n        I = [a<<s|i^m\
    \ for i,a in enumerate(A)]\n        I.sort(reverse=True)\n        for i,ai in\
    \ enumerate(I): I[i] = (ai^m)&m\n    else:\n        I = [a<<s|i for i,a in enumerate(A)]\n\
    \        I.sort()\n        for i,ai in enumerate(I): I[i] = ai&m\n    return I\n\
    \ndef sort_parallel_copies(*L: list, reverse=False):\n    N, K, order = len(L[0]),\
    \ len(L), argsort(L[0], reverse)\n    R = tuple([0]*N for _ in range(K))\n   \
    \ for k, Llst in enumerate(L):\n        Rlst = R[k]\n        for ri, li in enumerate(order):\n\
    \            Rlst[ri] = Llst[li]\n    return R\n"
  code: "import cp_library.alg.iter.__header__\nfrom cp_library.alg.iter.argsort_fn\
    \ import argsort\n\ndef sort_parallel_copies(*L: list, reverse=False):\n    N,\
    \ K, order = len(L[0]), len(L), argsort(L[0], reverse)\n    R = tuple([0]*N for\
    \ _ in range(K))\n    for k, Llst in enumerate(L):\n        Rlst = R[k]\n    \
    \    for ri, li in enumerate(order):\n            Rlst[ri] = Llst[li]\n    return\
    \ R\n"
  dependsOn:
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/sort_parallel_copies_fn.py
  requiredBy: []
  timestamp: '2025-03-27 22:10:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sort_parallel_copies_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort_parallel_copies_fn.py
- /library/cp_library/alg/iter/sort_parallel_copies_fn.py.html
title: cp_library/alg/iter/sort_parallel_copies_fn.py
---
