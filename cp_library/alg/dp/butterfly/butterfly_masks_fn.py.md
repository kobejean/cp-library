---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution_snippet.test.py
    title: test/library-checker/set-power-series/subset_convolution_snippet.test.py
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
    \n\n\"\"\"\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2080\n                \u2573          \u2572 \u2571          \u2572\
    \     \u2571          \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2572\u2500\u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2081\n                           \u2573 \u2573   \
    \       \u2572 \u2572 \u2571 \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2082\n                \u2573   \
    \       \u2571 \u2572          \u2572 \u2573 \u2573 \u2571          \n    x\u2086\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n \
    \                                       \u2573 \u2573 \u2573 \u2573         \n\
    \    x\u2081 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2084\n                \u2573          \u2572 \u2571          \u2571 \u2573\
    \ \u2573 \u2572          \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2571\u2500\u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2085\n                           \u2573 \u2573   \
    \       \u2571 \u2571 \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2086\n                \u2573   \
    \       \u2571 \u2572          \u2571     \u2572          \n    x\u2087 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n               \
    \  Algorithms - DP - Butterfly                     \n\"\"\"\n\ndef butterfly_masks(N,\
    \ Z):\n    for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n  \
    \          yield m^b, m\n            m = (m+1)|b\n\ndef fwht(A: list, N: int):\n\
    \    for m0, m1 in butterfly_masks(N, len(A)):\n        a0, a1 = A[m0], A[m1]\n\
    \        A[m0], A[m1] = a0+a1, a0-a1\n    return A\n\ndef subset_zeta(A: list[int],\
    \ N: int):\n    for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] += A[m0]\n\
    \    return A\n\ndef subset_zeta_pair(A: list[int], B: list[int], N: int):\n \
    \   for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] += A[m0]\n      \
    \  B[m1] += B[m0]\n    return A, B\n\ndef subset_mobius(A: list[int], N: int):\n\
    \    for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] -= A[m0]\n    return\
    \ A\n\ndef superset_zeta(A, N: int):\n    for m0, m1 in butterfly_masks(N, len(A)):\n\
    \        A[m0] += A[m1]\n    return A\n\ndef superset_mobius(A, N: int):\n   \
    \ for m0, m1 in butterfly_masks(N, len(A)):\n        A[m0] -= A[m1]\n    return\
    \ A\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n       \
    \ for m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n\n\n\
    def subset_conv(A,B,N):\n    assert len(A) == len(B)\n    Z = (N+1)*(M := 1<<N)\n\
    \    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)\n    for i,p in enumerate(P):\
    \ Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    subset_zeta_pair(Ar, Br, N)\n    for\
    \ i in range(0,Z,M):\n        for j in range(0,Z-i,M):\n            ij = i+j\n\
    \            for k in range(M): Cr[ij|k] += Ar[i|k] * Br[j|k]\n    subset_mobius(Cr,\
    \ N)\n    for i,p in enumerate(P): A[i] = Cr[p<<N|i]\n    return A\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.dp.__header__\n\
    import cp_library.alg.dp.butterfly.__header__\n\ndef butterfly_masks(N, Z):\n\
    \    for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n        \
    \    yield m^b, m\n            m = (m+1)|b\n\ndef fwht(A: list, N: int):\n   \
    \ for m0, m1 in butterfly_masks(N, len(A)):\n        a0, a1 = A[m0], A[m1]\n \
    \       A[m0], A[m1] = a0+a1, a0-a1\n    return A\n\ndef subset_zeta(A: list[int],\
    \ N: int):\n    for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] += A[m0]\n\
    \    return A\n\ndef subset_zeta_pair(A: list[int], B: list[int], N: int):\n \
    \   for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] += A[m0]\n      \
    \  B[m1] += B[m0]\n    return A, B\n\ndef subset_mobius(A: list[int], N: int):\n\
    \    for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] -= A[m0]\n    return\
    \ A\n\ndef superset_zeta(A, N: int):\n    for m0, m1 in butterfly_masks(N, len(A)):\n\
    \        A[m0] += A[m1]\n    return A\n\ndef superset_mobius(A, N: int):\n   \
    \ for m0, m1 in butterfly_masks(N, len(A)):\n        A[m0] -= A[m1]\n    return\
    \ A\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n       \
    \ for m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n\n\n\
    def subset_conv(A,B,N):\n    assert len(A) == len(B)\n    Z = (N+1)*(M := 1<<N)\n\
    \    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)\n    for i,p in enumerate(P):\
    \ Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    subset_zeta_pair(Ar, Br, N)\n    for\
    \ i in range(0,Z,M):\n        for j in range(0,Z-i,M):\n            ij = i+j\n\
    \            for k in range(M): Cr[ij|k] += Ar[i|k] * Br[j|k]\n    subset_mobius(Cr,\
    \ N)\n    for i,p in enumerate(P): A[i] = Cr[p<<N|i]\n    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/dp/butterfly/butterfly_masks_fn.py
  requiredBy: []
  timestamp: '2025-03-09 20:40:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution_snippet.test.py
documentation_of: cp_library/alg/dp/butterfly/butterfly_masks_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/butterfly/butterfly_masks_fn.py
- /library/cp_library/alg/dp/butterfly/butterfly_masks_fn.py.html
title: cp_library/alg/dp/butterfly/butterfly_masks_fn.py
---
