---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/incremental_scc.test.py
    title: test/library-checker/graph/incremental_scc.test.py
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
    \n\n\n\ndef argsort(A: list[int], reverse=False):\n    P = Packer(len(I := list(A))-1);\
    \ P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n    return I\n\n\n\nclass\
    \ Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length();\
    \ P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n\
    \    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def\
    \ enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A\n\
    \    def ienumerate(P, A, reverse=False):\n        if reverse:\n            for\
    \ i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n            for i,a\
    \ in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A));\
    \ return A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\
    \ndef argsort_bounded(A, mx=None, reverse=False):\n    N = len(A)\n    if mx is\
    \ None: mx = max(A)\n    if N*N.bit_length() < mx or mx < 1000: return argsort(A,\
    \ reverse)\n    I, cnt, t = [0]*N, [0]*(mx+1), 0\n    for a in A: cnt[a] += 1\n\
    \    if reverse:\n        for a in range(mx+1): cnt[~a], t = t, t+cnt[~a]\n  \
    \  else:\n        for a in range(mx+1): cnt[a], t = t, t+cnt[a]\n    for i,a in\
    \ enumerate(A): I[cnt[a]] = i; cnt[a] += 1\n    return I\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.arg.__header__\nfrom cp_library.alg.iter.arg.argsort_fn\
    \ import argsort\n\ndef argsort_bounded(A, mx=None, reverse=False):\n    N = len(A)\n\
    \    if mx is None: mx = max(A)\n    if N*N.bit_length() < mx or mx < 1000: return\
    \ argsort(A, reverse)\n    I, cnt, t = [0]*N, [0]*(mx+1), 0\n    for a in A: cnt[a]\
    \ += 1\n    if reverse:\n        for a in range(mx+1): cnt[~a], t = t, t+cnt[~a]\n\
    \    else:\n        for a in range(mx+1): cnt[a], t = t, t+cnt[a]\n    for i,a\
    \ in enumerate(A): I[cnt[a]] = i; cnt[a] += 1\n    return I"
  dependsOn:
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: cp_library/alg/iter/arg/argsort_bounded_fn.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/incremental_scc.test.py
documentation_of: cp_library/alg/iter/arg/argsort_bounded_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/arg/argsort_bounded_fn.py
- /library/cp_library/alg/iter/arg/argsort_bounded_fn.py.html
title: cp_library/alg/iter/arg/argsort_bounded_fn.py
---
