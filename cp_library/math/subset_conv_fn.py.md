---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: cp_library/math/subset_mobius_fn.py
    title: cp_library/math/subset_mobius_fn.py
  - icon: ':x:'
    path: cp_library/math/subset_zeta_fn.py
    title: cp_library/math/subset_zeta_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library-checker/set-power-series/subset_convolution.test.py
    title: test/library-checker/set-power-series/subset_convolution.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef subset_conv(A, B, N):\n    Z = 1 << N\n\n    # Prepare arrays for rank (popcount)\
    \ decomposition\n    Arank = [[0]*Z for _ in range(N+1)]\n    Brank = [[0]*Z for\
    \ _ in range(N+1)]\n\n    # Initialize rank arrays\n    for mask in range(Z):\n\
    \        rank = mask.bit_count()\n        Arank[rank][mask] = A[mask]\n      \
    \  Brank[rank][mask] = B[mask]\n\n    # Zeta transform for each rank\n    for\
    \ Ar in Arank: subset_zeta(Ar, N)\n    for Br in Brank: subset_zeta(Br, N)\n\n\
    \    # Convolution\n    Crank = [[0 for _ in range(Z)] for _ in range(N+1)]\n\
    \    for mask in range(Z):\n        for i in range(L := mask.bit_count()+1):\n\
    \            for j in range(min(L, N+1-i)):\n                k = i+j\n       \
    \         Crank[k][mask] = Crank[k][mask] + Arank[i][mask] * Brank[j][mask]\n\n\
    \    # M\xF6bius transform (inverse of Zeta transform)\n    for Cr in Crank: subset_mobius(Cr,\
    \ N)\n        \n    # Combine results\n    C = [0] * Z\n    for mask in range(Z):\n\
    \        rank = mask.bit_count()\n        C[mask] = Crank[rank][mask]\n\n    return\
    \ C\n\n\ndef subset_zeta(A, N, block=5):\n    for i in range(min(block,N)):\n\
    \        for mask in range(bit := 1<<i, 1<<N):\n            if mask & bit:\n \
    \               A[mask] += A[mask ^ bit]\n    for i in range(block,N):\n     \
    \   for base in range(bit := 1<<i, 1<<N, bit << 1):\n            for mask in range(base,\
    \ base+bit):\n                A[mask] += A[mask ^ bit]\n    return A\n\ndef subset_mobius(A,\
    \ N, block=5):\n    for i in range(min(block,N)):\n        for mask in range(bit\
    \ := 1<<i, 1<<N):\n            if mask & bit:\n                A[mask] -= A[mask\
    \ ^ bit]\n    for i in range(block,N):\n        for base in range(bit := 1<<i,\
    \ 1<<N, bit << 1):\n            for mask in range(base, base+bit):\n         \
    \       A[mask] -= A[mask ^ bit]\n    return A\n"
  code: "import cp_library.math.__header__\n\ndef subset_conv(A, B, N):\n    Z = 1\
    \ << N\n\n    # Prepare arrays for rank (popcount) decomposition\n    Arank =\
    \ [[0]*Z for _ in range(N+1)]\n    Brank = [[0]*Z for _ in range(N+1)]\n\n   \
    \ # Initialize rank arrays\n    for mask in range(Z):\n        rank = mask.bit_count()\n\
    \        Arank[rank][mask] = A[mask]\n        Brank[rank][mask] = B[mask]\n\n\
    \    # Zeta transform for each rank\n    for Ar in Arank: subset_zeta(Ar, N)\n\
    \    for Br in Brank: subset_zeta(Br, N)\n\n    # Convolution\n    Crank = [[0\
    \ for _ in range(Z)] for _ in range(N+1)]\n    for mask in range(Z):\n       \
    \ for i in range(L := mask.bit_count()+1):\n            for j in range(min(L,\
    \ N+1-i)):\n                k = i+j\n                Crank[k][mask] = Crank[k][mask]\
    \ + Arank[i][mask] * Brank[j][mask]\n\n    # M\xF6bius transform (inverse of Zeta\
    \ transform)\n    for Cr in Crank: subset_mobius(Cr, N)\n        \n    # Combine\
    \ results\n    C = [0] * Z\n    for mask in range(Z):\n        rank = mask.bit_count()\n\
    \        C[mask] = Crank[rank][mask]\n\n    return C\n\nfrom cp_library.math.subset_zeta_fn\
    \ import subset_zeta\nfrom cp_library.math.subset_mobius_fn import subset_mobius"
  dependsOn:
  - cp_library/math/subset_zeta_fn.py
  - cp_library/math/subset_mobius_fn.py
  isVerificationFile: false
  path: cp_library/math/subset_conv_fn.py
  requiredBy: []
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution.test.py
documentation_of: cp_library/math/subset_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/subset_conv_fn.py
- /library/cp_library/math/subset_conv_fn.py.html
title: cp_library/math/subset_conv_fn.py
---
