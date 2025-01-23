---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
    title: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
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
    from typing import Union\n\n\nclass BinaryIndexTree:\n    def __init__(bit, v:\
    \ Union[int,list]):\n        if isinstance(v, int):\n            bit.data, bit.size\
    \ = [0]*v, v\n        else:\n            bit.build(v)\n\n    def build(bit, data):\n\
    \        bit.data, bit.size = data, len(data)\n        for i in range(bit.size):\n\
    \            if (r := i|(i+1)) < bit.size: \n                data[r] += data[i]\n\
    \n    def get(bit, i: int):\n        assert 0 <= i < bit.size\n        s, z =\
    \ (data := bit.data)[i], i&(i+1)\n        for _ in range((i^z).bit_count()):\n\
    \            s, i = s-data[i-1], i-(i&-i)\n        return s\n    __getitem__ =\
    \ get\n    \n    def set(bit, i: int, x: int):\n        bit.add(i, x-bit.get(i))\n\
    \    __setitem__ = set\n        \n    def add(bit, i: int, x: int) -> None:\n\
    \        assert 0 <= i <= bit.size\n        data, size = bit.data, bit.size\n\
    \        while i < size:\n            data[i], i = data[i]+x, i|(i+1)\n\n    def\
    \ presum(bit, n: int):\n        assert 0 <= n <= bit.size\n        s, z, i, data\
    \ = 0, n.bit_count(), n-1, bit.data\n        for _ in range(z):\n            s,\
    \ i = s+data[i], (i&(i+1))-1\n        return s\n    \n    def range_sum(bit, l:\
    \ int, r: int):\n        return bit.presum(r) - bit.presum(l)\n\n    def prelist(bit):\n\
    \        pre = [0]+bit.data\n        for i in range(bit.size+1):\n           \
    \ pre[i] += pre[i&(i-1)]\n        return pre\n    \n    def bisect_left(bit, v):\n\
    \        data, i, s, m = bit.data, 0, 0, 1 << ((N := bit.size).bit_length()-1)\n\
    \        while m:\n            if (ni := i|m) <= N and (ns := s + data[ni-1])\
    \ < v:\n                s, i = ns, ni\n            m >>= 1\n        return i\n\
    \    \n    def bisect_right(bit, v):\n        data, i, s, m = bit.data, 0, 0,\
    \ 1 << ((N := bit.size).bit_length()-1)\n        while m:\n            if (ni\
    \ := i|m) <= N and (ns := s + data[ni-1]) <= v:\n                s, i = ns, ni\n\
    \            m >>= 1\n        return i\n\ndef inversion_cnt(Z, N: Union[int,None]\
    \ = None):\n    if N is None:\n        # coordinate compression\n        Zsort\
    \ = sorted(set(Z))\n        Zcomp = { v: i for i, v in enumerate(Zsort) }\n  \
    \      Z = [Zcomp[z] for z in Z]\n        N = len(Z)\n\n    bit = BinaryIndexTree(N)\n\
    \    cnt = 0\n    for z in reversed(Z):\n        cnt += bit.presum(z)\n      \
    \  bit.add(z, 1)\n    return cnt\n"
  code: "import cp_library.math.__header__\nfrom typing import Union\nfrom cp_library.ds.bit_cls\
    \ import BinaryIndexTree\n\ndef inversion_cnt(Z, N: Union[int,None] = None):\n\
    \    if N is None:\n        # coordinate compression\n        Zsort = sorted(set(Z))\n\
    \        Zcomp = { v: i for i, v in enumerate(Zsort) }\n        Z = [Zcomp[z]\
    \ for z in Z]\n        N = len(Z)\n\n    bit = BinaryIndexTree(N)\n    cnt = 0\n\
    \    for z in reversed(Z):\n        cnt += bit.presum(z)\n        bit.add(z, 1)\n\
    \    return cnt"
  dependsOn:
  - cp_library/ds/bit_cls.py
  isVerificationFile: false
  path: cp_library/math/inversion_cnt_fn.py
  requiredBy: []
  timestamp: '2025-01-24 05:21:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
documentation_of: cp_library/math/inversion_cnt_fn.py
layout: document
redirect_from:
- /library/cp_library/math/inversion_cnt_fn.py
- /library/cp_library/math/inversion_cnt_fn.py.html
title: cp_library/math/inversion_cnt_fn.py
---
