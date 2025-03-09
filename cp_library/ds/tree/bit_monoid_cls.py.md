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
    from typing import Callable, Sized, Union\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    \nclass BITMonoid(Sized[_T]):\n    def __init__(bit, op: Callable[[_T,_T],_T],\
    \ e: _T, v: Union[int,list[_T]]):\n        if isinstance(v, int): bit.d, bit.n\
    \ = [e]*v, v\n        else: bit.build(v)\n        bit.op, bit.e = op, e\n\n  \
    \  def __len__(bit) -> int:\n        return bit.n\n\n    def build(bit, d: list[_T])\
    \ -> None:\n        bit.d, bit.n = d, len(d)\n        for i in range(bit.n):\n\
    \            if (r := i|(i+1)) < bit.n: d[r] = bit.op(d[r], d[i])\n        \n\
    \    def add(bit, i: int, x: _T) -> None:\n        assert 0 <= i < bit.n\n   \
    \     d, n = bit.d, bit.n\n        while i < n:\n            d[i], i = bit.op(d[i],x),\
    \ i|(i+1)\n\n    def sum(bit, r: int) -> _T:\n        assert 0 <= r <= bit.n\n\
    \        s, z, i, d = 0, r.bit_count(), r-1, bit.d\n        for _ in range(z):\
    \ s, i = bit.op(s,d[i]), (i&(i+1))-1\n        return s\n       \n    def prelist(bit)\
    \ -> list[_T]:\n        pre = [bit.e]+bit.d\n        for i in range(bit.n+1):\
    \ pre[i] = bit.op(pre[i], pre[i&(i-1)])\n        return pre\n\n    def bisect_left(bit,\
    \ v) -> int:\n        if v <= bit.e: return 0\n        i, s = 0, bit.e\n     \
    \   ni = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ < v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n    \n \
    \   def bisect_right(bit, v) -> int:\n        i, s = 0, bit.e\n        ni = m\
    \ = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n"
  code: "import cp_library.ds.__header__\nfrom typing import Callable, Sized, Union\n\
    from cp_library.misc.typing import _T\n\nclass BITMonoid(Sized[_T]):\n    def\
    \ __init__(bit, op: Callable[[_T,_T],_T], e: _T, v: Union[int,list[_T]]):\n  \
    \      if isinstance(v, int): bit.d, bit.n = [e]*v, v\n        else: bit.build(v)\n\
    \        bit.op, bit.e = op, e\n\n    def __len__(bit) -> int:\n        return\
    \ bit.n\n\n    def build(bit, d: list[_T]) -> None:\n        bit.d, bit.n = d,\
    \ len(d)\n        for i in range(bit.n):\n            if (r := i|(i+1)) < bit.n:\
    \ d[r] = bit.op(d[r], d[i])\n        \n    def add(bit, i: int, x: _T) -> None:\n\
    \        assert 0 <= i < bit.n\n        d, n = bit.d, bit.n\n        while i <\
    \ n:\n            d[i], i = bit.op(d[i],x), i|(i+1)\n\n    def sum(bit, r: int)\
    \ -> _T:\n        assert 0 <= r <= bit.n\n        s, z, i, d = 0, r.bit_count(),\
    \ r-1, bit.d\n        for _ in range(z): s, i = bit.op(s,d[i]), (i&(i+1))-1\n\
    \        return s\n       \n    def prelist(bit) -> list[_T]:\n        pre = [bit.e]+bit.d\n\
    \        for i in range(bit.n+1): pre[i] = bit.op(pre[i], pre[i&(i-1)])\n    \
    \    return pre\n\n    def bisect_left(bit, v) -> int:\n        if v <= bit.e:\
    \ return 0\n        i, s = 0, bit.e\n        ni = m = bit.lb\n        while m:\n\
    \            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1])) < v: s, i = ns, ni\n\
    \            ni = (m:=m>>1)|i\n        return i\n    \n    def bisect_right(bit,\
    \ v) -> int:\n        i, s = 0, bit.e\n        ni = m = bit.lb\n        while\
    \ m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1])) <= v: s, i =\
    \ ns, ni\n            ni = (m:=m>>1)|i\n        return i"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/bit_monoid_cls.py
  requiredBy: []
  timestamp: '2025-03-09 20:40:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/bit_monoid_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit_monoid_cls.py
- /library/cp_library/ds/tree/bit_monoid_cls.py.html
title: cp_library/ds/tree/bit_monoid_cls.py
---
