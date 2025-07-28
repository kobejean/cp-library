---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_ranked_fn.py
    title: cp_library/math/conv/ior_mobius_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
    title: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_deconv_fn.py
    title: cp_library/math/conv/subset_deconv_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_div_fn.py
    title: cp_library/math/sps/sps_div_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_ln_fn.py
    title: cp_library/math/sps/sps_ln_fn.py
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
    \                     \n'''\n\ndef ior_zeta_pair_ranked(A, B, N, M, Z):\n    for\
    \ i in range(0, Z, M):\n        l, r = i+(1<<(i>>N))-1, i+M\n        for j in\
    \ range(N):\n            m = l|(b := 1<<j)\n            while m < r: A[m] += A[m^b];\
    \ B[m] += B[m^b]; m = m+1|b\n    return A, B\n\ndef ior_mobius_ranked(A: list[int],\
    \ N: int, M: int, Z: int):\n    for i in range(0, Z, M):\n        l, r = i, i+M-(1<<(N-(i>>N)))+1\n\
    \        for j in range(N):\n            m = l|(b := 1<<j)\n            while\
    \ m < r: A[m] -= A[m^b]; m = m+1|b\n    return A\n\ndef isubset_deconv_ranked(Ar,\
    \ Br, N, Z, M):\n    inv = 1 // Br[0]; ior_zeta_pair_ranked(Ar, Br, N, M, Z)\n\
    \    for i in range(0, Z, M):\n        for k in range(M): Ar[i|k] *= inv\n   \
    \     for j in range(M, Z-i, M):\n            ij = i + j; l = (1 << (j>>N))-1\n\
    \            for k in range(l, M): Ar[ij|k] -= Ar[i|k] * Br[j|k]\n    return ior_mobius_ranked(Ar,\
    \ N, M, Z)\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.conv.__header__\n\
    from cp_library.math.conv.ior_zeta_pair_ranked_fn import ior_zeta_pair_ranked\n\
    from cp_library.math.conv.ior_mobius_ranked_fn import ior_mobius_ranked\n\ndef\
    \ isubset_deconv_ranked(Ar, Br, N, Z, M):\n    inv = 1 // Br[0]; ior_zeta_pair_ranked(Ar,\
    \ Br, N, M, Z)\n    for i in range(0, Z, M):\n        for k in range(M): Ar[i|k]\
    \ *= inv\n        for j in range(M, Z-i, M):\n            ij = i + j; l = (1 <<\
    \ (j>>N))-1\n            for k in range(l, M): Ar[ij|k] -= Ar[i|k] * Br[j|k]\n\
    \    return ior_mobius_ranked(Ar, N, M, Z)"
  dependsOn:
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/isubset_deconv_ranked_fn.py
  requiredBy:
  - cp_library/math/sps/sps_ln_fn.py
  - cp_library/math/sps/sps_div_fn.py
  - cp_library/math/conv/subset_deconv_fn.py
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/subset_convolution_all.test.py
documentation_of: cp_library/math/conv/isubset_deconv_ranked_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/isubset_deconv_ranked_fn.py
- /library/cp_library/math/conv/isubset_deconv_ranked_fn.py.html
title: cp_library/math/conv/isubset_deconv_ranked_fn.py
---
