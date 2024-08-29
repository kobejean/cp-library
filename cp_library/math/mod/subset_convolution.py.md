---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/fzt.py
    title: cp_library/math/mod/fzt.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/ifzt.py
    title: cp_library/math/mod/ifzt.py
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
  bundledCode: "\ndef fzt(A, mod):\n    N = len(A).bit_length()-1\n\n    for i in\
    \ range(N):\n        bit = 1 << i\n        for mask in range(1 << N):\n      \
    \      if mask & bit:\n                A[mask] = (A[mask] + A[mask ^ bit]) % mod\n\
    \n    return A\n\ndef ifzt(A, mod):\n    N = len(A).bit_length()-1\n\n    for\
    \ i in range(N):\n        bit = 1 << i\n        for mask in range(1 << N):\n \
    \           if mask & bit:\n                A[mask] = (A[mask] - A[mask ^ bit])\
    \ % mod\n\n    return A\n\ndef subset_convolution(A, B, mod):\n    N = max(len(A),\
    \ len(B)).bit_length()\n    Z = 1 << (N-1)\n\n    # Prepare arrays for rank (popcount)\
    \ decomposition\n    Arank = [[0]*Z for _ in range(N)]\n    Brank = [[0]*Z for\
    \ _ in range(N)]\n\n    # Initialize rank arrays\n    for mask in range(Z):\n\
    \        rank = mask.bit_count()\n        Arank[rank][mask] = A[mask]\n      \
    \  Brank[rank][mask] = B[mask]\n\n    # Zeta transform for each rank\n    for\
    \ Ar in Arank: fzt(Ar, mod)\n    for Br in Brank: fzt(Br, mod)\n\n    # Convolution\n\
    \    Crank = [[0 for _ in range(Z)] for _ in range(N)]\n    for mask in range(Z):\n\
    \        L = mask.bit_count()+1\n        for i in range(L):\n            for j\
    \ in range(min(L, N-i)):\n                k = i+j\n                Crank[k][mask]\
    \ = (Crank[k][mask] + Arank[i][mask] * Brank[j][mask]) % mod\n\n    # M\xF6bius\
    \ transform (inverse of Zeta transform)\n    for Cr in Crank: ifzt(Cr, mod)\n\
    \        \n    # Combine results\n    C = [0] * Z\n    for mask in range(Z):\n\
    \        rank = mask.bit_count()\n        C[mask] = Crank[rank][mask]\n\n    return\
    \ C\n"
  code: "from cp_library.math.mod.fzt import fzt\nfrom cp_library.math.mod.ifzt import\
    \ ifzt\n\ndef subset_convolution(A, B, mod):\n    N = max(len(A), len(B)).bit_length()\n\
    \    Z = 1 << (N-1)\n\n    # Prepare arrays for rank (popcount) decomposition\n\
    \    Arank = [[0]*Z for _ in range(N)]\n    Brank = [[0]*Z for _ in range(N)]\n\
    \n    # Initialize rank arrays\n    for mask in range(Z):\n        rank = mask.bit_count()\n\
    \        Arank[rank][mask] = A[mask]\n        Brank[rank][mask] = B[mask]\n\n\
    \    # Zeta transform for each rank\n    for Ar in Arank: fzt(Ar, mod)\n    for\
    \ Br in Brank: fzt(Br, mod)\n\n    # Convolution\n    Crank = [[0 for _ in range(Z)]\
    \ for _ in range(N)]\n    for mask in range(Z):\n        L = mask.bit_count()+1\n\
    \        for i in range(L):\n            for j in range(min(L, N-i)):\n      \
    \          k = i+j\n                Crank[k][mask] = (Crank[k][mask] + Arank[i][mask]\
    \ * Brank[j][mask]) % mod\n\n    # M\xF6bius transform (inverse of Zeta transform)\n\
    \    for Cr in Crank: ifzt(Cr, mod)\n        \n    # Combine results\n    C =\
    \ [0] * Z\n    for mask in range(Z):\n        rank = mask.bit_count()\n      \
    \  C[mask] = Crank[rank][mask]\n\n    return C"
  dependsOn:
  - cp_library/math/mod/fzt.py
  - cp_library/math/mod/ifzt.py
  isVerificationFile: false
  path: cp_library/math/mod/subset_convolution.py
  requiredBy: []
  timestamp: '2024-08-29 17:40:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
documentation_of: cp_library/math/mod/subset_convolution.py
layout: document
redirect_from:
- /library/cp_library/math/mod/subset_convolution.py
- /library/cp_library/math/mod/subset_convolution.py.html
title: cp_library/math/mod/subset_convolution.py
---
