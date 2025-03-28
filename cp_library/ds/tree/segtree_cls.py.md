---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_a_segtree.test.py
    title: test/aoj/dsl/dsl_2_a_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite.test.py
    title: test/library-checker/data-structure/point_set_range_composite.test.py
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
    from typing import Callable, Generic, Union\nfrom typing import TypeVar\n_T =\
    \ TypeVar('T')\n\n\n\nclass SegTree(Generic[_T]):\n    def __init__(seg, op: Callable[[_T,\
    \ _T], _T], e: _T, v: Union[int, list[_T]]) -> None:\n        if isinstance(v,\
    \ int): v = [e] * v\n        seg.op, seg.e, seg.n = op, e, (n := len(v))\n   \
    \     seg.log, seg.sz, seg.d = (log := (n-1).bit_length()+1), (sz := 1 << log),\
    \ [e] * (sz << 1)\n        for i in range(n): seg.d[sz + i] = v[i]\n        for\
    \ i in range(sz-1,0,-1): seg.d[i] = op(seg.d[i<<1], seg.d[i<<1|1])\n\n    def\
    \ set(seg, p: int, x: _T) -> None:\n        seg.d[p := p + seg.sz], op = x, seg.op\n\
    \        for _ in range(seg.log): seg.d[p:=p>>1] = op(seg.d[p:=p^(p&1)], seg.d[p|1])\n\
    \    __setitem__ = set\n\n    def get(seg, p: int) -> _T:\n        return seg.d[p\
    \ + seg.sz]\n    __getitem__ = get\n\n    def prod(seg, l: int, r: int) -> _T:\n\
    \        sml = smr = seg.e\n        l, r = l+seg.sz, r+seg.sz\n        while l\
    \ < r:\n            if l&1: sml, l = seg.op(sml, seg.d[l]), l+1\n            if\
    \ r&1: smr = seg.op(seg.d[r:=r-1], smr)\n            l, r = l >> 1, r >> 1\n \
    \       return seg.op(sml, smr)\n\n    def all_prod(seg) -> _T:\n        return\
    \ seg.d[1]\n\n    def max_right(seg, l: int, f: Callable[[_T], bool]) -> int:\n\
    \        assert 0 <= l <= seg.n\n        assert f(seg.e)\n        if l == seg.n:\
    \ return seg.n\n        l, op, d, sm = l+(sz := seg.sz), seg.op, seg.d, seg.e\n\
    \        while True:\n            while l&1 == 0: l >>= 1\n            if not\
    \ f(op(sm, d[l])):\n                while l < sz:\n                    if f(op(sm,\
    \ d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n                return l - sz\n   \
    \         sm, l = op(sm, d[l]), l+1\n            if l&-l == l: return seg.n\n\n\
    \    def min_left(seg, r: int, f: Callable[[_T], bool]) -> int:\n        assert\
    \ 0 <= r <= seg.n\n        assert f(seg.e)\n        if r == 0: return 0\n    \
    \    r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d, seg.e\n        while True:\n\
    \            r -= 1\n            while r > 1 and r & 1: r >>= 1\n            if\
    \ not f(op(d[r], sm)):\n                while r < sz:\n                    if\
    \ f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm), r-1\n                return r\
    \ + 1 - sz\n            sm = op(d[r], sm)\n            if (r & -r) == r: return\
    \ 0\n"
  code: "import cp_library.__header__\nfrom typing import Callable, Generic, Union\n\
    from cp_library.misc.typing import _T\nimport cp_library.ds.__header__\nimport\
    \ cp_library.ds.tree.__header__\n\nclass SegTree(Generic[_T]):\n    def __init__(seg,\
    \ op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) -> None:\n     \
    \   if isinstance(v, int): v = [e] * v\n        seg.op, seg.e, seg.n = op, e,\
    \ (n := len(v))\n        seg.log, seg.sz, seg.d = (log := (n-1).bit_length()+1),\
    \ (sz := 1 << log), [e] * (sz << 1)\n        for i in range(n): seg.d[sz + i]\
    \ = v[i]\n        for i in range(sz-1,0,-1): seg.d[i] = op(seg.d[i<<1], seg.d[i<<1|1])\n\
    \n    def set(seg, p: int, x: _T) -> None:\n        seg.d[p := p + seg.sz], op\
    \ = x, seg.op\n        for _ in range(seg.log): seg.d[p:=p>>1] = op(seg.d[p:=p^(p&1)],\
    \ seg.d[p|1])\n    __setitem__ = set\n\n    def get(seg, p: int) -> _T:\n    \
    \    return seg.d[p + seg.sz]\n    __getitem__ = get\n\n    def prod(seg, l: int,\
    \ r: int) -> _T:\n        sml = smr = seg.e\n        l, r = l+seg.sz, r+seg.sz\n\
    \        while l < r:\n            if l&1: sml, l = seg.op(sml, seg.d[l]), l+1\n\
    \            if r&1: smr = seg.op(seg.d[r:=r-1], smr)\n            l, r = l >>\
    \ 1, r >> 1\n        return seg.op(sml, smr)\n\n    def all_prod(seg) -> _T:\n\
    \        return seg.d[1]\n\n    def max_right(seg, l: int, f: Callable[[_T], bool])\
    \ -> int:\n        assert 0 <= l <= seg.n\n        assert f(seg.e)\n        if\
    \ l == seg.n: return seg.n\n        l, op, d, sm = l+(sz := seg.sz), seg.op, seg.d,\
    \ seg.e\n        while True:\n            while l&1 == 0: l >>= 1\n          \
    \  if not f(op(sm, d[l])):\n                while l < sz:\n                  \
    \  if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n                return\
    \ l - sz\n            sm, l = op(sm, d[l]), l+1\n            if l&-l == l: return\
    \ seg.n\n\n    def min_left(seg, r: int, f: Callable[[_T], bool]) -> int:\n  \
    \      assert 0 <= r <= seg.n\n        assert f(seg.e)\n        if r == 0: return\
    \ 0\n        r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d, seg.e\n        while\
    \ True:\n            r -= 1\n            while r > 1 and r & 1: r >>= 1\n    \
    \        if not f(op(d[r], sm)):\n                while r < sz:\n            \
    \        if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm), r-1\n             \
    \   return r + 1 - sz\n            sm = op(d[r], sm)\n            if (r & -r)\
    \ == r: return 0"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/segtree_cls.py
  requiredBy: []
  timestamp: '2025-03-28 19:21:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl/dsl_2_a_segtree.test.py
  - test/library-checker/data-structure/point_set_range_composite.test.py
documentation_of: cp_library/ds/tree/segtree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/segtree_cls.py
- /library/cp_library/ds/tree/segtree_cls.py.html
title: cp_library/ds/tree/segtree_cls.py
---
