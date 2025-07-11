---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
    title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
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
    \n\n\ndef max2(a, b):\n    return a if a > b else b\n\n\n\ndef icoord_compress_with_queries(*A:\
    \ list[int], x=0, distinct=False):\n    N = mx = 0\n    for Ai in A: N += len(Ai);\
    \ mx = max2(mx, len(Ai))\n    si, mi = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)\n\
    \    S, k = [0]*N, 0\n    for i,Ai in enumerate(A):\n        for j,a in enumerate(Ai):\
    \ S[k]=a << sj | i << si | j; k += 1\n    S.sort(); r = p = -1\n    for aji in\
    \ S:\n        a, i, j = aji >> sj, (aji&mj) >> si , aji & mi\n        if x<=i\
    \ and (distinct or a != p): r = r+1; p = a\n        A[i][j] = r+(i<x)\n    return\
    \ A\n\n\ndef pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nfrom cp_library.alg.dp.max2_fn\
    \ import max2\nimport cp_library.alg.iter.__header__\nimport cp_library.alg.iter.cmpr.__header__\n\
    \ndef icoord_compress_with_queries(*A: list[int], x=0, distinct=False):\n    N\
    \ = mx = 0\n    for Ai in A: N += len(Ai); mx = max2(mx, len(Ai))\n    si, mi\
    \ = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)\n    S, k = [0]*N, 0\n   \
    \ for i,Ai in enumerate(A):\n        for j,a in enumerate(Ai): S[k]=a << sj |\
    \ i << si | j; k += 1\n    S.sort(); r = p = -1\n    for aji in S:\n        a,\
    \ i, j = aji >> sj, (aji&mj) >> si , aji & mi\n        if x<=i and (distinct or\
    \ a != p): r = r+1; p = a\n        A[i][j] = r+(i<x)\n    return A\nfrom cp_library.bit.pack.pack_sm_fn\
    \ import pack_sm"
  dependsOn:
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
documentation_of: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
- /library/cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py.html
title: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
---
