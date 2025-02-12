---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit_cls.py
    title: cp_library/ds/tree/bit_cls.py
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
    from typing import Union\nfrom typing import Sequence\n\n\nclass BIT(Sequence[int]):\n\
    \    def __init__(bit, v):\n        if isinstance(v, int): bit.d, bit.n = [0]*v,\
    \ v\n        else: bit.build(v)\n\n    def build(bit, data):\n        bit.d, bit.n\
    \ = data, len(data)\n        for i in range(bit.n):\n            if (r := i|i+1)\
    \ < bit.n: bit.d[r] += bit.d[i]\n\n    def add(bit, i, x):\n        while i <\
    \ bit.n:\n            bit.d[i] += x\n            i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        assert 0 <= n <= bit.n\n        s = 0\n        while\
    \ n: s, n = s+bit.d[n-1], n&n-1\n        return s\n\n    def range_sum(bit, l,\
    \ r):\n        s = 0\n        while r: s, r = s+bit.d[r-1], r&r-1\n        while\
    \ l: s, l = s-bit.d[l-1], l&l-1\n        return s\n\n    def __len__(bit) -> int:\n\
    \        return bit.n\n    \n    def __getitem__(bit, i: int) -> int:\n      \
    \  s, l = bit.d[i], i&(i+1)\n        while l != i: s, i = s-bit.d[i-1], i-(i&-i)\n\
    \        return s\n    get = __getitem__\n    \n    def __setitem__(bit, i: int,\
    \ x: int) -> None:\n        bit.add(i, x-bit[i])\n    set = __setitem__\n\n  \
    \  def presum(bit) -> list[int]:\n        pre = [0]+bit.d\n        for i in range(bit.n+1):\
    \ pre[i] += pre[i&i-1]\n        return pre\n    \n    def bisect_left(bit, v)\
    \ -> int:\n        return bit.bisect_right(v-1)+1\n    \n    def bisect_right(bit,\
    \ v) -> int:\n        d, i, s, m, n = bit.d, 0, 0, 1 << (bit.n.bit_length()-1),\
    \ bit.n\n        while m:\n            if (ni:=i|m) <= n and (ns:=s+d[(i|m)-1])\
    \ <= v: s, i = ns, ni\n            m >>= 1\n        return i\n\ndef inversion_cnt(Z,\
    \ N: Union[int,None] = None):\n    if N is None:\n        Zi = { z: i for i, z\
    \ in enumerate(sorted(set(Z))) }\n        Z, N = [Zi[z] for z in Z], len(Z)\n\
    \    bit, cnt = BIT(N), 0\n    for z in reversed(Z):\n        cnt += bit.sum(z)\n\
    \        bit.add(z, 1)\n    return cnt\n"
  code: "import cp_library.math.__header__\nfrom typing import Union\nfrom cp_library.ds.tree.bit_cls\
    \ import BIT\n\ndef inversion_cnt(Z, N: Union[int,None] = None):\n    if N is\
    \ None:\n        Zi = { z: i for i, z in enumerate(sorted(set(Z))) }\n       \
    \ Z, N = [Zi[z] for z in Z], len(Z)\n    bit, cnt = BIT(N), 0\n    for z in reversed(Z):\n\
    \        cnt += bit.sum(z)\n        bit.add(z, 1)\n    return cnt"
  dependsOn:
  - cp_library/ds/tree/bit_cls.py
  isVerificationFile: false
  path: cp_library/math/inversion_cnt_fn.py
  requiredBy: []
  timestamp: '2025-02-12 22:25:56+09:00'
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
