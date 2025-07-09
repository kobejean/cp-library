---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':warning:'
    path: cp_library/alg/iter/rank/rank_multi_fn.py
    title: cp_library/alg/iter/rank/rank_multi_fn.py
  - icon: ':warning:'
    path: cp_library/perf/examples/rank_benchmark.py
    title: cp_library/perf/examples/rank_benchmark.py
  - icon: ':warning:'
    path: perf/rank.py
    title: perf/rank.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
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
    \n\n\nclass Packer3:\n    def __init__(P, mxb: int, mxc: int):\n        bb, bc\
    \ = mxb.bit_length(), mxc.bit_length()\n        P.mc, P.mb, P.sb, P.sa = (1<<bc)-1,\
    \ (1<<bb)-1, bc, bc+bb\n    def enc(P, a: int, b: int, c: int): return a << P.sa\
    \ | b << P.sb | c\n    def dec(P, x: int) -> tuple[int, int, int]: return x >>\
    \ P.sa, (x >> P.sb) & P.mb, x & P.mc\n    def enumerate(P, A, N, reverse=False):\
    \ \n        V, k = [0]*N, 0\n        if reverse:\n            for i,Ai in enumerate(A):\n\
    \                for j, a in enumerate(Ai):V[k]=P.enc(-a, i, j);k+=1\n       \
    \ else:\n            for i,Ai in enumerate(A):\n                for j, a in enumerate(Ai):V[k]=P.enc(a,\
    \ i, j);k+=1\n        return V\n"
  code: "import cp_library.__header__\nimport cp_library.bit.__header__\nimport cp_library.bit.pack.__header__\n\
    \nclass Packer3:\n    def __init__(P, mxb: int, mxc: int):\n        bb, bc = mxb.bit_length(),\
    \ mxc.bit_length()\n        P.mc, P.mb, P.sb, P.sa = (1<<bc)-1, (1<<bb)-1, bc,\
    \ bc+bb\n    def enc(P, a: int, b: int, c: int): return a << P.sa | b << P.sb\
    \ | c\n    def dec(P, x: int) -> tuple[int, int, int]: return x >> P.sa, (x >>\
    \ P.sb) & P.mb, x & P.mc\n    def enumerate(P, A, N, reverse=False): \n      \
    \  V, k = [0]*N, 0\n        if reverse:\n            for i,Ai in enumerate(A):\n\
    \                for j, a in enumerate(Ai):V[k]=P.enc(-a, i, j);k+=1\n       \
    \ else:\n            for i,Ai in enumerate(A):\n                for j, a in enumerate(Ai):V[k]=P.enc(a,\
    \ i, j);k+=1\n        return V"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/pack/packer3_cls.py
  requiredBy:
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/alg/iter/rank/rank_multi_fn.py
  - cp_library/perf/examples/rank_benchmark.py
  - perf/rank.py
  timestamp: '2025-07-10 02:39:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_set_range_composite_large_array.test.py
documentation_of: cp_library/bit/pack/packer3_cls.py
layout: document
redirect_from:
- /library/cp_library/bit/pack/packer3_cls.py
- /library/cp_library/bit/pack/packer3_cls.py.html
title: cp_library/bit/pack/packer3_cls.py
---
