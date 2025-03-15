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
    \ndef sort_parallel(*L: list, reverse=False):\n    inv, order = [-1]*(N := len(L[0])),\
    \ argsort(L[0], reverse=reverse)\n    for i, idx in enumerate(order): inv[idx]\
    \ = i\n    for j in range(N):\n        i, k = inv[j], order[j]\n        for A\
    \ in L: A[j], A[k] = A[k], A[j] \n        order[i], inv[k] = k, i\n    return\
    \ L\n"
  code: "import cp_library.alg.iter.__header__\nfrom cp_library.alg.iter.argsort_fn\
    \ import argsort\n\ndef sort_parallel(*L: list, reverse=False):\n    inv, order\
    \ = [-1]*(N := len(L[0])), argsort(L[0], reverse=reverse)\n    for i, idx in enumerate(order):\
    \ inv[idx] = i\n    for j in range(N):\n        i, k = inv[j], order[j]\n    \
    \    for A in L: A[j], A[k] = A[k], A[j] \n        order[i], inv[k] = k, i\n \
    \   return L\n"
  dependsOn:
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/sort_parallel_fn.py
  requiredBy: []
  timestamp: '2025-03-15 19:36:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sort_parallel_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort_parallel_fn.py
- /library/cp_library/alg/iter/sort_parallel_fn.py.html
title: cp_library/alg/iter/sort_parallel_fn.py
---
