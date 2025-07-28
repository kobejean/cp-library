---
data:
  _extendedDependsOn:
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
    path: cp_library/math/conv/ior_mobius_fn.py
    title: cp_library/math/conv/ior_mobius_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_fn.py
    title: cp_library/math/conv/ior_zeta_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_conv_half_fn.py
    title: cp_library/math/conv/mod/isubset_conv_half_fn.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
    title: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
    title: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
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
    \ m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n\nfrom\
    \ typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\nimport sys\n\
    \ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n    try:\n\
    \        return lst.index(value, start, stop)\n    except:\n        return -1\n\
    \n\nclass view(Generic[_T]):\n    __slots__ = 'A', 'l', 'r'\n    def __init__(V,\
    \ A: list[_T], l: int = 0, r: int = 0): V.A, V.l, V.r = A, l, r\n    def __len__(V):\
    \ return V.r - V.l\n    def __getitem__(V, i: int): \n        if 0 <= i < V.r\
    \ - V.l: return V.A[V.l+i]\n        else: raise IndexError\n    def __setitem__(V,\
    \ i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V, v: _T): return list_find(V.A,\
    \ v, V.l, V.r) != -1\n    def set_range(V, l: int, r: int): V.l, V.r = l, r\n\
    \    def index(V, v: _T): return V.A.index(v, V.l, V.r) - V.l\n    def reverse(V):\n\
    \        l, r = V.l, V.r-1\n        while l < r: V.A[l], V.A[r] = V.A[r], V.A[l];\
    \ l += 1; r -= 1\n    def sort(V, /, *args, **kwargs):\n        A = V.A[V.l:V.r];\
    \ A.sort(*args, **kwargs)\n        for i,a in enumerate(A,V.l): V.A[i] = a\n \
    \   def pop(V): V.r -= 1; return V.A[V.r]\n    def append(V, v: _T): V.A[V.r]\
    \ = v; V.r += 1\n    def popleft(V): V.l += 1; return V.A[V.l-1]\n    def appendleft(V,\
    \ v: _T): V.l -= 1; V.A[V.l] = v; \n    def validate(V): return 0 <= V.l <= V.r\
    \ <= len(V.A)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2080\n                \u2573          \u2572 \u2571          \u2572\
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
    \       Math - Convolution                     \n'''\n\ndef ior_zeta(A: list[int],\
    \ N: int, Z: int = None):\n    Z = Z if Z else len(A)\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z: A[m] += A[m^b]; m = m+1|b\n    return\
    \ A\n\ndef isubset_conv_half(Ar: list[int], B: list[int], n: int, N: int, mod:\
    \ int, pcnt) -> list[int]:\n    Br = [0]*(z := (n+1)*(m := 1<<n))\n    for i in\
    \ range(m): Br[pcnt[i]<<n|i] = B[i]\n    ior_zeta(Br, n)\n    for i in range(z):\
    \ Br[i] = Br[i]%mod\n    for ij in range(n,-1,-1):\n        ij_, i_ = (ij+1)<<N|m,\
    \ ij<<n\n        for k in range(m): Ar[ij_|k] = (Br[i_|k] * Ar[k]) % mod\n   \
    \     for i in range(ij):\n            j = ij-i; i_, j_ = i<<n, j<<N\n       \
    \     for k in range(m): Ar[ij_|k] = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k]) % mod\n\
    \    for i in range(n+1):\n        i = i << N\n        for k in range(m): Ar[i|k|m]\
    \ += Ar[i|k]\n\ndef ior_mobius(A: list[int], N: int, Z: int = None):\n    Z =\
    \ Z if Z else len(A)\n    for i in range(N):\n        m = b = 1<<i\n        while\
    \ m < Z: A[m] -= A[m^b]; m = m+1|b\n    return A\n\n\ndef sps_exp_half(P, mod):\n\
    \    assert P[0] == 0\n    N = len(P).bit_length() - 1\n    Z = (N+1)*(M := 1<<N)\n\
    \    exp = [0]*Z; exp[0] = 1\n    pcnt = popcnts(N)\n    P = view(P); m = 1\n\
    \    for n in range(N):\n        P.set_range(m, m := m<<1)\n        isubset_conv_half(exp,\
    \ P, n, N, mod, pcnt)\n    ior_mobius(exp, N)\n    return [exp[p<<N|i] % mod for\
    \ i,p in enumerate(pcnt)]\n"
  code: "import cp_library.__header__\nfrom cp_library.bit.popcnts_fn import popcnts\n\
    from cp_library.ds.view.view_cls import view\nimport cp_library.math.__header__\n\
    from cp_library.math.conv.mod.isubset_conv_half_fn import isubset_conv_half\n\
    from cp_library.math.conv.ior_mobius_fn import ior_mobius\nimport cp_library.math.sps.__header__\n\
    \ndef sps_exp_half(P, mod):\n    assert P[0] == 0\n    N = len(P).bit_length()\
    \ - 1\n    Z = (N+1)*(M := 1<<N)\n    exp = [0]*Z; exp[0] = 1\n    pcnt = popcnts(N)\n\
    \    P = view(P); m = 1\n    for n in range(N):\n        P.set_range(m, m := m<<1)\n\
    \        isubset_conv_half(exp, P, n, N, mod, pcnt)\n    ior_mobius(exp, N)\n\
    \    return [exp[p<<N|i] % mod for i,p in enumerate(pcnt)]"
  dependsOn:
  - cp_library/bit/popcnts_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/math/conv/mod/isubset_conv_half_fn.py
  - cp_library/math/conv/ior_mobius_fn.py
  - cp_library/math/conv/ior_zeta_fn.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/math/sps/mod/sps_exp_half_fn.py
  requiredBy:
  - cp_library/math/sps/mod/sps_exp_adaptive_fn.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
documentation_of: cp_library/math/sps/mod/sps_exp_half_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/mod/sps_exp_half_fn.py
- /library/cp_library/math/sps/mod/sps_exp_half_fn.py.html
title: cp_library/math/sps/mod/sps_exp_half_fn.py
---
