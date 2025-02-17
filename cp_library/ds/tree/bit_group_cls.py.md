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
    from typing import Callable, Sequence, Union\nfrom typing import TypeVar\n_T =\
    \ TypeVar('T')\n\nclass BITGroup(Sequence[_T]):\n    def __init__(bit, op: Callable[[_T,_T],_T],\
    \ diff: Callable[[_T,_T],_T], e: _T, v: Union[int,list[_T]]):\n        if isinstance(v,\
    \ int): bit.data, bit.size = [e]*v, v\n        else: bit.build(v)\n        bit.op,\
    \ bit.e, bit.diff = op, e, diff\n\n    def __len__(bit) -> int:\n        return\
    \ bit.size\n\n    def build(bit, data: list[_T]) -> None:\n        bit.data, bit.size\
    \ = data, len(data)\n        for i in range(bit.size):\n            if (r := i|(i+1))\
    \ < bit.size: data[r] = bit.op(data[r], data[i])\n\n    def get(bit, i: int) ->\
    \ _T:\n        assert 0 <= i < bit.size\n        s, z = (data := bit.data)[i],\
    \ i&(i+1)\n        for _ in range((i^z).bit_count()):\n            s, i = bit.diff(s,\
    \ data[i-1]), i-(i&-i)\n        return s\n    __getitem__ = get\n    \n    def\
    \ set(bit, i: int, x: _T) -> None:\n        bit.add(i, bit.diff(x, bit.get(i)))\n\
    \    __setitem__ = set\n        \n    def add(bit, i: int, x: _T) -> None:\n \
    \       assert 0 <= i < bit.size\n        data, size = bit.data, bit.size\n  \
    \      while i < size:\n            data[i], i = bit.op(data[i],x), i|(i+1)\n\n\
    \    def sum(bit, n: int) -> _T:\n        assert 0 <= n <= bit.size\n        s,\
    \ z, i, data = 0, n.bit_count(), n-1, bit.data\n        for _ in range(z): s,\
    \ i = bit.op(s,data[i]), (i&(i+1))-1\n        return s\n    \n    def range_sum(bit,\
    \ l: int, r: int) -> _T:\n        return bit.diff(bit.sum(r),bit.sum(l))\n\n \
    \   def presum(bit) -> list[_T]:\n        pre = [bit.e]+bit.data\n        for\
    \ i in range(bit.size+1): pre[i] = bit.op(pre[i], pre[i&(i-1)])\n        return\
    \ pre\n    \n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)+1\n\
    \    \n    def bisect_right(bit, v) -> int:\n        d, i, s, m, n = bit.data,\
    \ 0, bit.e, bit.lead, bit.size\n        while m:\n            if (ni:=i|m) <=\
    \ n and (ns:=bit.op(s,d[ni-1])) <= v: s, i = ns, ni\n            m >>= 1\n   \
    \     return i\n"
  code: "import cp_library.ds.__header__\nfrom typing import Callable, Sequence, Union\n\
    from cp_library.misc.typing import _T\n\nclass BITGroup(Sequence[_T]):\n    def\
    \ __init__(bit, op: Callable[[_T,_T],_T], diff: Callable[[_T,_T],_T], e: _T, v:\
    \ Union[int,list[_T]]):\n        if isinstance(v, int): bit.data, bit.size = [e]*v,\
    \ v\n        else: bit.build(v)\n        bit.op, bit.e, bit.diff = op, e, diff\n\
    \n    def __len__(bit) -> int:\n        return bit.size\n\n    def build(bit,\
    \ data: list[_T]) -> None:\n        bit.data, bit.size = data, len(data)\n   \
    \     for i in range(bit.size):\n            if (r := i|(i+1)) < bit.size: data[r]\
    \ = bit.op(data[r], data[i])\n\n    def get(bit, i: int) -> _T:\n        assert\
    \ 0 <= i < bit.size\n        s, z = (data := bit.data)[i], i&(i+1)\n        for\
    \ _ in range((i^z).bit_count()):\n            s, i = bit.diff(s, data[i-1]), i-(i&-i)\n\
    \        return s\n    __getitem__ = get\n    \n    def set(bit, i: int, x: _T)\
    \ -> None:\n        bit.add(i, bit.diff(x, bit.get(i)))\n    __setitem__ = set\n\
    \        \n    def add(bit, i: int, x: _T) -> None:\n        assert 0 <= i < bit.size\n\
    \        data, size = bit.data, bit.size\n        while i < size:\n          \
    \  data[i], i = bit.op(data[i],x), i|(i+1)\n\n    def sum(bit, n: int) -> _T:\n\
    \        assert 0 <= n <= bit.size\n        s, z, i, data = 0, n.bit_count(),\
    \ n-1, bit.data\n        for _ in range(z): s, i = bit.op(s,data[i]), (i&(i+1))-1\n\
    \        return s\n    \n    def range_sum(bit, l: int, r: int) -> _T:\n     \
    \   return bit.diff(bit.sum(r),bit.sum(l))\n\n    def presum(bit) -> list[_T]:\n\
    \        pre = [bit.e]+bit.data\n        for i in range(bit.size+1): pre[i] =\
    \ bit.op(pre[i], pre[i&(i-1)])\n        return pre\n    \n    def bisect_left(bit,\
    \ v) -> int:\n        return bit.bisect_right(v-1)+1\n    \n    def bisect_right(bit,\
    \ v) -> int:\n        d, i, s, m, n = bit.data, 0, bit.e, bit.lead, bit.size\n\
    \        while m:\n            if (ni:=i|m) <= n and (ns:=bit.op(s,d[ni-1])) <=\
    \ v: s, i = ns, ni\n            m >>= 1\n        return i\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/bit_group_cls.py
  requiredBy: []
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/bit_group_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit_group_cls.py
- /library/cp_library/ds/tree/bit_group_cls.py.html
title: cp_library/ds/tree/bit_group_cls.py
---
