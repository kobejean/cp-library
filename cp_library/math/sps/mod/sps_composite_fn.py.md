---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
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
    path: cp_library/math/conv/ior_zeta_fn.py
    title: cp_library/math/conv/ior_zeta_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/polynomial_composite_set_power_series.test.py
    title: test/library-checker/set-power-series/polynomial_composite_set_power_series.test.py
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
    \ m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n\n\ndef\
    \ elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \n\nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    import sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
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
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n    x\u2080 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\n       \
    \         \u2573          \u2572 \u2571          \u2572     \u2571          \n\
    \    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2500\
    \u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2081\n                           \u2573 \u2573          \u2572 \u2572 \u2571\
    \ \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25BA X\u2082\n                \u2573          \u2571 \u2572    \
    \      \u2572 \u2573 \u2573 \u2571          \n    x\u2086 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n                         \
    \               \u2573 \u2573 \u2573 \u2573         \n    x\u2081 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2084\n             \
    \   \u2573          \u2572 \u2571          \u2571 \u2573 \u2573 \u2572       \
    \   \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\
    \u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2085\n                           \u2573 \u2573          \u2571 \u2571\
    \ \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2086\n                \u2573          \u2571 \u2572\
    \          \u2571     \u2572          \n    x\u2087 \u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n                      Math - Convolution\
    \                     \n'''\n\ndef ior_zeta(A: list[int], N: int, Z: int = None):\n\
    \    Z = Z if Z else len(A)\n    for i in range(N):\n        m = b = 1<<i\n  \
    \      while m < Z: A[m] += A[m^b]; m = m+1|b\n    return A\n\ndef ior_mobius_ranked(A:\
    \ list[int], N: int, M: int, Z: int):\n    for i in range(0, Z, M):\n        l,\
    \ r = i, i+M-(1<<(N-(i>>N)))+1\n        for j in range(N):\n            m = l|(b\
    \ := 1<<j)\n            while m < r: A[m] -= A[m^b]; m = m+1|b\n    return A\n\
    \n\n\ndef isubset_conv_zeta_ranked(Ar: list[int], Br: list[int], n: int, N: int,\
    \ mod: int) -> list[int]:\n    m = 1<<n\n    for ij in range(n,-1,-1):\n     \
    \   ij_, i_ = (ij+1)<<N|m, ij<<n\n        for k in range(m): Ar[ij_|k] = Br[i_|k]\
    \ * Ar[k] % mod\n        for i in range(ij):\n            j = ij-i; i_, j_ = i<<n,\
    \ j<<N\n            for k in range(m): Ar[ij_|k] = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k])\
    \ % mod\n\ndef sps_composite(A: list[int], B: list[int], mod: int) -> list[int]:\n\
    \    C = [0]*(M := 1 << (N := len(B).bit_length() - 1))\n    if not A: return\
    \ C\n    dA, B0, B1, Br, Cr, pcnt = A[:], elist(N+1), view(B), elist(N), [0]*(Z\
    \ := (N+1)*M), popcnts(N)\n    for n in range(N+1):\n        if n < N:\n     \
    \       # zeta transform of ranked \n            B1.set_range(1<<n, 2<<n)\n  \
    \          br = [0]*(z := (n+1)*(m := 1<<n))\n            for i in range(m): br[pcnt[i]<<n|i]\
    \ = B1[i]\n            ior_zeta(br, n)\n            for i in range(z): br[i] %=\
    \ mod\n            Br.append(br)\n        # evaluate current polynomial at B[0]\
    \ using Horner's method\n        t = 0\n        for j in range(len(dA)-1, -1,\
    \ -1): t = (t * B[0] + dA[j]) % mod\n        B0.append(t)\n        # update dA\
    \ to be the derivative\n        for j in range(1, len(dA)): dA[j-1] = (j * dA[j])\
    \ % mod\n        if dA: dA[-1] = 0\n    for n in range(N+1):\n        for m in\
    \ range(n-1, -1, -1):\n            # effectively computes `C[1<<m:2<<m] = subset_conv(C[:1<<m],\
    \ B[1<<m:2<<m])`\n            # but basically maintains `Cr`, the ranked zeta\
    \ transformed `C`\n            # partial zeta updates need to be made after loop\
    \ ends to propagate contributions\n            isubset_conv_zeta_ranked(Cr, Br[m],\
    \ m, N, mod)\n        # partial zeta updates\n        for m in range(n):\n   \
    \         b = 1 << m\n            for j in range(m+1):\n                j <<=\
    \ N\n                for k in range(j, j|b): Cr[k|b] += Cr[k]\n        for k in\
    \ range(1<<n): Cr[k] = B0[~n]\n    ior_mobius_ranked(Cr, N, M, Z)\n    for i,\
    \ p in enumerate(pcnt): C[i] = Cr[p<<N|i] % mod\n    return C\n"
  code: "import cp_library.__header__\nfrom cp_library.bit.popcnts_fn import popcnts\n\
    from cp_library.ds.list.elist_fn import elist\nfrom cp_library.ds.view.view_cls\
    \ import view\nimport cp_library.math.__header__\nfrom cp_library.math.conv.ior_zeta_fn\
    \ import ior_zeta\nfrom cp_library.math.conv.ior_mobius_ranked_fn import ior_mobius_ranked\n\
    import cp_library.math.sps.__header__\nimport cp_library.math.sps.mod.__header__\n\
    \ndef isubset_conv_zeta_ranked(Ar: list[int], Br: list[int], n: int, N: int, mod:\
    \ int) -> list[int]:\n    m = 1<<n\n    for ij in range(n,-1,-1):\n        ij_,\
    \ i_ = (ij+1)<<N|m, ij<<n\n        for k in range(m): Ar[ij_|k] = Br[i_|k] * Ar[k]\
    \ % mod\n        for i in range(ij):\n            j = ij-i; i_, j_ = i<<n, j<<N\n\
    \            for k in range(m): Ar[ij_|k] = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k])\
    \ % mod\n\ndef sps_composite(A: list[int], B: list[int], mod: int) -> list[int]:\n\
    \    C = [0]*(M := 1 << (N := len(B).bit_length() - 1))\n    if not A: return\
    \ C\n    dA, B0, B1, Br, Cr, pcnt = A[:], elist(N+1), view(B), elist(N), [0]*(Z\
    \ := (N+1)*M), popcnts(N)\n    for n in range(N+1):\n        if n < N:\n     \
    \       # zeta transform of ranked \n            B1.set_range(1<<n, 2<<n)\n  \
    \          br = [0]*(z := (n+1)*(m := 1<<n))\n            for i in range(m): br[pcnt[i]<<n|i]\
    \ = B1[i]\n            ior_zeta(br, n)\n            for i in range(z): br[i] %=\
    \ mod\n            Br.append(br)\n        # evaluate current polynomial at B[0]\
    \ using Horner's method\n        t = 0\n        for j in range(len(dA)-1, -1,\
    \ -1): t = (t * B[0] + dA[j]) % mod\n        B0.append(t)\n        # update dA\
    \ to be the derivative\n        for j in range(1, len(dA)): dA[j-1] = (j * dA[j])\
    \ % mod\n        if dA: dA[-1] = 0\n    for n in range(N+1):\n        for m in\
    \ range(n-1, -1, -1):\n            # effectively computes `C[1<<m:2<<m] = subset_conv(C[:1<<m],\
    \ B[1<<m:2<<m])`\n            # but basically maintains `Cr`, the ranked zeta\
    \ transformed `C`\n            # partial zeta updates need to be made after loop\
    \ ends to propagate contributions\n            isubset_conv_zeta_ranked(Cr, Br[m],\
    \ m, N, mod)\n        # partial zeta updates\n        for m in range(n):\n   \
    \         b = 1 << m\n            for j in range(m+1):\n                j <<=\
    \ N\n                for k in range(j, j|b): Cr[k|b] += Cr[k]\n        for k in\
    \ range(1<<n): Cr[k] = B0[~n]\n    ior_mobius_ranked(Cr, N, M, Z)\n    for i,\
    \ p in enumerate(pcnt): C[i] = Cr[p<<N|i] % mod\n    return C"
  dependsOn:
  - cp_library/bit/popcnts_fn.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/math/conv/ior_zeta_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/math/sps/mod/sps_composite_fn.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/polynomial_composite_set_power_series.test.py
documentation_of: cp_library/math/sps/mod/sps_composite_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/mod/sps_composite_fn.py
- /library/cp_library/math/sps/mod/sps_composite_fn.py.html
title: cp_library/math/sps/mod/sps_composite_fn.py
---
