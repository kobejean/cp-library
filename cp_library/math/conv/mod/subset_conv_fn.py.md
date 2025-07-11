---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_conv_fn.py
    title: cp_library/math/conv/mod/isubset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_mobius_fn.py
    title: cp_library/math/conv/subset_mobius_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_zeta_pair_fn.py
    title: cp_library/math/conv/subset_zeta_pair_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution.test.py
    title: test/library-checker/set-power-series/subset_convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution_all.test.py
    title: test/library-checker/set-power-series/subset_convolution_all.test.py
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
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2080\n                \u2573          \u2572 \u2571          \u2572     \u2571\
    \          \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\
    \u2500\u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2081\n                           \u2573 \u2573          \u2572\
    \ \u2572 \u2571 \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2082\n                \u2573          \u2571\
    \ \u2572          \u2572 \u2573 \u2573 \u2571          \n    x\u2086 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n             \
    \                           \u2573 \u2573 \u2573 \u2573         \n    x\u2081\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2084\n \
    \               \u2573          \u2572 \u2571          \u2571 \u2573 \u2573 \u2572\
    \          \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\
    \u2500\u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2085\n                           \u2573 \u2573          \u2571\
    \ \u2571 \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2086\n                \u2573          \u2571\
    \ \u2572          \u2571     \u2572          \n    x\u2087 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                      Math - Convolution\
    \                     \n'''\n\n\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n   \
    \ for i in range(N):\n        for m in range(b := 1<<i):\n            P[m^b] =\
    \ P[m] + 1\n    return P\n\ndef subset_zeta_pair(A: list[int], B: list[int], N:\
    \ int):\n    Z = len(A)\n    for i in range(N):\n        m = b = 1<<i\n      \
    \  while m < Z: A[m] += A[m^b]; B[m] += B[m^b]; m = m+1|b\n    return A, B\n\n\
    def subset_mobius(A: list[int], N: int):\n    Z = len(A)\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z: A[m] -= A[m^b]; m = m+1|b\n    return\
    \ A\n\ndef isubset_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:\n\
    \    assert len(A) == len(B)\n    Z = (N+1)*(M := 1<<N)\n    Ar,Br,Cr,P = [0]*Z,\
    \ [0]*Z, [0]*Z, popcnts(N)\n    for i,p in enumerate(P):\n        P[i] = p = p<<N|i\n\
    \        Ar[p], Br[p] = A[i], B[i]\n    subset_zeta_pair(Ar, Br, N)\n    for i\
    \ in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod\n    for i in range(0,Z,M):\n\
    \        for j in range(0,Z-i,M):\n            ij = i+j\n            for k in\
    \ range(M): Cr[ijk] = (Cr[ijk:=ij|k] + Ar[i|k] * Br[j|k]) % mod\n    subset_mobius(Cr,\
    \ N)\n    for i,p in enumerate(P): A[i] = Cr[p] % mod\n    return A\n\ndef subset_conv(A:\
    \ list[int], B: list[int], N: int, mod: int) -> list[int]:\n    return isubset_conv(list(A),\
    \ B, N, mod)\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    import cp_library.math.conv.mod.__header__\nfrom cp_library.math.conv.mod.isubset_conv_fn\
    \ import isubset_conv\n\ndef subset_conv(A: list[int], B: list[int], N: int, mod:\
    \ int) -> list[int]:\n    return isubset_conv(list(A), B, N, mod)"
  dependsOn:
  - cp_library/math/conv/mod/isubset_conv_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/subset_zeta_pair_fn.py
  - cp_library/math/conv/subset_mobius_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/mod/subset_conv_fn.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution.test.py
  - test/library-checker/set-power-series/subset_convolution_all.test.py
documentation_of: cp_library/math/conv/mod/subset_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/mod/subset_conv_fn.py
- /library/cp_library/math/conv/mod/subset_conv_fn.py.html
title: cp_library/math/conv/mod/subset_conv_fn.py
---
