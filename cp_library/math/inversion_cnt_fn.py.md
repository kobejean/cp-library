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
    from typing import Union\n\n\nclass BinaryIndexTree:\n    def __init__(self, v:\
    \ Union[int,list]):\n        if isinstance(v, int):\n            self.data, self.size\
    \ = [0]*v, v\n        else:\n            self.build(v)\n\n    def build(self,\
    \ data):\n        self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            if (r := i|(i+1)) < self.size: \n                data[r] += data[i]\n\
    \n    def get(self, i: int):\n        assert 0 <= i < self.size\n        s, z\
    \ = (data := self.data)[i], i&(i+1)\n        for _ in range((i^z).bit_count()):\n\
    \            s, i = s-data[i-1], i-(i&-i)\n        return s\n    \n    def set(self,\
    \ i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n    def add(self,\
    \ i: int, x: int) -> None:\n        assert 0 <= i <= self.size\n        i += 1\n\
    \        data, size = self.data, self.size\n        while i <= size:\n       \
    \     data[i-1], i = data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n\
    \        assert 0 <= i <= self.size\n        s = 0\n        data = self.data\n\
    \        for _ in range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n\
    \        return s\n    \n    def range_sum(self, l: int, r: int):\n        return\
    \ self.pref_sum(r) - self.pref_sum(l)\n\ndef inversion_cnt(Z, N: Union[int,None]\
    \ = None):\n    if N is None:\n        # coordinate compression\n        Zsort\
    \ = sorted(set(Z))\n        Zcomp = { v: i for i, v in enumerate(Zsort) }\n  \
    \      Z = [Zcomp[z] for z in Z]\n        N = len(Z)\n\n    bit = BinaryIndexTree(N)\n\
    \    cnt = 0\n    for z in reversed(Z):\n        cnt += bit.pref_sum(z)\n    \
    \    bit.add(z, 1)\n    return cnt\n"
  code: "import cp_library.math.__header__\nfrom typing import Union\nfrom cp_library.ds.bit_cls\
    \ import BinaryIndexTree\n\ndef inversion_cnt(Z, N: Union[int,None] = None):\n\
    \    if N is None:\n        # coordinate compression\n        Zsort = sorted(set(Z))\n\
    \        Zcomp = { v: i for i, v in enumerate(Zsort) }\n        Z = [Zcomp[z]\
    \ for z in Z]\n        N = len(Z)\n\n    bit = BinaryIndexTree(N)\n    cnt = 0\n\
    \    for z in reversed(Z):\n        cnt += bit.pref_sum(z)\n        bit.add(z,\
    \ 1)\n    return cnt"
  dependsOn:
  - cp_library/ds/bit_cls.py
  isVerificationFile: false
  path: cp_library/math/inversion_cnt_fn.py
  requiredBy: []
  timestamp: '2024-12-30 17:25:46+09:00'
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
