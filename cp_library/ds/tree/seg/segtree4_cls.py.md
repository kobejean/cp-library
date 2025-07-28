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
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list4_cls.py
    title: cp_library/ds/list/list4_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree_cls.py
    title: cp_library/ds/tree/seg/segtree_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree4_cls_test.py
    title: test/unittests/ds/tree/seg/segtree4_cls_test.py
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
    from typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n\n\n\ndef argsort(A: list[int],\
    \ reverse=False):\n    P = Packer(len(I := list(A))-1); P.ienumerate(I, reverse);\
    \ I.sort(); P.iindices(I)\n    return I\n\n\n\nclass Packer:\n    __slots__ =\
    \ 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 << P.s)\
    \ - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P, x:\
    \ int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False):\
    \ P.ienumerate(A:=list(A), reverse); return A\n    def ienumerate(P, A, reverse=False):\n\
    \        if reverse:\n            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n\
    \        else:\n            for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def\
    \ indices(P, A: list[int]): P.iindices(A:=list(A)); return A\n    def iindices(P,\
    \ A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\n\ndef isort_parallel(*L:\
    \ list, reverse=False):\n    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n\
    \    for i, j in enumerate(order): inv[j] = i\n    for i, j in enumerate(order):\n\
    \        for A in L: A[i], A[j] = A[j], A[i]\n        order[inv[i]], inv[j] =\
    \ j, inv[i]\n    return L\nfrom typing import Generic\n\n\nclass list4(Generic[_T1,\
    \ _T2, _T3, _T4]):\n    __slots__ = 'A1', 'A2', 'A3', 'A4'\n    def __init__(lst,\
    \ A1: list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4]):\n        lst.A1,\
    \ lst.A2, lst.A3, lst.A4 = A1, A2, A3, A4\n    def __len__(lst): return len(lst.A1)\n\
    \    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i]\n\
    \    def __setitem__(lst, i: int, v: tuple[_T1, _T2, _T3, _T4]): lst.A1[i], lst.A2[i],\
    \ lst.A3[i], lst.A4[i] = v\n    def __contains__(lst, v: tuple[_T1, _T2, _T3,\
    \ _T4]): raise NotImplementedError\n    def index(lst, v: tuple[_T1, _T2, _T3,\
    \ _T4]): raise NotImplementedError\n    def reverse(lst): lst.A1.reverse(); lst.A2.reverse();\
    \ lst.A3.reverse(); lst.A4.reverse()\n    def sort(lst, reverse=False): isort_parallel(lst.A1,\
    \ lst.A2, lst.A3, lst.A4, reverse=reverse)\n    def pop(lst): return lst.A1.pop(),\
    \ lst.A2.pop(), lst.A3.pop(), lst.A4.pop()\n    def append(lst, v: tuple[_T1,\
    \ _T2, _T3, _T4]):\n        v1, v2, v3, v4 = v\n        lst.A1.append(v1); lst.A2.append(v2);\
    \ lst.A3.append(v3); lst.A4.append(v4)\n    def add(lst, i: int, v: tuple[_T1,\
    \ _T2, _T3, _T4]): lst.A1[i] += v[0]; lst.A2[i] += v[1]; lst.A3[i] += v[2]; lst.A4[i]\
    \ += v[3]\n\n\nfrom typing import Callable, Generic, Union\n\nclass SegTree(Generic[_T]):\n\
    \    _lst = list\n    \n    def __init__(seg, op: Callable[[_T, _T], _T], e: _T,\
    \ v: Union[int, list[_T]]) -> None:\n        if isinstance(v, int): n = v; v =\
    \ None\n        else: n = len(v)\n        seg.op, seg.e, seg.n = op, e, n\n  \
    \      seg.log, seg.sz = (log := (n-1).bit_length()+1), (sz := 1 << log)\n   \
    \     if seg._lst is list: seg.d = [e]*(sz<<1)\n        else: seg.d = seg._lst(*([e_]*(sz<<1)\
    \ for e_ in e))\n        if v: seg._build(v)\n\n    def _build(seg, v):\n    \
    \    for i in range(seg.n): seg.d[seg.sz + i] = v[i]\n        for i in range(seg.sz-1,0,-1):\
    \ seg._merge(i, i<<1, i<<1|1)\n    \n    def _merge(seg, i, j, k): seg.d[i] =\
    \ seg.op(seg.d[j], seg.d[k])\n\n    def set(seg, p: int, x: _T) -> None:\n   \
    \     p += seg.sz\n        seg.d[p] = x\n        for _ in range(seg.log):\n  \
    \          p = p^(p&1)\n            seg._merge(p>>1, p, p|1)\n            p >>=\
    \ 1\n    __setitem__ = set\n\n    def get(seg, p: int) -> _T: return seg.d[p+seg.sz]\n\
    \    __getitem__ = get\n\n    def prod(seg, l: int, r: int) -> _T:\n        sml\
    \ = smr = seg.e\n        l, r = l+seg.sz, r+seg.sz\n        while l < r:\n   \
    \         if l&1: sml, l = seg.op(sml, seg.d[l]), l+1\n            if r&1: smr\
    \ = seg.op(seg.d[r:=r-1], smr)\n            l, r = l >> 1, r >> 1\n        return\
    \ seg.op(sml, smr)\n\n    def all_prod(seg) -> _T: return seg.d[1]\n\n    def\
    \ max_right(seg, l: int, f: Callable[[_T], bool]) -> int:\n        assert 0 <=\
    \ l <= seg.n\n        assert f(seg.e)\n        if l == seg.n: return seg.n\n \
    \       l, op, d, sm = l+(sz := seg.sz), seg.op, seg.d, seg.e\n        while True:\n\
    \            while l&1 == 0: l >>= 1\n            if not f(op(sm, d[l])):\n  \
    \              while l < sz:\n                    if f(op(sm, d[l:=l<<1])): sm,\
    \ l = op(sm, d[l]), l+1\n                return l - sz\n            sm, l = op(sm,\
    \ d[l]), l+1\n            if l&-l == l: return seg.n\n\n    def min_left(seg,\
    \ r: int, f: Callable[[_T], bool]) -> int:\n        assert 0 <= r <= seg.n\n \
    \       assert f(seg.e)\n        if r == 0: return 0\n        r, op, d, sm = r+(sz\
    \ := seg.sz), seg.op, seg.d, seg.e\n        while True:\n            r -= 1\n\
    \            while r > 1 and r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n\
    \                while r < sz:\n                    if f(op(d[r:=r<<1|1], sm)):\
    \ sm, r = op(d[r], sm), r-1\n                return r + 1 - sz\n            sm\
    \ = op(d[r], sm)\n            if (r & -r) == r: return 0\n\nclass SegTree4(SegTree[_T]):\n\
    \    _lst = list4\n"
  code: "import cp_library.__header__\nfrom cp_library.misc.typing import _T\nimport\
    \ cp_library.ds.__header__\nfrom cp_library.ds.list.list4_cls import list4\nimport\
    \ cp_library.ds.tree.__header__\nimport cp_library.ds.tree.seg.__header__\nfrom\
    \ cp_library.ds.tree.seg.segtree_cls import SegTree\n\nclass SegTree4(SegTree[_T]):\n\
    \    _lst = list4"
  dependsOn:
  - cp_library/ds/list/list4_cls.py
  - cp_library/ds/tree/seg/segtree_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: cp_library/ds/tree/seg/segtree4_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/tree/seg/segtree4_cls_test.py
documentation_of: cp_library/ds/tree/seg/segtree4_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/seg/segtree4_cls.py
- /library/cp_library/ds/tree/seg/segtree4_cls.py.html
title: cp_library/ds/tree/seg/segtree4_cls.py
---
