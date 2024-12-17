---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc325_f_minplus_conv_inplace.test.py
    title: test/abc325_f_minplus_conv_inplace.test.py
  - icon: ':heavy_check_mark:'
    path: test/min_plus_convolution_convex_arbitrary.test.py
    title: test/min_plus_convolution_convex_arbitrary.test.py
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
    from typing import Callable\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n\
    \    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n\ndef monotone_minima(N: int,\
    \ M: int, func: Callable[[int,int,int],bool]):\n    min_cols = [0] * N\n    stack:\
    \ list[tuple[int, ...]] = elist(N.bit_length() << 2)\n    stack.append((0, N,\
    \ 0, M))\n\n    while stack:\n        li, ri, lj, rj = stack.pop()\n        if\
    \ li == ri: continue\n        mi = li + ri >> 1\n        min_j = lj\n        for\
    \ j in range(lj + 1, rj):\n            if func(mi, min_j, j):\n              \
    \  min_j = j\n        min_cols[mi] = min_j\n        stack.append((li, mi, lj,\
    \ min_j + 1))\n        stack.append((mi + 1, ri, min_j, rj))\n\n    return min_cols\n\
    \ndef minplus_conv_arb_cnvx(arb: list[int], cnvx: list[int]) -> list[int]:\n \
    \   N, M = len(cnvx), len(arb)\n    \n    def cmp(i, j, k):\n        return i\
    \ >= k and (i-j >= N or (cnvx[i-j] + arb[j] >= cnvx[i-k] + arb[k]))\n    \n  \
    \  cols = monotone_minima(N+M-1, M, cmp)\n    return [arb[j] + cnvx[i-j] for i,\
    \ j in enumerate(cols)]\n\ndef minplus_conv_inplace(A: list[int], B: list[int]):\n\
    \    N, M = len(A), len(B)\n    for i in range(N-1,-1,-1):\n        A[i] = min(B[j]\
    \ + A[i-j] for j in range(min(M,i+1)))   \n"
  code: "import cp_library.math.__header__\nfrom typing import Callable\nfrom cp_library.ds.elist_fn\
    \ import elist\n\ndef monotone_minima(N: int, M: int, func: Callable[[int,int,int],bool]):\n\
    \    min_cols = [0] * N\n    stack: list[tuple[int, ...]] = elist(N.bit_length()\
    \ << 2)\n    stack.append((0, N, 0, M))\n\n    while stack:\n        li, ri, lj,\
    \ rj = stack.pop()\n        if li == ri: continue\n        mi = li + ri >> 1\n\
    \        min_j = lj\n        for j in range(lj + 1, rj):\n            if func(mi,\
    \ min_j, j):\n                min_j = j\n        min_cols[mi] = min_j\n      \
    \  stack.append((li, mi, lj, min_j + 1))\n        stack.append((mi + 1, ri, min_j,\
    \ rj))\n\n    return min_cols\n\ndef minplus_conv_arb_cnvx(arb: list[int], cnvx:\
    \ list[int]) -> list[int]:\n    N, M = len(cnvx), len(arb)\n    \n    def cmp(i,\
    \ j, k):\n        return i >= k and (i-j >= N or (cnvx[i-j] + arb[j] >= cnvx[i-k]\
    \ + arb[k]))\n    \n    cols = monotone_minima(N+M-1, M, cmp)\n    return [arb[j]\
    \ + cnvx[i-j] for i, j in enumerate(cols)]\n\ndef minplus_conv_inplace(A: list[int],\
    \ B: list[int]):\n    N, M = len(A), len(B)\n    for i in range(N-1,-1,-1):\n\
    \        A[i] = min(B[j] + A[i-j] for j in range(min(M,i+1)))   \n"
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/math/minplus_conv_fn.py
  requiredBy: []
  timestamp: '2024-12-17 21:24:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/min_plus_convolution_convex_arbitrary.test.py
  - test/abc325_f_minplus_conv_inplace.test.py
documentation_of: cp_library/math/minplus_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/minplus_conv_fn.py
- /library/cp_library/math/minplus_conv_fn.py.html
title: cp_library/math/minplus_conv_fn.py
---
