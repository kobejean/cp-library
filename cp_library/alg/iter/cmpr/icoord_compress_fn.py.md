---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_dec_fn.py
    title: cp_library/bit/pack/pack_dec_fn.py
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
    \n\n\n\ndef coord_compress(A: list[int], distinct = False):\n    s, m = pack_sm(len(A)-1)\n\
    \    V = [a<<s|i for i,a in enumerate(A)]; V.sort()\n    if distinct:\n      \
    \  for r, ai in enumerate(V): a, i = pack_dec(ai, s, m); A[i], V[r] = r, a\n \
    \   else:\n        r = p = -1\n        for ai in V:\n            a, i = pack_dec(ai,\
    \ s, m)\n            if a != p: r = r+1; V[r] = p = a\n            A[i] = r\n\
    \        del V[r+1:]\n    return A, V\n\n\ndef pack_dec(ab: int, s: int, m: int):\
    \ return ab>>s,ab&m\ndef pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.cmpr.__header__\n\ndef coord_compress(A: list[int],\
    \ distinct = False):\n    s, m = pack_sm(len(A)-1)\n    V = [a<<s|i for i,a in\
    \ enumerate(A)]; V.sort()\n    if distinct:\n        for r, ai in enumerate(V):\
    \ a, i = pack_dec(ai, s, m); A[i], V[r] = r, a\n    else:\n        r = p = -1\n\
    \        for ai in V:\n            a, i = pack_dec(ai, s, m)\n            if a\
    \ != p: r = r+1; V[r] = p = a\n            A[i] = r\n        del V[r+1:]\n   \
    \ return A, V\nfrom cp_library.bit.pack.pack_dec_fn import pack_dec\nfrom cp_library.bit.pack.pack_sm_fn\
    \ import pack_sm"
  dependsOn:
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/cmpr/icoord_compress_fn.py
  requiredBy: []
  timestamp: '2025-05-20 05:03:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/cmpr/icoord_compress_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/cmpr/icoord_compress_fn.py
- /library/cp_library/alg/iter/cmpr/icoord_compress_fn.py.html
title: cp_library/alg/iter/cmpr/icoord_compress_fn.py
---
