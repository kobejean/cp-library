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
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    path: cp_library/math/conv/isubset_conv_ranked_fn.py
    title: cp_library/math/conv/isubset_conv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_conv_fn.py
    title: cp_library/math/conv/subset_conv_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \n\nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
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
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\n\ndef popcnts(N):\n\
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
    \          \n'''\n\n\ndef max2(a, b):\n    return a if a > b else b\n\ndef ior_zeta_pair_ranked(A,\
    \ B, N, M, Z):\n    for i in range(0, Z, M):\n        l, r = i+(1<<(i>>N))-1,\
    \ i+M\n        for j in range(N):\n            m = l|(b := 1<<j)\n           \
    \ while m < r: A[m] += A[m^b]; B[m] += B[m^b]; m = m+1|b\n    return A, B\n\n\
    def ior_mobius_ranked(A: list[int], N: int, M: int, Z: int):\n    for i in range(0,\
    \ Z, M):\n        l, r = i, i+M-(1<<(N-(i>>N)))+1\n        for j in range(N):\n\
    \            m = l|(b := 1<<j)\n            while m < r: A[m] -= A[m^b]; m = m+1|b\n\
    \    return A\n\ndef isubset_conv_ranked(Ar, Br, N, M, Z) -> list[int]:\n    ior_zeta_pair_ranked(Ar,\
    \ Br, N, M, Z)\n    for ij in range(Z-M,-1,-M):\n        for k in range(M): Ar[ij|k]\
    \ *= Br[k]\n        r = M-(1 << (N-(ij>>N)))+1\n        for i in range(0,ij,M):\n\
    \            j = ij-i; l = (1 << (max2(i,j)>>N))-1\n            for k in range(l,r):\
    \ Ar[ij|k] += Ar[i|k] * Br[j|k]\n    return ior_mobius_ranked(Ar, N, M, Z)\n\n\
    def subset_conv(A: list[int], B: list[int], N: int) -> list[int]:\n    Z = (N+1)*(M:=1<<N)\n\
    \    Ar, Br, P = [0]*Z, [0]*Z, popcnts(N)\n    for i, p in enumerate(P): Ar[p<<N|i],\
    \ Br[p<<N|i] = A[i], B[i]\n    isubset_conv_ranked(Ar, Br, N, M, Z)\n    return\
    \ [Ar[p<<N|i] for i, p in enumerate(P)]\n\n\ndef sps_exp(P):\n    N = len(P).bit_length()\
    \ - 1\n    P = view(P); m = 1\n    exp = elist(1 << N); exp.append(1)\n    for\
    \ n in range(N):\n        P.set_range(m, m := m<<1)\n        exp.extend(subset_conv(exp,\
    \ P, n))\n    return exp\n"
  code: "import cp_library.__header__\nfrom cp_library.ds.elist_fn import elist\n\
    from cp_library.ds.view.view_cls import view\nimport cp_library.math.__header__\n\
    from cp_library.math.conv.subset_conv_fn import subset_conv\nimport cp_library.math.sps.__header__\n\
    \ndef sps_exp(P):\n    N = len(P).bit_length() - 1\n    P = view(P); m = 1\n \
    \   exp = elist(1 << N); exp.append(1)\n    for n in range(N):\n        P.set_range(m,\
    \ m := m<<1)\n        exp.extend(subset_conv(exp, P, n))\n    return exp"
  dependsOn:
  - cp_library/ds/elist_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/math/conv/subset_conv_fn.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/isubset_conv_ranked_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  isVerificationFile: false
  path: cp_library/math/sps/sps_exp_fn.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/sps/sps_exp_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/sps_exp_fn.py
- /library/cp_library/math/sps/sps_exp_fn.py.html
title: cp_library/math/sps/sps_exp_fn.py
---
