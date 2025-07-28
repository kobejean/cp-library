---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
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
    \n\n\n\ndef argsort_multi(*A: list[int], reverse=False):\n    P = Packer((N:=len(A[0]))-1);\
    \ I, J, s, m = [0]*N, [*range(N)], P.s, P.m\n    V = P.enumerate(A[-1], reverse);\
    \ V.sort()\n    if reverse:\n        for B in A[-2::-1]:\n            for i,v\
    \ in enumerate(V):V[i],I[i]=-B[j:=J[v&m]]<<s|i,j\n            I,J=J,I;V.sort()\n\
    \    else:\n        for B in A[-2::-1]:\n            for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j\n\
    \            I,J=J,I;V.sort()\n    for i,v in enumerate(V):I[i]=J[v&m]\n    return\
    \ I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int):\
    \ P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.arg.__header__\n\ndef argsort_multi(*A: list[int],\
    \ reverse=False):\n    P = Packer((N:=len(A[0]))-1); I, J, s, m = [0]*N, [*range(N)],\
    \ P.s, P.m\n    V = P.enumerate(A[-1], reverse); V.sort()\n    if reverse:\n \
    \       for B in A[-2::-1]:\n            for i,v in enumerate(V):V[i],I[i]=-B[j:=J[v&m]]<<s|i,j\n\
    \            I,J=J,I;V.sort()\n    else:\n        for B in A[-2::-1]:\n      \
    \      for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j\n            I,J=J,I;V.sort()\n\
    \    for i,v in enumerate(V):I[i]=J[v&m]\n    return I\nfrom cp_library.bit.pack.packer_cls\
    \ import Packer"
  dependsOn:
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: cp_library/alg/iter/arg/argsort_multi_fn.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
documentation_of: cp_library/alg/iter/arg/argsort_multi_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/arg/argsort_multi_fn.py
- /library/cp_library/alg/iter/arg/argsort_multi_fn.py.html
title: cp_library/alg/iter/arg/argsort_multi_fn.py
---
