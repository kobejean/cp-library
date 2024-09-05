---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "from typing import Any, List, Union\n\nclass BinaryIndexTree:\n  \
    \  def __init__(self, v: Union[int,List[Any]]):\n        if isinstance(v, int):\n\
    \            self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            r = i|(i+1)\n            if r\
    \ < self.size: \n                self.data[r] += self.data[i]\n\n    def add(self,\
    \ i: int, x: Any) -> None:\n        assert 0 <= i <= self.size\n        i += 1\n\
    \        while i <= self.size:\n            self.data[i-1], i = self.data[i-1]\
    \ + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n\
    \        s = 0\n        while i > 0:\n            s, i = s+self.data[i-1], i-(i&-i)\n\
    \        return s\n    \n    def range_sum(self, l: int, r: int) -> Any:\n   \
    \     assert 0 <= l <= r <= self.size\n        m = l&r if l.bit_length() == r.bit_length()\
    \ else 0\n        s = 0\n        while l > m:\n            s, l = s-self.data[l-1],\
    \ l-(l&-l)\n        while r > m:\n            s, r = s+self.data[r-1], r-(r&-r)\n\
    \        return s\n\nclass BinaryIndexRange:\n    def __init__(self, size: int):\n\
    \        self.size = size\n        self.bit1 = BinaryIndexTree(size)  # For storing\
    \ a[i] * i\n        self.bit2 = BinaryIndexTree(size)  # For storing a[i]\n\n\
    \    def add(self, l, r, x) -> None:\n        \"\"\"Add x to all elements in range\
    \ [l, r)\"\"\"\n        self.bit1.add(l, x * l)\n        self.bit1.add(r, -x *\
    \ r)\n        self.bit2.add(l, x)\n        self.bit2.add(r, -x)\n\n    def pref_sum(self,\
    \ i):\n        \"\"\"Get sum of elements in range [0, i)\"\"\"\n        return\
    \ self.bit1.pref_sum(i) - i * self.bit2.pref_sum(i)\n\n    def range_sum(self,\
    \ l, r):\n        \"\"\"Get sum of elements in range [l, r)\"\"\"\n        return\
    \ self.pref_sum(r) - self.pref_sum(l)\n\n    def get(self, i):\n        \"\"\"\
    Get the value at index i\"\"\"\n        return self.range_sum(i, i+1)\n\n    def\
    \ set(self, i, x):\n        \"\"\"Set the value at index i to x\"\"\"\n      \
    \  current_value = self.get(i)\n        self.add(i, i+1, x - current_value)\n"
  code: "from cp_library.ds.bit_cls import BinaryIndexTree\n\nclass BinaryIndexRange:\n\
    \    def __init__(self, size: int):\n        self.size = size\n        self.bit1\
    \ = BinaryIndexTree(size)  # For storing a[i] * i\n        self.bit2 = BinaryIndexTree(size)\
    \  # For storing a[i]\n\n    def add(self, l, r, x) -> None:\n        \"\"\"Add\
    \ x to all elements in range [l, r)\"\"\"\n        self.bit1.add(l, x * l)\n \
    \       self.bit1.add(r, -x * r)\n        self.bit2.add(l, x)\n        self.bit2.add(r,\
    \ -x)\n\n    def pref_sum(self, i):\n        \"\"\"Get sum of elements in range\
    \ [0, i)\"\"\"\n        return self.bit1.pref_sum(i) - i * self.bit2.pref_sum(i)\n\
    \n    def range_sum(self, l, r):\n        \"\"\"Get sum of elements in range [l,\
    \ r)\"\"\"\n        return self.pref_sum(r) - self.pref_sum(l)\n\n    def get(self,\
    \ i):\n        \"\"\"Get the value at index i\"\"\"\n        return self.range_sum(i,\
    \ i+1)\n\n    def set(self, i, x):\n        \"\"\"Set the value at index i to\
    \ x\"\"\"\n        current_value = self.get(i)\n        self.add(i, i+1, x - current_value)"
  dependsOn:
  - cp_library/ds/bit_cls.py
  isVerificationFile: false
  path: cp_library/ds/bir_cls.py
  requiredBy: []
  timestamp: '2024-09-05 11:18:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bir_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bir_cls.py
- /library/cp_library/ds/bir_cls.py.html
title: cp_library/ds/bir_cls.py
---
