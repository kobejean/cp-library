---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
    title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
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
    \ TypeVar('T')\n_U = TypeVar('U')\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n         \
    \   \u2503                                    7 \u2503            \n         \
    \   \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\
    \u251B            \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513     \
    \            \u2502              \n            \u2503                3 \u2503\u25C4\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\
    \u2501\u251B                 \u2502              \n            \u250F\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2513       \u2502              \n            \u2503\
    \      1 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5\
    \ \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524              \n     \
    \       \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502\
    \  \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502 \
    \             \n            \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\
    \u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\
    \u2501\u2501\u2513  \u2502              \n            \u2503 0 \u2503\u25C4\u2500\
    \u2524  \u2503 2 \u2503\u25C4\u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524 \
    \ \u2503 6 \u2503\u25C4\u2500\u2524              \n            \u2517\u2501\u252F\
    \u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\
    \u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502              \n \
    \             \u2502    \u2502    \u2502    \u2502    \u2502    \u2502    \u2502\
    \    \u2502              \n              \u25BC    \u25BC    \u25BC    \u25BC\
    \    \u25BC    \u25BC    \u25BC    \u25BC              \n            \u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\
    \u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513     \
    \       \n            \u2503 0 \u2503\u2503 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\
    \u2503 4 \u2503\u2503 5 \u2503\u2503 6 \u2503\u2503 7 \u2503            \n   \
    \         \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\
    \u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B            \n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n           Data Structure - Tree - Binary Index Tree     \
    \       \n'''\n\nclass BITMonoid(Generic[_T]):\n    def __init__(bit, op: Callable[[_T,_T],_T],\
    \ e: _T, v: Union[int,list[_T]]):\n        if isinstance(v, int): bit.d, bit.n\
    \ = [e]*v, v\n        else: bit.build(v)\n        bit.op, bit.e = op, e\n\n  \
    \  def __len__(bit) -> int:\n        return bit.n\n\n    def build(bit, d: list[_T])\
    \ -> None:\n        bit.d, bit.n = d, len(d)\n        for i in range(bit.n):\n\
    \            if (r := i|(i+1)) < bit.n: d[r] = bit.op(d[i], d[r])\n\n    def add(bit,\
    \ i: int, x: _T) -> None:\n        assert 0 <= i < bit.n\n        while i < bit.n:\n\
    \            bit.d[i] = bit.op(bit.d[i], x)\n            i |= i+1\n\n    def sum(bit,\
    \ r: int) -> _T:\n        assert 0 <= r <= bit.n\n        s = bit.e\n        while\
    \ r: s, r = bit.op(s,bit.d[r-1]), r&r-1\n        return s\n       \n    def prelist(bit)\
    \ -> list[_T]:\n        pre = [bit.e]+bit.d\n        for i in range(bit.n+1):\
    \ pre[i] = bit.op(pre[i&(i-1)], pre[i])\n        return pre\n\n    def bisect_left(bit,\
    \ v) -> int:\n        if v <= bit.e: return 0\n        i, s = 0, bit.e\n     \
    \   ni = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ < v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n    \n \
    \   def bisect_right(bit, v) -> int:\n        i, s = 0, bit.e\n        ni = m\
    \ = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n"
  code: "import cp_library.__header__\nfrom typing import Callable, Generic, Union\n\
    from cp_library.misc.typing import _T\nimport cp_library.ds.__header__\nimport\
    \ cp_library.ds.tree.__header__\nimport cp_library.ds.tree.bit.__header__\n\n\
    class BITMonoid(Generic[_T]):\n    def __init__(bit, op: Callable[[_T,_T],_T],\
    \ e: _T, v: Union[int,list[_T]]):\n        if isinstance(v, int): bit.d, bit.n\
    \ = [e]*v, v\n        else: bit.build(v)\n        bit.op, bit.e = op, e\n\n  \
    \  def __len__(bit) -> int:\n        return bit.n\n\n    def build(bit, d: list[_T])\
    \ -> None:\n        bit.d, bit.n = d, len(d)\n        for i in range(bit.n):\n\
    \            if (r := i|(i+1)) < bit.n: d[r] = bit.op(d[i], d[r])\n\n    def add(bit,\
    \ i: int, x: _T) -> None:\n        assert 0 <= i < bit.n\n        while i < bit.n:\n\
    \            bit.d[i] = bit.op(bit.d[i], x)\n            i |= i+1\n\n    def sum(bit,\
    \ r: int) -> _T:\n        assert 0 <= r <= bit.n\n        s = bit.e\n        while\
    \ r: s, r = bit.op(s,bit.d[r-1]), r&r-1\n        return s\n       \n    def prelist(bit)\
    \ -> list[_T]:\n        pre = [bit.e]+bit.d\n        for i in range(bit.n+1):\
    \ pre[i] = bit.op(pre[i&(i-1)], pre[i])\n        return pre\n\n    def bisect_left(bit,\
    \ v) -> int:\n        if v <= bit.e: return 0\n        i, s = 0, bit.e\n     \
    \   ni = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ < v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n    \n \
    \   def bisect_right(bit, v) -> int:\n        i, s = 0, bit.e\n        ni = m\
    \ = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/bit/bit_monoid_cls.py
  requiredBy: []
  timestamp: '2025-07-10 02:39:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
documentation_of: cp_library/ds/tree/bit/bit_monoid_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit/bit_monoid_cls.py
- /library/cp_library/ds/tree/bit/bit_monoid_cls.py.html
title: cp_library/ds/tree/bit/bit_monoid_cls.py
---
