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
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_ranked_fn.py
    title: cp_library/math/conv/ior_mobius_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
    title: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_conv_ranked_fn.py
    title: cp_library/math/conv/mod/isubset_conv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_conv_fn.py
    title: cp_library/math/conv/mod/subset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_pow_proj_fn.py
    title: cp_library/math/sps/mod/sps_pow_proj_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/power_projection_of_set_power_series.test.py
    title: test/library-checker/set-power-series/power_projection_of_set_power_series.test.py
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
    \n\n\n\nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\n\n\nclass view(Generic[_T]):\n    __slots__ = 'A', 'l', 'r'\n   \
    \ def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A, V.l, V.r = A, l,\
    \ r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int): \n\
    \        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\ndef popcnts(N):\n\
    \    P = [0]*(1 << N)\n    for i in range(N):\n        for m in range(b := 1<<i):\n\
    \            P[m^b] = P[m] + 1\n    return P\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\n                \u2573   \
    \       \u2572 \u2571          \u2572     \u2571          \n    x\u2084 \u2500\
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
    \          \n'''\n\n\ndef max2(a, b): return a if a > b else b\n\n\ndef ior_zeta_pair_ranked(A,\
    \ B, N, M, Z):\n    for i in range(0, Z, M):\n        l, r = i+(1<<(i>>N))-1,\
    \ i+M\n        for j in range(N):\n            m = l|(b := 1<<j)\n           \
    \ while m < r: A[m] += A[m^b]; B[m] += B[m^b]; m = m+1|b\n    return A, B\n\n\
    def ior_mobius_ranked(A: list[int], N: int, M: int, Z: int):\n    for i in range(0,\
    \ Z, M):\n        l, r = i, i+M-(1<<(N-(i>>N)))+1\n        for j in range(N):\n\
    \            m = l|(b := 1<<j)\n            while m < r: A[m] -= A[m^b]; m = m+1|b\n\
    \    return A\n\ndef isubset_conv_ranked(Ar, Br, N, M, Z, mod) -> list[int]:\n\
    \    ior_zeta_pair_ranked(Ar, Br, N, M, Z)\n    for i in range(Z): Ar[i], Br[i]\
    \ = Ar[i]%mod, Br[i]%mod\n    for ij in range(Z-M,-1,-M):\n        for k in range(M):\
    \ Ar[ij|k] = (Ar[ij|k] * Br[k]) % mod\n        r = M-(1 << (N-(ij>>N)))+1\n  \
    \      for i in range(0,ij,M):\n            j = ij-i; l = (1 << (max2(i,j)>>N))-1\n\
    \            for k in range(l,r): Ar[ij|k] += Ar[i|k] * Br[j|k] % mod\n    return\
    \ ior_mobius_ranked(Ar, N, M, Z)\n\ndef subset_conv(A: list[int], B: list[int],\
    \ N: int, mod: int) -> list[int]:\n    Z = (N+1)*(M:=1<<N)\n    Ar, Br, C, P =\
    \ [0]*Z, [0]*Z, [0]*M, popcnts(N)\n    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i]\
    \ = A[i], B[i]\n    isubset_conv_ranked(Ar, Br, N, M, Z, mod)\n    for i, p in\
    \ enumerate(P): C[i] = Ar[p<<N|i] % mod\n    return C\n\ndef sps_pow_proj(A, B,\
    \ M, mod):\n    N = len(B).bit_length() - 1\n    assert B[0] == 0, \"B[0] must\
    \ be 0 for sps_pow_proj\"\n    Aview, Bview, P = view(A := A[::-1]), view(B),\
    \ []\n    for i in range(N + 1):\n        P.append(A[(1<<N)-1]); A[(1<<N)-1] =\
    \ 0\n        for m in range(N - i):\n            i0 = (1<<N)-(1<<(m+1)); i1 =\
    \ 1 << m; i2 = (1<<N)-(1<<m)\n            Aview.set_range(i0, i0+(1<<m)); Bview.set_range(i1,\
    \ i1+(1<<m))\n            R = subset_conv(Aview, Bview, m, mod)\n            for\
    \ h in range(1 << m): A[i2+h], A[i0+h] = (A[i2+h]+R[h])%mod, 0\n    return P[:M]\n\
    \ndef sps_pow_proj_poly(A, B, M, mod):\n    N = len(B).bit_length()-1; b = B[0];\
    \ B[0] = 0\n    P, F, H = sps_pow_proj(A, B, N + 1, mod), [], [0]*(N+1); H[0]\
    \ = 1\n    for i in range(M):\n        v = 0\n        for j in range(N + 1):\n\
    \            if j < len(P): v = (v+H[j]*P[j])%mod\n        F.append(v)\n     \
    \   for j in range(N-1, -1, -1): H[j+1]=H[j]*(i+1)%mod\n        H[0]=H[0]*b%mod\n\
    \    return F\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.sps.__header__\n\
    import cp_library.math.sps.mod.__header__\nfrom cp_library.math.sps.mod.sps_pow_proj_fn\
    \ import sps_pow_proj\n\ndef sps_pow_proj_poly(A, B, M, mod):\n    N = len(B).bit_length()-1;\
    \ b = B[0]; B[0] = 0\n    P, F, H = sps_pow_proj(A, B, N + 1, mod), [], [0]*(N+1);\
    \ H[0] = 1\n    for i in range(M):\n        v = 0\n        for j in range(N +\
    \ 1):\n            if j < len(P): v = (v+H[j]*P[j])%mod\n        F.append(v)\n\
    \        for j in range(N-1, -1, -1): H[j+1]=H[j]*(i+1)%mod\n        H[0]=H[0]*b%mod\n\
    \    return F"
  dependsOn:
  - cp_library/math/sps/mod/sps_pow_proj_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/math/conv/mod/subset_conv_fn.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/mod/isubset_conv_ranked_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  isVerificationFile: false
  path: cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/power_projection_of_set_power_series.test.py
documentation_of: cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
- /library/cp_library/math/sps/mod/sps_pow_proj_poly_fn.py.html
title: cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
---
