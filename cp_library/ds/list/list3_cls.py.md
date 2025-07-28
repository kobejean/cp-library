---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit3_cls.py
    title: cp_library/ds/tree/bit/bit3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree3_cls.py
    title: cp_library/ds/tree/seg/segtree3_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/list/list3_cls_test.py
    title: test/unittests/ds/list/list3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit3_cls_test.py
    title: test/unittests/ds/tree/bit/bit3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree3_cls_test.py
    title: test/unittests/ds/tree/seg/segtree3_cls_test.py
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
    \n\n\n\ndef argsort(A: list[int], reverse=False):\n    P = Packer(len(I := list(A))-1);\
    \ P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n    return I\n\n\n\nclass\
    \ Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length();\
    \ P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n\
    \    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def\
    \ enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A\n\
    \    def ienumerate(P, A, reverse=False):\n        if reverse:\n            for\
    \ i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n            for i,a\
    \ in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A));\
    \ return A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\
    \n\ndef isort_parallel(*L: list, reverse=False):\n    inv, order = [0]*len(L[0]),\
    \ argsort(L[0], reverse=reverse)\n    for i, j in enumerate(order): inv[j] = i\n\
    \    for i, j in enumerate(order):\n        for A in L: A[i], A[j] = A[j], A[i]\n\
    \        order[inv[i]], inv[j] = j, inv[i]\n    return L\nfrom typing import Generic\n\
    from typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n\nclass list3(Generic[_T1, _T2,\
    \ _T3]):\n    __slots__ = 'A1', 'A2', 'A3'\n    def __init__(lst, A1: list[_T1],\
    \ A2: list[_T2], A3: list[_T3]):\n        lst.A1, lst.A2, lst.A3 = A1, A2, A3\n\
    \    def __len__(lst): return len(lst.A1)\n    def __getitem__(lst, i: int): return\
    \ lst.A1[i], lst.A2[i], lst.A3[i]\n    def __setitem__(lst, i: int, v: tuple[_T1,\
    \ _T2, _T3]): lst.A1[i], lst.A2[i], lst.A3[i] = v\n    def __contains__(lst, v:\
    \ tuple[_T1, _T2, _T3]): raise NotImplementedError\n    def index(lst, v: tuple[_T1,\
    \ _T2, _T3]): raise NotImplementedError\n    def reverse(lst): lst.A1.reverse();\
    \ lst.A2.reverse(); lst.A3.reverse()\n    def sort(lst, reverse=False): isort_parallel(lst.A1,\
    \ lst.A2, lst.A3, reverse=reverse)\n    def pop(lst): return lst.A1.pop(), lst.A2.pop(),\
    \ lst.A3.pop()\n    def append(lst, v: tuple[_T1, _T2, _T3]):\n        v1, v2,\
    \ v3 = v\n        lst.A1.append(v1); lst.A2.append(v2); lst.A3.append(v3)\n  \
    \  def add(lst, i: int, v: tuple[_T1, _T2, _T3]): lst.A1[i] += v[0]; lst.A2[i]\
    \ += v[1]; lst.A3[i] += v[2]\n"
  code: "from cp_library.alg.iter.sort.isort_parallel_fn import isort_parallel\nimport\
    \ cp_library.__header__\nfrom typing import Generic\nfrom cp_library.misc.typing\
    \ import _T1, _T2, _T3\nimport cp_library.ds.__header__\nimport cp_library.ds.view.__header__\n\
    \nclass list3(Generic[_T1, _T2, _T3]):\n    __slots__ = 'A1', 'A2', 'A3'\n   \
    \ def __init__(lst, A1: list[_T1], A2: list[_T2], A3: list[_T3]):\n        lst.A1,\
    \ lst.A2, lst.A3 = A1, A2, A3\n    def __len__(lst): return len(lst.A1)\n    def\
    \ __getitem__(lst, i: int): return lst.A1[i], lst.A2[i], lst.A3[i]\n    def __setitem__(lst,\
    \ i: int, v: tuple[_T1, _T2, _T3]): lst.A1[i], lst.A2[i], lst.A3[i] = v\n    def\
    \ __contains__(lst, v: tuple[_T1, _T2, _T3]): raise NotImplementedError\n    def\
    \ index(lst, v: tuple[_T1, _T2, _T3]): raise NotImplementedError\n    def reverse(lst):\
    \ lst.A1.reverse(); lst.A2.reverse(); lst.A3.reverse()\n    def sort(lst, reverse=False):\
    \ isort_parallel(lst.A1, lst.A2, lst.A3, reverse=reverse)\n    def pop(lst): return\
    \ lst.A1.pop(), lst.A2.pop(), lst.A3.pop()\n    def append(lst, v: tuple[_T1,\
    \ _T2, _T3]):\n        v1, v2, v3 = v\n        lst.A1.append(v1); lst.A2.append(v2);\
    \ lst.A3.append(v3)\n    def add(lst, i: int, v: tuple[_T1, _T2, _T3]): lst.A1[i]\
    \ += v[0]; lst.A2[i] += v[1]; lst.A3[i] += v[2]"
  dependsOn:
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: cp_library/ds/list/list3_cls.py
  requiredBy:
  - cp_library/ds/tree/seg/segtree3_cls.py
  - cp_library/ds/tree/bit/bit3_cls.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/tree/seg/segtree3_cls_test.py
  - test/unittests/ds/tree/bit/bit3_cls_test.py
  - test/unittests/ds/list/list3_cls_test.py
documentation_of: cp_library/ds/list/list3_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/list/list3_cls.py
- /library/cp_library/ds/list/list3_cls.py.html
title: cp_library/ds/list/list3_cls.py
---
