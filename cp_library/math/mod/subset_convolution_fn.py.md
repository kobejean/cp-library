---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mobius_transform_fn.py
    title: cp_library/math/mod/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/zeta_transform_fn.py
    title: cp_library/math/mod/zeta_transform_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef zeta_transform(A, mod):\n    N = len(A).bit_length()-1\n\n \
    \   for i in range(N):\n        bit = 1 << i\n        for mask in range(1 << N):\n\
    \            if mask & bit:\n                A[mask] = (A[mask] + A[mask ^ bit])\
    \ % mod\n\n    return A\n\ndef mobius_transform(A, mod):\n    N = len(A).bit_length()-1\n\
    \n    for i in range(N):\n        bit = 1 << i\n        for mask in range(1 <<\
    \ N):\n            if mask & bit:\n                A[mask] = (A[mask] - A[mask\
    \ ^ bit]) % mod\n\n    return A\n\ndef subset_convolution(A, B, mod):\n    N =\
    \ max(len(A), len(B)).bit_length()\n    Z = 1 << (N-1)\n\n    # Prepare arrays\
    \ for rank (popcount) decomposition\n    Arank = [[0]*Z for _ in range(N)]\n \
    \   Brank = [[0]*Z for _ in range(N)]\n\n    # Initialize rank arrays\n    for\
    \ mask in range(Z):\n        rank = mask.bit_count()\n        Arank[rank][mask]\
    \ = A[mask]\n        Brank[rank][mask] = B[mask]\n\n    # Zeta transform for each\
    \ rank\n    for Ar in Arank: zeta_transform(Ar, mod)\n    for Br in Brank: zeta_transform(Br,\
    \ mod)\n\n    # Convolution\n    Crank = [[0 for _ in range(Z)] for _ in range(N)]\n\
    \    for mask in range(Z):\n        L = mask.bit_count()+1\n        for i in range(L):\n\
    \            for j in range(min(L, N-i)):\n                k = i+j\n         \
    \       Crank[k][mask] = (Crank[k][mask] + Arank[i][mask] * Brank[j][mask]) %\
    \ mod\n\n    # M\xF6bius transform (inverse of Zeta transform)\n    for Cr in\
    \ Crank: mobius_transform(Cr, mod)\n        \n    # Combine results\n    C = [0]\
    \ * Z\n    for mask in range(Z):\n        rank = mask.bit_count()\n        C[mask]\
    \ = Crank[rank][mask]\n\n    return C\n"
  code: "from cp_library.math.mod.zeta_transform_fn import zeta_transform\nfrom cp_library.math.mod.mobius_transform_fn\
    \ import mobius_transform\n\ndef subset_convolution(A, B, mod):\n    N = max(len(A),\
    \ len(B)).bit_length()\n    Z = 1 << (N-1)\n\n    # Prepare arrays for rank (popcount)\
    \ decomposition\n    Arank = [[0]*Z for _ in range(N)]\n    Brank = [[0]*Z for\
    \ _ in range(N)]\n\n    # Initialize rank arrays\n    for mask in range(Z):\n\
    \        rank = mask.bit_count()\n        Arank[rank][mask] = A[mask]\n      \
    \  Brank[rank][mask] = B[mask]\n\n    # Zeta transform for each rank\n    for\
    \ Ar in Arank: zeta_transform(Ar, mod)\n    for Br in Brank: zeta_transform(Br,\
    \ mod)\n\n    # Convolution\n    Crank = [[0 for _ in range(Z)] for _ in range(N)]\n\
    \    for mask in range(Z):\n        L = mask.bit_count()+1\n        for i in range(L):\n\
    \            for j in range(min(L, N-i)):\n                k = i+j\n         \
    \       Crank[k][mask] = (Crank[k][mask] + Arank[i][mask] * Brank[j][mask]) %\
    \ mod\n\n    # M\xF6bius transform (inverse of Zeta transform)\n    for Cr in\
    \ Crank: mobius_transform(Cr, mod)\n        \n    # Combine results\n    C = [0]\
    \ * Z\n    for mask in range(Z):\n        rank = mask.bit_count()\n        C[mask]\
    \ = Crank[rank][mask]\n\n    return C"
  dependsOn:
  - cp_library/math/mod/zeta_transform_fn.py
  - cp_library/math/mod/mobius_transform_fn.py
  isVerificationFile: false
  path: cp_library/math/mod/subset_convolution_fn.py
  requiredBy: []
  timestamp: '2024-09-02 01:58:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
documentation_of: cp_library/math/mod/subset_convolution_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mod/subset_convolution_fn.py
- /library/cp_library/math/mod/subset_convolution_fn.py.html
title: cp_library/math/mod/subset_convolution_fn.py
---
