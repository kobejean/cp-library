---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
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
    \nclass BinaryIndexRange:\n    def __init__(self, size: int):\n        self.size\
    \ = size\n        self.bit1 = BinaryIndexTree(size)\n        self.bit2 = BinaryIndexTree(size)\n\
    \n    def add(self, l, r, x) -> None:\n        \"\"\"Add x to all elements in\
    \ range [l, r)\"\"\"\n        self.bit1.add(l, x * l)\n        self.bit1.add(r,\
    \ -x * r)\n        self.bit2.add(l, x)\n        self.bit2.add(r, -x)\n\n    def\
    \ presum(self, i):\n        \"\"\"Get sum of elements in range [0, i)\"\"\"\n\
    \        return self.bit1.presum(i) - i * self.bit2.presum(i)\n\n    def range_sum(self,\
    \ l, r):\n        \"\"\"Get sum of elements in range [l, r)\"\"\"\n        return\
    \ self.presum(r) - self.presum(l)\n\n    def get(self, i):\n        \"\"\"Get\
    \ the value at index i\"\"\"\n        return self.range_sum(i, i+1)\n\n    def\
    \ set(self, i, x):\n        \"\"\"Set the value at index i to x\"\"\"\n      \
    \  self.add(i, i+1, x - self.get(i))\n        \nfrom typing import Union\n\nclass\
    \ BinaryIndexTree:\n    def __init__(bit, v: Union[int,list]):\n        if isinstance(v,\
    \ int):\n            bit.data, bit.size = [0]*v, v\n        else:\n          \
    \  bit.build(v)\n\n    def build(bit, data):\n        bit.data, bit.size = data,\
    \ len(data)\n        for i in range(bit.size):\n            if (r := i|(i+1))\
    \ < bit.size: \n                data[r] += data[i]\n\n    def get(bit, i: int):\n\
    \        assert 0 <= i < bit.size\n        s, z = (data := bit.data)[i], i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-data[i-1], i-(i&-i)\n\
    \        return s\n    __getitem__ = get\n    \n    def set(bit, i: int, x: int):\n\
    \        bit.add(i, x-bit.get(i))\n    __setitem__ = set\n        \n    def add(bit,\
    \ i: int, x: int) -> None:\n        assert 0 <= i <= bit.size\n        data, size\
    \ = bit.data, bit.size\n        while i < size:\n            data[i], i = data[i]+x,\
    \ i|(i+1)\n\n    def presum(bit, n: int):\n        assert 0 <= n <= bit.size\n\
    \        s, z, i, data = 0, n.bit_count(), n-1, bit.data\n        for _ in range(z):\n\
    \            s, i = s+data[i], (i&(i+1))-1\n        return s\n    \n    def range_sum(bit,\
    \ l: int, r: int):\n        return bit.presum(r) - bit.presum(l)\n\n    def prelist(bit):\n\
    \        pre = [0]+bit.data\n        for i in range(bit.size+1):\n           \
    \ pre[i] += pre[i&(i-1)]\n        return pre\n    \n    def bisect_left(bit, v):\n\
    \        return bit.bisect_right(v-1)+1\n    \n    def bisect_right(bit, v):\n\
    \        d, i, s, m, n = bit.data, 0, 0, bit.lead, bit.size\n        while m:\n\
    \            if (ni:=i|m) <= n and (ns:=s+d[ni-1]) <= v:\n                s, i\
    \ = ns, ni\n            m >>= 1\n        return i\n"
  code: "import cp_library.ds.__header__\n\nclass BinaryIndexRange:\n    def __init__(self,\
    \ size: int):\n        self.size = size\n        self.bit1 = BinaryIndexTree(size)\n\
    \        self.bit2 = BinaryIndexTree(size)\n\n    def add(self, l, r, x) -> None:\n\
    \        \"\"\"Add x to all elements in range [l, r)\"\"\"\n        self.bit1.add(l,\
    \ x * l)\n        self.bit1.add(r, -x * r)\n        self.bit2.add(l, x)\n    \
    \    self.bit2.add(r, -x)\n\n    def presum(self, i):\n        \"\"\"Get sum of\
    \ elements in range [0, i)\"\"\"\n        return self.bit1.presum(i) - i * self.bit2.presum(i)\n\
    \n    def range_sum(self, l, r):\n        \"\"\"Get sum of elements in range [l,\
    \ r)\"\"\"\n        return self.presum(r) - self.presum(l)\n\n    def get(self,\
    \ i):\n        \"\"\"Get the value at index i\"\"\"\n        return self.range_sum(i,\
    \ i+1)\n\n    def set(self, i, x):\n        \"\"\"Set the value at index i to\
    \ x\"\"\"\n        self.add(i, i+1, x - self.get(i))\n        \nfrom cp_library.ds.bit_cls\
    \ import BinaryIndexTree"
  dependsOn:
  - cp_library/ds/bit_cls.py
  isVerificationFile: false
  path: cp_library/ds/bir_cls.py
  requiredBy: []
  timestamp: '2025-02-09 13:23:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bir_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bir_cls.py
- /library/cp_library/ds/bir_cls.py.html
title: cp_library/ds/bir_cls.py
---
