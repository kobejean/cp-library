---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/monotone_minima_fn.py
    title: cp_library/alg/dp/monotone_minima_fn.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc325_f_minplus_conv_inplace.test.py
    title: test/atcoder/abc/abc325_f_minplus_conv_inplace.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
    title: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/min_plus_convolution_convex_convex.test.py
    title: test/library-checker/convolution/min_plus_convolution_convex_convex.test.py
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
    \nfrom typing import Callable\n\ndef monotone_minima(N: int, M: int, func: Callable[[int,int,int],bool]):\n\
    \    '''\n    Finds row minima in a totally monotone N\xD7M matrix using the SMAWK\
    \ algorithm.\n    The matrix is defined implicitly through the comparison function.\n\
    \    \n    A matrix is totally monotone if the minimum in row i occurs at column\
    \ j,\n    then the minimum in row i+1 must occur at column j' where j \u2264 j'.\n\
    \    \n    Time: O(N log M), Space: O(N)\n    \n    Args:\n        N: Number of\
    \ rows\n        M: Number of columns\n        func(i,j,k): Returns True if element\
    \ (i,j) < element (i,k)\n    \n    Returns:\n        List of column indices containing\
    \ the minimum value for each row\n    \n    Example:\n        # Find minima where\
    \ each element is (i-j)\xB2\n        min_indices = monotone_minima(5, 5, lambda\
    \ i,j,k: (i-j)**2 < (i-k)**2)\n    '''\n    min_j, st = [0] * N, elist(N)\n  \
    \  st.append((0, N, 0, M))\n    while st:\n        li, ri, lj, rj = st.pop()\n\
    \        if li == ri: continue\n        mi, mj = li + ri >> 1, lj\n        for\
    \ j in range(lj + 1, rj):\n            if func(mi, mj, j): mj = j\n        min_j[mi]\
    \ = mj\n        st.append((li, mi, lj, mj+1))\n        st.append((mi+1, ri, mj,\
    \ rj))\n    return min_j\n\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n \
    \   from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n    x\u2080 \u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\n                \u2573\
    \          \u2572 \u2571          \u2572     \u2571          \n    x\u2084 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2500\u2500\u2571\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2081\n       \
    \                    \u2573 \u2573          \u2572 \u2572 \u2571 \u2571      \
    \    \n    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\
    \u2573\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2082\n                \u2573          \u2571 \u2572          \u2572\
    \ \u2573 \u2573 \u2571          \n    x\u2086 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2083\n                                     \
    \   \u2573 \u2573 \u2573 \u2573         \n    x\u2081 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2084\n                \u2573   \
    \       \u2572 \u2571          \u2571 \u2573 \u2573 \u2572          \n    x\u2085\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2573\u2500\u2572\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2085\n \
    \                          \u2573 \u2573          \u2571 \u2571 \u2572 \u2572\
    \          \n    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\
    \u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2086\n                \u2573          \u2571 \u2572          \u2571\
    \     \u2572          \n    x\u2087 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n                      Math - Convolution           \
    \          \n'''\n\ndef minplus_conv_arb_cnvx(arb: list[int], cnvx: list[int])\
    \ -> list[int]:\n    N, M = len(cnvx), len(arb)\n    def cmp(i, j, k):\n     \
    \   return i >= k and (i-j >= N or (cnvx[i-j] + arb[j] >= cnvx[i-k] + arb[k]))\n\
    \    cols = monotone_minima(N+M-1, M, cmp)\n    return [arb[j] + cnvx[i-j] for\
    \ i, j in enumerate(cols)]\n\ndef minplus_conv_cnvx(A: list[int], B: list[int])\
    \ -> list[int]:\n    if not (N := len(A)) | (M := len(B)): return []\n    C =\
    \ [0] * (K:=N+M-1)\n    C[0], I, J = A[i := 0] + B[j := 0], N-1, M-1\n    for\
    \ k in range(1, K):\n        if j == J or (i != I and A[i+1] + B[j] < A[i] + B[j+1]):\
    \ i += 1\n        else: j += 1\n        C[k] = A[i] + B[j]\n    return C\n\ndef\
    \ minplus_iconv(A: list[int], B: list[int]):\n    N, M = len(A), len(B)\n    for\
    \ i in range(N-1,-1,-1):\n        A[i] = min(B[j] + A[i-j] for j in range(min(M,i+1)))\
    \   \n"
  code: "import cp_library.__header__\nfrom cp_library.alg.dp.monotone_minima_fn import\
    \ monotone_minima\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    \ndef minplus_conv_arb_cnvx(arb: list[int], cnvx: list[int]) -> list[int]:\n \
    \   N, M = len(cnvx), len(arb)\n    def cmp(i, j, k):\n        return i >= k and\
    \ (i-j >= N or (cnvx[i-j] + arb[j] >= cnvx[i-k] + arb[k]))\n    cols = monotone_minima(N+M-1,\
    \ M, cmp)\n    return [arb[j] + cnvx[i-j] for i, j in enumerate(cols)]\n\ndef\
    \ minplus_conv_cnvx(A: list[int], B: list[int]) -> list[int]:\n    if not (N :=\
    \ len(A)) | (M := len(B)): return []\n    C = [0] * (K:=N+M-1)\n    C[0], I, J\
    \ = A[i := 0] + B[j := 0], N-1, M-1\n    for k in range(1, K):\n        if j ==\
    \ J or (i != I and A[i+1] + B[j] < A[i] + B[j+1]): i += 1\n        else: j +=\
    \ 1\n        C[k] = A[i] + B[j]\n    return C\n\ndef minplus_iconv(A: list[int],\
    \ B: list[int]):\n    N, M = len(A), len(B)\n    for i in range(N-1,-1,-1):\n\
    \        A[i] = min(B[j] + A[i-j] for j in range(min(M,i+1)))   \n"
  dependsOn:
  - cp_library/alg/dp/monotone_minima_fn.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/minplus_conv_fn.py
  requiredBy: []
  timestamp: '2025-04-02 01:29:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
  - test/library-checker/convolution/min_plus_convolution_convex_convex.test.py
  - test/atcoder/abc/abc325_f_minplus_conv_inplace.test.py
documentation_of: cp_library/math/conv/minplus_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/minplus_conv_fn.py
- /library/cp_library/math/conv/minplus_conv_fn.py.html
title: cp_library/math/conv/minplus_conv_fn.py
---
