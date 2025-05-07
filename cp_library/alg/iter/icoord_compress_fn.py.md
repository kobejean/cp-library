---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet_matrix_cls.py
    title: cp_library/ds/wavelet_matrix_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/range_kth_smallest.test.py
    title: test/library-checker/data-structure/range_kth_smallest.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_range_frequency_wavelet_matrix.test.py
    title: test/library-checker/data-structure/static_range_frequency_wavelet_matrix.test.py
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
    \n\n\ndef icoord_compress(A: list[int]):\n    s, m = pack_sm((N := len(A))-1)\n\
    \    R, V = [0]*N, [0]*N\n    for i,a in enumerate(A): A[i] = a<<s|i\n    A.sort()\n\
    \    r = p = -1\n    for ai in A:\n        a, i = pack_dec(ai, s, m)\n       \
    \ if a != p: V[r:=r+1] = p = a\n        R[i] = r\n    del V[r+1:]\n    return\
    \ R, V\n\n\n\ndef pack_sm(N: int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\
    \ndef pack_enc(a: int, b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab:\
    \ int, s: int, m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n\
    \    return [a << s | i for i,a in enumerate(A)]\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \ndef icoord_compress(A: list[int]):\n    s, m = pack_sm((N := len(A))-1)\n  \
    \  R, V = [0]*N, [0]*N\n    for i,a in enumerate(A): A[i] = a<<s|i\n    A.sort()\n\
    \    r = p = -1\n    for ai in A:\n        a, i = pack_dec(ai, s, m)\n       \
    \ if a != p: V[r:=r+1] = p = a\n        R[i] = r\n    del V[r+1:]\n    return\
    \ R, V\n\nfrom cp_library.bit.pack_sm_fn import pack_dec, pack_sm"
  dependsOn:
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/icoord_compress_fn.py
  requiredBy:
  - cp_library/ds/wavelet_matrix_cls.py
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/static_range_frequency_wavelet_matrix.test.py
  - test/library-checker/data-structure/range_kth_smallest.test.py
documentation_of: cp_library/alg/iter/icoord_compress_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/icoord_compress_fn.py
- /library/cp_library/alg/iter/icoord_compress_fn.py.html
title: cp_library/alg/iter/icoord_compress_fn.py
---
