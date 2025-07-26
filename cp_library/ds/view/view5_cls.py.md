---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_ranged_fn.py
    title: cp_library/alg/iter/arg/argsort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_ranged_fn.py
    title: cp_library/alg/iter/sort/isort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/csr5_cls.py
    title: cp_library/ds/view/csr5_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr5_cls_test.py
    title: test/unittests/ds/view/csr5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view5_cls_test.py
    title: test/unittests/ds/view/view5_cls_test.py
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
    from typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T\
    \ = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n\n\ndef argsort_ranged(A: list[int], l: int, r: int, reverse=False):\n   \
    \ P = Packer(r-l-1); I = [A[l+i] for i in range(r-l)]; P.ienumerate(I, reverse);\
    \ I.sort()\n    for i in range(r-l): I[i] = (I[i] & P.m) + l\n    return I\n\n\
    \n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s\
    \ = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return\
    \ a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x\
    \ & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse);\
    \ return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n  \
    \          for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n     \
    \       for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_ranged(*L: list, l: int, r: int, reverse=False):\n\
    \    n = r - l\n    order = argsort_ranged(L[0], l, r, reverse=reverse)\n    inv\
    \ = [0] * n\n    # order contains indices in range [l, r), need to map to [0,\
    \ n)\n    for i in range(n): inv[order[i]-l] = i\n    for i in range(n):\n   \
    \     j = order[i] - l  # j is in range [0, n)\n        for A in L: A[l+i], A[l+j]\
    \ = A[l+j], A[l+i]\n        order[inv[i]], order[inv[j]] = order[inv[j]], order[inv[i]]\n\
    \        inv[i], inv[j] = inv[j], inv[i]\n    return L\n\n\n\nclass view5(Generic[_T1,\
    \ _T2, _T3, _T4, _T5]):\n    __slots__ = 'A1', 'A2', 'A3', 'A4', 'A5', 'l', 'r'\n\
    \    def __init__(V, A1: list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4],\
    \ A5: list[_T5], l: int = 0, r: int = 0): \n        V.A1, V.A2, V.A3, V.A4, V.A5,\
    \ V.l, V.r = A1, A2, A3, A4, A5, l, r\n    def __len__(V): return V.r - V.l\n\
    \    def __getitem__(V, i: int): \n        if 0 <= i < V.r - V.l: return V.A1[V.l+i],\
    \ V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i], V.A5[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.A1[V.l+i],\
    \ V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i], V.A5[V.l+i] = v\n    def __contains__(V,\
    \ v: tuple[_T1, _T2, _T3, _T4, _T5]): raise NotImplemented\n    def set_range(V,\
    \ l: int, r: int): V.l, V.r = l, r\n    def index(V, v: tuple[_T1, _T2, _T3, _T4,\
    \ _T5]): raise NotImplemented\n    def reverse(V):\n        l, r = V.l, V.r-1\n\
    \        while l < r: \n            V.A1[l], V.A1[r] = V.A1[r], V.A1[l]\n    \
    \        V.A2[l], V.A2[r] = V.A2[r], V.A2[l]\n            V.A3[l], V.A3[r] = V.A3[r],\
    \ V.A3[l]\n            V.A4[l], V.A4[r] = V.A4[r], V.A4[l]\n            V.A5[l],\
    \ V.A5[r] = V.A5[r], V.A5[l]\n            l += 1; r -= 1\n    def sort(V, reverse=False):\
    \ isort_ranged(V.A1, V.A2, V.A3, V.A4, V.A5, l=V.l, r=V.r, reverse=reverse)\n\
    \    def pop(V): V.r -= 1; return V.A1[V.r], V.A2[V.r], V.A3[V.r], V.A4[V.r],\
    \ V.A5[V.r]\n    def append(V, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.A1[V.r],\
    \ V.A2[V.r], V.A3[V.r], V.A4[V.r], V.A5[V.r] = v; V.r += 1\n    def popleft(V):\
    \ V.l += 1; return V.A1[V.l-1], V.A2[V.l-1], V.A3[V.l-1], V.A4[V.l-1], V.A5[V.l-1]\n\
    \    def appendleft(V, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.l -= 1; V.A1[V.l],\
    \ V.A2[V.l], V.A3[V.l], V.A4[V.l], V.A5[V.l] = v\n    def validate(V): return\
    \ 0 <= V.l <= V.r <= len(V.A1)\n"
  code: "import cp_library.__header__\nfrom typing import Generic\nfrom cp_library.misc.typing\
    \ import _T1, _T2, _T3, _T4, _T5\nfrom cp_library.alg.iter.sort.isort_ranged_fn\
    \ import isort_ranged\nimport cp_library.ds.__header__\nimport cp_library.ds.view.__header__\n\
    \nclass view5(Generic[_T1, _T2, _T3, _T4, _T5]):\n    __slots__ = 'A1', 'A2',\
    \ 'A3', 'A4', 'A5', 'l', 'r'\n    def __init__(V, A1: list[_T1], A2: list[_T2],\
    \ A3: list[_T3], A4: list[_T4], A5: list[_T5], l: int = 0, r: int = 0): \n   \
    \     V.A1, V.A2, V.A3, V.A4, V.A5, V.l, V.r = A1, A2, A3, A4, A5, l, r\n    def\
    \ __len__(V): return V.r - V.l\n    def __getitem__(V, i: int): \n        if 0\
    \ <= i < V.r - V.l: return V.A1[V.l+i], V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i],\
    \ V.A5[V.l+i]\n        else: raise IndexError\n    def __setitem__(V, i: int,\
    \ v: tuple[_T1, _T2, _T3, _T4, _T5]): V.A1[V.l+i], V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i],\
    \ V.A5[V.l+i] = v\n    def __contains__(V, v: tuple[_T1, _T2, _T3, _T4, _T5]):\
    \ raise NotImplemented\n    def set_range(V, l: int, r: int): V.l, V.r = l, r\n\
    \    def index(V, v: tuple[_T1, _T2, _T3, _T4, _T5]): raise NotImplemented\n \
    \   def reverse(V):\n        l, r = V.l, V.r-1\n        while l < r: \n      \
    \      V.A1[l], V.A1[r] = V.A1[r], V.A1[l]\n            V.A2[l], V.A2[r] = V.A2[r],\
    \ V.A2[l]\n            V.A3[l], V.A3[r] = V.A3[r], V.A3[l]\n            V.A4[l],\
    \ V.A4[r] = V.A4[r], V.A4[l]\n            V.A5[l], V.A5[r] = V.A5[r], V.A5[l]\n\
    \            l += 1; r -= 1\n    def sort(V, reverse=False): isort_ranged(V.A1,\
    \ V.A2, V.A3, V.A4, V.A5, l=V.l, r=V.r, reverse=reverse)\n    def pop(V): V.r\
    \ -= 1; return V.A1[V.r], V.A2[V.r], V.A3[V.r], V.A4[V.r], V.A5[V.r]\n    def\
    \ append(V, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.A1[V.r], V.A2[V.r], V.A3[V.r],\
    \ V.A4[V.r], V.A5[V.r] = v; V.r += 1\n    def popleft(V): V.l += 1; return V.A1[V.l-1],\
    \ V.A2[V.l-1], V.A3[V.l-1], V.A4[V.l-1], V.A5[V.l-1]\n    def appendleft(V, v:\
    \ tuple[_T1, _T2, _T3, _T4, _T5]): V.l -= 1; V.A1[V.l], V.A2[V.l], V.A3[V.l],\
    \ V.A4[V.l], V.A5[V.l] = v\n    def validate(V): return 0 <= V.l <= V.r <= len(V.A1)"
  dependsOn:
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: cp_library/ds/view/view5_cls.py
  requiredBy:
  - cp_library/ds/view/csr5_cls.py
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/view/csr5_cls_test.py
  - test/unittests/ds/view/view5_cls_test.py
documentation_of: cp_library/ds/view/view5_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/view/view5_cls.py
- /library/cp_library/ds/view/view5_cls.py.html
title: cp_library/ds/view/view5_cls.py
---
