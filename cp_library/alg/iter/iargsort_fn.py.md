---
data:
  _extendedDependsOn:
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
    \    return [a << s | i for i,a in enumerate(A)]\n\ndef iargsort(A: list[int],\
    \ reverse=False):\n    s, m = pack_sm(len(A))\n    if reverse:\n        for i,a\
    \ in enumerate(A): A[i] = a<<s|i^m\n        A.sort(reverse=True)\n        for\
    \ i,a in enumerate(A): A[i] = (a^m)&m\n    else:\n        for i,a in enumerate(A):\
    \ A[i] = a<<s|i\n        A.sort()\n        for i,a in enumerate(A): A[i] = a&m\n\
    \    return A\n"
  code: "import cp_library.alg.iter.__header__\nfrom cp_library.bit.pack_sm_fn import\
    \ pack_sm\n\ndef iargsort(A: list[int], reverse=False):\n    s, m = pack_sm(len(A))\n\
    \    if reverse:\n        for i,a in enumerate(A): A[i] = a<<s|i^m\n        A.sort(reverse=True)\n\
    \        for i,a in enumerate(A): A[i] = (a^m)&m\n    else:\n        for i,a in\
    \ enumerate(A): A[i] = a<<s|i\n        A.sort()\n        for i,a in enumerate(A):\
    \ A[i] = a&m\n    return A\n"
  dependsOn:
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/iargsort_fn.py
  requiredBy: []
  timestamp: '2025-04-03 08:59:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/iargsort_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/iargsort_fn.py
- /library/cp_library/alg/iter/iargsort_fn.py.html
title: cp_library/alg/iter/iargsort_fn.py
---
