---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_ranked_fn.py
    title: cp_library/math/conv/ior_mobius_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
    title: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/isubset_conv_ranked_fn.py
    title: cp_library/math/conv/isubset_conv_ranked_fn.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/sps/sps_exp_fn.py
    title: cp_library/math/sps/sps_exp_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_mul_fn.py
    title: cp_library/math/sps/sps_mul_fn.py
  _extendedVerifiedWith:
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
    \n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n        for\
    \ m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n\n'''\n\
    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \ x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\
    \n                \u2573          \u2572 \u2571          \u2572     \u2571   \
    \       \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\
    \u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2081\n                           \u2573 \u2573          \u2572 \u2572\
    \ \u2571 \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2082\n                \u2573          \u2571 \u2572\
    \          \u2572 \u2573 \u2573 \u2571          \n    x\u2086 \u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n                   \
    \                     \u2573 \u2573 \u2573 \u2573         \n    x\u2081 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2084\n       \
    \         \u2573          \u2572 \u2571          \u2571 \u2573 \u2573 \u2572 \
    \         \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
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
    \                     \n'''\n\n\ndef max2(a, b): return a if a > b else b\n\n\
    def ior_zeta_pair_ranked(A, B, N, M, Z):\n    for i in range(0, Z, M):\n     \
    \   l, r = i+(1<<(i>>N))-1, i+M\n        for j in range(N):\n            m = l|(b\
    \ := 1<<j)\n            while m < r: A[m] += A[m^b]; B[m] += B[m^b]; m = m+1|b\n\
    \    return A, B\n\ndef ior_mobius_ranked(A: list[int], N: int, M: int, Z: int):\n\
    \    for i in range(0, Z, M):\n        l, r = i, i+M-(1<<(N-(i>>N)))+1\n     \
    \   for j in range(N):\n            m = l|(b := 1<<j)\n            while m < r:\
    \ A[m] -= A[m^b]; m = m+1|b\n    return A\n\ndef isubset_conv_ranked(Ar, Br, N,\
    \ M, Z) -> list[int]:\n    ior_zeta_pair_ranked(Ar, Br, N, M, Z)\n    for ij in\
    \ range(Z-M,-1,-M):\n        for k in range(M): Ar[ij|k] *= Br[k]\n        r =\
    \ M-(1 << (N-(ij>>N)))+1\n        for i in range(0,ij,M):\n            j = ij-i;\
    \ l = (1 << (max2(i,j)>>N))-1\n            for k in range(l,r): Ar[ij|k] += Ar[i|k]\
    \ * Br[j|k]\n    return ior_mobius_ranked(Ar, N, M, Z)\n\ndef subset_conv(A: list[int],\
    \ B: list[int], N: int) -> list[int]:\n    Z = (N+1)*(M:=1<<N)\n    Ar, Br, P\
    \ = [0]*Z, [0]*Z, popcnts(N)\n    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i]\
    \ = A[i], B[i]\n    isubset_conv_ranked(Ar, Br, N, M, Z)\n    return [Ar[p<<N|i]\
    \ for i, p in enumerate(P)]\n"
  code: "import cp_library.__header__\nfrom cp_library.bit.popcnts_fn import popcnts\n\
    import cp_library.math.__header__\nimport cp_library.math.conv.__header__\nfrom\
    \ cp_library.math.conv.isubset_conv_ranked_fn import isubset_conv_ranked\n\ndef\
    \ subset_conv(A: list[int], B: list[int], N: int) -> list[int]:\n    Z = (N+1)*(M:=1<<N)\n\
    \    Ar, Br, P = [0]*Z, [0]*Z, popcnts(N)\n    for i, p in enumerate(P): Ar[p<<N|i],\
    \ Br[p<<N|i] = A[i], B[i]\n    isubset_conv_ranked(Ar, Br, N, M, Z)\n    return\
    \ [Ar[p<<N|i] for i, p in enumerate(P)]"
  dependsOn:
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/isubset_conv_ranked_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/subset_conv_fn.py
  requiredBy:
  - cp_library/math/sps/sps_mul_fn.py
  - cp_library/math/sps/sps_exp_fn.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution_all.test.py
documentation_of: cp_library/math/conv/subset_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/subset_conv_fn.py
- /library/cp_library/math/conv/subset_conv_fn.py.html
title: cp_library/math/conv/subset_conv_fn.py
---
