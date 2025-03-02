---
data:
  _extendedDependsOn: []
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
    from typing import Callable, Generic, Union\nfrom typing import TypeVar\n_T =\
    \ TypeVar('T')\n\nclass SegTree(Generic[_T]):\n    def __init__(self, op: Callable[[_T,\
    \ _T], _T], e: _T, v: Union[int, list[_T]]) -> None:\n        if isinstance(v,\
    \ int): v = [e] * v\n        self.op, self.e, self.n = op, e, (n := len(v))\n\
    \        self.log, self.sz, self.d = (log := (n-1).bit_length()+1), (sz := 1 <<\
    \ log), [e] * (sz << 1)\n        for i in range(n): self.d[sz + i] = v[i]\n  \
    \      for i in range(sz-1,0,-1): self.d[i] = op(self.d[i<<1], self.d[i<<1|1])\n\
    \n    def set(self, p: int, x: _T) -> None:\n        assert 0 <= p < self.n\n\
    \        (d := self.d)[p := p + self.sz], op = x, self.op\n        for _ in range(self.log):\
    \ d[p:=p>>1] = op(d[p:=p^(p&1)], d[p|1])\n    __setitem__ = set\n\n    def get(self,\
    \ p: int) -> _T:\n        assert 0 <= p < self.n\n        return self.d[p + self.sz]\n\
    \    __getitem__ = get\n\n    def prod(self, l: int, r: int) -> _T:\n        assert\
    \ 0 <= l <= r <= self.n\n        sml = smr = self.e\n        l, r, op, d = l+self.sz,\
    \ r+self.sz, self.op, self.d\n        while l < r:\n            if l&1: sml, l\
    \ = op(sml, d[l]), l+1\n            if r&1: smr = op(d[r:=r-1], smr)\n       \
    \     l, r = l >> 1, r >> 1\n        return op(sml, smr)\n\n    def all_prod(self)\
    \ -> _T:\n        return self.d[1]\n\n    def max_right(self, l: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= l <= self.n\n        assert f(self.e)\n\
    \        if l == self.n: return self.n\n        l, op, d, sm = l+(sz := self.sz),\
    \ self.op, self.d, self.e\n        while True:\n            while l&1 == 0: l\
    \ >>= 1\n            if not f(op(sm, d[l])):\n                while l < sz:\n\
    \                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n   \
    \             return l - sz\n            sm, l = op(sm, d[l]), l+1\n         \
    \   if l&-l == l: return self.n\n\n    def min_left(self, r: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= r <= self.n\n        assert f(self.e)\n\
    \        if r == 0: return 0\n        r, op, d, sm = r+(sz := self.sz), self.op,\
    \ self.d, self.e\n        while True:\n            r -= 1\n            while r\
    \ > 1 and r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n              \
    \  while r < sz:\n                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r],\
    \ sm), r-1\n                return r + 1 - sz\n            sm = op(d[r], sm)\n\
    \            if (r & -r) == r: return 0\n"
  code: "import cp_library.ds.__header__\nfrom typing import Callable, Generic, Union\n\
    from cp_library.misc.typing import _T\n\nclass SegTree(Generic[_T]):\n    def\
    \ __init__(self, op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) ->\
    \ None:\n        if isinstance(v, int): v = [e] * v\n        self.op, self.e,\
    \ self.n = op, e, (n := len(v))\n        self.log, self.sz, self.d = (log := (n-1).bit_length()+1),\
    \ (sz := 1 << log), [e] * (sz << 1)\n        for i in range(n): self.d[sz + i]\
    \ = v[i]\n        for i in range(sz-1,0,-1): self.d[i] = op(self.d[i<<1], self.d[i<<1|1])\n\
    \n    def set(self, p: int, x: _T) -> None:\n        assert 0 <= p < self.n\n\
    \        (d := self.d)[p := p + self.sz], op = x, self.op\n        for _ in range(self.log):\
    \ d[p:=p>>1] = op(d[p:=p^(p&1)], d[p|1])\n    __setitem__ = set\n\n    def get(self,\
    \ p: int) -> _T:\n        assert 0 <= p < self.n\n        return self.d[p + self.sz]\n\
    \    __getitem__ = get\n\n    def prod(self, l: int, r: int) -> _T:\n        assert\
    \ 0 <= l <= r <= self.n\n        sml = smr = self.e\n        l, r, op, d = l+self.sz,\
    \ r+self.sz, self.op, self.d\n        while l < r:\n            if l&1: sml, l\
    \ = op(sml, d[l]), l+1\n            if r&1: smr = op(d[r:=r-1], smr)\n       \
    \     l, r = l >> 1, r >> 1\n        return op(sml, smr)\n\n    def all_prod(self)\
    \ -> _T:\n        return self.d[1]\n\n    def max_right(self, l: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= l <= self.n\n        assert f(self.e)\n\
    \        if l == self.n: return self.n\n        l, op, d, sm = l+(sz := self.sz),\
    \ self.op, self.d, self.e\n        while True:\n            while l&1 == 0: l\
    \ >>= 1\n            if not f(op(sm, d[l])):\n                while l < sz:\n\
    \                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n   \
    \             return l - sz\n            sm, l = op(sm, d[l]), l+1\n         \
    \   if l&-l == l: return self.n\n\n    def min_left(self, r: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= r <= self.n\n        assert f(self.e)\n\
    \        if r == 0: return 0\n        r, op, d, sm = r+(sz := self.sz), self.op,\
    \ self.d, self.e\n        while True:\n            r -= 1\n            while r\
    \ > 1 and r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n              \
    \  while r < sz:\n                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r],\
    \ sm), r-1\n                return r + 1 - sz\n            sm = op(d[r], sm)\n\
    \            if (r & -r) == r: return 0"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/segtree_cls.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/segtree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/segtree_cls.py
- /library/cp_library/ds/tree/segtree_cls.py.html
title: cp_library/ds/tree/segtree_cls.py
---
