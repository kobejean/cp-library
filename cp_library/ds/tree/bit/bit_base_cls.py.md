---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit2_cls.py
    title: cp_library/ds/tree/bit/bit2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit3_cls.py
    title: cp_library/ds/tree/bit/bit3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit4_cls.py
    title: cp_library/ds/tree/bit/bit4_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit5_cls.py
    title: cp_library/ds/tree/bit/bit5_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit6_cls.py
    title: cp_library/ds/tree/bit/bit6_cls.py
  - icon: ':warning:'
    path: perf/bit2.py
    title: perf/bit2.py
  - icon: ':warning:'
    path: perf/bit6.py
    title: perf/bit6.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit2_cls_test.py
    title: test/unittests/ds/tree/bit/bit2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit3_cls_test.py
    title: test/unittests/ds/tree/bit/bit3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit4_cls_test.py
    title: test/unittests/ds/tree/bit/bit4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit5_cls_test.py
    title: test/unittests/ds/tree/bit/bit5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit6_cls_test.py
    title: test/unittests/ds/tree/bit/bit6_cls_test.py
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
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\nfrom typing import Generic, Union,\
    \ Callable, Optional\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n            \u2503   \
    \                                 7 \u2503            \n            \u2517\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \       \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513                 \u2502\
    \              \n            \u2503                3 \u2503\u25C4\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \            \u2502              \n            \u250F\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513       \u2502              \n            \u2503      1 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\
    \u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u252F\u2501\u251B       \u2502              \n            \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502     \
    \         \n            \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\
    \u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524\
    \              \n            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502              \n              \u2502    \u2502    \u2502\
    \    \u2502    \u2502    \u2502    \u2502    \u2502              \n          \
    \    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC\
    \              \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\
    \u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503\
    \ 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6\
    \ \u2503\u2503 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\
    \u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data\
    \ Structure - Tree - Binary Index Tree            \n'''\n\nclass BITBase(Generic[_T]):\n\
    \    _lst = list\n    K: int = 1\n    \n    def __init__(bit, v: Union[int, list[_T]],\
    \ e: _T = None) -> None:\n        if isinstance(v, int):\n            bit._n =\
    \ v\n            if bit._lst is list:\n                bit._d = [e]*v if e is\
    \ not None else [0]*v\n            elif e is not None:\n                bit._d\
    \ = bit._lst(*([e_]*v for e_ in e))\n            else:\n                bit._d\
    \ = bit._lst(*([0]*v for _ in range(bit.K)))\n        else:\n            bit.build(v)\n\
    \        bit.e = e if e is not None else (0 if bit._lst is list else tuple(0 for\
    \ _ in range(bit.K)))\n        bit._lb = 1 << bit._n.bit_length()\n\n    def build(bit,\
    \ data: list[_T]):\n        bit._n = len(data)\n        if bit._lst is list:\n\
    \            bit._d = bit._lst(data)\n        else:\n            bit._d = bit._lst(*([data[i][j]\
    \ for i in range(len(data))] for j in range(len(data[0]))))\n        for i in\
    \ range(bit._n):\n            if (r := i | i + 1) < bit._n:\n                bit._add(r,\
    \ bit._d[i])\n\n    def _add(bit, i: int, x: _T) -> None:\n        bit._d[i] =\
    \ bit._op(bit._d[i], x)\n    \n    def _op(bit, a: _T, b: _T) -> _T:\n       \
    \ return a + b\n    \n    def _sub(bit, a: _T, b: _T) -> _T:\n        return a\
    \ - b\n\n    def add(bit, i: int, x: _T) -> None:\n        while i < bit._n: bit._add(i,\
    \ x); i |= i + 1\n\n    def sum(bit, n: int) -> _T:\n        s = bit.e\n     \
    \   while n: s, n = bit._op(s, bit._d[n - 1]), n & n - 1\n        return s\n\n\
    \    def sum_range(bit, l: int, r: int) -> _T:\n        s = bit.e\n        while\
    \ r: s, r = bit._op(s, bit._d[r - 1]), r & r - 1\n        while l: s, l = bit._sub(s,\
    \ bit._d[l - 1]), l & l - 1\n        return s\n\n    def __len__(bit) -> int:\
    \ return bit._n\n\n    def __getitem__(bit, i: int) -> _T:\n        s, l = bit._d[i],\
    \ i & (i + 1)\n        while l != i: s, i = bit._sub(s, bit._d[i - 1]), i - (i\
    \ & -i)\n        return s\n\n    get = __getitem__\n\n    def __setitem__(bit,\
    \ i: int, x: _T) -> None:\n        bit.add(i, bit._sub(x, bit[i]))\n\n    set\
    \ = __setitem__\n\n    def prelist(bit) -> list[_T]:\n        pre = [bit.e] +\
    \ bit._d[:] if bit._lst is list else bit._lst(*([e_] * (bit._n + 1) for e_ in\
    \ bit.e))\n        for i in range(bit._n): pre[i+1] = bit._d[i]\n        for i\
    \ in range(bit._n + 1):\n            if i & i - 1 < bit._n + 1:\n            \
    \    pre[i] = bit._op(pre[i], pre[i & i - 1])\n        return pre\n\n    def bisect_left(bit,\
    \ v, key: Optional[Callable] = None) -> int:\n        i = 0\n        s = bit.e\n\
    \        if v <= s: return -1\n        m = bit._lb\n        \n        if key:\n\
    \            while m := m >> 1:\n                if (ni := m | i) <= bit._n and\
    \ key(ns := bit._op(s, bit._d[ni - 1])) < v:\n                    s, i = ns, ni\n\
    \        else:\n            while m := m >> 1:\n                if (ni := m |\
    \ i) <= bit._n and (ns := bit._op(s, bit._d[ni - 1])) < v:\n                 \
    \   s, i = ns, ni\n        return i\n\n    def bisect_right(bit, v, key: Optional[Callable]\
    \ = None) -> int:\n        i = 0\n        s = bit.e\n        m = bit._lb\n   \
    \     \n        if key:\n            while m := m >> 1:\n                if (ni\
    \ := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni - 1])) <= v:\n      \
    \              s, i = ns, ni\n        else:\n            while m := m >> 1:\n\
    \                if (ni := m | i) <= bit._n and (ns := bit._op(s, bit._d[ni -\
    \ 1])) <= v:\n                    s, i = ns, ni\n        return i\n"
  code: "import cp_library.__header__\nfrom cp_library.misc.typing import _T\nfrom\
    \ typing import Generic, Union, Callable, Optional\nimport cp_library.ds.__header__\n\
    import cp_library.ds.tree.__header__\nimport cp_library.ds.tree.bit.__header__\n\
    \nclass BITBase(Generic[_T]):\n    _lst = list\n    K: int = 1\n    \n    def\
    \ __init__(bit, v: Union[int, list[_T]], e: _T = None) -> None:\n        if isinstance(v,\
    \ int):\n            bit._n = v\n            if bit._lst is list:\n          \
    \      bit._d = [e]*v if e is not None else [0]*v\n            elif e is not None:\n\
    \                bit._d = bit._lst(*([e_]*v for e_ in e))\n            else:\n\
    \                bit._d = bit._lst(*([0]*v for _ in range(bit.K)))\n        else:\n\
    \            bit.build(v)\n        bit.e = e if e is not None else (0 if bit._lst\
    \ is list else tuple(0 for _ in range(bit.K)))\n        bit._lb = 1 << bit._n.bit_length()\n\
    \n    def build(bit, data: list[_T]):\n        bit._n = len(data)\n        if\
    \ bit._lst is list:\n            bit._d = bit._lst(data)\n        else:\n    \
    \        bit._d = bit._lst(*([data[i][j] for i in range(len(data))] for j in range(len(data[0]))))\n\
    \        for i in range(bit._n):\n            if (r := i | i + 1) < bit._n:\n\
    \                bit._add(r, bit._d[i])\n\n    def _add(bit, i: int, x: _T) ->\
    \ None:\n        bit._d[i] = bit._op(bit._d[i], x)\n    \n    def _op(bit, a:\
    \ _T, b: _T) -> _T:\n        return a + b\n    \n    def _sub(bit, a: _T, b: _T)\
    \ -> _T:\n        return a - b\n\n    def add(bit, i: int, x: _T) -> None:\n \
    \       while i < bit._n: bit._add(i, x); i |= i + 1\n\n    def sum(bit, n: int)\
    \ -> _T:\n        s = bit.e\n        while n: s, n = bit._op(s, bit._d[n - 1]),\
    \ n & n - 1\n        return s\n\n    def sum_range(bit, l: int, r: int) -> _T:\n\
    \        s = bit.e\n        while r: s, r = bit._op(s, bit._d[r - 1]), r & r -\
    \ 1\n        while l: s, l = bit._sub(s, bit._d[l - 1]), l & l - 1\n        return\
    \ s\n\n    def __len__(bit) -> int: return bit._n\n\n    def __getitem__(bit,\
    \ i: int) -> _T:\n        s, l = bit._d[i], i & (i + 1)\n        while l != i:\
    \ s, i = bit._sub(s, bit._d[i - 1]), i - (i & -i)\n        return s\n\n    get\
    \ = __getitem__\n\n    def __setitem__(bit, i: int, x: _T) -> None:\n        bit.add(i,\
    \ bit._sub(x, bit[i]))\n\n    set = __setitem__\n\n    def prelist(bit) -> list[_T]:\n\
    \        pre = [bit.e] + bit._d[:] if bit._lst is list else bit._lst(*([e_] *\
    \ (bit._n + 1) for e_ in bit.e))\n        for i in range(bit._n): pre[i+1] = bit._d[i]\n\
    \        for i in range(bit._n + 1):\n            if i & i - 1 < bit._n + 1:\n\
    \                pre[i] = bit._op(pre[i], pre[i & i - 1])\n        return pre\n\
    \n    def bisect_left(bit, v, key: Optional[Callable] = None) -> int:\n      \
    \  i = 0\n        s = bit.e\n        if v <= s: return -1\n        m = bit._lb\n\
    \        \n        if key:\n            while m := m >> 1:\n                if\
    \ (ni := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni - 1])) < v:\n   \
    \                 s, i = ns, ni\n        else:\n            while m := m >> 1:\n\
    \                if (ni := m | i) <= bit._n and (ns := bit._op(s, bit._d[ni -\
    \ 1])) < v:\n                    s, i = ns, ni\n        return i\n\n    def bisect_right(bit,\
    \ v, key: Optional[Callable] = None) -> int:\n        i = 0\n        s = bit.e\n\
    \        m = bit._lb\n        \n        if key:\n            while m := m >> 1:\n\
    \                if (ni := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni\
    \ - 1])) <= v:\n                    s, i = ns, ni\n        else:\n           \
    \ while m := m >> 1:\n                if (ni := m | i) <= bit._n and (ns := bit._op(s,\
    \ bit._d[ni - 1])) <= v:\n                    s, i = ns, ni\n        return i"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/bit/bit_base_cls.py
  requiredBy:
  - cp_library/ds/tree/bit/bit2_cls.py
  - cp_library/ds/tree/bit/bit6_cls.py
  - cp_library/ds/tree/bit/bit4_cls.py
  - cp_library/ds/tree/bit/bit5_cls.py
  - cp_library/ds/tree/bit/bit3_cls.py
  - perf/bit6.py
  - perf/bit2.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/tree/bit/bit4_cls_test.py
  - test/unittests/ds/tree/bit/bit6_cls_test.py
  - test/unittests/ds/tree/bit/bit5_cls_test.py
  - test/unittests/ds/tree/bit/bit3_cls_test.py
  - test/unittests/ds/tree/bit/bit2_cls_test.py
documentation_of: cp_library/ds/tree/bit/bit_base_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit/bit_base_cls.py
- /library/cp_library/ds/tree/bit/bit_base_cls.py.html
title: cp_library/ds/tree/bit/bit_base_cls.py
---
