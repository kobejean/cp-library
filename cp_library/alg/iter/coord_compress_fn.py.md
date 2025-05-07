---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    \n\n\ndef coord_compress(A: list[int], distinct = False):\n    s, m = pack_sm((N\
    \ := len(A))-1)\n    R, V, S = [0]*N, elist(N), [a<<s|i for i,a in enumerate(A)];\
    \ S.sort()\n    r = p = -1\n    for ai in S:\n        a, i = pack_dec(ai, s, m)\n\
    \        if a != p or distinct: r, p = r+1, a; V.append(a)\n        R[i] = r\n\
    \    return R, V\n\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__\
    \ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\n\
    elist = newlist_hint\n    \n\n\ndef pack_sm(N: int):\n    s = N.bit_length()\n\
    \    return s, (1<<s)-1\n\ndef pack_enc(a: int, b: int, s: int):\n    return a\
    \ << s | b\n    \ndef pack_dec(ab: int, s: int, m: int):\n    return ab >> s,\
    \ ab & m\n\ndef pack_indices(A, s):\n    return [a << s | i for i,a in enumerate(A)]\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \ndef coord_compress(A: list[int], distinct = False):\n    s, m = pack_sm((N :=\
    \ len(A))-1)\n    R, V, S = [0]*N, elist(N), [a<<s|i for i,a in enumerate(A)];\
    \ S.sort()\n    r = p = -1\n    for ai in S:\n        a, i = pack_dec(ai, s, m)\n\
    \        if a != p or distinct: r, p = r+1, a; V.append(a)\n        R[i] = r\n\
    \    return R, V\n\nfrom cp_library.ds.elist_fn import elist\nfrom cp_library.bit.pack_sm_fn\
    \ import pack_dec, pack_sm"
  dependsOn:
  - cp_library/ds/elist_fn.py
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/coord_compress_fn.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/coord_compress_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/coord_compress_fn.py
- /library/cp_library/alg/iter/coord_compress_fn.py.html
title: cp_library/alg/iter/coord_compress_fn.py
---
