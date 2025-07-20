---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_commutative_cls.py
    title: cp_library/alg/tree/csr/hld_commutative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_monoid_cls.py
    title: cp_library/alg/tree/csr/hld_monoid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree2_cls.py
    title: cp_library/ds/tree/seg/segtree2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree3_cls.py
    title: cp_library/ds/tree/seg/segtree3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree4_cls.py
    title: cp_library/ds/tree/seg/segtree4_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree5_cls.py
    title: cp_library/ds/tree/seg/segtree5_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree6_cls.py
    title: cp_library/ds/tree/seg/segtree6_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_segtree_cls.py
    title: cp_library/ds/wavelet/wm_segtree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_segtree_compressed_cls.py
    title: cp_library/ds/wavelet/wm_segtree_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_segtree_points_cls.py
    title: cp_library/ds/wavelet/wm_segtree_points_cls.py
  - icon: ':warning:'
    path: perf/segtree2.py
    title: perf/segtree2.py
  - icon: ':warning:'
    path: perf/segtree6.py
    title: perf/segtree6.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_a_segtree.test.py
    title: test/aoj/dsl/dsl_2_a_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite.test.py
    title: test/library-checker/data-structure/point_set_range_composite.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_segtree_points.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_segtree_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_add_path_sum_hld_commutative.test.py
    title: test/library-checker/tree/vertex_add_path_sum_hld_commutative.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_add_path_sum_hld_monoid.test.py
    title: test/library-checker/tree/vertex_add_path_sum_hld_monoid.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_set_path_composite.test.py
    title: test/library-checker/tree/vertex_set_path_composite.test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree2_cls_test.py
    title: test/unittests/ds/tree/seg/segtree2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree3_cls_test.py
    title: test/unittests/ds/tree/seg/segtree3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree4_cls_test.py
    title: test/unittests/ds/tree/seg/segtree4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree5_cls_test.py
    title: test/unittests/ds/tree/seg/segtree5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree6_cls_test.py
    title: test/unittests/ds/tree/seg/segtree6_cls_test.py
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
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\nfrom typing import Callable, Generic,\
    \ Union\n\n\n\n\nclass SegTree(Generic[_T]):\n    _lst = list\n    \n    def __init__(seg,\
    \ op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) -> None:\n     \
    \   if isinstance(v, int): n = v; v = None\n        else: n = len(v)\n       \
    \ seg.op, seg.e, seg.n = op, e, n\n        seg.log, seg.sz = (log := (n-1).bit_length()+1),\
    \ (sz := 1 << log)\n        if seg._lst is list: seg.d = [e]*(sz<<1)\n       \
    \ else: seg.d = seg._lst(*([e_]*(sz<<1) for e_ in e))\n        if v: seg._build(v)\n\
    \n    def _build(seg, v):\n        for i in range(seg.n): seg.d[seg.sz + i] =\
    \ v[i]\n        for i in range(seg.sz-1,0,-1): seg._merge(i, i<<1, i<<1|1)\n \
    \   \n    def _merge(seg, i, j, k): seg.d[i] = seg.op(seg.d[j], seg.d[k])\n\n\
    \    def set(seg, p: int, x: _T) -> None:\n        p += seg.sz\n        seg.d[p]\
    \ = x\n        for _ in range(seg.log):\n            p = p^(p&1)\n           \
    \ seg._merge(p>>1, p, p|1)\n            p >>= 1\n    __setitem__ = set\n\n   \
    \ def get(seg, p: int) -> _T: return seg.d[p+seg.sz]\n    __getitem__ = get\n\n\
    \    def prod(seg, l: int, r: int) -> _T:\n        sml = smr = seg.e\n       \
    \ l, r = l+seg.sz, r+seg.sz\n        while l < r:\n            if l&1: sml, l\
    \ = seg.op(sml, seg.d[l]), l+1\n            if r&1: smr = seg.op(seg.d[r:=r-1],\
    \ smr)\n            l, r = l >> 1, r >> 1\n        return seg.op(sml, smr)\n\n\
    \    def all_prod(seg) -> _T: return seg.d[1]\n\n    def max_right(seg, l: int,\
    \ f: Callable[[_T], bool]) -> int:\n        assert 0 <= l <= seg.n\n        assert\
    \ f(seg.e)\n        if l == seg.n: return seg.n\n        l, op, d, sm = l+(sz\
    \ := seg.sz), seg.op, seg.d, seg.e\n        while True:\n            while l&1\
    \ == 0: l >>= 1\n            if not f(op(sm, d[l])):\n                while l\
    \ < sz:\n                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n\
    \                return l - sz\n            sm, l = op(sm, d[l]), l+1\n      \
    \      if l&-l == l: return seg.n\n\n    def min_left(seg, r: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= r <= seg.n\n        assert f(seg.e)\n  \
    \      if r == 0: return 0\n        r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d,\
    \ seg.e\n        while True:\n            r -= 1\n            while r > 1 and\
    \ r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n                while r\
    \ < sz:\n                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm),\
    \ r-1\n                return r + 1 - sz\n            sm = op(d[r], sm)\n    \
    \        if (r & -r) == r: return 0\n"
  code: "import cp_library.__header__\nfrom cp_library.misc.typing import _T\nfrom\
    \ typing import Callable, Generic, Union\nimport cp_library.ds.__header__\nimport\
    \ cp_library.ds.tree.__header__\nimport cp_library.ds.tree.seg.__header__\n\n\
    class SegTree(Generic[_T]):\n    _lst = list\n    \n    def __init__(seg, op:\
    \ Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) -> None:\n        if\
    \ isinstance(v, int): n = v; v = None\n        else: n = len(v)\n        seg.op,\
    \ seg.e, seg.n = op, e, n\n        seg.log, seg.sz = (log := (n-1).bit_length()+1),\
    \ (sz := 1 << log)\n        if seg._lst is list: seg.d = [e]*(sz<<1)\n       \
    \ else: seg.d = seg._lst(*([e_]*(sz<<1) for e_ in e))\n        if v: seg._build(v)\n\
    \n    def _build(seg, v):\n        for i in range(seg.n): seg.d[seg.sz + i] =\
    \ v[i]\n        for i in range(seg.sz-1,0,-1): seg._merge(i, i<<1, i<<1|1)\n \
    \   \n    def _merge(seg, i, j, k): seg.d[i] = seg.op(seg.d[j], seg.d[k])\n\n\
    \    def set(seg, p: int, x: _T) -> None:\n        p += seg.sz\n        seg.d[p]\
    \ = x\n        for _ in range(seg.log):\n            p = p^(p&1)\n           \
    \ seg._merge(p>>1, p, p|1)\n            p >>= 1\n    __setitem__ = set\n\n   \
    \ def get(seg, p: int) -> _T: return seg.d[p+seg.sz]\n    __getitem__ = get\n\n\
    \    def prod(seg, l: int, r: int) -> _T:\n        sml = smr = seg.e\n       \
    \ l, r = l+seg.sz, r+seg.sz\n        while l < r:\n            if l&1: sml, l\
    \ = seg.op(sml, seg.d[l]), l+1\n            if r&1: smr = seg.op(seg.d[r:=r-1],\
    \ smr)\n            l, r = l >> 1, r >> 1\n        return seg.op(sml, smr)\n\n\
    \    def all_prod(seg) -> _T: return seg.d[1]\n\n    def max_right(seg, l: int,\
    \ f: Callable[[_T], bool]) -> int:\n        assert 0 <= l <= seg.n\n        assert\
    \ f(seg.e)\n        if l == seg.n: return seg.n\n        l, op, d, sm = l+(sz\
    \ := seg.sz), seg.op, seg.d, seg.e\n        while True:\n            while l&1\
    \ == 0: l >>= 1\n            if not f(op(sm, d[l])):\n                while l\
    \ < sz:\n                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n\
    \                return l - sz\n            sm, l = op(sm, d[l]), l+1\n      \
    \      if l&-l == l: return seg.n\n\n    def min_left(seg, r: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= r <= seg.n\n        assert f(seg.e)\n  \
    \      if r == 0: return 0\n        r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d,\
    \ seg.e\n        while True:\n            r -= 1\n            while r > 1 and\
    \ r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n                while r\
    \ < sz:\n                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm),\
    \ r-1\n                return r + 1 - sz\n            sm = op(d[r], sm)\n    \
    \        if (r & -r) == r: return 0"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/seg/segtree_cls.py
  requiredBy:
  - cp_library/ds/wavelet/wm_segtree_points_cls.py
  - cp_library/ds/wavelet/wm_segtree_cls.py
  - cp_library/ds/wavelet/wm_segtree_compressed_cls.py
  - cp_library/ds/tree/seg/segtree4_cls.py
  - cp_library/ds/tree/seg/segtree6_cls.py
  - cp_library/ds/tree/seg/segtree3_cls.py
  - cp_library/ds/tree/seg/segtree2_cls.py
  - cp_library/ds/tree/seg/segtree5_cls.py
  - cp_library/alg/tree/csr/hld_monoid_cls.py
  - cp_library/alg/tree/csr/hld_commutative_cls.py
  - perf/segtree2.py
  - perf/segtree6.py
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/tree/vertex_set_path_composite.test.py
  - test/library-checker/tree/vertex_add_path_sum_hld_commutative.test.py
  - test/library-checker/tree/vertex_add_path_sum_hld_monoid.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
  - test/library-checker/data-structure/point_set_range_composite.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
  - test/library-checker/data-structure/point_set_range_composite_large_array.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree_points.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
  - test/unittests/ds/tree/seg/segtree2_cls_test.py
  - test/unittests/ds/tree/seg/segtree4_cls_test.py
  - test/unittests/ds/tree/seg/segtree3_cls_test.py
  - test/unittests/ds/tree/seg/segtree5_cls_test.py
  - test/unittests/ds/tree/seg/segtree6_cls_test.py
  - test/aoj/dsl/dsl_2_a_segtree.test.py
documentation_of: cp_library/ds/tree/seg/segtree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/seg/segtree_cls.py
- /library/cp_library/ds/tree/seg/segtree_cls.py.html
title: cp_library/ds/tree/seg/segtree_cls.py
---
